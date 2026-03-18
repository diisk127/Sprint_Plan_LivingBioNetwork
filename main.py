interface ExistencePacket {
    entityId: string;       // รหัสประจำตัวสิ่งมีชีวิต
    chemicalSignal: string; // สัญญาณสารเคมี
    dnaSequence: string;    // ชุดข้อมูล DNA สำหรับความจุสูง
    timestamp: number;      // Unix epoch time
}
