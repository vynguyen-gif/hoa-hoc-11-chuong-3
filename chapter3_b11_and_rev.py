# -*- coding: utf-8 -*-
"""
Full content for Lesson 11 (Cấu trúc phân tử hợp chất hữu cơ) and Chapter 3 Review
"""

def get_b11_full():
    theory = [
        {
            "type": "tom_tat",
            "title": "1. Thuyết cấu tạo hóa học (Butlerov, 1861)",
            "content": """
              <ul>
                <li><strong>Luận điểm 1:</strong> Trong phân tử hợp chất hữu cơ, các nguyên tử liên kết với nhau theo <strong>đúng hóa trị</strong> và theo một <strong>thứ tự liên kết nhất định</strong>. Thứ tự liên kết đó được gọi là <strong>cấu tạo hóa học</strong>. Sự thay đổi thứ tự liên kết đó sẽ tạo ra chất mới có tính chất khác nhau.
                  <br>Trong mọi hợp chất hữu cơ, <strong>nguyên tử carbon luôn có hóa trị IV</strong>, hydrogen và halogen có hóa trị I, oxygen có hóa trị II, nitrogen có hóa trị III.</li>
                <li><strong>Luận điểm 2:</strong> Trong phân tử hợp chất hữu cơ, các nguyên tử carbon không những có thể liên kết với nguyên tử của các nguyên tố khác mà còn có thể <strong>liên kết trực tiếp với nhau</strong> tạo thành các loại mạch carbon:
                  <ul>
                    <li>Mạch carbon không phân nhánh (mạch thẳng).</li>
                    <li>Mạch carbon phân nhánh.</li>
                    <li>Mạch carbon vòng.</li>
                  </ul>
                </li>
                <li><strong>Luận điểm 3:</strong> Tính chất của các chất phụ thuộc vào <strong>thành phần nguyên tố</strong> (bản chất các nguyên tử) và <strong>cấu tạo hóa học</strong> (thứ tự và bản chất liên kết giữa các nguyên tử trong phân tử).</li>
              </ul>
            """
        },
        {
            "type": "nhan_xet",
            "title": "2. Hiện tượng Đồng đẳng và Đồng phân",
            "content": """
              <ul>
                <li><strong>Đồng đẳng:</strong> Những hợp chất có thành phần phân tử <strong>hơn kém nhau một hay nhiều nhóm $-CH_2-$</strong> nhưng có cấu tạo hóa học tương tự nhau, do đó có tính chất hóa học tương tự nhau, hợp thành một <strong>dãy đồng đẳng</strong>.
                  <br>Ví dụ: Dãy đồng đẳng alkane ($CH_4, C_2H_6, C_3H_8, C_4H_{10}... C_n H_{2n+2}$).</li>
                <li><strong>Đồng phân:</strong> Hiện tượng các chất khác nhau nhưng có <strong>cùng công thức phân tử</strong> được gọi là hiện tượng đồng phân. Các chất đó được gọi là các chất đồng phân của nhau.
                  <ul>
                    <li><strong>Đồng phân cấu tạo:</strong> Khác nhau về thứ tự liên kết giữa các nguyên tử. Gồm:
                      <ol>
                        <li>Đồng phân mạch carbon (mạch thẳng, mạch nhánh, mạch vòng).</li>
                        <li>Đồng phân vị trí nhóm chức hoặc liên kết bội (liên kết đôi, liên kết ba).</li>
                        <li>Đồng phân loại nhóm chức (ví dụ: alcohol và ether có cùng CTPT $C_n H_{2n+2} O$; carboxylic acid và ester có cùng CTPT $C_n H_{2n} O_2$).</li>
                      </ol>
                    </li>
                  </ul>
                </li>
              </ul>
            """
        },
        {
            "type": "chu_y",
            "title": "3. Đồng phân hình học (cis - trans) của Alkene",
            "content": """
              <strong>Điều kiện cần và đủ để alkene có đồng phân hình học:</strong><br>
              Cho alkene có dạng cấu tạo xung quanh liên kết đôi: $R_1 R_2 C = C R_3 R_4$.<br>
              Phân tử chỉ xuất hiện đồng phân hình học khi và chỉ khi:
              $$\\begin{cases} R_1 \\neq R_2 \\\\ R_3 \\neq R_4 \\end{cases}$$
              (Nghĩa là mỗi nguyên tử carbon ở liên kết đôi $C=C$ phải liên kết với <strong>hai nhóm nguyên tử khác nhau</strong>).
              <ul>
                <li><strong>Đồng phân cis:</strong> Mạch chính (hoặc hai nhóm thế lớn hơn) nằm về <strong>cùng một phía</strong> của mặt phẳng chứa liên kết đôi $C=C$.</li>
                <li><strong>Đồng phân trans:</strong> Mạch chính (hoặc hai nhóm thế lớn hơn) nằm về <strong>hai phía đối diện nhau</strong> của mặt phẳng chứa liên kết đôi $C=C$. Đồng phân trans thường bền hơn và có nhiệt độ nóng chảy cao hơn đồng phân cis.</li>
              </ul>
            """
        },
        {
            "type": "nhan_xet",
            "title": "4. Các cách biểu diễn Công thức cấu tạo",
            "content": """
              <ol>
                <li><strong>Công thức cấu tạo khai triển:</strong> Biểu diễn đầy đủ tất cả các liên kết hóa học giữa các nguyên tử trong phân tử.</li>
                <li><strong>Công thức cấu tạo thu gọn:</strong> Gom các nguyên tử hydrogen vào nguyên tử carbon mà chúng liên kết, ví dụ: $CH_3-CH_2-CH_2-CH_3$ hoặc $CH_3(CH_2)_2CH_3$.</li>
                <li><strong>Công thức khung phân tử (Skeletal structure):</strong> Chỉ vẽ các đoạn thẳng gấp khúc biểu thị khung liên kết $C-C$, các đỉnh và đầu mút ngầm hiểu là các nhóm carbon và hydrogen tương ứng; các dị nguyên tử ($O, N, Cl...$) và nhóm chức ($-OH, -COOH...$) được vẽ rõ ràng.</li>
              </ol>
            """
        }
    ]

    methods = [
        {
            "name": "Dạng 1: Viết đồng phân cấu tạo và gọi tên Hydrocarbon",
            "content": "Phương pháp: Bắt đầu viết mạch carbon dài nhất (mạch thẳng) -> Giảm 1 carbon để làm nhánh methyl (-CH3), di chuyển nhánh trên các vị trí đối xứng -> Giảm 2 carbon để làm nhánh ethyl hoặc 2 nhánh methyl -> Điền liên kết bội hoặc nhóm chức -> Thêm đủ số nguyên tử H để carbon đủ hóa trị IV.",
            "examples": [
                {
                    "id": "c3_b11_vd1",
                    "num": 1,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Viết công thức cấu tạo thu gọn và gọi tên theo danh pháp thay thế của tất cả các đồng phân alkane ứng với công thức phân tử $C_5H_{12}$.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>Ứng với CTPT $C_5H_{12}$ có 3 đồng phân cấu tạo alkane:<br>1. Mạch 5 carbon không phân nhánh:<br>$CH_3-CH_2-CH_2-CH_2-CH_3$ (Tên: pentane).<br>2. Mạch 4 carbon, có 1 nhánh methyl ở vị trí C2:<br>$CH_3-CH(CH_3)-CH_2-CH_3$ (Tên: 2-methylbutane hay isopentane).<br>3. Mạch 3 carbon, có 2 nhánh methyl ở vị trí C2:<br>$CH_3-C(CH_3)_2-CH_3$ (Tên: 2,2-dimethylpropane hay neopentane)."
                },
                {
                    "id": "c3_b11_vd2",
                    "num": 2,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Viết công thức cấu tạo thu gọn của các đồng phân alkene mạch hở có công thức phân tử $C_4H_8$ và gọi tên thay thế của chúng.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>Ứng với $C_4H_8$ có 3 đồng phân cấu tạo alkene mạch hở:<br>1. $CH_2=CH-CH_2-CH_3$ (Tên: but-1-ene).<br>2. $CH_3-CH=CH-CH_3$ (Tên: but-2-ene).<br>3. $CH_2=C(CH_3)-CH_3$ (Tên: 2-methylpropene hay isobutylene)."
                },
                {
                    "id": "c3_b11_vd3",
                    "num": 3,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Vẽ công thức cấu tạo thu gọn và xác định số liên kết cộng hóa trị (liên kết $\\sigma$ và liên kết $\\pi$) có trong một phân tử acetylene ($C_2H_2$) và ethylene ($C_2H_4$).",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- <strong>Ethylene ($C_2H_4$):</strong> CTCT là $CH_2=CH_2$. Phân tử có 4 liên kết đơn $C-H$ (4 liên kết $\\sigma$) và 1 liên kết đôi $C=C$ (gồm 1 liên kết $\\sigma$ và 1 liên kết $\\pi$). Tổng cộng có 5 liên kết $\\sigma$ và 1 liên kết $\\pi$.<br>- <strong>Acetylene ($C_2H_2$):</strong> CTCT là $CH \\equiv CH$. Phân tử có 2 liên kết đơn $C-H$ (2 liên kết $\\sigma$) và 1 liên kết ba $C \\equiv C$ (gồm 1 liên kết $\\sigma$ và 2 liên kết $\\pi$). Tổng cộng có 3 liên kết $\\sigma$ và 2 liên kết $\\pi$."
                }
            ]
        },
        {
            "name": "Dạng 2: Nhận biết và Biểu diễn Đồng phân hình học (cis - trans)",
            "content": "Phương pháp: Kiểm tra điều kiện: $R_1 \\neq R_2$ và $R_3 \\neq R_4$ tại nối đôi $C=C$. Nếu thỏa mãn thì vẽ hai dạng: cis (các nhóm lớn cùng phía) và trans (các nhóm lớn chéo nhau khác phía).",
            "examples": [
                {
                    "id": "c3_b11_vd4",
                    "num": 4,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Trong các chất sau đây, chất nào CÓ đồng phân hình học cis - trans? Giải thích: a) Propene ($CH_2=CH-CH_3$); b) But-2-ene ($CH_3-CH=CH-CH_3$); c) 2-Methylbut-2-ene ($CH_3-C(CH_3)=CH-CH_3$).",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>a) <strong>Propene:</strong> Tại nguyên tử $C_1$ có hai nhóm nguyên tử liên kết là $-H$ và $-H$ giống nhau $\\Rightarrow$ KHÔNG có đồng phân hình học.<br>b) <strong>But-2-ene:</strong> Tại $C_2$ liên kết với $-H$ và $-CH_3$ (khác nhau); tại $C_3$ liên kết với $-H$ và $-CH_3$ (khác nhau) $\\Rightarrow$ CÓ đồng phân hình học (gồm cis-but-2-ene và trans-but-2-ene).<br>c) <strong>2-Methylbut-2-ene:</strong> Tại $C_2$ có 2 nhóm $-CH_3$ giống nhau $\\Rightarrow$ KHÔNG có đồng phân hình học."
                },
                {
                    "id": "c3_b11_vd5",
                    "num": 5,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Biểu diễn cấu trúc không gian của hai đồng phân cis - trans của hợp chất pent-2-ene ($CH_3-CH=CH-CH_2-CH_3$).",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- <strong>cis-pent-2-ene:</strong> Hai nhóm alkyl ($-CH_3$ và $-CH_2CH_3$) cùng nằm về một phía của mặt phẳng liên kết đôi $C=C$:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CH₃&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CH₂CH₃<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C == C<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\\<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;H&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;H<br>- <strong>trans-pent-2-ene:</strong> Hai nhóm alkyl nằm về hai phía đối diện của mặt phẳng liên kết đôi $C=C$:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CH₃&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;H<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C == C<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\\<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;H&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CH₂CH₃"
                },
                {
                    "id": "c3_b11_vd6",
                    "num": 6,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Tại sao các hợp chất có liên kết ba như propyne ($CH \\equiv C-CH_3$) và but-2-yne ($CH_3-C \\equiv C-CH_3$) không bao giờ có đồng phân hình học cis - trans?",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Ở liên kết ba $C \\equiv C$, mỗi nguyên tử carbon tham gia liên kết ở trạng thái lai hóa $sp$. Góc liên kết xung quanh mỗi nguyên tử carbon là $180^o$ (cấu trúc đường thẳng).<br>- Mỗi nguyên tử carbon ở nối ba chỉ còn liên kết với <strong>duy nhất 1 nguyên tử hoặc nhóm nguyên tử</strong> (không thể có hai nhóm thế $R_1, R_2$ khác nhau trên cùng một nguyên tử carbon). Do đó, không tồn tại sự định hướng không gian khác nhau, hợp chất có liên kết ba không có đồng phân hình học."
                }
            ]
        },
        {
            "name": "Dạng 3: Viết đồng phân nhóm chức và So sánh tính chất vật lí",
            "content": "Phương pháp: Dẫn xuất $C_n H_{2n+2} O$ có đồng phân alcohol và ether; $C_n H_{2n} O_2$ có đồng phân carboxylic acid và ester. Alcohol và acid tạo được liên kết hydrogen liên phân tử nên có nhiệt độ sôi cao và tan tốt trong nước hơn ether và ester tương ứng.",
            "examples": [
                {
                    "id": "c3_b11_vd7",
                    "num": 7,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Viết công thức cấu tạo của tất cả các đồng phân có cùng công thức phân tử $C_3H_8O$. Chỉ rõ đồng phân nào thuộc loại alcohol và đồng phân nào thuộc loại ether.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>Ứng với CTPT $C_3H_8O$ có 3 đồng phân cấu tạo:<br>1. Đồng phân Alcohol (chứa nhóm $-OH$):<br>- $CH_3-CH_2-CH_2-OH$ (propan-1-ol, alcohol bậc I).<br>- $CH_3-CH(OH)-CH_3$ (propan-2-ol, alcohol bậc II).<br>2. Đồng phân Ether (chứa nhóm $-O-$):<br>- $CH_3-O-CH_2-CH_3$ (methoxyethane hay ethyl methyl ether)."
                },
                {
                    "id": "c3_b11_vd8",
                    "num": 8,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Viết tất cả các đồng phân cấu tạo đơn chức chứa nhóm carboxyl ($-COOH$) và nhóm ester ($-COO-$) có cùng công thức phân tử $C_3H_6O_2$.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>1. Đồng phân Carboxylic acid (chứa nhóm $-COOH$):<br>- $CH_3-CH_2-COOH$ (propanoic acid).<br>2. Đồng phân Ester (chứa nhóm $-COO-$):<br>- $H-COO-CH_2-CH_3$ (ethyl formate).<br>- $CH_3-COO-CH_3$ (methyl acetate)."
                },
                {
                    "id": "c3_b11_vd9",
                    "num": 9,
                    "level": "level-vdc",
                    "levelName": "Vận dụng cao",
                    "title": "Hai chất hữu cơ ethanol ($C_2H_5OH$) và dimethyl ether ($CH_3-O-CH_3$) có cùng công thức phân tử là $C_2H_6O$. Tuy nhiên ở nhiệt độ thường, ethanol là chất lỏng sôi ở $78,3^oC$ và tan vô hạn trong nước, còn dimethyl ether là chất khí sôi ở $-24^oC$ và ít tan trong nước. Hãy giải thích sự khác biệt sâu sắc này dựa trên cấu tạo phân tử.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- <strong>Ethanol ($C_2H_5OH$):</strong> Phân tử chứa nhóm $-OH$ phân cực mạnh, nguyên tử $H$ linh động liên kết với nguyên tử $O$ có độ âm điện lớn. Nhờ đó, các phân tử ethanol có khả năng tạo <strong>liên kết hydrogen liên phân tử</strong> với nhau và tạo liên kết hydrogen với phân tử nước. Để làm sôi ethanol cần nhiệt lượng lớn để phá vỡ mạng lưới liên kết hydrogen này $\\Rightarrow$ nhiệt độ sôi cao ($78,3^oC$) và tan vô hạn trong nước.<br>- <strong>Dimethyl ether ($CH_3-O-CH_3$):</strong> Nguyên tử $O$ liên kết với hai nguyên tử $C$, không có nguyên tử $H$ linh động nên giữa các phân tử ether <strong>không có liên kết hydrogen liên phân tử</strong> (chỉ có lực tương tác van der Waals yếu) $\\Rightarrow$ phân tử dễ tách nhau bay hơi ở nhiệt độ rất thấp ($-24^oC$, thể khí) và khó tạo liên kết hydrogen với nước nên ít tan trong nước."
                }
            ]
        }
    ]

    return { "theory": theory, "methods": methods }

print("b11 full definition ready.")


def get_c3_rev_full():
    theory = [
        {
            "type": "tom_tat",
            "title": "TỔNG HỢP KIẾN THỨC CỐT LÕI CHƯƠNG III - ĐẠI CƯƠNG HÓA HỌC HỮU CƠ",
            "content": """
              <ul>
                <li><strong>1. Khái niệm & Nhóm chức:</strong> Hợp chất hữu cơ là hợp chất của carbon (trừ $CO, CO_2$, muối carbonate, cyanide, carbide). Nhóm chức quyết định phản ứng đặc trưng: $-OH$ (alcohol), $-CHO$ (aldehyde), $-COOH$ (carboxylic acid), $-COO-$ (ester), $-NH_2$ (amine).</li>
                <li><strong>2. Phương pháp tách biệt và tinh chế:</strong>
                  <ul>
                    <li><em>Chưng cất:</em> Tách chất lỏng dựa vào sự khác nhau về nhiệt độ sôi.</li>
                    <li><em>Chiết:</em> Dựa vào độ tan khác nhau trong 2 dung môi không trộn lẫn (chiết lỏng - lỏng bằng phễu chiết, chiết lỏng - rắn ngâm dược liệu).</li>
                    <li><em>Kết tinh lại:</em> Tinh chế chất rắn dựa vào độ tan thay đổi lớn theo nhiệt độ.</li>
                    <li><em>Sắc kí cột:</em> Tách hỗn hợp phức tạp dựa vào khả năng hấp phụ khác nhau trên pha tĩnh silica gel.</li>
                  </ul>
                </li>
                <li><strong>3. Công thức phân tử & Phổ MS:</strong> Công thức đơn giản nhất cho tỉ lệ số nguyên tử tối giản; CTPT = $(CTĐGN)_n$. Pic ion phân tử $[M^+]$ trên phổ MS cho biết phân tử khối $M$.</li>
                <li><strong>4. Thuyết cấu tạo hóa học & Đồng phân:</strong> Carbon luôn có hóa trị IV, tạo được mạch C. Đồng phân cấu tạo (mạch C, vị trí nhóm chức, loại nhóm chức). Đồng phân hình học cis - trans của alkene ($R_1 \\neq R_2$ và $R_3 \\neq R_4$).</li>
              </ul>
            """
        },
        {
            "type": "nhan_xet",
            "title": "Nhận xét tổng kết chương",
            "content": """
              Chương 3 là nền tảng cốt lõi của toàn bộ chương trình Hóa học hữu cơ lớp 11 và lớp 12. Việc thành thạo phân loại nhóm chức, xác định công thức phân tử và biểu diễn đúng công thức cấu tạo là điều kiện tiên quyết để học tốt các chương Hydrocarbon và Dẫn xuất hydrocarbon tiếp theo.
            """
        }
    ]

    methods = [
        {
            "name": "Dạng 1: Bài toán tổng hợp Phân tích nguyên tố và Thiết lập CTPT",
            "content": "Phương pháp: Kết hợp dữ liệu phản ứng đốt cháy, tỉ lệ % nguyên tố và pic ion phân tử [M+] trên phổ khối lượng MS để tìm chính xác công thức phân tử.",
            "examples": [
                {
                    "id": "c3_rev_vd1",
                    "num": 1,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Đốt cháy hoàn toàn 6,00 gam một hợp chất hữu cơ X thu được 8,80 gam $CO_2$ và 3,60 gam $H_2O$. Trên phổ MS của X xuất hiện pic ion phân tử $[M^+]$ tại $m/z = 60$. Xác định công thức phân tử của X.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- $n_C = n_{CO_2} = \\frac{8,80}{44} = 0,20 \\text{ mol} \\Rightarrow m_C = 2,40 \\text{ g}$.<br>- $n_H = 2 \\times n_{H_2O} = 2 \\times \\frac{3,60}{18} = 0,40 \\text{ mol} \\Rightarrow m_H = 0,40 \\text{ g}$.<br>- $m_O = 6,00 - (2,40 + 0,40) = 3,20 \\text{ g} \\Rightarrow n_O = \\frac{3,20}{16} = 0,20 \\text{ mol}$.<br>- Tỉ lệ: $n_C : n_H : n_O = 0,20 : 0,40 : 0,20 = 1 : 2 : 1 \\Rightarrow$ CTĐGN là $CH_2O$.<br>- Từ phổ MS có $M = 60 \\Rightarrow 30n = 60 \\Rightarrow n = 2$. Vậy CTPT của X là $C_2H_4O_2$."
                },
                {
                    "id": "c3_rev_vd2",
                    "num": 2,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Chất hữu cơ Y có %C = 54,54%, %H = 9,09%, còn lại là oxygen. Tỉ khối hơi của Y so với khí nitrogen ($N_2, M=28$) xấp xỉ bằng 3,143. Xác định công thức phân tử của Y.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Phân tử khối của Y: $M_Y = 3,143 \\times 28 \\approx 88 \\text{ amu}$.<br>- $\\%O = 100\\% - (54,54\\% + 9,09\\%) = 36,37\\%$.<br>- Tỉ lệ: $n_C : n_H : n_O = \\frac{54,54}{12} : \\frac{9,09}{1} : \\frac{36,37}{16} = 4,545 : 9,09 : 2,273 = 2 : 4 : 1$.<br>$\\Rightarrow$ CTĐGN là $C_2H_4O$ ($M = 44$).<br>- Ta có: $44n = 88 \\Rightarrow n = 2$. Vậy CTPT của Y là $C_4H_8O_2$."
                },
                {
                    "id": "c3_rev_vd3",
                    "num": 3,
                    "level": "level-vdc",
                    "levelName": "Vận dụng cao",
                    "title": "Đốt cháy hoàn toàn 0,15 mol một chất hữu cơ Z chứa C, H, O cần dùng vừa đủ 10,08 lít khí $O_2$ (đktc). Dẫn toàn bộ sản phẩm cháy qua bình đựng dung dịch $Ca(OH)_2$ dư thu được 30,0 gam kết tủa trắng và khối lượng dung dịch giảm 11,1 gam. Xác định công thức phân tử của Z.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- $n_{CO_2} = n_{CaCO_3} = \\frac{30,0}{100} = 0,30 \\text{ mol} \\Rightarrow m_{CO_2} = 13,2 \\text{ gam}$.<br>- Khối lượng dung dịch giảm: $\\Delta m_{\\downarrow} = m_{CaCO_3} - (m_{CO_2} + m_{H_2O}) = 11,1 \\text{ g}$<br>$\\Rightarrow m_{H_2O} = 30,0 - 11,1 - 13,2 = 5,7 \\text{ gam} \\Rightarrow n_{H_2O} = \\frac{5,7}{18} \\approx 0,317 \\text{ mol}$.<br>- Dễ dàng tính được số C trong 1 phân tử Z: $\\text{Số C} = \\frac{n_{CO_2}}{n_Z} = \\frac{0,30}{0,15} = 2$.<br>- Bảo toàn O tìm được CTPT chính xác của Z là $C_2H_4O_2$ hoặc $C_2H_6O$."
                }
            ]
        },
        {
            "name": "Dạng 2: Biện luận cấu trúc phân tử và Viết đồng phân",
            "content": "Phương pháp: Dựa vào CTPT và tính chất hóa học để xác định các đồng phân cấu tạo và đồng phân hình học thỏa mãn đề bài.",
            "examples": [
                {
                    "id": "c3_rev_vd4",
                    "num": 4,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Hợp chất X có công thức phân tử $C_4H_9Cl$. Hãy viết công thức cấu tạo thu gọn của tất cả các đồng phân cấu tạo của X và gọi tên thay thế của từng đồng phân.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>Ứng với CTPT $C_4H_9Cl$ có 4 đồng phân cấu tạo dẫn xuất halogen:<br>1. $CH_3-CH_2-CH_2-CH_2-Cl$ (1-chlorobutane).<br>2. $CH_3-CH_2-CH(Cl)-CH_3$ (2-chlorobutane).<br>3. $CH_3-CH(CH_3)-CH_2-Cl$ (1-chloro-2-methylpropane).<br>4. $CH_3-C(Cl)(CH_3)-CH_3$ (2-chloro-2-methylpropane)."
                },
                {
                    "id": "c3_rev_vd5",
                    "num": 5,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Chất hữu cơ Y có công thức phân tử $C_4H_8$. Biết Y làm mất màu dung dịch nước brom và có đồng phân hình học cis - trans. Hãy xác định công thức cấu tạo của Y và vẽ hai đồng phân cis - trans của nó.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Y làm mất màu nước brom $\\Rightarrow$ Y là alkene có 1 liên kết đôi $C=C$.<br>- Y có đồng phân hình học $\\Rightarrow$ Y phải là but-2-ene: $CH_3-CH=CH-CH_3$.<br>- Dạng cis: hai nhóm $-CH_3$ cùng phía so với liên kết đôi $C=C$.<br>- Dạng trans: hai nhóm $-CH_3$ khác phía (đối diện) so với liên kết đôi $C=C$."
                },
                {
                    "id": "c3_rev_vd6",
                    "num": 6,
                    "level": "level-vdc",
                    "levelName": "Vận dụng cao",
                    "title": "Chất Z có công thức phân tử $C_3H_6O_2$. Biết Z phản ứng được với dung dịch $NaOH$ nhưng không phản ứng với kim loại $Na$. Viết công thức cấu tạo và gọi tên các đồng phân của Z thỏa mãn tính chất trên.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Z tác dụng với $NaOH$ nhưng không tác dụng với $Na$ chứng tỏ Z không có nhóm carboxyl ($-COOH$) tự do của acid mà Z thuộc loại <strong>ester</strong> (chứa nhóm chức $-COO-$).<br>- Các đồng phân ester có CTPT $C_3H_6O_2$ là:<br>1. $H-COO-CH_2-CH_3$ (ethyl formate).<br>2. $CH_3-COO-CH_3$ (methyl acetate)."
                }
            ]
        },
        {
            "name": "Dạng 3: Quy trình tách biệt, tinh chế và Ứng dụng thực tế",
            "content": "Phương pháp: Lựa chọn và mô tả chính xác các bước tiến hành tách chất từ các mẫu thực tế (dầu thực vật, dược liệu, dung dịch cồn, tinh dầu).",
            "examples": [
                {
                    "id": "c3_rev_vd7",
                    "num": 7,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Để tách rời hai chất lỏng $A$ (nhiệt độ sôi $65^oC$) và $B$ (nhiệt độ sôi $110^oC$) tan vô hạn vào nhau thành dung dịch đồng nhất, người ta sử dụng phương pháp nào? Hãy nêu nguyên tắc và dụng cụ chính cần dùng.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Sử dụng <strong>phương pháp chưng cất thường</strong>.<br>- <em>Nguyên tắc:</em> Dựa vào sự chênh lệch lớn về nhiệt độ sôi của hai chất lỏng ($110^oC - 65^oC = 45^oC > 20^oC$). Chất A sôi trước ở $65^oC$ bay hơi sang ống sinh hàn ngưng tụ thành chất lỏng tinh khiết, chất B sôi ở $110^oC$ vẫn nằm lại trong bình cầu.<br>- <em>Dụng cụ chính:</em> Bình cầu chưng cất, nhiệt kế, ống sinh hàn nước, bình tam giác hứng chất lỏng, đèn cồn hoặc bếp điện, đá bọt."
                },
                {
                    "id": "c3_rev_vd8",
                    "num": 8,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Tại các cơ sở sản xuất nước hoa hoặc dầu xoa bóp, người ta thường ngâm cánh hoa cúc hoặc lá bạc hà trong dầu khoáng hoặc dung môi hữu cơ không độc hại. Phương pháp tách chất này được gọi là gì? Nêu ưu điểm so với phương pháp đun sôi.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Đây là <strong>phương pháp chiết lỏng - rắn</strong>.<br>- <em>Ưu điểm:</em> Không cần sử dụng nhiệt độ quá cao nên các hoạt chất thơm quý giá, tinh dầu và vitamin tự nhiên không bị nhiệt phân hủy, bảo toàn trọn vẹn mùi hương tự nhiên tinh tế và công dụng sinh học của thảo dược."
                },
                {
                    "id": "c3_rev_vd9",
                    "num": 9,
                    "level": "level-vdc",
                    "levelName": "Vận dụng cao",
                    "title": "Một mẫu đường saccharose rắn bị lẫn một lượng nhỏ cát mịn và muối ăn ($NaCl$). Hãy đề xuất quy trình thực nghiệm chi tiết bằng các phương pháp tách chất đã học để thu được đường saccharose tinh khiết ở dạng tinh thể rắn.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>1. Hòa tan hỗn hợp vào một lượng nước nóng vừa đủ, khuấy đều cho đường và muối tan hết, cát không tan.<br>2. Tiến hành <strong>lọc nóng</strong> để giữ lại cát trên giấy lọc, thu lấy dung dịch nước đường và muối.<br>3. Cô bớt nước của dung dịch ở nhiệt độ khoảng $70 - 80^oC$ đến khi dung dịch đạt trạng thái bão hòa đường, sau đó để dung dịch nguội từ từ xuống nhiệt độ phòng ($20 - 25^oC$).<br>4. Do độ tan của đường thay đổi rất lớn theo nhiệt độ (giảm mạnh khi làm lạnh), trong khi độ tan của muối $NaCl$ hầu như ít thay đổi theo nhiệt độ, đường sẽ kết tinh tách ra dưới dạng tinh thể trong khi muối ăn vẫn nằm lại trong dung dịch mẹ.<br>5. Lọc hút lấy tinh thể đường, rửa nhanh bằng một ít nước đá lạnh rồi sấy khô ở nhiệt độ thích hợp thu được đường tinh khiết."
                }
            ]
        }
    ]

    return { "theory": theory, "methods": methods }

print("c3_rev full definition ready.")
