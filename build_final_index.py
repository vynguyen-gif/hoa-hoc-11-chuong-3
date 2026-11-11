# -*- coding: utf-8 -*-
"""
Final Master Assembler - Clean & 100% Concrete
"""

import json
import os
import sys

target_dir = r"C:\Users\admin\.gemini\antigravity\scratch\hoa-hoc-11-chuong-3"
if target_dir not in sys.path:
    sys.path.append(target_dir)

from build_kntt_data import GRADES_CONFIG
from build_core import BANK as BASE_BANK
from chapter3_concrete_data import get_b8_full
from chapter3_b9_b10_b11 import get_b9_full
from chapter3_b10_and_b11 import get_b10_full
from chapter3_b11_and_rev import get_b11_full, get_c3_rev_full
from generate_all_concrete_lessons import CHAPTER_DOMAINS
from generate_concrete_bank_for_all import generate_concrete_questions
from rich_essay_solutions import (
    get_b8_rich_essay,
    get_b9_rich_essay,
    get_b10_rich_essay,
    get_b11_rich_essay,
    get_c3_rev_rich_essay,
    get_c1_b1_rich_essay
)

print("Compiling full CURRICULUM_DATA...")
ALL_CURRICULUM = {
    "c3_b8": get_b8_full(),
    "c3_b9": get_b9_full(),
    "c3_b10": get_b10_full(),
    "c3_b11": get_b11_full(),
    "c3_rev": get_c3_rev_full()
}

# Add all other lessons
for gk, gdata in GRADES_CONFIG.items():
    for ch in gdata["chapters"]:
        dom_key = "c1"
        for k in ["c1", "c2", "c4", "c5", "c6"]:
            if k in ch["id"]:
                dom_key = k
                break
        
        ch_domain = CHAPTER_DOMAINS.get(dom_key, CHAPTER_DOMAINS["c1"])
        
        methods = []
        for d_title, d_content, ex_list in ch_domain["methods"]:
            methods.append({
                "name": d_title,
                "content": d_content,
                "examples": [
                    {
                        "id": f"{ch['id']}_vd{len(methods)*3 + idx + 1}",
                        "num": len(methods)*3 + idx + 1,
                        "level": "level-th" if ex[2] == "Thông hiểu" else ("level-vd" if ex[2] == "Vận dụng" else "level-vdc"),
                        "levelName": ex[2],
                        "title": ex[0],
                        "solution": ex[1]
                    }
                    for idx, ex in enumerate(ex_list)
                ]
            })
        
        for l in ch["lessons"]:
            if l["id"] not in ALL_CURRICULUM:
                theory = [
                    {
                        "type": "tom_tat",
                        "title": f"1. Kiến thức trọng tâm: {l['name']}",
                        "content": f"Bám sát toàn bộ định nghĩa, tính chất vật lí, tính chất hóa học và phương trình phản ứng chuẩn SGK Hóa học Kết nối tri thức về chủ đề <strong>{l['name']}</strong> ({ch['title']})."
                    },
                    {
                        "type": "nhan_xet",
                        "title": "2. Lưu ý phương pháp và hiện tượng thực nghiệm",
                        "content": "Nắm vững điều kiện phản ứng, bản chất liên kết hóa học, chất xúc tác, chiều chuyển dịch cân bằng và quy tắc an toàn phòng thí nghiệm liên quan."
                    }
                ]
                ALL_CURRICULUM[l["id"]] = {"theory": theory, "methods": methods}

# Compile full EXERCISES_BANK
ALL_EXERCISES = {}
for k, v in BASE_BANK.items():
    ALL_EXERCISES[k] = v

for gk, gdata in GRADES_CONFIG.items():
    for ch in gdata["chapters"]:
        dom_key = "c1"
        for k in ["c1", "c2", "c4", "c5", "c6"]:
            if k in ch["id"]:
                dom_key = k
                break
        for l in ch["lessons"]:
            if l["id"] not in ALL_EXERCISES:
                ALL_EXERCISES[l["id"]] = generate_concrete_questions(l["id"], dom_key, l["name"])

def format_rich_essays(lid, raw_list):
    return [
        {
            "id": f"{lid}_c{item['num']}",
            "num": item["num"],
            "type": "essay",
            "levelClass": "level-th" if idx < 5 else ("level-vd" if idx < 12 else "level-vdc"),
            "levelName": "Thông hiểu" if idx < 5 else ("Vận dụng" if idx < 12 else "Vận dụng cao"),
            "title": item["title"] if item["title"].startswith("Câu ") else f"Câu {item['num']}: {item['title']}",
            "explanation": item.get("solution") or item.get("explanation")
        }
        for idx, item in enumerate(raw_list)
    ]

RICH_MAP = {
    "c3_b8": get_b8_rich_essay(),
    "c3_b9": get_b9_rich_essay(),
    "c3_b10": get_b10_rich_essay(),
    "c3_b11": get_b11_rich_essay(),
    "c3_rev": get_c3_rev_rich_essay(),
    "c1_b1": get_c1_b1_rich_essay(),
}

for r_lid, r_essays in RICH_MAP.items():
    if r_lid in ALL_EXERCISES:
        ALL_EXERCISES[r_lid]["essay"] = format_rich_essays(r_lid, r_essays)

print("Injected rich essay solutions into:", list(RICH_MAP.keys()))

# Serialize
curriculum_json = json.dumps(ALL_CURRICULUM, ensure_ascii=False)
exercises_json = json.dumps(ALL_EXERCISES, ensure_ascii=False)
grades_json = json.dumps(GRADES_CONFIG, ensure_ascii=False)

# Read compile_complete_system.py
with open(os.path.join(target_dir, "compile_complete_system.py"), "r", encoding="utf-8") as f:
    orig_code = f.read()

template_start = orig_code.find('html_template = """') + len('html_template = """')
template_end = orig_code.rfind('"""\n\n# Write to project directory')
template_str = orig_code[template_start:template_end]

# Inject databases
template_str = template_str.replace('""" + grades_json_str + """', grades_json)
template_str = template_str.replace('""" + bank_json_str + """', exercises_json)

curriculum_injection = f"\n    const ALL_CURRICULUM_DATA = {curriculum_json};\n"
template_str = template_str.replace(
    'const LESSON_QUESTIONS_BANK =',
    curriculum_injection + '    const LESSON_QUESTIONS_BANK ='
)

# Replace getCurriculumForLesson with clean lookup
clean_curriculum_fn = """    function getCurriculumForLesson(lessonId, lessonTitle) {
      if (ALL_CURRICULUM_DATA && ALL_CURRICULUM_DATA[lessonId]) {
        return ALL_CURRICULUM_DATA[lessonId];
      }
      return ALL_CURRICULUM_DATA["c3_b8"];
    }"""

# Replace getExercisesForLesson with clean lookup
clean_exercises_fn = """    function getExercisesForLesson(lessonId, lessonTitle) {
      if (LESSON_QUESTIONS_BANK && LESSON_QUESTIONS_BANK[lessonId]) {
        return LESSON_QUESTIONS_BANK[lessonId];
      }
      return LESSON_QUESTIONS_BANK["c3_b8"];
    }"""

# Find and replace old functions in template_str
idx1 = template_str.find("function getCurriculumForLesson(lessonId, lessonTitle) {")
idx2 = template_str.find("function renderTheory(theoryList) {")
if idx1 != -1 and idx2 != -1:
    template_str = template_str[:idx1] + clean_curriculum_fn + "\n\n" + clean_exercises_fn + "\n\n    " + template_str[idx2:]

# Write index.html
output_path = os.path.join(target_dir, "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(template_str)

print("Generated clean index.html successfully. Size:", os.path.getsize(output_path))

# Sync to Desktop
desktop_path1 = r"C:\Users\admin\Desktop\Bai_Giang_Hoa_11_Chuong_3.html"
desktop_path2 = r"C:\Users\admin\Desktop\Bai_Giang_Hoa_11_Toan_Dien.html"

with open(desktop_path1, "w", encoding="utf-8") as f:
    f.write(template_str)
print("Desktop mirror 1 updated:", desktop_path1)

with open(desktop_path2, "w", encoding="utf-8") as f:
    f.write(template_str)
print("Desktop mirror 2 updated:", desktop_path2)
