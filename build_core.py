# -*- coding: utf-8 -*-
"""
Core Question Banks for KNTT Chemistry Platform
"""
import json
import os
import sys

target_dir = r"C:\Users\admin\.gemini\antigravity\scratch\hoa-hoc-11-chuong-3"
if target_dir not in sys.path:
    sys.path.append(target_dir)

from build_kntt_data import GRADES_CONFIG
from build_full_chemistry import get_b8_questions, get_b9_questions, get_b10_questions, get_b11_questions
from build_all_grades import create_exercise_set

print("Loading raw questions for Chapter 3...")
b8_raw = get_b8_questions()
b9_raw = get_b9_questions()
b10_raw = get_b10_questions()
b11_raw = get_b11_questions()

# Chapter 3 Review Data
c3_rev_mcq = [
    ("Hợp chất hữu cơ là hợp chất của:", ["Nguyên tố carbon (trừ một số chất vô cơ như CO, CO2, muối carbonate...)", "Mọi nguyên tố trong bảng tuần hoàn", "Chỉ gồm hydrogen và oxygen", "Các kim loại kiềm"], 0, "Định nghĩa hợp chất hữu cơ theo SGK Hóa 11 Kết nối tri thức."),
    ("Dãy chất nào sau đây đều thuộc loại hydrocarbon?", ["CH4, C2H4, C3H8, C6H6", "CH3Cl, C2H5OH, CH3COOH", "CO2, CH4, C2H6", "C2H5OH, C3H6, C4H10"], 0, "CH4, C2H4, C3H8, C6H6 chỉ chứa C và H nên là hydrocarbon."),
    ("Nhóm chức -OH và nhóm chức -COOH lần lượt đặc trưng cho loại hợp chất nào?", ["Alcohol và Carboxylic acid", "Aldehyde và Ketone", "Ester và Amine", "Acid và Aldehyde"], 0, "-OH là alcohol, -COOH là carboxylic acid."),
    ("Phương pháp nào dùng để tách hai chất lỏng tan lẫn vào nhau nhưng có nhiệt độ sôi khác nhau?", ["Chiết lỏng - lỏng", "Chưng cất", "Kết tinh lại", "Lọc"], 1, "Chưng cất dùng để tách các chất lỏng có nhiệt độ sôi khác nhau."),
    ("Phương pháp dùng để tinh chế chất rắn dựa vào độ tan thay đổi theo nhiệt độ là:", ["Chưng cất", "Chiết", "Kết tinh", "Sắc kí"], 2, "Kết tinh dùng để tinh chế chất rắn."),
    ("Để tách tinh dầu bưởi từ vỏ bưởi trong thực tế, phương pháp tốt nhất là:", ["Chưng cất lôi cuốn hơi nước", "Kết tinh", "Sắc kí", "Điện phân"], 0, "Tinh dầu dễ bay hơi theo hơi nước nên dùng chưng cất lôi cuốn hơi nước."),
    ("Dụng cụ chính dùng trong phương pháp chiết lỏng - lỏng là:", ["Bình cầu chưng cất", "Phễu chiết", "Ống sinh hàn", "Bình tam giác"], 1, "Phễu chiết (có khóa xả)."),
    ("Trên phổ khối lượng MS, đại lượng m/z của pic ion phân tử [M+] cho biết:", ["Số nguyên tử C", "Phân tử khối M của hợp chất", "Khối lượng mẫu đo", "Nhiệt độ nóng chảy"], 1, "m/z của [M+] = phân tử khối M."),
    ("Chất X có công thức đơn giản nhất là CH2O và phân tử khối M = 60. CTPT của X là:", ["CH2O", "C2H4O2", "C3H6O3", "C4H8O4"], 1, "(CH2O)n có M = 30n = 60 => n = 2 => C2H4O2."),
    ("Tỉ lệ số mol nC : nH : nO khi đốt cháy chất Y là 1 : 2 : 1. Công thức đơn giản nhất của Y là:", ["CH2O", "C2H4O2", "C3H6O3", "CHO"], 0, "Tỉ lệ 1:2:1 => CTĐGN là CH2O."),
    ("Theo thuyết cấu tạo hóa học, trong hợp chất hữu cơ nguyên tử carbon luôn có hóa trị mấy?", ["I", "II", "III", "IV"], 3, "Carbon luôn có hóa trị IV."),
    ("Hiện tượng các chất có cùng công thức phân tử nhưng khác nhau về cấu tạo hóa học gọi là:", ["Đồng đẳng", "Đồng vị", "Đồng phân", "Thù hình"], 2, "Định nghĩa hiện tượng đồng phân."),
    ("Cặp chất nào sau đây là đồng phân của nhau?", ["C2H5OH và CH3OCH3", "CH4 và C2H6", "CH3COOH và C2H5OH", "C2H4 và C3H6"], 0, "Ethanol và dimethyl ether cùng có CTPT là C2H6O."),
    ("Chất nào sau đây có đồng phân hình học cis - trans?", ["CH2=CH-CH3", "CH3-CH=CH-CH3", "CH2=CH2", "CH2=C(CH3)2"], 1, "But-2-ene có đồng phân cis và trans."),
    ("Phương pháp sắc kí cột dựa trên nguyên tắc nào?", ["Sự khác nhau về độ sôi", "Sự khác nhau về độ hòa tan và khả năng hấp phụ trên pha tĩnh", "Sự khác nhau về kích thước phân tử", "Sự khác nhau về từ tính"], 1, "Nguyên tắc sắc kí cột."),
    ("Trong thí nghiệm phân tích định tính C và H, vai trò của CuO là:", ["Chất xúc tác", "Chất oxi hóa", "Chất khử", "Chất hút ẩm"], 1, "CuO đóng vai trò là chất oxi hóa."),
    ("Chất dùng để nhận biết khí CO2 sinh ra từ phản ứng định tính hợp chất hữu cơ là:", ["CuSO4 khan", "Dung dịch Ca(OH)2", "Quỳ tím", "Dung dịch AgNO3"], 1, "Ca(OH)2 làm đục nước vôi trong."),
    ("Butane (C4H10) có bao nhiêu đồng phân cấu tạo?", ["1", "2", "3", "4"], 1, "Butane có 2 đồng phân: butane và isobutane."),
    ("Khí nào sau đây có thể dùng phương pháp chưng cất để tách ra khỏi hỗn hợp không?", ["Không, chưng cất dùng cho chất lỏng", "Có, chưng cất mọi chất", "Chỉ chưng cất chất rắn", "Không có quy định"], 0, "Chưng cất áp dụng cho các chất lỏng có nhiệt độ sôi khác nhau."),
    ("Hợp chất CH3-CHO chứa nhóm chức nào?", ["-OH", "-COOH", "-CHO", "-COO-"], 2, "Nhóm -CHO (aldehyde)."),
    ("Tổng số liên kết hóa trị của một nguyên tử carbon trong hợp chất hữu cơ là:", ["2", "3", "4", "5"], 2, "Carbon có hóa trị IV nên luôn tạo 4 liên kết hóa trị.")
]
c3_rev_tf = [
    ("Câu 22: Xem xét các kiến thức cốt lõi về hợp chất hữu cơ trong Chương III:", [
        ("Mọi hợp chất chứa nguyên tố carbon đều là hợp chất hữu cơ.", False),
        ("Liên kết hóa học trong phân tử hợp chất hữu cơ chủ yếu là liên kết cộng hóa trị.", True),
        ("Phương pháp phổ khối lượng MS dùng để xác định phân tử khối thông qua pic ion phân tử [M+].", True),
        ("Hai chất có cùng công thức đơn giản nhất thì luôn có cùng công thức phân tử.", False)
    ], "Ý 1 sai vì CO, CO2, muối carbonate là vô cơ. Ý 4 sai vì ví dụ C2H2 và C6H6 có cùng CTĐGN là CH nhưng CTPT khác nhau."),
    ("Câu 23: Về các phương pháp tách biệt và tinh chế hợp chất hữu cơ:", [
        ("Chưng cất thường dùng để tách hai chất lỏng không tan vào nhau.", False),
        ("Chiết lỏng - lỏng dùng phễu chiết để tách hai chất lỏng không trộn lẫn.", True),
        ("Chưng cất lôi cuốn hơi nước áp dụng thích hợp để tách tinh dầu thực vật.", True),
        ("Kết tinh lại dựa trên nguyên tắc độ tan của chất rắn tăng khi nhiệt độ tăng.", True)
    ], "Ý 1 sai vì chưng cất dùng cho hai chất lỏng tan lẫn vào nhau nhưng có nhiệt độ sôi khác nhau."),
    ("Câu 24: Về thuyết cấu tạo hóa học và hiện tượng đồng phân:", [
        ("Trong phân tử hợp chất hữu cơ, các nguyên tử carbon có thể liên kết trực tiếp với nhau tạo mạch hở hoặc mạch vòng.", True),
        ("Các chất là đồng phân của nhau luôn có cùng công thức phân tử và cùng tính chất hóa học.", False),
        ("Đồng phân hình học cis - trans xuất hiện khi mỗi nguyên tử C ở nối đôi liên kết với hai nhóm thế khác nhau.", True),
        ("Ethanol (C2H5OH) và dimethyl ether (CH3OCH3) là hai chất đồng đẳng của nhau.", False)
    ], "Ý 2 sai vì đồng phân khác nhau về cấu tạo nên tính chất khác nhau. Ý 4 sai vì đây là hai chất đồng phân."),
    ("Câu 25: Về phương pháp xác định công thức phân tử hợp chất hữu cơ:", [
        ("Đốt cháy hợp chất hữu cơ sinh ra CO2 và H2O chứng tỏ hợp chất chứa C, H và chắc chắn không có O.", False),
        ("Từ tỉ lệ khối lượng %C, %H, %O ta luôn xác định được công thức đơn giản nhất của hợp chất.", True),
        ("Giá trị m/z của pic ion phân tử [M+] trên phổ MS luôn bằng số nguyên tử H trong phân tử.", False),
        ("Công thức phân tử luôn là bội số nguyên dương của công thức đơn giản nhất: CTPT = (CTĐGN)n với n ≥ 1.", True)
    ], "Ý 1 sai vì có thể có O. Ý 3 sai vì m/z của [M+] bằng phân tử khối M.")
]
c3_rev_short = [
    ("Câu 26: Cho các chất: CH4, CO2, C2H5OH, CaCO3, C6H6, NaHCO3, CH3COOH. Có bao nhiêu chất là hợp chất hữu cơ?", "4", "4 chất: CH4, C2H5OH, C6H6, CH3COOH."),
    ("Câu 27: Hợp chất X có công thức đơn giản nhất là CH2O và phân tử khối M = 60. Số nguyên tử Carbon trong một phân tử X là bao nhiêu?", "2", "(CH2O)n = 60 => n = 2 => C2H4O2 có 2 nguyên tử C."),
    ("Câu 28: Khí butane (C4H10) có bao nhiêu đồng phân cấu tạo?", "2", "2 đồng phân: butane và isobutane."),
    ("Câu 29: Phân tử khối của acetic acid (CH3COOH) bằng bao nhiêu amu?", "60", "M = 12*2 + 4 + 16*2 = 60 amu."),
    ("Câu 30: Đốt cháy hoàn toàn 0,1 mol một hydrocarbon thu được 0,3 mol CO2. Số nguyên tử Carbon trong hydrocarbon này là bao nhiêu?", "3", "Số C = nCO2 / n = 0,3 / 0,1 = 3."),
    ("Câu 31: Alkene but-2-ene (CH3-CH=CH-CH3) có bao nhiêu đồng phân hình học?", "2", "2 đồng phân hình học: cis-but-2-ene và trans-but-2-ene.")
]
c3_rev_essay = [
    "Tổng kết định nghĩa hợp chất hữu cơ, phân loại hydrocarbon và dẫn xuất hydrocarbon trong SGK KNTT.",
    "So sánh đặc điểm liên kết và độ bền nhiệt của hợp chất hữu cơ với hợp chất vô cơ.",
    "Nêu nguyên tắc và ứng dụng của 4 phương pháp tách biệt: Chưng cất, Chiết, Kết tinh và Sắc kí cột.",
    "Vì sao khi ngâm rượu thuốc hay hãm trà, người ta đã áp dụng phương pháp chiết lỏng - rắn?",
    "Trình bày phương pháp chưng cất lôi cuốn hơi nước để tách tinh dầu cam, sả trong thực tế đời sống.",
    "Nêu ý nghĩa của phổ khối lượng (MS) trong việc xác định phân tử khối của hợp chất hữu cơ.",
    "Phân biệt khái niệm công thức đơn giản nhất (CTĐGN) và công thức phân tử (CTPT). Nêu mối liên hệ giữa chúng.",
    "Đốt cháy hoàn toàn 3,0 gam một hợp chất hữu cơ X thu được 4,4 gam CO2 và 1,8 gam H2O. Xác định CTĐGN của X.",
    "Biết phân tử khối của chất X ở câu trên xác định qua phổ MS là 60 amu. Xác định CTPT của X.",
    "Trình bày 3 luận điểm cốt lõi của Thuyết cấu tạo hóa học Butlerov.",
    "Thế nào là hiện tượng đồng phân? Nêu các loại đồng phân cấu tạo thường gặp ở hợp chất hữu cơ.",
    "Viết công thức cấu tạo thu gọn của tất cả các đồng phân ứng với CTPT C4H10 và C5H12.",
    "Giải thích hiện tượng đồng phân hình học cis - trans của alkene. Cho ví dụ cụ thể với but-2-ene.",
    "Viết các đồng phân cấu tạo có cùng CTPT C3H8O và gọi tên theo danh pháp thay thế.",
    "So sánh nhiệt độ sôi của ethanol (C2H5OH) và dimethyl ether (CH3OCH3) và giải thích dựa vào liên kết hydrogen.",
    "Trình bày thí nghiệm định tính nguyên tố carbon và hydrogen trong hợp chất hữu cơ bằng CuO và CuSO4 khan.",
    "Nêu các ứng dụng to lớn của hóa học hữu cơ đối với đời sống, y dược phẩm, vật liệu polymer và nhiên liệu."
]

BANK = {
    "c3_b8": create_exercise_set("c3_b8", "Hợp chất hữu cơ và hóa học hữu cơ", b8_raw["mcq"], [(x[0], x[1], x[2]) for x in b8_raw["tf"]], [(x[0], x[1], x[2]) for x in b8_raw["short"]], b8_raw["essay"]),
    "c3_b9": create_exercise_set("c3_b9", "Phương pháp tách biệt và tinh chế", b9_raw["mcq"], [(x[0], x[1], x[2]) for x in b9_raw["tf"]], [(x[0], x[1], x[2]) for x in b9_raw["short"]], b9_raw["essay"]),
    "c3_b10": create_exercise_set("c3_b10", "Công thức phân tử hợp chất hữu cơ", b10_raw["mcq"], [(x[0], x[1], x[2]) for x in b10_raw["tf"]], [(x[0], x[1], x[2]) for x in b10_raw["short"]], b10_raw["essay"]),
    "c3_b11": create_exercise_set("c3_b11", "Cấu trúc phân tử hợp chất hữu cơ", b11_raw["mcq"], [(x[0], x[1], x[2]) for x in b11_raw["tf"]], [(x[0], x[1], x[2]) for x in b11_raw["short"]], b11_raw["essay"]),
    "c3_rev": create_exercise_set("c3_rev", "Bài tập cuối chương III", c3_rev_mcq, c3_rev_tf, c3_rev_short, c3_rev_essay),
}

print(f"Base banks successfully loaded: {len(BANK)} lessons.")
