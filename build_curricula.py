# -*- coding: utf-8 -*-
"""
Curriculum and Question Bank Engine for Chemistry KNTT 10, 11, 12
"""

import json

# Knowledge templates by grade and chapter to ensure 100% topic-accuracy
TOPIC_DATABASE = {
    # HÓA HỌC 10
    "g10_b1": {
        "title": "Bài 1. Nhập môn hóa học",
        "grade": "10",
        "chapter": "CHƯƠNG 1. CẤU TẠO NGUYÊN TỬ",
        "summary": [
            ("Đối tượng nghiên cứu của hóa học", ["Hóa học là ngành khoa học tự nhiên nghiên cứu về thành phần, cấu trúc, tính chất và sự biến đổi của chất cũng như ứng dụng của chúng.", "Chất có ở xung quanh chúng ta: chất tự nhiên (nước, khoáng sản, không khí) và chất nhân tạo (nhựa, dược phẩm, phân bón)."]),
            ("Phương pháp học tập và nghiên cứu hóa học", ["Phương pháp nghiên cứu gồm: Quan sát, thu thập thông tin -> Đề xuất giả thuyết -> Thực nghiệm kiểm chứng -> Phân tích dữ liệu -> Rút ra kết luận.", "Quy tắc an toàn trong phòng thí nghiệm: Đeo kính bảo hộ, áo blouse; không nếm hóa chất; tuân thủ hướng dẫn của giáo viên."])
        ],
        "notes": [
            ("Ứng dụng thực tiễn của hóa học", "Hóa học đóng vai trò trung tâm kết nối các ngành khoa học (y học, sinh học, địa chất, vật liệu), cung cấp thuốc chữa bệnh, năng lượng mới và xử lý ô nhiễm môi trường.", False),
            ("Lưu ý an toàn phòng thí nghiệm", "Khi xảy ra sự cố hóa chất đổ ra bàn hoặc dính vào da, cần bình tĩnh báo ngay cho giáo viên và rửa ngay bằng nhiều nước sạch dưới vòi nước chảy.", True)
        ],
        "methods": [
            ("Dạng 1: Phân biệt hiện tượng vật lí và hiện tượng hóa học", "Hiện tượng vật lí là sự biến đổi về trạng thái, hình thái mà không tạo ra chất mới. Hiện tượng hóa học là sự biến đổi có sinh ra chất mới.", [
                ("Hiện tượng cồn để trong lọ không đậy nắp bị bay hơi là hiện tượng gì?", "Cồn chuyển từ thể lỏng sang thể hơi, không sinh ra chất mới nên là hiện tượng vật lí.", "Thông hiểu"),
                ("Đốt cháy nến (paraffin) trong không khí tạo ra khí carbon dioxide và hơi nước là hiện tượng gì?", "Có chất mới tạo thành là CO₂ và H₂O nên đây là hiện tượng hóa học.", "Thông hiểu"),
                ("Cho đinh sắt vào dung dịch copper sulfate (CuSO₄), đinh sắt có lớp kim loại màu đỏ bám ngoài và dung dịch nhạt màu dần. Giải thích hiện tượng.", "Đã có phản ứng hóa học: Fe + CuSO₄ -> FeSO₄ + Cu (Cu màu đỏ bám trên đinh sắt).", "Vận dụng")
            ]),
            ("Dạng 2: Quy tắc an toàn và sơ cứu trong phòng thí nghiệm", "Ghi nhớ các biểu tượng nguy hiểm (dễ cháy, ăn mòn, độc hại) và các bước xử lí tai nạn hóa chất.", [
                ("Ý nghĩa của biểu tượng có hình ngọn lửa trên nhãn chai hóa chất là gì?", "Biểu tượng cảnh báo chất dễ cháy, cần để xa nguồn lửa và nhiệt.", "Thông hiểu"),
                ("Khi bị acid đặc bắn vào da, bước sơ cứu đầu tiên cần làm ngay là gì?", "Rửa ngay dưới vòi nước chảy trong ít nhất 10-15 phút để làm trôi acid và giảm nhiệt độ, sau đó mới dùng dung dịch NaHCO₃ loãng rửa lại.", "Vận dụng"),
                ("Vì sao không được nếm hoặc ngửi trực tiếp các hóa chất trong phòng thí nghiệm?", "Vì nhiều hóa chất có độc tính cao, có thể gây bỏng đường hô hấp, ngộ độc hoặc nguy hiểm đến tính mạng.", "Vận dụng")
            ]),
            ("Dạng 3: Các bước thực hiện phương pháp nghiên cứu hóa học", "Tuân thủ quy trình 5 bước: Quan sát -> Giả thuyết -> Thí nghiệm -> Phân tích -> Kết luận.", [
                ("Bước nào trong quy trình nghiên cứu khoa học giúp kiểm tra giả thuyết đã đặt ra?", "Bước thực nghiệm (tiến hành thí nghiệm có đối chứng).", "Thông hiểu"),
                ("Muốn kiểm tra xem nhiệt độ có ảnh hưởng đến tốc độ hòa tan của đường trong nước không, ta cần làm thí nghiệm như thế nào?", "Dùng cùng một khối lượng đường hạt, hòa tan vào hai cốc nước có cùng thể tích nhưng ở nhiệt độ khác nhau (một cốc nước lạnh, một cốc nước nóng), quan sát thời gian tan hết.", "Vận dụng cao"),
                ("Nêu các yếu tố cần giữ cố định khi tiến hành thí nghiệm khảo sát một biến số.", "Giữ cố định nhiệt độ, áp suất, lượng hóa chất, nồng độ và dụng cụ đo (chỉ thay đổi duy nhất đại lượng cần khảo sát).", "Vận dụng cao")
            ])
        ],
        "keywords": ["hóa học", "chất tự nhiên", "chất nhân tạo", "phòng thí nghiệm", "hiện tượng hóa học", "hiện tượng vật lí", "biến đổi chất", "an toàn hóa chất"]
    },
    "g10_b2": {
        "title": "Bài 2. Nguyên tử và cấu tạo nguyên tử",
        "grade": "10",
        "chapter": "CHƯƠNG 1. CẤU TẠO NGUYÊN TỬ",
        "summary": [
            ("Thành phần cấu tạo nguyên tử", ["Nguyên tử gồm hạt nhân mang điện tích dương và vỏ electron mang điện tích âm.", "Hạt nhân gồm các hạt proton (p, mang điện tích +1) và neutron (n, không mang điện).", "Vỏ nguyên tử gồm các electron (e, mang điện tích -1). Khối lượng electron rất nhỏ (khoảng 1/1840 amu)."]),
            ("Kích thước và khối lượng nguyên tử", ["Nguyên tử trung hòa về điện: Số proton (Z) = Số electron (e).", "Đơn vị khối lượng nguyên tử là amu (1 amu ≈ 1,6605 × 10⁻²⁷ kg).", "Khối lượng nguyên tử tập trung hầu hết ở hạt nhân: A = Z + N (A là số khối)."])
        ],
        "notes": [
            ("Mô hình Rutherford - Bohr", "Electron chuyển động xung quanh hạt nhân trên những quỹ đạo xác định (lớp electron) giống như các hành tinh quay quanh Mặt Trời.", False),
            ("Đặc điểm hạt nhân", "Kích thước hạt nhân cực kì nhỏ so với kích thước nguyên tử (đường kính nguyên tử lớn hơn hạt nhân khoảng 10.000 lần), nguyên tử có cấu tạo rỗng.", True)
        ],
        "methods": [
            ("Dạng 1: Mối quan hệ giữa p, n, e và số khối A", "Nguyên tử trung hòa điện: Z = p = e. Số khối A = Z + N. Tổng số hạt trong nguyên tử: 2Z + N.", [
                ("Một nguyên tử có 11 proton và 12 neutron. Tính số electron và số khối A của nguyên tử đó.", "Nguyên tử trung hòa điện nên số e = số p = 11. Số khối A = Z + N = 11 + 12 = 23 (Na).", "Thông hiểu"),
                ("Tổng số hạt cơ bản (p, n, e) trong một nguyên tử là 40. Trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 12. Tìm số p, n, e.", "Hệ phương trình: 2Z + N = 40 và 2Z - N = 12. Cộng lại: 4Z = 52 => Z = 13 (Al); N = 14. Vậy p = e = 13, n = 14.", "Vận dụng"),
                ("Nguyên tử X có tổng số hạt là 52. Số hạt không mang điện chiếm 34,62% tổng số hạt. Xác định số khối A của X.", "N = 52 * 0,3462 ≈ 18. Số hạt mang điện 2Z = 52 - 18 = 34 => Z = 17 (Cl). Số khối A = 17 + 18 = 35.", "Vận dụng cao")
            ]),
            ("Dạng 2: Điện tích hạt nhân và kí hiệu nguyên tử", "Điện tích hạt nhân = +Z. Kí hiệu nguyên tử: Z^A X.", [
                ("Hạt nhân nguyên tử Carbon có 6 proton. Điện tích hạt nhân của nguyên tử Carbon là bao nhiêu?", "Điện tích hạt nhân là +6 (hoặc 6+).", "Thông hiểu"),
                ("Viết kí hiệu nguyên tử của nguyên tố Potassium (K) biết hạt nhân có 19 proton và 20 neutron.", "Z = 19, A = 19 + 20 = 39. Kí hiệu là: 19^39 K.", "Thông hiểu"),
                ("Cho ion M²⁺ có tổng số hạt mang điện là 22. Xác định nguyên tố M.", "Ion M²⁺ có số electron = Z - 2. Tổng số hạt mang điện của ion = Z + (Z - 2) = 2Z - 2 = 22 => 2Z = 24 => Z = 12. Vậy M là Magnesium (Mg).", "Vận dụng")
            ]),
            ("Dạng 3: Bán kính và khối lượng riêng của nguyên tử", "V = 4/3 * π * R³. Khối lượng riêng d = m / V.", [
                ("Bán kính nguyên tử hydro xấp xỉ 0,053 nm. Đổi bán kính này sang đơn vị mét.", "1 nm = 10⁻⁹ m => R = 0,053 * 10⁻⁹ m = 5,3 * 10⁻¹¹ m.", "Thông hiểu"),
                ("Nguyên tử vàng (Au) có bán kính xấp xỉ 0,144 nm và khối lượng mol M = 197 g/mol. Tính khối lượng riêng của nguyên tử Au (coi nguyên tử là hình cầu).", "V = 4/3 * π * (0,144*10⁻⁷)³ = 1,25 * 10⁻²³ cm³. Khối lượng 1 nguyên tử = 197 / (6,022*10²³) = 3,27*10⁻²² g. d = m/V ≈ 26,16 g/cm³.", "Vận dụng cao"),
                ("Tính tỉ lệ thể tích của nguyên tử so với thể tích của hạt nhân biết bán kính nguyên tử lớn gấp 10.000 lần bán kính hạt nhân.", "V tỉ lệ với R³ => V_nguyên tử / V_hạt nhân = (10⁴)³ = 10¹² lần.", "Vận dụng")
            ])
        ],
        "keywords": ["proton", "neutron", "electron", "hạt nhân", "số khối", "điện tích hạt nhân", "Rutherford", "Bohr"]
    },
    # HÓA HỌC 12
    "g12_b1": {
        "title": "Bài 1. Ester",
        "grade": "12",
        "chapter": "CHƯƠNG 1. ESTER - LIPID",
        "summary": [
            ("Khái niệm và danh pháp ester", ["Khi thay nhóm -OH ở nhóm carboxyl của carboxylic acid bằng nhóm -OR' thì thu được ester: R-COO-R'.", "Ester no, đơn chức, mạch hở có CTPT chung: CₙH₂ₙO₂ (n ≥ 2).", "Tên ester = Tên gốc hydrocarbon R' + tên gốc acid RCOO (đổi đuôi ic -> at). Ví dụ: CH₃COOC₂H₅ là ethyl acetate."]),
            ("Tính chất hóa học và điều chế", ["Phản ứng thủy phân trong môi trường acid (thuận nghịch): RCOOR' + H₂O ⇌ RCOOH + R'OH.", "Phản ứng thủy phân trong môi trường kiềm (phản ứng xà phòng hóa, một chiều): RCOOR' + NaOH -> RCOONa + R'OH.", "Điều chế ester bằng phản ứng ester hóa giữa carboxylic acid và alcohol có xúc tác H₂SO₄ đặc."])
        ],
        "notes": [
            ("Mùi hương đặc trưng của ester", "Nhiều ester có mùi thơm hoa quả chín: Isoamyl acetate (mùi chuối chín), ethyl butyrate (mùi dứa), benzyl acetate (mùi hoa nhài), được dùng làm hương liệu thực phẩm và mỹ phẩm.", False),
            ("Nhiệt độ sôi của ester", "Ester không có liên kết hydrogen liên phân tử như alcohol và carboxylic acid nên có nhiệt độ sôi thấp hơn nhiều so với alcohol và acid có cùng phân tử khối hoặc cùng số nguyên tử C.", True)
        ],
        "methods": [
            ("Dạng 1: Viết đồng phân và gọi tên ester", "Ester no đơn chức CnH2nO2. Bắt đầu từ acid fomic HCOO-, sau đó tăng mạch carbon ở gốc acid.", [
                ("Viết tất cả các đồng phân ester có công thức phân tử C₂H₄O₂ và gọi tên.", "Chỉ có 1 đồng phân duy nhất: HCOOCH₃ (methyl formate).", "Thông hiểu"),
                ("Công thức phân tử C₃H₆O₂ có bao nhiêu đồng phân ester? Gọi tên từng đồng phân.", "Có 2 đồng phân ester: HCOOC₂H₅ (ethyl formate) và CH₃COOCH₃ (methyl acetate).", "Thông hiểu"),
                ("Có bao nhiêu đồng phân ester ứng với công thức phân tử C₄H₈O₂?", "Có 4 đồng phân: HCOOCH₂CH₂CH₃, HCOOCH(CH₃)₂, CH₃COOC₂H₅, C₂H₅COOCH₃.", "Vận dụng")
            ]),
            ("Dạng 2: Phản ứng xà phòng hóa ester", "Phương trình: RCOOR' + NaOH -> RCOONa + R'OH. Áp dụng định luật bảo toàn khối lượng: m_ester + m_NaOH = m_muối + m_alcohol.", [
                ("Thủy phân hoàn toàn 8,8 gam ethyl acetate (CH₃COOC₂H₅) trong dung dịch NaOH vừa đủ. Tính khối lượng muối CH₃COONa thu được.", "n_ester = 8,8 / 88 = 0,1 mol => n_muối = 0,1 mol => m_muối = 0,1 * 82 = 8,2 gam.", "Thông hiểu"),
                ("Xà phòng hóa hoàn toàn 7,4 gam ester X no, đơn chức mạch hở cần 100 mL dung dịch NaOH 1M. Tìm công thức phân tử của X.", "n_NaOH = 0,1 mol => n_X = 0,1 mol => M_X = 7,4 / 0,1 = 74 amu. CnH2nO2 = 14n + 32 = 74 => n = 3 => CTPT là C₃H₆O₂.", "Vận dụng"),
                ("Thủy phân hoàn toàn 0,1 mol ester đơn chức X tác dụng vừa đủ với 0,2 mol NaOH thu được 16,4 gam muối và nước. Xác định cấu tạo của X.", "Tỉ lệ n_ester : n_NaOH = 1 : 2 và sản phẩm tạo ra muối + nước chứng tỏ X là ester của phenol (RCOOC₆H₄R'). X có CTCT CH₃COOC₆H₅ (phenyl acetate).", "Vận dụng cao")
            ]),
            ("Dạng 3: Hiệu suất phản ứng ester hóa", "RCOOH + R'OH ⇌ RCOOR' + H₂O. Hiệu suất H% = (lượng thực tế / lượng lí thuyết) * 100%.", [
                ("Đun sôi hỗn hợp gồm 6,0 gam CH₃COOH và 6,0 gam C₂H₅OH với H₂SO₄ đặc làm xúc tác thu được 5,28 gam ethyl acetate. Tính hiệu suất của phản ứng.", "n_acid = 0,1 mol; n_alcohol = 0,13 mol => lí thuyết tính theo acid: n_lí thuyết = 0,1 mol (8,8g). n_thực tế = 5,28 / 88 = 0,06 mol => H = (0,06 / 0,1) * 100% = 60%.", "Vận dụng"),
                ("Cần bao nhiêu gam acetic acid phản ứng với ethanol dư (hiệu suất 80%) để thu được 17,6 gam ethyl acetate?", "n_ester = 17,6 / 88 = 0,2 mol => n_acid cần = 0,2 / 0,8 = 0,25 mol => m_acid = 0,25 * 60 = 15 gam.", "Vận dụng"),
                ("Trình bày vai trò của H₂SO₄ đặc và đá bọt trong thí nghiệm điều chế ethyl acetate trong phòng thí nghiệm.", "H₂SO₄ đặc đóng vai trò xúc tác làm tăng tốc độ phản ứng và hút nước làm cân bằng chuyển dịch theo chiều thuận tạo ester; đá bọt giúp hỗn hợp sôi êm, tránh sôi bùng.", "Vận dụng cao")
            ])
        ],
        "keywords": ["ester", "xà phòng hóa", "ester hóa", "ethyl acetate", "isoamyl acetate", "thủy phân", "hương liệu"]
    }
}

print("TOPIC_DATABASE loaded.")
