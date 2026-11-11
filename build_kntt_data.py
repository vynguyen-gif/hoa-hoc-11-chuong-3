# -*- coding: utf-8 -*-
import json

GRADES_CONFIG = {
    "g10": {
        "title": "Hóa học 10 - Kết nối tri thức",
        "chapters": [
            {
                "id": "g10_c1",
                "title": "CHƯƠNG 1. CẤU TẠO NGUYÊN TỬ",
                "lessons": [
                    {"id": "g10_b1", "code": "Bài 1", "name": "Nhập môn hóa học"},
                    {"id": "g10_b2", "code": "Bài 2", "name": "Nguyên tử và cấu tạo nguyên tử"},
                    {"id": "g10_b3", "code": "Bài 3", "name": "Nguyên tố hóa học"},
                    {"id": "g10_b4", "code": "Bài 4", "name": "Cấu trúc lớp vỏ electron nguyên tử"},
                    {"id": "g10_c1_rev", "code": "Ôn tập", "name": "Bài tập cuối chương I"}
                ]
            },
            {
                "id": "g10_c2",
                "title": "CHƯƠNG 2. BẢNG TUẦN HOÀN CÁC NGUYÊN TỐ HÓA HỌC",
                "lessons": [
                    {"id": "g10_b5", "code": "Bài 5", "name": "Cấu tạo bảng tuần hoàn các nguyên tố hóa học"},
                    {"id": "g10_b6", "code": "Bài 6", "name": "Xu hướng biến đổi một số tính chất trong bảng tuần hoàn"},
                    {"id": "g10_b7", "code": "Bài 7", "name": "Định luật tuần hoàn và ý nghĩa của bảng tuần hoàn"},
                    {"id": "g10_c2_rev", "code": "Ôn tập", "name": "Bài tập cuối chương II"}
                ]
            },
            {
                "id": "g10_c3",
                "title": "CHƯƠNG 3. LIÊN KẾT HÓA HỌC",
                "lessons": [
                    {"id": "g10_b8", "code": "Bài 8", "name": "Quy tắc octet"},
                    {"id": "g10_b9", "code": "Bài 9", "name": "Liên kết ion"},
                    {"id": "g10_b10", "code": "Bài 10", "name": "Liên kết cộng hóa trị"},
                    {"id": "g10_b11", "code": "Bài 11", "name": "Liên kết hydrogen và tương tác van der Waals"},
                    {"id": "g10_c3_rev", "code": "Ôn tập", "name": "Bài tập cuối chương III"}
                ]
            },
            {
                "id": "g10_c4",
                "title": "CHƯƠNG 4. PHẢN ỨNG OXI HÓA - KHỬ",
                "lessons": [
                    {"id": "g10_b12", "code": "Bài 12", "name": "Phản ứng oxi hóa - khử"},
                    {"id": "g10_c4_rev", "code": "Ôn tập", "name": "Bài tập cuối chương IV"}
                ]
            },
            {
                "id": "g10_c5",
                "title": "CHƯƠNG 5. NĂNG LƯỢNG HÓA HỌC",
                "lessons": [
                    {"id": "g10_b13", "code": "Bài 13", "name": "Enthalpy tạo thành và biến thiên enthalpy của phản ứng"},
                    {"id": "g10_b14", "code": "Bài 14", "name": "Biểu thức tính biến thiên enthalpy của phản ứng hóa học"},
                    {"id": "g10_c5_rev", "code": "Ôn tập", "name": "Bài tập cuối chương V"}
                ]
            },
            {
                "id": "g10_c6",
                "title": "CHƯƠNG 6. TỐC ĐỘ PHẢN ỨNG HÓA HỌC",
                "lessons": [
                    {"id": "g10_b15", "code": "Bài 15", "name": "Phương trình tốc độ phản ứng và hằng số tốc độ"},
                    {"id": "g10_b16", "code": "Bài 16", "name": "Các yếu tố ảnh hưởng đến tốc độ phản ứng"},
                    {"id": "g10_c6_rev", "code": "Ôn tập", "name": "Bài tập cuối chương VI"}
                ]
            },
            {
                "id": "g10_c7",
                "title": "CHƯƠNG 7. NGUYÊN TỐ NHÓM HALOGEN",
                "lessons": [
                    {"id": "g10_b17", "code": "Bài 17", "name": "Đơn chất halogen"},
                    {"id": "g10_b18", "code": "Bài 18", "name": "Hydrogen halide và một số phản ứng của ion halide"},
                    {"id": "g10_c7_rev", "code": "Ôn tập", "name": "Bài tập cuối chương VII"}
                ]
            }
        ]
    },
    "g11": {
        "title": "Hóa học 11 - Kết nối tri thức",
        "chapters": [
            {
                "id": "g11_c1",
                "title": "CHƯƠNG 1. CÂN BẰNG HÓA HỌC",
                "lessons": [
                    {"id": "c1_b1", "code": "Bài 1", "name": "Khái niệm về cân bằng hóa học"},
                    {"id": "c1_b2", "code": "Bài 2", "name": "Cân bằng trong dung dịch nước"},
                    {"id": "c1_rev", "code": "Ôn tập", "name": "Bài tập cuối chương I"}
                ]
            },
            {
                "id": "g11_c2",
                "title": "CHƯƠNG 2. NITROGEN VÀ SULFUR",
                "lessons": [
                    {"id": "c2_b3", "code": "Bài 3", "name": "Đơn chất nitrogen"},
                    {"id": "c2_b4", "code": "Bài 4", "name": "Ammonia và một số hợp chất ammonium"},
                    {"id": "c2_b5", "code": "Bài 5", "name": "Một số hợp chất với oxygen của nitrogen"},
                    {"id": "c2_b6", "code": "Bài 6", "name": "Một số dạng đơn chất sulfur"},
                    {"id": "c2_b7", "code": "Bài 7", "name": "Sulfur dioxide và sulfuric acid"},
                    {"id": "c2_rev", "code": "Ôn tập", "name": "Bài tập cuối chương II"}
                ]
            },
            {
                "id": "g11_c3",
                "title": "CHƯƠNG 3. ĐẠI CƯƠNG VỀ HÓA HỌC HỮU CƠ",
                "lessons": [
                    {"id": "c3_b8", "code": "Bài 8", "name": "Hợp chất hữu cơ và hóa học hữu cơ"},
                    {"id": "c3_b9", "code": "Bài 9", "name": "Phương pháp tách biệt và tinh chế hợp chất hữu cơ"},
                    {"id": "c3_b10", "code": "Bài 10", "name": "Công thức phân tử hợp chất hữu cơ"},
                    {"id": "c3_b11", "code": "Bài 11", "name": "Cấu trúc phân tử hợp chất hữu cơ"},
                    {"id": "c3_rev", "code": "Ôn tập", "name": "Bài tập cuối chương III"}
                ]
            },
            {
                "id": "g11_c4",
                "title": "CHƯƠNG 4. HYDROCARBON",
                "lessons": [
                    {"id": "c4_b12", "code": "Bài 12", "name": "Alkane"},
                    {"id": "c4_b13", "code": "Bài 13", "name": "Hydrocarbon không no (Alkene và Alkyne)"},
                    {"id": "c4_b14", "code": "Bài 14", "name": "Arene (Hydrocarbon thơm)"},
                    {"id": "c4_rev", "code": "Ôn tập", "name": "Bài tập cuối chương IV"}
                ]
            },
            {
                "id": "g11_c5",
                "title": "CHƯƠNG 5. DẪN XUẤT HALOGEN - ALCOHOL - PHENOL",
                "lessons": [
                    {"id": "c5_b15", "code": "Bài 15", "name": "Dẫn xuất halogen"},
                    {"id": "c5_b16", "code": "Bài 16", "name": "Alcohol"},
                    {"id": "c5_b17", "code": "Bài 17", "name": "Phenol"},
                    {"id": "c5_rev", "code": "Ôn tập", "name": "Bài tập cuối chương V"}
                ]
            },
            {
                "id": "g11_c6",
                "title": "CHƯƠNG 6. HỢP CHẤT CARBONYL - CARBOXYLIC ACID",
                "lessons": [
                    {"id": "c6_b18", "code": "Bài 18", "name": "Hợp chất carbonyl (Aldehyde và Ketone)"},
                    {"id": "c6_b19", "code": "Bài 19", "name": "Carboxylic acid"},
                    {"id": "c6_rev", "code": "Ôn tập", "name": "Bài tập cuối chương VI"}
                ]
            }
        ]
    },
    "g12": {
        "title": "Hóa học 12 - Kết nối tri thức",
        "chapters": [
            {
                "id": "g12_c1",
                "title": "CHƯƠNG 1. ESTER - LIPID",
                "lessons": [
                    {"id": "g12_b1", "code": "Bài 1", "name": "Ester"},
                    {"id": "g12_b2", "code": "Bài 2", "name": "Lipid. Xà phòng và chất giặt rửa"},
                    {"id": "g12_c1_rev", "code": "Ôn tập", "name": "Bài tập cuối chương I"}
                ]
            },
            {
                "id": "g12_c2",
                "title": "CHƯƠNG 2. CARBOHYDRATE",
                "lessons": [
                    {"id": "g12_b3", "code": "Bài 3", "name": "Glucose và fructose"},
                    {"id": "g12_b4", "code": "Bài 4", "name": "Saccharose và maltose"},
                    {"id": "g12_b5", "code": "Bài 5", "name": "Tinh bột và cellulose"},
                    {"id": "g12_c2_rev", "code": "Ôn tập", "name": "Bài tập cuối chương II"}
                ]
            },
            {
                "id": "g12_c3",
                "title": "CHƯƠNG 3. HỢP CHẤT CHỨA NITROGEN",
                "lessons": [
                    {"id": "g12_b6", "code": "Bài 6", "name": "Amine"},
                    {"id": "g12_b7", "code": "Bài 7", "name": "Amino acid và peptide"},
                    {"id": "g12_b8", "code": "Bài 8", "name": "Protein và enzyme"},
                    {"id": "g12_c3_rev", "code": "Ôn tập", "name": "Bài tập cuối chương III"}
                ]
            },
            {
                "id": "g12_c4",
                "title": "CHƯƠNG 4. POLYMER",
                "lessons": [
                    {"id": "g12_b9", "code": "Bài 9", "name": "Đại cương về polymer"},
                    {"id": "g12_b10", "code": "Bài 10", "name": "Vật liệu polymer"},
                    {"id": "g12_c4_rev", "code": "Ôn tập", "name": "Bài tập cuối chương IV"}
                ]
            },
            {
                "id": "g12_c5",
                "title": "CHƯƠNG 5. PIN ĐIỆN VÀ ĐIỆN PHÂN",
                "lessons": [
                    {"id": "g12_b11", "code": "Bài 11", "name": "Thế điện cực và nguồn điện hóa học"},
                    {"id": "g12_b12", "code": "Bài 12", "name": "Điện phân"},
                    {"id": "g12_c5_rev", "code": "Ôn tập", "name": "Bài tập cuối chương V"}
                ]
            },
            {
                "id": "g12_c6",
                "title": "CHƯƠNG 6. ĐẠI CƯƠNG VỀ KIM LOẠI",
                "lessons": [
                    {"id": "g12_b13", "code": "Bài 13", "name": "Cấu tạo và liên kết kim loại"},
                    {"id": "g12_b14", "code": "Bài 14", "name": "Tính chất của kim loại"},
                    {"id": "g12_b15", "code": "Bài 15", "name": "Tách kim loại và tái chế"},
                    {"id": "g12_b16", "code": "Bài 16", "name": "Hợp kim và sự ăn mòn kim loại"},
                    {"id": "g12_c6_rev", "code": "Ôn tập", "name": "Bài tập cuối chương VI"}
                ]
            },
            {
                "id": "g12_c7",
                "title": "CHƯƠNG 7. NGUYÊN TỐ NHÓM IA VÀ NHÓM IIA",
                "lessons": [
                    {"id": "g12_b17", "code": "Bài 17", "name": "Nguyên tố nhóm IA"},
                    {"id": "g12_b18", "code": "Bài 18", "name": "Nguyên tố nhóm IIA"},
                    {"id": "g12_c7_rev", "code": "Ôn tập", "name": "Bài tập cuối chương VII"}
                ]
            },
            {
                "id": "g12_c8",
                "title": "CHƯƠNG 8. KIM LOẠI CHUYỂN TIẾP DÃY THỨ NHẤT VÀ PHỨC CHẤT",
                "lessons": [
                    {"id": "g12_b19", "code": "Bài 19", "name": "Đại cương về kim loại chuyển tiếp dãy thứ nhất"},
                    {"id": "g12_b20", "code": "Bài 20", "name": "Sơ lược về phức chất"},
                    {"id": "g12_c8_rev", "code": "Ôn tập", "name": "Bài tập cuối chương VIII"}
                ]
            }
        ]
    }
}

print("Config defined successfully.")
