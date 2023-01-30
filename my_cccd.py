import re
from typing import List, Dict, Union, Any


def _remove_accents(input_str: str) -> str:
    """
    :rtype: remove vietnamese
    """
    s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
    s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
    s = ''
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s


def _add_to_result(label: str, text: str, pattern: str) -> dict:
    res = {
        "Label": label,
        "Text": text,
        "Pattern": pattern
    }
    return res


def handle_CCCD(text: str, list_area: list) -> list:
    pattern_loai_giay_to = "^C.N.C..C.C.NG.D.N$"
    pattern_so_CCCD = "((^(s.|so|.{1,3}no).+.[^<<]\d)|\b\d{12}\b)"
    pattern_ho_va_ten = "(h..v..t.n|full|full.name)"
    pattern_ngay_sinh = "^(ng.y.sinh|date.of.b)(.+)$"
    pattern_gioi_tinh = "(((g..i.t.nh|sex)(.+))(qu.c.t.ch)|Nationality)(.+)"
    pattern_que_quan = "(qu..qu.n|place.of.origin).+(:|\s{2,3})(.+)?"
    pattern_noi_thuong_tru = "(n.i.th..ng.tr.|place.of.residence).*(:|\s{2,3})"
    pattern_co_gia_tri_den = "(c..gi..tr.).+:.+(\s{2,3})"
    pattern_dac_diem_nhan_dang = "(..c..i.m.nh.n.d.ng|personal|identification)"
    pattern_ngay_lam_CCCD = "(ng.y.[^sinh]|month|year).+"
    pattern_chuc_vu = "(C.C|TR..NG|C.NH).[A-Z]+"
    pattern_nguoi_ky = "[A-Z0-9]+<<\d"

    list_res: List[Dict[str, Union[str, Any]]] = []

    lines = text.split("\n")

    for i, line in enumerate(lines):
        line_remove = _remove_accents(line)
        if re.search(pattern_loai_giay_to, line_remove, re.IGNORECASE):
            list_res.append(_add_to_result("loai_giay_to", line, pattern_loai_giay_to))
            continue
        if re.search(pattern_so_CCCD, line_remove, re.IGNORECASE):
            list_res.append(_add_to_result("so_CCCD", line, pattern_so_CCCD))
            continue
        if re.search(pattern_ho_va_ten, line_remove, re.IGNORECASE):
            list_res.append(_add_to_result("ho_va_ten", lines[i+1], pattern_ho_va_ten))
            continue
        if re.search(pattern_ngay_sinh, line_remove, re.IGNORECASE):
            list_res.append(_add_to_result("ngay_sinh", line, pattern_ngay_sinh))
            continue
        if re.search(pattern_gioi_tinh, line_remove, re.IGNORECASE):
            list_res.append(_add_to_result("gioi_tinh", line, pattern_gioi_tinh))
            continue
        if re.search(pattern_que_quan, line_remove, re.IGNORECASE):
            list_res.append(_add_to_result("que_quan", line, pattern_que_quan))
            continue
        if re.search(pattern_noi_thuong_tru, line_remove, re.IGNORECASE):
            list_res.append(_add_to_result("noi_thuong_tru", line, pattern_noi_thuong_tru))
            continue
        if re.search(pattern_co_gia_tri_den, line_remove, re.IGNORECASE):
            list_res.append(_add_to_result("co_gia_tri_den", line, pattern_co_gia_tri_den))
            continue
        if re.search(pattern_dac_diem_nhan_dang, line_remove, re.IGNORECASE):
            list_res.append(_add_to_result("dac_diem_nhan_dang", line, pattern_dac_diem_nhan_dang))
            continue
        if re.search(pattern_ngay_lam_CCCD, line_remove, re.IGNORECASE):
            list_res.append(_add_to_result("ngay_lam_CCCD", line, pattern_ngay_lam_CCCD))
            continue
        if re.search(pattern_chuc_vu, line_remove, re.IGNORECASE):
            list_res.append(_add_to_result("chuc_vu", line, pattern_chuc_vu))
            continue
        if re.search(pattern_nguoi_ky, line_remove, re.IGNORECASE):
            list_res.append(_add_to_result("nguoi_ky", line, pattern_nguoi_ky))
            continue

    return list_res
