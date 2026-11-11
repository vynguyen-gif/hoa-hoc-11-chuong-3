# -*- coding: utf-8 -*-
"""
Full content for Lesson 10, Lesson 11, and Chapter 3 Review
"""

def get_b10_full():
    theory = [
        {
            "type": "tom_tat",
            "title": "1. Công thức đơn giản nhất và Công thức phân tử",
            "content": """
              <ul>
                <li><strong>Công thức đơn giản nhất (CTĐGN):</strong> Cho biết <strong>tỉ lệ số lượng nguyên tử tối giản</strong> (tỉ lệ các số nguyên dương nguyên tố cùng nhau) giữa các nguyên tố có trong phân tử hợp chất hữu cơ.
                  <br>Ví dụ: Acetic acid $C_2H_4O_2$ có CTĐGN là $CH_2O$ (tỉ lệ C : H : O = 1 : 2 : 1). Benzene $C_6H_6$ và acetylene $C_2H_2$ đều có chung CTĐGN là $CH$.</li>
                <li><strong>Công thức phân tử (CTPT):</strong> Cho biết <strong>số lượng nguyên tử thực tế</strong> của mỗi nguyên tố trong một phân tử hợp chất hữu cơ.
                  <br>Mối liên hệ tổng quát: $\\text{CTPT} = (\\text{CTĐGN})_n$ với $n$ là số nguyên dương ($n \\ge 1$). Khi biết phân tử khối $M$, ta tìm được $n = \\frac{M}{M_{\\text{CTĐGN}}}$.</li>
              </ul>
            """
        },
        {
            "type": "nhan_xet",
            "title": "2. Phương pháp xác định phân tử khối bằng Phổ khối lượng (MS)",
            "content": """
              <ul>
                <li><strong>Phổ khối lượng (Mass Spectrometry - MS):</strong> Là phương pháp hiện đại, chính xác nhất hiện nay dùng để xác định phân tử khối của hợp chất hữu cơ.</li>
                <li><strong>Pic ion phân tử $[M^+]$:</strong>
                  <ul>
                    <li>Khi mẫu chất bị bắn phá bởi chùm electron mang năng lượng cao, phân tử mất đi 1 electron tạo thành ion phân tử: $M + e^- \\rightarrow [M^+] + 2e^-$.</li>
                    <li>Trên phổ MS, pic tương ứng với ion phân tử $[M^+]$ thường là pic có giá trị $m/z$ (tỉ số khối lượng trên điện tích) <strong>lớn nhất</strong> (nằm ở rìa ngoài cùng bên phải của phổ, không kể các pic đồng vị rất nhỏ).</li>
                    <li><strong>Giá trị $m/z$ của pic $[M^+]$ chính là giá trị phân tử khối $M$</strong> của chất cần xác định (tính theo amu hoặc g/mol).</li>
                  </ul>
                </li>
              </ul>
            """
        },
        {
            "type": "tom_tat",
            "title": "3. Các phương pháp thiết lập Công thức phân tử",
            "content": """
              <ul>
                <li><strong>Cách 1: Từ thành phần phần trăm khối lượng (%C, %H, %O, %N):</strong>
                  <ul>
                    <li>Lập tỉ lệ mol tối giản: $n_C : n_H : n_O : n_N = \\frac{\\%C}{12} : \\frac{\\%H}{1} : \\frac{\\%O}{16} : \\frac{\\%N}{14} = p : q : r : s$.</li>
                    <li>Rút ra công thức đơn giản nhất $C_p H_q O_r N_s$.</li>
                    <li>Từ phân tử khối $M$ xác định qua phổ MS, giải phương trình: $(12p + q + 16r + 14s) \\times n = M \\Rightarrow n \\Rightarrow \\text{CTPT}$.</li>
                  </ul>
                </li>
                <li><strong>Cách 2: Tính trực tiếp số nguyên tử từ phân tử khối $M$:</strong>
                  <ul>
                    <li>Số nguyên tử $C = \\frac{M \\times \\%C}{12 \\times 100\\%}$</li>
                    <li>Số nguyên tử $H = \\frac{M \\times \\%H}{1 \\times 100\\%}$</li>
                    <li>Số nguyên tử $O = \\frac{M \\times \\%O}{16 \\times 100\\%}$</li>
                  </ul>
                </li>
              </ul>
            """
        },
        {
            "type": "chu_y",
            "title": "Chú ý khi tính toán từ sản phẩm đốt cháy",
            "content": """
              Đốt cháy hợp chất hữu cơ thu được $CO_2$ và $H_2O$:<br>
              - $n_C = n_{CO_2}$; $n_H = 2 \\times n_{H_2O}$.<br>
              - Luôn kiểm tra xem hợp chất có oxygen hay không bằng cách tính: $m_O = m_A - (12 \\times n_C + 1 \\times n_H)$.<br>
              - Nếu $m_O > 0 \\Rightarrow n_O = \\frac{m_O}{16}$. Sau đó lập tỉ lệ $n_C : n_H : n_O$.
            """
        }
    ]

    methods = [
        {
            "name": "Dạng 1: Xác định công thức đơn giản nhất từ % khối lượng",
            "content": "Phương pháp: Lập tỉ lệ mol: $x : y : z = \\frac{\\%C}{12} : \\frac{\\%H}{1} : \\frac{\\%O}{16}$. Chia tất cả các số cho số nhỏ nhất để đưa về tỉ lệ các số nguyên tối giản.",
            "examples": [
                {
                    "id": "c3_b10_vd1",
                    "num": 1,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Phân tích nguyên tố cho thấy vitamin C chứa 40,91% C, 4,55% H và 54,54% O về khối lượng. Xác định công thức đơn giản nhất của vitamin C.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Lập tỉ lệ số mol các nguyên tử trong phân tử:<br>$n_C : n_H : n_O = \\frac{40,91}{12} : \\frac{4,55}{1} : \\frac{54,54}{16} = 3,41 : 4,55 : 3,41$.<br>- Chia các số cho số nhỏ nhất ($3,41$):<br>$\\Rightarrow 1 : 1,333 : 1 = 1 : \\frac{4}{3} : 1 = 3 : 4 : 3$.<br>$\\Rightarrow$ Vậy công thức đơn giản nhất của vitamin C là $C_3H_4O_3$."
                },
                {
                    "id": "c3_b10_vd2",
                    "num": 2,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Một hydrocarbon chứa 85,71% carbon về khối lượng, còn lại là hydrogen. Tìm công thức đơn giản nhất của hydrocarbon này.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Phần trăm khối lượng của Hydrogen: $\\%H = 100\\% - 85,71\\% = 14,29\\%$.<br>- Tỉ lệ số mol nguyên tử:<br>$n_C : n_H = \\frac{85,71}{12} : \\frac{14,29}{1} = 7,1425 : 14,29 = 1 : 2$.<br>$\\Rightarrow$ Vậy công thức đơn giản nhất của hydrocarbon là $CH_2$."
                },
                {
                    "id": "c3_b10_vd3",
                    "num": 3,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Hợp chất hữu cơ X chứa các nguyên tố C, H, N có tỉ lệ khối lượng tương ứng là $m_C : m_H : m_N = 18 : 5 : 7$. Xác định công thức đơn giản nhất của X.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Ta có tỉ lệ mol các nguyên tử:<br>$n_C : n_H : n_N = \\frac{m_C}{12} : \\frac{m_H}{1} : \\frac{m_N}{14} = \\frac{18}{12} : \\frac{5}{1} : \\frac{7}{14} = 1,5 : 5 : 0,5$.<br>- Chia tất cả các số cho $0,5$:<br>$\\Rightarrow 3 : 10 : 1$.<br>$\\Rightarrow$ Vậy công thức đơn giản nhất của hợp chất X là $C_3H_{10}N$ (hoặc $C_3H_9N$ nếu tỉ lệ thực tế amine)."
                }
            ]
        },
        {
            "name": "Dạng 2: Biện luận CTPT từ CTĐGN và Phổ khối lượng (MS)",
            "content": "Phương pháp: Dựa vào pic ion phân tử $[M^+]$ trên phổ MS để xác định phân tử khối $M$. Giải phương trình: $M_{(\\text{CTĐGN})} \\times n = M \\Rightarrow n \\Rightarrow \\text{CTPT}$.",
            "examples": [
                {
                    "id": "c3_b10_vd4",
                    "num": 4,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Hợp chất hữu cơ A có công thức đơn giản nhất là $CH_2O$. Phổ khối lượng (MS) của chất A cho thấy pic ion phân tử $[M^+]$ xuất hiện tại $m/z = 60$. Hãy xác định công thức phân tử của chất A.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Giá trị $m/z$ của pic ion phân tử $[M^+]$ bằng $60 \\Rightarrow$ Phân tử khối của A là $M = 60 \\text{ amu}$.<br>- Công thức phân tử của A có dạng $(CH_2O)_n$.<br>- Ta có: $M = (12 + 2 \\times 1 + 16) \\times n = 30n = 60 \\Rightarrow n = \\frac{60}{30} = 2$.<br>$\\Rightarrow$ Vậy công thức phân tử của chất A là $C_2H_4O_2$."
                },
                {
                    "id": "c3_b10_vd5",
                    "num": 5,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Aspirin (thuốc giảm đau, hạ sốt) có công thức đơn giản nhất là $C_9H_8O_4$. Phổ MS của aspirin ghi nhận pic $[M^+]$ tại $m/z = 180$. Tìm công thức phân tử của aspirin.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Phân tử khối của aspirin từ phổ MS là $M = 180 \\text{ amu}$.<br>- Khối lượng mol ứng với CTĐGN $C_9H_8O_4$: $M_{\\text{CTĐGN}} = 12 \\times 9 + 8 \\times 1 + 16 \\times 4 = 108 + 8 + 64 = 180 \\text{ amu}$.<br>- Ta có: $180 \\times n = 180 \\Rightarrow n = 1$.<br>$\\Rightarrow$ Vậy công thức phân tử của aspirin trùng với công thức đơn giản nhất là $C_9H_8O_4$."
                },
                {
                    "id": "c3_b10_vd6",
                    "num": 6,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Một ester X có công thức đơn giản nhất là $C_2H_4O$. Tỉ khối hơi của X so với khí helium ($He, M=4$) bằng 22. Hãy xác định công thức phân tử của ester X.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Phân tử khối của ester X: $M_X = d_{X/He} \\times M_{He} = 22 \\times 4 = 88 \\text{ amu}$.<br>- Khối lượng của cụm $(C_2H_4O)$: $12 \\times 2 + 4 \\times 1 + 16 = 44 \\text{ amu}$.<br>- Ta có: $44 \\times n = 88 \\Rightarrow n = \\frac{88}{44} = 2$.<br>$\\Rightarrow$ Vậy công thức phân tử của ester X là $(C_2H_4O)_2 = C_4H_8O_2$."
                }
            ]
        },
        {
            "name": "Dạng 3: Xác định CTPT từ dữ liệu phản ứng đốt cháy",
            "content": "Phương pháp: Tính $n_C = n_{CO_2}, n_H = 2 n_{H_2O}, n_O = \\frac{m_A - m_C - m_H}{16}$. Sau đó tính số nguyên tử trong 1 phân tử: $\\text{Số C} = \\frac{n_C}{n_A}$, $\\text{Số H} = \\frac{n_H}{n_A}$, $\\text{Số O} = \\frac{n_O}{n_A}$.",
            "examples": [
                {
                    "id": "c3_b10_vd7",
                    "num": 7,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Đốt cháy hoàn toàn 2,20 gam một hợp chất hữu cơ Y chứa C, H, O thu được 4,40 gam $CO_2$ và 1,80 gam $H_2O$. Biết phân tử khối của Y là 88 amu. Hãy xác định công thức phân tử của Y.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Số mol $CO_2$: $n_{CO_2} = \\frac{4,40}{44} = 0,10 \\text{ mol} \\Rightarrow n_C = 0,10 \\text{ mol} (m_C = 1,20 \\text{ g})$.<br>- Số mol $H_2O$: $n_{H_2O} = \\frac{1,80}{18} = 0,10 \\text{ mol} \\Rightarrow n_H = 0,20 \\text{ mol} (m_H = 0,20 \\text{ g})$.<br>- Khối lượng oxygen trong Y: $m_O = 2,20 - (1,20 + 0,20) = 0,80 \\text{ gam} \\Rightarrow n_O = \\frac{0,80}{16} = 0,05 \\text{ mol}$.<br>- Số mol của Y đã đốt cháy: $n_Y = \\frac{2,20}{88} = 0,025 \\text{ mol}$.<br>- Số nguyên tử trong phân tử Y:<br>$\\text{Số C} = \\frac{n_C}{n_Y} = \\frac{0,10}{0,025} = 4$; $\\text{Số H} = \\frac{n_H}{n_Y} = \\frac{0,20}{0,025} = 8$; $\\text{Số O} = \\frac{n_O}{n_Y} = \\frac{0,05}{0,025} = 2$.<br>$\\Rightarrow$ Vậy công thức phân tử của Y là $C_4H_8O_2$."
                },
                {
                    "id": "c3_b10_vd8",
                    "num": 8,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Đốt cháy hoàn toàn 0,10 mol một hydrocarbon mạch hở Z cần vừa đủ 11,2 lít khí $O_2$ (đktc) thu được 6,72 lít khí $CO_2$ (đktc) và $m$ gam hơi nước. Xác định công thức phân tử của Z.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Số mol $O_2$ đã dùng: $n_{O_2} = \\frac{11,2}{22,4} = 0,50 \\text{ mol}$.<br>- Số mol $CO_2$ thu được: $n_{CO_2} = \\frac{6,72}{22,4} = 0,30 \\text{ mol} \\Rightarrow \\text{Số nguyên tử C} = \\frac{0,30}{0,10} = 3$.<br>- Áp dụng Định luật bảo toàn nguyên tố Oxygen cho phản ứng cháy:<br>$2 \\times n_{O_2} = 2 \\times n_{CO_2} + n_{H_2O} \\Rightarrow 2 \\times 0,50 = 2 \\times 0,30 + n_{H_2O} \\Rightarrow n_{H_2O} = 1,00 - 0,60 = 0,40 \\text{ mol}$.<br>- Số nguyên tử Hydrogen trong phân tử Z: $\\text{Số H} = \\frac{2 \\times n_{H_2O}}{n_Z} = \\frac{2 \\times 0,40}{0,10} = 8$.<br>$\\Rightarrow$ Vậy công thức phân tử của Z là $C_3H_8$ (propane)."
                },
                {
                    "id": "c3_b10_vd9",
                    "num": 9,
                    "level": "level-vdc",
                    "levelName": "Vận dụng cao",
                    "title": "Đốt cháy hoàn toàn 1,18 gam một amine no, đơn chức, mạch hở Q bằng lượng không khí vừa đủ (chứa 20% $O_2$ và 80% $N_2$ về thể tích). Dẫn toàn bộ hỗn hợp khí và hơi sau phản ứng qua bình đựng $P_2O_5$ dư, thấy khối lượng bình tăng 1,62 gam và có 8,512 lít khí trơ (đktc) thoát ra khỏi bình. Tìm công thức phân tử của amine Q.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Bình $P_2O_5$ hút toàn bộ nước: $m_{H_2O} = 1,62 \\text{ gam} \\Rightarrow n_{H_2O} = \\frac{1,62}{18} = 0,09 \\text{ mol} \\Rightarrow n_H = 0,18 \\text{ mol}$.<br>- Amine no, đơn chức, mạch hở có CTPT dạng $C_n H_{2n+3} N$.<br>- Ta có tỉ lệ: $\\frac{n_H}{n_Q} = 2n + 3$. Khối lượng phân tử: $M_Q = 14n + 17$.<br>- Khối lượng $Q$: $m_Q = n_Q \\times (14n + 17) = \\frac{0,18}{2n+3} \\times (14n + 17) = 1,18 \\text{ gam}$.<br>$\\Rightarrow 0,18 \\times (14n + 17) = 1,18 \\times (2n + 3) \\Rightarrow 2,52n + 3,06 = 2,36n + 3,54$<br>$\\Rightarrow 0,16n = 0,48 \\Rightarrow n = 3$.<br>$\\Rightarrow$ Vậy công thức phân tử của amine Q là $C_3H_9N$ (phân tử khối $M = 59 \\text{ amu}$)."
                }
            ]
        }
    ]

    return { "theory": theory, "methods": methods }

print("b10 full definition ready.")
