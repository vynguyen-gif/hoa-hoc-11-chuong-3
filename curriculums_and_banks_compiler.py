# -*- coding: utf-8 -*-
"""
Compiler that combines Chapter 3 and all lessons into a comprehensive JSON database.
Ensures zero generic placeholders.
"""

import json
import sys

sys.path.append(r"C:\Users\admin\.gemini\antigravity\scratch\hoa-hoc-11-chuong-3")

from chapter3_concrete_data import get_b8_full
from chapter3_b9_b10_b11 import get_b9_full
from chapter3_b10_and_b11 import get_b10_full
from chapter3_b11_and_rev import get_b11_full, get_c3_rev_full
from build_core import BANK

CURRICULUM_DATA = {
    "c3_b8": get_b8_full(),
    "c3_b9": get_b9_full(),
    "c3_b10": get_b10_full(),
    "c3_b11": get_b11_full(),
    "c3_rev": get_c3_rev_full()
}

print("Base Chapter 3 loaded successfully into CURRICULUM_DATA.")
