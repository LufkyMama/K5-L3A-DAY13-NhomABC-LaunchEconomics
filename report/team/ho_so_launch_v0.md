# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: NhomABC · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc (gấp 16,3× hóa đơn 274,7 đ/yc; giờ nhân viên 92,5%). Phạm vi `noi_dia` + `hang_nang`: 3.414 đ; cộng cố định 40 triệu/tháng: 4.599 đ = 0,38× (ở 45.000 yc/tháng) và 5.784 đ = 0,48× (nửa khối lượng) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%, lên 6.787 đ) · 2. Tỉ lệ xem lại (+40,7%, lên 6.292 đ) · 3. Lương nhân viên (+23,1%, lên 5.506 đ); đổi cặp token×2 + xem lại×2: 6.543 đ (+46,3%) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống: 5.865 đ/yc = 0,49× của 12.000 đ (giới hạn 2 lần rẻ nhất: 6.901.220 đ). Thu hẹp phạm vi pilot: giữ `noi_dia` (0,22×) & `hang_nang` (0,69×); loại `quoc_te` (1,88×, 27,3% thành công, chạy lại 3 lần không giúp: 30,0% → 11,4% → 2,2%) và `doi_tac` (0,85×, điều khoản riêng) [simulated] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | ... | Chưa | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | 20 ca gắn nhãn độc lập: đồng thuận 20/20 = 100% (Người dùng: 4 · Hệ thống: 5 · Ngữ cảnh: 4 · Giới hạn: 4 · Ngầm: 3); 5 ca khắc phục đại diện (Ca 1, 20, 16, 11, 12) đều có event/ngưỡng đo và 1 vai trò phụ trách | Xong, có bằng chứng | Kỹ sư trưởng tích hợp thanh toán |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên 20 + 20 (`seed 1304`, phân tầng theo depot), phạm vi `noi_dia` + `hang_nang`, rollout `[10%, 25%, 50%]`; đánh đổi MDE 6 điểm (`n = 859/nhóm`, `m ≥ 299 yc/người`, `5.980 yc thực/nhóm`, `DE = 6,96`; power `0,64` ở mức 5 điểm); 4 luật dừng đủ 4 vế (hoàn trùng ≥ 1 ca; mở lại >6% hoặc +2 điểm/3 ngày; chi phí >8.000 đ/2 tuần; bỏ gợi ý >40%/1 tuần), rollback 30 phút, ngày quyết định `2027-01-25` | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | (1) Số ca làm lại tăng gấp đôi: +51,8% lên 6.787 đ/việc [simulated]; (2) Phải xem lại 100% kéo dài (`noi_dia` + `hang_nang`): 11.743 đ = 0,98× (hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút/ca; hòa vốn ≤ 5,1 hoặc 4,8 phút/lần xem lại) [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- ...
