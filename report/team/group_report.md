# Báo cáo nhóm · NhomABC · L3A

Thành viên và vai trò ghi trong [TEAM.md](../../TEAM.md).

## Mục tiêu và cách tiếp cận

Đánh giá chi phí, lỗi và khả năng thiết kế pilot có đối chứng cho trợ lý hoàn phí LogiX-VN. Số liệu đến từ 1.200 yêu cầu và 1.624 lượt chạy trong đợt thử giả lập.

## Kết quả A–E

| Phần | Kết quả chính |
| --- | --- |
| A · Chi phí | Ba phép thử A1 đạt. Chi phí 4.472 đ/việc thành công và 5.865 đ/yêu cầu khi tính cả xử lý thủ công [simulated]. |
| B · Độ nhạy | Làm lại là khoản nhạy nhất (+51,8% khi gấp đôi). Xem lại 100% có thể lên 12.415 đ/việc [simulated]. |
| C · Lỗi | Bảng có 20 ca và 5 biện pháp khắc phục. Việc gắn nhãn độc lập của cả hai người cần xác nhận từ bộ nhãn gốc. |
| D · Pilot | Chia theo nhân viên 20 + 20, mục tiêu 5.980 yêu cầu mỗi nhóm cho MDE +6 điểm phần trăm. Power khoảng 64% nếu tác động thật chỉ +5 điểm. |
| E · Gate 2a | Đợt chạy thử ghi nhận 82,83% đóng đúng hạn và không mở lại, 27,12% sửa hoặc bỏ gợi ý, 4,25% mở lại. Hồ sơ đề xuất Go có điều kiện. |

Bằng chứng nằm trong [bảng chi phí](bang_chi_phi.md), [bảng lỗi](bang_loi.md), [kế hoạch pilot](pilot_plan.yaml), [đặc tả chỉ số](chi_so.md) và [hồ sơ launch](ho_so_launch_v0.md).

## Khó khăn và cách xử lý

Chia theo cụm nhân viên thiếu lực thống kê cho +5 điểm, nên pilot chốt MDE +6 điểm và kiểm lại cỡ mẫu hiệu dụng nếu tải giữa nhân viên chênh lệch. Lần push CP4 ban đầu gặp lỗi kết nối GitHub cổng 443. Nhánh theo dõi hiện đã có commit CP4.

## Hạn chế và duyệt chéo

Đợt thử giả lập thiếu đối chứng, nên chỉ dùng để mô tả số quan sát và lập kế hoạch đo. Theo phiếu đã lưu, NhomABC chấm Soopi 30/30 và đề xuất Go có điều kiện. Phiếu ghi phản hồi của Soopi về thời lượng đo ở pha 50% và chi phí xử lý thủ công. Điểm hội đồng chấm NhomABC chưa có trong hồ sơ này. [Phiếu chấm](phieu_cham.md)
