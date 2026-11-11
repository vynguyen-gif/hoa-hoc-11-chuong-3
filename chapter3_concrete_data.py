# -*- coding: utf-8 -*-
"""
Chapter 3 Comprehensive Concrete Data
Includes detailed theory, diagrams, 9 specific examples, and 48 specific exercises for each lesson in Chapter 3.
"""

def get_b8_full():
    theory = [
        {
            "type": "tom_tat",
            "title": "1. Khái niệm và Đặc điểm chung của hợp chất hữu cơ",
            "content": """
              <ul>
                <li><strong>Khái niệm:</strong> Hợp chất hữu cơ là hợp chất của nguyên tố carbon (trừ một số chất vô cơ thường gặp như carbon monoxide $CO$, carbon dioxide $CO_2$, muối carbonate $CO_3^{2-}$, muối hydrogencarbonate $HCO_3^-$, các muối cyanide $CN^-$, carbide như $CaC_2, Al_4C_3...$).</li>
                <li><strong>Hóa học hữu cơ:</strong> Là ngành hóa học chuyên nghiên cứu về thành phần, cấu trúc, tính chất và các phương pháp tổng hợp hợp chất hữu cơ.</li>
                <li><strong>Đặc điểm cấu tạo:</strong>
                  <ul>
                    <li>Liên kết hóa học chủ yếu giữa các nguyên tử trong phân tử hợp chất hữu cơ là <strong>liên kết cộng hóa trị</strong> (phân cực hoặc không phân cực).</li>
                    <li>Nguyên tử carbon luôn thể hiện <strong>hóa trị IV</strong>. Các nguyên tử carbon có khả năng liên kết trực tiếp với nhau tạo thành mạch carbon (mạch không phân nhánh, mạch phân nhánh hoặc mạch vòng).</li>
                  </ul>
                </li>
              </ul>
            """
        },
        {
            "type": "chu_y",
            "title": "Chú ý: Tính chất vật lí và hóa học chung",
            "content": """
              <ol>
                <li><strong>Tính chất vật lí:</strong> Đa số hợp chất hữu cơ có nhiệt độ nóng chảy và nhiệt độ sôi thấp (dễ bay hơi), hầu như không tan trong nước nhưng tan tốt trong các dung môi hữu cơ không phân cực (xăng, benzene, ether...).</li>
                <li><strong>Tính chất hóa học:</strong> Các hợp chất hữu cơ kém bền với nhiệt và dễ cháy. Phản ứng hóa học hữu cơ thường diễn ra chậm, không hoàn toàn theo một chiều, cần có nhiệt độ hoặc chất xúc tác và tạo ra hỗn hợp nhiều sản phẩm.</li>
              </ol>
            """
        },
        {
            "type": "tom_tat",
            "title": "2. Phân loại hợp chất hữu cơ và Khái niệm Nhóm chức",
            "content": """
              <ul>
                <li><strong>Phân loại theo thành phần nguyên tố:</strong>
                  <ul>
                    <li><strong>Hydrocarbon:</strong> Phân tử chỉ chứa 2 nguyên tố là carbon và hydrogen. Gồm hydrocarbon no (alkane), hydrocarbon không no (alkene, alkyne) và arene (hydrocarbon thơm như benzene).</li>
                    <li><strong>Dẫn xuất của hydrocarbon:</strong> Phân tử ngoài C và H còn chứa các nguyên tố khác như $O, N, S$, halogen ($Cl, Br, F, I)...$</li>
                  </ul>
                </li>
                <li><strong>Khái niệm Nhóm chức:</strong> Nhóm chức là nguyên tử hoặc nhóm nguyên tử gây ra những phản ứng hóa học đặc trưng của phân tử hợp chất hữu cơ.
                  <table style="width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 13.5px;">
                    <tr style="background: #e2e8f0; font-weight: bold;">
                      <th style="border: 1px solid #cbd5e1; padding: 6px;">Tên loại hợp chất</th>
                      <th style="border: 1px solid #cbd5e1; padding: 6px;">Kí hiệu nhóm chức</th>
                      <th style="border: 1px solid #cbd5e1; padding: 6px;">Tên nhóm chức</th>
                      <th style="border: 1px solid #cbd5e1; padding: 6px;">Ví dụ chất cụ thể</th>
                    </tr>
                    <tr>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">Alcohol</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px; text-align: center;">$-OH$</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">Hydroxy</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">$CH_3CH_2OH$ (ethanol)</td>
                    </tr>
                    <tr>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">Aldehyde</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px; text-align: center;">$-CHO$</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">Formyl / Aldehyde</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">$CH_3CHO$ (acetaldehyde)</td>
                    </tr>
                    <tr>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">Carboxylic acid</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px; text-align: center;">$-COOH$</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">Carboxyl</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">$CH_3COOH$ (acetic acid)</td>
                    </tr>
                    <tr>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">Ester</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px; text-align: center;">$-COO-$</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">Ester</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">$CH_3COOCH_3$ (methyl acetate)</td>
                    </tr>
                    <tr>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">Amine</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px; text-align: center;">$-NH_2$</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">Amino</td>
                      <td style="border: 1px solid #cbd5e1; padding: 6px;">$CH_3NH_2$ (methylamine)</td>
                    </tr>
                  </table>
                </li>
              </ul>
            """
        },
        {
            "type": "nhan_xet",
            "title": "3. Phân tích định tính nguyên tố trong hợp chất hữu cơ",
            "content": """
              <ul>
                <li><strong>Định tính Carbon và Hydrogen:</strong>
                  <ul>
                    <li>Trộn đều hợp chất hữu cơ với bột <strong>$CuO$ khan</strong> (đóng vai trò là chất oxi hóa), cho vào ống nghiệm khô rồi nung nóng.</li>
                    <li>Khí và hơi thoát ra được dẫn qua ống nghiệm có chứa miếng bông tẩm <strong>$CuSO_4$ khan màu trắng</strong>: Nếu bông chuyển sang <strong>màu xanh lam</strong> ($\text{CuSO}_4 \cdot 5\text{H}_2\text{O}$) chứng tỏ có nguyên tố <strong>Hydrogen</strong> ($H$).</li>
                    <li>Tiếp tục dẫn khí qua bình chứa <strong>dung dịch nước vôi trong $Ca(OH)_2$ dư</strong>: Nếu xuất hiện kết tủa trắng $CaCO_3$ làm vẩn đục dung dịch chứng tỏ có nguyên tố <strong>Carbon</strong> ($C$).</li>
                  </ul>
                </li>
                <li><strong>Định tính Nitrogen:</strong> Nung hợp chất hữu cơ với hỗn hợp vôi tôi xút ($NaOH + CaO$), khí $NH_3$ sinh ra làm quỳ tím ẩm chuyển sang màu xanh.</li>
                <li><strong>Định tính Halogen:</strong> Nung hợp chất hữu cơ với vôi sống, hòa tan sản phẩm trong dung dịch $HNO_3$ loãng rồi nhỏ dung dịch $AgNO_3$, xuất hiện kết tủa trắng ($AgCl$), vàng nhạt ($AgBr$) hoặc vàng đậm ($AgI$).</li>
              </ul>
            """
        },
        {
            "type": "chu_y",
            "title": "Cảnh báo an toàn thí nghiệm",
            "content": """
              <strong>Quy tắc tháo ống dẫn khí trước khi tắt đèn cồn:</strong><br>
              Khi kết thúc thí nghiệm định tính $C$ và $H$, phải <strong>tháo rời ống dẫn khí</strong> ra khỏi dung dịch $Ca(OH)_2$ trước khi tắt đèn cồn. Nếu tắt đèn cồn trước, nhiệt độ trong ống nghiệm nung giảm đột ngột làm áp suất khí trong ống giảm mạnh, dung dịch $Ca(OH)_2$ sẽ bị hút ngược vào ống nghiệm đang nóng gây nứt vỡ ống và gây bỏng hóa chất!
            """
        }
    ]

    methods = [
        {
            "name": "Dạng 1: Phân loại hợp chất hữu cơ và Xác định nhóm chức",
            "content": "Phương pháp: Dựa vào thành phần nguyên tố để phân loại thành hydrocarbon (chỉ C, H) hay dẫn xuất (C, H và O, N, S, Cl...). Quan sát công thức cấu tạo để chỉ rõ nhóm chức: alcohol (-OH), carboxylic acid (-COOH), aldehyde (-CHO), ester (-COO-), amine (-NH2).",
            "examples": [
                {
                    "id": "c3_b8_vd1",
                    "num": 1,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Cho các chất sau: $CH_4, C_2H_5OH, CaCO_3, C_6H_6, CH_3Cl, CO_2, CH_3COOH$. Hãy phân loại các chất trên thành: Hợp chất vô cơ, Hydrocarbon và Dẫn xuất của hydrocarbon.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Hợp chất vô cơ: $CaCO_3$ (muối carbonate) và $CO_2$ (carbon dioxide).<br>- Hydrocarbon (chỉ chứa C và H): $CH_4$ (methane) và $C_6H_6$ (benzene).<br>- Dẫn xuất của hydrocarbon (ngoài C, H còn chứa O, Cl): $C_2H_5OH$ (ethanol), $CH_3Cl$ (chloromethane), $CH_3COOH$ (acetic acid)."
                },
                {
                    "id": "c3_b8_vd2",
                    "num": 2,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Chỉ ra nhóm chức có trong các phân tử sau và cho biết chúng thuộc loại hợp chất hữu cơ nào: a) $CH_3-CH_2-OH$; b) $CH_3-CH=O$; c) $CH_3-COO-CH_2-CH_3$; d) $CH_3-CH_2-NH_2$.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>a) Nhóm chức: $-OH$ (nhóm hydroxy) -> Hợp chất thuộc loại Alcohol.<br>b) Nhóm chức: $-CHO$ (nhóm formyl/aldehyde) -> Hợp chất thuộc loại Aldehyde.<br>c) Nhóm chức: $-COO-$ (nhóm ester) -> Hợp chất thuộc loại Ester.<br>d) Nhóm chức: $-NH_2$ (nhóm amino) -> Hợp chất thuộc loại Amine."
                },
                {
                    "id": "c3_b8_vd3",
                    "num": 3,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Paracetamol (thuốc hạ sốt, giảm đau phổ biến) có công thức cấu tạo: $p-HO-C_6H_4-NH-CO-CH_3$. Hãy xác định các nhóm chức hóa học có mặt trong phân tử paracetamol.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>Phân tử paracetamol chứa hai nhóm chức chính:<br>1. Nhóm chức phenol: $-OH$ liên kết trực tiếp với vòng thơm benzene (cho tính chất của phenol).<br>2. Nhóm chức amide: $-NH-CO-$ liên kết giữa nguyên tử nitrogen của nhóm amine và nhóm carbonyl (dẫn xuất carboxylic acid)."
                }
            ]
        },
        {
            "name": "Dạng 2: Phân tích định tính nguyên tố trong hợp chất hữu cơ",
            "content": "Phương pháp: Nắm vững vai trò chất oxi hóa của bột CuO khan, chất nhận biết nước là CuSO4 khan (trắng -> xanh), chất nhận biết CO2 là Ca(OH)2 (tạo kết tủa trắng CaCO3). Viết các phương trình hóa học diễn ra.",
            "examples": [
                {
                    "id": "c3_b8_vd4",
                    "num": 4,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Mô tả hiện tượng xảy ra và viết phương trình hóa học minh họa khi nung nóng hỗn hợp bột đường glucose ($C_6H_{12}O_6$) với bột $CuO$ khan trong ống nghiệm đậy kín có ống dẫn khí dẫn qua bông chứa $CuSO_4$ khan và dung dịch $Ca(OH)_2$.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Bột $CuO$ màu đen chuyển dần sang màu đỏ gạch của kim loại $Cu$. PTHH: $C_6H_{12}O_6 + 12CuO \\xrightarrow{t^o} 6CO_2\\uparrow + 6H_2O\\uparrow + 12Cu$.<br>- Hơi nước $H_2O$ thoát ra làm đổi màu bông chứa $CuSO_4$ khan từ màu trắng sang màu xanh lam: $CuSO_4 + 5H_2O \\rightarrow CuSO_4 \\cdot 5H_2O$.<br>- Khí $CO_2$ thoát ra làm dung dịch nước vôi trong vẩn đục: $CO_2 + Ca(OH)_2 \\rightarrow CaCO_3\\downarrow (\\text{trắng}) + H_2O$."
                },
                {
                    "id": "c3_b8_vd5",
                    "num": 5,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Tại sao trong thí nghiệm nung chất hữu cơ với $CuO$, ống nghiệm lại được đặt hơi dốc miệng xuống phía dưới một góc nhỏ (khoảng 10 - 15 độ)?",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>Trong quá trình nung nóng, hơi nước $H_2O$ sinh ra từ phản ứng bay lên và có thể ngưng tụ thành giọt lỏng ở thành ống nghiệm gần miệng. Việc đặt miệng ống nghiệm hơi dốc xuống giúp giọt nước ngưng tụ chảy ra phía ngoài, tránh trường hợp giọt nước chảy ngược trở lại đáy ống nghiệm đang ở nhiệt độ rất cao, gây sốc nhiệt làm nứt vỡ ống nghiệm."
                },
                {
                    "id": "c3_b8_vd6",
                    "num": 6,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Nêu phương pháp hóa học cụ thể để kiểm tra xem trong phân tử dung môi ethyl chloride ($C_2H_5Cl$) có chứa nguyên tố clo hay không.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>1. Lấy khoảng 1 mL $C_2H_5Cl$ vào ống nghiệm, thêm 2 mL dung dịch $NaOH$ loãng rồi đun nóng nhẹ (phản ứng thủy phân tạo $C_2H_5OH$ và $NaCl$).<br>2. Để nguội ống nghiệm, acid hóa dung dịch bằng vài giọt dung dịch $HNO_3$ loãng để trung hòa hết $NaOH$ dư.<br>3. Nhỏ vài giọt dung dịch $AgNO_3$ vào ống nghiệm: Xuất hiện kết tủa trắng của $AgCl$ ($Ag^+ + Cl^- \\rightarrow AgCl\\downarrow$). Hiện tượng này chứng minh trong phân tử có chứa nguyên tố chlorine."
                }
            ]
        },
        {
            "name": "Dạng 3: Bài toán đốt cháy và Định luật bảo toàn nguyên tố",
            "content": "Phương pháp: Áp dụng các định luật bảo toàn:<br>- Bảo toàn C: $n_C = n_{CO_2} = \\frac{m_{CO_2}}{44}$<br>- Bảo toàn H: $n_H = 2 \\times n_{H_2O} = 2 \\times \\frac{m_{H_2O}}{18}$<br>- Khối lượng O trong mẫu: $m_O = m_A - (m_C + m_H) = m_A - (12 \\times n_C + 1 \\times n_H)$. Nếu $m_O = 0$ -> phân tử chỉ có C, H. Nếu $m_O > 0$ -> phân tử có C, H, O.",
            "examples": [
                {
                    "id": "c3_b8_vd7",
                    "num": 7,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Đốt cháy hoàn toàn 4,60 gam một hợp chất hữu cơ X thu được 8,80 gam $CO_2$ và 5,40 gam $H_2O$. Chứng minh rằng phân tử chất X có chứa nguyên tố oxygen và tính khối lượng của nguyên tố oxygen trong 4,60 gam X.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Ta có: $n_C = n_{CO_2} = \\frac{8,80}{44} = 0,20 \\text{ mol} \\Rightarrow m_C = 0,20 \\times 12 = 2,40 \\text{ gam}$.<br>- $n_H = 2 \\times n_{H_2O} = 2 \\times \\frac{5,40}{18} = 0,60 \\text{ mol} \\Rightarrow m_H = 0,60 \\times 1 = 0,60 \\text{ gam}$.<br>- Tổng khối lượng $C$ và $H$ là: $m_C + m_H = 2,40 + 0,60 = 3,00 \\text{ gam} < 4,60 \\text{ gam}$.<br>$\\Rightarrow$ Trong X nhất thiết phải có nguyên tố oxygen ($O$).<br>- Khối lượng nguyên tố oxygen là: $m_O = 4,60 - 3,00 = 1,60 \\text{ gam} \\Rightarrow n_O = \\frac{1,60}{16} = 0,10 \\text{ mol}$."
                },
                {
                    "id": "c3_b8_vd8",
                    "num": 8,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Đốt cháy hoàn toàn 0,10 mol một hydrocarbon Y mạch hở thu được 13,2 gam $CO_2$ và 7,20 gam $H_2O$. Xác định công thức phân tử của hydrocarbon Y.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Số mol $CO_2$: $n_{CO_2} = \\frac{13,2}{44} = 0,30 \\text{ mol}$.<br>- Số mol $H_2O$: $n_{H_2O} = \\frac{7,20}{18} = 0,40 \\text{ mol}$.<br>- Số nguyên tử Carbon trong 1 phân tử Y: $\\text{Số C} = \\frac{n_C}{n_Y} = \\frac{0,30}{0,10} = 3$.<br>- Số nguyên tử Hydrogen trong 1 phân tử Y: $\\text{Số H} = \\frac{2 \\times n_{H_2O}}{n_Y} = \\frac{2 \\times 0,40}{0,10} = 8$.<br>$\\Rightarrow$ Vậy công thức phân tử của hydrocarbon Y là $C_3H_8$ (propane)."
                },
                {
                    "id": "c3_b8_vd9",
                    "num": 9,
                    "level": "level-vdc",
                    "levelName": "Vận dụng cao",
                    "title": "Đốt cháy hoàn toàn 6,00 gam hợp chất hữu cơ Z cần dùng vừa đủ 6,72 lít khí $O_2$ (đo ở điều kiện tiêu chuẩn). Dẫn toàn bộ sản phẩm cháy lần lượt qua bình (1) đựng $H_2SO_4$ đặc dư và bình (2) đựng dung dịch $Ba(OH)_2$ dư. Thấy khối lượng bình (1) tăng thêm 3,60 gam và bình (2) xuất hiện $m$ gam kết tủa trắng. Tính giá trị của $m$.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Khối lượng bình (1) tăng chính là khối lượng của nước bị hấp phụ: $m_{H_2O} = 3,60 \\text{ gam} \\Rightarrow n_{H_2O} = \\frac{3,60}{18} = 0,20 \\text{ mol}$.<br>- Số mol $O_2$ đã dùng: $n_{O_2} = \\frac{6,72}{22,4} = 0,30 \\text{ mol} \\Rightarrow m_{O_2} = 0,30 \\times 32 = 9,60 \\text{ gam}$.<br>- Theo Định luật bảo toàn khối lượng phản ứng cháy: $m_Z + m_{O_2} = m_{CO_2} + m_{H_2O}$<br>$\\Rightarrow m_{CO_2} = 6,00 + 9,60 - 3,60 = 12,00 \\text{ gam} \\Rightarrow n_{CO_2} = \\frac{12,00}{44} = \\frac{3}{11} \\text{ mol}$.<br>- Khí $CO_2$ đi qua dung dịch $Ba(OH)_2$ dư tạo kết tủa trắng $BaCO_3$: $CO_2 + Ba(OH)_2 \\rightarrow BaCO_3\\downarrow + H_2O$.<br>- Theo PTHH: $n_{BaCO_3} = n_{CO_2} = \\frac{3}{11} \\text{ mol} \\Rightarrow m = \\frac{3}{11} \\times 197 \\approx 53,73 \\text{ gam}$."
                }
            ]
        }
    ]

    return { "theory": theory, "methods": methods }

print("b8 full definition ready.")
