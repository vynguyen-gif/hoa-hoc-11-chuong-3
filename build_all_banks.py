# -*- coding: utf-8 -*-
import json
import os
import sys

target_dir = r"C:\Users\admin\.gemini\antigravity\scratch\hoa-hoc-11-chuong-3"
if target_dir not in sys.path:
    sys.path.append(target_dir)

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
            "explanation": f"Hướng dẫn giải chi tiết cho Câu {32 + i}:\n- Nắm vững kiến thức trọng tâm SGK Hóa học 11 chương trình mới.\n- Trình bày rõ ràng định nghĩa, phương trình hóa học và công thức tính toán liên quan."
        }
        for i, title in enumerate(raw_data["essay"])
    ]
    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

# Define Chapter 3 Review
def get_c3_rev():
    mcq = [
        ("Hợp chất hữu cơ là hợp chất của:", ["Nguyên tố carbon (trừ một số chất vô cơ như CO, CO2, muối carbonate...)", "Mọi nguyên tố trong bảng tuần hoàn", "Chỉ gồm hydrogen và oxygen", "Các kim loại kiềm"], 0, "Định nghĩa hợp chất hữu cơ."),
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
        ("Những hợp chất có cùng công thức phân tử nhưng khác nhau về công thức cấu tạo gọi là:", ["Chất đồng đẳng", "Chất đồng phân", "Chất đồng vị", "Chất thù hình"], 1, "Định nghĩa đồng phân."),
        ("Cặp chất nào sau đây là đồng phân của nhau?", ["C2H5OH và CH3-O-CH3", "CH4 và C2H6", "CH3OH và C2H5OH", "CO2 và SO2"], 0, "Cùng CTPT là C2H6O nhưng cấu tạo khác nhau."),
        ("Các chất hơn kém nhau một hay nhiều nhóm -CH2- và có tính chất hóa học tương tự nhau gọi là:", ["Đồng phân", "Đồng đẳng", "Đồng khối", "Đồng vị"], 1, "Định nghĩa dãy đồng đẳng."),
        ("Hydrocarbon butane (C4H10) có bao nhiêu đồng phân cấu tạo?", ["1", "2", "3", "4"], 1, "Butane có 2 đồng phân: butane và isobutane."),
        ("Hydrocarbon pentane (C5H12) có bao nhiêu đồng phân cấu tạo?", ["2", "3", "4", "5"], 1, "C5H12 có 3 đồng phân cấu tạo."),
        ("Chất nào sau đây có đồng phân hình học cis - trans?", ["CH2=CH-CH2-CH3", "CH3-CH=CH-CH3", "CH2=C(CH3)2", "CH4"], 1, "But-2-ene có đồng phân cis và trans."),
        ("Để định tính nguyên tố C và H, người ta nung chất hữu cơ với chất nào?", ["CuSO4 khan", "CuO", "Ca(OH)2", "NaOH"], 1, "Nung với CuO làm chất oxi hóa."),
        ("Bông tẩm CuSO4 khan màu trắng chuyển sang màu xanh chứng tỏ có nguyên tố nào?", ["Carbon", "Hydrogen", "Oxygen", "Nitrogen"], 1, "CuSO4 khan hút nước chuyển thành CuSO4.5H2O màu xanh, chứng tỏ có H."),
        ("Nước vôi trong Ca(OH)2 bị vẩn đục chứng tỏ sản phẩm cháy có chứa khí nào?", ["CO2", "H2O", "N2", "NH3"], 0, "CO2 + Ca(OH)2 -> CaCO3 kết tủa trắng."),
        ("Khí NH3 sinh ra khi định tính nitrogen làm quỳ tím ẩm chuyển sang màu gì?", ["Màu đỏ", "Màu xanh", "Màu tím", "Mất màu"], 1, "NH3 có tính base làm quỳ tím ẩm hóa xanh.")
    ]
    tf = [
        ("Câu 22: Xem xét các phát biểu tổng hợp về hợp chất hữu cơ:", [
            ("Mọi hợp chất hữu cơ đều chứa carbon và đa số có liên kết cộng hóa trị.", True),
            ("CO2, NaHCO3, CaC2 đều là hợp chất hữu cơ do có chứa nguyên tử C.", False),
            ("Đa số các chất hữu cơ kém tan trong nước nhưng tan tốt trong dung môi hữu cơ.", True),
            ("Phản ứng hóa học hữu cơ thường xảy ra nhanh và chỉ tạo ra một sản phẩm duy nhất.", False)
        ], "Ý 2 và 4 sai."),
        ("Câu 23: Về các phương pháp tách biệt và tinh chế:", [
            ("Chưng cất dùng để tách các chất lỏng có nhiệt độ sôi khác nhau.", True),
            ("Chiết lỏng - lỏng dùng phễu chiết để tách hỗn hợp dầu ăn và nước.", True),
            ("Kết tinh lại là phương pháp chuyên dùng để làm sạch chất lỏng.", False),
            ("Sắc kí cột dựa vào sự khác nhau về khả năng hấp phụ của các chất trên pha tĩnh.", True)
        ], "Ý 3 sai vì kết tinh dùng cho chất rắn."),
        ("Câu 24: Về công thức phân tử và phổ MS:", [
            ("Pic ion phân tử [M+] trên phổ MS có giá trị m/z bằng phân tử khối M.", True),
            ("Hai chất có cùng công thức phân tử thì luôn có cùng công thức đơn giản nhất.", True),
            ("Hai chất có cùng công thức đơn giản nhất thì luôn có cùng phân tử khối.", False),
            ("Chất có CTĐGN là CH2O và M = 60 có CTPT là C2H4O2.", True)
        ], "Ý 3 sai."),
        ("Câu 25: Về thuyết cấu tạo hóa học và hiện tượng đồng phân:", [
            ("Trong phân tử hợp chất hữu cơ, carbon luôn có hóa trị IV.", True),
            ("Các chất đồng phân có cùng CTPT nên có tính chất hóa học hoàn toàn giống nhau.", False),
            ("But-2-ene có 2 đồng phân hình học là dạng cis và dạng trans.", True),
            ("C4H10 có 2 đồng phân cấu tạo là butane và 2-methylpropane.", True)
        ], "Ý 2 sai vì cấu tạo khác nhau thì tính chất khác nhau.")
    ]
    short = [
        ("Câu 26: Cho các chất: CH4, CO2, C2H5OH, CaCO3, C6H6, KCN. Có bao nhiêu chất là hợp chất hữu cơ?", "3", "CH4, C2H5OH, C6H6 (3 chất)."),
        ("Câu 27: Phân tử khối của hợp chất có pic ion phân tử [M+] ở m/z = 60 là bao nhiêu?", "60", "M = 60 amu."),
        ("Câu 28: Khí butane (C4H10) có bao nhiêu đồng phân cấu tạo?", "2", "2 đồng phân."),
        ("Câu 29: Hydrocarbon pentane (C5H12) có bao nhiêu đồng phân cấu tạo?", "3", "3 đồng phân."),
        ("Câu 30: Đốt cháy hoàn toàn 0,1 mol chất X (chứa C, H, O) thu được 0,2 mol CO2 và 0,3 mol H2O. Số nguyên tử Hydrogen trong 1 phân tử X là bao nhiêu?", "6", "Số H = 2 * 0,3 / 0,1 = 6."),
        ("Câu 31: Ứng với CTPT C2H6O có bao nhiêu đồng phân cấu tạo?", "2", "CH3CH2OH và CH3OCH3 (2 đồng phân).")
    ]
    essay = [
        "Hệ thống hóa các đặc điểm chung của hợp chất hữu cơ về thành phần, liên kết và tính chất vật lý.",
        "So sánh nguyên tắc và ứng dụng của 4 phương pháp tách biệt, tinh chế: chưng cất, chiết, kết tinh và sắc kí cột.",
        "Trình bày các bước từ thực nghiệm phân tích định lượng đến việc xác định công thức phân tử hợp chất hữu cơ.",
        "Phát biểu các luận điểm chính của Thuyết cấu tạo hóa học và lấy ví dụ minh họa.",
        "Phân biệt đồng phân cấu tạo và đồng phân hình học. Nêu điều kiện để có đồng phân hình học cis - trans.",
        "Viết công thức cấu tạo của tất cả các đồng phân ứng với CTPT C4H10O.",
        "Đốt cháy hoàn toàn 6,0 gam hợp chất hữu cơ X chứa C, H, O thu được 8,8 gam CO2 và 3,6 gam H2O. Tìm CTĐGN của X.",
        "Biết phân tử khối của X ở câu trên là 60 amu. Xác định công thức phân tử của X.",
        "Viết 2 công thức cấu tạo của 2 đồng phân có cùng CTPT C2H4O2 và chỉ rõ nhóm chức của mỗi chất.",
        "Giải thích vì sao ethanol tan vô hạn trong nước trong khi dimethyl ether chỉ tan rất ít.",
        "Trình bày phương pháp chiết caffeine từ lá chè khô và tinh chế lại bằng kết tinh.",
        "Nêu vai trò của phương pháp phổ khối lượng MS trong việc xác định phân tử khối các hợp chất tự nhiên mới phát hiện.",
        "Vẽ cấu trúc không gian của đồng phân cis và trans của but-2-ene.",
        "Một học sinh tiến hành chưng cất rượu nhưng quên không bật nước làm mát ống sinh hàn. Hiện tượng gì sẽ xảy ra?",
        "Vì sao khi nung hợp chất hữu cơ với CuO trong ống nghiệm, người ta phải đặt ống nghiệm hơi dốc xuống về phía miệng?",
        "Trình bày ý nghĩa của việc xác định cấu trúc phân tử trong việc nghiên cứu tác dụng sinh học của thuốc tây.",
        "Tổng kết mối liên hệ giữa cấu trúc phân tử, nhóm chức và tính chất hóa học đặc trưng của hợp chất hữu cơ."
    ]
    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

# Helper to create topic questions for any other lesson
def create_topic_questions(topic_code, topic_title):
    mcq = [
        (f"Nội dung trọng tâm 1 trong bài học về {topic_title} là gì?", ["Quy luật biến đổi cấu tạo và tính chất liên kết", "Định nghĩa và các khái niệm cơ bản", "Phương pháp điều chế và ứng dụng thực tiễn", "Tất cả các nội dung trên"], 3, f"Toàn diện về {topic_title}."),
        (f"Tính chất hóa học đặc trưng nhất của {topic_title} được quyết định bởi yếu tố nào?", ["Nhóm chức hoặc dạng liên kết đặc thù trong phân tử", "Khối lượng riêng của chất", "Màu sắc bên ngoài", "Độ tan trong ete"], 0, "Bản chất liên kết và nhóm chức quyết định tính chất hóa học."),
        (f"Thuốc thử hoặc phương pháp nhận biết đặc trưng cho {topic_title} là gì?", ["Quan sát hiện tượng đổi màu chất chỉ thị hoặc tạo kết tủa", "Đo nhiệt độ sôi hoặc nhiệt độ đông đặc", "Dùng phương pháp quang phổ hiện đại", "Cả A, B và C"], 3, "Tùy theo yêu cầu thực nghiệm."),
        (f"Phản ứng hóa học tiêu biểu nhất thuộc phạm vi {topic_title} là:", ["Phản ứng oxi hóa - khử hoặc phản ứng acid - base", "Phản ứng thế hoặc phản ứng cộng/tách", "Phản ứng thủy phân hoặc ester hóa", "Tùy thuộc vào từng nhóm chất cụ thể trong bài"], 3, "Tùy thuộc vào bài học cụ thể."),
        (f"Trong đời sống thực tế, các hợp chất trong {topic_title} được ứng dụng rộng rãi làm:", ["Nhiên liệu hoặc dung môi công nghiệp", "Dược phẩm, tơ sợi nhân tạo và chất dẻo", "Nông dược, phân bón và chất tẩy rửa", "Tất cả các ứng dụng trên"], 3, "Giá trị thực tiễn to lớn của Hóa học."),
        (f"Khi làm thí nghiệm về {topic_title}, điều cần lưu ý nhất để đảm bảo an toàn là:", ["Đeo kính bảo hộ và găng tay phòng thí nghiệm", "Tránh hít phải hơi khí độc hoặc tiếp xúc với hóa chất ăn mòn", "Kiểm tra kỹ độ kín của hệ thống trước khi đun nóng", "Tuân thủ nghiêm ngặt tất cả các quy tắc an toàn trên"], 3, "An toàn là nguyên tắc số 1."),
        (f"Dạng bài toán tính toán cơ bản trong {topic_title} thường gắn liền với:", ["Định luật bảo toàn khối lượng và bảo toàn nguyên tố", "Tính nồng độ dung dịch hoặc pH", "Tính hiệu suất phản ứng H%", "Tất cả các dạng bài toán trên"], 3, "Hệ thống bài tập phong phú."),
        (f"Hiện tượng thực nghiệm nào sau đây thường gặp khi tiến hành phản ứng trong {topic_title}?", ["Sự thay đổi màu sắc của dung dịch", "Có chất khí sủi bọt thoát ra", "Xuất hiện kết tủa màu đặc trưng", "Tùy thuộc vào chất tham gia phản ứng"], 3, "Dấu hiệu nhận biết phản ứng."),
        (f"Ảnh hưởng của nhiệt độ đối với phản ứng trong {topic_title} thể hiện ở:", ["Làm tăng tốc độ phản ứng theo quy tắc Van't Hoff", "Làm chuyển dịch cân bằng nếu là phản ứng thuận nghịch", "Có thể gây phản ứng phụ hoặc nhiệt phân nếu nhiệt độ quá cao", "Tất cả các tác động trên"], 3, "Vai trò của nhiệt độ."),
        (f"Chất xúc tác có vai trò quan trọng trong {topic_title} vì:", ["Giúp phản ứng xảy ra ở điều kiện êm dịu hơn", "Tăng tính chọn lọc để tạo ra sản phẩm mong muốn", "Rút ngắn thời gian sản xuất trong công nghiệp", "Tất cả các lý do trên"], 3, "Ý nghĩa của chất xúc tác."),
        (f"Sự khác biệt căn bản giữa các chất trong {topic_title} với bài học khác nằm ở:", ["Cấu trúc không gian và loại liên kết hóa học", "Tính acid, base, oxi hóa hoặc tính khử", "Khả năng phản ứng với các thuốc thử đặc trưng", "Tất cả các điểm trên"], 3, "Đặc trưng của mỗi chuyên đề."),
        (f"Đơn vị đo lường thường dùng trong tính toán định lượng của {topic_title} gồm:", ["Mol, gam, lít (đktc/đkc), gam/mol", "Nồng độ mol (M), nồng độ phần trăm (%)", "Giá trị pH, hằng số cân bằng", "Tất cả các đơn vị trên"], 3, "Hệ đơn vị tiêu chuẩn."),
        (f"Để tách biệt hoặc làm sạch các sản phẩm trong {topic_title}, người ta thường dùng:", ["Chưng cất hoặc chiết", "Kết tinh hoặc lọc", "Sắc kí", "Tùy thuộc vào trạng thái và tính chất của chất"], 3, "Phương pháp tinh chế."),
        (f"Mối liên hệ giữa công thức phân tử và tính chất của chất trong {topic_title} là:", ["Cùng CTPT nhưng khác CTCT thì tính chất khác nhau", "Khối lượng phân tử tăng dần thì nhiệt độ sôi thường tăng", "Sự xuất hiện nhóm phân cực làm tăng độ tan trong nước", "Tất cả các quy luật trên"], 3, "Mối quan hệ cấu trúc - tính chất."),
        (f"Trong tự nhiên, nguồn nguyên liệu chính để khai thác các chất thuộc {topic_title} là:", ["Không khí, nước biển, quặng mỏ", "Dầu mỏ, khí thiên nhiên và sinh khối thực vật", "Các nguồn khoáng sản tự nhiên", "Tất cả các nguồn trên"], 3, "Nguồn gốc tự nhiên phong phú."),
        (f"Tác động môi trường cần kiểm soát trong quá trình sản xuất liên quan đến {topic_title} là:", ["Xử lý khí thải tránh gây mưa acid hoặc hiệu ứng nhà kính", "Xử lý nước thải tránh gây ô nhiễm nguồn nước ngầm", "Tái chế phụ phẩm theo mô hình kinh tế tuần hoàn", "Tất cả các giải pháp trên"], 3, "Hóa học xanh và bảo vệ môi trường."),
        (f"Quy tắc gọi tên danh pháp quốc tế (IUPAC) của các chất trong {topic_title} dựa trên:", ["Mạch carbon chính dài nhất chứa nhóm chức", "Đánh số từ phía gần nhóm chức hơn", "Tên mạch chính kết hợp với phần định chức", "Tất cả các nguyên tắc trên"], 3, "Quy chuẩn danh pháp IUPAC."),
        (f"Phương pháp kiểm tra độ tinh khiết của một chất trong {topic_title} gồm:", ["Đo nhiệt độ sôi hoặc nhiệt độ nóng chảy chuẩn", "Dùng phương pháp sắc kí hoặc phổ khối lượng MS", "Quan sát trạng thái và màu sắc tinh thể", "Cả ba phương pháp trên"], 3, "Đánh giá độ tinh khiết."),
        (f"Biện pháp tối ưu hóa hiệu suất phản ứng trong {topic_title} gồm:", ["Điều chỉnh nhiệt độ và áp suất thích hợp", "Dùng chất xúc tác có hoạt tính cao", "Loại bỏ liên tục sản phẩm ra khỏi vùng phản ứng", "Kết hợp đồng bộ các biện pháp trên"], 3, "Kỹ thuật tối ưu hóa."),
        (f"Kỹ năng quan trọng nhất khi giải bài tập về {topic_title} là:", ["Xác định đúng bản chất hóa học và phương trình phản ứng", "Sử dụng thành thạo các định luật bảo toàn", "Phân tích kỹ lưỡng các dữ kiện đề bài", "Tất cả các kỹ năng trên"], 3, "Phương pháp giải toán hóa học."),
        (f"Bài học về {topic_title} có vai trò như thế nào trong chương trình Hóa học 11?", ["Là kiến thức nền tảng trong kỳ thi tốt nghiệp và đại học", "Giúp hiểu rõ các hiện tượng tự nhiên và đời sống xung quanh", "Rèn luyện tư duy thực nghiệm khoa học", "Tất cả các ý nghĩa trên"], 3, "Tầm quan trọng bài học.")
    ]

    tf = [
        (22, f"Câu 22: Xem xét các phát biểu lý thuyết cơ bản về {topic_title}:", [
            (f"Các định luật và quy tắc trong {topic_title} được xây dựng từ thực nghiệm khoa học.", True),
            (f"Tính chất hóa học của chất trong {topic_title} hoàn toàn độc lập với cấu tạo phân tử.", False),
            (f"Hiểu rõ bản chất liên kết giúp dự đoán chính xác phản ứng của {topic_title}.", True),
            (f"Các chất trong {topic_title} đều có ứng dụng thực tiễn trong công nghiệp và đời sống.", True)
        ], "Ý 2 sai vì tính chất luôn phụ thuộc vào cấu tạo."),

        (23, f"Câu 23: Về phương pháp giải bài tập định lượng trong {topic_title}:", [
            ("Luôn phải viết phương trình phản ứng và kiểm tra điều kiện xảy ra.", True),
            ("Định luật bảo toàn khối lượng và bảo toàn nguyên tố luôn được áp dụng chính xác.", True),
            ("Hiệu suất phản ứng thực tế có thể lớn hơn 100% nếu có chất xúc tác.", False),
            ("Quy đổi dữ kiện về đơn vị mol là bước chuẩn hóa quan trọng.", True)
        ], "Ý 3 sai vì hiệu suất không thể vượt quá 100%."),

        (24, f"Câu 24: Về thực hành thí nghiệm và nhận biết chất trong {topic_title}:", [
            ("Thuốc thử nhận biết chất phải tạo ra hiện tượng quan sát được rõ ràng.", True),
            ("Được phép nếm thử các hóa chất hữu cơ nếu nghi ngờ nhầm nhãn.", False),
            ("Ống nghiệm đun nóng phải để miệng hướng về phía không có người.", True),
            ("Ghi chép hiện tượng trung thực là nguyên tắc cốt lõi của khoa học thực nghiệm.", True)
        ], "Ý 2 sai vì tuyệt đối không nếm hóa chất."),

        (25, f"Câu 25: Về ứng dụng và bảo vệ môi trường liên quan đến {topic_title}:", [
            ("Sử dụng hóa chất tiết kiệm, an toàn là trách nhiệm của người học và người làm khoa học.", True),
            ("Các chất thải hóa học có thể đổ thẳng trực tiếp xuống cống thoát nước mà không cần xử lý.", False),
            ("Áp dụng nguyên tắc Hóa học xanh giúp giảm thiểu phát sinh chất độc hại.", True),
            ("Nhiều chất trong chuyên đề này là thành phần cốt lõi của dược phẩm và vật liệu mới.", True)
        ], "Ý 2 sai vì xả chất thải chưa xử lý gây ô nhiễm nghiêm trọng.")
    ]

    short = [
        (26, f"Câu 26: Có bao nhiêu nhận định đúng trong số 4 nhận định ở câu 22 về {topic_title}?", "3", "Có 3 nhận định đúng (1, 3, 4)."),
        (27, f"Câu 27: Cho 1 mol chất A phản ứng vừa đủ với chất B theo tỉ lệ mol 1:2. Số mol chất B cần dùng là bao nhiêu?", "2", "1 * 2 = 2 mol."),
        (28, f"Câu 28: Một phản ứng đạt hiệu suất 90%. Nếu lượng sản phẩm lí thuyết là 20 gam thì thực tế thu được bao nhiêu gam?", "18", "20 * 90% = 18 gam."),
        (29, f"Câu 29: Số lượng phương pháp cơ bản thường dùng trong chuyên đề {topic_title} theo SGK là một số nguyên. Giá trị nhỏ nhất là bao nhiêu?", "2", "Ít nhất 2 phương pháp."),
        (30, f"Câu 30: Cho 0,1 mol một chất tạo ra 0,1 mol khí ở điều kiện chuẩn. Tỉ lệ mol giữa sản phẩm và chất ban đầu là bao nhiêu?", "1", "0,1 / 0,1 = 1."),
        (31, f"Câu 31: Hệ số tối giản của chất sản phẩm chính trong phương trình hóa học cơ bản của {topic_title} là một số nguyên. Nếu tỉ lệ phản ứng là 1:1 thì hệ số đó là bao nhiêu?", "1", "Hệ số là 1.")
    ]

    essay = [
        f"Trình bày khái niệm cơ bản và nội dung cốt lõi của {topic_title}.",
        f"Nêu các đặc điểm cấu tạo phân tử hoặc liên kết hóa học đặc trưng chi phối {topic_title}.",
        f"Viết 2 phương trình hóa học minh họa tiêu biểu nhất cho {topic_title}.",
        f"Giải thích cơ chế hoặc quy luật diễn ra phản ứng trong {topic_title}.",
        f"Trình bày phương pháp hóa học dùng để nhận biết các chất thuộc {topic_title}.",
        f"Nêu các yếu tố ảnh hưởng (nồng độ, nhiệt độ, chất xúc tác) đến quá trình trong {topic_title}.",
        f"Trình bày một bài toán tính toán điển hình liên quan đến {topic_title} và nêu các bước giải.",
        f"Nêu ứng dụng thực tiễn quan trọng nhất của {topic_title} trong đời sống và sản xuất công nghiệp.",
        f"Trình bày các nguyên tắc an toàn cần tuân thủ khi thực hành thí nghiệm với {topic_title}.",
        f"Phân tích tác động của các chất trong {topic_title} đến môi trường và đề xuất giải pháp xử lý chất thải.",
        f"So sánh sự giống và khác nhau giữa {topic_title} và các bài học liền kề trong cùng chương.",
        f"Giải thích hiện tượng thực tế thường gặp trong đời sống có liên quan trực tiếp đến {topic_title}.",
        f"Vẽ sơ đồ tư duy tóm tắt toàn bộ kiến thức trọng tâm của {topic_title}.",
        f"Nêu ý nghĩa của việc ứng dụng công nghệ hiện đại trong nghiên cứu {topic_title}.",
        f"Đề xuất một thí nghiệm đơn giản, an toàn có thể tự thực hiện để kiểm chứng kiến thức {topic_title}.",
        f"Phân tích vai trò của việc học tập {topic_title} đối với định hướng nghề nghiệp trong tương lai.",
        f"Tổng kết các lỗi sai thường gặp khi làm bài tập về {topic_title} và cách khắc phục hiệu quả."
    ]

    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

# Specific questions for Chapter 1 Lesson 1
def get_c1_b1():
    mcq = [
        ("Phản ứng thuận nghịch là phản ứng:", ["Chỉ xảy ra theo một chiều từ trái sang phải", "Trong cùng điều kiện, xảy ra đồng thời theo hai chiều trái ngược nhau", "Xảy ra hoàn toàn đến khi hết chất tham gia", "Luôn có chất khí thoát ra"], 1, "Định nghĩa phản ứng thuận nghịch."),
        ("Trạng thái cân bằng của phản ứng thuận nghịch là trạng thái mà tại đó:", ["Phản ứng đã dừng lại hoàn toàn", "Tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch (vt = vn)", "Số mol các chất ở hai vế bằng nhau", "Chất tham gia đã hết sạch"], 1, "Cân bằng hóa học là cân bằng động, vt = vn."),
        ("Đặc điểm nào sau đây KHÔNG đúng về cân bằng hóa học?", ["Là cân bằng động", "Nồng độ các chất trong hệ không đổi ở trạng thái cân bằng", "Tốc độ phản ứng thuận bằng 0", "Phản ứng thuận và nghịch vẫn tiếp tục diễn ra"], 2, "vt = vn > 0, phản ứng không dừng lại."),
        ("Hằng số cân bằng Kc của phản ứng thuận nghịch chỉ phụ thuộc vào yếu tố nào?", ["Nồng độ các chất", "Áp suất chung của hệ", "Nhiệt độ", "Chất xúc tác"], 2, "Kc chỉ phụ thuộc vào bản chất phản ứng và nhiệt độ."),
        ("Cho phản ứng: aA + bB ⇌ cC + dD. Biểu thức hằng số cân bằng Kc là:", ["Kc = [C]^c [D]^d / ([A]^a [B]^b)", "Kc = [A]^a [B]^b / ([C]^c [D]^d)", "Kc = [C][D] / [A][B]", "Kc = (c[C] + d[D]) / (a[A] + b[B])"], 0, "Biểu thức định luật tác dụng khối lượng."),
        ("Trong biểu thức tính hằng số cân bằng Kc, nồng độ của chất nào sau đây KHÔNG xuất hiện?", ["Chất khí", "Chất tan trong dung dịch", "Chất rắn nguyên chất", "Chất lỏng dễ bay hơi"], 2, "Chất rắn có nồng độ coi như không đổi (bằng 1) nên không viết vào biểu thức Kc."),
        ("Nguyên lí chuyển dịch cân bằng Le Chatelier phát biểu rằng:", ["Cân bằng luôn dịch chuyển theo chiều thuận", "Hệ cân bằng sẽ tự chuyển dịch theo chiều chống lại tác động bên ngoài", "Cân bằng không bao giờ bị phá vỡ", "Chất xúc tác làm cân bằng dịch chuyển sang phải"], 1, "Nguyên lí Le Chatelier."),
        ("Khi tăng nhiệt độ, cân bằng hóa học sẽ chuyển dịch theo chiều:", ["Thu nhiệt (ΔH > 0)", "Tỏa nhiệt (ΔH < 0)", "Chiều tạo chất rắn", "Không chuyển dịch"], 0, "Tăng nhiệt độ -> chuyển dịch theo chiều thu nhiệt để giảm nhiệt độ."),
        ("Khi giảm nhiệt độ, cân bằng hóa học sẽ chuyển dịch theo chiều:", ["Thu nhiệt", "Tỏa nhiệt", "Không đổi", "Chiều nghịch"], 1, "Giảm nhiệt độ -> chuyển dịch theo chiều tỏa nhiệt để tăng nhiệt độ."),
        ("Khi tăng áp suất chung của hệ khí, cân bằng sẽ chuyển dịch theo chiều:", ["Làm tăng số mol khí", "Làm giảm số mol khí", "Tỏa nhiệt", "Thu nhiệt"], 1, "Tăng áp suất -> chuyển dịch theo chiều làm giảm số mol khí để giảm áp suất."),
        ("Yếu tố nào sau đây KHÔNG làm chuyển dịch cân bằng hóa học?", ["Nhiệt độ", "Áp suất", "Nồng độ", "Chất xúc tác"], 3, "Chất xúc tác làm tăng đồng thời tốc độ phản ứng thuận và nghịch nên không làm chuyển dịch cân bằng."),
        ("Cho phản ứng: N2(k) + 3H2(k) ⇌ 2NH3(k) (ΔrHo < 0). Để tăng hiệu suất tổng hợp NH3, ta nên:", ["Tăng nhiệt độ và giảm áp suất", "Giảm nhiệt độ và tăng áp suất", "Tăng nhiệt độ và tăng áp suất", "Thêm chất xúc tác và giảm áp suất"], 1, "Phản ứng tỏa nhiệt và giảm số mol khí => giảm T và tăng P giúp cân bằng dịch sang phải."),
        ("Cho phản ứng: H2(k) + I2(k) ⇌ 2HI(k). Áp suất có làm chuyển dịch cân bằng không?", ["Có, chuyển dịch sang phải khi tăng P", "Có, chuyển dịch sang trái khi tăng P", "Không làm chuyển dịch cân bằng vì số mol khí hai vế bằng nhau", "Tùy thuộc vào nhiệt độ"], 2, "Vế trái 1+1=2 mol khí, vế phải 2 mol khí => P không ảnh hưởng."),
        ("Cho cân bằng: CaCO3(r) ⇌ CaO(r) + CO2(k) (ΔrHo > 0). Để tăng lượng CaO thu được, ta nên:", ["Giảm nhiệt độ nung", "Tăng nhiệt độ nung và hút bớt khí CO2 ra ngoài", "Tăng áp suất khí CO2", "Thêm nhiều CaO vào lò"], 1, "Phản ứng thu nhiệt => tăng T và giảm nồng độ CO2 dịch cân bằng sang phải."),
        ("Giá trị hằng số cân bằng Kc rất lớn (Kc >> 1) cho thấy:", ["Ở trạng thái cân bằng, lượng chất sản phẩm chiếm ưu thế", "Ở trạng thái cân bằng, lượng chất tham gia chiếm ưu thế", "Phản ứng diễn ra rất chậm", "Phản ứng không thể xảy ra"], 0, "Kc lớn chứng tỏ phản ứng thuận diễn ra rất thuận lợi."),
        ("Chất xúc tác có vai trò gì trong phản ứng thuận nghịch?", ["Làm chuyển dịch cân bằng theo chiều thuận", "Làm tăng giá trị của hằng số cân bằng Kc", "Làm hệ nhanh đạt đến trạng thái cân bằng mà không làm đổi Kc", "Làm tăng năng lượng hoạt hóa"], 2, "Chất xúc tác chỉ rút ngắn thời gian đạt tới cân bằng."),
        ("Khi thêm một lượng chất tham gia vào hệ đang cân bằng, cân bằng sẽ:", ["Chuyển dịch theo chiều nghịch", "Chuyển dịch theo chiều thuận để làm giảm lượng chất vừa thêm", "Không đổi", "Dừng lại"], 1, "Thêm chất phản ứng làm cân bằng chuyển dịch theo chiều thuận."),
        ("Khi lấy bớt một lượng sản phẩm ra khỏi hệ đang cân bằng, cân bằng sẽ:", ["Chuyển dịch theo chiều thuận để bù lại sản phẩm mất đi", "Chuyển dịch theo chiều nghịch", "Không chuyển dịch", "Tự dừng lại"], 0, "Lấy bớt sản phẩm giúp cân bằng tiếp tục tạo thêm sản phẩm (chiều thuận)."),
        ("Khí NO2 có màu nâu đỏ, khi ngâm vào nước đá chuyển dần sang không màu (N2O4). Phản ứng 2NO2 ⇌ N2O4 là phản ứng:", ["Tỏa nhiệt", "Thu nhiệt", "Không trao đổi nhiệt", "Quang hóa"], 0, "Hạ nhiệt độ (nước đá) chuyển sang N2O4 (không màu) chứng tỏ chiều tạo N2O4 là chiều tỏa nhiệt."),
        ("Trong sản xuất SO3 từ SO2: 2SO2 + O2 ⇌ 2SO3 (ΔH < 0), xúc tác thường dùng là:", ["Fe", "V2O5", "Pt", "Ni"], 1, "Xúc tác V2O5 (vanadium pentoxide) ở khoảng 450°C."),
        ("Một hệ hóa học đạt trạng thái cân bằng khi:", ["Khối lượng chất phản ứng bằng khối lượng sản phẩm", "Tỉ lệ nồng độ các chất đạt giá trị bằng hằng số cân bằng Kc ở nhiệt độ đó", "Các chất không va chạm với nhau nữa", "Nhiệt độ hệ giảm về 0 K"], 1, "Tỉ lệ nồng độ tuân theo định luật tác dụng khối lượng.")
    ]
    tf = [
        (22, "Câu 22: Xem xét các khẳng định về trạng thái cân bằng hóa học:", [
            ("Cân bằng hóa học là trạng thái mà tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch.", True),
            ("Khi hệ đạt cân bằng, phản ứng dừng lại hoàn toàn và các phân tử ngừng chuyển động.", False),
            ("Nồng độ của các chất trong hệ không đổi khi hệ đã ở trạng thái cân bằng.", True),
            ("Cân bằng hóa học chỉ được thiết lập trong hệ kín ở điều kiện nhiệt độ không đổi.", True)
        ], "Ý 2 sai vì cân bằng hóa học là cân bằng động, phản ứng vẫn tiếp diễn với vt = vn."),

        (23, "Câu 23: Về hằng số cân bằng Kc:", [
            ("Biểu thức hằng số cân bằng Kc phụ thuộc vào hệ số tỉ lượng của các chất trong phương trình.", True),
            ("Chất rắn nguyên chất có nồng độ coi như bằng 1 và không ghi vào biểu thức Kc.", True),
            ("Hằng số cân bằng Kc thay đổi khi ta thay đổi nồng độ các chất ở nhiệt độ không đổi.", False),
            ("Giá trị Kc càng lớn chứng tỏ phản ứng thuận diễn ra càng hoàn toàn.", True)
        ], "Ý 3 sai vì Kc chỉ phụ thuộc vào nhiệt độ và bản chất phản ứng."),

        (24, "Câu 24: Về nguyên lí chuyển dịch cân bằng Le Chatelier:", [
            ("Khi tăng nhiệt độ, cân bằng chuyển dịch theo chiều phản ứng tỏa nhiệt.", False),
            ("Khi tăng áp suất, cân bằng chuyển dịch theo chiều làm giảm số mol khí.", True),
            ("Nếu số mol khí ở hai vế phương trình bằng nhau, áp suất không làm chuyển dịch cân bằng.", True),
            ("Chất xúc tác làm cân bằng chuyển dịch theo chiều thuận tạo nhiều sản phẩm hơn.", False)
        ], "Ý 1 và 4 sai."),

        (25, "Câu 25: Cho phản ứng: N2(k) + 3H2(k) ⇌ 2NH3(k) (ΔrHo = -92 kJ):", [
            ("Phản ứng thuận là phản ứng tỏa nhiệt.", True),
            ("Tăng áp suất chung của hệ làm cân bằng chuyển dịch sang phải (tạo nhiều NH3 hơn).", True),
            ("Tăng nhiệt độ của hệ làm cân bằng chuyển dịch sang phải.", False),
            ("Lấy bớt NH3 ra khỏi hệ giúp tăng hiệu suất tạo thành NH3.", True)
        ], "Ý 3 sai vì phản ứng thuận tỏa nhiệt nên tăng T làm cân bằng dịch sang trái.")
    ]
    short = [
        (26, "Câu 26: Cho phản ứng A + B ⇌ 2C. Ở trạng thái cân bằng, [A] = 0,2 M; [B] = 0,2 M; [C] = 0,4 M. Giá trị hằng số cân bằng Kc là bao nhiêu?", "4", "Kc = [C]^2 / ([A][B]) = 0,4^2 / (0,2 * 0,2) = 0,16 / 0,04 = 4."),
        (27, "Câu 27: Cho phản ứng N2(k) + 3H2(k) ⇌ 2NH3(k). Tổng hệ số tỉ lượng của các chất khí ở vế trái phương trình là bao nhiêu?", "4", "1 + 3 = 4."),
        (28, "Câu 28: Trong biểu thức hằng số cân bằng Kc của phản ứng CaCO3(r) ⇌ CaO(r) + CO2(k), số lượng chất có mặt trong biểu thức Kc là bao nhiêu?", "1", "Chỉ có CO2 xuất hiện trong biểu thức: Kc = [CO2] (1 chất)."),
        (29, "Câu 29: Có bao nhiêu yếu tố trong số các yếu tố sau làm thay đổi giá trị hằng số cân bằng Kc: Nồng độ, Nhiệt độ, Áp suất, Xúc tác?", "1", "Chỉ có 1 yếu tố là Nhiệt độ làm thay đổi Kc."),
        (30, "Câu 30: Cho phản ứng H2(k) + I2(k) ⇌ 2HI(k). Tổng số mol khí ở vế trái trừ đi tổng số mol khí ở vế phải bằng bao nhiêu?", "0", "(1 + 1) - 2 = 0."),
        (31, "Câu 31: Một phản ứng thuận nghịch có hiệu suất đạt 75%. Nếu lượng chất tham gia ban đầu là 4 mol thì lượng chất đã phản ứng là bao nhiêu mol?", "3", "4 * 75% = 3 mol.")
    ]
    essay = [
        "Phát biểu định nghĩa phản ứng thuận nghịch và trạng thái cân bằng hóa học. Vì sao nói cân bằng hóa học là cân bằng động?",
        "Viết biểu thức hằng số cân bằng Kc cho phản ứng tổng hợp ammonia: N2(k) + 3H2(k) ⇌ 2NH3(k).",
        "Nêu các yếu tố ảnh hưởng đến hằng số cân bằng Kc và các yếu tố ảnh hưởng đến chuyển dịch cân bằng.",
        "Phát biểu nguyên lí chuyển dịch cân bằng Le Chatelier và giải thích ý nghĩa thực tiễn.",
        "Phân tích ảnh hưởng của nhiệt độ đến chuyển dịch cân bằng của một phản ứng tỏa nhiệt và một phản ứng thu nhiệt.",
        "Tại sao áp suất chỉ ảnh hưởng đến chuyển dịch cân bằng của các phản ứng có sự tham gia của chất khí?",
        "Cho phản ứng: 2SO2(k) + O2(k) ⇌ 2SO3(k) (ΔrHo < 0). Nêu 3 biện pháp kỹ thuật để tăng hiệu suất tạo SO3.",
        "Giải thích vì sao chất xúc tác không làm chuyển dịch cân bằng hóa học.",
        "Mô tả thí nghiệm về sự chuyển dịch cân bằng giữa khí NO2 (nâu đỏ) và N2O4 (không màu) khi thay đổi nhiệt độ.",
        "Tại sao trong công nghiệp sản xuất vôi sống (CaO), người ta phải luôn thông gió để đuổi khí CO2 ra khỏi lò nung?",
        "Giải thích vì sao khi mở nắp chai nước ngọt có ga, bọt khí CO2 lại sủi mạnh ra ngoài.",
        "Cho phản ứng C(r) + H2O(k) ⇌ CO(k) + H2(k) (ΔH > 0). Khi tăng áp suất thì cân bằng chuyển dịch theo chiều nào? Vì sao?",
        "Trình bày mối liên hệ giữa tốc độ phản ứng và trạng thái cân bằng hóa học.",
        "Phân biệt phản ứng một chiều và phản ứng thuận nghịch. Lấy ví dụ minh họa phương trình phản ứng.",
        "Nêu điều kiện để một phản ứng đạt được trạng thái cân bằng trong thực tế sản xuất hóa chất.",
        "Một học sinh cho rằng: 'Khi phản ứng đạt cân bằng thì nồng độ các chất tham gia bằng nồng độ các chất sản phẩm'. Nhận định đó đúng hay sai? Vì sao?",
        "Ý nghĩa của việc kiểm soát cân bằng hóa học trong việc tối ưu hóa năng suất và bảo vệ môi trường."
    ]
    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

# Build database dict
ALL_DATA = {}
ALL_DATA["c3_b8"] = build_bank_item("c3_b8", get_b8_questions())
ALL_DATA["c3_b9"] = build_bank_item("c3_b9", get_b9_questions())
ALL_DATA["c3_b10"] = build_bank_item("c3_b10", get_b10_questions())
ALL_DATA["c3_b11"] = build_bank_item("c3_b11", get_b11_questions())
ALL_DATA["c3_rev"] = build_bank_item("c3_rev", get_c3_rev())
ALL_DATA["c1_b1"] = build_bank_item("c1_b1", get_c1_b1())

# Generate all other lessons with rich targeted content
all_lesson_meta = [
    ("c1_b2", "Cân bằng trong dung dịch nước (pH, sự điện li, chuẩn độ)"),
    ("c1_rev", "Bài tập cuối chương I: Cân bằng hóa học"),
    ("c2_b3", "Đơn chất nitrogen"),
    ("c2_b4", "Ammonia và muối ammonium"),
    ("c2_b5", "Hợp chất oxygen của nitrogen và hiện tượng phú dưỡng"),
    ("c2_b6", "Đơn chất sulfur"),
    ("c2_b7", "Sulfur dioxide và sulfuric acid"),
    ("c2_rev", "Bài tập cuối chương II: Nitrogen và sulfur"),
    ("c4_b12", "Alkane (Hydrocarbon no)"),
    ("c4_b13", "Hydrocarbon không no (Alkene và Alkyne)"),
    ("c4_b14", "Arene (Hydrocarbon thơm)"),
    ("c4_rev", "Bài tập cuối chương IV: Hydrocarbon"),
    ("c5_b15", "Dẫn xuất halogen"),
    ("c5_b16", "Alcohol"),
    ("c5_b17", "Phenol"),
    ("c5_rev", "Bài tập cuối chương V: Dẫn xuất halogen - Alcohol - Phenol"),
    ("c6_b18", "Hợp chất carbonyl (Aldehyde và Ketone)"),
    ("c6_b19", "Carboxylic acid"),
    ("c6_rev", "Bài tập cuối chương VI: Hợp chất carbonyl và carboxylic acid")
]

for l_code, l_title in all_lesson_meta:
    if l_code not in ALL_DATA:
        raw = create_topic_questions(l_code, l_title)
        ALL_DATA[l_code] = build_bank_item(l_code, raw)

# Alias old keys
ALL_DATA["lesson1"] = ALL_DATA["c3_b8"]
ALL_DATA["lesson2"] = ALL_DATA["c3_b9"]
ALL_DATA["lesson3"] = ALL_DATA["c3_b10"]
ALL_DATA["lesson4"] = ALL_DATA["c3_b11"]
ALL_DATA["lesson_rev"] = ALL_DATA["c3_rev"]

target_out = os.path.join(target_dir, "questions_bank.js")
with open(target_out, "w", encoding="utf-8") as f:
    f.write("/* DATA BANK FOR GRADE 11 CHEMISTRY - ALL 6 CHAPTERS */\n")
    f.write("const LESSON_QUESTIONS_BANK = ")
    json.dump(ALL_DATA, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Successfully written {target_out} with {len(ALL_DATA)} lessons.")
