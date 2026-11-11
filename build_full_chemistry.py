# -*- coding: utf-8 -*-
"""
Chemistry 11 Builder Script
Generates lesson-tailored questions and methods for Grade 11 Chemistry.
Every lesson has 100% topic-accurate questions matching its specific domain.
"""

import json

def get_b8_questions():
    # Bài 8: Hợp chất hữu cơ và hóa học hữu cơ
    mcq = [
        ("Chất nào sau đây là hợp chất hữu cơ?", ["CO2", "CaCO3", "C2H5OH", "KCN"], 2, "C2H5OH là hợp chất hữu cơ (alcohol). CO2, CaCO3, KCN là hợp chất vô cơ của carbon."),
        ("Hợp chất hữu cơ nhất thiết phải chứa nguyên tố nào sau đây?", ["Hydrogen", "Carbon", "Oxygen", "Nitrogen"], 1, "Mọi hợp chất hữu cơ đều phải chứa nguyên tố carbon."),
        ("Liên kết hóa học chủ yếu trong phân tử hợp chất hữu cơ là loại liên kết nào?", ["Liên kết ion", "Liên kết cộng hóa trị", "Liên kết kim loại", "Liên kết phi kim"], 1, "Các nguyên tử trong hợp chất hữu cơ liên kết chủ yếu bằng liên kết cộng hóa trị."),
        ("Dãy chất nào sau đây đều gồm các hợp chất hữu cơ?", ["CH4, C2H6, CO2", "C6H12O6, C2H5OH, CH3COOH", "CaC2, CH3Cl, Na2CO3", "CO, HCN, C2H2"], 1, "C6H12O6, C2H5OH, CH3COOH đều là hợp chất hữu cơ."),
        ("Đặc điểm nào sau đây KHÔNG phải là đặc điểm chung của hợp chất hữu cơ?", ["Nhiệt độ nóng chảy và nhiệt độ sôi thường thấp", "Kém bền với nhiệt và dễ cháy", "Liên kết chủ yếu là liên kết ion", "Phản ứng thường xảy ra chậm và tạo hỗn hợp sản phẩm"], 2, "Liên kết trong hợp chất hữu cơ chủ yếu là liên kết cộng hóa trị, không phải liên kết ion."),
        ("Dựa vào thành phần nguyên tố, hợp chất hữu cơ được phân thành hai loại chính là:", ["Hydrocarbon và dẫn xuất của hydrocarbon", "Chất no và chất không no", "Chất mạch hở và chất mạch vòng", "Chất đơn chức và chất đa chức"], 0, "Phân loại lớn theo thành phần gồm Hydrocarbon (chỉ C, H) và Dẫn xuất hydrocarbon (có thêm O, N, S, halogen...)."),
        ("Chất nào sau đây thuộc loại hydrocarbon?", ["CH3Cl", "C2H5OH", "C6H6", "CH3COOH"], 2, "C6H6 (benzene) chỉ chứa C và H nên là hydrocarbon."),
        ("Chất nào sau đây là dẫn xuất của hydrocarbon?", ["CH4", "C2H4", "C3H8", "C2H5Cl"], 3, "C2H5Cl chứa C, H và nguyên tố Cl nên là dẫn xuất hydrocarbon."),
        ("Nhóm nguyên tử gây ra những phản ứng hóa học đặc trưng của phân tử hợp chất hữu cơ được gọi là:", ["Nhóm ankyl", "Nhóm thế", "Nhóm chức", "Gốc tự do"], 2, "Định nghĩa nhóm chức trong hóa học hữu cơ."),
        ("Nhóm chức -OH có tên gọi là gì và đặc trưng cho loại hợp chất nào?", ["Nhóm carboxyl, đặc trưng cho acid", "Nhóm hydroxy, đặc trưng cho alcohol", "Nhóm aldehyde, đặc trưng cho aldehyde", "Nhóm amino, đặc trưng cho amine"], 1, "Nhóm -OH là nhóm hydroxy, đặc trưng cho alcohol và phenol."),
        ("Nhóm chức -COOH đặc trưng cho loại hợp chất hữu cơ nào sau đây?", ["Alcohol", "Aldehyde", "Carboxylic acid", "Ester"], 2, "Nhóm carboxyl (-COOH) đặc trưng cho carboxylic acid."),
        ("Chất nào sau đây chứa nhóm chức aldehyde (-CHO)?", ["CH3COOH", "HCHO", "CH3OH", "CH3COOCH3"], 1, "HCHO (methanal / formaldehyde) chứa nhóm chức aldehyde (-CHO)."),
        ("Nhóm chức ester có dạng cấu tạo nào sau đây?", ["-COOH", "-COO-", "-CHO", "-O-"], 1, "Nhóm ester có dạng -COO- liên kết giữa hai gốc hydrocarbon."),
        ("Hợp chất CH3-NH2 chứa nhóm chức nào sau đây?", ["Nhóm hydroxy", "Nhóm carboxyl", "Nhóm amino", "Nhóm carbonyl"], 2, "CH3-NH2 chứa nhóm amino (-NH2), thuộc loại amine."),
        ("Trong thí nghiệm phân tích định tính nguyên tố C và H, người ta trộn chất hữu cơ với chất nào để nung nóng?", ["CuO khan", "CuSO4 khan", "Ca(OH)2", "NaOH rắn"], 0, "Trộn với CuO làm chất oxi hóa để chuyển C thành CO2 và H thành H2O."),
        ("Để nhận biết hơi nước (H2O) sinh ra trong phản ứng oxi hóa chất hữu cơ, người ta dùng thuốc thử nào?", ["Dung dịch Ca(OH)2", "CuSO4 khan màu trắng", "Dung dịch Br2", "Quỳ tím ẩm"], 1, "CuSO4 khan màu trắng hút nước tạo CuSO4.5H2O có màu xanh lam đặc trưng."),
        ("Để nhận biết khí CO2 sinh ra từ quá trình phân tích định tính C, người ta dẫn khí qua:", ["Dung dịch H2SO4 đặc", "Dung dịch nước vôi trong Ca(OH)2", "Dung dịch CuSO4", "Dung dịch KMnO4"], 1, "Khí CO2 tác dụng với dung dịch Ca(OH)2 tạo kết tủa trắng CaCO3 làm đục nước vôi trong."),
        ("Để định tính nguyên tố nitrogen trong hợp chất hữu cơ, người ta chuyển N thành hợp chất nào sau đây?", ["N2O", "NO2", "NH3", "HNO3"], 2, "Chuyển thành khí NH3, nhận biết bằng quỳ tím ẩm hóa xanh."),
        ("Chất nào sau đây khi cháy hoàn toàn chỉ tạo ra CO2 và H2O?", ["CH3Cl", "C2H5OH", "CH3NH2", "C6H5NO2"], 1, "C2H5OH chỉ chứa C, H, O nên khi cháy hoàn toàn chỉ tạo CO2 và H2O."),
        ("Dung dịch nào sau đây làm quỳ tím chuyển sang màu đỏ?", ["C2H5OH", "CH3COOH", "CH3NH2", "C6H12O6"], 1, "CH3COOH (acetic acid) có tính acid làm quỳ tím hóa đỏ."),
        ("Phát biểu nào sau đây đúng về ngành Hóa học hữu cơ?", ["Chuyên nghiên cứu kim loại và hợp kim", "Chuyên nghiên cứu các hợp chất vô cơ của vỏ Trái Đất", "Chuyên nghiên cứu về các hợp chất hữu cơ", "Chuyên nghiên cứu các phản ứng hạt nhân"], 2, "Hóa học hữu cơ là ngành nghiên cứu cấu trúc, tính chất, tổng hợp và ứng dụng các hợp chất hữu cơ.")
      ]

    tf = [
      ("Câu 22: Xem xét các nhận định về khái niệm và phân loại hợp chất hữu cơ:", [
        ("Mọi hợp chất chứa nguyên tố carbon đều được xếp vào hợp chất hữu cơ.", False),
        ("Hydrocarbon là những hợp chất hữu cơ mà phân tử chỉ gồm hai nguyên tố carbon và hydrogen.", True),
        ("Dẫn xuất hydrocarbon là những hợp chất mà phân tử ngoài C, H còn có các nguyên tố khác như O, N, Cl...", True),
        ("CO, CO2, Na2CO3, Al4C3 đều là hợp chất hữu cơ của carbon.", False)
      ], "Ý 1 và 4 sai vì CO, CO2, muối carbonate, carbide... là hợp chất vô cơ của carbon."),

      ("Câu 23: Về đặc điểm liên kết và tính chất vật lý của hợp chất hữu cơ:", [
        ("Liên kết trong hợp chất hữu cơ chủ yếu là liên kết ion bền vững.", False),
        ("Đa số các hợp chất hữu cơ có nhiệt độ nóng chảy và nhiệt độ sôi thấp hơn hợp chất ion vô cơ.", True),
        ("Hầu hết các hợp chất hữu cơ không tan hoặc ít tan trong nước, nhưng tan tốt trong dung môi hữu cơ.", True),
        ("Các phản ứng hóa học hữu cơ thường diễn ra rất nhanh và chỉ tạo ra một sản phẩm duy nhất.", False)
      ], "Ý 1 sai vì liên kết chủ yếu là cộng hóa trị. Ý 4 sai vì phản ứng hữu cơ thường chậm và tạo hỗn hợp nhiều sản phẩm."),

      ("Câu 24: Về các nhóm chức cơ bản trong phân tử hợp chất hữu cơ:", [
        ("Nhóm chức là nhóm nguyên tử quyết định tính chất hóa học đặc trưng của hợp chất hữu cơ.", True),
        ("Ethanol (C2H5OH) chứa nhóm chức hydroxy (-OH) đặc trưng cho alcohol.", True),
        ("Acetaldehyde (CH3CHO) chứa nhóm chức carboxyl (-COOH) đặc trưng cho acid.", False),
        ("Acetic acid (CH3COOH) có khả năng làm quỳ tím chuyển sang màu đỏ do chứa nhóm -COOH.", True)
      ], "Ý 3 sai vì nhóm -CHO là nhóm aldehyde, nhóm -COOH mới là carboxyl."),

      ("Câu 25: Về phương pháp phân tích định tính nguyên tố trong hợp chất hữu cơ:", [
        ("Bột CuO đóng vai trò là chất khử để oxi hóa hợp chất hữu cơ thành CO2 và H2O.", False),
        ("Bông tẩm CuSO4 khan màu trắng chuyển sang màu xanh lam chứng tỏ có nguyên tố hydrogen.", True),
        ("Dung dịch Ca(OH)2 bị vẩn đục chứng tỏ trong phân tử hợp chất hữu cơ có nguyên tố carbon.", True),
        ("Khí NH3 sinh ra khi phân tích định tính nitrogen có thể làm đổi màu quỳ tím ẩm sang màu đỏ.", False)
      ], "Ý 1 sai vì CuO là chất oxi hóa. Ý 4 sai vì NH3 có tính base làm quỳ tím ẩm hóa xanh.")
    ]

    short = [
      ("Câu 26: Cho các chất: CH4, CO2, C2H5OH, CaCO3, C6H6, KCN, CH3COOH. Có bao nhiêu chất là hợp chất hữu cơ?", "4", "Các chất hữu cơ gồm: CH4, C2H5OH, C6H6, CH3COOH (4 chất)."),
      ("Câu 27: Cho các chất: C2H6, CH3Cl, C2H5OH, C3H8, CH3COOCH3, C4H10. Có bao nhiêu chất là dẫn xuất của hydrocarbon?", "3", "Dẫn xuất hydrocarbon gồm CH3Cl, C2H5OH, CH3COOCH3 (3 chất). C2H6, C3H8, C4H10 là hydrocarbon."),
      ("Câu 28: Trong một phân tử acetic acid (CH3COOH), có bao nhiêu nguyên tử Oxygen?", "2", "CH3COOH có 2 nguyên tử O trong nhóm -COOH."),
      ("Câu 29: Hợp chất ethyl alcohol (C2H5OH) có phân tử khối bằng bao nhiêu amu?", "46", "M = 12*2 + 6*1 + 16 = 46 amu."),
      ("Câu 30: Đốt cháy hoàn toàn 1 mol methane (CH4) cần vừa đủ bao nhiêu mol O2?", "2", "CH4 + 2O2 -> CO2 + 2H2O => cần 2 mol O2."),
      ("Câu 31: Một hợp chất hữu cơ chứa 1 nhóm -OH và 1 nhóm -COOH. Tổng số nguyên tử Oxygen trong một phân tử hợp chất đó là bao nhiêu?", "3", "1 nhóm -OH (1 O) + 1 nhóm -COOH (2 O) = 3 nguyên tử Oxygen.")
    ]

    essay = [
      "Nêu định nghĩa hợp chất hữu cơ và hóa học hữu cơ. Lấy ví dụ 2 hợp chất hữu cơ và 2 hợp chất vô cơ chứa carbon.",
      "Giải thích vì sao số lượng hợp chất hữu cơ đã biết (hơn hàng chục triệu chất) lại nhiều hơn rất nhiều so với hợp chất vô cơ.",
      "Nêu 4 đặc điểm chung về cấu tạo và tính chất vật lý của các hợp chất hữu cơ so với hợp chất vô cơ.",
      "Phân biệt khái niệm Hydrocarbon và Dẫn xuất hydrocarbon. Mỗi loại lấy 2 ví dụ công thức phân tử cụ thể.",
      "Thế nào là nhóm chức? Kể tên và viết kí hiệu của 4 nhóm chức hữu cơ quan trọng mà em đã học.",
      "Trình bày vai trò và hiện tượng xảy ra của bột CuO và CuSO4 khan trong thí nghiệm phân tích định tính C và H.",
      "Viết phương trình hóa học giải thích hiện tượng nước vôi trong bị vẩn đục khi dẫn sản phẩm cháy của hợp chất hữu cơ qua bình chứa Ca(OH)2.",
      "Tại sao khi nung nóng chất hữu cơ với CuO để định tính C và H, trước khi tắt đèn cồn người ta phải tháo ống dẫn khí ra khỏi ống nghiệm đựng dung dịch Ca(OH)2?",
      "Nêu phương pháp phân tích định tính nguyên tố nitrogen trong hợp chất hữu cơ bằng cách chuyển hóa thành ammonia (NH3).",
      "Nêu phương pháp nhận biết sự có mặt của nguyên tố halogen (Cl, Br) trong dẫn xuất hydrocarbon bằng phản ứng với dung dịch AgNO3.",
      "Giải thích vì sao xăng dầu (hỗn hợp hydrocarbon) lại nhẹ hơn nước và nổi trên mặt nước.",
      "Tại sao khi dập tắt đám cháy xăng dầu, người ta tuyệt đối không được dùng nước mà phải dùng cát, chăn ướt hoặc bình bọt CO2?",
      "So sánh độ tan trong nước của ethanol (C2H5OH) và hexane (C6H14). Giải thích ngắn gọn dựa trên cấu tạo phân tử.",
      "Vì sao các phản ứng hóa học của hợp chất hữu cơ thường có tốc độ chậm và cần phải đun nóng hoặc có chất xúc tác?",
      "Viết công thức cấu tạo của 2 chất hữu cơ có cùng công thức phân tử C2H6O và chỉ rõ nhóm chức của mỗi chất.",
      "Nêu một số ứng dụng thực tế quan trọng của các hợp chất hữu cơ trong đời sống hàng ngày (nhiên liệu, thực phẩm, y tế, tơ sợi).",
      "Hãy trình bày quy tắc an toàn cơ bản khi làm việc với các dung môi và hóa chất hữu cơ dễ cháy trong phòng thí nghiệm."
    ]

    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

def get_b9_questions():
    # Bài 9: Phương pháp tách biệt và tinh chế hợp chất hữu cơ
    mcq = [
        ("Phương pháp nào sau đây dùng để tách các chất lỏng có nhiệt độ sôi khác nhau đáng kể trong hỗn hợp đồng nhất?", ["Chiết lỏng - lỏng", "Chưng cất", "Kết tinh lại", "Sắc kí cột"], 1, "Chưng cất dựa trên sự khác nhau về nhiệt độ sôi của các chất lỏng."),
        ("Dụng cụ nào sau đây là thiết bị chính trong phương pháp chiết lỏng - lỏng?", ["Ống sinh hàn", "Bình cầu đáy tròn", "Phễu chiết", "Cột sắc kí"], 2, "Phễu chiết (có khóa) dùng để tách hai lớp chất lỏng không trộn lẫn."),
        ("Phương pháp chưng cất lôi cuốn hơi nước thường được ứng dụng để thu nhận chất nào trong thực tế?", ["Đường ăn", "Muối ăn", "Tinh dầu thực vật (bưởi, sả, tràm)", "Cồn công nghiệp"], 2, "Tinh dầu có Ts cao nhưng dễ bay hơi cùng hơi nước nên dùng chưng cất lôi cuốn hơi nước."),
        ("Để tách riêng dầu ăn ra khỏi hỗn hợp nước và dầu ăn, người ta dùng phương pháp nào?", ["Chưng cất thường", "Chiết lỏng - lỏng", "Kết tinh", "Lọc qua giấy lọc"], 1, "Dầu ăn không tan trong nước và nhẹ hơn nước nên dùng phễu chiết để tách riêng."),
        ("Hoạt động hãm chè khô lấy nước uống hoặc ngâm rượu thuốc là ứng dụng của phương pháp nào?", ["Chiết lỏng - lỏng", "Chiết lỏng - rắn", "Chưng cất lôi cuốn hơi nước", "Kết tinh phân đoạn"], 1, "Hòa tan chất từ pha rắn vào dung môi lỏng là phương pháp chiết lỏng - rắn."),
        ("Phương pháp kết tinh dùng để tinh chế các hợp chất ở trạng thái nào?", ["Chất khí", "Chất lỏng", "Chất rắn", "Hỗn hợp nhũ tương"], 2, "Kết tinh dùng để làm sạch và thu hồi các chất rắn tinh khiết."),
        ("Dung môi thích hợp để kết tinh lại một chất rắn cần thỏa mãn điều kiện nào sau đây?", ["Hòa tan tốt chất ở nhiệt độ cao và hòa tan kém ở nhiệt độ thấp", "Hòa tan tốt chất ở mọi nhiệt độ", "Không hòa tan chất ở bất kỳ nhiệt độ nào", "Có nhiệt độ sôi cao hơn 200°C"], 0, "Dung môi phải hòa tan tốt ở nhiệt độ sôi và hòa tan kém ở nhiệt độ thấp để chất dễ kết tinh khi làm nguội."),
        ("Trong phương pháp sắc kí cột, pha tĩnh thường là chất nào sau đây?", ["Nước cất", "Silica gel hoặc Alumina", "Cồn ethanol", "Khí nitrogen"], 1, "Pha tĩnh là chất rắn có diện tích bề mặt lớn, có khả năng hấp phụ (silica gel SiO2 hoặc alumina Al2O3)."),
        ("Trong phương pháp sắc kí cột, chất nào sẽ di chuyển ra khỏi cột sắc kí trước?", ["Chất bị hấp phụ mạnh hơn trên pha tĩnh", "Chất bị hấp phụ yếu hơn trên pha tĩnh", "Chất có khối lượng phân tử lớn hơn", "Chất có màu đậm hơn"], 1, "Chất bị pha tĩnh hấp phụ yếu hơn sẽ bị pha động rửa trôi nhanh hơn và ra khỏi cột trước."),
        ("Khi nấu rượu etylic thủ công từ cơm rượu lên men, người ta áp dụng phương pháp nào?", ["Phương pháp chiết", "Phương pháp chưng cất", "Phương pháp kết tinh", "Phương pháp thăng hoa"], 1, "Ethanol có Ts = 78,3°C thấp hơn nước (100°C) nên bay hơi trước trong quá trình chưng cất."),
        ("Đá bọt (mảnh sứ xốp) cho vào bình cầu chưng cất có tác dụng gì?", ["Làm tăng nhiệt độ sôi của hỗn hợp", "Giúp chất lỏng sôi êm dịu, tránh hiện tượng quá sôi làm trào chất lỏng", "Làm xúc tác cho phản ứng hóa học", "Hút sạch tạp chất bẩn"], 1, "Đá bọt tạo các tâm bọt khí giúp chất lỏng sôi đều và êm dịu."),
        ("Trong bộ dụng cụ chưng cất, nước làm mát được dẫn vào ống sinh hàn theo chiều nào?", ["Vào từ đầu dưới và ra ở đầu trên", "Vào từ đầu trên và ra ở đầu dưới", "Vào cả hai đầu cùng một lúc", "Không cần dẫn nước lưu thông"], 0, "Nguyên tắc: nước làm mát đi vào từ đầu dưới và ra ở đầu trên để ống sinh hàn luôn ngập đầy nước làm mát hiệu quả nhất."),
        ("Nhiệt kế cắm vào bình chưng cất có bầu thủy ngân đặt ở vị trí nào là chuẩn xác?", ["Chìm sâu dưới đáy bình chất lỏng", "Ngang với miệng nhánh dẫn hơi của bình cầu", "Đặt phía ngoài ống sinh hàn", "Đặt lơ lửng trên nắp bình"], 1, "Đặt ngang miệng nhánh dẫn hơi để đo chính xác nhiệt độ sôi của luồng hơi đang bay qua ống sinh hàn."),
        ("Khi tiến hành chiết lỏng - lỏng bằng phễu chiết, thao tác nào sau đây là BẮT BUỘC?", ["Đun sôi phễu chiết trên ngọn lửa đèn cồn", "Lắc đều và định kì mở khóa phễu để xả áp suất khí", "Đậy kín nắp phễu khi mở khóa xả chất lỏng", "Dùng đũa thủy tinh khuấy liên tục"], 1, "Cần lắc đều và thường xuyên dốc ngược phễu mở khóa xả bớt áp suất khí sinh ra."),
        ("Khi mở khóa phễu chiết để tách hai chất lỏng không trộn lẫn, ta thực hiện như thế nào?", ["Mở nắp trên của phễu rồi mở khóa từ từ xả lớp chất lỏng phía dưới", "Đậy chặt nắp phễu rồi xả cả hai lớp cùng lúc", "Đổ ngược toàn bộ qua miệng phễu", "Dùng ống hút để hút lớp trên ra trước"], 0, "Phải mở nắp phễu để thông khí quyển, sau đó mở khóa xả lớp chất lỏng nặng ở dưới ra bình hứng."),
        ("Để tách chất màu trong lá cây (chlorophyll và carotenoid), phương pháp tách chất thích hợp nhất là:", ["Chưng cất lôi cuốn hơi nước", "Kết tinh lại", "Sắc kí cột", "Thăng hoa"], 2, "Sắc kí cột (hoặc sắc kí bản mỏng) dùng để tách hỗn hợp các chất màu phức tạp."),
        ("Để thu được tinh thể muối ăn NaCl từ nước biển, diêm dân đã dùng phương pháp nào?", ["Chưng cất lôi cuốn hơi nước", "Kết tinh (làm bay hơi nước nhờ năng lượng mặt trời)", "Chiết lỏng - lỏng", "Sắc kí"], 1, "Cho nước biển bay hơi nước dưới nắng gió để NaCl kết tinh lắng xuống."),
        ("Tách đường saccharose tinh khiết từ nước mía ép bằng phương pháp cô đặc và để nguội là ứng dụng của:", ["Phương pháp kết tinh", "Phương pháp chiết", "Phương pháp chưng cất", "Phương pháp sắc kí"], 0, "Cô đặc dung dịch nước mía rồi hạ nhiệt độ cho đường kết tinh."),
        ("Caffeine tan tốt trong dung môi hữu cơ dichloromethane và tan ít trong nước. Để tách caffeine từ nước trà, ta dùng:", ["Phương pháp chiết lỏng - lỏng", "Phương pháp lọc qua bông", "Phương pháp đun sôi bay hơi nước", "Phương pháp điện phân"], 0, "Dùng dichloromethane chiết caffeine ra khỏi pha nước trà."),
        ("Ưu điểm nổi bật của phương pháp chiết nhiều lần với lượng nhỏ dung môi so với chiết một lần với lượng lớn dung môi là:", ["Tiết kiệm thời gian hơn", "Hiệu suất tách chiết chất tan cao hơn nhiều", "Dễ quan sát màu sắc hơn", "Không cần phễu chiết"], 1, "Chiết nhiều lần bằng lượng nhỏ dung môi luôn cho lượng chất tan chiết được lớn hơn và kiệt hơn."),
        ("Chất rắn sau khi kết tinh lại được tách ra khỏi dung dịch mẹ bằng thao tác nào?", ["Chưng cất", "Lọc (lọc thường hoặc lọc hút chân không)", "Chiết", "Đun sôi"], 1, "Dùng phễu lọc để lọc lấy tinh thể rắn và rửa bằng dung môi lạnh.")
      ]

    tf = [
      ("Câu 22: Xem xét các phát biểu về phương pháp chưng cất:", [
        ("Chưng cất dùng để tách các chất lỏng có nhiệt độ sôi khác nhau trong hỗn hợp đồng nhất.", True),
        ("Chất có nhiệt độ sôi cao hơn sẽ bay hơi trước và ngưng tụ ở bình hứng trước.", False),
        ("Nước làm mát trong ống sinh hàn phải chảy từ đầu thấp (dưới) lên đầu cao (trên).", True),
        ("Chưng cất lôi cuốn hơi nước phù hợp để tách các tinh dầu có nhiệt độ sôi cao và dễ bay hơi theo hơi nước.", True)
      ], "Ý 2 sai vì chất có nhiệt độ sôi THẤP HƠN sẽ bay hơi trước."),

      ("Câu 23: Về phương pháp chiết trong hóa học:", [
        ("Chiết lỏng - lỏng dựa vào độ tan khác nhau của chất tan trong hai dung môi không trộn lẫn vào nhau.", True),
        ("Có thể dùng phễu chiết để tách riêng hỗn hợp gồm nước và rượu ethanol.", False),
        ("Pha trà, ngâm sâm trong rượu là các ví dụ thực tế về phương pháp chiết lỏng - rắn.", True),
        ("Trong phễu chiết, chất lỏng nào có khối lượng riêng lớn hơn sẽ chìm ở lớp dưới.", True)
      ], "Ý 2 sai vì ethanol và nước tan vô hạn vào nhau tạo dung dịch đồng nhất, không phân lớp nên không thể chiết lỏng - lỏng."),

      ("Câu 24: Về phương pháp kết tinh và tinh chế chất rắn:", [
        ("Kết tinh lại dựa vào độ tan của chất rắn thay đổi theo nhiệt độ trong một dung môi thích hợp.", True),
        ("Dung môi kết tinh cần hòa tan tốt tạp chất ở nhiệt độ cao và kết tinh cùng với chất cần lấy.", False),
        ("Bước lọc nóng trong quy trình kết tinh lại nhằm loại bỏ các tạp chất không tan.", True),
        ("Sau khi để nguội dung dịch bão hòa, chất rắn sẽ kết tinh dưới dạng tinh thể tinh khiết.", True)
      ], "Ý 2 sai vì dung môi không được làm tạp chất kết tinh cùng với chất chính."),

      ("Câu 25: Về phương pháp sắc kí cột:", [
        ("Sắc kí cột gồm hai pha: pha tĩnh (chất rắn hấp phụ) và pha động (dung môi lỏng hòa tan).", True),
        ("Các chất di chuyển qua cột sắc kí với tốc độ giống nhau hoàn toàn.", False),
        ("Chất bị pha tĩnh hấp phụ mạnh hơn sẽ di chuyển chậm hơn và ra khỏi cột sau.", True),
        ("Sắc kí cột có thể dùng để tách các chất màu có cấu trúc và tính chất rất gần nhau.", True)
      ], "Ý 2 sai vì các chất có khả năng hấp phụ khác nhau nên di chuyển với tốc độ khác nhau.")
    ]

    short = [
      ("Câu 26: Cho 4 phương pháp: Chưng cất, Chiết, Kết tinh, Sắc kí. Có bao nhiêu phương pháp thường dùng để tinh chế chất ở trạng thái rắn?", "1", "Chỉ có phương pháp Kết tinh (1 phương pháp) chuyên dùng tinh chế chất rắn."),
      ("Câu 27: Nhiệt độ sôi của ethanol nguyên chất ở áp suất khí quyển chuẩn là bao nhiêu °C? (Lấy số nguyên gần đúng)", "78", "Nhiệt độ sôi của ethanol là 78,3°C (làm tròn số nguyên: 78)."),
      ("Câu 28: Từ 10 kg lá sả tươi chứa 2% tinh dầu, qua chưng cất thu được 160 gam tinh dầu nguyên chất. Hiệu suất chưng cất tinh dầu đạt bao nhiêu %?", "80", "m_lí thuyết = 10000 * 2% = 200 g. H% = (160 / 200) * 100% = 80%."),
      ("Câu 29: Hòa tan 50 gam đường thô bẩn vào nước sôi. Sau khi kết tinh lại thu được 40 gam đường tinh khiết. Phần trăm khối lượng đường thu hồi được là bao nhiêu %?", "80", "% thu hồi = (40 / 50) * 100% = 80%."),
      ("Câu 30: Cho 100 mL dung dịch nước chứa 2,0 gam chất X. Hệ số phân bố giữa ether và nước là K = 3. Khi chiết với 100 mL ether, khối lượng X (gam) còn lại trong nước là bao nhiêu? (Lấy 1 chữ số thập phân, dạng 0.5)", "0.5", "K = (x/100) / ((2-x)/100) = 3 => x/(2-x) = 3 => x = 6 - 3x => 4x = 6 => x = 1,5 g (vào ether) => còn trong nước = 2 - 1,5 = 0,5 gam."),
      ("Câu 31: Khi chưng cất phân đoạn hỗn hợp 3 chất lỏng có Ts lần lượt là 65°C, 78°C và 100°C, chất có Ts bao nhiêu °C sẽ bay hơi và ngưng tụ ra khỏi hệ thống đầu tiên?", "65", "Chất có nhiệt độ sôi thấp nhất (65°C) sẽ bay hơi và ngưng tụ đầu tiên.")
    ]

    essay = [
      "Trình bày nguyên tắc chung và các bộ phận chính của bộ dụng cụ chưng cất chất lỏng trong phòng thí nghiệm.",
      "Tại sao khi lắp ống sinh hàn làm mát trong chưng cất, dòng nước làm mát phải đi vào từ đầu dưới và ra ở đầu trên?",
      "Nêu vai trò của nhiệt kế và đá bọt trong quá trình chưng cất chất lỏng.",
      "Phân biệt phương pháp chưng cất thường và phương pháp chưng cất lôi cuốn hơi nước. Nêu ví dụ ứng dụng của từng phương pháp.",
      "Trình bày quy trình sản xuất tinh dầu bưởi hoặc tinh dầu sả bằng phương pháp chưng cất lôi cuốn hơi nước.",
      "Thế nào là phương pháp chiết? Phân biệt chiết lỏng - lỏng và chiết lỏng - rắn. Lấy ví dụ minh họa trong đời sống.",
      "Mô tả các thao tác chuẩn khi sử dụng phễu chiết để tách hai chất lỏng không trộn lẫn vào nhau.",
      "Tại sao trong quá trình chiết lỏng - lỏng, người ta phải định kì dốc ngược phễu chiết và mở khóa xả áp suất khí?",
      "Giải thích vì sao chiết nhiều lần với lượng nhỏ dung môi lại cho hiệu suất tách chất cao hơn chiết 1 lần với toàn bộ lượng dung môi đó.",
      "Trình bày các tiêu chuẩn chọn dung môi thích hợp cho quá trình tinh chế chất rắn bằng phương pháp kết tinh lại.",
      "Mô tả quy trình 4 bước cơ bản để làm sạch một chất rắn bằng phương pháp kết tinh lại trong phòng thí nghiệm.",
      "Tại sao trong phương pháp kết tinh lại, người ta phải lọc nóng dung dịch bão hòa thay vì để nguội rồi mới lọc?",
      "Nêu nguyên tắc hoạt động của phương pháp sắc kí cột. Định nghĩa pha tĩnh và pha động.",
      "Yếu tố nào quyết định thứ tự các chất di chuyển ra khỏi cột sắc kí trong phương pháp sắc kí cột?",
      "Đề xuất phương pháp phù hợp để tách riêng từng chất trong hỗn hợp gồm: nước, cát mịn, muối ăn (NaCl) và dầu hỏa.",
      "Trình bày cách tách caffeine ra khỏi nước chè xanh bằng phương pháp chiết dùng dung môi hữu cơ dichloromethane.",
      "Nêu các biện pháp an toàn khi sử dụng các dung môi hữu cơ dễ bay hơi, dễ cháy (ether, cồn, acetone, hexane) trong phòng thí nghiệm."
    ]

    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

def get_b10_questions():
    # Bài 10: Công thức phân tử hợp chất hữu cơ
    mcq = [
        ("Công thức đơn giản nhất của hợp chất hữu cơ cho biết thông tin nào sau đây?", ["Số lượng nguyên tử thực tế của mỗi nguyên tố", "Tỉ lệ số nguyên tử tối giản giữa các nguyên tố trong phân tử", "Cấu trúc không gian của phân tử", "Thứ tự liên kết giữa các nguyên tử"], 1, "CTĐGN cho biết tỉ lệ số nguyên tử nguyên tối giản giữa các nguyên tố."),
        ("Công thức phân tử của hợp chất hữu cơ cho biết thông tin gì?", ["Số lượng thực tế nguyên tử của mỗi nguyên tố trong một phân tử", "Vị trí của nhóm chức", "Mạch cacbon phân nhánh hay không", "Tính chất vật lý của chất"], 0, "CTPT cho biết số lượng nguyên tử thực tế của mỗi nguyên tố."),
        ("Phương pháp hiện đại phổ biến nhất hiện nay để xác định phân tử khối của hợp chất hữu cơ là:", ["Phương pháp đo áp suất thẩm thấu", "Phương pháp nghiệm lạnh", "Phổ khối lượng (MS)", "Phổ hồng ngoại (IR)"], 2, "Phổ khối lượng MS (Mass Spectrometry) dùng để xác định phân tử khối chính xác."),
        ("Trên phổ khối lượng MS, giá trị m/z của pic ion phân tử kí hiệu là gì và tương ứng với đại lượng nào?", ["[M+], tương ứng với phân tử khối", "[Base], tương ứng với khối lượng mẫu", "[H+], tương ứng với số nguyên tử H", "[C+], tương ứng với số nguyên tử C"], 0, "Pic ion phân tử kí hiệu là [M+], có m/z bằng phân tử khối M của chất."),
        ("Hợp chất X có công thức đơn giản nhất là CH2 và phân tử khối M = 42. Công thức phân tử của X là:", ["CH2", "C2H4", "C3H6", "C4H8"], 2, "(CH2)n có M = 14n = 42 => n = 3. CTPT là C3H6."),
        ("Hợp chất hữu cơ Y có công thức đơn giản nhất là CH2O. Phổ MS của Y cho thấy pic [M+] ở m/z = 60. Công thức phân tử của Y là:", ["CH2O", "C2H4O2", "C3H6O3", "C4H8O4"], 1, "M = 30n = 60 => n = 2. CTPT là C2H4O2."),
        ("Phân tích thành phần một hydrocarbon cho %C = 85,71% và %H = 14,29%. Công thức đơn giản nhất của hydrocarbon này là:", ["CH", "CH2", "CH3", "C2H5"], 1, "nC : nH = (85,71/12) : (14,29/1) = 7,14 : 14,29 = 1 : 2 => CTĐGN là CH2."),
        ("Hai hợp chất C2H2 (acetylene) và C6H6 (benzene) có cùng:", ["Công thức phân tử", "Công thức đơn giản nhất", "Phân tử khối", "Nhiệt độ sôi"], 1, "Cả hai đều có công thức đơn giản nhất là CH."),
        ("Hợp chất hữu cơ Z chứa 40% C, 6,67% H và 53,33% O về khối lượng. Tỉ lệ mol nC : nH : nO là:", ["1 : 1 : 1", "1 : 2 : 1", "2 : 4 : 1", "1 : 3 : 1"], 1, "40/12 : 6,67/1 : 53,33/16 = 3,33 : 6,67 : 3,33 = 1 : 2 : 1."),
        ("Đốt cháy hoàn toàn một hợp chất hữu cơ chỉ thu được CO2 và H2O. Kết luận nào sau đây chắc chắn đúng?", ["Hợp chất đó chỉ chứa hai nguyên tố C và H", "Hợp chất đó chắc chắn có chứa C, H và có thể có O", "Hợp chất đó chắc chắn chứa N", "Hợp chất đó là một alkane"], 1, "Sản phẩm cháy là CO2 và H2O chứng tỏ có C, H; nguyên tố O có thể có trong hợp chất hoặc lấy từ O2 khí quyển."),
        ("Đốt cháy hoàn toàn 4,6 gam chất X thu được 4,48 lít CO2 (đktc) và 5,4 gam H2O. Khối lượng O trong 4,6 gam X là:", ["1,6 gam", "0,8 gam", "2,4 gam", "0 gam"], 0, "nC = 0,2 mol (2,4g C); nH = 2 * (5,4/18) = 0,6 mol (0,6g H). mO = 4,6 - 2,4 - 0,6 = 1,6 gam."),
        ("Khí hydrocarbon X có tỉ khối đối với heli (He, M=4) bằng 7. Phân tử khối của X là:", ["14", "28", "42", "56"], 1, "M_X = 7 * 4 = 28 (C2H4)."),
        ("Tỉ khối hơi của ester Y so với không khí (M_kk = 29) xấp xỉ 2,07. Phân tử khối của Y là:", ["60", "74", "88", "102"], 0, "M = 2,07 * 29 ≈ 60 amu (HCOOCH3)."),
        ("Nicotine trong thuốc lá có phân tích nguyên tố: %C = 74,07%, %H = 8,64%, %N = 17,29%. Tỉ lệ tối giản C : H : N là:", ["5 : 7 : 1", "4 : 5 : 1", "10 : 14 : 2", "3 : 4 : 1"], 0, "74,07/12 : 8,64/1 : 17,29/14 = 6,17 : 8,64 : 1,235 = 5 : 7 : 1 (C5H7N)."),
        ("Một hydrocarbon có CTPT là CnH2n+2. Khi n = 4, phân tử khối của hydrocarbon đó là:", ["44", "58", "72", "86"], 1, "C4H10 có M = 12*4 + 10 = 58 amu."),
        ("Chất nào sau đây có công thức đơn giản nhất trùng với công thức phân tử?", ["C2H4", "C6H6", "C2H6O", "C4H8O2"], 2, "C2H6O có tỉ lệ 2:6:1 tối giản nên CTĐGN trùng với CTPT là C2H6O."),
        ("Phổ MS của aspirin cho thấy pic ion phân tử [M+] xuất hiện tại m/z = 180. Phân tử khối của aspirin là:", ["90 amu", "180 amu", "360 amu", "120 amu"], 1, "Phân tử khối M bằng giá trị m/z của pic [M+] = 180 amu."),
        ("Đốt cháy hoàn toàn 0,1 mol hydrocarbon Q thu được 0,3 mol CO2 và 0,4 mol H2O. Công thức phân tử của Q là:", ["CH4", "C2H6", "C3H8", "C4H10"], 2, "Số C = 0,3 / 0,1 = 3; Số H = 2 * 0,4 / 0,1 = 8 => C3H8."),
        ("Khi đốt cháy hoàn toàn một hydrocarbon A, nếu nCO2 = nH2O thì công thức phân tử của A có dạng chung là:", ["CnH2n+2", "CnH2n", "CnH2n-2", "CnH2n-6"], 1, "Đốt cháy hydrocarbon mạch hở cho nCO2 = nH2O thì đó là alkene CnH2n."),
        ("Một hợp chất chứa C, H, O có phân tử khối M = 46. Biết số nguyên tử C là 2 và hợp chất phản ứng được với Na. CTPT của chất đó là:", ["C2H4O", "C2H6O", "CH2O2", "C3H8O"], 1, "C2H6O (M = 46), tác dụng với Na là ethanol C2H5OH."),
        ("Mối quan hệ giữa công thức phân tử (CTPT) và công thức đơn giản nhất (CTĐGN) được biểu diễn qua hệ thức:", ["CTPT = (CTĐGN) * n (với n nguyên dương)", "CTPT luôn bằng 2 lần CTĐGN", "CTPT luôn nhỏ hơn CTĐGN", "Không có mối liên hệ nào"], 0, "CTPT = (CTĐGN)n với n là số nguyên dương (n ≥ 1).")
      ]

    tf = [
      ("Câu 22: Xem xét các khẳng định về các loại công thức của hợp chất hữu cơ:", [
        ("Công thức đơn giản nhất cho biết tỉ lệ số nguyên tử tối giản giữa các nguyên tố trong phân tử.", True),
        ("Hai chất có công thức phân tử khác nhau thì không thể có cùng công thức đơn giản nhất.", False),
        ("Công thức phân tử luôn cho biết số lượng nguyên tử thực tế của mỗi nguyên tố trong phân tử.", True),
        ("Hợp chất C2H5OH có công thức đơn giản nhất trùng với công thức phân tử là C2H6O.", True)
      ], "Ý 2 sai vì ví dụ C2H2 và C6H6 có CTPT khác nhau nhưng cùng CTĐGN là CH."),

      ("Câu 23: Về phương pháp xác định phân tử khối bằng phổ khối lượng (MS):", [
        ("Trong phổ khối lượng, pic ion phân tử [M+] thường có giá trị m/z lớn nhất.", True),
        ("Giá trị m/z của pic ion phân tử [M+] cho biết trực tiếp phân tử khối M của chất phân tích.", True),
        ("Pic có cường độ tương đối 100% luôn luôn là pic ion phân tử [M+].", False),
        ("Dựa vào phổ MS có thể phân biệt được hai chất có phân tử khối khác nhau.", True)
      ], "Ý 3 sai vì pic có cường độ 100% là pic cơ bản (base peak), có thể là mảnh ion phân đoạn."),

      ("Câu 24: Về phương pháp xác định CTPT từ thành phần phần trăm khối lượng:", [
        ("Biết phần trăm khối lượng các nguyên tố giúp tìm được công thức đơn giản nhất.", True),
        ("Chỉ cần biết phần trăm khối lượng các nguyên tố là đủ để xác định chính xác công thức phân tử.", False),
        ("Để tìm được CTPT từ CTĐGN, cần phải biết thêm phân tử khối (M) của hợp chất.", True),
        ("Hợp chất có %C = 40%, %H = 6,67%, %O = 53,33% có công thức đơn giản nhất là CH2O.", True)
      ], "Ý 2 sai vì từ % khối lượng chỉ tìm được CTĐGN, phải có thêm phân tử khối mới tìm được CTPT."),

      ("Câu 25: Về phản ứng đốt cháy hợp chất hữu cơ chứa C, H, O:", [
        ("Số mol nguyên tử C trong hợp chất luôn bằng số mol CO2 thu được sau phản ứng cháy.", True),
        ("Số mol nguyên tử H trong hợp chất bằng số mol H2O thu được sau phản ứng cháy.", False),
        ("Khối lượng nguyên tố O trong hợp chất tính bằng: m_hợp chất - (m_C + m_H).", True),
        ("Nếu đốt cháy một hydrocarbon thu được nH2O > nCO2 thì hydrocarbon đó là alkane.", True)
      ], "Ý 2 sai vì nH = 2 * nH2O (mỗi phân tử nước có 2 nguyên tử H).")
    ]

    short = [
      ("Câu 26: Phổ MS của một hợp chất hữu cơ X cho pic ion phân tử [M+] ở m/z = 74. Phân tử khối của X bằng bao nhiêu amu?", "74", "m/z của [M+] = 74 => Phân tử khối M = 74 amu."),
      ("Câu 27: Một hợp chất hữu cơ Y có công thức đơn giản nhất là C2H5 và phân tử khối M = 58. Trong một phân tử Y có bao nhiêu nguyên tử Carbon?", "4", "(C2H5)n có M = 29n = 58 => n = 2. CTPT là C4H10 (có 4 nguyên tử C)."),
      ("Câu 28: Đốt cháy hoàn toàn 0,2 mol hydrocarbon Z thu được 0,6 mol CO2. Số nguyên tử Carbon trong phân tử Z là bao nhiêu?", "3", "Số C = nCO2 / nZ = 0,6 / 0,2 = 3."),
      ("Câu 29: Đốt cháy hoàn toàn một hydrocarbon thu được 8,8 gam CO2 (0,2 mol) và 5,4 gam H2O (0,3 mol). Tỉ lệ số nguyên tử H : C trong phân tử đó là bao nhiêu? (Điền số nguyên)", "3", "nH = 2*0,3 = 0,6 mol; nC = 0,2 mol => nH : nC = 0,6 : 0,2 = 3 : 1 (tỉ lệ H:C = 3)."),
      ("Câu 30: Một ester có công thức đơn giản nhất là C2H4O và có phân tử khối M = 88. Hệ số n trong hệ thức CTPT = (CTĐGN)n là bao nhiêu?", "2", "M(C2H4O) = 44. Ta có 44n = 88 => n = 2."),
      ("Câu 31: Khối lượng phân tử của hợp chất C3H6O2 là bao nhiêu amu?", "74", "M = 12*3 + 1*6 + 16*2 = 36 + 6 + 32 = 74 amu.")
    ]

    essay = [
      "Định nghĩa Công thức đơn giản nhất, Công thức phân tử và Công thức cấu tạo. Nêu mối liên hệ giữa chúng.",
      "Cho ví dụ 3 cặp chất khác nhau nhưng có cùng công thức đơn giản nhất.",
      "Trình bày nguyên tắc xác định phân tử khối của hợp chất hữu cơ dựa trên phương pháp phổ khối lượng (MS).",
      "Thế nào là pic ion phân tử [M+] và pic cơ bản trong phổ khối lượng MS?",
      "Trình bày các bước thiết lập công thức đơn giản nhất từ phần trăm khối lượng của các nguyên tố C, H, O.",
      "Một hợp chất hữu cơ X chứa 85,71% C và 14,29% H về khối lượng. Tìm công thức đơn giản nhất của X.",
      "Hợp chất hữu cơ Y có công thức đơn giản nhất là CH2O và phân tử khối M = 60. Tìm công thức phân tử của Y.",
      "Đốt cháy hoàn toàn 4,4 gam chất hữu cơ A chứa C, H, O thu được 8,8 gam CO2 và 3,6 gam H2O. Tính khối lượng nguyên tố C, H, O trong A.",
      "Từ kết quả phân tích định lượng của chất A ở câu trên, hãy tìm công thức đơn giản nhất của A.",
      "Biết phân tử khối của chất A ở câu trên là 88 amu. Hãy xác định công thức phân tử của A.",
      "Đốt cháy hoàn toàn 0,1 mol một hydrocarbon B cần dùng vừa đủ 0,5 mol O2 thu được 0,3 mol CO2 và 0,4 mol H2O. Tìm CTPT của B.",
      "Trình bày cách tính phân tử khối của chất khí hoặc hơi dựa vào tỉ khối hơi đối với không khí hoặc khí hydrogen.",
      "Vitamin C (ascorbic acid) chứa 40,91% C, 4,55% H và 54,54% O về khối lượng. Phân tử khối xác định bằng phổ MS là 176. Tìm CTPT của vitamin C.",
      "Nicotine có CTPT là C10H14N2. Hãy tính phần trăm khối lượng của nguyên tố nitrogen trong nicotine.",
      "Vì sao khi đốt cháy hợp chất hữu cơ chứa C, H, O trong bình kín với O2 dư, thể tích khí giảm đi sau khi ngưng tụ hơi nước?",
      "Trình bày phương pháp tính số nguyên tử Carbon và Hydrogen trực tiếp từ tỉ lệ số mol CO2 và H2O khi đốt cháy hoàn toàn hydrocarbon.",
      "Nêu ý nghĩa thực tiễn của việc xác định chính xác công thức phân tử trong việc nghiên cứu và tổng hợp các loại thuốc tân dược."
    ]

    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

def get_b11_questions():
    # Bài 11: Cấu trúc phân tử hợp chất hữu cơ
    mcq = [
        ("Thuyết cấu tạo hóa học do nhà hóa học nào đề xướng vào năm 1861?", ["D.I. Mendeleev", "A.M. Butlerov", "A. Lavoisier", "J. Dalton"], 1, "A.M. Butlerov đề xướng Thuyết cấu tạo hóa học năm 1861."),
        ("Theo thuyết cấu tạo hóa học, nguyên tử carbon luôn thể hiện hóa trị mấy trong hợp chất hữu cơ?", ["II", "III", "IV", "I"], 2, "Carbon luôn luôn có hóa trị IV."),
        ("Các nguyên tử carbon trong phân tử hợp chất hữu cơ có thể liên kết với nhau tạo thành các loại mạch nào?", ["Chỉ mạch thẳng", "Chỉ mạch nhánh", "Mạch hở (không phân nhánh, phân nhánh) và mạch vòng", "Chỉ mạch vòng"], 2, "Carbon có thể tạo mạch không nhánh, mạch nhánh và mạch vòng."),
        ("Tính chất của các hợp chất hữu cơ phụ thuộc vào yếu tố nào sau đây?", ["Chỉ thành phần nguyên tố", "Chỉ khối lượng phân tử", "Thành phần nguyên tố và cấu tạo hóa học", "Chỉ nhiệt độ môi trường"], 2, "Tính chất phụ thuộc vào thành phần nguyên tố và cấu tạo hóa học (trật tự liên kết)."),
        ("Hiện tượng các chất khác nhau nhưng có cùng công thức phân tử được gọi là:", ["Hiện tượng đồng vị", "Hiện tượng đồng đẳng", "Hiện tượng đồng phân", "Hiện tượng thù hình"], 2, "Cùng CTPT nhưng khác CTCT là hiện tượng đồng phân."),
        ("Cặp chất nào sau đây là đồng phân của nhau?", ["CH3-O-CH3 và CH3-CH2-OH", "CH4 và C2H6", "CH3OH và C2H5OH", "C2H4 và C3H6"], 0, "CH3-O-CH3 (dimethyl ether) và C2H5OH (ethanol) có cùng CTPT là C2H6O."),
        ("Những hợp chất có thành phần phân tử hơn kém nhau một hay nhiều nhóm -CH2- nhưng có tính chất hóa học tương tự nhau gọi là:", ["Các chất đồng vị", "Các chất đồng đẳng", "Các chất đồng phân", "Các chất đồng khối"], 1, "Định nghĩa dãy đồng đẳng."),
        ("Dãy chất nào sau đây hợp thành một dãy đồng đẳng?", ["CH4, C2H4, C3H6", "CH4, C2H6, C3H8, C4H10", "CH3OH, C2H5OH, CH3COOH", "C2H2, C3H6, C4H8"], 1, "Dãy alkane: CH4, C2H6, C3H8, C4H10... cùng dãy đồng đẳng."),
        ("Hợp chất butane (C4H10) có bao nhiêu đồng phân cấu tạo?", ["1", "2", "3", "4"], 1, "C4H10 có 2 đồng phân: butane (mạch thẳng) và isobutane (mạch nhánh)."),
        ("Hợp chất pentane (C5H12) có bao nhiêu đồng phân cấu tạo?", ["2", "3", "4", "5"], 1, "C5H12 có 3 đồng phân: pentane, isopentane và neopentane."),
        ("Ứng với CTPT C3H8O có bao nhiêu đồng phân alcohol (chứa nhóm -OH)?", ["1", "2", "3", "4"], 1, "Có 2 đồng phân alcohol: propan-1-ol và propan-2-ol."),
        ("Ứng với CTPT C3H8O có bao nhiêu đồng phân cấu tạo (gồm cả alcohol và ether)?", ["2", "3", "4", "5"], 1, "Có 3 đồng phân: 2 alcohol (propan-1-ol, propan-2-ol) và 1 ether (CH3-O-C2H5)."),
        ("Đồng phân hình học (cis - trans) thường xuất hiện ở hợp chất có chứa đặc điểm cấu tạo nào?", ["Liên kết ba C≡C", "Liên kết đôi C=C", "Liên kết đơn C-C", "Vòng benzen"], 1, "Đồng phân cis-trans xuất hiện khi có liên kết đôi C=C (hoặc mạch vòng) cản trở quay tự do."),
        ("Điều kiện cần và đủ để alkene R1R2C=CR3R4 có đồng phân hình học là:", ["R1 khác R2 và R3 khác R4", "R1 giống R2", "R3 giống R4", "Tất cả các nhóm R đều giống nhau"], 0, "Mỗi nguyên tử C ở nối đôi phải liên kết với 2 nhóm nguyên tử khác nhau: R1 ≠ R2 và R3 ≠ R4."),
        ("Chất nào sau đây CÓ đồng phân hình học cis - trans?", ["CH2=CH-CH2-CH3 (but-1-ene)", "CH3-CH=CH-CH3 (but-2-ene)", "CH2=C(CH3)2 (2-methylpropene)", "CH2=CH2 (ethene)"], 1, "But-2-ene có dạng CH3-CH=CH-CH3 thỏa mãn điều kiện nên có đồng phân cis và trans."),
        ("Chất nào sau đây KHÔNG có đồng phân hình học?", ["CH3-CH=CH-C2H5", "CH3-CH=CH-CH3", "CH2=CH-CH3", "CHCl=CHCl"], 2, "Propene (CH2=CH-CH3) có C đầu liên kết với 2 nguyên tử H giống nhau nên không có đồng phân hình học."),
        ("Trong đồng phân cis của but-2-ene, hai nhóm methyl (-CH3) nằm ở vị trí nào so với mặt phẳng liên kết đôi?", ["Cùng một phía", "Khác phía (đối diện nhau)", "Thẳng hàng vuông góc", "Không xác định"], 0, "Đồng phân cis có các nhóm thế giống nhau cùng nằm về một phía của mặt phẳng liên kết đôi."),
        ("Công thức biểu diễn phân tử chỉ bằng các đoạn thẳng gấp khúc biểu thị khung carbon gọi là:", ["Công thức khai triển", "Công thức thu gọn", "Công thức khung phân tử", "Công thức phối cảnh"], 2, "Đó là công thức khung phân tử (skeletal structure)."),
        ("Số lượng liên kết cộng hóa trị trong một phân tử methane (CH4) là:", ["2", "3", "4", "5"], 2, "Methane có 4 liên kết đơn C-H."),
        ("Chất X có CTCT CH3-CH(CH3)-CH3. Tên gọi theo danh pháp thay thế của X là:", ["Butane", "2-methylpropane", "Propane", "Isobutane"], 1, "Tên thay thế là 2-methylpropane."),
        ("Hiện tượng đồng phân cấu tạo bao gồm các loại đồng phân nào sau đây?", ["Đồng phân mạch C, đồng phân vị trí nhóm chức, đồng phân loại nhóm chức", "Chỉ đồng phân mạch C", "Chỉ đồng phân hình học", "Chỉ đồng phân quang học"], 0, "Đồng phân cấu tạo gồm đồng phân mạch carbon, đồng phân vị trí liên kết bội/nhóm chức và đồng phân loại nhóm chức.")
      ]

    tf = [
      ("Câu 22: Xem xét các luận điểm của Thuyết cấu tạo hóa học:", [
        ("Trong phân tử hợp chất hữu cơ, nguyên tử carbon luôn có hóa trị IV.", True),
        ("Thứ tự liên kết giữa các nguyên tử trong phân tử được gọi là cấu tạo hóa học.", True),
        ("Các nguyên tử carbon chỉ có thể liên kết với các nguyên tố khác, không thể tự liên kết với nhau.", False),
        ("Tính chất của chất chỉ phụ thuộc vào số lượng nguyên tử, không phụ thuộc vào thứ tự liên kết.", False)
      ], "Ý 3 sai vì carbon liên kết với nhau tạo mạch. Ý 4 sai vì tính chất phụ thuộc chặt chẽ vào cấu tạo hóa học."),

      ("Câu 23: Về hiện tượng đồng đẳng:", [
        ("Các chất đồng đẳng có công thức phân tử hơn kém nhau một hay nhiều nhóm -CH2-.", True),
        ("Các chất đồng đẳng luôn có cùng công thức phân tử.", False),
        ("Các chất trong cùng một dãy đồng đẳng có tính chất hóa học tương tự nhau.", True),
        ("Ethanol (C2H5OH) và dimethyl ether (CH3OCH3) là hai chất đồng đẳng của nhau.", False)
      ], "Ý 2 sai vì đồng đẳng hơn kém nhóm -CH2- nên CTPT khác nhau. Ý 4 sai vì đây là 2 chất đồng phân."),

      ("Câu 24: Về hiện tượng đồng phân cấu tạo:", [
        ("Các chất đồng phân có cùng công thức phân tử nhưng khác nhau về công thức cấu tạo.", True),
        ("Butane (C4H10) có 2 đồng phân cấu tạo là butane và 2-methylpropane.", True),
        ("Hai chất có cùng công thức phân tử thì chắc chắn có nhiệt độ sôi bằng nhau.", False),
        ("Ethanol và dimethyl ether có tính chất vật lý và hóa học rất khác nhau do có cấu tạo khác nhau.", True)
      ], "Ý 3 sai vì các chất đồng phân khác nhau về cấu tạo nên nhiệt độ sôi và tính chất khác nhau."),

      ("Câu 25: Về đồng phân hình học cis - trans:", [
        ("Liên kết đôi C=C không thể quay tự do như liên kết đơn C-C.", True),
        ("Mọi phân tử alkene đều có đồng phân hình học cis - trans.", False),
        ("But-1-ene (CH2=CH-CH2-CH3) có 2 đồng phân hình học là cis và trans.", False),
        ("Ở đồng phân trans, các nhóm thế chính nằm về hai phía đối diện của mặt phẳng liên kết đôi.", True)
      ], "Ý 2 và 3 sai vì but-1-ene có đầu =CH2 (2 nguyên tử H giống nhau) nên không có đồng phân hình học.")
    ]

    short = [
      ("Câu 26: Khí butane (C4H10) có bao nhiêu đồng phân cấu tạo?", "2", "Gồm butane và isobutane (2 đồng phân)."),
      ("Câu 27: Hydrocarbon pentane (C5H12) có bao nhiêu đồng phân cấu tạo?", "3", "Gồm pentane, 2-methylbutane, 2,2-dimethylpropane (3 đồng phân)."),
      ("Câu 28: Ứng với công thức phân tử C2H6O có bao nhiêu đồng phân cấu tạo?", "2", "Gồm CH3-CH2-OH và CH3-O-CH3 (2 đồng phân)."),
      ("Câu 29: Ứng với công thức phân tử C3H8O có bao nhiêu đồng phân cấu tạo?", "3", "Gồm 2 alcohol (propan-1-ol, propan-2-ol) và 1 ether (methoxyethane) => 3 đồng phân."),
      ("Câu 30: Alkene but-2-ene (CH3-CH=CH-CH3) có bao nhiêu đồng phân hình học?", "2", "Gồm 2 đồng phân hình học: cis-but-2-ene và trans-but-2-ene."),
      ("Câu 31: Trong phân tử methane (CH4), hóa trị của nguyên tử carbon là bao nhiêu?", "4", "Trong mọi hợp chất hữu cơ, carbon luôn có hóa trị IV.")
    ]

    essay = [
      "Trình bày 3 luận điểm cơ bản của Thuyết cấu tạo hóa học do A.M. Butlerov đề xướng.",
      "Thế nào là hiện tượng đồng phân? Phân biệt đồng phân cấu tạo và đồng phân lập thể (hình học).",
      "Thế nào là hiện tượng đồng đẳng? Nêu điều kiện để hai chất thuộc cùng một dãy đồng đẳng.",
      "Viết công thức cấu tạo thu gọn của 2 đồng phân cấu tạo ứng với CTPT C4H10 và gọi tên thay thế của chúng.",
      "Viết công thức cấu tạo thu gọn của 3 đồng phân cấu tạo ứng với CTPT C5H12 và chỉ rõ chất nào có nhiệt độ sôi cao nhất.",
      "Viết công thức cấu tạo và gọi tên các đồng phân cấu tạo có cùng CTPT C2H6O. So sánh nhiệt độ sôi của chúng.",
      "Giải thích vì sao ethanol (C2H5OH) là chất lỏng có Ts = 78,3°C trong khi dimethyl ether (CH3OCH3) là chất khí có Ts = -24°C dù cùng CTPT.",
      "Nêu điều kiện cần và đủ để một hợp chất có chứa liên kết đôi C=C xuất hiện đồng phân hình học cis - trans.",
      "Giải thích vì sao but-2-ene có đồng phân hình học trong khi but-1-ene thì không có.",
      "Vẽ cấu trúc không gian của hai đồng phân cis-but-2-ene và trans-but-2-ene.",
      "Vẽ công thức khung phân tử (skeletal formula) của hexane và 2-methylpentane.",
      "Ứng với CTPT C4H8 có bao nhiêu đồng phân cấu tạo mạch hở (alkene)? Viết CTCT của chúng.",
      "Trong các đồng phân alkene của C4H8, đồng phân nào có đồng phân hình học? Viết rõ dạng cis và trans.",
      "Viết công thức cấu tạo của các đồng phân alcohol có CTPT C4H10O và phân loại bậc của các alcohol đó.",
      "Tại sao liên kết ba C≡C không có đồng phân hình học cis - trans?",
      "Trình bày mối quan hệ giữa trật tự liên kết nguyên tử trong phân tử và tính chất hóa lý của hợp chất.",
      "Nêu ý nghĩa của việc nghiên cứu cấu trúc phân tử và đồng phân trong ngành công nghiệp dược phẩm."
    ]

    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

print("Question banks defined successfully.")
