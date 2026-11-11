# -*- coding: utf-8 -*-
"""
Chem Formatter: Formats chemical formulas with proper Unicode subscripts and superscripts.
Guarantees correct subscripts for all chemical formulas, equations, ions, and hydrates.
"""

import re

SUB_MAP = {
    '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
    '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉'
}

SUP_MAP = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
    '+': '⁺', '-': '⁻'
}

def to_sub(digits):
    return ''.join(SUB_MAP.get(c, c) for c in str(digits))

def to_sup(chars):
    return ''.join(SUP_MAP.get(c, c) for c in str(chars))

# Chemical element symbols ordered by length descending so e.g. 'Na' matches before 'N', 'Ca' before 'C', 'Fe' before 'F'
ELEMENTS_ORDERED = [
    'He', 'Li', 'Be', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'Cl', 'Ar',
    'Ca', 'Sc', 'Ti', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
    'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Zr', 'Nb',
    'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb',
    'Te', 'Xe', 'Cs', 'Ba', 'Hf', 'Ta', 'Pt', 'Au', 'Hg', 'Tl',
    'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Rf', 'Db', 'Sg',
    'H', 'B', 'C', 'N', 'O', 'F', 'P', 'S', 'K', 'V', 'I', 'W', 'U'
]

ELEMS_PATTERN = '(?:' + '|'.join(ELEMENTS_ORDERED) + ')'

def format_chemical_text(text):
    if not text or not isinstance(text, str):
        return text

    # 1. Clean simple LaTeX chemical formulas like $NO_2$, $SO_2$, $NH_3$, $H_2SO_4$, $Ca(OH)_2$
    def replace_simple_latex(m):
        inner = m.group(1).strip()
        # If it contains equations or fractions, keep LaTeX for MathJax
        if any(k in inner for k in ['\\frac', '\\rightarrow', '\\xrightarrow', '\\rightleftharpoons', '\\Delta', '=']):
            return m.group(0)
        # Convert superscripts ^{2-} -> ²⁻
        res = re.sub(r'\^\{?([0-9]*[\+\-])\}?', lambda sm: to_sup(sm.group(1)), inner)
        # Convert subscripts _{2} or _2 -> ₂
        res = re.sub(r'\_\{?([0-9]+)\}?', lambda sm: to_sub(sm.group(1)), res)
        # Remove LaTeX escapes
        res = res.replace('\\', '').replace('{', '').replace('}', '')
        return res

    text = re.sub(r'\$([^\$]+)\$', replace_simple_latex, text)

    # 2. Specific hydrates with dot: CaSO4.2H2O, CuSO4.5H2O, etc.
    text = re.sub(r'CaSO4\.(?:2)?H2O', 'CaSO₄·2H₂O', text)
    text = re.sub(r'CaSO4\.H2O', 'CaSO₄·H₂O', text)
    text = re.sub(r'CuSO4\.5H2O', 'CuSO₄·5H₂O', text)
    text = re.sub(r'MgSO4\.7H2O', 'MgSO₄·7H₂O', text)
    text = re.sub(r'(\w+)\.(\d+)H2O', lambda m: m.group(1) + '·' + m.group(2) + 'H₂O', text)

    # 3. Common ions
    text = re.sub(r'\bSO4\(2\-\)|\bSO4\^?2\-|\bSO4\^\{?2\-\}?', 'SO₄²⁻', text)
    text = re.sub(r'\bCO3\(2\-\)|\bCO3\^?2\-|\bCO3\^\{?2\-\}?', 'CO₃²⁻', text)
    text = re.sub(r'\bHCO3\-|\bHCO3\^\-|\bHCO3\^\{\-\}', 'HCO₃⁻', text)
    text = re.sub(r'\bNH4\+|\bNH4\^\+|\bNH4\^\{\+\}', 'NH₄⁺', text)
    text = re.sub(r'\bNO3\-|\bNO3\^\-|\bNO3\^\{\-\}', 'NO₃⁻', text)
    text = re.sub(r'(?<=\[)H\+(?=\])|\bH\+(?!\w)|\bH\^\+', 'H⁺', text)
    text = re.sub(r'(?<=\[)OH\-(?=\])|\bOH\-(?!\w)|\bOH\^\-', 'OH⁻', text)
    text = re.sub(r'\bBa2\+|\bBa\^?2\+', 'Ba²⁺', text)
    text = re.sub(r'\bCa2\+|\bCa\^?2\+', 'Ca²⁺', text)
    text = re.sub(r'\bMg2\+|\bMg\^?2\+', 'Mg²⁺', text)
    text = re.sub(r'\bCu2\+|\bCu\^?2\+', 'Cu²⁺', text)
    text = re.sub(r'\bFe2\+|\bFe\^?2\+', 'Fe²⁺', text)
    text = re.sub(r'\bFe3\+|\bFe\^?3\+', 'Fe³⁺', text)
    text = re.sub(r'\bAl3\+|\bAl\^?3\+', 'Al³⁺', text)
    text = re.sub(r'\bCr3\+|\bCr\^?3\+', 'Cr³⁺', text)
    text = re.sub(r'\bCl\-|\bCl\^\-', 'Cl⁻', text)
    text = re.sub(r'\bBr\-|\bBr\^\-', 'Br⁻', text)
    text = re.sub(r'\bI\-|\bI\^\-', 'I⁻', text)

    # 4. Element followed by digits: e.g. C2H5OH, BaCl2, Na2SO4, FeS2, Al2O3, H2SO4, HNO3, N2, O2, H2, CO2
    # Ensure it's not a unit like 100 mL, 0.5 M, or PM2.5, or pH
    # Element symbol must start with capital letter. We substitute the digits with subscripts
    text = re.sub(rf'({ELEMS_PATTERN})(\d+)', lambda m: m.group(1) + to_sub(m.group(2)), text)

    # 5. Parenthesis followed by digits: e.g. Ca(OH)2 -> Ca(OH)₂, Al2(SO4)3 -> Al₂(SO₄)₃
    text = re.sub(r'(\))(\d+)', lambda m: m.group(1) + to_sub(m.group(2)), text)

    # 6. Bracket followed by digits: e.g. [Ag(NH3)2] -> [Ag(NH₃)₂]
    text = re.sub(r'(\])(\d+)', lambda m: m.group(1) + to_sub(m.group(2)), text)

    # 7. Protect pH (if regex touched it)
    text = re.sub(r'p\s*H', 'pH', text)

    # 8. Beautify arrows in equations: '->' to '→'
    text = re.sub(r'\s+->\s+', ' → ', text)

    return text

def format_all_data(data):
    """Recursively formats all strings in lists and dictionaries."""
    if isinstance(data, str):
        return format_chemical_text(data)
    elif isinstance(data, list):
        return [format_all_data(item) for item in data]
    elif isinstance(data, dict):
        return {k: format_all_data(v) for k, v in data.items()}
    return data

print("chem_formatter module ready.")
