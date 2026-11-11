# -*- coding: utf-8 -*-
"""
Generate complete 48 concrete questions for any Chemistry lesson
"""

def generate_concrete_questions(lid, domain_key, lesson_name):
    # Concrete MCQ pool based on domain
    if domain_key == "c1":
        mcq_items = [
            ("Phản ứng nào sau đây là phản ứng thuận nghịch?", ["N2(k) + 3H2(k) ⇌ 2NH3(k)", "2H2 + O2 -> 2H2O", "NaOH + HCl -> NaCl + H2O", "Fe + 2HCl -> FeCl2 + H2"], 0, "N2 + 3H2 ⇌ 2NH3 là phản ứng thuận nghịch xảy ra 2 chiều."),
            ("Khi phản ứng thuận nghịch đạt trạng thái cân bằng thì:", ["v_thuận = v_nghịch > 0", "v_thuận = 0", "Phản ứng dừng lại hoàn toàn", "Nồng độ các chất bằng nhau"], 0, "Cân bằng hóa học là cân bằng động, tốc độ thuận bằng tốc độ nghịch."),
            ("Biểu thức hằng số cân bằng Kc của phản ứng H2(k) + I2(k) ⇌ 2HI(k) là:", ["Kc = [HI]^2 / ([H2] * [I2])", "Kc = [HI] / ([H2] * [I2])", "Kc = ([H2] * [I2]) / [HI]^2", "Kc = 2[HI] / ([H2] * [I2])"], 0, "Biểu thức chuẩn của Kc."),
            ("Chất nào sau đây KHÔNG xuất hiện trong biểu thức hằng số cân bằng Kc?", ["Chất khí", "Chất tan trong dung dịch", "Chất rắn nguyên chất", "Chất lỏng bay hơi"], 2, "Chất rắn có nồng độ không đổi nên quy ước không ghi vào Kc."),
            ("Cho cân bằng: N2 + 3H2 ⇌ 2NH3 (ΔH < 0). Để cân bằng chuyển dịch theo chiều thuận cần:", ["Giảm nhiệt độ và tăng áp suất", "Tăng nhiệt độ và giảm áp suất", "Tăng nhiệt độ và tăng áp suất", "Giảm nhiệt độ và giảm áp suất"], 0, "Chiều thuận tỏa nhiệt và giảm số mol khí."),
            ("Chất điện li mạnh trong nước là:", ["CH3COOH", "NaCl", "H2O", "C2H5OH"], 1, "NaCl là muối tan phân li hoàn toàn thành ion."),
            ("Dung dịch có pH = 2 thì nồng độ ion H+ là:", ["0,01 M", "0,1 M", "0,001 M", "2 M"], 0, "[H+] = 10^-pH = 10^-2 M = 0,01 M."),
            ("Dung dịch nào sau đây làm quỳ tím hóa đỏ?", ["HCl", "NaOH", "NaCl", "Ba(OH)2"], 0, "Dung dịch acid HCl làm quỳ tím hóa đỏ."),
            ("Theo thuyết Brønsted - Lowry, acid là chất có khả năng:", ["Cho proton H+", "Nhận proton H+", "Cho electron", "Nhận electron"], 0, "Acid là chất cho H+."),
            ("Theo thuyết Brønsted - Lowry, base là chất có khả năng:", ["Nhận proton H+", "Cho proton H+", "Cho electron", "Điện li ra OH-"], 0, "Base là chất nhận H+."),
            ("Chất nào sau đây là chất lưỡng tính theo Brønsted - Lowry?", ["HCO3-", "Cl-", "Na+", "SO4(2-)"], 0, "HCO3- vừa cho H+ vừa nhận H+ được."),
            ("Trộn 100 mL dung dịch HCl 0,1M với 100 mL dung dịch NaOH 0,1M. Dung dịch thu được có pH bằng:", ["7", "1", "13", "0"], 0, "Trung hòa hoàn toàn tạo dung dịch trung tính pH = 7."),
            ("Trong phương pháp chuẩn độ acid - base, chất chỉ thị phenolphthalein đổi sang màu gì ở điểm tương đương khi chuẩn độ acid bằng base?", ["Màu hồng (hồng tím)", "Màu đỏ", "Màu xanh", "Màu vàng"], 0, "Phenolphthalein đổi màu hồng trong môi trường kiềm nhẹ."),
            ("Ở 25°C, tích số ion của nước Kw bằng:", ["1,0 x 10^-14", "1,0 x 10^-7", "1,0 x 10^-1", "1,0 x 10^-12"], 0, "Kw = [H+] * [OH-] = 10^-14."),
            ("Dung dịch có [OH-] = 10^-4 M có môi trường gì và pH bằng bao nhiêu?", ["Base, pH = 10", "Acid, pH = 4", "Trung tính, pH = 7", "Base, pH = 4"], 0, "pOH = 4 => pH = 10 > 7 (môi trường base)."),
            ("Hằng số cân bằng Kc của một phản ứng xác định chỉ phụ thuộc vào:", ["Nhiệt độ", "Áp suất", "Nồng độ", "Chất xúc tác"], 0, "Kc chỉ phụ thuộc nhiệt độ và bản chất phản ứng."),
            ("Chất xúc tác có tác dụng gì đối với trạng thái cân bằng?", ["Tăng tốc độ đạt tới cân bằng, không làm chuyển dịch cân bằng", "Làm cân bằng chuyển dịch theo chiều thuận", "Làm tăng Kc", "Làm giảm áp suất"], 0, "Xúc tác không làm chuyển dịch cân bằng."),
            ("Cho phản ứng C(r) + CO2(k) ⇌ 2CO(k). Khi tăng áp suất, cân bằng sẽ chuyển dịch theo:", ["Chiều nghịch", "Chiều thuận", "Không chuyển dịch", "Dừng lại"], 0, "Vế trái có 1 mol khí, vế phải có 2 mol khí. Tăng áp suất chuyển dịch theo chiều nghịch."),
            ("Dung dịch NH3 làm quỳ tím chuyển sang màu gì?", ["Màu xanh", "Màu đỏ", "Màu vàng", "Không đổi màu"], 0, "NH3 có tính base yếu làm quỳ tím hóa xanh."),
            ("Cặp chất nào sau đây xảy ra phản ứng trao đổi ion trong dung dịch?", ["BaCl2 + Na2SO4", "NaCl + KNO3", "HCl + NaNO3", "CaCl2 + KNO3"], 0, "Tạo kết tủa BaSO4 trắng."),
            ("Khí CO2 tan trong nước tạo ra dung dịch có tính:", ["Acid yếu", "Base yếu", "Trung tính", "Acid rất mạnh"], 0, "CO2 + H2O ⇌ H2CO3 là acid yếu.")
        ]
    elif domain_key == "c2":
        mcq_items = [
            ("Khí nitrogen chiếm khoảng bao nhiêu phần trăm thể tích khí quyển Trái Đất?", ["78%", "21%", "1%", "0,04%"], 0, "Khí N2 chiếm khoảng 78% thể tích không khí."),
            ("Ở nhiệt độ thường, đơn chất nitrogen khá trơ về mặt hóa học là do:", ["Phân tử có liên kết ba N≡N rất bền vững", "Bán kính nguyên tử nhỏ", "Độ âm điện lớn", "Có tính oxi hóa mạnh"], 0, "Năng lượng liên kết ba N≡N rất lớn (945 kJ/mol)."),
            ("Trong phòng thí nghiệm, khí ammonia NH3 được thu bằng phương pháp:", ["Đẩy không khí úp ngược bình", "Đẩy không khí ngửa bình", "Đẩy nước", "Cả 3 phương pháp"], 0, "NH3 nhẹ hơn không khí (M=17) và tan rất nhiều trong nước."),
            ("Dung dịch ammonia có tính base yếu là do:", ["Phân tử NH3 nhận proton H+ từ nước tạo ion OH-", "Phân tử NH3 phân li ra OH-", "Có chứa ion H+", "Có tính khử mạnh"], 0, "NH3 + H2O ⇌ NH4+ + OH-."),
            ("Muối ammonium khi đun nóng với dung dịch kiềm giải phóng khí có mùi khai là:", ["NH3", "NO2", "N2", "H2S"], 0, "NH4+ + OH- -> NH3↑ + H2O."),
            ("Axit nitric HNO3 là một axit có tính chất đặc trưng là:", ["Tính acid mạnh và tính oxi hóa rất mạnh", "Tính acid yếu", "Chỉ có tính khử", "Chỉ có tính oxi hóa yếu"], 0, "HNO3 là chất oxi hóa rất mạnh."),
            ("Kim loại nào sau đây KHÔNG tác dụng được với dung dịch HNO3 đặc nóng?", ["Au và Pt", "Fe và Cu", "Al và Zn", "Ag và Pb"], 0, "Vàng (Au) và bạch kim (Pt) không tan trong HNO3 đặc nóng."),
            ("Khí NO2 sinh ra trong phản ứng của Cu với HNO3 đặc có màu gì?", ["Màu nâu đỏ", "Không màu", "Màu vàng lục", "Màu xanh lam"], 0, "NO2 là khí màu nâu đỏ, độc."),
            ("Hiện tượng 'phú dưỡng' (eutrophication) trong các ao hồ chủ yếu do dư thừa hàm lượng nguyên tố nào?", ["Nitrogen (N) và Phosphorus (P)", "Carbon và Oxygen", "Sodium và Chlorine", "Sắt và Nhôm"], 0, "Dư thừa N và P từ phân bón và nước thải."),
            ("Đơn chất sulfur ở điều kiện thường là chất rắn có màu gì?", ["Màu vàng", "Màu đỏ", "Màu trắng", "Màu tím"], 0, "Sulfur là chất rắn màu vàng."),
            ("Sulfur dioxide SO2 thể hiện tính khử khi tác dụng với chất nào sau đây?", ["Dung dịch nước brom (Br2)", "Khí H2S", "Dung dịch NaOH", "Khí H2"], 0, "SO2 làm mất màu nước brom: SO2 + Br2 + 2H2O -> 2HBr + H2SO4."),
            ("Khí SO2 là một trong những nguyên nhân chính gây ra hiện tượng môi trường nào?", ["Mưa acid", "Thủng tầng ozone", "Hiệu ứng nhà kính duy nhất", "Triều cường"], 0, "SO2 và NOx gây mưa acid."),
            ("Axit sunfuric đặc nguội làm thụ động hóa các kim loại nào?", ["Fe, Al, Cr", "Cu, Ag, Au", "Mg, Zn, Fe", "Na, K, Ca"], 0, "Fe, Al, Cr bị thụ động hóa trong H2SO4 đặc nguội."),
            ("Để nhận biết ion sulfate SO4(2-) trong dung dịch, người ta dùng thuốc thử:", ["Dung dịch BaCl2", "Dung dịch AgNO3", "Quỳ tím", "Dung dịch NaOH"], 0, "Tạo kết tủa trắng BaSO4 không tan trong axit mạnh."),
            ("Quy tắc pha loãng axit H2SO4 đặc an toàn là:", ["Rót từ từ axit đặc vào nước và khuấy đều", "Rót nhanh nước vào axit đặc", "Rót đồng thời cả hai vào nhau", "Đun nóng axit rồi mới đổ nước"], 0, "Luôn rót axit vào nước."),
            ("Muối sulfate nào sau đây được dùng làm chất cản quang trong chụp X-quang đường tiêu hóa?", ["BaSO4", "CuSO4", "MgSO4", "CaSO4"], 0, "BaSO4 không tan trong nước và acid dịch vị, cản quang tốt."),
            ("Thạch cao sống có công thức hóa học là:", ["CaSO4.2H2O", "CaSO4.H2O", "CaSO4", "MgSO4.7H2O"], 0, "CaSO4.2H2O là thạch cao sống."),
            ("Muối ammonium nitrate có công thức hóa học là:", ["NH4NO3", "(NH4)2SO4", "NH4Cl", "(NH4)2CO3"], 0, "NH4NO3 là ammonium nitrate."),
            ("Số oxi hóa của sulfur trong phân tử H2SO4 là:", ["+6", "+4", "0", "-2"], 0, "S trong H2SO4 có số oxi hóa +6 cao nhất."),
            ("Khí nào sau đây có mùi trứng thối đặc trưng?", ["H2S", "SO2", "NH3", "NO2"], 0, "H2S có mùi trứng thối."),
            ("Axit nitric được sử dụng trong công nghiệp để sản xuất:", ["Phân đạm và thuốc nổ", "Nước ngọt có ga", "Xi măng xây dựng", "Xà phòng bánh"], 0, "Sản xuất phân bón (NH4NO3) và thuốc nổ TNT.")
        ]
    else:
        # Default organic / general concrete questions
        mcq_items = [
            ("Hydrocarbon no, mạch hở alkane có công thức chung là:", ["CnH2n+2 (n ≥ 1)", "CnH2n (n ≥ 2)", "CnH2n-2", "CnH2n-6"], 0, "Công thức chung của alkane là CnH2n+2."),
            ("Phản ứng đặc trưng của alkane là:", ["Phản ứng thế", "Phản ứng cộng", "Phản ứng trùng hợp", "Phản ứng tráng bạc"], 0, "Alkane chỉ có liên kết đơn nên đặc trưng bởi phản ứng thế."),
            ("Khí methane (CH4) là thành phần chính của:", ["Khí thiên nhiên và khí biogas", "Khí than ướt", "Khí cười", "Khí lò cao"], 0, "Khí thiên nhiên chứa tới 95% methane."),
            ("Cho methane phản ứng với chlorine có chiếu sáng tỉ lệ mol 1:1 thu được:", ["CH3Cl và HCl", "CH2Cl2", "CHCl3", "CCl4"], 0, "CH4 + Cl2 -> CH3Cl + HCl."),
            ("Chất nào sau đây làm mất màu dung dịch nước brom ở điều kiện thường?", ["Ethylene (C2H4)", "Ethane (C2H6)", "Methane (CH4)", "Propane (C3H8)"], 0, "Ethylene có liên kết đôi C=C tác dụng brom làm mất màu."),
            ("Trùng hợp ethylene thu được polymer nào sau đây?", ["Polyethylene (PE)", "Polypropylene (PP)", "PVC", "Teflon"], 0, "Trùng hợp C2H4 tạo nhựa PE."),
            ("Alkene tác dụng với H2O (xúc tác H+) tuân theo quy tắc nào?", ["Quy tắc Markovnikov", "Quy tắc Zaitsev", "Quy tắc Hund", "Quy tắc Pauli"], 0, "Cộng HX vào alkene bất đối xứng theo Markovnikov."),
            ("Chất nào sau đây có phản ứng tạo kết tủa vàng nhạt với dung dịch AgNO3/NH3?", ["Acetylene (CH≡CH)", "Ethylene", "Methane", "Benzene"], 0, "Alkyne có nối ba đầu mạch (1-alkyne) có H linh động phản ứng với AgNO3/NH3."),
            ("Benzene (C6H6) có cấu trúc phân tử dạng:", ["Lục giác đều phẳng", "Hình tam giác", "Hình chóp", "Mạch hở uốn khúc"], 0, "Benzene có vòng lục giác đều 6 cạnh phẳng."),
            ("Phản ứng nitro hóa benzene bằng hỗn hợp HNO3 đặc và H2SO4 đặc tạo thành:", ["Nitrobenzene (C6H5NO2)", "Aniline", "Phenol", "Toluene"], 0, "Tạo nitrobenzene màu vàng nhạt."),
            ("Alcohol no, đơn chức, mạch hở có công thức chung là:", ["CnH2n+1OH (n ≥ 1)", "CnH2n(OH)2", "CnH2n-1OH", "C6H5OH"], 0, "Công thức alkane alcohol là CnH2n+1OH."),
            ("Alcohol nào sau đây có trong thành phần các loại đồ uống có cồn?", ["Ethanol (C2H5OH)", "Methanol (CH3OH)", "Glycerol", "Ethylene glycol"], 0, "Ethanol là cồn thực phẩm."),
            ("Chất nào sau đây rất độc, có thể gây mù mắt hoặc tử vong khi uống phải rượu giả?", ["Methanol (CH3OH)", "Ethanol", "Glucose", "Acetic acid"], 0, "Methanol cực độc do chuyển hóa thành formaldehyde và formic acid."),
            ("Phenol (C6H5OH) tác dụng được với dung dịch nào sau đây?", ["Dung dịch NaOH", "Dung dịch NaCl", "Dung dịch HCl", "Dung dịch Na2SO4"], 0, "Phenol có tính acid yếu nên tác dụng với bazơ mạnh NaOH."),
            ("Nhỏ nước brom vào dung dịch phenol xuất hiện kết tủa màu gì?", ["Màu trắng (2,4,6-tribromophenol)", "Màu vàng", "Màu đen", "Màu đỏ"], 0, "Tạo kết tủa trắng 2,4,6-tribromophenol."),
            ("Hợp chất aldehyde có nhóm chức đặc trưng là:", ["-CHO", "-COOH", "-OH", "-COO-"], 0, "Nhóm -CHO là aldehyde."),
            ("Chất nào sau đây tham gia phản ứng tráng bạc tạo lớp bạc sáng bóng?", ["Acetaldehyde (CH3CHO)", "Ethanol", "Acetic acid", "Acetone"], 0, "Aldehyde tham gia phản ứng tráng bạc."),
            ("Acetic acid (CH3COOH) có nồng độ khoảng 2 - 5% trong đời sống được gọi là:", ["Giấm ăn", "Cồn y tế", "Dầu hỏa", "Nước vôi"], 0, "Giấm ăn là dung dịch acetic acid loãng."),
            ("Phản ứng giữa carboxylic acid và alcohol có xúc tác H2SO4 đặc gọi là:", ["Phản ứng ester hóa", "Phản ứng xà phòng hóa", "Phản ứng trùng ngưng", "Phản ứng lên men"], 0, "Phản ứng ester hóa."),
            ("Ester ethyl acetate (CH3COOC2H5) có mùi hương đặc trưng của:", ["Hoa quả chín (mùi dưa, táo thơm)", "Mùi trứng thối", "Mùi khai", "Không mùi"], 0, "Ester có mùi thơm hoa quả."),
            ("Chất béo (triglyceride) là triester của carboxylic acid béo với:", ["Glycerol (propane-1,2,3-triol)", "Ethanol", "Methanol", "Ethylene glycol"], 0, "Chất béo là ester của glycerol.")
        ]

    mcq = [
        {
            "id": f"{lid}_c{i+1}",
            "num": i + 1,
            "type": "mcq",
            "levelClass": "level-nb" if i < 7 else ("level-th" if i < 15 else "level-vd"),
            "levelName": "Nhận biết" if i < 7 else ("Thông hiểu" if i < 15 else "Vận dụng"),
            "title": f"Câu {i+1}: {item[0]}",
            "options": item[1],
            "correct": item[2],
            "explanation": item[3]
        }
        for i, item in enumerate(mcq_items)
    ]

    tf = [
        {
            "id": f"{lid}_c22",
            "num": 22,
            "type": "tf",
            "levelClass": "level-th",
            "levelName": "Thông hiểu",
            "title": f"Câu 22: Xem xét các phát biểu về tính chất và quy luật hóa học trong bài học {lesson_name}:",
            "statements": [
                {"text": "a) Các phản ứng hóa học luôn tuân theo các định luật bảo toàn khối lượng và bảo toàn nguyên tố.", "ans": True},
                {"text": "b) Điều kiện nhiệt độ và xúc tác không ảnh hưởng đến tốc độ của quá trình phản ứng.", "ans": False},
                {"text": "c) Cấu trúc phân tử quyết định trực tiếp đến tính chất vật lí và hóa học của hợp chất.", "ans": True},
                {"text": "d) Mọi biến đổi hóa học đều diễn ra hoàn toàn 100% không tạo ra sản phẩm phụ.", "ans": False}
            ],
            "explanation": "Ý a và c đúng theo các nguyên lí hóa học cơ bản. Ý b sai vì nhiệt độ và xúc tác ảnh hưởng mạnh đến tốc độ phản ứng. Ý d sai vì nhiều phản ứng là thuận nghịch hoặc tạo hỗn hợp sản phẩm phụ."
        },
        {
            "id": f"{lid}_c23",
            "num": 23,
            "type": "tf",
            "levelClass": "level-th",
            "levelName": "Thông hiểu",
            "title": f"Câu 23: Về thực hành thí nghiệm và an toàn trong phòng thí nghiệm hóa học:",
            "statements": [
                {"text": "a) Đeo kính bảo hộ và áo choàng phòng thí nghiệm là bắt buộc khi làm việc với hóa chất độc hại.", "ans": True},
                {"text": "b) Khi đun nóng chất lỏng trong ống nghiệm, hướng miệng ống nghiệm về phía bạn bè để cùng quan sát.", "ans": False},
                {"text": "c) Hóa chất thừa sau thí nghiệm không được đổ tùy tiện vào bồn rửa mà phải thu gom xử lí theo quy định.", "ans": True},
                {"text": "d) Có thể dùng tay trần để cầm trực tiếp các hóa chất có tính ăn mòn như axit đặc và kiềm rắn.", "ans": False}
            ],
            "explanation": "Ý b sai vì có thể gây bỏng nguy hiểm cho người đối diện. Ý d sai vì hóa chất ăn mòn gây bỏng nặng cho da."
        },
        {
            "id": f"{lid}_c24",
            "num": 24,
            "level": "level-vd",
            "levelName": "Vận dụng",
            "title": f"Câu 24: Về các phương pháp tách chất, nhận biết và ứng dụng thực tiễn:",
            "statements": [
                {"text": "a) Các chất có nhiệt độ sôi khác nhau có thể tách biệt bằng phương pháp chưng cất.", "ans": True},
                {"text": "b) Hai chất lỏng hòa tan hoàn toàn vào nhau tạo dung dịch đồng nhất luôn tách được bằng phễu chiết thông thường.", "ans": False},
                {"text": "c) Phản ứng tạo kết tủa hoặc đổi màu chỉ thị thường được dùng trong nhận biết hóa học.", "ans": True},
                {"text": "d) Khí độc sinh ra trong phòng thí nghiệm cần được hấp thụ bằng dung dịch thích hợp trước khi thải ra ngoài.", "ans": True}
            ],
            "explanation": "Ý b sai vì phễu chiết chỉ dùng cho hai chất lỏng không trộn lẫn tạo hai lớp phân cách."
        },
        {
            "id": f"{lid}_c25",
            "num": 25,
            "level": "level-vd",
            "levelName": "Vận dụng",
            "title": f"Câu 25: Về tính toán hóa học và định luật bảo toàn:",
            "statements": [
                {"text": "a) Số mol electron nhường luôn bằng số mol electron nhận trong phản ứng oxi hóa - khử.", "ans": True},
                {"text": "b) Khối lượng các chất sản phẩm luôn bằng khối lượng các chất tham gia phản ứng.", "ans": True},
                {"text": "c) Hiệu suất của mọi phản ứng hóa học trong thực tế công nghiệp luôn luôn đạt 100%.", "ans": False},
                {"text": "d) Nồng độ mol của dung dịch tính bằng số mol chất tan chia cho thể tích dung dịch (lít).", "ans": True}
            ],
            "explanation": "Ý c sai vì trong thực tế có sự hao hụt, phản ứng thuận nghịch hoặc tạo sản phẩm phụ nên hiệu suất luôn < 100%."
        }
    ]

    short = [
        {
            "id": f"{lid}_c26",
            "num": 26,
            "type": "short",
            "levelClass": "level-vd",
            "levelName": "Vận dụng",
            "title": "Câu 26: Hòa tan hoàn toàn 5,6 gam bột sắt (Fe, M=56) vào dung dịch HCl dư. Thể tích khí H2 thu được ở điều kiện tiêu chuẩn là bao nhiêu lít?",
            "correctText": "2.24",
            "explanation": "nFe = 5,6 / 56 = 0,1 mol. Fe + 2HCl -> FeCl2 + H2 => nH2 = 0,1 mol => V = 0,1 * 22,4 = 2,24 lít."
        },
        {
            "id": f"{lid}_c27",
            "num": 27,
            "type": "short",
            "levelClass": "level-vd",
            "levelName": "Vận dụng",
            "title": "Câu 27: Cần dùng bao nhiêu gam NaOH (M=40) để trung hòa hoàn toàn 100 mL dung dịch HCl 0,5 M?",
            "correctText": "2",
            "explanation": "nHCl = 0,1 * 0,5 = 0,05 mol => nNaOH = 0,05 mol => mNaOH = 0,05 * 40 = 2,0 gam."
        },
        {
            "id": f"{lid}_c28",
            "num": 28,
            "type": "short",
            "levelClass": "level-vd",
            "levelName": "Vận dụng",
            "title": "Câu 28: Đốt cháy hoàn toàn 0,2 mol một hydrocarbon thu được 0,6 mol CO2. Số nguyên tử Carbon trong phân tử hydrocarbon này là bao nhiêu?",
            "correctText": "3",
            "explanation": "Số C = nCO2 / n = 0,6 / 0,2 = 3."
        },
        {
            "id": f"{lid}_c29",
            "num": 29,
            "type": "short",
            "levelClass": "level-vd",
            "levelName": "Vận dụng",
            "title": "Câu 29: Phân tử khối của acetic acid (CH3COOH) bằng bao nhiêu amu?",
            "correctText": "60",
            "explanation": "M = 12*2 + 4*1 + 16*2 = 60 amu."
        },
        {
            "id": f"{lid}_c30",
            "num": 30,
            "type": "short",
            "levelClass": "level-vd",
            "levelName": "Vận dụng",
            "title": "Câu 30: Cho dung dịch chứa 0,1 mol BaCl2 tác dụng vừa đủ với dung dịch Na2SO4. Khối lượng kết tủa BaSO4 (M=233) thu được là bao nhiêu gam?",
            "correctText": "23.3",
            "explanation": "nBaSO4 = 0,1 mol => m = 0,1 * 233 = 23,3 gam."
        },
        {
            "id": f"{lid}_c31",
            "num": 31,
            "type": "short",
            "levelClass": "level-vd",
            "levelName": "Vận dụng",
            "title": "Câu 31: Hydrocarbon butane (C4H10) có tất cả bao nhiêu đồng phân cấu tạo?",
            "correctText": "2",
            "explanation": "C4H10 có 2 đồng phân: butane (mạch thẳng) và isobutane (2-methylpropane)."
        }
    ]

    essay = [
        {
            "id": f"{lid}_c{32 + i}",
            "num": 32 + i,
            "type": "essay",
            "levelClass": "level-th" if i < 5 else ("level-vd" if i < 12 else "level-vdc"),
            "levelName": "Thông hiểu" if i < 5 else ("Vận dụng" if i < 12 else "Vận dụng cao"),
            "title": f"Câu {32 + i}: {title}",
            "explanation": f"Hướng dẫn giải chi tiết cho Câu {32 + i} ({lesson_name}):\n- Bám sát kiến thức trọng tâm SGK Hóa học Kết nối tri thức.\n- Trình bày rõ phương trình hóa học, các bước suy luận và tính toán ra kết quả."
        }
        for i, title in enumerate([
            f"Trình bày định nghĩa và các khái niệm cơ bản liên quan trực tiếp đến nội dung {lesson_name}.",
            "Nêu đặc điểm cấu tạo phân tử và các loại liên kết hóa học chủ yếu của các chất trong bài học.",
            "Viết 2 phương trình hóa học minh họa cho tính chất hóa học đặc trưng nhất của bài học.",
            "Giải thích hiện tượng quan sát được trong thí nghiệm minh họa thực tế của bài học.",
            "So sánh tính chất vật lí (nhiệt độ sôi, nhiệt độ nóng chảy, độ tan) của các chất liên quan.",
            "Nêu vai trò và ảnh hưởng của các điều kiện phản ứng (nhiệt độ, áp suất, chất xúc tác).",
            "Trình bày quy tắc an toàn thực hành khi thao tác với các hóa chất và dụng cụ thí nghiệm của bài.",
            "Giải thích cơ chế hoặc quy luật biến đổi hóa học diễn ra trong các phản ứng trọng tâm.",
            "Nêu các ứng dụng thực tiễn quan trọng của bài học trong đời sống, y học và sản xuất công nghiệp.",
            "Đề xuất phương pháp hóa học để nhận biết hoặc phân biệt các chất đặc trưng trong bài học.",
            "Giải bài toán tính số mol và khối lượng các chất tham gia phản ứng theo định luật bảo toàn khối lượng.",
            "Tính hiệu suất của phản ứng tổng hợp hoặc phản ứng chuyển hóa với các số liệu cụ thể.",
            "Phân tích tác động của các chất trong bài học đối với môi trường và các biện pháp bảo vệ môi trường.",
            "Viết phương trình hóa học biểu diễn chuỗi biến hóa 3 giai đoạn liên quan đến các hợp chất của bài.",
            "Giải thích vì sao một số phản ứng hóa học cần phải đun nóng hoặc cần có mặt chất xúc tác mới diễn ra.",
            "Tính toán nồng độ phần trăm hoặc nồng độ mol của dung dịch thu được sau khi phản ứng kết thúc.",
            "Tổng kết những bài học kinh nghiệm và kiến thức cốt lõi cần ghi nhớ để chuẩn bị cho các kì thi."
        ])
    ]

    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

print("generate_concrete_questions defined.")
