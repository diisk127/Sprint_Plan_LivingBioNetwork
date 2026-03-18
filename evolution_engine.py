class BioInfrastructure:
    def __init__(self):
        self.substrate = "Organic Nutrient Mix"

    def convert_chemical_to_digital(self, chemical_signal):
        # จำลองการแปลงสัญญาณจากสารเคมีเป็น Digital Bit
        return 1 if chemical_signal >= 0.5 else 0
class BiologicalEncryption:
    @staticmethod
    def encrypt(data, genetic_key):
        return f"DNA::{genetic_key}::[{data}]"

    @staticmethod
    def validate_genetic_key(provided_key, expected_key):
        # ตรวจสอบความถูกต้องของ DNA
        is_match = provided_key == expected_key
        status = "MATCH FOUND" if is_match else "MUTATION DETECTED / MISMATCH"
        print(f"  [Security Check] {provided_key} vs {expected_key} -> {status}")
        return is_match

    @staticmethod
    def decrypt(packet_string, receiver_key):
        try:
            parts = packet_string.split("::")
            if len(parts) < 3: return "Error: Invalid Packet Structure"
            
            extracted_key = parts[1]
            data = parts[2]
            
            if BiologicalEncryption.validate_genetic_key(extracted_key, receiver_key):
                return f"Access Granted: {data}"
            else:
                return "Access Denied: Security protocol triggered!"
        except Exception as e:
            return f"Error: {str(e)}"
