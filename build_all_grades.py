# -*- coding: utf-8 -*-
"""
Full KNTT Chemistry Curriculums and Question Banks for Grade 10, Grade 11, Grade 12
"""

# Helper to build standard 48-question format
def create_exercise_set(lesson_key, topic_title, mcq_list, tf_list, short_list, essay_list):
    mcq = [
        {
            "id": f"{lesson_key}_c{i+1}",
            "num": i + 1,
            "type": "mcq",
            "levelClass": "level-nb" if i < 7 else ("level-th" if i < 15 else "level-vd"),
            "levelName": "Nhận biết" if i < 7 else ("Thông hiểu" if i < 15 else "Vận dụng"),
            "title": f"Câu {i+1}: {item[0]}",
            "options": item[1],
            "correct": item[2],
            "explanation": item[3]
        }
        for i, item in enumerate(mcq_list)
    ]
    tf = [
        {
            "id": f"{lesson_key}_c{22 + idx}",
            "num": 22 + idx,
            "type": "tf",
            "levelClass": "level-th" if idx < 2 else "level-vd",
            "levelName": "Thông hiểu" if idx < 2 else "Vận dụng",
            "title": item[0],
            "statements": [{"text": s[0], "ans": s[1]} for s in item[1]],
            "explanation": item[2]
        }
        for idx, item in enumerate(tf_list)
    ]
    short = [
        {
            "id": f"{lesson_key}_c{26 + idx}",
            "num": 26 + idx,
            "type": "short",
            "levelClass": "level-vd",
            "levelName": "Vận dụng",
            "title": item[0],
            "correctText": item[1],
            "explanation": item[2]
        }
        for idx, item in enumerate(short_list)
    ]
    essay = [
        {
            "id": f"{lesson_key}_c{32 + i}",
            "num": 32 + i,
            "type": "essay",
            "levelClass": "level-th" if i < 5 else ("level-vd" if i < 12 else "level-vdc"),
            "levelName": "Thông hiểu" if i < 5 else ("Vận dụng" if i < 12 else "Vận dụng cao"),
            "title": f"Câu {32 + i}: {title}",
            "explanation": f"Hướng dẫn giải Câu {32 + i} ({topic_title} - SGK Kết nối tri thức):\n- Bám sát kiến thức trọng tâm SGK.\n- Trình bày định nghĩa, giải thích hiện tượng và phương trình hóa học chi tiết."
        }
        for i, title in enumerate(essay_list)
    ]
    return {"mcq": mcq, "tf": tf, "short": short, "essay": essay}

print("create_exercise_set ready.")
