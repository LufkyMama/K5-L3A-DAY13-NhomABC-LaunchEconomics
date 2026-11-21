# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Gắn nhãn và đối chiếu

Người 1: Vũ Nguyễn Hoàng Minh · Người 2: Nguyễn Tuấn Dũng. Cột Minh và cột thống nhất là bản nháp do Codex điền từ đáp án hướng dẫn, chờ Minh rà và nhóm xác nhận.

| Ca | Nhãn người 1 (Minh, bản nháp) | Nhãn người 2 (Dũng) | Trùng? | Nhãn thống nhất (đề xuất) |
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

**Mức khớp bản nháp với nhãn Dũng:** 20/20 (100%). **Tỉ lệ đồng thuận giữa hai bộ nhãn độc lập:** chưa xác định.

## Quy tắc phân biệt cho các ca không trùng

Lượt đối chiếu bản nháp có 0 ca khác nhãn. Khi có hai bộ nhãn độc lập, ghi một câu quy tắc cho mỗi ca khác nhãn. Nếu đồng thuận dưới 80%, ghi định nghĩa đã viết lại.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Dự thảo khắc phục do Codex đề xuất. Các ngưỡng dưới đây dùng để xem xét khi thiết kế pilot.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Ghi event `refund_account_validation_failed` khi số tài khoản không đạt quy tắc của ngân hàng đã chọn. Đếm theo ngày và cảnh báo nếu có ít nhất 1 lệnh hoàn được tạo sau khi xác thực thất bại. | Kiểm tra số tài khoản trước khi tạo lệnh, chỉ rõ trường cần sửa và yêu cầu khách xác nhận lại. | Kỹ sư trưởng tích hợp thanh toán |
| 20 | Hệ thống | Đối soát sổ cái mỗi giờ theo mã đơn và mã giao dịch đủ điều kiện hoàn. Cảnh báo nếu có ít nhất 2 bản ghi hoàn thành công cho cùng giao dịch. | Dùng khóa chống trùng ổn định cho mỗi giao dịch cần hoàn. Trả lại trạng thái lệnh đã có khi nhận yêu cầu gửi lại. | Kỹ sư trưởng tích hợp thanh toán |
| 16 | Ngữ cảnh | Ghi giờ địa phương và kênh trong event `refund_notification_sent`. Rà hằng ngày và cảnh báo nếu có ít nhất 1 Zalo gửi trong khung giờ yên lặng đã cấu hình. | Xếp thông báo vào hàng đợi đến hết giờ yên lặng. Hiển thị trạng thái hoàn tiền ngay trong ứng dụng. | Quản lý sản phẩm CSKH |
| 11 | Giới hạn hệ thống | Đếm event `unsupported_input` có `input_type=audio` mỗi tuần. Rà mọi ca thiếu event hướng dẫn chuyển sang chữ. | Báo rõ giới hạn ngay khi nhận tệp thoại và cho khách tiếp tục bằng văn bản trên cùng yêu cầu. | Quản lý sản phẩm trợ lý hoàn phí |
| 12 | Ngầm | Theo dõi tiền token trung bình mỗi yêu cầu theo depot và loại yêu cầu mỗi tuần. Cảnh báo khi một depot vượt gấp 2 lần trung vị các depot trong cùng loại trong 2 tuần liên tiếp. | Ghi rõ trường thiếu khi tool trả kết quả, sửa hợp đồng dữ liệu depot và giới hạn số lần gọi lặp khi thiếu cùng một trường. | Kỹ sư trưởng tích hợp dữ liệu depot |
