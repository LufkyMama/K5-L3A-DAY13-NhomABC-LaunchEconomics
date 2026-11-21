# Báo cáo cá nhân — NguyenTuanDung-2A202603559

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tuấn Dũng
- MSSV: 2A202603559
- Email: dungnguyentuan080@gmail.com
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ và điều phối Gate 2a

## 2. Phần việc phụ trách

- Quản lý và cập nhật xuyên suốt hồ sơ tổng hợp 1 trang `report/team/ho_so_launch_v0.md` từ CP1 đến CP5.
- Cập nhật thông tin nhóm và phân vai trong `TEAM.md`.
- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR ở CP3 (`report/team/bang_loi.md`), đối chiếu đồng thuận với Người gắn nhãn 1 (Vũ Nguyễn Hoàng Minh).
- Rà soát ngưỡng an toàn, thời hạn, người có quyền dừng trong `report/team/pilot_plan.yaml` (CP4) và đối chiếu chéo số liệu giữa `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md` trước cổng Gate 2a.
- Đại diện nhóm trình bày đề xuất Gate 2a và tổng hợp phiếu chấm chéo `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- **Chuẩn bị & CP1–CP2:** Khởi tạo khung `ho_so_launch_v0.md`, cập nhật `TEAM.md`; tổng hợp số liệu chi phí thật (4.472 đ/việc, 5.865 đ/yc cả hệ thống `[simulated]`), phạm vi thu hẹp `noi_dia + hang_nang`, bảng độ nhạy (top 3 yếu tố: làm lại +51,8%, xem lại +40,7%, lương +23,1%) và các rủi ro kinh tế (xem lại 100% lên 11.743–12.415 đ `[simulated]`) vào Mục 1, 2, 3, 7 của hồ sơ.
- **CP3:** Gắn nhãn độc lập đủ 20/20 ca lỗi theo nguyên nhân gốc (đạt đồng thuận 20/20 = 100% với Minh) và cập nhật Mục 5 vào hồ sơ.
- **CP4:** Rà soát 4 luật dừng, ngưỡng an toàn (6% / +2 điểm so với đối chứng, nền 4,25% toàn mẫu và 3,97% trong phạm vi), đánh đổi MDE 6 điểm (power 0,64 ở mức 5 điểm), cập nhật Mục 6 vào hồ sơ.
- **CP5:** Chốt hoàn chỉnh 1 trang `ho_so_launch_v0.md` (đủ 7 mục, đúng trạng thái `Giả lập` / `Xong, có bằng chứng`, không dùng từ cấm, đề xuất **Go có điều kiện** kèm 4 điều kiện có vai trò phụ trách và ngày kiểm tra cụ thể), chuẩn bị bảo vệ Gate 2a và tổng hợp `phieu_cham.md`.

## 4. Bằng chứng

- Commit `0979c2c`: cập nhật thông tin nhóm và vai trò trong `TEAM.md` và khung `report/team/ho_so_launch_v0.md`.
- Commit `1f2fe43`: cập nhật Mục 1, 2, 3, 7 (chi phí, độ nhạy, phạm vi pilot, rủi ro kinh tế) trong `report/team/ho_so_launch_v0.md`.
- Commit `bdf0617`: hoàn thiện bộ nhãn độc lập 20 ca của Người gắn nhãn 2 trong `report/team/bang_loi.md`.
- Commit `8f9c8e5` và commit chốt CP5: cập nhật Mục 4, 5, 6, 7 và đề xuất **Go có điều kiện** trong `report/team/ho_so_launch_v0.md`.
- File `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`, `report/team/phieu_cham.md`, `TEAM.md`.

## 5. Công cụ AI đã dùng

- Dùng Antigravity (trợ lý lập trình) để giải thích yêu cầu từng checkpoint, kiểm tra định dạng quy tắc lab (nhãn `simulated`, không dùng từ cấm, kiểm tra đối chiếu số liệu giữa các file báo cáo) và hỗ trợ soạn thảo cấu trúc báo cáo.
- Tự kiểm tra lại toàn bộ con số đối chiếu với `src/lab13.py`, `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md` và đối chiếu độc lập 20 ca lỗi với thành viên nhóm trước khi commit.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ các mốc CP1–CP5, đảm bảo tính nhất quán giữa toàn bộ 6 file hồ sơ trước giờ duyệt chéo 17:00.
- Điểm rút kinh nghiệm: cần đồng bộ lịch commit rõ ràng giữa các thành viên ở các file dùng chung (`ho_so_launch_v0.md`, `pilot_plan.yaml`) để tránh xung đột nhánh khi làm song song.
