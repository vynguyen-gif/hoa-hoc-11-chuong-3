# -*- coding: utf-8 -*-
"""
Script to build comprehensive KNTT Chemistry Platform for Grade 10, 11, 12.
All content strictly adheres to 'Kết nối tri thức với cuộc sống'.
"""
import json
import os
import sys

target_dir = r"C:\Users\admin\.gemini\antigravity\scratch\hoa-hoc-11-chuong-3"
if target_dir not in sys.path:
    sys.path.append(target_dir)

from build_kntt_data import GRADES_CONFIG
from build_full_chemistry import get_b8_questions, get_b9_questions, get_b10_questions, get_b11_questions
from build_all_grades import create_exercise_set

print("Loading Chapter 3 raw questions...")
b8_raw = get_b8_questions()
b9_raw = get_b9_questions()
b10_raw = get_b10_questions()
b11_raw = get_b11_questions()

# Build lesson exercise bank dictionary
BANK = {}

BANK["c3_b8"] = create_exercise_set(
    "c3_b8", 
    "Hợp chất hữu cơ và hóa học hữu cơ",
    b8_raw["mcq"],
    [(item[0], item[1], item[2]) for item in b8_raw["tf"]],
    [(item[0], item[1], item[2]) for item in b8_raw["short"]],
    b8_raw["essay"]
)

BANK["c3_b9"] = create_exercise_set(
    "c3_b9", 
    "Phương pháp tách biệt và tinh chế hợp chất hữu cơ",
    b9_raw["mcq"],
    [(item[0], item[1], item[2]) for item in b9_raw["tf"]],
    [(item[0], item[1], item[2]) for item in b9_raw["short"]],
    b9_raw["essay"]
)

BANK["c3_b10"] = create_exercise_set(
    "c3_b10", 
    "Công thức phân tử hợp chất hữu cơ",
    b10_raw["mcq"],
    [(item[0], item[1], item[2]) for item in b10_raw["tf"]],
    [(item[0], item[1], item[2]) for item in b10_raw["short"]],
    b10_raw["essay"]
)

BANK["c3_b11"] = create_exercise_set(
    "c3_b11", 
    "Cấu trúc phân tử hợp chất hữu cơ",
    b11_raw["mcq"],
    [(item[0], item[1], item[2]) for item in b11_raw["tf"]],
    [(item[0], item[1], item[2]) for item in b11_raw["short"]],
    b11_raw["essay"]
)

print("Chapter 3 lessons loaded:", len(BANK))
