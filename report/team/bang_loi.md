# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: **Vũ Nguyễn Hoàng Minh** · Người gắn nhãn 2: **Nguyễn Tuấn Dũng**. Hai người gắn độc lập cả 20 ca trong 8 phút, không trao đổi; bảng thống nhất chỉ được tổng hợp sau khi so nhãn.

| Ca | Nhãn người gắn nhãn 1 (Minh) | Nhãn người gắn nhãn 2 (Dũng) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận: 20/20 = 100%** (ngưỡng yêu cầu: từ 16/20 = 80%). Cả hai bộ nhãn khớp đáp án 20/20 ca.

## Quy tắc phân biệt cho ca bất đồng

Lượt gắn nhãn này **không có ca bất đồng**. Nhóm viết sẵn quy tắc dưới đây để dùng khi gặp ca dễ lẫn:

- **Ca 6, 9 — Do người dùng, không phải Hệ thống:** gốc lỗi là khách chọn sai mục hoặc nhập sai mã; việc trợ lý không gợi ý thuộc cột khắc phục, không đổi nhãn.
- **Ca 13 — Giới hạn hệ thống:** yêu cầu nằm ngoài phạm vi/không có dữ liệu, kể cả khi trợ lý trả lời chung chung thay vì nói rõ giới hạn.
- **Ca 8, 15 — Hệ thống, không phải Ngầm:** sai đã lộ ra và nhân viên bắt được; Ngầm chỉ dùng khi cả khách lẫn hệ thống không nhận ra cho tới lúc kiểm tra mẫu.
- **Ca 18 — Ngữ cảnh:** số tiền đúng chính sách, chỉ giả định “khách hiểu cách tính” là không khớp hoàn cảnh.
- **Ca 12 — Ngầm:** kết quả vẫn đúng nhưng chi phí gấp 3 lần suốt 3 tuần mà không ai thấy; “sai” có thể là sai về chi phí, không chỉ về câu trả lời.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Mỗi dòng có cách phát hiện đo được bằng event, ngưỡng và tần suất; người phụ trách là một vai trò có quyền quyết định. Mọi event đều mang `trace_id` để nối với trace của agent.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_account_validation_failed` khi số tài khoản không đạt quy tắc ngân hàng; đếm hằng ngày, cảnh báo nếu có ít nhất 1 lệnh hoàn được tạo sau khi xác thực thất bại | Kiểm tra số tài khoản trước khi tạo lệnh, chỉ rõ trường cần sửa và yêu cầu khách xác nhận lại | Kỹ sư trưởng tích hợp thanh toán |
| 20 | Hệ thống | Đối soát sổ cái mỗi giờ theo mã đơn và mã giao dịch; cảnh báo nếu có ít nhất 2 bản ghi hoàn thành công cho cùng một giao dịch | Dùng khóa chống trùng ổn định cho mỗi giao dịch cần hoàn; trả lại trạng thái lệnh đã có khi nhận yêu cầu gửi lại | Kỹ sư trưởng tích hợp thanh toán |
| 16 | Ngữ cảnh | Event `refund_notification_sent` ghi giờ địa phương và kênh; rà hằng ngày, cảnh báo nếu có ít nhất 1 tin Zalo gửi trong khung giờ yên tĩnh đã cấu hình | Xếp thông báo vào hàng đợi đến hết giờ yên tĩnh; hiển thị trạng thái hoàn tiền ngay trong ứng dụng | Quản lý sản phẩm CSKH |
| 11 | Giới hạn hệ thống | Đếm event `unsupported_input` có `input_type=audio` mỗi tuần; rà các ca thiếu event hướng dẫn chuyển sang chữ, ngưỡng 0 ca thiếu | Báo rõ giới hạn ngay khi nhận tệp thoại và cho khách tiếp tục bằng văn bản trên cùng yêu cầu | Quản lý sản phẩm trợ lý hoàn phí |
| 12 | Ngầm | Theo dõi tiền token trung bình mỗi yêu cầu theo depot và loại yêu cầu mỗi tuần; cảnh báo khi một depot vượt gấp 2 lần trung vị các depot trong cùng loại trong 2 tuần liên tiếp | Ghi rõ trường thiếu khi tool trả kết quả; sửa hợp đồng dữ liệu depot và giới hạn số lần gọi lặp khi thiếu cùng một trường | Kỹ sư trưởng tích hợp dữ liệu depot |
