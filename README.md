# Repo Final Living Bio-Network
### โปรเจกต์นี้จำลองระบบโครงสร้างพื้นฐานที่ใช้สัญญาณเคมีและ DNA เป็นหลัก โดยมีระบบจัดการเส้นทาง (Routing) ที่สามารถวิวัฒนาการตัวเองได้ (เกิดใหม่หรือถูกตัดทิ้ง) และมีระบบรักษาความปลอดภัยแบบ Genetic Encryption
---
## 1. main.py (ศูนย์กลางการควบคุม)
#### 
* เป็นจุดรันโปรแกรมหลัก (Terminal Interface)

* ทำหน้าที่เชื่อมโยงทุกส่วนเข้าด้วยกัน: รับสัญญาณเคมี -> แปลงเป็นดิจิทัล -> เข้ารหัสด้วย DNA -> ตรวจสอบสิทธิ์ผู้ใช้

* มีการจำลองวงจรชีวิตของเครือข่าย (Evolution Loop) ในทุกรอบที่ผู้ใช้งานโต้ตอบ
## 2. bio_infrastructure.py (โครงสร้างพื้นฐานชีวภาพ)
####
* BioInfrastructure: กำหนดสารอาหารพื้นฐาน (Substrate) และฟังก์ชันแปลงสัญญาณ

* convert_chemical_to_digital: ทำหน้าที่เป็น Sensor แปลงค่าสัญญาณเคมี (Analog) ให้กลายเป็น Bit (0 หรือ 1)
## 3. evolution_engine.py (กลไกวิวัฒนาการ)
####
* NetworkState & Route: จัดการสถานะเครือข่ายและพลังงาน (Energy Pool)

* evolve_network: ระบบคัดเลือกตามธรรมชาติ เส้นทางไหนประสิทธิภาพต่ำ (< 0.5) หรือพลังงานหมดจะถูก "Pruning" (ตัดทิ้ง)

* spawn_new_path: หากพลังงานเพียงพอ ระบบจะสุ่มสร้างเส้นทางใหม่ (Mycelium) ขึ้นมาเอง
## 4. security.py / bio_infrastructure.py (ระบบความปลอดภัย)
####
* BiologicalEncryption: จำลองการเข้ารหัสข้อมูลโดยใช้ "Genetic Key" หรือลำดับ DNA

* validate_genetic_key: ตรวจสอบความถูกต้องของรหัส หากรหัสไม่ตรงจะแจ้งว่าเกิดการกลายพันธุ์ (Mutation Detected) และล็อกระบบทันที
## 5. ExistencePacket.ts (โครงสร้างข้อมูล)
####
* ไฟล์ TypeScript ที่กำหนด Interface ของชุดข้อมูล (Packet) ประกอบด้วย ID สิ่งมีชีวิต, สัญญาณเคมี, ลำดับ DNA และ Timestamp เพื่อให้การส่งต่อข้อมูลมีโครงสร้างที่ชัดเจน

---
## Workflow การทำงาน
####
1. Analyze: ระบบเช็กเส้นทางที่ดีที่สุดและแสดงสถานะพลังงาน

2. Sense: รับสัญญาณเคมีแล้วแปลงเป็น Digital Bit

3. Encrypt: นำข้อมูลไปใส่แพ็กเกจ DNA เข้ารหัสด้วย Key GATTACA_2026

4. Interact: รอผู้ใช้กรอกรหัส DNA เพื่อถอดรหัส

5. Evolve: ระบบคำนวณการใช้พลังงาน ตัดเส้นทางที่แย่ และสร้างเส้นทางใหม่



# โค้ดตัวอย่าง main.py

```python
import random
from bio_infrastructure import BioInfrastructure
from evolution_engine import evolve_network, NetworkState
from security import BiologicalEncryption

def run_terminal():
    print("=== BIO-DIGITAL INTERACTIVE TERMINAL ===")
    bio_infra = BioInfrastructure()
    net_state = NetworkState()
    MASTER_DNA = "GATTACA_2026"
    
    while True:
        print("\n" + "-"*40)
        # 1. แนะนำเส้นทางที่ดีที่สุด
        best = net_state.get_best_route()
        if best:
            print(f"[*] RECOMMENDED ROUTE: {best.id} (Efficiency: {best.efficiency:.2f})")
        else:
            print("[!] SYSTEM DEAD: No active routes!")
            break

        # 2. จำลองรับข้อมูล
        bit = bio_infra.convert_chemical_to_digital(random.random())
        packet = BiologicalEncryption.encrypt(f"Signal_Bit_{bit}", MASTER_DNA)
        
        # 3. User Input
        user_key = input("Enter DNA Access Key to decode (or 'exit'): ")
        if user_key.lower() == 'exit': break
        
        # 4. ตรวจสอบความปลอดภัย
        print(f"\nResult: {BiologicalEncryption.decrypt(packet, user_key)}")

        # 5. วิวัฒนาการโครงข่าย
        evolve_network(net_state)
        if random.random() > 0.6: net_state.spawn_new_path()

if __name__ == "__main__":
    run_terminal()
```
