class BiologicalEncryption:
    @staticmethod
    def encrypt(data, genetic_key):
        return f"DNA::{genetic_key}::[{data}]"

    @staticmethod
    def validate_genetic_key(provided_key, expected_key):
        is_match = provided_key == expected_key
        if is_match:
            print(f"  [Security] {provided_key} -> MATCH FOUND (Accessing Nucleus...)")
        else:
            print(f"  [Security] {provided_key} -> MUTATION DETECTED (Key Does Not Match.)")
        return is_match

    @staticmethod
    def decrypt(packet_string, receiver_key):
        try:
            parts = packet_string.split("::")
            if len(parts) < 3: return "Invalid Packet"
            extracted_key, data = parts[1], parts[2]
            
            if BiologicalEncryption.validate_genetic_key(extracted_key, receiver_key):
                return f"SUCCESS: {data}"
            else:
                # แสดงข้อความ MUTATION DETECTED ให้เห็นชัดบนหน้าเว็บ
                return "MUTATION DETECTED: FAILED · Bio-Security Lockdown"
        except Exception as e:
            return f"Error: {str(e)}"
