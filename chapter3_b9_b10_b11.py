# -*- coding: utf-8 -*-
"""
Chapter 3 Complete Content for Lessons 9, 10, 11, and Review
"""

def get_b9_full():
    theory = [
        {
            "type": "tom_tat",
            "title": "1. Phương pháp chưng cất (Distillation)",
            "content": """
              <ul>
                <li><strong>Nguyên tắc:</strong> Dựa vào sự khác nhau về <strong>nhiệt độ sôi</strong> của các chất lỏng trong hỗn hợp ở cùng một áp suất nhất định. Chất có nhiệt độ sôi thấp hơn sẽ chuyển thành hơi trước, được dẫn qua ống sinh hàn làm lạnh để ngưng tụ thành chất lỏng tinh khiết (chất chưng cất).</li>
                <li><strong>Các hình thức chưng cất:</strong>
                  <ul>
                    <li><strong>Chưng cất thường:</strong> Dùng để tách các chất lỏng tan lẫn vào nhau có nhiệt độ sôi cách xa nhau đáng kể (thường chênh lệch $\\ge 20 - 30^oC$), ví dụ: tách hỗn hợp ethanol và nước.</li>
                    <li><strong>Chưng cất phân đoạn:</strong> Dùng cột chưng cất phân đoạn (có nhiều đĩa đệm) để tách các chất lỏng có nhiệt độ sôi gần nhau (ví dụ: chưng cất dầu mỏ, sản xuất cồn tinh luyện).</li>
                    <li><strong>Chưng cất lôi cuốn hơi nước:</strong> Dùng để tách các chất lỏng hữu cơ khó tan trong nước, có nhiệt độ sôi cao nhưng có khả năng bay hơi cùng với hơi nước ở nhiệt độ dưới $100^oC$ (ví dụ: tách tinh dầu cam, sả, bưởi, hoa hồng...).</li>
                  </ul>
                </li>
              </ul>
            """
        },
        {
            "type": "chu_y",
            "title": "Lưu ý kĩ thuật khi lắp ráp bộ chưng cất",
            "content": """
              <ol>
                <li><strong>Vai trò của đá bọt:</strong> Luôn cho vài viên đá bọt (mảnh sứ xốp không tráng men) vào bình cầu đáy tròn trước khi đun. Đá bọt tạo các tâm sôi giúp hỗn hợp sôi êm dịu, tránh hiện tượng quá nhiệt dẫn đến <strong>sôi bùng đột ngột</strong> làm chất lỏng trào sang ống sinh hàn.</li>
                <li><strong>Dòng nước làm mát:</strong> Nước làm mát trong áo ống sinh hàn phải <strong>đi vào ở đầu thấp</strong> (phía dưới) và <strong>đi ra ở đầu cao</strong> (phía trên). Cách lắp này đảm bảo áo sinh hàn luôn đầy nước, tối ưu hóa quá trình trao đổi nhiệt làm ngưng tụ triệt để hơi chất lỏng.</li>
                <li><strong>Vị trí nhiệt kế:</strong> Thủy ngân kế phải được đặt sao cho bầu nhiệt kế nằm ngang ngay vị trí nhánh rẽ của bình cầu dẫn hơi sang ống sinh hàn để đo đúng nhiệt độ của luồng hơi đang bay sang.</li>
              </ol>
            """
        },
        {
            "type": "tom_tat",
            "title": "2. Phương pháp chiết (Extraction)",
            "content": """
              <ul>
                <li><strong>Nguyên tắc:</strong> Dựa trên sự khác nhau về <strong>độ hòa tan</strong> của một chất trong hai dung môi không trộn lẫn vào nhau.</li>
                <li><strong>Chiết lỏng - lỏng:</strong>
                  <ul>
                    <li>Dùng <strong>phễu chiết</strong> có khóa xả để tách hai chất lỏng không trộn lẫn tạo thành hai lớp phân cách (ví dụ: tách dầu ăn và nước, tách hỗn hợp benzene và nước).</li>
                    <li>Chất lỏng có khối lượng riêng nhỏ hơn sẽ nổi ở lớp trên, chất lỏng có khối lượng riêng lớn hơn sẽ chìm ở lớp dưới. Mở khóa phễu chiết để xả từ từ lớp chất lỏng ở dưới ra cốc hứng, sau đó đóng khóa lại.</li>
                  </ul>
                </li>
                <li><strong>Chiết lỏng - rắn:</strong> Dùng dung môi lỏng để hòa tan và rút hoạt chất hữu cơ ra khỏi vật liệu rắn (nguyên liệu tự nhiên). Ứng dụng thực tế: Ngâm rượu thuốc (rượu hòa tan hoạt chất từ củ đinh lăng, tam thất), hãm trà/chè xanh, pha cà phê.</li>
              </ul>
            """
        },
        {
            "type": "nhan_xet",
            "title": "3. Phương pháp kết tinh lại (Recrystallization) và Sắc kí cột (Column Chromatography)",
            "content": """
              <ul>
                <li><strong>Phương pháp kết tinh lại:</strong> Dùng để tách biệt và tinh chế các chất rắn. Dựa trên nguyên tắc <strong>độ tan của chất rắn thay đổi mạnh theo nhiệt độ</strong> (thường tăng mạnh khi đun nóng và giảm khi làm lạnh).
                  <br><em>Quy trình:</em> Hòa tan chất rắn thô vào dung môi sôi để tạo dung dịch bão hòa -> <strong>Lọc nóng</strong> để loại bỏ các tạp chất không tan -> Để nguội từ từ cho chất cần tinh chế kết tinh thành tinh thể nguyên chất -> Lọc hút lấy tinh thể, rửa bằng dung môi lạnh và sấy khô.</li>
                <li><strong>Phương pháp sắc kí cột:</strong> Dùng để tách các chất trong một lượng rất nhỏ hỗn hợp phức tạp. Dựa trên sự khác nhau về <strong>khả năng hấp phụ</strong> của các chất trên bề mặt pha tĩnh (chất hấp phụ rắn như silica gel $SiO_2$ hoặc alumina $Al_2O_3$) và độ tan trong pha động (dung môi lỏng rửa giải). Chất bị hấp phụ kém hơn sẽ di chuyển nhanh hơn dọc theo cột và được rửa giải ra trước.</li>
              </ul>
            """
        }
    ]

    methods = [
        {
            "name": "Dạng 1: Phương pháp chưng cất và Thao tác thí nghiệm",
            "content": "Phương pháp: Xác định nhiệt độ sôi của các chất. Lựa chọn dạng chưng cất thích hợp: chưng cất thường (chất lỏng khác nhiệt độ sôi), chưng cất lôi cuốn hơi nước (tinh dầu thơm dễ bay hơi theo hơi nước). Nhớ các quy tắc an toàn về đá bọt, dòng nước sinh hàn, vị trí nhiệt kế.",
            "examples": [
                {
                    "id": "c3_b9_vd1",
                    "num": 1,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Để nấu rượu gạo truyền thống từ dịch lên men tinh bột (hỗn hợp gồm rượu ethanol, nước, bã hèm rượu và men), người ta dùng phương pháp tách chất nào? Hãy giải thích nguyên tắc tách của phương pháp đó.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Người ta sử dụng <strong>phương pháp chưng cất</strong>.<br>- <em>Nguyên tắc:</em> Ethanol có nhiệt độ sôi ($78,3^oC$) thấp hơn nhiều so với nhiệt độ sôi của nước ($100^oC$). Khi đun sôi nồi chưng cất, ethanol bay hơi trước nhiều hơn nước. Luồng hơi bay lên ống dẫn được làm lạnh bằng nước ngoài bồn ngưng tụ, tạo thành dòng rượu lỏng có nồng độ cồn cao hơn dịch ban đầu, trong khi bã hèm và chất không bay hơi nằm lại trong nồi."
                },
                {
                    "id": "c3_b9_vd2",
                    "num": 2,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Một học sinh lắp ráp bộ dụng cụ chưng cất để tách ethanol từ rượu vang nhưng quên cho đá bọt vào bình cầu và lắp ống cấp nước làm mát vào đầu phía trên của ống sinh hàn. Hãy chỉ ra hai lỗi sai này sẽ dẫn đến những hậu quả gì.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>1. <strong>Quên cho đá bọt:</strong> Khi đun sôi, chất lỏng trong bình cầu dễ bị hiện tượng quá nhiệt và sôi bùng đột ngột, làm chất lỏng trào mạnh vào ống sinh hàn mà không kịp bay hơi ngưng tụ, làm bẩn sản phẩm chưng cất và có thể gây nguy cơ cháy nổ.<br>2. <strong>Cấp nước vào đầu trên ống sinh hàn:</strong> Nước chảy từ trên xuống theo trọng lực sẽ nhanh chóng thoát ra ở đầu dưới, làm cho khoang áo làm mát không thể đầy nước và có nhiều khoảng khí rỗng. Khả năng trao đổi nhiệt bị giảm sút nghiêm trọng, hơi ethanol không ngưng tụ được hết và sẽ thoát ra ngoài dạng khí gây hao hụt và ô nhiễm."
                },
                {
                    "id": "c3_b9_vd3",
                    "num": 3,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Tại sao để thu hồi tinh dầu sả (thành phần chính là citral, sôi ở $229^oC$ và dễ bị nhiệt phân hủy), người nông dân lại sử dụng phương pháp chưng cất lôi cuốn hơi nước mà không đun trực tiếp ở nhiệt độ cao?",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Tinh dầu sả có nhiệt độ sôi rất cao ($229^oC$). Nếu đun nóng trực tiếp đến nhiệt độ này, các phân tử tinh dầu sẽ bị nhiệt phân hủy làm mất mùi thơm tự nhiên hoặc bị biến tính thành chất độc hại.<br>- Khi sục luồng hơi nước vào khối lá sả (hoặc đun sôi cùng nước), áp suất hơi của hỗn hợp tinh dầu - nước là tổng áp suất riêng phần của hai chất. Do đó, hỗn hợp sẽ sôi ở nhiệt độ <strong>dưới $100^oC$</strong> (thấp hơn nhiệt độ sôi của cả nước và tinh dầu), tinh dầu sả dễ dàng bay theo hơi nước sang bộ ngưng tụ một cách an toàn mà không bị phân hủy."
                }
            ]
        },
        {
            "name": "Dạng 2: Kĩ thuật chiết và Lựa chọn dung môi chiết",
            "content": "Phương pháp: Dung môi chiết phải hòa tan chất cần tách tốt hơn dung môi ban đầu, không trộn lẫn với dung môi ban đầu và có nhiệt độ sôi thấp dễ tách ra sau khi chiết. Sử dụng phễu chiết: lắc đều, mở khóa xả áp, để yên tách 2 lớp, xả lớp dưới, giữ lớp trên.",
            "examples": [
                {
                    "id": "c3_b9_vd4",
                    "num": 4,
                    "level": "level-th",
                    "levelName": "Thông hiểu",
                    "title": "Trình bày các bước thực hiện thao tác chiết để tách riêng chất hữu cơ $A$ tan trong nước bằng dung môi hữu cơ diethyl ether trong phòng thí nghiệm bằng phễu chiết.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>1. Đóng khóa phễu chiết, rót dung dịch chứa chất $A$ trong nước vào phễu chiết, sau đó cho thêm diethyl ether vào (khoảng 1/3 dung tích phễu).<br>2. Đậy chặt nút phễu chiết, dùng tay giữ chặt nút và khóa, dốc ngược phễu chiết và lắc đều khoảng vài phút. Thi thoảng mở nhẹ khóa phễu chiết để xả bớt áp suất hơi sinh ra rồi đóng khóa lại.<br>3. Đặt phễu chiết lên giá sắt, mở nút đậy trên miệng phễu chiết, để yên cho hỗn hợp tách hoàn toàn thành 2 lớp chất lỏng phân cách rõ rệt (ether nhẹ hơn nổi lên trên hòa tan chất A, lớp nước ở dưới).<br>4. Mở nhẹ khóa phễu chiết cho lớp nước ở dưới chảy từ từ xuống bình hứng phía dưới, khi mặt phân cách chạm đến khóa thì đóng ngay khóa lại. Rót lớp dung dịch ether chứa chất A từ miệng trên của phễu chiết ra bình thu hồi."
                },
                {
                    "id": "c3_b9_vd5",
                    "num": 5,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Hỗn hợp lỏng gồm benzene (khối lượng riêng $d = 0,88 \\text{ g/mL}$) và dung dịch nước muối ăn ($d = 1,15 \\text{ g/mL}$). Khi cho vào phễu chiết và để yên, lớp chất lỏng nào sẽ nằm ở trên và lớp nào nằm ở dưới? Giải thích.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Benzene là chất lỏng không phân cực, không tan và không trộn lẫn với nước muối ăn.<br>- Benzene có khối lượng riêng ($d = 0,88 \\text{ g/mL}$) nhỏ hơn khối lượng riêng của nước muối ($d = 1,15 \\text{ g/mL}$).<br>$\\Rightarrow$ Do đó, lớp benzene sẽ nhẹ hơn và nổi lên ở lớp trên, còn dung dịch nước muối ăn nặng hơn sẽ chìm xuống ở lớp dưới trong phễu chiết."
                },
                {
                    "id": "c3_b9_vd6",
                    "num": 6,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Người ta thường ngâm củ tam thất hoặc nhân sâm vào rượu etylic 40 - 45 độ để bồi bổ sức khỏe. Quá trình này ứng dụng phương pháp tách chất nào? Hãy chỉ ra đâu là chất tan, dung môi và bã chiết.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Đây là ứng dụng của <strong>phương pháp chiết lỏng - rắn</strong>.<br>- <em>Chất tan:</em> Các saponin và các hoạt chất sinh học quý có trong củ tam thất hoặc nhân sâm.<br>- <em>Dung môi chiết:</em> Rượu etylic (ethanol pha nước có nồng độ $40 - 45^o$).<br>- <em>Bã chiết:</em> Phần bã xơ của củ tam thất hoặc nhân sâm sau khi các hoạt chất đã bị hòa tan vào rượu."
                }
            ]
        },
        {
            "name": "Dạng 3: Phương pháp kết tinh lại và Sắc kí cột",
            "content": "Phương pháp: Tính khối lượng kết tinh từ độ tan: $m_{\\text{kết tinh}} = m_{\\text{tan ở } T_1} - m_{\\text{tan ở } T_2}$. Trong sắc kí cột: chất bị hấp phụ yếu trên pha tĩnh sẽ bị pha động cuốn trôi và thoát ra khỏi cột trước.",
            "examples": [
                {
                    "id": "c3_b9_vd7",
                    "num": 7,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Độ tan của benzoic acid ($C_6H_5COOH$) trong nước ở $95^oC$ là 68,0 gam/lít và ở $20^oC$ là 2,90 gam/lít. Tính khối lượng tối đa tinh thể benzoic acid thu được khi làm lạnh 250 mL dung dịch bão hòa benzoic acid từ $95^oC$ xuống $20^oC$.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Khối lượng benzoic acid tan trong 250 mL ($0,25 \\text{ lít}$) dung dịch bão hòa ở $95^oC$:<br>$m_1 = 68,0 \\times 0,25 = 17,00 \\text{ gam}$.<br>- Khối lượng benzoic acid còn tan trong 250 mL dung dịch ở $20^oC$:<br>$m_2 = 2,90 \\times 0,25 = 0,725 \\text{ gam}$.<br>- Khối lượng benzoic acid kết tinh tách ra dưới dạng tinh thể:<br>$m_{\\text{kết tinh}} = m_1 - m_2 = 17,00 - 0,725 = 16,275 \\text{ gam}$."
                },
                {
                    "id": "c3_b9_vd8",
                    "num": 8,
                    "level": "level-vd",
                    "levelName": "Vận dụng",
                    "title": "Trong quy trình kết tinh lại chất rắn, giải thích tại sao bước lọc loại bỏ tạp chất không tan bắt buộc phải tiến hành khi dung dịch còn đang nóng (lọc nóng) và dùng phễu lọc có cuống ngắn hoặc thành ấm?",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- Chất rắn cần tinh chế có độ tan giảm rất nhanh khi nhiệt độ hạ xuống.<br>- Nếu để dung dịch nguội rồi mới lọc thì chất cần tinh chế sẽ lập tức kết tinh ngay trên phễu và giấy lọc lẫn vào tạp chất không tan, gây tắc phễu và tổn thất chất rắn.<br>- Do đó phải <strong>lọc nóng</strong> (khi chất vẫn tan hoàn toàn) và dùng phễu cuống ngắn (hoặc ủ ấm phễu) để dung dịch chảy nhanh qua giấy lọc trước khi kịp nguội, chỉ giữ lại tạp chất không tan trên giấy lọc."
                },
                {
                    "id": "c3_b9_vd9",
                    "num": 9,
                    "level": "level-vdc",
                    "levelName": "Vận dụng cao",
                    "title": "Dùng phương pháp sắc kí cột với chất hấp phụ silica gel để tách hỗn hợp gồm ba chất $X, Y, Z$. Biết khả năng bị hấp phụ trên silica gel giảm dần theo thứ tự: $X > Y > Z$. Hãy dự đoán thứ tự các chất thoát ra khỏi cột sắc kí khi liên tục cho dung môi rửa giải chạy qua cột. Giải thích.",
                    "solution": "<strong>Lời giải chi tiết:</strong><br>- <strong>Thứ tự các chất thoát ra khỏi đáy cột là:</strong> $Z$ thoát ra đầu tiên, tiếp theo là $Y$, và cuối cùng là $X$.<br>- <em>Giải thích:</em> Chất $Z$ bị silica gel (pha tĩnh) hấp phụ yếu nhất nên liên kết lỏng lẻo nhất, dễ bị dòng dung môi lỏng (pha động) cuốn trôi di chuyển nhanh nhất dọc theo cột và thoát ra trước tiên. Ngược lại, chất $X$ bị silica gel hấp phụ mạnh nhất nên bám chặt nhất trên hạt silica gel, di chuyển chậm nhất và sẽ thoát ra sau cùng."
                }
            ]
        }
    ]

    return { "theory": theory, "methods": methods }

print("b9 full definition ready.")
