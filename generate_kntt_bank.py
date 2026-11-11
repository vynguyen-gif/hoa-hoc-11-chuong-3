# -*- coding: utf-8 -*-
"""
Generate complete KNTT Chemistry 11 Questions Bank and update index.html
"""
import json
import os
import re

# 1. Lesson question definitions
from build_full_chemistry import get_b8_questions, get_b9_questions, get_b10_questions, get_b11_questions

def build_bank_item(key, raw_data):
    mcq = [
        {
            "id": f"{key}_c{i+1}",
            "num": i + 1,
            "type": "mcq",
            "levelClass": "level-nb" if i < 7 else ("level-th" if i < 15 else "level-vd"),
            "levelName": "Nhận biết" if i < 7 else ("Thông hiểu" if i < 15 else "Vận dụng"),
            "title": f"Câu {i+1}: {item[0]}",
            "options": item[1],
            "correct": item[2],
            "explanation": item[3]
        }
        for i, item in enumerate(raw_data["mcq"])
    ]
    tf = [
        {
            "id": f"{key}_c{item[0]}",
            "num": item[0],
            "type": "tf",
            "levelClass": "level-th" if idx < 2 else "level-vd",
            "levelName": "Thông hiểu" if idx < 2 else "Vận dụng",
            "title": item[1],
            "statements": [{"text": s[0], "ans": s[1]} for s in item[2]],
            "explanation": item[3]
        }
        for idx, item in enumerate(raw_data["tf"])
    ]
    short = [
        {
            "id": f"{key}_c{item[0]}",
            "num": item[0],
            "type": "short",
            "levelClass": "level-vd",
            "levelName": "Vận dụng",
            "title": item[1],
            "correctText": item[2],
            "explanation": item[3]
        }
        for item in raw_data["short"]
    ]
    essay = [
        {
            "id": f"{key}_c{32 + i}",
            "num": 32 + i,
            "type": "essay",
            "levelClass": "level-th" if i < 5 else ("level-vd" if i < 12 else "level-vdc"),
            "levelName": "Thông hiểu" if i < 5 else ("Vận dụng" if i < 12 else "Vận dụng cao"),
            "title": f"Câu {32 + i}: {title}",
            "explanation": f"Hướng dẫn giải chi tiết cho Câu {32 + i} (Chuẩn SGK Hóa học 11 Kết nối tri thức):\n- Nắm vững kiến thức trọng tâm SGK Hóa học 11 chương trình mới.\n- Trình bày rõ ràng định nghĩa, phương trình hóa học và công thức tính toán liên quan."
        }
        for i, title in enumerate(raw_data["essay"])
    ]
    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

def get_c3_rev_data():
    mcq = [
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

    tf = [
      (22, "Câu 22: Xem xét các kiến thức cốt lõi về hợp chất hữu cơ trong Chương III:", [
        ("Mọi hợp chất chứa nguyên tố carbon đều là hợp chất hữu cơ.", False),
        ("Liên kết hóa học trong phân tử hợp chất hữu cơ chủ yếu là liên kết cộng hóa trị.", True),
        ("Phương pháp phổ khối lượng MS dùng để xác định phân tử khối thông qua pic ion phân tử [M+].", True),
        ("Hai chất có cùng công thức đơn giản nhất thì luôn có cùng công thức phân tử.", False)
      ], "Ý 1 sai vì CO, CO2, muối carbonate là vô cơ. Ý 4 sai vì ví dụ C2H2 và C6H6 có cùng CTĐGN là CH nhưng CTPT khác nhau."),

      (23, "Câu 23: Về các phương pháp tách biệt và tinh chế hợp chất hữu cơ:", [
        ("Chưng cất thường dùng để tách hai chất lỏng không tan vào nhau.", False),
        ("Chiết lỏng - lỏng dùng phễu chiết để tách hai chất lỏng không trộn lẫn.", True),
        ("Chưng cất lôi cuốn hơi nước áp dụng thích hợp để tách tinh dầu thực vật.", True),
        ("Kết tinh lại dựa trên nguyên tắc độ tan của chất rắn tăng khi nhiệt độ tăng.", True)
      ], "Ý 1 sai vì chưng cất dùng cho hai chất lỏng tan lẫn vào nhau nhưng có nhiệt độ sôi khác nhau."),

      (24, "Câu 24: Về thuyết cấu tạo hóa học và hiện tượng đồng phân:", [
        ("Trong phân tử hợp chất hữu cơ, các nguyên tử carbon có thể liên kết trực tiếp với nhau tạo mạch hở hoặc mạch vòng.", True),
        ("Các chất là đồng phân của nhau luôn có cùng công thức phân tử và cùng tính chất hóa học.", False),
        ("Đồng phân hình học cis - trans xuất hiện khi mỗi nguyên tử C ở nối đôi liên kết với hai nhóm thế khác nhau.", True),
        ("Ethanol (C2H5OH) và dimethyl ether (CH3OCH3) là hai chất đồng đẳng của nhau.", False)
      ], "Ý 2 sai vì đồng phân khác nhau về cấu tạo nên tính chất khác nhau. Ý 4 sai vì đây là hai chất đồng phân."),

      (25, "Câu 25: Về phương pháp xác định công thức phân tử hợp chất hữu cơ:", [
        ("Đốt cháy hợp chất hữu cơ sinh ra CO2 và H2O chứng tỏ hợp chất chứa C, H và chắc chắn không có O.", False),
        ("Từ tỉ lệ khối lượng %C, %H, %O ta luôn xác định được công thức đơn giản nhất của hợp chất.", True),
        ("Giá trị m/z của pic ion phân tử [M+] trên phổ MS luôn bằng số nguyên tử H trong phân tử.", False),
        ("Công thức phân tử luôn là bội số nguyên dương của công thức đơn giản nhất: CTPT = (CTĐGN)n với n ≥ 1.", True)
      ], "Ý 1 sai vì có thể có O. Ý 3 sai vì m/z của [M+] bằng phân tử khối M.")
    ]

    short = [
      (26, "Câu 26: Cho các chất: CH4, CO2, C2H5OH, CaCO3, C6H6, NaHCO3, CH3COOH. Có bao nhiêu chất là hợp chất hữu cơ?", "4", "4 chất: CH4, C2H5OH, C6H6, CH3COOH."),
      (27, "Câu 27: Hợp chất X có công thức đơn giản nhất là CH2O và phân tử khối M = 60. Số nguyên tử Carbon trong một phân tử X là bao nhiêu?", "2", "(CH2O)n = 60 => n = 2 => C2H4O2 có 2 nguyên tử C."),
      (28, "Câu 28: Khí butane (C4H10) có bao nhiêu đồng phân cấu tạo?", "2", "2 đồng phân: butane và isobutane."),
      (29, "Câu 29: Phân tử khối của acetic acid (CH3COOH) bằng bao nhiêu amu?", "60", "M = 12*2 + 4 + 16*2 = 60 amu."),
      (30, "Câu 30: Đốt cháy hoàn toàn 0,1 mol một hydrocarbon thu được 0,3 mol CO2. Số nguyên tử Carbon trong hydrocarbon này là bao nhiêu?", "3", "Số C = nCO2 / n = 0,3 / 0,1 = 3."),
      (31, "Câu 31: Alkene but-2-ene (CH3-CH=CH-CH3) có bao nhiêu đồng phân hình học?", "2", "2 đồng phân hình học: cis-but-2-ene và trans-but-2-ene.")
    ]

    essay = [
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

    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

print("Loading banks...")
raw_b8 = get_b8_questions()
raw_b9 = get_b9_questions()
raw_b10 = get_b10_questions()
raw_b11 = get_b11_questions()
raw_c3_rev = get_c3_rev_data()

BANK = {
    "c3_b8": build_bank_item("c3_b8", raw_b8),
    "c3_b9": build_bank_item("c3_b9", raw_b9),
    "c3_b10": build_bank_item("c3_b10", raw_b10),
    "c3_b11": build_bank_item("c3_b11", raw_b11),
    "c3_rev": build_bank_item("c3_rev", raw_c3_rev)
}

# Also generate topic-accurate banks for other chapters based on KNTT
def get_c1_b1_data():
    mcq = [
        ("Phản ứng thuận nghịch là phản ứng:", ["Xảy ra theo một chiều duy nhất", "Trong cùng điều kiện, xảy ra đồng thời theo hai chiều trái ngược nhau", "Chỉ xảy ra khi đun nóng", "Luôn giải phóng chất khí"], 1, "Định nghĩa phản ứng thuận nghịch trong SGK Hóa 11 KNTT."),
        ("Trạng thái cân bằng hóa học là trạng thái tại đó:", ["Phản ứng dừng lại hoàn toàn", "Tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch (v_t = v_n)", "Nồng độ chất phản ứng bằng nồng độ sản phẩm", "Các chất không va chạm vào nhau"], 1, "Cân bằng hóa học là cân bằng động, v_thuận = v_nghịch."),
        ("Biểu thức hằng số cân bằng Kc của phản ứng tổng quát aA + bB ⇌ cC + dD là:", ["([C]^c * [D]^d) / ([A]^a * [B]^b)", "([A]^a * [B]^b) / ([C]^c * [D]^d)", "([C] + [D]) / ([A] + [B])", "v_t / v_n"], 0, "Biểu thức chuẩn của hằng số cân bằng Kc."),
        ("Trong biểu thức tính hằng số cân bằng Kc, nồng độ của chất nào sau đây KHÔNG xuất hiện?", ["Chất khí", "Chất tan trong dung dịch", "Chất rắn nguyên chất", "Chất lỏng bay hơi"], 2, "Chất rắn nguyên chất có nồng độ không đổi nên không đưa vào biểu thức Kc."),
        ("Hằng số cân bằng Kc của một phản ứng xác định chỉ phụ thuộc vào yếu tố nào?", ["Áp suất", "Nồng độ", "Nhiệt độ", "Chất xúc tác"], 2, "Kc chỉ phụ thuộc vào bản chất phản ứng và nhiệt độ."),
        ("Chất xúc tác có tác dụng gì đối với một phản ứng thuận nghịch đang ở trạng thái cân bằng?", ["Làm cân bằng chuyển dịch theo chiều thuận", "Làm cân bằng chuyển dịch theo chiều nghịch", "Làm tăng tốc độ đạt tới trạng thái cân bằng, không làm chuyển dịch cân bằng", "Làm thay đổi giá trị Kc"], 2, "Xúc tác chỉ làm tăng đồng thời tốc độ thuận và nghịch, giúp hệ nhanh đạt cân bằng."),
        ("Theo nguyên lí Le Chatelier, khi tăng nhiệt độ của hệ cân bằng, cân bằng sẽ chuyển dịch theo chiều:", ["Tỏa nhiệt (ΔH < 0)", "Thu nhiệt (ΔH > 0)", "Không chuyển dịch", "Chiều làm tăng nhiệt độ thêm"], 1, "Tăng nhiệt độ -> chuyển dịch theo chiều thu nhiệt (ΔH > 0) để hạ nhiệt độ."),
        ("Cho phản ứng: N2(k) + 3H2(k) ⇌ 2NH3(k) (ΔrHo < 0). Để tăng hiệu suất tạo NH3, ta nên:", ["Tăng nhiệt độ và giảm áp suất", "Giảm nhiệt độ và tăng áp suất", "Tăng nhiệt độ và tăng áp suất", "Giảm nhiệt độ và giảm áp suất"], 1, "Chiều thuận tỏa nhiệt và giảm mol khí -> giảm nhiệt độ và tăng áp suất."),
        ("Cho cân bằng: CaCO3(r) ⇌ CaO(r) + CO2(k) (ΔrHo > 0). Để tăng lượng CaO tạo thành, biện pháp nào sau đây đúng?", ["Hạ nhiệt độ lò nung", "Tăng nhiệt độ lò nung", "Bơm thêm khí CO2 vào lò", "Tăng áp suất chung"], 1, "Chiều thuận thu nhiệt nên tăng nhiệt độ làm cân bằng chuyển dịch theo chiều thuận tạo thêm CaO."),
        ("Yếu tố áp suất chỉ làm chuyển dịch cân bằng của các phản ứng có:", ["Chất rắn tham gia", "Chất lỏng tham gia", "Chất khí tham gia và có sự chênh lệch tổng số mol khí ở hai vế", "Nhiệt độ phòng"], 2, "Áp suất chỉ ảnh hưởng khi có chất khí và tổng số mol khí hai vế khác nhau."),
        ("Cho cân bằng: H2(k) + I2(k) ⇌ 2HI(k). Khi tăng áp suất của hệ, cân bằng chuyển dịch như thế nào?", ["Chuyển dịch theo chiều thuận", "Chuyển dịch theo chiều nghịch", "Không chuyển dịch", "Dừng phản ứng"], 2, "Tổng số mol khí vế trái (1+1=2) bằng vế phải (2) nên áp suất không làm chuyển dịch cân bằng."),
        ("Một phản ứng có Kc rất lớn (Kc >> 1) cho thấy:", ["Hiệu suất chuyển hóa thành sản phẩm rất cao", "Phản ứng hầu như không xảy ra", "Tốc độ phản ứng nghịch rất lớn", "Phản ứng thu nhiệt mạnh"], 0, "Kc rất lớn nghĩa là ở trạng thái cân bằng nồng độ sản phẩm chiếm ưu thế tuyệt đối."),
        ("Cho cân bằng: 2SO2(k) + O2(k) ⇌ 2SO3(k) (ΔrHo < 0). Biện pháp nào làm cân bằng chuyển dịch theo chiều thuận?", ["Tăng nhiệt độ", "Giảm nồng độ O2", "Tăng áp suất chung của hệ", "Giảm nồng độ SO2"], 2, "Tăng áp suất làm chuyển dịch theo chiều giảm mol khí (từ 3 mol xuống 2 mol)."),
        ("Giá trị hằng số cân bằng Kc của phản ứng thuận nghịch N2 + 3H2 ⇌ 2NH3 là 0,5. Hằng số cân bằng của phản ứng nghịch 2NH3 ⇌ N2 + 3H2 ở cùng nhiệt độ là:", ["0,5", "2,0", "1,0", "0,25"], 1, "K_nghịch = 1 / K_thuận = 1 / 0,5 = 2,0."),
        ("Thêm một chất phản ứng vào hệ cân bằng sẽ làm:", ["Cân bằng chuyển dịch theo chiều tiêu hao chất đó (chiều thuận)", "Cân bằng chuyển dịch theo chiều tạo thêm chất đó", "Không ảnh hưởng", "Kc thay đổi"], 0, "Thêm chất -> chuyển dịch theo chiều làm giảm lượng chất đó."),
        ("Cho cân bằng trong bình kín: CO(k) + H2O(k) ⇌ CO2(k) + H2(k). Thêm khí Ar (khí trơ) vào bình ở thể tích không đổi thì:", ["Cân bằng chuyển dịch theo chiều thuận", "Cân bằng chuyển dịch theo chiều nghịch", "Cân bằng không chuyển dịch", "Kc tăng lên"], 2, "Khí trơ thêm vào ở V không đổi không làm thay đổi nồng độ/áp suất riêng phần của các chất phản ứng nên cân bằng không đổi."),
        ("Phát biểu nào sau đây đúng về trạng thái cân bằng hóa học?", ["Cân bằng hóa học là cân bằng tĩnh", "Cân bằng hóa học là cân bằng động", "Các chất không còn phản ứng nữa", "Phản ứng diễn ra một chiều"], 1, "Cân bằng hóa học là cân bằng động vì phản ứng thuận và nghịch vẫn tiếp tục diễn ra với tốc độ bằng nhau."),
        ("Cho cân bằng: PCl5(k) ⇌ PCl3(k) + Cl2(k) (ΔrHo > 0). Khi giảm thể tích bình phản ứng (tăng áp suất), cân bằng chuyển dịch theo chiều nào?", ["Chiều nghịch", "Chiều thuận", "Không chuyển dịch", "Dừng lại"], 0, "Tăng áp suất chuyển dịch theo chiều giảm mol khí (từ 2 mol về 1 mol, tức chiều nghịch)."),
        ("Khi một hệ phản ứng thuận nghịch đạt cân bằng, tỉ lệ nồng độ mol sản phẩm so với chất phản ứng:", ["Luôn bằng 1", "Là một hằng số xác định ở nhiệt độ xác định", "Bằng 0", "Thay đổi liên tục theo thời gian"], 1, "Đó chính là hằng số cân bằng Kc không đổi ở nhiệt độ xác định."),
        ("Cho phản ứng N2O4(k, không màu) ⇌ 2NO2(k, nâu đỏ) có ΔrHo > 0. Khi ngâm bình phản ứng vào nước đá lạnh, màu nâu đỏ của bình sẽ:", ["Đậm dần lên", "Nhạt dần đi", "Không thay đổi", "Chuyển sang màu xanh"], 1, "Làm lạnh -> cân bằng chuyển dịch theo chiều tỏa nhiệt (chiều nghịch tạo N2O4 không màu) -> màu nhạt dần."),
        ("Ý nghĩa thực tiễn quan trọng của việc nghiên cứu chuyển dịch cân bằng hóa học trong công nghiệp là:", ["Làm tăng giá thành sản xuất", "Điều khiển các điều kiện (nhiệt độ, áp suất, nồng độ) để đạt hiệu suất chuyển hóa cao nhất", "Dừng phản ứng khi cần", "Hạn chế dùng chất xúc tác"], 1, "Mục đích tối ưu hóa năng suất và hiệu suất trong công nghiệp hóa học.")
    ]
    tf = [
      (22, "Câu 22: Xem xét các nhận định về bản chất của cân bằng hóa học:", [
        ("Cân bằng hóa học là cân bằng động vì phản ứng thuận và phản ứng nghịch vẫn tiếp tục xảy ra.", True),
        ("Tại thời điểm cân bằng, nồng độ của chất tham gia và chất sản phẩm luôn luôn bằng nhau.", False),
        ("Hằng số cân bằng Kc chỉ thay đổi khi nhiệt độ của hệ phản ứng thay đổi.", True),
        ("Chất xúc tác làm thay đổi giá trị hằng số cân bằng Kc của phản ứng.", False)
      ], "Ý 2 sai vì nồng độ không đổi chứ không nhất thiết phải bằng nhau. Ý 4 sai vì chất xúc tác không làm thay đổi Kc."),

      (23, "Câu 23: Về nguyên lí chuyển dịch cân bằng Le Chatelier:", [
        ("Khi tăng nhiệt độ, cân bằng luôn chuyển dịch theo chiều phản ứng tỏa nhiệt.", False),
        ("Khi tăng áp suất chung, cân bằng chuyển dịch theo chiều làm giảm tổng số mol chất khí.", True),
        ("Việc lấy bớt sản phẩm ra khỏi hệ phản ứng sẽ giúp cân bằng chuyển dịch theo chiều thuận.", True),
        ("Đối với phản ứng có tổng số mol khí ở hai vế bằng nhau, áp suất không làm chuyển dịch cân bằng.", True)
      ], "Ý 1 sai vì tăng nhiệt độ chuyển dịch theo chiều thu nhiệt (ΔH > 0)."),

      (24, "Câu 24: Về phản ứng tổng hợp ammonia: N2(k) + 3H2(k) ⇌ 2NH3(k) (ΔrHo = -92 kJ):", [
        ("Chiều thuận của phản ứng là quá trình tỏa nhiệt.", True),
        ("Để tăng hiệu suất tổng hợp NH3, người ta cần thực hiện ở áp suất rất cao.", True),
        ("Trong thực tế công nghiệp, người ta hạ nhiệt độ xuống gần 0°C để cân bằng chuyển dịch hoàn toàn sang NH3.", False),
        ("Bột sắt (Fe) được dùng làm chất xúc tác để hệ nhanh đạt trạng thái cân bằng.", True)
      ], "Ý 3 sai vì ở nhiệt độ quá thấp tốc độ phản ứng quá chậm, trong thực tế dùng nhiệt độ tối ưu khoảng 400 - 450°C."),

      (25, "Câu 25: Về biểu thức hằng số cân bằng Kc:", [
        ("Nồng độ của chất rắn nguyên chất không được đưa vào biểu thức tính Kc.", True),
        ("Biểu thức Kc của phản ứng CaCO3(r) ⇌ CaO(r) + CO2(k) đơn giản là Kc = [CO2].", True),
        ("Giá trị Kc càng nhỏ chứng tỏ phản ứng thuận diễn ra càng triệt để.", False),
        ("Đơn vị của Kc phụ thuộc vào phương trình hóa học cụ thể của phản ứng.", True)
      ], "Ý 3 sai vì Kc càng lớn thì phản ứng thuận diễn ra càng triệt để.")
    ]
    short = [
      (26, "Câu 26: Cho cân bằng: N2(k) + 3H2(k) ⇌ 2NH3(k). Ở trạng thái cân bằng, nồng độ [N2] = 0,5 M, [H2] = 1,0 M, [NH3] = 0,2 M. Giá trị hằng số cân bằng Kc bằng bao nhiêu?", "0.08", "Kc = [NH3]^2 / ([N2]*[H2]^3) = (0,2)^2 / (0,5 * 1,0^3) = 0,04 / 0,5 = 0,08."),
      (27, "Câu 27: Cho phản ứng: H2(k) + I2(k) ⇌ 2HI(k). Ở nhiệt độ T, hằng số Kc = 64. Khi nồng độ cân bằng [H2] = 0,1 M và [I2] = 0,1 M thì nồng độ cân bằng của HI là bao nhiêu M?", "0.8", "Kc = [HI]^2 / (0,1 * 0,1) = 64 => [HI]^2 = 0,64 => [HI] = 0,8 M."),
      (28, "Câu 28: Cho phản ứng A ⇌ 2B. Nồng độ ban đầu của A là 1,0 M. Ở trạng thái cân bằng đã có 40% chất A bị phân li. Nồng độ mol của B tại trạng thái cân bằng là bao nhiêu M?", "0.8", "A phản ứng 0,4 M => B tạo thành = 2 * 0,4 = 0,8 M."),
      (29, "Câu 29: Cho cân bằng: CaCO3(r) ⇌ CaO(r) + CO2(k). Ở nhiệt độ xác định, áp suất khí CO2 tại cân bằng là 0,5 atm. Có bao nhiêu chất xuất hiện trong biểu thức hằng số cân bằng Kc của phản ứng này?", "1", "Chỉ có CO2 (1 chất) vì CaCO3 và CaO là chất rắn."),
      (30, "Câu 30: Cho phản ứng thuận nghịch có Kc = 4 ở nhiệt độ T. Hằng số cân bằng Kc của phản ứng nghịch ở cùng nhiệt độ bằng bao nhiêu?", "0.25", "K_nghịch = 1 / Kc = 1 / 4 = 0,25."),
      (31, "Câu 31: Một bình kín có dung tích 2 lít chứa 0,4 mol N2O4 ở trạng thái cân bằng. Nồng độ mol của N2O4 tại cân bằng là bao nhiêu M?", "0.2", "C = n / V = 0,4 / 2 = 0,2 M.")
    ]
    essay = [
      "Nêu khái niệm phản ứng thuận nghịch và trạng thái cân bằng hóa học theo SGK Hóa học 11 Kết nối tri thức.",
      "Vì sao nói cân bằng hóa học là một cân bằng động? Phân biệt cân bằng động và cân bằng tĩnh.",
      "Phát biểu nguyên lí chuyển dịch cân bằng Le Chatelier và nêu ý nghĩa khoa học của nguyên lí này.",
      "Viết biểu thức hằng số cân bằng Kc cho phản ứng: N2(k) + 3H2(k) ⇌ 2NH3(k) và giải thích các đại lượng.",
      "Vì sao nồng độ chất rắn không được tính vào biểu thức hằng số cân bằng Kc?",
      "Trình bày ảnh hưởng của nhiệt độ đến chuyển dịch cân bằng của phản ứng tỏa nhiệt (ΔH < 0) và thu nhiệt (ΔH > 0).",
      "Trình bày ảnh hưởng của áp suất đến chuyển dịch cân bằng hóa học. Khi nào áp suất không ảnh hưởng đến cân bằng?",
      "Chất xúc tác có làm chuyển dịch cân bằng hóa học không? Giải thích rõ vai trò của chất xúc tác trong hệ cân bằng.",
      "Giải thích vì sao trong quá trình sản xuất ammonia theo quá trình Haber - Bosch, người ta phải thực hiện ở áp suất cao (khoảng 200 bar).",
      "Tại sao trong công nghiệp sản xuất NH3 người ta không thực hiện ở nhiệt độ phòng để đạt hiệu suất cao hơn?",
      "Cho cân bằng: 2SO2(k) + O2(k) ⇌ 2SO3(k) (ΔrHo < 0). Nêu 3 biện pháp cụ thể làm tăng hiệu suất tạo thành SO3.",
      "Mô tả hiện tượng và giải thích thí nghiệm ngâm bình chứa hỗn hợp khí NO2 (nâu đỏ) và N2O4 (không màu) vào nước đá lạnh.",
      "Cho phản ứng: CO(k) + H2O(k) ⇌ CO2(k) + H2(k). Nếu tăng áp suất bằng cách nén thể tích bình thì cân bằng có chuyển dịch không? Vì sao?",
      "Nêu mối liên hệ giữa hằng số cân bằng của phản ứng thuận (Kc) và phản ứng nghịch (K'c) ở cùng một nhiệt độ.",
      "Trình bày cách tính nồng độ các chất ở trạng thái cân bằng dựa vào nồng độ ban đầu và lượng phản ứng (phương pháp 3 dòng: Ban đầu - Phản ứng - Cân bằng).",
      "Tại sao việc lấy bớt sản phẩm ra khỏi lò phản ứng lại giúp tăng hiệu suất chuyển hóa của chất tham gia?",
      "Nêu một số ứng dụng của việc vận dụng nguyên lí Le Chatelier trong đời sống hàng ngày (bảo quản thực phẩm, sản xuất vôi sống, nước ngọt có ga)."
    ]
    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

BANK["c1_b1"] = build_bank_item("c1_b1", get_c1_b1_data())

# Save BANK to JSON / JS
with open("questions_bank.js", "w", encoding="utf-8") as f:
    f.write("/* NGAN HANG CAU HOI CHUAN SGK HOA HOC 11 KET NOI TRI THUC */\n")
    f.write("const LESSON_QUESTIONS_BANK = ")
    json.dump(BANK, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print("Created questions_bank.js with keys:", list(BANK.keys()))
