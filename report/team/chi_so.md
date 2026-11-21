# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Ba chỉ số đầu tính trên 1.200 yêu cầu của đợt chạy thử. Đây là **chỉ số trong đợt chạy thử**, không phải kết luận trợ lý đã nâng chỉ số, vì đợt chạy thử không có nhóm đối chứng.

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200) |
| Dùng (nhóm đề xuất) | Tỉ lệ gợi ý được giữ nguyên | `quyet_dinh_xem_lai` là `giu`, chia số yêu cầu được xem lại | **72,88%** (129/177) |
| An toàn (nhóm đề xuất) | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số đơn sai tiền chia số đơn được kiểm tra mẫu | Chưa có dữ liệu kiểm tra mẫu; đo hằng tuần trong pilot |

- Trong phạm vi `noi_dia + hang_nang`: tỉ lệ mở lại 7 ngày là **3,97%** (39/982); riêng `noi_dia` 3,16%, `hang_nang` 8,23%.
- Chỉ số chính bằng đúng tỉ lệ đóng trong 24 giờ (994/1.200) vì không có ca nào đóng trong 24 giờ lại bị mở lại trong 7 ngày.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `attempt`, `tokens_in/out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | `giu/sua/bo`, `phut_xem_lai` (đo thật), `trace_id` | Khi bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai`, `ly_do`, `trace_id` | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi sổ |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `trace_id` | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | `reopened_at`, `reason`, `trace_id` | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan`, `so_tien_dung`, `trace_id` | Hằng tuần, khi kiểm tra mẫu |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, event dùng để tính là:

- **Chính (82,83%):** `refund_request_created` để xác định yêu cầu và nhóm; `ticket_closed` để đo đóng trong 24 giờ; `ticket_reopened` để loại ca mở lại trong 7 ngày.
- **Dùng — bỏ qua gợi ý (27,12%):** `agent_suggestion_shown` để biết gợi ý đã hiện; `staff_review_decision` để đếm `sua` và `bo`.
- **An toàn — mở lại (4,25%):** `ticket_reopened`, nối với `refund_request_created` qua `trace_id`.
- **Dùng — giữ gợi ý (72,88%):** `staff_review_decision` với quyết định `giu`, chia tổng số quyết định.
- **An toàn — sai tiền qua kiểm tra mẫu:** `refund_ledger_write` để lấy số tiền đã hoàn; `audit_sample_checked` để so với số tiền đúng.

Chỉ số nào không tính được từ danh sách event trên thì chưa đo được. Cả năm chỉ số trong bảng đều có event tương ứng.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công lên **6.787 đ** [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp về `noi_dia`, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | **11.743 đ = 0,98×** của 12.000 đ; **12.415 đ = 1,03×** nếu làm lại 15,3 phút/ca [simulated] | % yêu cầu được xem lại còn > 50% cuối bước 0.25 | Giảm xem lại theo bậc khi tỉ lệ `sua + bo` < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng: **+1.185 đ/việc** ở 45.000 yêu cầu/tháng, **+2.370 đ/việc** nếu còn một nửa [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
