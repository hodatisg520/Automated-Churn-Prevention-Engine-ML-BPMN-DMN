# Hệ thống AI & Tự động hoá Giữ chân Khách hàng (Customer Churn Retention)

![BPMN Process Diagram](camunda_models/churn_process.png)
*(Sơ đồ luồng tự động hóa quy trình nghiệp vụ BPMN)*

![DMN Decision Table](camunda_models/churn_decision.png)
*(Bảng ra quyết định tự động DMN dựa trên xác suất rời mạng)*

---

## 🎯 Vấn đề doanh nghiệp
Trong ngành viễn thông, việc tìm kiếm một khách hàng mới thường tốn kém gấp 5-25 lần so với việc giữ chân khách hàng hiện tại. Tuy nhiên, doanh nghiệp thường gặp hai rào cản lớn:
1. **Phản ứng chậm:** Chỉ chăm sóc khi khách hàng đã gọi điện yêu cầu hủy dịch vụ, lúc này đã quá muộn.
2. **Chi phí cào bằng:** Tặng voucher giảm giá cho tất cả mọi người (kể cả những người không có ý định rời đi, hoặc khách hàng mang lại ít lợi nhuận), dẫn đến lãng phí khổng lồ ngân sách Marketing.

## 🧠 Giải pháp AI
Để giải quyết bài toán trên, dự án sử dụng **Machine Learning** (dựa trên tập dữ liệu Telco Customer Churn) nhằm "bắt mạch" khách hàng. 
Thay vì dự đoán nhị phân (Rời đi / Không rời đi), mô hình AI được tinh chỉnh để trả về **Xác suất rời mạng (Churn Probability)**. Ví dụ: *Khách hàng A có 85% nguy cơ rời mạng vào tháng tới.*

Kết hợp với chỉ số **LTV (Lifetime Value - Giá trị vòng đời khách hàng)**, hệ thống phân loại rõ khách hàng nào là VIP cần giữ lại bằng mọi giá, khách hàng nào là Standard chỉ cần các phương án chăm sóc cơ bản.

## ⚙️ Cách tự động hóa bằng Camunda
Xác suất từ AI chỉ là con số vô tri nếu không được gắn vào hành động kinh doanh thực tế. Dự án sử dụng **Camunda (BPMN & DMN)** để tự động hóa hoàn toàn quy trình ra quyết định mà không cần nhân sự can thiệp thủ công:

- **DMN (Decision Model and Notation):** Đóng vai trò là "bộ não nghiệp vụ". Nhận đầu vào là *Xác suất rời mạng* (từ mô hình AI) và *Phân khúc khách hàng* (VIP/Standard). Hệ thống tự động đối chiếu quy tắc để ra quyết định:
  - `Khách VIP + Nguy cơ cao (>= 70%)` ➡️ Tặng voucher 30% và phân bổ nhân sự gọi điện trực tiếp.
  - `Khách Standard + Nguy cơ cao` ➡️ Gửi SMS tự động tặng data 4G.
- **BPMN (Business Process Model and Notation):** Đóng vai trò là "người điều phối". Quản lý luồng chạy xuyên suốt từ việc lấy dữ liệu (Start) -> Gọi AI dự đoán (Service Task) -> Đưa vào DMN ra quyết định (Business Rule Task) -> Thực thi gửi Email/SMS (Send Task).

## 🚀 Kết quả mong đợi
- **Tăng tỷ lệ giữ chân khách hàng (Retention Rate):** Khách hàng được chăm sóc "đúng người, đúng thời điểm, đúng phương thức".
- **Tối ưu chi phí (Cost Optimization):** Ngân sách khuyến mãi (Voucher, Data) chỉ tập trung giải ngân cho nhóm khách hàng có giá trị cao (VIP) và thực sự có nguy cơ rời mạng.
- **Vận hành tự động (Zero-touch Operations):** Quy trình diễn ra hoàn toàn tự động, giải phóng hàng ngàn giờ làm việc thủ công của đội ngũ CSKH, giảm thiểu độ trễ trong xử lý rủi ro.

---
**Cấu trúc thư mục dự án:**
- `/data`: Chứa file dữ liệu gốc Telco Customer Churn (CSV).
- `/notebooks`: Chứa Jupyter Notebook huấn luyện mô hình AI và file model đã export.
- `/camunda_models`: Chứa các sơ đồ thiết kế BPMN, DMN và hình ảnh kết xuất.
- `main.py`: File kịch bản (Script) mô phỏng lại toàn bộ luồng tích hợp của hệ thống.
