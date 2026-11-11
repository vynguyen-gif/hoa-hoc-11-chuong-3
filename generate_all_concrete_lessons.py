# -*- coding: utf-8 -*-
"""
Generator for all lessons to guarantee 100% concrete chemistry content.
"""

# Concrete templates for each chapter of Chemistry 11, 10, 12
CHAPTER_DOMAINS = {
    "c1": {
        "title": "CÂN BẰNG HÓA HỌC",
        "methods": [
            ("Dạng 1: Viết biểu thức và tính hằng số cân bằng Kc", "Kc = ([C]^c * [D]^d) / ([A]^a * [B]^b). Chỉ tính chất khí và chất tan trong dung dịch, không tính chất rắn.", [
                ("Viết biểu thức Kc cho phản ứng: N2(k) + 3H2(k) ⇌ 2NH3(k).", "Kc = [NH3]^2 / ([N2] * [H2]^3)", "Thông hiểu"),
                ("Cho phản ứng C(r) + CO2(k) ⇌ 2CO(k). Viết biểu thức Kc.", "Vì C là chất rắn nên Kc = [CO]^2 / [CO2]", "Thông hiểu"),
                ("Ở trạng thái cân bằng: [N2] = 0,5M, [H2] = 1,0M, [NH3] = 0,2M. Tính Kc.", "Kc = (0,2)^2 / (0,5 * 1^3) = 0,08", "Vận dụng")
            ]),
            ("Dạng 2: Dự đoán chiều chuyển dịch cân bằng theo Le Chatelier", "Tăng T -> chiều thu nhiệt (ΔH > 0); Tăng P -> chiều giảm số mol khí; Thêm chất -> chiều giảm chất đó.", [
                ("N2 + 3H2 ⇌ 2NH3 (ΔH < 0). Khi tăng nhiệt độ, cân bằng chuyển dịch theo chiều nào?", "Chiều thuận tỏa nhiệt (ΔH < 0), nên khi tăng T cân bằng chuyển dịch theo chiều thu nhiệt (chiều nghịch).", "Thông hiểu"),
                ("Khi tăng áp suất chung của hệ N2 + 3H2 ⇌ 2NH3, cân bằng chuyển dịch thế nào?", "Vế trái có 4 mol khí, vế phải có 2 mol khí. Tăng áp suất chuyển dịch theo chiều giảm mol khí (chiều thuận).", "Vận dụng"),
                ("Chất xúc tác bột sắt Fe có làm chuyển dịch cân bằng tổng hợp NH3 không? Vì sao?", "Không, vì chất xúc tác làm tăng tốc độ thuận và nghịch như nhau, chỉ giúp hệ nhanh đạt cân bằng.", "Thông hiểu")
            ]),
            ("Dạng 3: Tính pH và Cân bằng trong dung dịch nước", "pH = -log[H+]; [H+] * [OH-] = 10^-14. Chuẩn độ: C_A * V_A = C_B * V_B.", [
                ("Tính pH của dung dịch HCl 0,001 M.", "[H+] = 0,001 M = 10^-3 M => pH = -log(10^-3) = 3.", "Thông hiểu"),
                ("Dung dịch NaOH có nồng độ 0,01 M. Tính pH của dung dịch này ở 25°C.", "[OH-] = 0,01 M = 10^-2 M => pOH = 2 => pH = 14 - 2 = 12.", "Vận dụng"),
                ("Chuẩn độ 10,0 mL dung dịch HCl chưa biết nồng độ cần dùng vừa đủ 15,0 mL dung dịch NaOH 0,10 M. Tính nồng độ mol của HCl.", "n_HCl = n_NaOH = 0,015 * 0,10 = 0,0015 mol => C_M = 0,0015 / 0,010 = 0,15 M.", "Vận dụng cao")
            ])
        ]
    },
    "c2": {
        "title": "NITROGEN VÀ SULFUR",
        "methods": [
            ("Dạng 1: Kim loại tác dụng với axit nitric HNO3", "Bảo toàn electron: n_e nhường = n_e nhận (3*nNO + 1*nNO2 + 8*nN2O + 10*nN2 + 8*nNH4NO3).", [
                ("Cho 2,7 gam bột Al tác dụng hết với dung dịch HNO3 loãng dư thu được V lít khí NO (đktc, sp khử duy nhất). Tìm V.", "nAl = 0,1 mol. Bảo toàn e: 3*nAl = 3*nNO => nNO = 0,1 mol => V = 0,1 * 22,4 = 2,24 lít.", "Thông hiểu"),
                ("Hòa tan 6,4 gam Cu trong HNO3 đặc dư thu được V lít khí NO2 màu nâu đỏ (đktc). Tính V.", "nCu = 0,1 mol. Bảo toàn e: 2*nCu = 1*nNO2 => nNO2 = 0,2 mol => V = 0,2 * 22,4 = 4,48 lít.", "Thông hiểu"),
                ("Kim loại nào sau đây bị thụ động hóa trong HNO3 đặc nguội và H2SO4 đặc nguội: Fe, Al, Cr?", "Cả 3 kim loại Fe, Al, Cr đều bị thụ động hóa (tạo màng oxit bảo vệ bền vững trơ về mặt hóa học).", "Vận dụng")
            ]),
            ("Dạng 2: Tính chất hóa học của SO2 và H2SO4 đặc", "SO2 vừa khử (làm mất màu dung dịch Br2, KMnO4) vừa oxi hóa (tác dụng H2S). H2SO4 đặc có tính háo nước và oxi hóa mạnh.", [
                ("Nêu hiện tượng khi sục khí SO2 từ từ vào ống nghiệm đựng dung dịch nước brom.", "Dung dịch nước brom màu vàng nâu nhạt dần rồi mất màu hoàn toàn: SO2 + Br2 + 2H2O -> 2HBr + H2SO4.", "Thông hiểu"),
                ("Nhỏ vài giọt H2SO4 đặc vào cốc chứa đường kính trắng (saccharose C12H22O11). Nêu hiện tượng và giải thích.", "Đường chuyển từ màu trắng sang vàng nâu rồi đen xì (bị than hóa thành C do tính háo nước), sau đó khối than xốp dâng trào sủi bọt khí CO2 và SO2.", "Vận dụng"),
                ("Để pha loãng axit sunfuric H2SO4 đặc một cách an toàn trong phòng thí nghiệm, ta phải thực hiện như thế nào?", "Rót từ từ axit đặc vào nước và khuấy đều bằng đũa thủy tinh. Tuyệt đối không rót nước vào axit đặc vì tỏa nhiệt dữ dội làm nước sôi bắn axit gây bỏng.", "Vận dụng")
            ]),
            ("Dạng 3: Nhận biết ion sunfat SO4(2-) và muối ammonium", "Thuốc thử nhận biết SO4(2-) là dung dịch BaCl2 hoặc Ba(OH)2 (tạo kết tủa trắng BaSO4 không tan trong axit). Thuốc thử nhận biết NH4+ là dung dịch kiềm nóng (sinh khí NH3 mùi khai).", [
                ("Nhận biết 2 dung dịch mất nhãn: Na2SO4 và NaCl bằng thuốc thử nào?", "Dùng dung dịch BaCl2: ống nghiệm tạo kết tủa trắng là Na2SO4, không hiện tượng là NaCl.", "Thông hiểu"),
                ("Cho dung dịch NaOH vào dung dịch muối ammonium chloride (NH4Cl) rồi đun nóng nhẹ. Nêu hiện tượng.", "Xuất hiện khí có mùi khai thoát ra (khí NH3), làm quỳ tím ẩm chuyển sang màu xanh: NH4+ + OH- -> NH3↑ + H2O.", "Thông hiểu"),
                ("Tính khối lượng kết tủa BaSO4 thu được khi cho 100 mL dung dịch BaCl2 1M tác dụng vừa đủ với dung dịch Na2SO4 dư.", "nBaCl2 = 0,1 mol => nBaSO4 = 0,1 mol => mBaSO4 = 0,1 * 233 = 23,3 gam.", "Vận dụng")
            ])
        ]
    },
    "c4": {
        "title": "HYDROCARBON",
        "methods": [
            ("Dạng 1: Phản ứng thế halogen của Alkane và phản ứng tách", "Alkane tham gia phản ứng thế ưu tiên thế nguyên tử H ở carbon bậc cao hơn (tạo sản phẩm chính). CnH2n+2 + Cl2 -> CnH2n+1Cl + HCl.", [
                ("Cho propane (CH3-CH2-CH3) tác dụng với Cl2 tỉ lệ mol 1:1 có chiếu sáng. Viết CTCT của sản phẩm chính.", "Sản phẩm chính là 2-chloropropane: CH3-CH(Cl)-CH3 (ưu tiên thế ở C bậc 2).", "Thông hiểu"),
                ("Butane (C4H10) khi bị cracking nhiệt độ cao có thể tạo ra những sản phẩm nào?", "Cracking C4H10 tạo: CH4 + C3H6, C2H6 + C2H4, C4H8 + H2.", "Vận dụng"),
                ("Đốt cháy hoàn toàn 0,1 mol một alkane X thu được 0,4 mol CO2. Xác định CTPT của X.", "Số C = nCO2 / nX = 0,4 / 0,1 = 4 => C4H10 (butane).", "Thông hiểu")
            ]),
            ("Dạng 2: Phản ứng cộng và trùng hợp của Alkene, Alkyne", "Cộng halogen, cộng H2, cộng HX (tuân theo quy tắc Markovnikov: H vào C có nhiều H hơn). Trùng hợp ethylene -> PE.", [
                ("Cho propene (CH3-CH=CH2) cộng với HBr theo quy tắc Markovnikov. Viết CTCT của sản phẩm chính.", "Sản phẩm chính là 2-bromopropane: CH3-CH(Br)-CH3.", "Thông hiểu"),
                ("Khí ethylene (C2H4) làm mất màu dung dịch nào ở điều kiện thường?", "Ethylene có liên kết đôi C=C làm mất màu dung dịch nước brom (Br2) và thuốc tím (KMnO4).", "Thông hiểu"),
                ("Dẫn khí acetylene (CH≡CH) qua dung dịch AgNO3 trong NH3. Nêu hiện tượng và viết PTHH.", "Xuất hiện kết tủa màu vàng nhạt của bạc acetylide: CH≡CH + 2AgNO3 + 2NH3 -> AgC≡CAg↓ + 2NH4NO3.", "Vận dụng")
            ]),
            ("Dạng 3: Phản ứng thế và oxi hóa của Arene (Benzene và Toluene)", "Toluene phản ứng thế vào vòng benzene ưu tiên định hướng vào vị trí ortho và para. Oxi hóa nhánh methyl bằng KMnO4 đun nóng.", [
                ("Cho toluene (C6H5-CH3) tác dụng với HNO3 đặc xúc tác H2SO4 đặc tỉ lệ mol 1:3 thu được sản phẩm nổ TNT. Viết CTCT của TNT.", "TNT là 2,4,6-trinitrotoluene: C6H2(CH3)(NO2)3.", "Thông hiểu"),
                ("Benzene có làm mất màu dung dịch KMnO4 ở nhiệt độ thường và khi đun nóng không? Toluene thì sao?", "Benzene không làm mất màu KMnO4 cả khi đun nóng. Toluene làm mất màu dung dịch KMnO4 khi đun nóng (nhánh -CH3 bị oxi hóa thành -COOK).", "Vận dụng"),
                ("Cho 7,8 gam benzene tác dụng hoàn toàn với Br2 lỏng (xúc tác Fe). Tính khối lượng bromobenzene thu được (hiệu suất 80%).", "nC6H6 = 0,1 mol => n_lí thuyết = 0,1 mol. m_lí thuyết = 0,1 * 157 = 15,7g => m_thực tế = 15,7 * 0,8 = 12,56 gam.", "Vận dụng cao")
            ])
        ]
    },
    "c5": {
        "title": "DẪN XUẤT HALOGEN - ALCOHOL - PHENOL",
        "methods": [
            ("Dạng 1: Phản ứng thủy phân dẫn xuất halogen và tách HX", "R-X + NaOH -> R-OH + NaX (thủy phân). R-CH2-CH(X)-R' + NaOH/cồn, to -> R-CH=CH-R' (tách HX theo Zaitsev).", [
                ("Đun sôi ethyl bromide (C2H5Br) trong dung dịch NaOH. Viết phương trình phản ứng hóa học xảy ra.", "C2H5Br + NaOH -> C2H5OH + NaBr.", "Thông hiểu"),
                ("Đun nóng 2-bromobutane (CH3-CH(Br)-CH2-CH3) với KOH trong ethanol. Viết CTCT sản phẩm chính.", "Quy tắc Zaitsev: Br tách cùng H ở C liền kề có bậc cao hơn => sản phẩm chính là but-2-ene: CH3-CH=CH-CH3.", "Vận dụng"),
                ("Nêu phương pháp nhận biết nguyên tố clo trong benzyl chloride (C6H5CH2Cl).", "Thủy phân bằng NaOH đun nóng, acid hóa bằng HNO3 rồi nhỏ AgNO3 thấy xuất hiện kết tủa trắng AgCl.", "Vận dụng")
            ]),
            ("Dạng 2: Phản ứng của Alcohol với Na, CuO và tách nước", "R-OH + Na -> R-ONa + 1/2 H2. R-CH2OH + CuO -> R-CHO + Cu + H2O. Tách nước ở 170°C tạo alkene; ở 140°C tạo ether.", [
                ("Cho 4,6 gam sodium (Na) tác dụng hết với ethanol (C2H5OH) dư. Tính thể tích khí H2 thu được ở đktc.", "nNa = 0,2 mol. nH2 = 0,1 mol => V = 0,1 * 22,4 = 2,24 lít.", "Thông hiểu"),
                ("Oxi hóa propan-1-ol và propan-2-ol bằng CuO đun nóng thu được sản phẩm hữu cơ thuộc loại gì?", "Propan-1-ol (alcohol bậc 1) tạo aldehyde (propanal); propan-2-ol (alcohol bậc 2) tạo ketone (acetone).", "Thông hiểu"),
                ("Đun nóng ethanol với H2SO4 đặc ở 140°C thu được chất gì? Ở 170°C thu được chất gì?", "Ở 140°C thu được diethyl ether: 2C2H5OH -> C2H5-O-C2H5 + H2O. Ở 170°C thu được ethylene: C2H5OH -> C2H4 + H2O.", "Vận dụng")
            ]),
            ("Dạng 3: Tính chất đặc trưng của Phenol và phân biệt với Alcohol", "Phenol có tính acid yếu: tác dụng NaOH, không đổi màu quỳ tím. Phản ứng thế vòng thơm cực dễ: tác dụng nước Br2 tạo kết tủa trắng 2,4,6-tribromophenol.", [
                ("Nêu hiện tượng khi nhỏ vài giọt dung dịch nước brom vào ống nghiệm chứa dung dịch phenol.", "Xuất hiện kết tủa trắng của 2,4,6-tribromophenol: C6H5OH + 3Br2 -> C6H2Br3OH↓ + 3HBr.", "Thông hiểu"),
                ("Chất nào sau đây tác dụng được với dung dịch NaOH: ethanol hay phenol? Viết PTHH.", "Chỉ có phenol tác dụng với NaOH (do tính acid): C6H5OH + NaOH -> C6H5ONa (sodium phenolate) + H2O.", "Thông hiểu"),
                ("Sục khí CO2 vào dung dịch sodium phenolate (C6H5ONa). Nêu hiện tượng và giải thích.", "Dung dịch bị vẩn đục do phenol được giải phóng (ít tan trong nước): C6H5ONa + CO2 + H2O -> C6H5OH↓ + NaHCO3 (axit cacbonic mạnh hơn phenol).", "Vận dụng cao")
            ])
        ]
    },
    "c6": {
        "title": "HỢP CHẤT CARBONYL - CARBOXYLIC ACID",
        "methods": [
            ("Dạng 1: Phản ứng tráng bạc và nhận biết Aldehyde, Ketone", "Aldehyde tham gia phản ứng tráng bạc: R-CHO + 2[Ag(NH3)2]OH -> R-COONH4 + 2Ag↓ + 3NH3 + H2O. Riêng HCHO tạo 4Ag.", [
                ("Cho 4,4 gam acetaldehyde (CH3CHO) tác dụng với lượng dư dung dịch AgNO3 trong NH3 đun nóng. Tính khối lượng bạc (Ag) sinh ra.", "nCH3CHO = 4,4 / 44 = 0,1 mol => nAg = 2 * 0,1 = 0,2 mol => mAg = 0,2 * 108 = 21,6 gam.", "Thông hiểu"),
                ("Thuốc thử nào dùng để phân biệt acetaldehyde (CH3CHO) và acetone (CH3COCH3)?", "Dùng thuốc thử Tollens (AgNO3/NH3): acetaldehyde cho kết tủa gương bạc Ag sáng bóng; acetone không phản ứng.", "Thông hiểu"),
                ("Phản ứng iodoform (tác dụng với I2 trong NaOH tạo kết tủa vàng CHI3) dùng để nhận biết hợp chất nào?", "Dùng nhận biết các hợp chất có nhóm methyl ketone: CH3-C(=O)- (như ethanal, acetone).", "Vận dụng")
            ]),
            ("Dạng 2: Tính chất axit của Carboxylic acid", "R-COOH làm quỳ tím hóa đỏ; tác dụng với kim loại trước H, oxit bazo, bazo và muối carbonate giải phóng khí CO2.", [
                ("Viết phương trình hóa học khi cho acetic acid (CH3COOH) lần lượt tác dụng với: a) Mg; b) NaOH; c) CaCO3.", "a) 2CH3COOH + Mg -> (CH3COO)2Mg + H2↑; b) CH3COOH + NaOH -> CH3COONa + H2O; c) 2CH3COOH + CaCO3 -> (CH3COO)2Ca + CO2↑ + H2O.", "Thông hiểu"),
                ("Để trung hòa hoàn toàn 100 mL dung dịch CH3COOH 1M cần dùng vừa đủ bao nhiêu gam NaOH?", "nCH3COOH = 0,1 mol => nNaOH = 0,1 mol => mNaOH = 0,1 * 40 = 4,0 gam.", "Thông hiểu"),
                ("Cho acetic acid tác dụng với bột baking soda (NaHCO3). Nêu hiện tượng thực tế.", "Sủi bọt khí mạnh (khí CO2 thoát ra): CH3COOH + NaHCO3 -> CH3COONa + CO2↑ + H2O.", "Thông hiểu")
            ]),
            ("Dạng 3: Phản ứng ester hóa và Hiệu suất", "RCOOH + R'OH ⇌ RCOOR' + H2O (xúc tác H2SO4 đặc, đun nóng). H% = (lượng thực tế / lượng lí thuyết) * 100%.", [
                ("Đun nóng hỗn hợp gồm 6,0 gam CH3COOH và 6,0 gam C2H5OH với xúc tác H2SO4 đặc thu được 5,28 gam ethyl acetate. Tính hiệu suất phản ứng.", "n_acid = 0,1 mol, n_alcohol = 0,13 mol => lí thuyết tính theo acid (0,1 mol = 8,8g). n_thực tế = 5,28/88 = 0,06 mol => H = (0,06/0,1)*100% = 60%.", "Vận dụng"),
                ("Nêu vai trò của H2SO4 đặc trong phản ứng ester hóa giữa acid và alcohol.", "H2SO4 đặc vừa làm chất xúc tác tăng tốc độ phản ứng, vừa hút nước làm cân bằng chuyển dịch theo chiều thuận tạo nhiều ester hơn.", "Thông hiểu"),
                ("So sánh nhiệt độ sôi của acetic acid (CH3COOH, M=60) và ethyl alcohol (C2H5OH, M=46). Giải thích.", "Acetic acid có nhiệt độ sôi (118°C) cao hơn ethanol (78,3°C) do acid tạo được liên kết hydrogen dạng nhị hợp (dimer) bền vững hơn liên kết hydrogen của alcohol.", "Vận dụng cao")
            ])
        ]
    }
}

print("Chapter domains defined.")
