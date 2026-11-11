# -*- coding: utf-8 -*-
"""
All Concrete Essay Bank: Real, Full Step-by-Step Solutions for all 17 Essay Questions
No generic placeholder text anywhere.
"""

def get_domain_essay_bank(domain_key, lesson_name, lid):
    if domain_key == "c1":
        return [
            {
                "num": 32,
                "title": f"Trình bày định nghĩa phản ứng thuận nghịch, trạng thái cân bằng hoá học và biểu thức hằng số cân bằng Kc đối với {lesson_name}.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Phản ứng thuận nghịch:</strong> Là phản ứng hóa học xảy ra theo cả hai chiều thuận và nghịch trong cùng điều kiện xác định ($aA + bB \\rightleftharpoons cC + dD$).<br>"
                               "2. <strong>Trạng thái cân bằng hóa học:</strong> Là trạng thái của phản ứng thuận nghịch khi tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch ($v_t = v_n > 0$). Đây là một <em>cân bằng động</em>, nồng độ các chất trong hệ không đổi theo thời gian.<br>"
                               "3. <strong>Hằng số cân bằng Kc:</strong> Đối với phản ứng trên, $K_c = \\frac{[C]^c [D]^d}{[A]^a [B]^b}$. $K_c$ chỉ phụ thuộc vào bản chất phản ứng và nhiệt độ, không phụ thuộc vào nồng độ ban đầu hay sự có mặt của chất xúc tác."
            },
            {
                "num": 33,
                "title": "Nêu thuyết Brønsted - Lowry về acid - base và phân loại các chất/ion sau: HCl, NaOH, NH3, HCO3-, CH3COO-.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Thuyết Brønsted - Lowry:</strong> Acid là chất có khả năng cho proton ($H^+$); Base là chất có khả năng nhận proton ($H^+$).<br>"
                               "2. <strong>Phân loại cụ thể:</strong><br>"
                               "- $HCl$: Là acid vì nhường proton cho nước: $HCl + H_2O \\rightarrow H_3O^+ + Cl^-$.<br>"
                               "- $NaOH$: Phân li tạo $OH^-$ có khả năng nhận $H^+$, dung dịch có tính base mạnh.<br>"
                               "- $NH_3$: Là base vì nhận proton từ nước: $NH_3 + H_2O \\rightleftharpoons NH_4^+ + OH^-$.<br>"
                               "- $HCO_3^-$: Là ion lưỡng tính vì vừa có thể cho vừa có thể nhận $H^+$:<br>"
                               "&nbsp;&nbsp;+ Cho $H^+$: $HCO_3^- + H_2O \\rightleftharpoons CO_3^{2-} + H_3O^+$ (tính acid).<br>"
                               "&nbsp;&nbsp;+ Nhận $H^+$: $HCO_3^- + H_2O \\rightleftharpoons H_2CO_3 + OH^-$ (tính base).<br>"
                               "- $CH_3COO^-$: Là base (nhận $H^+$): $CH_3COO^- + H_2O \\rightleftharpoons CH_3COOH + OH^-$."
            },
            {
                "num": 34,
                "title": "Viết 2 phương trình hoá học minh hoạ cho phản ứng thuận nghịch và phản ứng trao đổi ion trong dung dịch điện li.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Phản ứng thuận nghịch:</strong> Quá trình tổng hợp ammonia từ nitrogen và hydrogen trong pha khí:<br>"
                               "$$N_2(g) + 3H_2(g) \\xrightleftharpoons[Fe, p]{t^o} 2NH_3(g) \\quad \\Delta_r H_{298}^o = -92\\text{ kJ}$$<br>"
                               "2. <strong>Phản ứng trao đổi ion tạo kết tủa:</strong> Cho dung dịch barium chloride tác dụng với dung dịch sodium sulfate:<br>"
                               "$$BaCl_2(aq) + Na_2SO_4(aq) \\rightarrow BaSO_4\\downarrow (\\text{trắng}) + 2NaCl(aq)$$<br>"
                               "Phương trình ion rút gọn: $Ba^{2+}(aq) + SO_4^{2-}(aq) \\rightarrow BaSO_4\\downarrow$."
            },
            {
                "num": 35,
                "title": "Giải thích hiện tượng đổi màu dung dịch khi thêm acid hoặc kiềm vào hệ cân bằng chromate và dichromate.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "Trong dung dịch nước tồn tại cân bằng chuyển dịch màu sắc giữa ion chromate và dichromate:<br>"
                               "$$2CrO_4^{2-} \\text{ (màu vàng)} + 2H^+ \\rightleftharpoons Cr_2O_7^{2-} \\text{ (màu da cam)} + H_2O$$<br>"
                               "1. <strong>Khi thêm dung dịch acid (HCl):</strong> Nồng độ ion $H^+$ tăng lên, theo nguyên lí Le Chatelier, cân bằng tự động chuyển dịch theo chiều thuận để làm giảm $H^+$, tạo thêm nhiều ion $Cr_2O_7^{2-}$ làm dung dịch chuyển sang màu da cam đậm.<br>"
                               "2. <strong>Khi thêm dung dịch base (NaOH):</strong> Ion $OH^-$ phản ứng với $H^+$ tạo $H_2O$, làm nồng độ $H^+$ giảm xuống. Cân bằng chuyển dịch theo chiều nghịch để tái tạo $H^+$, sinh ra nhiều ion $CrO_4^{2-}$ làm dung dịch chuyển trở lại màu vàng tươi."
            },
            {
                "num": 36,
                "title": "So sánh độ dẫn điện của dung dịch HCl 0,1 M và dung dịch CH3COOH 0,1 M có cùng thể tích. Giải thích chi tiết.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>So sánh:</strong> Dung dịch $HCl$ 0,1 M dẫn điện tốt hơn rất nhiều so với dung dịch $CH_3COOH$ 0,1 M (bóng đèn trong mạch thử độ dẫn điện sáng rực với $HCl$ và chỉ sáng mờ le lói với $CH_3COOH$).<br>"
                               "2. <strong>Giải thích bản chất:</strong><br>"
                               "- Khả năng dẫn điện của dung dịch phụ thuộc vào nồng độ các ion tự do mang điện tích trong dung dịch.<br>"
                               "- $HCl$ là chất điện li mạnh, phân li hoàn toàn: $HCl \\rightarrow H^+ + Cl^- \\Rightarrow [H^+] = [Cl^-] = 0,1\\text{ M}$. Mật độ ion mang điện tích rất cao.<br>"
                               "- $CH_3COOH$ là chất điện li yếu, phân li thuận nghịch một phần: $CH_3COOH \\rightleftharpoons CH_3COO^- + H^+$. Với hằng số $K_a \\approx 1,75 \\times 10^{-5}$, độ điện li $\\alpha \\approx 1,3\\%$, nồng độ ion tự do chỉ khoảng $1,3 \\times 10^{-3}\\text{ M}$ (nhỏ hơn gần 100 lần so với $HCl$), do đó khả năng dẫn điện yếu hơn nhiều."
            },
            {
                "num": 37,
                "title": "Phát biểu nguyên lí chuyển dịch cân bằng Le Chatelier và phân tích ảnh hưởng của nhiệt độ, áp suất đến cân bằng phản ứng.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Phát biểu nguyên lí:</strong> Một phản ứng thuận nghịch đang ở trạng thái cân bằng, khi chịu một tác động từ bên ngoài (như biến đổi nhiệt độ, áp suất hoặc nồng độ), cân bằng sẽ tự chuyển dịch theo chiều làm giảm tác động bên ngoài đó.<br>"
                               "2. <strong>Ảnh hưởng của nhiệt độ:</strong><br>"
                               "- Khi tăng nhiệt độ, cân bằng chuyển dịch theo chiều thu nhiệt (chiều có $\\Delta_r H > 0$).<br>"
                               "- Khi giảm nhiệt độ, cân bằng chuyển dịch theo chiều tỏa nhiệt (chiều có $\\Delta_r H < 0$).<br>"
                               "3. <strong>Ảnh hưởng của áp suất:</strong><br>"
                               "- Áp suất chỉ ảnh hưởng đến hệ cân bằng có mặt chất khí và có sự biến thiên tổng số mol khí giữa hai vế.<br>"
                               "- Khi tăng áp suất chung của hệ, cân bằng chuyển dịch theo chiều làm giảm số mol khí; khi giảm áp suất, cân bằng chuyển dịch theo chiều làm tăng số mol khí."
            },
            {
                "num": 38,
                "title": "Trình bày quy tắc an toàn thực hành khi thao tác với các hóa chất và dụng cụ thí nghiệm của bài.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Thao tác với dung dịch acid mạnh và base mạnh:</strong> Luôn đeo kính bảo hộ và găng tay cao su. Khi pha loãng $H_2SO_4$ đặc, luôn rót từ từ acid vào cốc chứa sẵn nước và khuấy đều bằng đũa thủy tinh, tuyệt đối không làm ngược lại vì sẽ làm nước sôi cục bộ bắn acid ăn mòn vào người.<br>"
                               "2. <strong>Kĩ thuật sử dụng buret và pipet trong chuẩn độ:</strong> Dùng quả bóp hút cao su để nạp hóa chất vào pipet, cấm dùng miệng hút. Nạp dung dịch vào buret phải xả bọt khí ở khóa đuôi; đọc thể tích ngang tầm mắt tại đáy mặt khum cong của chất lỏng để triệt tiêu sai số thị giác.<br>"
                               "3. <strong>Sơ cứu và xử lí chất thải:</strong> Nếu bị dính acid vào da, rửa ngay dưới vòi nước chảy liên tục trong 10-15 phút, sau đó rửa lại bằng dung dịch $NaHCO_3$ loãng 2%. Dung dịch thừa phải được trung hòa về khoảng pH 6 - 8 trước khi đổ vào cống xả thải chung."
            },
            {
                "num": 39,
                "title": "Giải thích vì sao dung dịch CH3COONa có môi trường base (pH > 7) còn dung dịch NH4Cl có môi trường acid (pH < 7).",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Dung dịch CH3COONa:</strong><br>"
                               "- Phân li hoàn toàn trong nước: $CH_3COONa \\rightarrow Na^+ + CH_3COO^-$.<br>"
                               "- Cation $Na^+$ là cation của base mạnh ($NaOH$) nên không bị thủy phân.<br>"
                               "- Anion $CH_3COO^-$ là base liên hợp của acid yếu $CH_3COOH$, nhận proton từ nước (sự thủy phân):<br>"
                               "$$CH_3COO^- + H_2O \\rightleftharpoons CH_3COOH + OH^-$$<br>"
                               "Ion $OH^-$ sinh ra làm cho $[OH^-] > [H^+] \\Rightarrow pH > 7$ (môi trường kiềm nhẹ làm quỳ tím hóa xanh nhạt).<br>"
                               "2. <strong>Dung dịch NH4Cl:</strong><br>"
                               "- Phân li: $NH_4Cl \\rightarrow NH_4^+ + Cl^-$. Ion $Cl^-$ trơ không bị thủy phân.<br>"
                               "- Cation $NH_4^+$ là acid liên hợp của base yếu $NH_3$, nhường proton cho nước:<br>"
                               "$$NH_4^+ + H_2O \\rightleftharpoons NH_3 + H_3O^+$$<br>"
                               "Ion $H_3O^+$ ($H^+$) sinh ra làm $[H^+] > [OH^-] \\Rightarrow pH < 7$ (môi trường acid làm quỳ tím hóa hồng nhạt)."
            },
            {
                "num": 40,
                "title": "Nêu các ứng dụng thực tiễn của việc kiểm soát pH trong nông nghiệp, y học và xử lí môi trường.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Trong nông nghiệp và thổ nhưỡng:</strong> Cây trồng phát triển tối ưu trong từng dải pH nhất định (lúa nước: pH 5,5 - 6,5; ngô, mía: pH 6,0 - 7,0). Khi đất bị chua phèn (pH < 5,0), người nông dân bón vôi bột ($CaO, Ca(OH)_2$) để nâng pH, khử độc ion nhôm $Al^{3+}$, sắt $Fe^{3+}$ tự do.<br>"
                               "2. <strong>Trong y học và sinh lí cơ thể:</strong> Độ pH của máu người được điều hòa nghiêm ngặt bởi hệ đệm bicarbonate ($H_2CO_3 / HCO_3^-$) trong dải hẹp $7,35 - 7,45$. Dịch vị dạ dày chứa acid $HCl$ với pH từ 1,5 đến 2,5 giúp hoạt hóa pepsin tiêu hóa đạm; bệnh nhân viêm loét dạ dày do dư acid được kê đơn dùng thuốc chứa $Al(OH)_3, Mg(OH)_2$ hoặc $NaHCO_3$ để trung hòa bớt acid.<br>"
                               "3. <strong>Trong xử lí môi trường:</strong> Nước thải công nghiệp trước khi thải ra sông hồ phải được điều chỉnh pH về dải an toàn (6,5 - 8,5) để tránh gây hủy diệt hệ vi sinh vật và sinh vật thủy sinh."
            },
            {
                "num": 41,
                "title": "Trình bày phương pháp hoá học nhận biết 3 dung dịch mất nhãn: HCl, Ba(OH)2, Na2SO4.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Thuốc thử:</strong> Dùng quỳ tím và chính dung dịch vừa nhận biết.<br>"
                               "2. <strong>Tiến hành:</strong><br>"
                               "- Lấy một ít mỗi dung dịch ra làm mẫu thử tương ứng.<br>"
                               "- Nhúng mẩu giấy quỳ tím vào 3 mẫu thử:<br>"
                               "&nbsp;&nbsp;+ Mẫu thử làm quỳ tím hóa đỏ là dung dịch $HCl$.<br>"
                               "&nbsp;&nbsp;+ Mẫu thử làm quỳ tím hóa xanh là dung dịch $Ba(OH)_2$.<br>"
                               "&nbsp;&nbsp;+ Mẫu thử không làm đổi màu quỳ tím là dung dịch $Na_2SO_4$.<br>"
                               "3. <strong>Kiểm chứng lại bằng phản ứng:</strong> Nhỏ vài giọt dung dịch $Ba(OH)_2$ vừa nhận biết vào ống nghiệm chứa $Na_2SO_4$, thấy xuất hiện ngay kết tủa trắng $BaSO_4$ không tan trong acid:<br>"
                               "$$Ba(OH)_2 + Na_2SO_4 \\rightarrow BaSO_4\\downarrow + 2NaOH$$"
            },
            {
                "num": 42,
                "title": "Cho 100 mL dung dịch Ba(OH)2 0,1 M tác dụng với 100 mL dung dịch H2SO4 0,08 M. Tính khối lượng kết tủa BaSO4 thu được và pH của dung dịch sau phản ứng.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Số mol các chất ban đầu:</strong><br>"
                               "- $n_{Ba(OH)_2} = 0,1 \\times 0,1 = 0,01\\text{ mol} \\Rightarrow n_{Ba^{2+}} = 0,01\\text{ mol}; \\quad n_{OH^-} = 0,02\\text{ mol}$.<br>"
                               "- $n_{H_2SO_4} = 0,1 \\times 0,08 = 0,008\\text{ mol} \\Rightarrow n_{SO_4^{2-}} = 0,008\\text{ mol}; \\quad n_{H^+} = 0,016\\text{ mol}$.<br>"
                               "2. <strong>Tính khối lượng kết tủa:</strong><br>"
                               "$$Ba^{2+} + SO_4^{2-} \\rightarrow BaSO_4\\downarrow$$<br>"
                               "So sánh tỉ lệ: $n_{Ba^{2+}} (0,01) > n_{SO_4^{2-}} (0,008) \\Rightarrow Ba^{2+}$ dư, tính theo $SO_4^{2-}$.<br>"
                               "$\\Rightarrow n_{BaSO_4} = 0,008\\text{ mol} \\Rightarrow m_{BaSO_4} = 0,008 \\times 233 = 1,864\\text{ gam}$.<br>"
                               "3. <strong>Tính pH của dung dịch sau phản ứng:</strong><br>"
                               "$$H^+ + OH^- \\rightarrow H_2O$$<br>"
                               "- $n_{OH^-\\text{ dư}} = 0,02 - 0,016 = 0,004\\text{ mol}$.<br>"
                               "- Tổng thể tích dung dịch sau trộn: $V_{dd} = 100 + 100 = 200\\text{ mL} = 0,2\\text{ L}$.<br>"
                               "- Nồng độ $OH^-$ dư: $[OH^-] = \\frac{0,004}{0,2} = 0,02\\text{ M}$.<br>"
                               "- $pOH = -\\log(0,02) \\approx 1,70 \\Rightarrow pH = 14 - 1,70 = 12,30$."
            },
            {
                "num": 43,
                "title": "Cho 0,4 mol N2 tác dụng với 0,9 mol H2 trong bình kín có xúc tác Fe ở nhiệt độ cao. Khi cân bằng thu được 0,2 mol NH3. Tính hiệu suất phản ứng tổng hợp.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Phương trình hóa học:</strong><br>"
                               "$$N_2(g) + 3H_2(g) \\rightleftharpoons 2NH_3(g)$$<br>"
                               "2. <strong>Xác định chất phản ứng hết theo lí thuyết:</strong><br>"
                               "So sánh tỉ lệ mol ban đầu theo hệ số phản ứng: $\\frac{0,4}{1} > \\frac{0,9}{3} = 0,3 \\Rightarrow$ Hiệu suất phản ứng phải tính theo $H_2$.<br>"
                               "3. <strong>Tính lượng phản ứng và hiệu suất:</strong><br>"
                               "- Theo PTHH, số mol $H_2$ đã tham gia phản ứng là: $n_{H_2\\text{ pứ}} = \\frac{3}{2} n_{NH_3} = \\frac{3}{2} \\times 0,2 = 0,3\\text{ mol}$.<br>"
                               "- Hiệu suất của phản ứng tổng hợp $NH_3$:<br>"
                               "$$H\\% = \\frac{n_{H_2\\text{ pứ}}}{n_{H_2\\text{ ban đầu}}} \\times 100\\% = \\frac{0,3}{0,9} \\times 100\\% \\approx 33,33\\%.$$"
            },
            {
                "num": 44,
                "title": "Phân tích tác động của các nguồn thải acid, kiềm đối với môi trường tự nhiên và giải pháp xử lí nước thải bằng phương pháp trung hòa.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Tác động môi trường:</strong> Nước thải công nghiệp chứa acid mạnh (từ mạ điện, luyện kim) hoặc kiềm mạnh (từ dệt nhuộm, sản xuất giấy) làm biến đổi đột ngột pH nguồn nước tiếp nhận. Khi pH < 6 hoặc pH > 9, màng mang của cá bị tổn thương, hệ thủy sinh bị ngộ độc chết hàng loạt; acid ngấm vào đất hòa tan các ion kim loại nặng ($Cd^{2+}, Pb^{2+}, Hg^{2+}$) gây ô nhiễm chuỗi thức ăn sinh thái.<br>"
                               "2. <strong>Giải pháp bằng phương pháp trung hòa:</strong><br>"
                               "- <em>Xử lí nước thải acid:</em> Dùng vôi tôi ($Ca(OH)_2$) hoặc đá vôi nghiền vụn ($CaCO_3$) sục vào bể lắng trung hòa: $2H^+ + Ca(OH)_2 \\rightarrow Ca^{2+} + 2H_2O$. Phương pháp này rẻ tiền và kết tủa bớt một số tạp chất.<br>"
                               "- <em>Xử lí nước thải kiềm:</em> Sục khí thải công nghiệp chứa $CO_2$ hoặc dùng dung dịch $H_2SO_4$ loãng để trung hòa về pH 7,0 trước khi xả ra môi trường."
            },
            {
                "num": 45,
                "title": "Viết phương trình hóa học biểu diễn chuỗi biến hóa 3 giai đoạn: N2 -> NH3 -> NO -> NO2 kèm điều kiện cụ thể.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Giai đoạn 1 (N2 thành NH3):</strong><br>"
                               "$$N_2(g) + 3H_2(g) \\xrightleftharpoons[450^o\\text{C}, 200\\text{ bar}]{\\text{xúc tác Fe}} 2NH_3(g)$$<br>"
                               "2. <strong>Giai đoạn 2 (NH3 thành NO):</strong> Oxi hóa ammonia có xúc tác bạch kim ở nhiệt độ cao:<br>"
                               "$$4NH_3 + 5O_2 \\xrightarrow{850-900^o\\text{C}, Pt} 4NO + 6H_2O$$<br>"
                               "3. <strong>Giai đoạn 3 (NO thành NO2):</strong> Khí NO không màu tự oxi hóa trong không khí ở nhiệt độ phòng tạo khí màu nâu đỏ:<br>"
                               "$$2NO + O_2 \\rightarrow 2NO_2$$"
            },
            {
                "num": 46,
                "title": "Giải thích vì sao một số phản ứng hóa học cần phải đun nóng hoặc có chất xúc tác thích hợp mới diễn ra.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Khái niệm năng lượng hoạt hóa (Ea):</strong> Năng lượng hoạt hóa là năng lượng tối thiểu mà các phân tử chất tham gia phản ứng cần phải có để va chạm hiệu quả và bẻ gãy các liên kết hóa học cũ nhằm hình thành liên kết mới.<br>"
                               "2. <strong>Tác dụng của việc đun nóng:</strong> Làm tăng nhiệt độ $\\Rightarrow$ tăng động năng trung bình của các phân tử, làm tăng số lượng phân tử có năng lượng bằng hoặc lớn hơn năng lượng hoạt hóa, đồng thời tăng tần số va chạm hiệu quả giữa các phân tử, làm tốc độ phản ứng tăng mạnh.<br>"
                               "3. <strong>Tác dụng của chất xúc tác:</strong> Chất xúc tác làm thay đổi cơ chế phản ứng, tạo ra một lộ trình phản ứng mới có năng lượng hoạt hóa $E_a$ thấp hơn nhiều so với khi không có xúc tác, giúp phản ứng diễn ra nhanh chóng ở điều kiện nhiệt độ êm dịu hơn mà chất xúc tác không bị tiêu hao sau phản ứng."
            },
            {
                "num": 47,
                "title": "Hòa tan hoàn toàn 4 gam NaOH rắn vào nước cất để được 500 mL dung dịch. Tính nồng độ mol của NaOH và pH của dung dịch thu được.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Tính số mol NaOH:</strong><br>"
                               "$$n_{NaOH} = \\frac{m}{M} = \\frac{4}{40} = 0,1\\text{ mol}$$<br>"
                               "2. <strong>Nồng độ mol của dung dịch:</strong><br>"
                               "$$C_M = \\frac{n}{V} = \\frac{0,1}{0,5} = 0,2\\text{ M}$$<br>"
                               "3. <strong>Tính pH:</strong><br>"
                               "- $NaOH$ là bazơ mạnh phân li hoàn toàn: $NaOH \\rightarrow Na^+ + OH^- \\Rightarrow [OH^-] = 0,2\\text{ M}$.<br>"
                               "- $pOH = -\\log[OH^-] = -\\log(0,2) \\approx 0,70$.<br>"
                               "- $pH = 14 - pOH = 14 - 0,70 = 13,30$."
            },
            {
                "num": 48,
                "title": f"Tổng kết những bài học kinh nghiệm và kiến thức cốt lõi cần ghi nhớ khi giải bài tập về {lesson_name}.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Cân bằng động và biểu thức Kc:</strong> Luôn ghi nhớ quy ước không đưa nồng độ chất rắn nguyên chất vào biểu thức hằng số cân bằng $K_c$. Khi viết biểu thức hằng số cân bằng, số mũ của mỗi chất chính là hệ số tỉ lượng trong phương trình hóa học đã cân bằng.<br>"
                               "2. <strong>Quy luật Le Chatelier:</strong> Chú ý khi tăng áp suất, chỉ những hệ phản ứng có số mol khí ở hai vế chênh lệch nhau mới bị chuyển dịch cân bằng; nếu $\\Delta n_{khí} = 0$ thì áp suất không ảnh hưởng.<br>"
                               "3. <strong>Tính toán pH:</strong> Với dung dịch kiềm, luôn tính qua nồng độ ion $OH^- \\rightarrow pOH \\rightarrow pH = 14 - pOH$, tuyệt đối không suy trực tiếp $pH = -\\log[OH^-]$ để tránh sai số cơ bản trong bài thi."
            }
        ]

    elif domain_key == "c2":
        return [
            {
                "num": 32,
                "title": f"Trình bày cấu tạo phân tử, số oxi hóa và tính chất hóa học cơ bản của nitrogen và các hợp chất trong {lesson_name}.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Phân tử Nitrogen (N2):</strong> Gồm hai nguyên tử N liên kết với nhau bằng một liên kết ba rất bền vững ($:N \\equiv N:$). Năng lượng liên kết rất lớn ($945\\text{ kJ/mol}$), do đó ở nhiệt độ thường nitrogen khá trơ về mặt hóa học.<br>"
                               "2. <strong>Các mức số oxi hóa của nitrogen:</strong> $-3$ (trong $NH_3, NH_4^+$), $0$ (trong $N_2$), $+1$ ($N_2O$), $+2$ ($NO$), $+3$ ($N_2O_3, HNO_2$), $+4$ ($NO_2$), $+5$ ($HNO_3, NO_3^-$).<br>"
                               "3. <strong>Tính chất hóa học:</strong> Nitrogen vừa có tính oxi hóa (tác dụng với kim loại kiềm, $Mg, H_2$) vừa có tính khử (tác dụng với $O_2$ ở nhiệt độ cao hoặc tia lửa điện)."
            },
            {
                "num": 33,
                "title": "Nêu cấu tạo phân tử và giải thích nguyên nhân gây nên tính base yếu và tính khử của ammonia (NH3).",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Cấu tạo phân tử NH3:</strong> Có dạng hình chóp tam giác, nguyên tử N ở đỉnh chóp liên kết với 3 nguyên tử H bằng 3 liên kết cộng hóa trị phân cực. Trên nguyên tử N còn một cặp electron tự do chưa liên kết.<br>"
                               "2. <strong>Tính base yếu:</strong> Nhờ có cặp electron tự do chưa liên kết, phân tử $NH_3$ dễ dàng nhận proton $H^+$ từ nước: $NH_3 + H_2O \\rightleftharpoons NH_4^+ + OH^-$, làm quỳ tím chuyển màu xanh.<br>"
                               "3. <strong>Tính khử mạnh:</strong> Trong $NH_3$, nguyên tử N có số oxi hóa thấp nhất là $-3$, do đó $NH_3$ dễ dàng bị oxi hóa lên các số oxi hóa cao hơn ($0, +2$) khi tác dụng với các chất oxi hóa như $O_2, Cl_2, CuO$."
            },
            {
                "num": 34,
                "title": "Viết 2 phương trình hóa học minh họa tính khử của ammonia (NH3) và tính oxi hóa mạnh của acid nitric (HNO3).",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Tính khử của NH3:</strong> Khí $NH_3$ khử bột $CuO$ màu đen thành kim loại $Cu$ màu đỏ ở nhiệt độ cao:<br>"
                               "$$2NH_3 + 3CuO \\xrightarrow{t^o} N_2 + 3Cu + 3H_2O$$<br>"
                               "2. <strong>Tính oxi hóa mạnh của HNO3:</strong> Dung dịch $HNO_3$ đặc oxi hóa kim loại đồng ($Cu$) giải phóng khí $NO_2$ màu nâu đỏ:<br>"
                               "$$Cu + 4HNO_3 \\text{ (đặc)} \\rightarrow Cu(NO_3)_2 + 2NO_2\\uparrow (\\text{nâu đỏ}) + 2H_2O$$"
            },
            {
                "num": 35,
                "title": "Mô tả hiện tượng và viết phương trình hóa học của thí nghiệm khói trắng giữa khí ammonia và khí hydrogen chloride.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Hiện tượng quan sát được:</strong> Khi đưa hai đầu đũa thủy tinh (một đũa nhúng vào dung dịch $NH_3$ đặc, một đũa nhúng vào dung dịch $HCl$ đặc) lại gần nhau, ngay lập tức xuất hiện làn khói trắng dày đặc bao quanh hai đầu đũa dù hai đũa chưa chạm vào nhau.<br>"
                               "2. <strong>Giải thích và phương trình hóa học:</strong> Cả $NH_3$ và $HCl$ đều là những chất khí dễ bay hơi thoát ra khỏi dung dịch đậm đặc. Khi gặp nhau trong không khí, chúng kết hợp ngay với nhau tạo thành các hạt tinh thể muối ammonium chloride cực nhỏ phân tán lơ lửng trong không khí nhìn như khói trắng:<br>"
                               "$$NH_3(g) + HCl(g) \\rightarrow NH_4Cl(s) \\text{ (khói trắng tinh thể)}$$"
            },
            {
                "num": 36,
                "title": "So sánh tính chất vật lí và độ tan trong nước của khí NH3 và khí N2. Giải thích chi tiết.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Độ tan:</strong> Khí $NH_3$ tan cực kì nhiều trong nước (ở $20^o\\text{C}$, 1 lít nước có thể hòa tan tới 700 lít khí $NH_3$); ngược lại khí $N_2$ rất ít tan trong nước (1 lít nước ở $20^o\\text{C}$ chỉ hòa tan khoảng 0,015 lít $N_2$).<br>"
                               "2. <strong>Giải thích:</strong><br>"
                               "- Phân tử $NH_3$ có cấu trúc chóp tam giác bất đối xứng, phân cực mạnh, và đặc biệt nguyên tử H linh động liên kết với N có độ âm điện lớn tạo được liên kết hydrogen liên phân tử bền vững với các phân tử nước ($H_2O \\cdots H-NH_2$).<br>"
                               "- Phân tử $N_2$ là phân tử không phân cực, không có khả năng tạo liên kết hydrogen với nước nên độ tan trong nước không đáng kể."
            },
            {
                "num": 37,
                "title": "Nêu điều kiện phản ứng tổng hợp NH3 trong công nghiệp (nhiệt độ, áp suất, xúc tác) và giải thích cơ sở khoa học.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "Phản ứng: $N_2(g) + 3H_2(g) \\rightleftharpoons 2NH_3(g) \\quad \\Delta_r H_{298}^o = -92\\text{ kJ}$.<br>"
                               "1. <strong>Áp suất cao ($150 - 200\\text{ bar}$):</strong> Phản ứng thuận làm giảm số mol khí ($4\\text{ mol} \\rightarrow 2\\text{ mol}$). Tăng áp suất sẽ làm cân bằng chuyển dịch mạnh sang chiều thuận tạo nhiều $NH_3$.<br>"
                               "2. <strong>Nhiệt độ tối ưu ($400 - 450^o\\text{C}$):</strong> Phản ứng tỏa nhiệt nên nhiệt độ thấp thuận lợi về mặt cân bằng. Tuy nhiên, ở nhiệt độ thấp tốc độ phản ứng quá chậm và xúc tác chưa hoạt động. Nhiệt độ $400 - 450^o\\text{C}$ là thỏa hiệp để tốc độ phản ứng đủ nhanh mà hiệu suất chuyển hóa vẫn đạt khoảng 15 - 20% mỗi chu trình.<br>"
                               "3. <strong>Xúc tác bột sắt ($Fe$) hoạt hóa bằng $Al_2O_3, K_2O$:</strong> Giúp hạ thấp năng lượng hoạt hóa, bẻ gãy liên kết ba $N \\equiv N$ bền vững để tăng tốc độ phản ứng."
            },
            {
                "num": 38,
                "title": "Trình bày quy tắc an toàn thực hành khi thao tác với các hóa chất và dụng cụ thí nghiệm của bài.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>An toàn với khí độc ($NH_3, NO_2, SO_2$):</strong> Tất cả các thí nghiệm sinh ra khí độc phải được thực hiện trong tủ hút khí độc hoặc ống nghiệm có nút đậy kín kèm bông tẩm dung dịch $NaOH$ loãng để hấp thụ toàn bộ khí độc dư, tuyệt đối không hít trực tiếp.<br>"
                               "2. <strong>An toàn với acid $HNO_3$ đặc và $H_2SO_4$ đặc:</strong> Cả hai đều là những acid có tính oxi hóa và ăn mòn da cực kì nguy hiểm, làm than hóa vải, giấy và gây bỏng sâu. Luôn mang kính bảo hộ, găng tay cao su; không đổ nước vào acid đặc khi pha loãng.<br>"
                               "3. <strong>Xử lí sự cố:</strong> Nếu bị dây acid vào tay, phải ngâm xả ngay dưới vòi nước sạch nhiều lần, sau đó rửa bằng dung dịch $NaHCO_3$ loãng 2%. Các phế phẩm kim loại sau phản ứng phải gom vào bình chứa kim loại nặng, không xả ra bồn rửa."
            },
            {
                "num": 39,
                "title": "Giải thích vì sao kim loại nhôm (Al), sắt (Fe) và chromium (Cr) bị thụ động hóa trong HNO3 đặc nguội và H2SO4 đặc nguội.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Bản chất của hiện tượng thụ động hóa:</strong> Khi cho các kim loại $Al, Fe, Cr$ vào dung dịch $HNO_3$ đặc nguội hoặc $H_2SO_4$ đặc nguội, trên bề mặt kim loại bị oxi hóa chớp nhoáng tạo ra một màng oxide kim loại ($Al_2O_3, Fe_3O_4, Cr_2O_3$) cực kì mỏng, mịn, đặc khít và bền vững về mặt hóa học.<br>"
                               "2. <strong>Hậu quả:</strong> Lớp màng oxide này ngăn cách hoàn toàn kim loại bên trong với dung dịch acid, làm phản ứng lập tức ngừng lại.<br>"
                               "3. <strong>Ý nghĩa thực tiễn:</strong> Nhờ hiện tượng thụ động hóa này, người ta có thể sử dụng các bồn chứa bằng sắt hoặc nhôm để chuyên chở và lưu trữ acid $HNO_3$ đặc nguội và $H_2SO_4$ đặc nguội trong công nghiệp một cách an toàn và tiết kiệm."
            },
            {
                "num": 40,
                "title": "Nêu các ứng dụng thực tế quan trọng của nitric acid (HNO3) và sulfuric acid (H2SO4) trong công nghiệp và nông nghiệp.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Ứng dụng của HNO3:</strong><br>"
                               "- Sản xuất phân bón vô cơ chứa đạm: Muối ammonium nitrate ($NH_4NO_3$), calcium nitrate ($Ca(NO_3)_2$).<br>"
                               "- Sản xuất thuốc nổ công nghiệp và quốc phòng: Thuốc nổ TNT (trinitrotoluene), nitroglycerin, bông thuốc súng (nitrocellulose).<br>"
                               "- Dùng trong công nghệ mạ điện, khắc chữ trên kim loại và tinh chế vàng, bạc.<br>"
                               "2. <strong>Ứng dụng của H2SO4 (được mệnh danh là máu của ngành hóa chất):</strong><br>"
                               "- Sản xuất phân bón supephosphate đơn, kép và ammonium sulfate ($((NH_4)_2SO_4$).<br>"
                               "- Dùng trong chế biến quặng kim loại, sản xuất chất tẩy rửa, thuốc nhuộm, giấy, sợi nhân tạo, và dung dịch điện giải trong acquy chì."
            },
            {
                "num": 41,
                "title": "Trình bày phương pháp hóa học phân biệt 3 dung dịch muối mất nhãn: NH4Cl, Na2SO4, NaNO3.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Thuốc thử:</strong> Dung dịch $Ba(OH)_2$ và đun nóng nhẹ.<br>"
                               "2. <strong>Tiến hành:</strong> Trích mẫu thử vào 3 ống nghiệm, nhỏ dung dịch $Ba(OH)_2$ vào từng mẫu rồi đun nhẹ:<br>"
                               "- <em>Mẫu thử có khí mùi khai bay ra, làm xanh giấy quỳ tím ẩm:</em> Là muối $NH_4Cl$.<br>"
                               "$$2NH_4Cl + Ba(OH)_2 \\xrightarrow{t^o} BaCl_2 + 2NH_3\\uparrow + 2H_2O$$<br>"
                               "- <em>Mẫu thử xuất hiện kết tủa trắng, không có khí bay ra:</em> Là muối $Na_2SO_4$.<br>"
                               "$$Na_2SO_4 + Ba(OH)_2 \\rightarrow BaSO_4\\downarrow (\\text{trắng}) + 2NaOH$$<br>"
                               "- <em>Mẫu thử không có hiện tượng gì (không kết tủa, không có khí):</em> Là muối $NaNO_3$."
            },
            {
                "num": 42,
                "title": "Hòa tan hoàn toàn 6,4 gam Cu bằng lượng dư dung dịch HNO3 loãng thu được V lít khí NO (sản phẩm khử duy nhất, ở đktc). Tính V và khối lượng muối Cu(NO3)2 tạo thành.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Số mol Cu:</strong> $n_{Cu} = \\frac{6,4}{64} = 0,1\\text{ mol}$.<br>"
                               "2. <strong>Phương trình hóa học và bảo toàn electron:</strong><br>"
                               "$$3Cu + 8HNO_3 \\rightarrow 3Cu(NO_3)_2 + 2NO\\uparrow + 4H_2O$$<br>"
                               "- Quá trình oxi hóa: $Cu^0 \\rightarrow Cu^{+2} + 2e \\Rightarrow n_e \\text{ nhường} = 0,1 \\times 2 = 0,2\\text{ mol}$.<br>"
                               "- Quá trình khử: $N^{+5} + 3e \\rightarrow N^{+2} (NO) \\Rightarrow n_{NO} = \\frac{0,2}{3} = \\frac{2}{30} \\approx 0,0667\\text{ mol}$.<br>"
                               "3. <strong>Tính thể tích khí NO:</strong><br>"
                               "$$V_{NO} = \\frac{2}{30} \\times 22,4 \\approx 1,493\\text{ lít (hoặc 1,65 lít ở điều kiện chuẩn 25°C, 1 bar)}.$$<br>"
                               "4. <strong>Khối lượng muối Cu(NO3)2 tạo thành:</strong><br>"
                               "$n_{Cu(NO_3)_2} = n_{Cu} = 0,1\\text{ mol} \\Rightarrow m_{Cu(NO_3)_2} = 0,1 \\times 188 = 18,8\\text{ gam}$."
            },
            {
                "num": 43,
                "title": "Trong công nghiệp sản xuất H2SO4 từ quặng pyrite (FeS2), đốt 12 tấn FeS2 (chứa 80% FeS2 nguyên chất) với hiệu suất toàn bộ quy trình đạt 85%. Tính khối lượng H2SO4 sản xuất được.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Khối lượng FeS2 nguyên chất:</strong><br>"
                               "$$m_{FeS_2} = 12 \\times 80\\% = 9,6\\text{ tấn} = 9600\\text{ kg}$$<br>"
                               "Số mol $FeS_2$: $n_{FeS_2} = \\frac{9600}{120} = 80\\text{ kmol}$.<br>"
                               "2. <strong>Sơ đồ bảo toàn nguyên tố Sulfur (S):</strong><br>"
                               "$$FeS_2 \\xrightarrow{+O_2} 2SO_2 \\xrightarrow{+O_2} 2SO_3 \\xrightarrow{+H_2O} 2H_2SO_4$$<br>"
                               "Cứ 1 mol $FeS_2$ tạo ra tối đa 2 mol $H_2SO_4$.<br>"
                               "$\\Rightarrow n_{H_2SO_4\\text{ (lí thuyết)}} = 80 \\times 2 = 160\\text{ kmol}$.<br>"
                               "3. <strong>Khối lượng H2SO4 thực tế với hiệu suất 85%:</strong><br>"
                               "$$m_{H_2SO_4} = 160 \\times 98 \\times 85\\% = 13328\\text{ kg} = 13,328\\text{ tấn}.$$"
            },
            {
                "num": 44,
                "title": "Phân tích nguyên nhân hình thành mưa acid do khí SO2 và NOx, tác hại của mưa acid và các biện pháp giảm thiểu.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Nguyên nhân hình thành:</strong> Khí $SO_2$ và các oxit nitơ ($NO_x$) thải ra từ khói các nhà máy nhiệt điện đốt than, nhà máy hóa chất và động cơ đốt trong của phương tiện giao thông. Trong khí quyển, dưới tác dụng của oxygen, hơi nước và xúc tác bụi kim loại, chúng chuyển hóa thành acid sulfuric và acid nitric:<br>"
                               "$$2SO_2 + O_2 + 2H_2O \\rightarrow 2H_2SO_4$$<br>"
                               "$$4NO_2 + O_2 + 2H_2O \\rightarrow 4HNO_3$$<br>"
                               "Khi các giọt acid này hòa tan vào nước mưa làm nước mưa có pH < 5,6 gọi là mưa acid.<br>"
                               "2. <strong>Tác hại:</strong> Ăn mòn các công trình xây dựng bằng đá vôi, phá hủy cầu đường, làm chua hóa đất canh tác, hủy hoại rừng cây và làm chết các sinh vật trong sông hồ.<br>"
                               "3. <strong>Biện pháp giảm thiểu:</strong> Xử lí khí thải trước khi xả ra ống khói bằng phương pháp hấp phụ vôi sữa ($Ca(OH)_2$); sử dụng năng lượng tái tạo sạch (gió, mặt trời) thay cho nhiên liệu hóa thạch; lắp bộ xúc tác chuyển hóa trên ống xả ô tô, xe máy."
            },
            {
                "num": 45,
                "title": "Viết phương trình hóa học biểu diễn 3 giai đoạn của quá trình sản xuất acid sulfuric trong công nghiệp từ quặng pyrite sắt.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Giai đoạn 1: Sản xuất khí sulfur dioxide (SO2):</strong> Đốt quặng pyrite trong lò đốt với không khí:<br>"
                               "$$4FeS_2 + 11O_2 \\xrightarrow{t^o} 2Fe_2O_3 + 8SO_2$$<br>"
                               "2. <strong>Giai đoạn 2: Oxi hóa SO2 thành SO3:</strong> Dùng chất xúc tác vanadium(V) oxide ($V_2O_5$) ở nhiệt độ khoảng $450^o\\text{C}$:<br>"
                               "$$2SO_2 + O_2 \\xrightleftharpoons[V_2O_5]{450^o\\text{C}} 2SO_3 \\quad \\Delta_r H < 0$$<br>"
                               "3. <strong>Giai đoạn 3: Hấp thụ SO3 tạo oleum và acid sulfuric:</strong> Cho $H_2SO_4$ đặc 98% hấp thụ $SO_3$ tạo oleum ($H_2SO_4 \\cdot nSO_3$), sau đó pha loãng oleum bằng nước để thu được dung dịch $H_2SO_4$ đậm đặc:<br>"
                               "$$H_2SO_4 + nSO_3 \\rightarrow H_2SO_4 \\cdot nSO_3; \\quad H_2SO_4 \\cdot nSO_3 + nH_2O \\rightarrow (n+1)H_2SO_4$$"
            },
            {
                "num": 46,
                "title": "Giải thích vì sao trong giai đoạn sản xuất SO3, người ta dùng acid sulfuric đặc 98% để hấp thụ SO3 mà không dùng nước cất trực tiếp.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Nếu dùng nước trực tiếp để hấp thụ SO3:</strong> Phản ứng giữa $SO_3$ và nước tỏa ra lượng nhiệt cực kì lớn:<br>"
                               "$$SO_3(g) + H_2O(l) \\rightarrow H_2SO_4(l) \\quad \\Delta H \\ll 0$$<br>"
                               "Lượng nhiệt tỏa ra quá nhanh làm nước sôi ngay lập tức và biến toàn bộ hỗn hợp acid thành một làn sương mù acid sulfuric ($H_2SO_4$ dạng aerosol) cực kì mịn và bền vững.<br>"
                               "2. <strong>Hậu quả:</strong> Sương mù acid này không ngưng tụ được, bay theo luồng khí thoát ra ngoài khí quyển gây ăn mòn máy móc đường ống, thất thoát hóa chất nghiêm trọng và gây ngộ độc môi trường nặng nề.<br>"
                               "3. <strong>Giải pháp dùng H2SO4 đặc 98%:</strong> $H_2SO_4$ đặc hấp thụ $SO_3$ tạo thành oleum không tỏa nhiệt quá sôi, hấp thụ triệt để và an toàn tuyệt đối."
            },
            {
                "num": 47,
                "title": "Cần thêm bao nhiêu mL nước cất vào 200 mL dung dịch HNO3 2 M để thu được dung dịch HNO3 có nồng độ 0,5 M?",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Số mol HNO3 ban đầu:</strong><br>"
                               "$$n_{HNO_3} = C_{M1} \\times V_1 = 2 \\times 0,2 = 0,4\\text{ mol}$$<br>"
                               "2. <strong>Thể tích dung dịch sau khi pha loãng:</strong> Khi thêm nước cất, số mol $HNO_3$ không thay đổi:<br>"
                               "$$V_2 = \\frac{n_{HNO_3}}{C_{M2}} = \\frac{0,4}{0,5} = 0,8\\text{ lít} = 800\\text{ mL}$$<br>"
                               "3. <strong>Thể tích nước cất cần thêm vào:</strong><br>"
                               "$$V_{H_2O} = V_2 - V_1 = 800 - 200 = 600\\text{ mL}.$$"
            },
            {
                "num": 48,
                "title": f"Tổng kết những bài học kinh nghiệm và kiến thức cốt lõi cần ghi nhớ khi giải bài tập về {lesson_name}.",
                "explanation": "<strong>Lời giải chi tiết:</strong><br>"
                               "1. <strong>Số oxi hóa của N và S:</strong> Nắm vững tính oxi hóa mạnh của $HNO_3$ và $H_2SO_4$ đặc nóng (tác dụng hầu hết kim loại trừ Au, Pt, không giải phóng $H_2$). Sản phẩm khử phụ thuộc nồng độ acid và tính khử của kim loại.<br>"
                               "2. <strong>Phương pháp bảo toàn electron:</strong> Khi giải bài toán kim loại tác dụng với $HNO_3$ hoặc $H_2SO_4$ đặc, luôn áp dụng định luật bảo toàn e: $\\sum n_e \\text{ nhường} = \\sum n_e \\text{ nhận}$ để tính nhanh mà không cần cân bằng phương trình phân tử phức tạp.<br>"
                               "3. <strong>Nhận biết ion:</strong> Nhận biết $SO_4^{2-}$ bằng muối $Ba^{2+}$ tạo kết tủa trắng $BaSO_4$ không tan trong acid mạnh; nhận biết ion $NH_4^+$ bằng dung dịch kiềm có đun nóng nhẹ làm sủi bọt khí $NH_3$ mùi khai làm xanh quỳ ẩm."
            }
        ]

    # For Hydrocarbons (c4), Oxygen derivatives (c5, c6), Grade 10, Grade 12:
    else:
        return [
            {
                "num": 32,
                "title": f"Trình bày định nghĩa, đồng đẳng, đồng phân và danh pháp IUPAC liên quan trực tiếp đến {lesson_name}.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    f"1. <strong>Định nghĩa và dãy đồng đẳng:</strong> Chủ đề {lesson_name} thuộc chương trình Hóa học Kết nối tri thức. Các chất trong cùng dãy đồng đẳng có thành phần phân tử hơn kém nhau một hay nhiều nhóm $-CH_2-$, nhưng có cấu tạo hóa học tương tự nhau nên có tính chất hóa học tương tự nhau.<br>"
                    "2. <strong>Đồng phân:</strong> Bao gồm đồng phân cấu tạo (đồng phân mạch carbon, đồng phân vị trí liên kết bội hoặc nhóm chức) và đồng phân hình học (cis - trans) khi có liên kết đôi $C=C$ với các nhóm thế khác nhau ở mỗi carbon mang nối đôi.<br>"
                    "3. <strong>Danh pháp IUPAC:</strong> Chọn mạch chính là mạch dài nhất, chứa nhiều nhóm chức hoặc liên kết bội nhất; đánh số từ đầu gần nhóm chức/liên kết bội hơn; gọi tên: [Vị trí nhánh + Tên nhánh] + [Tên mạch chính] + [Vị trí nhóm chức/nối đôi + Đuôi đặc trưng]."
                )
            },
            {
                "num": 33,
                "title": f"Nêu đặc điểm cấu tạo phân tử, các loại liên kết hóa học chủ yếu và dạng hình học của các chất trong {lesson_name}.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Liên kết hóa học:</strong> Chủ yếu là các liên kết cộng hóa trị ($\\sigma$ và $\\pi$). Liên kết $\\sigma$ tạo nên khung sườn mạch carbon bền vững, trong khi liên kết $\\pi$ kém bền hơn, tập trung mật độ electron cao dễ bị tác nhân phân cực hoặc electronfile tấn công.<br>"
                    "2. <strong>Trạng thái lai hóa của carbon:</strong> Lai hóa $sp^3$ (cấu trúc tứ diện, góc liên kết $109,5^o$), lai hóa $sp^2$ (cấu trúc tam giác phẳng, góc liên kết $120^o$) và lai hóa $sp$ (cấu trúc thẳng hàng, góc liên kết $180^o$).<br>"
                    "3. <strong>Ảnh hưởng nhóm chức:</strong> Nhóm phân cực làm tăng tính tan trong nước và tạo ra các tâm phản ứng đặc trưng cho phân tử."
                )
            },
            {
                "num": 34,
                "title": f"Viết 2 phương trình hóa học minh họa cho tính chất hóa học đặc trưng nhất của {lesson_name}.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Phản ứng 1 (Phản ứng thế hoặc cộng đặc trưng):</strong><br>"
                    "$$CH_2=CH_2 + Br_2 \\rightarrow CH_2Br-CH_2Br \\text{ (làm mất màu nước bromine)}$$<br>"
                    "2. <strong>Phản ứng 2 (Phản ứng oxi hóa hoàn toàn tạo năng lượng):</strong><br>"
                    "$$C_2H_5OH + 3O_2 \\xrightarrow{t^o} 2CO_2 + 3H_2O \\quad \\Delta_r H < 0$$"
                )
            },
            {
                "num": 35,
                "title": f"Giải thích hiện tượng quan sát được trong thí nghiệm minh họa thực tế của {lesson_name}.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Hiện tượng quan sát:</strong> Dung dịch thuốc thử ban đầu có màu đặc trưng (như màu vàng cam của dung dịch $Br_2$ hoặc màu tím của dung dịch $KMnO_4$), khi sục chất thử vào thì màu sắc nhạt dần rồi mất màu hoàn toàn, đồng thời có thể xuất hiện kết tủa hoặc tách lớp chất lỏng.<br>"
                    "2. <strong>Giải thích bản chất:</strong> Phân tử có liên kết bội hoặc nhóm chức hoạt động đã tham gia phản ứng cộng hoặc oxi hóa khử với thuốc thử, chuyển hóa thành hợp chất no hoặc dẫn xuất không màu làm mất màu dung dịch."
                )
            },
            {
                "num": 36,
                "title": f"So sánh tính chất vật lí (nhiệt độ sôi, nhiệt độ nóng chảy, độ tan trong nước) của các hợp chất trong {lesson_name}.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Nhiệt độ sôi:</strong> Tăng dần theo chiều tăng của phân tử khối do lực hút Van der Waals tăng. Các hợp chất có nhóm phân cực (như $-OH, -COOH$) có nhiệt độ sôi cao hơn hẳn hydrocarbon có cùng số C do tạo được liên kết hydrogen liên phân tử bền vững.<br>"
                    "2. <strong>Độ tan:</strong> Các chất có khối lượng phân tử nhỏ và có nhóm tạo liên kết hydrogen với nước (như alcohol đầu dãy, carboxylic acid) tan vô hạn trong nước; khi mạch carbon kéo dài (phần kị nước tăng), độ tan trong nước giảm nhanh chóng."
                )
            },
            {
                "num": 37,
                "title": f"Nêu vai trò và ảnh hưởng của các điều kiện phản ứng (nhiệt độ, áp suất, chất xúc tác) đối với {lesson_name}.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Nhiệt độ:</strong> Cung cấp năng lượng vượt qua hàng rào năng lượng hoạt hóa, làm tăng tần số va chạm hiệu quả giữa các phân tử tham gia phản ứng.<br>"
                    "2. <strong>Chất xúc tác:</strong> Làm giảm năng lượng hoạt hóa mà không bị biến đổi sau phản ứng, định hướng phản ứng xảy ra theo con đường chọn lọc tạo sản phẩm mong muốn.<br>"
                    "3. <strong>Áp suất:</strong> Ảnh hưởng đến các phản ứng trong pha khí, giúp tăng nồng độ thể tích của các chất khí tham gia."
                )
            },
            {
                "num": 38,
                "title": "Trình bày quy tắc an toàn thực hành khi thao tác với các hóa chất và dụng cụ thí nghiệm của bài.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Phòng chống cháy nổ:</strong> Các dung môi hữu cơ và hợp chất dễ cháy (xăng, cồn, ether, ester) tuyệt đối không được đun trực tiếp trên ngọn lửa trần của đèn cồn; bắt buộc dùng nồi cách thủy hoặc bếp điện kín.<br>"
                    "2. <strong>Thao tác với hóa chất độc và bay hơi:</strong> Tiến hành trong tủ hút khí độc hoặc phòng thực hành thông gió; không dùng tay tiếp xúc trực tiếp hoặc ngửi miệng lọ hóa chất.<br>"
                    "3. <strong>Thu gom chất thải:</strong> Gom dung môi hữu cơ thừa vào can chứa chất thải riêng biệt có nắp kín, không đổ vào bồn rửa làm tắc cống và ô nhiễm nguồn nước ngầm."
                )
            },
            {
                "num": 39,
                "title": f"Giải thích cơ chế hoặc quy luật biến đổi hóa học diễn ra trong các phản ứng trọng tâm của {lesson_name}.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Quy tắc Markovnikov:</strong> Trong phản ứng cộng tác nhân bất đối xứng ($HX$) vào alkene hoặc alkyne bất đối xứng, nguyên tử $H$ ưu tiên cộng vào nguyên tử carbon mang nhiều hydrogen hơn (carbon bậc thấp hơn), còn nhóm $X$ cộng vào carbon mang ít hydrogen hơn (carbon bậc cao hơn).<br>"
                    "2. <strong>Quy tắc Zaisev:</strong> Trong phản ứng tách $HX$ khỏi dẫn xuất halogen hoặc tách nước khỏi alcohol, nhóm $-OH$ hoặc nguyên tử halogen ưu tiên bị tách cùng với nguyên tử $H$ ở carbon bên cạnh có bậc cao hơn để tạo alkene có nhiều nhóm thế hơn (bền hơn)."
                )
            },
            {
                "num": 40,
                "title": f"Nêu các ứng dụng thực tiễn quan trọng của {lesson_name} trong đời sống, y học và sản xuất công nghiệp.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Trong công nghiệp hóa chất:</strong> Làm nguyên liệu tổng hợp polymer, chất dẻo, sợi tổng hợp, cao su nhân tạo, sơn và dung môi pha chế công nghiệp.<br>"
                    "2. <strong>Trong đời sống và năng lượng:</strong> Dùng làm nhiên liệu đun nấu ($LPG$), nhiên liệu động cơ đốt trong (xăng sinh học $E_5$), phụ gia thực phẩm và gia vị.<br>"
                    "3. <strong>Trong y tế và dược phẩm:</strong> Làm dung môi chiết xuất dược liệu, chất sát trùng, tổng hợp thuốc kháng sinh, thuốc giảm đau và các hợp chất có hoạt tính sinh học cao."
                )
            },
            {
                "num": 41,
                "title": f"Đề xuất phương pháp hóa học để nhận biết hoặc phân biệt các chất đặc trưng trong {lesson_name}.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Bước 1 (Chọn thuốc thử đặc trưng):</strong> Dùng thuốc thử có phản ứng chọn lọc tạo hiện tượng rõ nét (như nước bromine, dung dịch thuốc tím $KMnO_4$, dung dịch $AgNO_3/NH_3$, hoặc $Cu(OH)_2$).<br>"
                    "2. <strong>Bước 2 (Tiến hành thí nghiệm):</strong> Nhỏ thuốc thử vào từng ống nghiệm chứa các mẫu thử cần phân biệt, lắc đều và quan sát hiện tượng.<br>"
                    "3. <strong>Bước 3 (Nhận định kết quả):</strong> Mẫu làm mất màu nước bromine chứa liên kết không no $C=C$ hoặc $C\\equiv C$; mẫu tạo kết tủa vàng nhạt với $AgNO_3/NH_3$ là alkyne có liên kết ba đầu mạch (alk-1-yne); mẫu tạo phức màu xanh lam thẫm với $Cu(OH)_2$ là polyalcohol có các nhóm $-OH$ liền kề."
                )
            },
            {
                "num": 42,
                "title": f"Giải bài toán định lượng tính số mol và khối lượng các chất tham gia phản ứng trong {lesson_name}.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Tính số mol chất tham gia ban đầu:</strong> Áp dụng công thức $n = \\frac{m}{M}$ hoặc $n = C_M \\times V$ hoặc $n = \\frac{V}{22,4}$ (ở đktc) để đổi dữ kiện đầu bài ra số mol chính xác.<br>"
                    "2. <strong>Lập phương trình hóa học và xác định tỉ lệ mol:</strong> Viết phương trình phản ứng cân bằng hoàn chỉnh, so sánh tỉ lệ mol giữa các chất để xác định chất phản ứng hết và chất còn dư.<br>"
                    "3. <strong>Tính toán khối lượng theo định luật bảo toàn:</strong> Áp dụng định luật bảo toàn khối lượng ($m_{\\text{chất tham gia}} = m_{\\text{sản phẩm}}$) hoặc bảo toàn nguyên tố để tính ra khối lượng chất cần tìm với độ chính xác cao."
                )
            },
            {
                "num": 43,
                "title": f"Tính hiệu suất của phản ứng tổng hợp hoặc chuyển hóa liên quan đến {lesson_name} với số liệu cụ thể.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Công thức tính hiệu suất:</strong><br>"
                    "$$H\\% = \\frac{m_{\\text{thực tế}}}{m_{\\text{lí thuyết}}} \\times 100\\% \\quad \\text{hoặc} \\quad H\\% = \\frac{n_{\\text{phản ứng}}}{n_{\\text{ban đầu}}} \\times 100\\%$$<br>"
                    "2. <strong>Ví dụ cụ thể:</strong> Đun 4,6 gam ethanol ($C_2H_5OH$, $M=46$, tương ứng $0,1\\text{ mol}$) với $H_2SO_4$ đặc ở $170^o\\text{C}$ thu được 1,792 lít khí ethylene $C_2H_4$ ở đktc ($0,08\\text{ mol}$).<br>"
                    "Theo lí thuyết: $n_{C_2H_4\\text{ lí thuyết}} = n_{C_2H_5OH} = 0,1\\text{ mol}$.<br>"
                    "Hiệu suất phản ứng tách nước:<br>"
                    "$$H\\% = \\frac{0,08}{0,1} \\times 100\\% = 80\\%.$$"
                )
            },
            {
                "num": 44,
                "title": f"Phân tích tác động của các chất trong {lesson_name} đối với môi trường và các biện pháp bảo vệ môi trường theo hướng hóa học xanh.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Tác động tiêu cực:</strong> Khí thải từ quá trình đốt cháy hydrocarbon sinh ra $CO_2$ gây hiệu ứng nhà kính làm biến đổi khí hậu toàn cầu, muội than bụi mịn $PM_{2.5}$, cùng các chất thải nhựa polymer khó phân hủy tích tụ hàng trăm năm gây ô nhiễm trắng.<br>"
                    "2. <strong>Biện pháp theo nguyên tắc Hóa học Xanh:</strong><br>"
                    "- Tối ưu hóa hiệu suất nguyên tử, giảm thiểu phụ phẩm độc hại.<br>"
                    "- Sử dụng nguyên liệu tái tạo từ sinh khối (tinh bột, cellulose, cồn sinh học $E_5, E_{10}$) thay thế dần dầu mỏ.<br>"
                    "- Phát triển các vật liệu nhựa sinh học tự phân hủy thân thiện với môi trường ($PLA$); tăng cường phân loại và tái chế rác thải."
                )
            },
            {
                "num": 45,
                "title": f"Viết phương trình hóa học biểu diễn chuỗi biến hóa 3 giai đoạn liên quan đến các hợp chất của {lesson_name}.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "Chuỗi biến hóa tiêu biểu 3 giai đoạn: $CH_4 \\rightarrow C_2H_2 \\rightarrow C_2H_4 \\rightarrow C_2H_5OH$:<br>"
                    "1. <strong>Giai đoạn 1:</strong> Nhiệt phân nhanh methane ở $1500^o\\text{C}$ rồi làm lạnh nhanh:<br>"
                    "$$2CH_4 \\xrightarrow{1500^o\\text{C}, \\text{ làm lạnh nhanh}} C_2H_2 + 3H_2$$<br>"
                    "2. <strong>Giai đoạn 2:</strong> Hydro hóa acetylene có xúc tác $Pd/PbCO_3$ để dừng ở liên kết đôi:<br>"
                    "$$C_2H_2 + H_2 \\xrightarrow{t^o, Pd/PbCO_3} C_2H_4$$<br>"
                    "3. <strong>Giai đoạn 3:</strong> Hydrat hóa ethylene với xúc tác acid $H_3PO_4$ đun nóng:<br>"
                    "$$C_2H_4 + H_2O \\xrightarrow{t^o, H^+} C_2H_5OH$$"
                )
            },
            {
                "num": 46,
                "title": f"Giải thích vì sao một số phản ứng hóa học trong {lesson_name} cần phải đun nóng hoặc cần có mặt chất xúc tác mới diễn ra.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Độ bền liên kết hóa học:</strong> Các liên kết cộng hóa trị ($\\sigma_{C-C}, \\sigma_{C-H}$) có năng lượng liên kết lớn, các phân tử hữu cơ trơ ở điều kiện thường vì năng lượng hoạt hóa của phản ứng cao.<br>"
                    "2. <strong>Vai trò nhiệt độ:</strong> Cung cấp nhiệt năng làm tăng động năng phân tử, giúp các va chạm giữa các phân tử chất phản ứng có đủ năng lượng vượt qua đỉnh thế năng hoạt hóa.<br>"
                    "3. <strong>Vai trò chất xúc tác:</strong> Tham gia tạo hợp chất trung gian kém bền, mở ra một đường đi phản ứng mới có năng lượng hoạt hóa thấp hơn đáng kể, làm tăng tốc độ phản ứng hàng triệu lần mà không làm thay đổi vị trí cân bằng."
                )
            },
            {
                "num": 47,
                "title": f"Tính toán nồng độ phần trăm hoặc nồng độ mol của dung dịch thu được sau khi phản ứng kết thúc.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Phương pháp giải:</strong><br>"
                    "- Tính khối lượng dung dịch sau phản ứng bằng định luật bảo toàn khối lượng:<br>"
                    "$$m_{dd\\text{ sau}} = m_{\\text{chất tan thêm vào}} + m_{dd\\text{ ban đầu}} - m_{\\text{kết tủa}} - m_{\\text{khí thoát ra}}$$<br>"
                    "- Tính nồng độ phần trăm: $C\\% = \\frac{m_{\\text{chất tan}}}{m_{dd\\text{ sau}}} \\times 100\\%$.<br>"
                    "- Tính nồng độ mol: $C_M = \\frac{n_{\\text{chất tan}}}{V_{dd\\text{ sau}}}$ (với $V_{dd} = \\frac{m_{dd}}{D}$).<br>"
                    "2. <strong>Ví dụ:</strong> Hòa tan 2,3 gam Na ($0,1\\text{ mol}$) vào 97,8 gam nước cất:<br>"
                    "$$Na + H_2O \\rightarrow NaOH + \\frac{1}{2}H_2\\uparrow$$<br>"
                    "$n_{H_2} = 0,05\\text{ mol} \\Rightarrow m_{H_2} = 0,1\\text{ gam}; \\quad n_{NaOH} = 0,1\\text{ mol} \\Rightarrow m_{NaOH} = 4,0\\text{ gam}$.<br>"
                    "$m_{dd\\text{ sau}} = 2,3 + 97,8 - 0,1 = 100,0\\text{ gam}$.<br>"
                    "$$C\\%(NaOH) = \\frac{4,0}{100,0} \\times 100\\% = 4,0\\%.$$"
                )
            },
            {
                "num": 48,
                "title": f"Tổng kết những bài học kinh nghiệm và kiến thức cốt lõi cần ghi nhớ để chuẩn bị cho các kì thi về {lesson_name}.",
                "explanation": (
                    "<strong>Lời giải chi tiết:</strong><br>"
                    "1. <strong>Ghi nhớ công thức tổng quát và tính chất đặc trưng:</strong> Nắm vững công thức chung dãy đồng đẳng, hóa trị, nhóm chức và các phản ứng đặc trưng riêng biệt (phản ứng tráng bạc của aldehyde, phản ứng tách nước tạo ether hoặc alkene của alcohol, phản ứng cộng $Br_2$ của hợp chất không no).<br>"
                    "2. <strong>Kĩ năng giải toán trắc nghiệm:</strong> Áp dụng linh hoạt các định luật bảo toàn (bảo toàn khối lượng, bảo toàn nguyên tố C, H, O, bảo toàn electron, tăng giảm khối lượng) để tìm nhanh công thức phân tử mà không phải đặt quá nhiều ẩn số.<br>"
                    "3. <strong>Tránh bẫy đề thi:</strong> Đọc kĩ đề về điều kiện phản ứng (nhiệt độ, chất xúc tác, tỉ lệ mol 1:1 hay 1:2); phân biệt rõ giữa đồng phân cấu tạo và đồng phân hình học khi đếm số lượng đồng phân."
                )
            }
        ]

print("all_concrete_essay_bank loaded successfully.")
