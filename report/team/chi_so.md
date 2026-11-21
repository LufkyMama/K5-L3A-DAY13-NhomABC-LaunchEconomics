# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính | Đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h=1` và `mo_lai_trong_7_ngay=0`, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ sửa hoặc bỏ gợi ý | Số yêu cầu đã xem lại có quyết định `sua` hoặc `bo`, chia số yêu cầu đã xem lại | **27,12%** (48/177) |
| An toàn | Tỉ lệ mở lại trong 7 ngày | Số yêu cầu có `mo_lai_trong_7_ngay=1`, chia tổng số yêu cầu | **4,25%** (51/1.200) |
| Dùng | Tỉ lệ mở trợ lý trên yêu cầu hợp lệ | Số yêu cầu hợp lệ của nhóm can thiệp có ít nhất một lượt mở trợ lý, chia tổng yêu cầu hợp lệ của nhóm đó | Đo trong pilot |
| An toàn | Tỉ lệ hoàn sai tiền qua kiểm tra mẫu | Số giao dịch được kiểm tra có số tiền hoàn khác số đúng theo chính sách, chia tổng giao dịch đã kiểm tra trong tuần | Đo trong pilot |

Các số tính thử do [lab13.py](../../src/lab13.py) tính từ 1.200 yêu cầu của đợt chạy thử giả lập. Đợt chạy thử thiếu đối chứng, nên các số này mô tả kết quả quan sát trong mẫu. Mở lại là tín hiệu an toàn, còn xác định sai tiền cần đối soát. Trong phạm vi pilot, mẫu ghi nhận 3,97% (39/982), gồm 3,16% (26/824) ở nội địa và 8,23% (13/158) ở hàng nặng. Trong pilot, báo riêng từng loại theo nhóm để phát hiện chênh lệch bị che khi gộp.

Chỉ số bổ trợ của nhóm: **72,88%** (129/177) yêu cầu đã xem lại có quyết định `giu`. Dùng quyết định cuối từ `staff_review_decision` trên mỗi yêu cầu.

## Danh sách event

Mỗi yêu cầu được cấp `trace_id` khi tiếp nhận, kể cả ở nhóm đối chứng. Các event giữ cùng `trace_id` và `request_id` để nối theo yêu cầu. Khi tính tỉ lệ theo yêu cầu, chỉ đếm một lần trên mỗi `request_id`.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống yêu cầu | `trace_id`, `request_id`, `received_at`, `loai`, `depot` | Khi tiếp nhận |
| `pilot_request_assigned` | Hệ thống điều phối | `trace_id`, `request_id`, `staff_id`, `arm`, `eligible`, `phase` | Khi chuyển ca cho nhân viên |
| `agent_session_opened` | Giao diện CSKH | `trace_id`, `request_id`, `staff_id`, `opened_at` | Khi mở trợ lý cho yêu cầu |
| `agent_run_completed` | Agent | `trace_id`, `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status` | Sau mỗi lượt chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `trace_id`, `request_id`, `suggestion_id`, `staff_id`, `shown_at` | Khi hiện gợi ý |
| `staff_review_decision` | Giao diện CSKH | `trace_id`, `request_id`, `suggestion_id`, `decision` (giu, sua, bo), `review_minutes`, `decided_at` | Khi nhân viên chốt quyết định |
| `staff_rework_completed` | Giao diện CSKH | `trace_id`, `request_id`, `rework_minutes`, `reason` | Khi hoàn tất làm lại |
| `refund_ledger_write` | Sổ cái | `trace_id`, `request_id`, `source_transaction_id`, `ledger_entry_id`, `idempotency_key`, `amount`, `status` | Khi sổ cái phản hồi |
| `handoff_to_staff` | Backend điều phối | `trace_id`, `request_id`, `reason`, `attempt`, `handoff_at` | Khi chuyển yêu cầu sang xử lý thủ công |
| `ticket_closed` | Hệ thống ticket | `trace_id`, `request_id`, `closed_at`, `resolution` | Khi đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | `trace_id`, `request_id`, `reopened_at`, `reason` | Khi mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | `trace_id`, `request_id`, `ledger_entry_id`, `actual_amount`, `expected_amount`, `policy_version`, `checked_at` | Khi kiểm tra mẫu hằng tuần |

**Event dùng cho từng chỉ số**

- Đóng trong 24 giờ và không mở lại trong 7 ngày: nối `refund_request_created`, `pilot_request_assigned`, `ticket_closed` và `ticket_reopened`. Đếm tất cả yêu cầu hợp lệ đủ thời gian theo dõi, kể cả ca chưa đóng.
- Sửa hoặc bỏ gợi ý: dùng quyết định cuối từ `staff_review_decision` trên mỗi yêu cầu đã xem lại. Luật dừng CP4 dùng cùng mẫu số.
- Mở lại trong 7 ngày: nối `pilot_request_assigned`, `ticket_closed` và `ticket_reopened` để xác định nhóm và khoảng thời gian từ đóng đến mở lại. Mẫu số là yêu cầu đủ thời gian theo dõi trong từng nhóm.
- Mở trợ lý: nối `pilot_request_assigned` và `agent_session_opened`. Mẫu số lấy từ toàn bộ yêu cầu hợp lệ ở nhóm can thiệp.
- Hoàn sai tiền: so `actual_amount` với `expected_amount` trong `audit_sample_checked`, đếm một lần theo `ledger_entry_id`. Luật dừng riêng cho hoàn trùng lấy dữ liệu từ `refund_ledger_write`.

## E2 · Rủi ro kinh tế

Tác động lấy từ [bảng độ nhạy B1–B4](bang_chi_phi.md). Các ngưỡng theo dõi dưới đây là đề xuất vận hành.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Chi phí làm lại tăng | Gấp đôi chi phí làm lại đưa chi phí mỗi việc thành công lên **6.787 đ (+51,8%)** [simulated] | Tỉ lệ yêu cầu phải làm lại vượt 7% trong tuần. Mẫu thử trong phạm vi là 4,89% (48/982). Đếm theo `staff_rework_completed` trên yêu cầu nhóm can thiệp. | Rà 20 trace làm lại. Nếu chi phí vượt 8.000 đ trong hai tuần liên tiếp, giữ pha và đề xuất thu hẹp về nội địa. | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | **11.743 đ/việc**, hoặc **12.415 đ/việc** theo thời gian làm lại quan sát trong mẫu, so với mốc 12.000 đ [simulated] | Rà nếu tỉ lệ xem lại còn trên 50% vào cuối pha 25%. Theo dõi phút xem lại và tỉ lệ sửa hoặc bỏ qua `staff_review_decision`. | Giữ pha nếu chi phí vượt ngưỡng CP4. Chỉ thử giảm mức xem lại theo bậc khi tỉ lệ sửa hoặc bỏ dưới 15%, đối soát tiền và tỉ lệ mở lại vẫn đạt yêu cầu an toàn. | Trưởng nhóm CSKH |
| Khối lượng thấp hơn kế hoạch | Chi phí cố định tăng từ 1.185 lên 2.370 đ/việc nếu khối lượng giảm một nửa [simulated] | Số việc thành công theo tuần xuống dưới 50% kế hoạch. | Kiểm tra lại dự phóng chi phí cố định và giữ nguyên phạm vi cho tới khi đủ mẫu hiệu dụng. | PM trợ lý hoàn phí |
