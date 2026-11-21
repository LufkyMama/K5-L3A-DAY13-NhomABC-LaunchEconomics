# Team

## Thông tin nhóm

- Tên nhóm: NhomABC
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-NhomABC-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: https://github.com/LufkyMama/K5-L3A-DAY13-NhomABC-LaunchEconomics

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Vũ Nguyễn Hoàng Minh | 2A202603541 | minhhoang6724@gmail.com | LufkyMama |  Kiểm số và pilot |
|   2 | Bùi Thế Anh | 2A202603546 | theanh7888189@gmail.com | theahASR | Code và chi phí |
|   3 | Nguyễn Tuấn Dũng | 2A202603559 | dungnguyentuan080@gmail.com | Ntd1411 | Hồ sơ và điều phối |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## BuiTheAnh-2A202603546

### Phần việc phụ trách

- Người viết code (code và chi phí): `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/chi_so.md`.
- CP1–CP2: mô hình chi phí và bảng độ nhạy; CP3: rà soát bảng lỗi và cách khắc phục; CP4: tỉ lệ mở lại 7 ngày và kiểm tra chéo cỡ mẫu; CP5: chỉ số, event, rủi ro kinh tế.

### Đóng góp cụ thể

- CP1: viết A1–A4, ba phép thử ĐẠT; CPS 4.472 đ/việc (16,3× hoá đơn), 978 việc thành công; điền bảng A1–A4.
- CP2: 9 kịch bản B1; B2 cặp 6.543 đ (+46,3%) và xếp hạng làm lại/xem lại/lương; B3 giới hạn 2 lần rẻ nhất 6.901.220 đ; B4 xem lại 100% 11.743 đ = 0,98×.
- CP3: rà 20 ca, giữ hai bộ nhãn độc lập của Minh và Dũng (đồng thuận 20/20), viết quy tắc ca dễ lẫn, hoàn thiện bảng khắc phục 5 ca đủ 5 loại.
- CP4: tỉ lệ mở lại 4,25% (51/1.200) và 3,97% (39/982); thêm D1 vào `lab13.py`, kiểm tra chéo 1.251/3.103/1.000/300/299; power 0,64 ở mức 5 điểm.
- CP5: hoàn tất `chi_so.md` (3 chỉ số + 2 bổ sung, 10 event có `trace_id`, 3 rủi ro); điền mục 4 và đề xuất Go có điều kiện trong hồ sơ.

### Bằng chứng

- Các commit `48cb5ee`, `c5607dc`, `e77669d`, `7ac96b7`, `33f7333`; `git notes` mô tả từng commit.
- Các file `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/pilot_plan.yaml`, `report/team/2A202603546_BuiTheAnh.md`.

## NguyenTuanDung-2A202603559

### Phần việc phụ trách

- Người gắn nhãn 2 kiêm giữ hồ sơ và điều phối Gate 2a (`report/team/ho_so_launch_v0.md`, `TEAM.md`, `report/team/phieu_cham.md`).
- Gắn nhãn độc lập 20 ca lỗi theo Google PAIR (CP3), rà soát luật dừng và ngưỡng an toàn (CP4), chốt hồ sơ 1 trang và đại diện bảo vệ Gate 2a (CP5).

### Đóng góp cụ thể

- Cập nhật `TEAM.md` và điền xuyên suốt 7 mục cùng đề xuất **Go có điều kiện** (kèm 4 điều kiện có vai trò và ngày kiểm tra) trong `report/team/ho_so_launch_v0.md`.
- Gắn nhãn độc lập 20/20 ca lỗi trong `report/team/bang_loi.md` (đạt đồng thuận 20/20 = 100% với Vũ Nguyễn Hoàng Minh).
- Rà soát số liệu chéo giữa `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, đảm bảo đủ nhãn `simulated` và không vi phạm quy tắc lab.

### Bằng chứng

- Các commit `0979c2c`, `1f2fe43`, `bdf0617`, `8f9c8e5` và commit chốt CP5 trên nhánh `main`.
- Các file `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`, `report/team/2A202603559_NguyenTuanDung.md`, `TEAM.md`.
