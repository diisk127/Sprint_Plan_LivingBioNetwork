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
### 3.1 Product Owner และ System Architect
#### 

ผู้รับผิดชอบหลัก: Product Owner และ System Architect

หน้าที่:

* ออกแบบการแสดงผล (Dashboard/Visualization) เพื่อให้ผู้ใช้เข้าใจสถานะของเครือข่ายจำลอง

* พัฒนารูปแบบการโต้ตอบและรับข้อมูล (Interface) จากสภาพแวดล้อมเข้าสู่ระบบดิจิทัล

* ตรวจสอบความถูกต้องของการนำข้อมูลจากโลกภายนอกเข้าสู่โครงสร้างเครือข่าย

### 3.2 Existence Communication Layer

ผู้รับผิดชอบหลัก: System Architect และ Backend Engineer

หน้าที่:

* กำหนดโปรโตคอลการจัดเก็บข้อมูลในรูปแบบ DNA Sequence และการส่งสัญญาณผ่านสารเคมี

* ออกแบบโครงสร้างข้อมูล ExistencePacket เพื่อให้ Node ต่างๆ สามารถสื่อสารรหัสพันธุกรรมกันได้อย่างแม่นยำ

* จัดการระบบการเข้ารหัสชีวภาพ (Biological Encryption) เพื่อความปลอดภัยของข้อมูล

### 3.3 Evolution Engine
ผู้รับผิดชอบหลัก: Backend Engineer และ Quality Assurance (QA)

หน้าที่:

* พัฒนาและทดสอบอัลกอริทึมการหาเส้นทางใหม่ (Adaptive Routing) เมื่อการเชื่อมต่อขาดหาย

* ออกแบบและตรวจสอบ Logic ของการอัปเดตระบบ (Firmware Update Logic) ผ่านเครือข่ายจำลอง

* QA: ทำการจำลองสถานการณ์ (Scenario Testing) เพื่อดูพฤติกรรมการตัดสินใจของระบบ

### 3.4 Infrastructure & Quality Layer

ผู้รับผิดชอบหลัก: Quality Assurance (QA)

หน้าที่:

* System Integrity: ตรวจสอบความเสถียรของระบบจำลอง Node และประสิทธิภาพการประมวลผล

* Bug Tracking: ค้นหาและรายงานข้อผิดพลาดของระบบก่อนการ Deploy งานในแต่ละ Sprint

* Compliance: ควบคุมมาตรฐานของโค้ดและโครงสร้างข้อมูลให้เป็นไปตามที่ Architect ออกแบบไว้

### 3.5 Documentation & Quality Control

ผู้รับผิดชอบหลัก: Scrum Master และ All Team Member

หน้าที่:

* ควบคุมการเขียนเอกสาร Technical Spec ทั้งหมดใน GitHub ให้เป็นปัจจุบันและอ่านง่าย

* ตรวจสอบคุณภาพงาน (Sprint Review) ให้ตรงตามมาตรฐานที่ตกลงกันไว้ใน Product Backlog

* บันทึกปัญหาและอุปสรรค (Retrospective) เพื่อปรับปรุงกระบวนการทำงานใน Sprint ถัดไป


## 4. Decision & Escalation Flow
#### 
* Reality Integration & Feedback Issue → Product Owner
(ปัญหาด้านการแสดงผลและส่วนต่อประสานผู้ใช้งาน)

* Data Protocol & Encryption Conflict → System Architect
(ปัญหาด้านการรับส่งข้อมูลและการเข้ารหัสระบบ)

* Adaptive Routing & Logic Error → Backend Engineer
(ปัญหาด้านตรรกะการทำงานและการประมวลผลหลังบ้าน)

* System Stability & Test Failure → Quality Assurance (QA)
(ปัญหาด้านความเสถียร บัค และผลการทดสอบที่ไม่ผ่านเกณฑ์)

* Process & Quality Approval → Scrum Master
(การอนุมัติเอกสารและการตรวจสอบมาตรฐานการทำงานในทีม)

#### Final escalation authority: Product Owner & System Architect

## 5. Collaboration Rules
* Daily Bio-Pulse (Standup): ประชุมอัปเดตสถานะงานสั้นๆ 10–15 นาที เพื่อติดตามความคืบหน้าของแต่ละ Layer และกำจัดปัญหาคอขวด (Blockers) ก่อนเริ่มงานวันถัดไป

* Bi-Weekly Network Review: จัดการสาธิต (Demo) และสรุปความสำเร็จของเครือข่าย เช่น อัลกอริทึมการเติบโตหรือโครงสร้าง DNA ทุกสิ้นสุดรอบ Sprint 2 สัปดาห์

* Core-Protocol Peer Review: การแก้ไขเนื้อหาสำคัญในสายหลัก (Main Branch) ต้องได้รับการตรวจสอบและยืนยันความถูกต้องอย่างน้อย 1 Approval เพื่อรักษาเสถียรภาพของสถาปัตยกรรม

* Architecture Guardrail: การปรับเปลี่ยนกลไกหลักของระบบ (เช่น การแก้ไขโปรโตคอลการสื่อสารโมเลกุล) ต้องผ่านการเห็นชอบจาก System Architect ก่อนทำการแก้ไข

* Real-time Documentation Sync: เมื่อมีการอัปเดต Evolution Engine หรือส่วนโครงสร้างพื้นฐาน ต้องทำการบันทึกข้อมูลลงใน GitHub ทันที เพื่อให้ทีมเข้าถึงข้อมูลทางเทคนิคล่าสุดได้

## 6. Accountability Matrix (RACI Model)

### 6. Accountability Matrix (RACI Model)

| Task | Architect | Backend | QA | Scrum Master | PO |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Architecture Design** | **A** | R | C | I | I |
| **Protocol Implementation** | C | **A** | R | I | I |
| **System Logic & Bug Testing** | I | C | **A** | R | I |
| **Sprint Management** | I | I | I | **A** | R |
| **Documentation & Quality** | C | I | R | **A** | I |

**Legend:**
* **R** = Responsible (ผู้ลงมือทำหลัก)
* **A** = Accountable (ผู้อนุมัติและรับผิดชอบผลลัพธ์)
* **C** = Consulted (ผู้ให้คำปรึกษาหรือให้ข้อมูล)
* **I** = Informed (ผู้รับทราบความคืบหน้า)

## 7. Commitment Statement
ทีมงาน Living Bio Network (LEN) ยืนยันว่าจะปฏิบัติหน้าที่ตามบทบาทที่ได้รับมอบหมายอย่างเต็มความสามารถ และร่วมกันพัฒนาโครงสร้างเครือข่ายชีวภาพให้สำเร็จตามเป้าหมายของแต่ละ Sprint ที่กำหนดไว้



























