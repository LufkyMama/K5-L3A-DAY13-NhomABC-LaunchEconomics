"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng / tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
                so_yeu_cau=len(reqs))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print(f'{"gap_lan":12s} {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:>14,.1f}')

    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print('\nA3 · Tách theo loại yêu cầu')
    print(f'{"loai":10s} {"so_yc":>7s} {"ty_le_ok":>9s} {"lan_chay/yc":>12s} {"cps":>12s} {"so_voi_12000":>14s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        so_lan_chay = sub['so_lan_chay'].sum() / len(sub)
        print(f'{loai:10s} {len(sub):7d} {kq["thanh_cong"] / len(sub):9.1%} '
              f'{so_lan_chay:12.2f} {kq["cps"]:12,.0f} {kq["cps"] / BASELINE:13.2f}x')

    # Tỉ lệ ok theo từng lần thử, để trả lời "chạy lại có giúp không"
    theo_lan = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                .assign(ok=lambda d: (d['status'] == 'ok').astype(float))
                .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('\nTỉ lệ ok theo lần thử (A3)')
    print(theo_lan.round(3).to_string())

    # TODO CP1 · Nhiệm vụ A4: chi phí cố định cho phạm vi noi_dia + hang_nang.
    print('\nA4 · Chi phí cố định (noi_dia + hang_nang)')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    # Quy mô đầy đủ: 45.000 yêu cầu/tháng × tỉ lệ thành công của mẫu (900/1.200)
    ty_le_thanh_cong = kq_pv['thanh_cong'] / len(reqs)
    for nhan, khoi_luong in [('45.000 yêu cầu/tháng', 45_000),
                             ('Một nửa khối lượng', 22_500)]:
        thanh_cong_thang = khoi_luong * ty_le_thanh_cong
        co_dinh = CHI_PHI_CO_DINH / thanh_cong_thang
        cps = kq_pv['cps'] + co_dinh
        print(f'{nhan:24s} thanh_cong/thang={thanh_cong_thang:9,.0f} '
              f'co_dinh={co_dinh:7,.0f} cps={cps:8,.0f} so_voi_12000={cps / BASELINE:5.2f}x')

    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    print('\nB1 · Đổi từng yếu tố')
    goc = ket_qua['cps']
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    print(f'{"Gốc (A2)":28s} {goc:10,.0f}')
    thay_doi = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        thay_doi[ten] = (cps / goc - 1) * 100
        print(f'{ten:28s} {cps:10,.0f} {thay_doi[ten]:+7.1f}%')

    print('\nB2 · Đổi một cặp và xếp hạng')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'{"Giá token gấp đôi + xem lại gấp đôi":40s} {cap:10,.0f} {(cap / goc - 1) * 100:+7.1f}%')
    xep_hang = {
        'Số ca làm lại': thay_doi['Làm lại gấp đôi'],
        'Tỉ lệ xem lại': thay_doi['Xem lại gấp đôi'],
        'Lương nhân viên': thay_doi['Lương tăng 25%'],
    }
    for hang, (ten, phan_tram) in enumerate(sorted(xep_hang.items(), key=lambda x: -x[1]), 1):
        print(f'  {hang}. {ten:20s} {phan_tram:+.1f}%')

    print('\nB3 · Giới hạn chạy lại')
    print(f'{"Giới hạn":10s} {"Tổng trợ lý":>12s} {"Không thành công":>17s} {"Cả hệ thống":>12s} {"CPS":>9s}')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_thanh_cong = len(reqs) - kq['thanh_cong']
        ca_he_thong = kq['tong'] + BASELINE * khong_thanh_cong
        print(f'{k} lần     {kq["tong"]:12,.0f} {khong_thanh_cong:17d} '
              f'{ca_he_thong:12,.0f} {kq["cps"]:9,.0f}')

    print('\nB4 · Nếu phải xem lại tất cả (noi_dia + hang_nang)')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pv)
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    so_co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    token_tool = kq_pv['token'] + kq_pv['tool']
    xem_lai_100 = so_co_ok * 5 * LUONG_PHUT
    lam_lai_9 = so_lam_lai * 9 * LUONG_PHUT
    tong_100 = token_tool + xem_lai_100 + lam_lai_9
    cps_100 = tong_100 / kq_pv['thanh_cong']
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    lam_lai_tb = so_lam_lai * phut_lam_lai_tb * LUONG_PHUT
    tong_tb = token_tool + xem_lai_100 + lam_lai_tb
    cps_tb = tong_tb / kq_pv['thanh_cong']
    hoa_von_9 = (BASELINE * kq_pv['thanh_cong'] - token_tool - lam_lai_9) / (so_co_ok * LUONG_PHUT)
    hoa_von_tb = (BASELINE * kq_pv['thanh_cong'] - token_tool - lam_lai_tb) / (so_co_ok * LUONG_PHUT)
    print(f'Xem lại 100%, làm lại 9 phút: {cps_100:,.0f} đ = {cps_100 / BASELINE:.2f}x của 12.000 đ')
    print(f'Xem lại 100%, làm lại {phut_lam_lai_tb:.1f} phút: {cps_tb:,.0f} đ = {cps_tb / BASELINE:.2f}x của 12.000 đ')
    print(f'Hoà vốn: xem lại <= {hoa_von_9:.1f} phút (làm lại 9 phút) hoặc <= {hoa_von_tb:.1f} phút (làm lại {phut_lam_lai_tb:.1f} phút)')
    print(f'Chi tiết: {so_co_ok} yêu cầu có lần ok × 5 phút = {xem_lai_100:,.0f} đ; '
          f'{so_lam_lai} ca làm lại; token+tool = {token_tool:,.0f} đ; tổng = {tong_100:,.0f} đ')

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
