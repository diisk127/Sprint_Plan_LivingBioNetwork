# Living Bio Network
## Role and Responsibility Document
####
Version : 1.0 

Sprint : Alpha 

Methodology : Agile Scrum 

## 1. Team Members
| No. | Name | Student ID |
|:---:|:---|:---:|
| 1 | นางสาวกวินธิดา อนุนิวัฒน์ | 673380390-5 |
| 2 | นายภควัฒน์ สุขมณี | 673380418-9 |
| 3 | นางสาวกัญญาวีร์ สิงห์ลี | 673380573-7 |
| 4 | นายณัฏฐชัย ผลดี | 673380581-8 |
| 5 | นายธนนันต์ สาวิกัน | 673380586-8 |

---

## 2. Role Assignment Matrix
| Role | Assigned To | Primary Responsibilities | Secondary Responsibilities | Decision Authority |
|:---|:---|:---|:---|:---|
| **Product Owner** | นางสาวกวินธิดา อนุนิวัฒน์ | กำหนดทิศทางโปรเจกต์และลำดับความสำคัญของ Backlog | ตรวจสอบคุณภาพงานในแต่ละ Sprint | อนุมัติ Scope งานทั้งหมด |
| **System Architect** | นายภควัฒน์ สุขมณี |ออกแบบโครงสร้างทั้งระบบ (Layer Architecture) | ตรวจสอบความสอดคล้องของเอกสารเทคนิค | อนุมัติการเปลี่ยนแปลงสถาปัตยกรรม |
| **Quality Assurance (QA)** | นางสาวกัญญาวีร์ สิงห์ลี | ตรวจสอบความถูกต้องของระบบและทดสอบหาข้อผิดพลาด (Bug Testing) | จัดทำคู่มือการใช้งานและรายงานผลการทดสอบ | เกณฑ์การปล่อยผ่านระบบ (Release Criteria) |
| **Backend Engineer** | นายณัฏฐชัย ผลดี | พัฒนา Node Simulation, Routing Logic และ Packet Handling | ปรับปรุง Performance ของระบบเครือข่าย | การตัดสินใจระดับ Implementation โค้ด |
| **Scrum Master** | นายธนนันต์ สาวิกัน | ดูแลกระบวนการทำงานแบบ Scrum และขจัดอุปสรรคในทีม | ประสานงานระหว่างสมาชิกภายในทีม | กระบวนการทำงาน (Process) |

---

## 3. Responsibility Breakdown by Layer
### 3.1 Human Awareness & Reality Integration Layer
#### 

ผู้รับผิดชอบหลัก: Product Owner และ System Architect

หน้าที่:

* ออกแบบการแสดงผล (Eco-Feedback) เพื่อให้มนุษย์เข้าใจสถานะของเครือข่ายชีวภาพผ่านประสาทสัมผัส

* พัฒนารูปแบบการโต้ตอบ (Biometric Interface) เช่น การใช้ความร้อนหรือความชื้นจากร่างกายเพื่อป้อนข้อมูลเข้าสู่ระบบ

*  ตรวจสอบความถูกต้องของการนำข้อมูลจากโลกแห่งความเป็นจริงเข้าสู่โครงสร้างเครือข่าย

### 3.2 Existence Communication Layer

ผู้รับผิดชอบหลัก: System Architect และ Backend Engineer

หน้าที่:

* กำหนดโปรโตคอลการจัดเก็บข้อมูลในรูปแบบ DNA Sequence และการส่งสัญญาณผ่านสารเคมี

* ออกแบบโครงสร้างข้อมูล ExistencePacket เพื่อให้ Node ต่างๆ สามารถสื่อสารรหัสพันธุกรรมกันได้อย่างแม่นยำ

* จัดการระบบการเข้ารหัสชีวภาพ (Biological Encryption) เพื่อความปลอดภัยของข้อมูล

### 3.3 Evolution Engine
ผู้รับผิดชอบหลัก: Backend Engineer และ Biotechnical Specialist

หน้าที่:

* พัฒนาอัลกอริทึมการงอกใหม่ (Adaptive Growth) เพื่อให้เครือข่ายหาเส้นทางใหม่ได้เองเมื่อสายใยราขาด

* ออกแบบระบบ Logic สำหรับการ Update Firmware ผ่านกระบวนการส่งโปรตีนหรือตัดต่อยีนแบคทีเรีย

* ควบคุมพฤติกรรมการตัดสินใจของระบบเมื่อเจอสิ่งเร้าจากสภาพแวดล้อมที่เปลี่ยนแปลง

### 3.4 Infrastructure Layer

ผู้รับผิดชอบหลัก: Biotechnical Specialist

หน้าที่:

* จัดเตรียมและควบคุมคุณภาพของ Substrate (ฐานสารอาหาร) เพื่อให้สายใยราเติบโตได้อย่างมั่นคง

* ติดตั้งและตั้งค่า Bio-Sensors เพื่อแปลงสัญญาณทางเคมีและไฟฟ้าชีวภาพให้เป็นข้อมูลดิจิทัล

* ดูแลความปลอดภัยทางชีวภาพ (Bio-containment) ไม่ให้เครือข่ายแพร่กระจายจนควบคุมไม่ได้

### 3.5 Documentation & Quality Control

ผู้รับผิดชอบหลัก: Scrum Master และ All Team Member

หน้าที่:

* ควบคุมการเขียนเอกสาร Technical Spec ทั้งหมดใน GitHub ให้เป็นปัจจุบันและอ่านง่าย

* ตรวจสอบคุณภาพงาน (Sprint Review) ให้ตรงตามมาตรฐานที่ตกลงกันไว้ใน Product Backlog

* บันทึกปัญหาและอุปสรรค (Retrospective) เพื่อปรับปรุงกระบวนการทำงานใน Sprint ถัดไป


Gemini said
เข้าใจแล้วครับ คุณต้องการแปลงเนื้อหาความรับผิดชอบในแต่ละ Layer (4.1 - 4.4) ให้กลายเป็น Decision & Escalation Flow แบบรายการข้อ 1-5 ตามตัวอย่างในรูปภาพสุดท้ายที่คุณส่งมา

นี่คือเนื้อหาที่ปรับให้เป็นรูปแบบโฟลว์สำหรับโปรเจกต์ Living Bio Network ครับ:

## 4. Decision & Escalation Flow
#### 

1. Reality Integration & Feedback Issue → Product Owner

   สำหรับปัญหาด้านการแสดงผล Eco-Feedback และส่วนต่อประสาน Biometric Interface

2. Molecular Protocol & Encryption Conflict → System Architect

   สำหรับปัญหาด้านการรับส่งข้อมูลผ่านโมเลกุลและการเข้ารหัสด้วยยีน (Biological Encryption)

3. Adaptive Growth & Evolution Logic Error → Backend Engineer

   สำหรับปัญหาด้านตรรกะการปรับตัวของระบบและกลไกการวิวัฒนาการทางพันธุกรรม

4. Substrate & Bio-Sensor Failure → Biotechnical Specialist

   สำหรับปัญหาด้านโครงสร้างพื้นฐานทางชีวภาพ สารอาหาร และเซ็นเซอร์ตรวจจับสัญญาณ

5. Documentation & Quality Approval → Scrum Master 

   สำหรับการอนุมัติเอกสาร Technical Spec และการตรวจสอบคุณภาพงานในแต่ละ Sprint

#### Final escalation authority: Product Owner & System Architect

## 5. Collaboration Rules
* Daily Bio-Pulse (Standup): ประชุมอัปเดตสถานะงานสั้นๆ 10–15 นาที เพื่อติดตามความคืบหน้าของแต่ละ Layer และกำจัดปัญหาคอขวด (Blockers) ก่อนเริ่มงานวันถัดไป

* Bi-Weekly Network Review: จัดการสาธิต (Demo) และสรุปความสำเร็จของเครือข่าย เช่น อัลกอริทึมการเติบโตหรือโครงสร้าง DNA ทุกสิ้นสุดรอบ Sprint 2 สัปดาห์

* Core-Protocol Peer Review: การแก้ไขเนื้อหาสำคัญในสายหลัก (Main Branch) ต้องได้รับการตรวจสอบและยืนยันความถูกต้องอย่างน้อย 1 Approval เพื่อรักษาเสถียรภาพของสถาปัตยกรรม

* Architecture Guardrail: การปรับเปลี่ยนกลไกหลักของระบบ (เช่น การแก้ไขโปรโตคอลการสื่อสารโมเลกุล) ต้องผ่านการเห็นชอบจาก System Architect ก่อนทำการแก้ไข

Real-time Documentation Sync: เมื่อมีการอัปเดต Evolution Engine หรือส่วนโครงสร้างพื้นฐาน ต้องทำการบันทึกข้อมูลลงใน GitHub ทันที เพื่อให้ทีมเข้าถึงข้อมูลทางเทคนิคล่าสุดได้

## 6. Accountability Matrix (RACI Model)

| Task | Architect | Backend | Biotech | Scrum Master | PO |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Architecture Design** | R | C | C | I | A |
| **Protocol Implementation** | C | R | C | I | I |
| **Biological Growth Logic** | C | C | R | I | I |
| **Sprint Management** | I | I | I | R | C |
| **Documentation** | C | I | I | R | I |

**Legend:**
* **R** = Responsible (ผู้ลงมือทำหลัก)
* **A** = Accountable (ผู้อนุมัติและรับผิดชอบผลลัพธ์)
* **C** = Consulted (ผู้ให้คำปรึกษาหรือให้ข้อมูล)
* **I** = Informed (ผู้รับทราบความคืบหน้า)

## 7. Commitment Statement
ทีมงาน Living Bio Network (LEN) ยืนยันว่าจะปฏิบัติหน้าที่ตามบทบาทที่ได้รับมอบหมายอย่างเต็มความสามารถ และร่วมกันพัฒนาโครงสร้างเครือข่ายชีวภาพให้สำเร็จตามเป้าหมายของแต่ละ Sprint ที่กำหนดไว้



























