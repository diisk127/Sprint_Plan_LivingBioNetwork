from flask import Flask, render_template, request, redirect, url_for
import random

from bio_infrastructure import BioInfrastructure
from evolution_engine import NetworkState, evolve_network
from security import BiologicalEncryption


app = Flask(__name__, template_folder=".")

# ใช้ state เดียวกันในทุก request (จำลองระบบที่รันต่อเนื่อง)
bio_infra = BioInfrastructure()
net_state = NetworkState()
MASTER_DNA = "GATTACA_2026"


def snapshot_state():
    """
    สร้าง context ปัจจุบัน โดยไม่รันรอบวิวัฒนาการใหม่
    ใช้เวลาที่ผู้ใช้ยังไม่ได้ใส่คีย์ หรือใส่คีย์ไม่ครบ
    """
    best = net_state.get_best_route()
    routes_view = [
        {
            "id": r.id,
            "efficiency": r.efficiency,
            "maintenance_cost": r.maintenance_cost,
        }
        for r in net_state.routes
    ]

    if best is None:
        return {
            "system_dead": True,
            "message": "SYSTEM DEAD: No active routes!",
            "recommended_route": None,
            "chemical_value": 0.0,
            "bit": 0,
            "raw_signal": "",
            "packet": "",
            "access_result": None,
            "security_log": None,
            "energy_pool": net_state.energy_pool,
            "routes": routes_view,
        }

    # ไม่มีการสุ่มสัญญาณ/วิวัฒนาการใหม่ แค่สะท้อนสถานะคร่าว ๆ
    return {
        "system_dead": False,
        "recommended_route": best,
        "chemical_value": 0.0,
        "bit": 0,
        "raw_signal": "",
        "packet": "",
        "access_result": None,
        "security_log": None,
        "energy_pool": net_state.energy_pool,
        "routes": routes_view,
    }


def run_single_cycle(user_key: str | None):
    """
    รันหนึ่งรอบของ workflow ตาม README:
    1) Analyze  2) Sense  3) Encrypt  4) Interact  5) Evolve
    แล้วคืนค่าข้อมูลทั้งหมดไปแสดงในหน้าเว็บ
    """
    # 1. Analyze – หาเส้นทางที่ดีที่สุด
    best = net_state.get_best_route()
    if best is None:
        # ถึงระบบจะตายแล้ว ก็ยังส่ง energy_pool และ routes ไปให้ template ใช้งานได้
        routes_view = [
            {
                "id": r.id,
                "efficiency": r.efficiency,
                "maintenance_cost": r.maintenance_cost,
            }
            for r in net_state.routes
        ]
        return {
            "system_dead": True,
            "message": "SYSTEM DEAD: No active routes!",
            "recommended_route": None,
            "chemical_value": 0.0,
            "bit": 0,
            "raw_signal": "",
            "packet": "",
            "access_result": None,
            "security_log": None,
            "energy_pool": net_state.energy_pool,
            "routes": routes_view,
        }

    # 2. Sense – จำลองรับสัญญาณเคมีแล้วแปลงเป็น Bit
    chemical_value = random.random()
    bit = bio_infra.convert_chemical_to_digital(chemical_value)
    raw_signal = f"Signal_Bit_{bit}"

    # 3. Encrypt – เข้ารหัสข้อมูลด้วย DNA key
    packet = BiologicalEncryption.encrypt(raw_signal, MASTER_DNA)

    # 4. Interact – ตรวจสอบ access key ที่ผู้ใช้ใส่
    access_result = None
    security_log = None
    if user_key is not None and user_key != "":
        # decrypt() จะ print log ความปลอดภัยออกมาที่ stdout อยู่แล้ว
        access_result = BiologicalEncryption.decrypt(packet, user_key)
        security_log = "Security check executed. See server console for detail."

    # 5. Evolve – วิวัฒนาการโครงข่าย
    evolve_network(net_state)
    if random.random() > 0.6:
        net_state.spawn_new_path()

    # เตรียมข้อมูลสรุปของเครือข่าย
    routes_view = [
        {
            "id": r.id,
            "efficiency": r.efficiency,
            "maintenance_cost": r.maintenance_cost,
        }
        for r in net_state.routes
    ]

    return {
        "system_dead": False,
        "recommended_route": best,
        "chemical_value": chemical_value,
        "bit": bit,
        "raw_signal": raw_signal,
        "packet": packet,
        "access_result": access_result,
        "security_log": security_log,
        "energy_pool": net_state.energy_pool,
        "routes": routes_view,
    }


@app.route("/", methods=["GET", "POST"])
def index():
    user_key = None
    if request.method == "POST":
        # อ่าน DNA key จากฟอร์ม
        user_key = request.form.get("dna_key", "").strip()
        # ถ้าไม่ได้ใส่ key ให้เตือนและไม่รันรอบใหม่
        if not user_key:
            context = snapshot_state()
            context["user_key"] = ""
            context["error_message"] = "กรุณาใส่ DNA Access Key ก่อนดำเนินการ"
            return render_template("index.html", **context)
        # ป้องกันการ reload จากการ refresh ด้วย PRG pattern
        return redirect(url_for("result", dna_key=user_key))

    # initial load – ยังไม่กรอก key ก็ยังให้เห็นสถานะระบบ
    context = snapshot_state()
    context["user_key"] = ""
    return render_template("index.html", **context)


@app.route("/result")
def result():
    user_key = request.args.get("dna_key", "").strip()
    context = run_single_cycle(user_key=user_key if user_key else None)
    context["user_key"] = user_key
    return render_template("index.html", **context)


@app.route("/reset")
def reset():
    """
    รีเซ็ตสถานะเครือข่ายทั้งหมดให้กลับไปจุดเริ่มต้น
    แล้วพากลับไปหน้าแรก
    """
    global net_state
    net_state = NetworkState()
    return redirect(url_for("index"))


if __name__ == "__main__":
    # ตัวอย่างการรัน:  python web_app.py
    # แล้วเปิดเบราว์เซอร์ไปที่ http://127.0.0.1:5000
    app.run(debug=True)

