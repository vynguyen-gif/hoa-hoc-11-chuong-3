# -*- coding: utf-8 -*-
import json
import os

target_dir = r"C:\Users\admin\.gemini\antigravity\scratch\hoa-hoc-11-chuong-3"

def build_lesson(key, topic_name, mcq_data, tf_data, short_data, essay_data):
    return {
        "mcq": [
            {
                "id": f"{key}_c{i+1}",
                "num": i + 1,
                "type": "mcq",
                "levelClass": "level-nb" if i < 7 else ("level-th" if i < 15 else "level-vd"),
                "levelName": "Nhận biết" if i < 7 else ("Thông hiểu" if i < 15 else "Vận dụng"),
                "title": f"Câu {i+1}: {item[0]}",
                "options": item[1],
                "correct": item[2],
                "explanation": item[3]
            }
            for i, item in enumerate(mcq_data)
        ],
        "tf": [
            {
                "id": f"{key}_c{item[0]}",
                "num": item[0],
                "type": "tf",
                "levelClass": "level-th" if idx < 2 else "level-vd",
                "levelName": "Thông hiểu" if idx < 2 else "Vận dụng",
                "title": item[1],
                "statements": [{"text": s[0], "ans": s[1]} for s in item[2]],
                "explanation": item[3]
            }
            for idx, item in enumerate(tf_data)
        ],
        "short": [
            {
                "id": f"{key}_c{item[0]}",
                "num": item[0],
                "type": "short",
                "levelClass": "level-vd",
                "levelName": "Vận dụng",
                "title": item[1],
                "correctText": item[2],
                "explanation": item[3]
            }
            for item in short_data
        ],
        "essay": [
            {
                "id": f"{key}_c{32 + i}",
                "num": 32 + i,
                "type": "essay",
                "levelClass": "level-th" if i < 5 else ("level-vd" if i < 12 else "level-vdc"),
                "levelName": "Thông hiểu" if i < 5 else ("Vận dụng" if i < 12 else "Vận dụng cao"),
                "title": f"Câu {32 + i}: {title}",
                "explanation": f"Hướng dẫn giải Câu {32 + i} ({topic_name}):\n- Bám sát kiến thức trọng tâm bài học.\n- Trình bày rõ ràng các khái niệm, phương trình hóa học và công thức toán học liên quan."
            }
            for i, title in enumerate(essay_data)
        ]
    }

print("Builder ready")
