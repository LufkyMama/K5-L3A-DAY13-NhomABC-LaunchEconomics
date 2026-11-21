# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: NhomABC · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc (gấp 16,3× hóa đơn 274,7 đ/yc; giờ nhân viên 92,5%). Phạm vi `noi_dia` + `hang_nang`: 3.414 đ; cộng cố định 40 triệu/tháng: 4.599 đ = 0,38× (ở 45.000 yc/tháng) và 5.784 đ = 0,48× (nửa khối lượng) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%, lên 6.787 đ) · 2. Tỉ lệ xem lại (+40,7%, lên 6.292 đ) · 3. Lương nhân viên (+23,1%, lên 5.506 đ); đổi cặp token×2 + xem lại×2: 6.543 đ (+46,3%) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống trên toàn mẫu: 5.865 đ/yc = 0,49× của 12.000 đ (giới hạn 2 lần rẻ nhất: 6.901.220 đ). Thu hẹp phạm vi pilot: giữ `noi_dia` (0,22×) & `hang_nang` (0,69×); loại `quoc_te` (1,88×, 27,3% thành công, chạy lại 3 lần không giúp: 30,0% → 11,4% → 2,2%) và `doi_tac` (0,85×, điều khoản riêng) [simulated] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử giả lập: 82,83% đóng đúng hạn và không mở lại, 27,12% sửa hoặc bỏ gợi ý, 4,25% mở lại. Hàng nặng mở lại 8,23% (13/158), so với 3,16% ở nội địa. Có 12 event dự kiến. | Giả lập | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Có 20 ca và 5 biện pháp cho 5 loại. Cần xác nhận nguồn bộ nhãn độc lập của Minh trước khi dùng kết quả đồng thuận. | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Ngẫu nhiên theo nhân viên, 20 + 20, phân tầng theo depot. Mục tiêu 5.980 yêu cầu/nhóm, MDE +6 điểm, power khoảng 64% ở +5 điểm. Có 4 luật dừng và hoàn nguyên trong 30 phút. | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | (1) Số ca làm lại tăng gấp đôi: +51,8% lên 6.787 đ/việc [simulated]; (2) Phải xem lại 100% kéo dài (`noi_dia` + `hang_nang`): 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút/ca; hòa vốn ≤ 5,1 hoặc 4,8 phút/lần xem lại) [simulated]; (3) Khối lượng giảm một nửa: cố định tăng lên +2.370 đ/việc → 5.784 đ [simulated] | Giả lập | PM trợ lý hoàn phí |

**Điều kiện trước khi mở pilot (mốc rà soát đề xuất 30/11/2026)**

- Kỹ sư trưởng tích hợp thanh toán kiểm thử khóa chống trùng và đối soát sổ cái cho ca 7 và 20.
- Kỹ sư trưởng agent rà bằng chứng gắn nhãn độc lập của CP3 và kiểm thử nối event bằng `trace_id` cho cả hai nhóm. PM kiểm tra số phút đo thực tế sau tuần đầu vào ngày 08/12/2026.
- Giám đốc vận hành xác nhận có đủ 20 + 20 nhân viên và đủ lưu lượng để đạt 5.980 yêu cầu/nhóm, chấp nhận MDE +6 điểm. Nếu chưa đủ mẫu, dời mốc quyết định dự kiến 25/01/2027.
- Trưởng nhóm CSKH xác nhận trước khi mở pilot cách ghi phút thực tế và lịch rà mở lại riêng cho hàng nặng. Ngày 17/12/2026, rà điều kiện giảm xem lại theo bậc: tỉ lệ sửa hoặc bỏ dưới 15% và đạt ngưỡng an toàn. Kịch bản xem lại 100% có thể vượt chi phí làm thủ công (12.415 đ so với 12.000 đ) [simulated].

**Đề xuất: Go có điều kiện** cho pilot `noi_dia` và `hang_nang` sau khi hoàn tất các điều kiện trên.
