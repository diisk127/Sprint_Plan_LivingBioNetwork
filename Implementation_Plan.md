# Living-Bio-Network
## Implementation Plan v1.0

**Version:** 1.0
**Sprint:** Alpha
**Methodology:** Agile Scrum
**Author:** นางสาวกวินธิดา อนุนิวัฒน์

---

## 1. ทีมและบทบาท

| ชื่อ | รหัสนักศึกษา | บทบาท | หน้าที่หลักใน Implementation |
|:---|:---:|:---|:---|
| นางสาวกวินธิดา อนุนิวัฒน์ | 673380390-5 | Product Owner | กำหนด Scope, อนุมัติ Backlog, ตรวจสอบคุณภาพงาน |
| นายภควัฒน์ สุขมณี | 673380418-9 | System Architect | ออกแบบโครงสร้างทุก Layer, ตรวจสอบโค้ดให้ตรง Spec |
| นางสาวกัญญาวีร์ สิงห์ลี | 673380573-7 | QA | เขียน Test Case, ทดสอบระบบ, ติดตาม Bug |
| นายณัฏฐชัย ผลดี | 673380581-8 | Backend Engineer | เขียนโค้ดทุกส่วน, พัฒนา Simulation |
| นายธนนันต์ สาวิกัน | 673380586-8 | Scrum Master | ดูแลกระบวนการ Scrum, ประสานงาน, จัดการเอกสาร |

---

## 2. วิเคราะห์งาน (Implementation Analysis)

### 2.1 ประเมินความซับซ้อนของแต่ละ Component

| Component | Layer | ความยาก (1-5) | ความเสี่ยง | เวลาที่ประเมิน |
|:---|:---|:---:|:---|:---|
| BioNode Runtime | Infrastructure | 3 | ต่ำ | 8–10 ชม. |
| BioNetworkState | Infrastructure | 3 | ต่ำ | 6–8 ชม. |
| Adaptive Bio Routing | Evolution Engine | 5 | สูง | 20–25 ชม. |
| Existence Communication | Communication Layer | 4 | ปานกลาง | 12–15 ชม. |
| Biological Encryption | Structural Privacy | 4 | ปานกลาง | 10–12 ชม. |
| Bio Logging | Infrastructure | 2 | ต่ำ | 4–6 ชม. |
| Unit Test Suite | QA | 3 | ปานกลาง | 8–10 ชม. |
| Documentation | ทุก Layer | 2 | ต่ำ | ต่อเนื่อง |

**รวมเวลาที่ประเมิน:** 68–86 ชั่วโมง
**เวลาที่ทีมมี:** 5 Sprint × 5 คน × 6 ชั่วโมง = 150 ชั่วโมง
**เวลาสำรอง:** 64–82 ชั่วโมง

### 2.2 ลำดับการพัฒนา (Critical Path)

งานที่ต้องทำตามลำดับ:
```
BioNode → BioNetworkState → Adaptive Routing → Communication Layer → Privacy Engine
```

งานที่ทำพร้อมกันได้:
- Bio Logging ทำควบคู่กับ BioNode ได้
- Unit Test เขียนควบคู่กับทุก Component
- Documentation เขียนต่อเนื่องตลอด

### 2.3 ความเสี่ยงและแผนรับมือ

| ความเสี่ยง | ผลกระทบ | แผนรับมือ |
|:---|:---|:---|
| Signal broadcast วนลูปไม่รู้จบ | สูง | เพิ่ม visited tracking ใน BioNode |
| Routing คำนวณ Density ผิดพลาด | ปานกลาง | เขียน Unit Test ครอบคลุมทุก Case |
| Simulation ช้าเมื่อ Node มากกว่า 100 | ปานกลาง | จำกัด Scaling ใน Sprint Alpha ก่อน |
| Integration ระหว่าง Layer ล้มเหลว | สูง | ทดสอบทีละ Layer ก่อนรวม |
| สมาชิกขาดระหว่าง Sprint | ปานกลาง | กระจายงาน, ทำ Knowledge Transfer |

---

## 3. ทบทวนสถาปัตยกรรม (Architectural Review)

### 3.1 สรุปผลการทบทวนแต่ละ Layer

| Layer | สถานะ | ข้อสังเกต |
|:---|:---:|:---|
| Infrastructure Layer |  ผ่าน | BioNode และ Sensor ออกแบบชัดเจน |
| Evolution Engine |  ผ่านมีเงื่อนไข | ต้องกำหนดค่า THRESHOLD และ OPTIMAL_LEVEL |
| Existence Communication Layer |  ผ่าน | ExistencePacket Schema ครบถ้วน |
| Structural Privacy Layer |  ผ่าน | Genetic Key Encryption ออกแบบดี |
| Human Awareness Layer |  ผ่านมีเงื่อนไข | Biometric Interface ต้องระบุให้ชัดเจนขึ้น |

### 3.2 สิ่งที่ต้องแก้ไขก่อนเริ่ม Sprint Beta

1. กำหนดค่า THRESHOLD สำหรับ Route Efficiency ให้ชัดเจน
2. กำหนดค่า OPTIMAL_LEVEL สำหรับ Traffic Density
3. ออกแบบ Biometric Interface ให้ละเอียดขึ้น

### 3.3 การตัดสินใจสำคัญ

**การตัดสินใจที่ 1: ภาษาที่ใช้พัฒนา**
ใช้ Python เพราะทีมคุ้นเคย พัฒนาได้เร็ว รองรับ Graph และ Simulation ได้ดี —  ตกลงแล้ว

**การตัดสินใจที่ 2: โครงสร้างข้อมูล BioNode**
ใช้ Dictionary สำหรับ connected_nodes เพื่อให้ค้นหาได้เร็วกว่า List —  ตกลงแล้ว

**การตัดสินใจที่ 3: วิธี Routing**
ใช้ Greedy Algorithm เลือก Fiber ที่ Density สูงสุดใน Sprint Alpha ก่อน แล้วค่อยพัฒนาเป็น Dijkstra ใน Sprint Beta —  ตกลงแล้ว

**การตัดสินใจที่ 4: Encryption**
ใช้ Genetic Key แบบ String Matching ใน Sprint Alpha เพื่อให้ง่ายก่อน แล้วค่อยเพิ่มความซับซ้อนใน Sprint Delta —  ตกลงแล้ว

---

## 4. แผนงานรายสัปดาห์ (Sprint Roadmap)

### Sprint Alpha — BioNode Simulation Foundation (2 สัปดาห์)

**เป้าหมาย:** BioNode เชื่อมต่อกันและส่ง BioSignal ผ่าน Adaptive Basic Routing ได้

**งานที่ต้องทำ:**

| งาน | ผู้รับผิดชอบ | กำหนดเสร็จ | เกณฑ์ผ่าน |
|:---|:---|:---:|:---|
| BA-01: BioNode Runtime | ณัฏฐชัย | Day 3 | grow, transmit, receive ทำงานได้ |
| BA-02: BioNetworkState | ณัฏฐชัย | Day 4 | เพิ่ม Node และ Fiber ได้ |
| BA-03: Adaptive Routing | ณัฏฐชัย + ภควัฒน์ | Day 7 | เลือก Fiber density สูงสุดได้ |
| BA-04: Bio Logging | ณัฏฐชัย | Day 5 | Log แสดงสถานะได้ ไม่กระทบ Sim |
| BA-05: Unit Test Setup | กัญญาวีร์ | Day 8 | Coverage ≥ 60% |

**เกณฑ์ที่ต้องผ่านก่อนปิด Sprint Alpha:**
- BioNode ส่ง BioSignal End-to-end ได้
- ไม่มี infinite loop
- Unit Test Coverage ≥ 60%
- ไม่มี Critical Bug
- เอกสารอัปเดตแล้ว

---

### Sprint Beta — Evolution Engine (2 สัปดาห์)

**เป้าหมาย:** เครือข่ายเติบโตและปรับโครงสร้างอัตโนมัติได้

**งานที่ต้องทำ:**

| งาน | ผู้รับผิดชอบ | เกณฑ์ผ่าน |
|:---|:---|:---|
| Fiber Density Decay | ณัฏฐชัย | Density ลดลงเมื่อไม่ใช้งาน |
| Traffic-Based Reinforcement | ณัฏฐชัย | Density เพิ่มเมื่อใช้งานหนาแน่น |
| Auto Growth Algorithm | ณัฏฐชัย + ภควัฒน์ | สร้างเส้นทางใหม่อัตโนมัติได้ |
| Topology Evolution Simulation | ณัฏฐชัย | เห็น Before/After ชัดเจน |
| Efficiency Metrics | กัญญาวีร์ | วัดค่า Throughput/Latency ได้ |

---

### Sprint Gamma — BioSignal Communication Layer (2 สัปดาห์)

**เป้าหมาย:** ส่ง BioPacket แบบมีโปรโตคอลและความปลอดภัยเบื้องต้น

**งานที่ต้องทำ:**

| งาน | ผู้รับผิดชอบ | เกณฑ์ผ่าน |
|:---|:---|:---|
| BioPacket Schema | ภควัฒน์ | Schema ครบทุก Field |
| Encoding/Decoding Logic | ณัฏฐชัย | Encode แล้ว Decode กลับได้ถูกต้อง |
| Transmission Handler | ณัฏฐชัย | ส่ง Packet End-to-end ได้ |
| Integrity Validation | กัญญาวีร์ | ตรวจจับ Corrupt Packet ได้ |

---

### Sprint Delta — Structural Privacy Engine (2 สัปดาห์)

**เป้าหมาย:** ระบบ Encryption ด้วย Genetic Key ทำงานได้จริง

**งานที่ต้องทำ:**

| งาน | ผู้รับผิดชอบ | เกณฑ์ผ่าน |
|:---|:---|:---|
| Genetic Key Schema | ภควัฒน์ | Key Format กำหนดชัดเจน |
| Identity-Bound Decoding | ณัฏฐชัย | Node ที่ Key ไม่ตรงเข้าไม่ได้ |
| Selective Visibility Routing | ณัฏฐชัย | ส่งได้เฉพาะ Node ที่มีสิทธิ์ |
| Security Simulation | กัญญาวีร์ | ทดสอบ Attack Scenario ผ่าน |

---

### Sprint Epsilon — Environmental Adaptation Layer (2 สัปดาห์)

**เป้าหมาย:** เครือข่ายตอบสนองต่อสภาพแวดล้อมได้

**งานที่ต้องทำ:**

| งาน | ผู้รับผิดชอบ | เกณฑ์ผ่าน |
|:---|:---|:---|
| Temperature Simulation | ณัฏฐชัย | Routing เปลี่ยนตามอุณหภูมิ |
| Moisture Impact Modeling | ณัฏฐชัย | สัญญาณอ่อนลงเมื่อความชื้นสูง |
| Stress-Based Topology Adjustment | ณัฏฐชัย + ภควัฒน์ | โครงสร้างปรับเมื่อระบบ Stress |
| Adaptive Throttling Logic | ณัฏฐชัย | จำกัด Traffic อัตโนมัติได้ |

---

## 5. หน้าที่รายบุคคลในการพัฒนา

### นางสาวกวินธิดา อนุนิวัฒน์ (Product Owner)
- กำหนดและอัปเดต Product Backlog ทุก Sprint
- อนุมัติ Scope และตัดสินใจเรื่องลำดับความสำคัญ
- ตรวจสอบว่า Deliverable ตรงกับสิ่งที่ต้องการ
- เข้าร่วม Sprint Review และให้ Feedback

### นายภควัฒน์ สุขมณี (System Architect)
- ออกแบบโครงสร้างทุก Layer ก่อนเริ่มเขียนโค้ด
- เขียน Interface Contract ระหว่าง Layer
- ตรวจสอบโค้ดของ ณัฏฐชัย ให้ตรงกับ Architecture
- บันทึก Architecture Decision ทุกครั้งที่มีการเปลี่ยนแปลง

### นางสาวกัญญาวีร์ สิงห์ลี (QA)
- เขียน Test Plan ก่อนเริ่มพัฒนาแต่ละ Sprint
- เขียน Test Case ครอบคลุมทุก Component
- รัน Test และรายงานผลทุกวัน
- ติดตาม Bug และตรวจสอบว่าแก้แล้วจริง

### นายณัฏฐชัย ผลดี (Backend Engineer)
- เขียนโค้ดทุก Component ตาม Architecture ที่ภควัฒน์ออกแบบ
- เขียน Unit Test ควบคู่กับโค้ด
- แก้บักตาม Report ของ กัญญาวีร์
- เตรียม Demo Script ทุก Sprint

### นายธนนันต์ สาวิกัน (Scrum Master)
- ดูแลการประชุม Daily Bio-Pulse ทุกวัน
- จัดการ Blocker ที่ทีมติดขัด
- อัปเดตเอกสารและ GitHub ให้เป็นปัจจุบัน
- ดำเนิน Sprint Review และ Retrospective

---

## 6. เกณฑ์ความสำเร็จรวมของโปรเจค (Definition of Done)

Sprint จะถือว่าเสร็จสมบูรณ์เมื่อ:

- Feature ทำงานใน Simulation ได้จริง
- Unit Test Coverage ≥ 80% (ยกเว้น Sprint Alpha ที่ใช้ 60%)
- ไม่มี Critical Bug
- เอกสารอัปเดตแล้ว
- Demo ผ่านการตรวจสอบของ Product Owner

---

## 7. แผนรับมือเมื่อเกิดปัญหา

**ถ้าทำงานช้ากว่ากำหนด**
ตัด Nice-to-have ออกก่อน เพิ่ม Pair Programming ระหว่าง ณัฏฐชัย และ ภควัฒน์

**ถ้า Integration ล้มเหลว**
ย้อนกลับ Commit ก่อนหน้า ทดสอบทีละ Layer ใหม่ตั้งแต่ต้น

**ถ้าสมาชิกขาดเกิน 2 วัน**
กวินธิดา รับงาน PO + QA Support, ภควัฒน์ รับงาน Architect + Code Review เพิ่ม, ธนนันต์ รับงาน SM + Documentation

**ถ้า Routing ช้าเกินไป**
จำกัด Node ไว้ที่ 50 ตัวก่อน แล้วค่อย Optimize ใน Sprint Beta

---

## 8. ลายเซ็นอนุมัติ

| ชื่อ | บทบาท | ลายเซ็น | วันที่ |
|:---|:---|:---:|:---:|
| นางสาวกวินธิดา อนุนิวัฒน์ | Product Owner | | |
| นายภควัฒน์ สุขมณี | System Architect | | |
| นางสาวกัญญาวีร์ สิงห์ลี | QA | | |
| นายณัฏฐชัย ผลดี | Backend Engineer | | |
| นายธนนันต์ สาวิกัน | Scrum Master | | |

---

*Living-Bio-Network Implementation Plan v1.0 — CP352005 Networks*
