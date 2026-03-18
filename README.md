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
