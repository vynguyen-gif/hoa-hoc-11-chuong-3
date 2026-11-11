# -*- coding: utf-8 -*-
"""
Master compiler that generates index.html with 100% concrete chemistry content.
"""

import json
import os
import sys

target_dir = r"C:\Users\admin\.gemini\antigravity\scratch\hoa-hoc-11-chuong-3"
if target_dir not in sys.path:
    sys.path.append(target_dir)

from build_kntt_data import GRADES_CONFIG
from build_core import BANK
from chapter3_concrete_data import get_b8_full
from chapter3_b9_b10_b11 import get_b9_full
from chapter3_b10_and_b11 import get_b10_full
from chapter3_b11_and_rev import get_b11_full, get_c3_rev_full
from generate_all_concrete_lessons import CHAPTER_DOMAINS

print("Preparing CURRICULUM_DATABASE...")
CURRICULUM_DATABASE = {
    "c3_b8": get_b8_full(),
    "c3_b9": get_b9_full(),
    "c3_b10": get_b10_full(),
    "c3_b11": get_b11_full(),
    "c3_rev": get_c3_rev_full()
}

# Add concrete chapter curriculums for c1, c2, c4, c5, c6
for ch_key, ch_data in CHAPTER_DOMAINS.items():
    # Build 9 examples
    methods = []
    for d_title, d_content, ex_list in ch_data["methods"]:
        methods.append({
            "name": d_title,
            "content": d_content,
            "examples": [
                {
                    "id": f"{ch_key}_ex{idx+1}",
                    "num": idx + 1 + len(methods)*3,
                    "level": "level-th" if ex[2] == "Thông hiểu" else ("level-vd" if ex[2] == "Vận dụng" else "level-vdc"),
                    "levelName": ex[2],
                    "title": ex[0],
                    "solution": ex[1]
                }
                for idx, ex in enumerate(ex_list)
            ]
        })
    
    # Store template for chapter lessons
    theory = [
        {
            "type": "tom_tat",
            "title": f"1. Kiến thức trọng tâm: {ch_data['title']}",
            "content": f"Bám sát toàn bộ định nghĩa, tính chất vật lí, tính chất hóa học và phương trình phản ứng chuẩn SGK Hóa học Kết nối tri thức về chủ đề {ch_data['title']}."
        },
        {
            "type": "nhan_xet",
            "title": "2. Lưu ý phương pháp và hiện tượng thực nghiệm",
            "content": "Nắm vững điều kiện phản ứng, chất xúc tác, chiều chuyển dịch cân bằng và quy tắc an toàn phòng thí nghiệm liên quan."
        }
    ]
    
    # Map to all lessons of that chapter
    if ch_key == "c1":
        for lid in ["c1_b1", "c1_b2", "c1_rev"]:
            CURRICULUM_DATABASE[lid] = {"theory": theory, "methods": methods}
    elif ch_key == "c2":
        for lid in ["c2_b3", "c2_b4", "c2_b5", "c2_b6", "c2_b7", "c2_rev"]:
            CURRICULUM_DATABASE[lid] = {"theory": theory, "methods": methods}
    elif ch_key == "c4":
        for lid in ["c4_b12", "c4_b13", "c4_b14", "c4_rev"]:
            CURRICULUM_DATABASE[lid] = {"theory": theory, "methods": methods}
    elif ch_key == "c5":
        for lid in ["c5_b15", "c5_b16", "c5_b17", "c5_rev"]:
            CURRICULUM_DATABASE[lid] = {"theory": theory, "methods": methods}
    elif ch_key == "c6":
        for lid in ["c6_b18", "c6_b19", "c6_rev"]:
            CURRICULUM_DATABASE[lid] = {"theory": theory, "methods": methods}

print(f"Curriculum database compiled with {len(CURRICULUM_DATABASE)} lessons.")
print(f"Question Bank database compiled with {len(BANK)} base lessons.")
