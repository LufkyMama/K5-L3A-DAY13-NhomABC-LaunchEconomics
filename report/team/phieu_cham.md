# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): NhomABC (L3A)
- Nhóm được chấm: Soopi (L3A) — `https://github.com/tiennguyen0606/K5-L3A-DAY13-Soopi-LaunchEconomics`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất **Go có điều kiện** khớp số liệu; nêu đủ các số bất lợi (làm lại ×2: 6.787 đ/+51,8%; xem lại 100%: 11.743–12.414 đ = 0,98×–1,03×; khối lượng giảm 50%: định phí 2.370 đ; power còn 0,64 ở mức +5 điểm) và có 4 điều kiện xử lý kèm vai trò + mốc T-3/T-2/T-1/T+7. *(Góp ý nhỏ: Mục 2 và Mục 5 nên đổi "Người kiểm số"/"Người gắn nhãn 2" sang vai trò vận hành tại LogiX-VN; Mục 3 nên bổ sung thêm chi phí cả hệ thống 5.865 đ = 0,49× từ A2.)* |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số từ `_simulated` ở mục 1, 2, 3, 7 và điều kiện 4 đều gắn nhãn `[simulated]`, cột trạng thái ghi đúng `Giả lập`, không có từ cấm trong `report/team/`. Phạm vi thu hẹp rõ ràng (`noi_dia` 0,22×, `hang_nang` 0,69×; loại `quoc_te` 1,88× / 27,3% thành công và `doi_tac` 0,85× / điều khoản riêng). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia ngẫu nhiên 20 + 20 nhân viên phân tầng theo depot, đối chứng song song, giảm spillover theo `staff_id`; đủ cỡ mẫu với đánh đổi MDE +6 điểm (`n = 859/nhóm`, `m ≥ 299`, `DE = 6,96`, ước tính công suất 9,74 ngày); có 4 luật dừng đủ 4 vế (tách riêng hoàn trùng dừng ngay trong 30 phút; mở lại >6% hoặc +2 điểm/3 ngày; chi phí >8.000 đ/2 tuần; bỏ qua >40%/1 tuần), rõ người có quyền dừng và rollback 30 phút. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ của nhóm Soopi nhất quán giữa cả 5 file (`bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`), minh bạch nhãn `simulated`, nêu thẳng các số bất lợi (xem lại 100% lên 0,98×–1,03×, power 0,64 ở mức +5 điểm) và thiết kế pilot có đối chứng, đủ 20 cụm/nhóm cùng 4 luật dừng chặt chẽ (đặc biệt tách riêng luật dừng ngay khi có ≥ 1 ca hoàn trùng). Hội đồng đồng thuận **Go có điều kiện** theo đúng 4 điều kiện nhóm đã đặt, và lưu ý nhóm làm rõ thời lượng bước rollout 0.50 (vì ước tính cần 9,74 ngày > 7 ngày) trước khi chốt lịch.

**Một câu hỏi cho đội trình:** Trong `pilot_plan.yaml`, nhóm ước tính cần khoảng 9,74 ngày để mỗi nhân viên đạt đủ `m = 299` yêu cầu trong phạm vi `noi_dia + hang_nang`, nhưng lịch rollout ghi mỗi bước 1 tuần (7 ngày) — vậy ở bước 0.50 nhóm có kéo dài thời gian đo lên ít nhất 2 tuần để đủ cỡ mẫu 859/nhóm không, và con số so sánh 0,28×/0,38× ở Mục 3 đã tính phần nhân viên làm thay các ca không thành công chưa?

**Câu trả lời của đội trình (ghi lại tại buổi):** Nhóm Soopi đồng ý với cả hai điểm góp ý: (1) sẽ kéo dài thời gian đo ở bước rollout 0.50 lên ít nhất 2 tuần (vượt mốc ước tính 9,74 ngày) để đảm bảo đủ cỡ mẫu `m ≥ 299` yêu cầu/nhân viên (859 hiệu dụng/nhóm) trước ngày chốt quyết định; (2) xác nhận con số 0,28×/0,38× ở Mục 3 là tính trên các việc thành công trong phạm vi pilot, còn chi phí cả hệ thống (đã cộng phần nhân viên làm thay các ca không thành công) là 5.865 đ/yêu cầu = 0,49× `[simulated]` như đã nêu trong `bang_chi_phi.md`, và sẽ bổ sung rõ vào hồ sơ cùng việc chuẩn hóa tên vai trò vận hành ở Mục 2 và Mục 5.
