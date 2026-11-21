# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

`python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`.

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút) | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | tổng ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | 329.585 ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** "hoá đơn chia số yêu cầu" (4.472 ÷ 274,7) [simulated].
- Khoản lớn nhất là **làm lại, 51,8%** tổng chi phí [simulated]; tiếp theo là xem lại 40,7%, nên giờ nhân viên chiếm 92,5%.
- Kiểm tra tay: 5.600 tool call × 15 đ = 84.000 đ; 1.132 phút làm lại × 2.000 đ = 2.264.000 đ — khớp bảng.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | 0,85× |

- Loại không đáng để trợ lý xử lý là **quoc_te**: 22.515 đ/việc = 1,88× của 12.000 đ, chỉ 27,3% thành công.
- Với quoc_te, chạy lại tới 3 lần **không giúp**: tỉ lệ ok theo lần thử là 30,0% → 11,4% → 2,2%, vì lỗi lặp lại trên cùng yêu cầu nên chỉ tốn thêm tiền.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 | 4.599 | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 | 5.784 | 0,48× |

- Chi phí cố định **không đổi kết luận** ở quy mô đầy đủ: 4.599 đ/việc = 0,38× của 12.000 đ [simulated].
- Nhưng khi khối lượng giảm một nửa, cố định lên 2.370 đ/việc và chi phí thành 5.784 đ = 0,48×, nên hồ sơ phải ghi rõ đang tính ở khối lượng nào.
- Cách tính: 45.000 × 900/1.200 = 33.750 việc thành công/tháng; 40.000.000 ÷ 33.750 = 1.185 đ; (3.072.513 ÷ 900) + 1.185 = 4.599 đ [simulated].

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1% |

Gốc A2: 4.472 đ [simulated]. Tự kiểm tra: mỗi cặp "gấp đôi/giảm một nửa" đối xứng đúng (5,6 ↔ 2,8; 40,7 ↔ 20,3; 51,8 ↔ 25,9).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng (+5,6% + 40,7%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 lần | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

- Giới hạn **2 lần rẻ nhất cho công ty**: 6.901.220 đ cả hệ thống, nhưng **không trùng** giới hạn cho chi phí mỗi việc thành công thấp nhất là 1 lần (4.111 đ).
- Tối ưu riêng chi phí mỗi việc thành công sẽ đẩy thêm **85 việc** (319 − 234) sang nhân viên làm thay.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`): **11.743 đ = 0,98×** của 12.000 đ với 9 phút làm lại; **12.415 đ = 1,03×** nếu dùng 15,3 phút/ca như dữ liệu [simulated].
- Cách tính: 948 yêu cầu có lần ok × 5 phút × 2.000 = 9.480.000 đ; 48 ca làm lại × 9 phút × 2.000 = 864.000 đ; token + tool = 224.513 đ; tổng 10.568.513 đ ÷ 900 = 11.743 đ [simulated].
- Pilot phải học được **tỉ lệ xem lại giảm an toàn đến đâu** và mỗi lần xem lại phải **≤ 5,1 phút** (hoặc ≤ 4,8 phút nếu làm lại 15,3 phút); xem lại 100% thì gần như không tiết kiệm vì tiền xem lại chiếm 85–90% chi phí.
