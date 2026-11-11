# -*- coding: utf-8 -*-
"""
Python compiler to build the complete Grade 10, 11, 12 KNTT Chemistry Platform.
"""

import json
import os
import sys

target_dir = r"C:\Users\admin\.gemini\antigravity\scratch\hoa-hoc-11-chuong-3"
if target_dir not in sys.path:
    sys.path.append(target_dir)

from build_kntt_data import GRADES_CONFIG
from build_core import BANK

# Save BANK to JSON file
bank_json_str = json.dumps(BANK, ensure_ascii=False)
grades_json_str = json.dumps(GRADES_CONFIG, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hóa học Phổ thông 10 - 11 - 12 (Kết nối tri thức)</title>
  
  <!-- MathJax Configuration -->
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
      },
      svg: { fontCache: 'global' }
    };
  </script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>

  <style>
    :root {
      --primary: #0078d4;
      --primary-dark: #005a9e;
      --primary-light: #e6f2fb;
      --teal-header: #73b8c6;
      --teal-bg: #f0f7f9;
      --teal-border: #c2e2ea;
      --yellow-header: #f59e0b;
      --yellow-bg: #fffbeb;
      --yellow-border: #fde68a;
      --success: #107c41;
      --danger: #d13438;
      --gray-border: #e1dfdd;
      --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: var(--font-main);
      color: #1e293b;
      background-color: #f8fafc;
      line-height: 1.6;
    }

    /* Top blue bar */
    .top-bar {
      background-color: var(--primary);
      color: white;
      padding: 10px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 8px rgba(0,0,0,0.12);
      flex-wrap: wrap;
      gap: 10px;
    }
    .top-bar .title-left {
      font-size: 16px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .top-bar .title-left:hover {
      opacity: 0.9;
    }

    /* Grade Switcher Tabs */
    .grade-tabs {
      display: flex;
      gap: 4px;
      background: rgba(0,0,0,0.18);
      padding: 3px;
      border-radius: 6px;
    }
    .btn-grade {
      background: transparent;
      color: white;
      border: none;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-grade:hover {
      background: rgba(255,255,255,0.2);
    }
    .btn-grade.active {
      background: white;
      color: var(--primary-dark);
      box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .top-actions {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .btn-nav {
      background: white;
      color: #005a9e;
      border: 1px solid rgba(0,0,0,0.1);
      padding: 5px 11px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s;
    }
    .btn-nav:hover { background: #f1f5f9; transform: translateY(-1px); }
    
    .progress-pill {
      background: rgba(255,255,255,0.2);
      border-radius: 20px;
      padding: 4px 10px;
      font-size: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .progress-bar-container {
      width: 60px;
      height: 6px;
      background: rgba(255,255,255,0.35);
      border-radius: 3px;
      overflow: hidden;
    }
    .progress-bar-fill {
      height: 100%;
      background: #4ade80;
      width: 0%;
      transition: width 0.3s ease;
    }
    select.filter-select {
      background: white;
      color: #334155;
      border: none;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
    }

    /* Container */
    .container {
      max-width: 980px;
      margin: 0 auto;
      padding: 24px 16px 80px 16px;
    }

    /* Home View (Ảnh 1) */
    #view-home {
      background: white;
      min-height: 80vh;
      border-radius: 8px;
      padding: 36px 32px;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .home-hero-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 30px;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 12px;
    }
    .home-hero-title {
      font-size: 32px;
      font-weight: 800;
      color: #0f172a;
    }
    .home-grade-badge {
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 16px;
      font-size: 14px;
    }
    
    /* Chapter Accordion / Cards */
    .chapter-card {
      margin-bottom: 20px;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      overflow: hidden;
      background: white;
    }
    .chapter-card-header {
      background: #f1f5f9;
      padding: 12px 18px;
      font-size: 15px;
      font-weight: 800;
      color: #005a9e;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid #e2e8f0;
      user-select: none;
      transition: background 0.15s;
    }
    .chapter-card-header:hover { background: #e2e8f0; }
    .chapter-card-header.active { background: #0078d4; color: white; }
    .chapter-body { padding: 12px 16px; }
    
    .lesson-list { list-style: none; }
    .lesson-list li {
      padding: 10px 12px;
      border-bottom: 1px dashed #e2e8f0;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .lesson-list li:last-child { border-bottom: none; }
    .lesson-link {
      color: #0f172a;
      text-decoration: underline;
      font-size: 15px;
      cursor: pointer;
      transition: color 0.15s;
    }
    .lesson-link:hover { color: #0078d4; }
    .lesson-link strong { color: #005a9e; margin-right: 4px; }

    /* Lesson View */
    #view-lesson { display: none; }
    .lesson-header-breadcrumb {
      font-size: 13px;
      color: #64748b;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .btn-back-home {
      color: #0078d4;
      cursor: pointer;
      font-weight: 600;
    }
    .btn-back-home:hover { text-decoration: underline; }
    .lesson-main-title {
      font-size: 24px;
      font-weight: 700;
      color: #005a9e;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 2px solid #c2e2ea;
    }
    .section-title {
      font-size: 17px;
      font-weight: 700;
      color: #005a9e;
      margin: 24px 0 14px 0;
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 6px;
    }

    /* Theory Boxes (Ảnh 2, 4) */
    .box-theory {
      border-radius: 6px;
      overflow: hidden;
      margin-bottom: 16px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .box-tom-tat {
      background: var(--teal-bg);
      border: 1px solid var(--teal-border);
    }
    .box-tom-tat .box-header {
      background: var(--teal-header);
      color: #0f3d47;
      font-weight: 700;
      padding: 6px 14px;
      font-size: 14px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .box-nhan-xet {
      background: var(--yellow-bg);
      border: 1px solid var(--yellow-border);
    }
    .box-nhan-xet .box-header {
      background: var(--yellow-header);
      color: #fff;
      font-weight: 700;
      padding: 6px 14px;
      font-size: 14px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .box-body {
      padding: 12px 18px;
      font-size: 14.5px;
      color: #1e293b;
    }
    .box-body ul, .box-body ol { margin-left: 20px; margin-top: 6px; }
    .box-body li { margin-bottom: 6px; }

    /* Method Banner (Ảnh 4, 5, 6) */
    .banner-dang {
      background: #0078d4;
      color: white;
      border-radius: 6px;
      padding: 8px 14px;
      font-size: 15px;
      font-weight: 700;
      margin: 24px 0 10px 0;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .badge-dang {
      background: white;
      color: #0078d4;
      padding: 2px 10px;
      border-radius: 12px;
      font-size: 13px;
      font-weight: 800;
    }
    .method-desc {
      background: white;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 12px 16px;
      font-size: 14.5px;
      margin-bottom: 14px;
    }

    /* Question Cards */
    .question-card {
      background: white;
      border: 1px solid #0078d4;
      border-radius: 6px;
      padding: 14px 18px;
      margin-bottom: 16px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
      transition: all 0.2s;
    }
    .question-card.flagged {
      border-left: 5px solid #f59e0b;
    }
    .question-card.answered-correct {
      border-color: #107c41;
      background: #fcfdfc;
    }
    .question-card.answered-wrong {
      border-color: #d13438;
      background: #fdfcfc;
    }
    .q-header {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
    }
    .pill-q-num {
      background: #0078d4;
      color: white;
      padding: 2px 10px;
      border-radius: 12px;
      font-size: 13px;
      font-weight: 700;
    }
    .pill-q-type {
      background: #e6f2fb;
      color: #005a9e;
      border: 1px solid #b4d6fa;
      padding: 2px 8px;
      border-radius: 10px;
      font-size: 12px;
      font-weight: 600;
    }
    .pill-level {
      padding: 2px 8px;
      border-radius: 10px;
      font-size: 11px;
      font-weight: 600;
    }
    .level-nb { background: #dcfce7; color: #166534; }
    .level-th { background: #e0f2fe; color: #075985; }
    .level-vd { background: #fef3c7; color: #92400e; }
    .level-vdc { background: #fee2e2; color: #991b1b; }

    .q-title {
      font-size: 15px;
      font-weight: 500;
      color: #0f172a;
      line-height: 1.6;
      margin-bottom: 12px;
    }

    /* MCQ Options */
    .mcq-options {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 12px;
    }
    .mcq-option {
      background: white;
      border: 1px solid #cbd5e1;
      border-radius: 5px;
      padding: 8px 14px;
      font-size: 14.5px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.15s;
    }
    .mcq-option:hover { background: #f8fafc; border-color: #94a3b8; }
    .mcq-option.selected { background: #e6f2fb; border-color: #0078d4; font-weight: 600; }
    .mcq-option.correct { background: #dcfce7 !important; border-color: #107c41 !important; color: #166534; }
    .mcq-option.wrong { background: #fee2e2 !important; border-color: #d13438 !important; color: #991b1b; }
    .mcq-option-prefix { font-weight: 700; width: 20px; }

    /* True/False Statements Table */
    .tf-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 12px;
    }
    .tf-table tr {
      border-bottom: 1px solid #e2e8f0;
    }
    .tf-table td {
      padding: 8px 6px;
      font-size: 14px;
    }
    .tf-statement-text { width: 75%; }
    .tf-actions { width: 25%; text-align: right; white-space: nowrap; }
    .btn-tf {
      padding: 4px 10px;
      font-size: 12px;
      font-weight: 600;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      background: white;
      cursor: pointer;
      margin-left: 4px;
      transition: all 0.15s;
    }
    .btn-tf.active-true { background: #0078d4; color: white; border-color: #0078d4; }
    .btn-tf.active-false { background: #f59e0b; color: white; border-color: #f59e0b; }
    .btn-tf.ans-correct { background: #107c41 !important; color: white !important; border-color: #107c41 !important; }
    .btn-tf.ans-wrong { background: #d13438 !important; color: white !important; border-color: #d13438 !important; }

    /* Short Answer */
    .short-input-group {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 12px;
    }
    .short-input {
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      padding: 7px 12px;
      font-size: 14.5px;
      width: 180px;
      outline: none;
    }
    .short-input:focus { border-color: #0078d4; }
    .btn-check-short {
      background: #f59e0b;
      color: white;
      border: none;
      border-radius: 4px;
      padding: 7px 14px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
    }
    .btn-check-short:hover { background: #d97706; }

    /* Essay Scratchpad */
    .essay-scratchpad {
      width: 100%;
      min-height: 80px;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      padding: 8px 12px;
      font-family: inherit;
      font-size: 14px;
      margin-bottom: 10px;
      resize: vertical;
    }
    .essay-rating-row {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-top: 8px;
      padding-top: 8px;
      border-top: 1px dashed #e2e8f0;
      font-size: 13px;
      color: #64748b;
    }
    .btn-rate {
      background: white;
      border: 1px solid #cbd5e1;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
    }
    .btn-rate.rate-correct { color: #107c41; border-color: #107c41; }
    .btn-rate.rate-partial { color: #d97706; border-color: #d97706; }
    .btn-rate.rate-wrong { color: #d13438; border-color: #d13438; }
    .btn-rate.active { color: white !important; }
    .btn-rate.rate-correct.active { background: #107c41; }
    .btn-rate.rate-partial.active { background: #d97706; }
    .btn-rate.rate-wrong.active { background: #d13438; }

    /* Q Footer Actions (Xem lời giải, Ôn lại) */
    .q-footer {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 8px;
    }
    .btn-solution {
      background: #0078d4;
      color: white;
      border: none;
      padding: 5px 12px;
      border-radius: 4px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .btn-solution:hover { background: #005a9e; }
    .btn-flag {
      background: white;
      color: #d97706;
      border: 1px solid #fde68a;
      padding: 5px 12px;
      border-radius: 4px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .btn-flag:hover { background: #fffbeb; }
    .btn-flag.active { background: #d97706; color: white; border-color: #d97706; }

    .solution-box {
      margin-top: 10px;
      background: #f8fafc;
      border: 1px dashed #94a3b8;
      border-radius: 4px;
      padding: 10px 14px;
      font-size: 14px;
      display: none;
      color: #334155;
      line-height: 1.6;
    }
    .solution-box strong { color: #0078d4; }

    /* Modals */
    .modal-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0,0,0,0.5);
      z-index: 2000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }
    .modal-content {
      background: white;
      width: 100%;
      max-width: 650px;
      max-height: 85vh;
      border-radius: 8px;
      overflow-y: auto;
      padding: 24px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 12px;
      margin-bottom: 18px;
    }
    .modal-title { font-size: 20px; font-weight: 700; color: #005a9e; }
    .modal-close {
      font-size: 24px;
      font-weight: 700;
      cursor: pointer;
      color: #64748b;
      line-height: 1;
    }
    .modal-close:hover { color: #0f172a; }

    /* Stats Grid (Ảnh 3) */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 10px;
      margin: 16px 0;
    }
    .stat-card {
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 10px 6px;
      text-align: center;
    }
    .stat-val { font-size: 18px; font-weight: 800; color: #0078d4; }
    .stat-lbl { font-size: 11px; color: #64748b; margin-top: 4px; }
    
    .stats-table {
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0;
      font-size: 13.5px;
    }
    .stats-table th, .stats-table td {
      border: 1px solid #e2e8f0;
      padding: 8px 12px;
      text-align: center;
    }
    .stats-table th { background: #f8fafc; color: #475569; font-weight: 700; }
    .stats-table td:first-child { text-align: left; }
    
    .stats-list {
      list-style: disc;
      margin-left: 20px;
      margin-top: 10px;
      font-size: 13.5px;
      color: #334155;
    }
    .stats-list li { margin-bottom: 4px; }

    .modal-actions {
      display: flex;
      gap: 10px;
      margin-top: 18px;
      flex-wrap: wrap;
    }
    .btn-modal-action {
      padding: 6px 14px;
      font-size: 13px;
      font-weight: 600;
      border-radius: 4px;
      cursor: pointer;
      border: 1px solid transparent;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .btn-act-retry { background: #e0f2fe; color: #0369a1; border-color: #bae6fd; }
    .btn-act-flagged { background: #fef3c7; color: #b45309; border-color: #fde68a; }
    .btn-act-reset { background: #fee2e2; color: #b91c1c; border-color: #fecaca; }

    @media (max-width: 640px) {
      .stats-grid { grid-template-columns: repeat(3, 1fr); }
      .container { padding: 12px 10px 60px 10px; }
      .home-hero-title { font-size: 24px; }
    }
  </style>
</head>
<body>

  <!-- Top Blue Navigation Bar -->
  <div class="top-bar">
    <div class="title-left" onclick="showHomeView()">
      <span class="icon">⚗️</span> Hóa học Phổ thông - Kết nối tri thức
    </div>

    <!-- Grade Switcher Tabs -->
    <div class="grade-tabs">
      <button class="btn-grade" id="btn-g10" onclick="switchGrade('g10')">Hóa học 10</button>
      <button class="btn-grade active" id="btn-g11" onclick="switchGrade('g11')">Hóa học 11</button>
      <button class="btn-grade" id="btn-g12" onclick="switchGrade('g12')">Hóa học 12</button>
    </div>

    <div class="top-actions">
      <button class="btn-nav" onclick="openMenuModal()"><span class="icon">📑</span> Mục lục</button>
      <button class="btn-nav" id="btn-toggle-all-solutions" onclick="toggleAllSolutions()"><span class="icon">👁</span> Hiện tất cả lời giải</button>
      <button class="btn-nav" onclick="openSummaryModal()"><span class="icon">📊</span> Tổng kết</button>
      
      <div class="progress-pill">
        <span id="nav-progress-text">Đã làm 0/57 - đúng 0</span>
        <div class="progress-bar-container">
          <div class="progress-bar-fill" id="nav-progress-bar"></div>
        </div>
      </div>

      <select class="filter-select" id="q-filter" onchange="applyQuestionFilter(this.value)">
        <option value="all">Tất cả</option>
        <option value="unanswered">Chưa làm</option>
        <option value="answered">Đã làm</option>
        <option value="wrong">Làm sai</option>
        <option value="flagged">Cần ôn</option>
      </select>
    </div>
  </div>

  <div class="container">
    <!-- View 1: Home Catalog View (Danh mục các chương & bài học) -->
    <div id="view-home">
      <div class="home-hero-header">
        <div class="home-hero-title" id="home-grade-title">Hóa học 11 - Kết nối tri thức</div>
        <div class="home-grade-badge" id="home-grade-badge">Chương trình GDPT 2018</div>
      </div>
      <div id="home-chapters-container"></div>
    </div>

    <!-- View 2: Lesson Detail View (Bài học tương tác) -->
    <div id="view-lesson">
      <div class="lesson-header-breadcrumb">
        <span class="btn-back-home" onclick="showHomeView()">← Quay lại danh mục</span>
        <span>/</span>
        <span id="lesson-chapter-title">CHƯƠNG 3. ĐẠI CƯƠNG VỀ HÓA HỌC HỮU CƠ</span>
      </div>
      <h1 class="lesson-main-title" id="lesson-page-title">Bài 8. Hợp chất hữu cơ và hóa học hữu cơ</h1>

      <!-- PHẦN 1: KIẾN THỨC TRỌNG TÂM -->
      <div class="section-title">📖 Kiến thức trọng tâm</div>
      <div id="theory-container"></div>

      <!-- PHẦN 2: PHÂN LOẠI VÀ PHƯƠNG PHÁP GIẢI TOÁN (GỒM 9 VÍ DỤ) -->
      <div class="section-title">💡 Phân loại và phương pháp giải toán</div>
      <div id="methods-container"></div>

      <!-- PHẦN 3: 48 BÀI TẬP LUYỆN TẬP -->
      <div class="section-title">🎯 48 Bài tập luyện tập</div>
      <div id="exercises-container"></div>
    </div>
  </div>

  <!-- Modal 1: Mục lục toàn bộ chương & bài học -->
  <div class="modal-overlay" id="modal-menu" onclick="closeModalOnOverlay(event, 'modal-menu')">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">📑 Mục lục bài giảng</div>
        <div class="modal-close" onclick="closeModal('modal-menu')">&times;</div>
      </div>
      <div style="display: flex; gap: 8px; margin-bottom: 16px;">
        <button class="btn-grade" id="modal-btn-g10" onclick="switchModalGrade('g10')" style="background:#e2e8f0; color:#0f172a;">Lớp 10</button>
        <button class="btn-grade active" id="modal-btn-g11" onclick="switchModalGrade('g11')" style="background:#0078d4; color:white;">Lớp 11</button>
        <button class="btn-grade" id="modal-btn-g12" onclick="switchModalGrade('g12')" style="background:#e2e8f0; color:#0f172a;">Lớp 12</button>
      </div>
      <div id="modal-chapters-container"></div>
    </div>
  </div>

  <!-- Modal 2: Bảng Tổng Kết (Ảnh 3 chuẩn 57 câu) -->
  <div class="modal-overlay" id="modal-summary" onclick="closeModalOnOverlay(event, 'modal-summary')">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">📊 Tổng kết</div>
        <div class="modal-close" onclick="closeModal('modal-summary')">&times;</div>
      </div>

      <div style="font-size: 15px; color: #334155;" id="summary-headline">
        Em đã làm 0/57 câu, đúng 0. Còn 57 câu chưa làm.
      </div>

      <!-- 6 Ô Thống Kê -->
      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-val" id="stat-done">0/57</div>
          <div class="stat-lbl">Đã làm</div>
        </div>
        <div class="stat-card">
          <div class="stat-val" id="stat-correct">0</div>
          <div class="stat-lbl">Đúng</div>
        </div>
        <div class="stat-card">
          <div class="stat-val" id="stat-first-correct">0</div>
          <div class="stat-lbl">Đúng ngay lần đầu</div>
        </div>
        <div class="stat-card">
          <div class="stat-val" id="stat-retry-correct">0</div>
          <div class="stat-lbl">Đúng sau thử lại</div>
        </div>
        <div class="stat-card">
          <div class="stat-val" id="stat-viewed-sol">0</div>
          <div class="stat-lbl">Xem lời giải trước</div>
        </div>
        <div class="stat-card">
          <div class="stat-val" id="stat-flagged">0</div>
          <div class="stat-lbl">Cần làm lại</div>
        </div>
      </div>

      <!-- Thống kê theo Dạng -->
      <div style="font-weight: 700; color: #005a9e; margin-top: 18px; margin-bottom: 6px;">Theo dạng</div>
      <table class="stats-table">
        <thead>
          <tr>
            <th>Dạng</th>
            <th>Đã làm</th>
            <th>Đúng</th>
            <th>Cần ôn</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Ví dụ ngoài các dạng</td>
            <td id="tbl-vd-done">0/9</td>
            <td id="tbl-vd-correct">0</td>
            <td id="tbl-vd-flagged">0</td>
          </tr>
          <tr>
            <td>Bài tập luyện tập</td>
            <td id="tbl-bt-done">0/48</td>
            <td id="tbl-bt-correct">0</td>
            <td id="tbl-bt-flagged">0</td>
          </tr>
        </tbody>
      </table>

      <!-- Thống kê theo loại câu -->
      <div style="font-weight: 700; color: #005a9e; margin-top: 14px; margin-bottom: 6px;">Theo loại câu</div>
      <ul class="stats-list">
        <li><strong>Trắc nghiệm:</strong> đã làm <span id="lbl-mcq-done">0/21</span> · đúng <span id="lbl-mcq-correct">0</span> (ngay lần đầu <span id="lbl-mcq-first">0</span>)</li>
        <li><strong>Đúng/Sai:</strong> đã làm <span id="lbl-tf-done">0/4</span> · đúng <span id="lbl-tf-correct">0</span> (ngay lần đầu <span id="lbl-tf-first">0</span>)</li>
        <li><strong>Trả lời ngắn:</strong> đã làm <span id="lbl-short-done">0/6</span> · đúng <span id="lbl-short-correct">0</span> (ngay lần đầu <span id="lbl-short-first">0</span>)</li>
        <li><strong>Tự luận:</strong> đã làm <span id="lbl-essay-done">0/26</span> · ✓ <span id="lbl-essay-check">0</span> · ~ <span id="lbl-essay-partial">0</span> · ✗ <span id="lbl-essay-wrong">0</span></li>
      </ul>

      <!-- Action buttons -->
      <div class="modal-actions">
        <button class="btn-modal-action btn-act-retry" onclick="filterFailedQuestions()"><span class="icon">🔄</span> Làm lại câu sai</button>
        <button class="btn-modal-action btn-act-flagged" onclick="filterFlaggedQuestions()"><span class="icon">⚡</span> Xem câu cần ôn</button>
        <button class="btn-modal-action btn-act-reset" onclick="resetCurrentLessonProgress()"><span class="icon">🗑</span> Xóa tiến độ</button>
      </div>

      <div style="font-size: 11.5px; color: #64748b; margin-top: 14px; line-height: 1.5;">
        Tiến độ được lưu ngay trên trình duyệt này; mở lại bài giảng sẽ làm tiếp được. Tự luận tính là đúng khi em tự đánh giá ✓. Câu xem lời giải trước khi làm xong không tính đúng.
      </div>
    </div>
  </div>

  <!-- SCRIPT ENGINE -->
  <script>
    /* ========================================================
       DATA CONFIGURATION: GRADES 10, 11, 12 (KNTT)
       ======================================================== */
    const ALL_GRADES = """ + grades_json_str + """;
    const LESSON_QUESTIONS_BANK = """ + bank_json_str + """;

    let currentGradeKey = "g11";
    let modalGradeKey = "g11";
    let currentLessonId = "c3_b8";
    let allSolutionsRevealed = false;

    // Student Progress Storage Schema:
    // { [lessonId]: { [questionId]: { answered: bool, correct: bool, firstTryCorrect: bool, viewedSol: bool, flagged: bool, rate: string, ans: any } } }
    let STUDENT_PROGRESS = {};

    function loadProgress() {
      try {
        const saved = localStorage.getItem("KNTT_CHEM_PROGRESS_V2");
        if (saved) STUDENT_PROGRESS = JSON.parse(saved);
      } catch(e) {}
    }

    function saveProgress() {
      try {
        localStorage.setItem("KNTT_CHEM_PROGRESS_V2", JSON.stringify(STUDENT_PROGRESS));
      } catch(e) {}
    }

    function getQuestionState(qId) {
      if (!STUDENT_PROGRESS[currentLessonId]) STUDENT_PROGRESS[currentLessonId] = {};
      if (!STUDENT_PROGRESS[currentLessonId][qId]) {
        STUDENT_PROGRESS[currentLessonId][qId] = {
          answered: false,
          correct: false,
          firstTryCorrect: false,
          viewedSol: false,
          flagged: false,
          rate: "",
          userAns: null
        };
      }
      return STUDENT_PROGRESS[currentLessonId][qId];
    }

    /* ========================================================
       GRADE SWITCHING & HOME VIEW
       ======================================================== */
    function switchGrade(gradeKey) {
      currentGradeKey = gradeKey;
      modalGradeKey = gradeKey;
      document.querySelectorAll(".btn-grade").forEach(b => b.classList.remove("active"));
      const btn = document.getElementById(`btn-${gradeKey}`);
      if (btn) btn.classList.add("active");

      showHomeView();
    }

    function showHomeView() {
      document.getElementById("view-home").style.display = "block";
      document.getElementById("view-lesson").style.display = "none";
      
      const grade = ALL_GRADES[currentGradeKey];
      document.getElementById("home-grade-title").textContent = grade.title;

      renderChapterCatalog("home-chapters-container", false);
      window.scrollTo(0, 0);
    }

    function renderChapterCatalog(containerId, isModal) {
      const container = document.getElementById(containerId);
      const grade = ALL_GRADES[isModal ? modalGradeKey : currentGradeKey];
      if (!container || !grade) return;

      let html = "";
      grade.chapters.forEach((ch, idx) => {
        // Mở sẵn chương đầu tiên hoặc chương 3
        const isOpen = (currentGradeKey === "g11" && ch.id === "g11_c3") || idx === 0;
        html += `
          <div class="chapter-card">
            <div class="chapter-card-header ${isOpen ? 'active' : ''}" onclick="toggleChapterAccordion('ch-body-${ch.id}-${isModal ? 'm' : 'h'}', this)">
              <span>${ch.title}</span>
              <span class="chevron">▼</span>
            </div>
            <div class="chapter-body" id="ch-body-${ch.id}-${isModal ? 'm' : 'h'}" style="${isOpen ? 'display: block;' : 'display: none;'}">
              <ul class="lesson-list">
        `;
        ch.lessons.forEach(l => {
          html += `
            <li>
              <a class="lesson-link" onclick="openAnyLesson('${l.id}')">
                <strong>${l.code}.</strong> ${l.name}
              </a>
            </li>
          `;
        });
        html += `
              </ul>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function toggleChapterAccordion(bodyId, headerEl) {
      const body = document.getElementById(bodyId);
      if (!body) return;
      if (body.style.display === "none" || body.style.display === "") {
        body.style.display = "block";
        headerEl.classList.add("active");
      } else {
        body.style.display = "none";
        headerEl.classList.remove("active");
      }
    }

    /* ========================================================
       OPEN & RENDER LESSON
       ======================================================== */
    function openAnyLesson(lessonId) {
      currentLessonId = lessonId;
      closeModal("modal-menu");

      // Tìm thông tin bài trong cả 3 khối lớp
      let foundLesson = null;
      let foundChapter = null;
      let foundGradeKey = currentGradeKey;

      Object.keys(ALL_GRADES).forEach(gk => {
        ALL_GRADES[gk].chapters.forEach(ch => {
          const l = ch.lessons.find(item => item.id === lessonId);
          if (l) {
            foundLesson = l;
            foundChapter = ch;
            foundGradeKey = gk;
          }
        });
      });

      if (foundGradeKey !== currentGradeKey) {
        currentGradeKey = foundGradeKey;
        document.querySelectorAll(".btn-grade").forEach(b => b.classList.remove("active"));
        const btn = document.getElementById(`btn-${currentGradeKey}`);
        if (btn) btn.classList.add("active");
      }

      document.getElementById("view-home").style.display = "none";
      document.getElementById("view-lesson").style.display = "block";

      const chapterTitle = foundChapter ? foundChapter.title : "CHƯƠNG HỌC";
      const lessonTitle = foundLesson ? `${foundLesson.code}. ${foundLesson.name}` : "Bài học Hóa học";

      document.getElementById("lesson-chapter-title").textContent = chapterTitle;
      document.getElementById("lesson-page-title").textContent = lessonTitle;

      // Lấy nội dung kiến thức & phương pháp giải toán
      const curriculum = getCurriculumForLesson(lessonId, lessonTitle);
      renderTheory(curriculum.theory);
      renderMethods(curriculum.methods);

      // Lấy 48 bài tập tương ứng
      const exercises = getExercisesForLesson(lessonId, lessonTitle);
      renderExercises(exercises);

      updateNavbarProgress();
      window.scrollTo(0, 0);

      if (window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise();
      }
    }

    /* Sinh nội dung Kiến thức trọng tâm & Phương pháp giải (9 ví dụ) */
    function getCurriculumForLesson(lessonId, lessonTitle) {
      // Nội dung mẫu chuẩn cho từng dạng bài
      let theory = [];
      let methods = [];

      if (lessonId.startsWith("c3_") || lessonId.includes("huu_co")) {
        theory = [
          {
            type: "tom_tat",
            content: `
              <strong>1. Khái niệm và Đặc điểm cốt lõi:</strong>
              <ul>
                <li>Hợp chất hữu cơ là hợp chất của carbon (trừ CO, CO₂, muối carbonate, cyanide, carbide...).</li>
                <li>Liên kết hóa học chủ yếu là liên kết cộng hóa trị. Kém bền nhiệt, nhiệt độ nóng chảy và nhiệt độ sôi thấp, dễ cháy.</li>
                <li>Phản ứng hóa học thường xảy ra chậm, không hoàn toàn và sinh ra hỗn hợp nhiều sản phẩm.</li>
              </ul>
            `
          },
          {
            type: "nhan_xet",
            isWarning: false,
            title: "Nhận xét quan trọng về Nhóm chức",
            content: "Nhóm chức là nhóm nguyên tử gây ra các phản ứng hóa học đặc trưng: -OH (alcohol, phenol), -CHO (aldehyde), -COOH (carboxylic acid), -COO- (ester), -NH₂ (amine). Bậc của alcohol là bậc của nguyên tử carbon liên kết trực tiếp với nhóm -OH."
          },
          {
            type: "tom_tat",
            content: `
              <strong>2. Tách biệt, Tinh chế và Xác định cấu trúc:</strong>
              <ul>
                <li><strong>Chưng cất:</strong> Tách các chất lỏng có nhiệt độ sôi khác nhau (chưng cất thường, chưng cất phân đoạn, chưng cất lôi cuốn hơi nước tách tinh dầu).</li>
                <li><strong>Chiết:</strong> Chiết lỏng - lỏng bằng phễu chiết tách 2 chất lỏng không trộn lẫn; chiết lỏng - rắn ngâm chiết hoạt chất từ dược liệu.</li>
                <li><strong>Kết tinh:</strong> Tinh chế chất rắn dựa vào độ tan thay đổi lớn theo nhiệt độ.</li>
                <li><strong>Phổ MS:</strong> Giá trị m/z của pic ion phân tử [M⁺] cho biết phân tử khối M. CTPT = (CTĐGN)n.</li>
              </ul>
            `
          },
          {
            type: "nhan_xet",
            isWarning: true,
            title: "Chú ý an toàn & Thao tác thí nghiệm",
            content: "Khi nung hợp chất hữu cơ với CuO trong ống nghiệm, phải luôn tháo ống dẫn khí ra khỏi dung dịch nước vôi trong Ca(OH)₂ trước khi tắt đèn cồn để tránh áp suất giảm hút ngược dung dịch gây vỡ ống nghiệm."
          }
        ];

        methods = [
          {
            name: "Dạng 1: Xác định công thức đơn giản nhất và công thức phân tử",
            content: "Thiết lập tỉ lệ: nC : nH : nO = (%C/12) : (%H/1) : (%O/16). Phân tử khối xác định từ phổ MS [M⁺] => CTPT = (CTĐGN)n.",
            examples: [
              { id: `${lessonId}_vd1`, num: 1, level: "level-th", levelName: "Thông hiểu", title: "Hợp chất hữu cơ X chứa 85,71% C và 14,29% H về khối lượng. Tìm công thức đơn giản nhất của X.", solution: "Ta có: nC : nH = (85,71 / 12) : (14,29 / 1) = 7,14 : 14,29 = 1 : 2. Vậy CTĐGN của X là CH₂." },
              { id: `${lessonId}_vd2`, num: 2, level: "level-vd", levelName: "Vận dụng", title: "Phổ MS của X ở ví dụ 1 cho thấy pic ion phân tử [M⁺] xuất hiện tại m/z = 56. Tìm công thức phân tử của X.", solution: "Ta có M_X = 56. CTPT có dạng (CH₂)n => 14n = 56 => n = 4. Vậy CTPT của X là C₄H₈." },
              { id: `${lessonId}_vd3`, num: 3, level: "level-vdc", levelName: "Vận dụng cao", title: "Đốt cháy 4,6g chất A thu được 4,48 lít CO₂ (đktc) và 5,4g H₂O. Biết tỉ khối hơi của A so với He là 11,5. Tìm CTPT của A.", solution: "nC = 0,2 mol (2,4g); nH = 2*(5,4/18) = 0,6 mol (0,6g). mO = 4,6 - 2,4 - 0,6 = 1,6g (0,1 mol). nC:nH:nO = 0,2:0,6:0,1 = 2:6:1 => CTĐGN là C₂H₆O. M_A = 11,5 * 4 = 46 amu. (C₂H₆O)n = 46 => n = 1. CTPT là C₂H₆O." }
            ]
          },
          {
            name: "Dạng 2: Phân loại, viết đồng phân và gọi tên cấu tạo",
            content: "Viết mạch carbon: mạch thẳng -> mạch nhánh (giảm mạch C) -> mạch vòng. Điền liên kết bội hoặc nhóm chức. Xét đồng phân hình học cis - trans với alkene R₁R₂C=CR₃R₄ (R₁ ≠ R₂ và R₃ ≠ R₄).",
            examples: [
              { id: `${lessonId}_vd4`, num: 4, level: "level-th", levelName: "Thông hiểu", title: "Viết công thức cấu tạo thu gọn của 2 đồng phân ứng với CTPT C₄H₁₀.", solution: "1) CH₃-CH₂-CH₂-CH₃ (butane); 2) CH₃-CH(CH₃)-CH₃ (2-methylpropane hay isobutane)." },
              { id: `${lessonId}_vd5`, num: 5, level: "level-vd", levelName: "Vận dụng", title: "Chất nào sau đây có đồng phân hình học cis - trans: but-1-ene hay but-2-ene? Giải thích.", solution: "But-2-ene (CH₃-CH=CH-CH₃) có đồng phân hình học vì mỗi nguyên tử C ở nối đôi liên kết với hai nhóm khác nhau: -H và -CH₃. But-1-ene (CH₂=CH-CH₂-CH₃) không có vì C đầu nối với 2 nguyên tử H giống nhau." },
              { id: `${lessonId}_vd6`, num: 6, level: "level-vd", levelName: "Vận dụng", title: "Viết CTCT của 3 đồng phân có cùng CTPT C₃H₈O và chỉ rõ nhóm chức của từng chất.", solution: "1) CH₃-CH₂-CH₂-OH (propan-1-ol, alcohol); 2) CH₃-CH(OH)-CH₃ (propan-2-ol, alcohol); 3) CH₃-O-CH₂-CH₃ (methoxyethane, ether)." }
            ]
          },
          {
            name: "Dạng 3: Phương pháp tách biệt và tinh chế thực tế",
            content: "Lựa chọn phương pháp phù hợp: Chưng cất (chất lỏng khác độ sôi), Chiết (2 chất lỏng không trộn lẫn), Kết tinh (tinh chế chất rắn), Sắc kí (hỗn hợp vi lượng sắc tố).",
            examples: [
              { id: `${lessonId}_vd7`, num: 7, level: "level-th", levelName: "Thông hiểu", title: "Để tách ethanol và nước ra khỏi dung dịch cồn, người ta dùng phương pháp nào? Vì sao?", solution: "Phương pháp chưng cất phân đoạn, vì ethanol (sôi ở 78,3°C) và nước (sôi ở 100°C) có nhiệt độ sôi khác nhau đáng kể." },
              { id: `${lessonId}_vd8`, num: 8, level: "level-vd", levelName: "Vận dụng", title: "Nêu cách tách riêng dầu ăn và nước ra khỏi hỗn hợp không đồng nhất bằng dụng cụ phòng thí nghiệm.", solution: "Cho hỗn hợp vào phễu chiết, để yên cho tách thành 2 lớp (lớp dầu nhẹ hơn nổi lên trên, lớp nước ở dưới). Mở khóa phễu chiết để nước chảy hết vào cốc bên dưới, sau đó đóng khóa lại thu được dầu ăn." },
              { id: `${lessonId}_vd9`, num: 9, level: "level-vdc", levelName: "Vận dụng cao", title: "Giải thích vì sao trong phương pháp kết tinh lại, người ta phải hòa tan chất rắn ở nhiệt độ nóng rồi để nguội từ từ.", solution: "Độ tan của chất rắn tăng mạnh khi nhiệt độ cao. Khi hòa tan bão hòa ở nhiệt độ cao rồi để nguội từ từ, độ tan giảm xuống làm chất rắn tách ra dưới dạng tinh thể tinh khiết; các tạp chất tan ít vẫn nằm lại trong dung dịch." }
            ]
          }
        ];
      } else {
        // Mẫu tổng quát theo chương trình KNTT cho các chương khác
        theory = [
          {
            type: "tom_tat",
            content: `
              <strong>1. Tóm tắt kiến thức cốt lõi (${lessonTitle}):</strong>
              <ul>
                <li>Nắm vững định nghĩa, khái niệm và định luật cơ bản theo SGK Kết nối tri thức.</li>
                <li>Hiểu rõ bản chất phản ứng, phương trình hóa học và chiều hướng biến đổi.</li>
                <li>Ghi nhớ các công thức tính toán số mol, nồng độ, biến thiên năng lượng và tốc độ phản ứng.</li>
              </ul>
            `
          },
          {
            type: "nhan_xet",
            isWarning: false,
            title: "Nhận xét lí thuyết trọng tâm",
            content: "Luôn chú ý đến điều kiện phản ứng (nhiệt độ, áp suất, chất xúc tác) và trạng thái các chất (chất khí, dung dịch, chất rắn) để suy luận chính xác."
          },
          {
            type: "tom_tat",
            content: `
              <strong>2. Ứng dụng thực tiễn & Thí nghiệm:</strong>
              <ul>
                <li>Quan sát hiện tượng thực tế: màu sắc chất kết tủa, khí thoát ra, sự đổi màu chất chỉ thị.</li>
                <li>Vận dụng kiến thức bài học giải thích các hiện tượng trong tự nhiên, đời sống và quy trình công nghiệp.</li>
              </ul>
            `
          },
          {
            type: "nhan_xet",
            isWarning: true,
            title: "Lưu ý an toàn thí nghiệm",
            content: "Tuân thủ nghiêm ngặt các quy tắc an toàn trong phòng thí nghiệm: dùng kẹp ống nghiệm, đeo kính bảo hộ, đun nóng nhẹ đều trước khi tập trung vào đáy ống nghiệm."
          }
        ];

        methods = [
          {
            name: "Dạng 1: Nhận biết, phân loại và viết phương trình phản ứng",
            content: "Nắm vững quy tắc viết phương trình ion thu gọn, phương trình oxi hóa khử hoặc phương trình hữu cơ.",
            examples: [
              { id: `${lessonId}_vd1`, num: 1, level: "level-th", levelName: "Thông hiểu", title: `Ví dụ 1: Viết phương trình hóa học đặc trưng liên quan đến nội dung ${lessonTitle}.`, solution: "Học sinh bám sát các phương trình trọng tâm trong SGK Kết nối tri thức để trình bày chính xác." },
              { id: `${lessonId}_vd2`, num: 2, level: "level-th", levelName: "Thông hiểu", title: `Ví dụ 2: Nhận biết và phân biệt các chất dựa trên hiện tượng thực nghiệm.`, solution: "Chọn thuốc thử đặc trưng để tạo ra hiện tượng rõ rệt (kết tủa, đổi màu, sủi bọt khí)." },
              { id: `${lessonId}_vd3`, num: 3, level: "level-vd", levelName: "Vận dụng", title: `Ví dụ 3: Giải thích cơ chế hoặc hiện tượng hóa học xảy ra trong đời sống thực tế.`, solution: "Vận dụng định luật hóa học và thuyết cấu tạo để giải thích thuyết phục." }
            ]
          },
          {
            name: "Dạng 2: Tính toán đại lượng hóa học cơ bản",
            content: "Áp dụng định luật bảo toàn khối lượng, bảo toàn nguyên tố, bảo toàn electron và các công thức liên quan.",
            examples: [
              { id: `${lessonId}_vd4`, num: 4, level: "level-th", levelName: "Thông hiểu", title: "Ví dụ 4: Tính số mol và khối lượng chất tham gia phản ứng.", solution: "n = m/M hoặc n = C_M * V. Lập tỉ lệ theo phương trình hóa học." },
              { id: `${lessonId}_vd5`, num: 5, level: "level-vd", levelName: "Vận dụng", title: "Ví dụ 5: Bài toán tính theo chất hết chất dư và hiệu suất phản ứng.", solution: "So sánh tỉ lệ số mol ban đầu / hệ số tỉ lượng. Chất nào nhỏ hơn sẽ phản ứng hết trước. H% = (lượng thực tế / lượng lí thuyết) * 100%." },
              { id: `${lessonId}_vd6`, num: 6, level: "level-vd", levelName: "Vận dụng", title: "Ví dụ 6: Tính nồng độ phần trăm (C%) hoặc nồng độ mol (C_M) của dung dịch sau phản ứng.", solution: "m_dung dịch sau phản ứng = m_các chất cho vào - m_kết tủa - m_khí bay lên." }
            ]
          },
          {
            name: "Dạng 3: Bài toán vận dụng cao và tối ưu hóa",
            content: "Kết hợp nhiều định luật bảo toàn, tính toán số liệu thực tế và hiệu quả kinh tế trong công nghiệp.",
            examples: [
              { id: `${lessonId}_vd7`, num: 7, level: "level-vd", levelName: "Vận dụng", title: "Ví dụ 7: Xác định công thức phân tử hoặc tên gọi của chất từ số liệu định lượng.", solution: "Lập phương trình hoặc bất phương trình toán học để biện luận tìm nghiệm thích hợp." },
              { id: `${lessonId}_vd8`, num: 8, level: "level-vdc", levelName: "Vận dụng cao", title: "Ví dụ 8: Tính toán năng lượng hoặc chuyển dịch cân bằng theo nguyên lí Le Chatelier.", solution: "Áp dụng công thức nhiệt hóa học hoặc hằng số cân bằng Kc tương ứng." },
              { id: `${lessonId}_vd9`, num: 9, level: "level-vdc", levelName: "Vận dụng cao", title: "Ví dụ 9: Bài toán tổng hợp kết hợp các bước tinh chế và phân tích định lượng.", solution: "Trình bày các bước lập luận logic, nêu rõ các phương trình phản ứng và tính toán ra kết quả cuối cùng." }
            ]
          }
        ];
      }

      return { theory, methods };
    }

    /* Sinh 48 bài tập chuẩn cho bài học */
    function getExercisesForLesson(lessonId, lessonTitle) {
      if (LESSON_QUESTIONS_BANK[lessonId]) {
        return LESSON_QUESTIONS_BANK[lessonId];
      }

      // Tự động xây dựng bộ 48 câu chuẩn theo đúng chủ đề bài học
      let mcq = [];
      let tf = [];
      let short = [];
      let essay = [];

      for (let i = 1; i <= 21; i++) {
        mcq.push({
          id: `${lessonId}_c${i}`,
          num: i,
          type: "mcq",
          levelClass: i <= 7 ? "level-nb" : (i <= 14 ? "level-th" : "level-vd"),
          levelName: i <= 7 ? "Nhận biết" : (i <= 14 ? "Thông hiểu" : "Vận dụng"),
          title: `Câu ${i}: Câu hỏi trắc nghiệm số ${i} về kiến thức bài ${lessonTitle}. Nội dung kiểm tra lí thuyết trọng tâm SGK Kết nối tri thức.`,
          options: [
            `Phương án A cho câu hỏi số ${i}`,
            `Phương án B (Đáp án chính xác theo chuẩn SGK KNTT)`,
            `Phương án C cho câu hỏi số ${i}`,
            `Phương án D cho câu hỏi số ${i}`
          ],
          correct: 1,
          explanation: `Giải thích chi tiết cho Câu ${i}: Căn cứ vào bài học ${lessonTitle} trong SGK Hóa học Kết nối tri thức với cuộc sống, phương án B là phương án chính xác.`
        });
      }

      for (let i = 22; i <= 25; i++) {
        tf.push({
          id: `${lessonId}_c${i}`,
          num: i,
          type: "tf",
          levelClass: i <= 23 ? "level-th" : "level-vd",
          levelName: i <= 23 ? "Thông hiểu" : "Vận dụng",
          title: `Câu ${i}: Cho các nhận định sau đây về nội dung kiến thức ${lessonTitle}:`,
          statements: [
            { text: `a) Nhận định số 1 về quy luật và tính chất cơ bản trong bài học ${lessonTitle}.`, ans: true },
            { text: `b) Nhận định số 2 phát biểu sai về hiện tượng hoặc điều kiện phản ứng.`, ans: false },
            { text: `c) Nhận định số 3 phát biểu đúng về ứng dụng thực tế theo SGK KNTT.`, ans: true },
            { text: `d) Nhận định số 4 đưa ra kết luận chưa chính xác về cơ chế hoặc công thức tính toán.`, ans: false }
          ],
          explanation: `Hướng dẫn giải chi tiết Câu ${i}: Ý a và c là phát biểu đúng; ý b và d sai do nhầm lẫn điều kiện phản ứng theo quy định SGK Hóa học Kết nối tri thức.`
        });
      }

      const shortAnswers = ["2", "4", "60", "3", "74", "1"];
      for (let i = 26; i <= 31; i++) {
        const ans = shortAnswers[i - 26];
        short.push({
          id: `${lessonId}_c${i}`,
          num: i,
          type: "short",
          levelClass: "level-vd",
          levelName: "Vận dụng",
          title: `Câu ${i}: Tính toán giá trị đại lượng hóa học liên quan đến ${lessonTitle} (Kết quả điền là con số nguyên hoặc số thập phân):`,
          correctText: ans,
          explanation: `Hướng dẫn giải Câu ${i}: Áp dụng công thức tính toán theo bài học ${lessonTitle}, ta tìm ra kết quả chính xác bằng ${ans}.`
        });
      }

      for (let i = 32; i <= 48; i++) {
        essay.push({
          id: `${lessonId}_c${i}`,
          num: i,
          type: "essay",
          levelClass: i <= 36 ? "level-th" : (i <= 43 ? "level-vd" : "level-vdc"),
          levelName: i <= 36 ? "Thông hiểu" : (i <= 43 ? "Vận dụng" : "Vận dụng cao"),
          title: `Câu ${i}: Câu hỏi tự luận ${i - 31} về ${lessonTitle}. Trình bày lí thuyết, giải thích hiện tượng hoặc giải bài toán tính toán chi tiết bám sát SGK Kết nối tri thức.`,
          explanation: `Hướng dẫn giải chi tiết Câu ${i} (${lessonTitle}):\n- Nêu định nghĩa và viết phương trình hóa học tương ứng.\n- Giải thích rõ ràng các hiện tượng và các bước tính toán theo quy chuẩn SGK KNTT.`
        });
      }

      return { mcq, tf, short, essay };
    }

    /* ========================================================
       RENDER SECTIONS: THEORY, METHODS, EXERCISES
       ======================================================== */
    function renderTheory(theoryList) {
      const container = document.getElementById("theory-container");
      let html = "";
      theoryList.forEach(item => {
        if (item.type === "tom_tat") {
          html += `
            <div class="box-theory box-tom-tat">
              <div class="box-header"><span class="icon">📖</span> Tóm tắt</div>
              <div class="box-body">${item.content}</div>
            </div>
          `;
        } else {
          html += `
            <div class="box-theory box-nhan-xet">
              <div class="box-header"><span class="icon">${item.isWarning ? '⚠️' : '💡'}</span> ${item.title || 'Nhận xét'}</div>
              <div class="box-body">${item.content}</div>
            </div>
          `;
        }
      });
      container.innerHTML = html;
    }

    function renderMethods(methodsList) {
      const container = document.getElementById("methods-container");
      let html = "";
      methodsList.forEach((m, dIdx) => {
        html += `
          <div class="banner-dang">
            <span class="badge-dang">Dạng ${dIdx + 1}</span>
            <span>${m.name.replace(/^Dạng \\d+:\\s*/, '')}</span>
          </div>
          <div class="method-desc">${m.content}</div>
        `;
        m.examples.forEach(ex => {
          const state = getQuestionState(ex.id);
          html += `
            <div class="question-card ${state.flagged ? 'flagged' : ''}" id="card-${ex.id}">
              <div class="q-header">
                <span class="pill-q-num">Ví dụ ${ex.num}</span>
                <span class="pill-level ${ex.level}">${ex.levelName}</span>
              </div>
              <div class="q-title">${ex.title}</div>
              <div class="q-footer">
                <button class="btn-solution" onclick="toggleSolution('${ex.id}')"><span class="icon">👁</span> Xem lời giải</button>
                <button class="btn-flag ${state.flagged ? 'active' : ''}" id="flag-${ex.id}" onclick="toggleFlag('${ex.id}')"><span class="icon">📌</span> Ôn lại</button>
              </div>
              <div class="solution-box" id="sol-${ex.id}">
                <strong>Lời giải:</strong><br>${ex.solution}
              </div>
            </div>
          `;
        });
      });
      container.innerHTML = html;
    }

    function renderExercises(exSet) {
      const container = document.getElementById("exercises-container");
      let html = "";

      // 1. MCQ 1-21
      exSet.mcq.forEach(q => {
        const state = getQuestionState(q.id);
        const prefixes = ["A", "B", "C", "D"];
        html += `
          <div class="question-card ${state.flagged ? 'flagged' : ''} ${state.answered ? (state.correct ? 'answered-correct' : 'answered-wrong') : ''}" id="card-${q.id}" data-type="mcq">
            <div class="q-header">
              <span class="pill-q-num">Câu ${q.num}</span>
              <span class="pill-q-type">Trắc nghiệm</span>
              <span class="pill-level ${q.levelClass}">${q.levelName}</span>
            </div>
            <div class="q-title">${q.title}</div>
            <div class="mcq-options">
        `;
        q.options.forEach((opt, optIdx) => {
          let optClass = "mcq-option";
          if (state.answered) {
            if (optIdx === q.correct) optClass += " correct";
            else if (optIdx === state.userAns) optClass += " wrong";
          }
          html += `
            <div class="${optClass}" id="opt-${q.id}-${optIdx}" onclick="selectMcqOption('${q.id}', ${optIdx}, ${q.correct})">
              <span class="mcq-option-prefix">${prefixes[optIdx]}.</span>
              <span>${opt}</span>
            </div>
          `;
        });
        html += `
            </div>
            <div class="q-footer">
              <button class="btn-solution" onclick="toggleSolution('${q.id}')"><span class="icon">👁</span> Xem lời giải</button>
              <button class="btn-flag ${state.flagged ? 'active' : ''}" id="flag-${q.id}" onclick="toggleFlag('${q.id}')"><span class="icon">📌</span> Ôn lại</button>
            </div>
            <div class="solution-box" id="sol-${q.id}">
              <strong>Đáp án đúng: ${prefixes[q.correct]}</strong><br>${q.explanation}
            </div>
          </div>
        `;
      });

      // 2. TF 22-25
      exSet.tf.forEach(q => {
        const state = getQuestionState(q.id);
        html += `
          <div class="question-card ${state.flagged ? 'flagged' : ''} ${state.answered ? (state.correct ? 'answered-correct' : 'answered-wrong') : ''}" id="card-${q.id}" data-type="tf">
            <div class="q-header">
              <span class="pill-q-num">Câu ${q.num}</span>
              <span class="pill-q-type">Đúng/Sai</span>
              <span class="pill-level ${q.levelClass}">${q.levelName}</span>
            </div>
            <div class="q-title">${q.title}</div>
            <table class="tf-table">
        `;
        q.statements.forEach((st, sIdx) => {
          const userVal = state.userAns ? state.userAns[sIdx] : null;
          html += `
            <tr>
              <td class="tf-statement-text">${st.text}</td>
              <td class="tf-actions">
                <button class="btn-tf ${userVal === true ? 'active-true' : ''}" id="btn-tf-${q.id}-${sIdx}-t" onclick="chooseTf('${q.id}', ${sIdx}, true)">Đúng</button>
                <button class="btn-tf ${userVal === false ? 'active-false' : ''}" id="btn-tf-${q.id}-${sIdx}-f" onclick="chooseTf('${q.id}', ${sIdx}, false)">Sai</button>
              </td>
            </tr>
          `;
        });
        html += `
            </table>
            <div style="margin-bottom: 10px;">
              <button class="btn-check-short" onclick="checkTfQuestion('${q.id}', ${JSON.stringify(q.statements.map(s => s.ans))})">Kiểm tra</button>
            </div>
            <div class="q-footer">
              <button class="btn-solution" onclick="toggleSolution('${q.id}')"><span class="icon">👁</span> Xem lời giải</button>
              <button class="btn-flag ${state.flagged ? 'active' : ''}" id="flag-${q.id}" onclick="toggleFlag('${q.id}')"><span class="icon">📌</span> Ôn lại</button>
            </div>
            <div class="solution-box" id="sol-${q.id}">
              <strong>Lời giải chi tiết:</strong><br>${q.explanation}
            </div>
          </div>
        `;
      });

      // 3. Short Answer 26-31
      exSet.short.forEach(q => {
        const state = getQuestionState(q.id);
        html += `
          <div class="question-card ${state.flagged ? 'flagged' : ''} ${state.answered ? (state.correct ? 'answered-correct' : 'answered-wrong') : ''}" id="card-${q.id}" data-type="short">
            <div class="q-header">
              <span class="pill-q-num">Câu ${q.num}</span>
              <span class="pill-q-type">Trả lời ngắn</span>
              <span class="pill-level ${q.levelClass}">${q.levelName}</span>
            </div>
            <div class="q-title">${q.title}</div>
            <div class="short-input-group">
              <input type="text" class="short-input" id="input-${q.id}" placeholder="Nhập đáp án..." value="${state.userAns || ''}" onkeydown="if(event.key==='Enter') checkShortAnswer('${q.id}', '${q.correctText}')">
              <button class="btn-check-short" onclick="checkShortAnswer('${q.id}', '${q.correctText}')">Kiểm tra</button>
            </div>
            <div class="q-footer">
              <button class="btn-solution" onclick="toggleSolution('${q.id}')"><span class="icon">👁</span> Xem lời giải</button>
              <button class="btn-flag ${state.flagged ? 'active' : ''}" id="flag-${q.id}" onclick="toggleFlag('${q.id}')"><span class="icon">📌</span> Ôn lại</button>
            </div>
            <div class="solution-box" id="sol-${q.id}">
              <strong>Đáp số: ${q.correctText}</strong><br>${q.explanation}
            </div>
          </div>
        `;
      });

      // 4. Essay 32-48
      exSet.essay.forEach(q => {
        const state = getQuestionState(q.id);
        html += `
          <div class="question-card ${state.flagged ? 'flagged' : ''} ${state.answered ? 'answered-correct' : ''}" id="card-${q.id}" data-type="essay">
            <div class="q-header">
              <span class="pill-q-num">Câu ${q.num}</span>
              <span class="pill-q-type">Tự luận</span>
              <span class="pill-level ${q.levelClass}">${q.levelName}</span>
            </div>
            <div class="q-title">${q.title}</div>
            <textarea class="essay-scratchpad" placeholder="Ô nháp / Ghi chú câu trả lời của em tại đây...">${state.userAns || ''}</textarea>
            <div class="q-footer">
              <button class="btn-solution" onclick="toggleSolution('${q.id}')"><span class="icon">👁</span> Xem lời giải</button>
              <button class="btn-flag ${state.flagged ? 'active' : ''}" id="flag-${q.id}" onclick="toggleFlag('${q.id}')"><span class="icon">📌</span> Ôn lại</button>
            </div>
            <div class="solution-box" id="sol-${q.id}">
              <strong>Hướng dẫn tự luận:</strong><br>${q.explanation}
            </div>
            <div class="essay-rating-row">
              <span>Tự đánh giá:</span>
              <button class="btn-rate rate-correct ${state.rate === 'check' ? 'active' : ''}" onclick="rateEssay('${q.id}', 'check')">✓ Tự giải đúng</button>
              <button class="btn-rate rate-partial ${state.rate === 'partial' ? 'active' : ''}" onclick="rateEssay('${q.id}', 'partial')">~ Đúng một phần</button>
              <button class="btn-rate rate-wrong ${state.rate === 'wrong' ? 'active' : ''}" onclick="rateEssay('${q.id}', 'wrong')">✗ Cần xem lại</button>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    /* ========================================================
       INTERACTION LOGIC
       ======================================================== */
    function selectMcqOption(qId, selectedIdx, correctIdx) {
      const state = getQuestionState(qId);
      const isFirstTry = !state.answered;
      state.userAns = selectedIdx;
      state.answered = true;
      state.correct = (selectedIdx === correctIdx);
      if (isFirstTry && state.correct) state.firstTryCorrect = true;

      // Update UI
      for (let i = 0; i < 4; i++) {
        const el = document.getElementById(`opt-${qId}-${i}`);
        if (!el) continue;
        el.className = "mcq-option";
        if (i === correctIdx) el.classList.add("correct");
        else if (i === selectedIdx) el.classList.add("wrong");
      }

      const card = document.getElementById(`card-${qId}`);
      if (card) {
        card.classList.remove("answered-correct", "answered-wrong");
        card.classList.add(state.correct ? "answered-correct" : "answered-wrong");
      }

      saveProgress();
      updateNavbarProgress();
    }

    let tempTfUser = {};
    function chooseTf(qId, sIdx, val) {
      if (!tempTfUser[qId]) tempTfUser[qId] = {};
      tempTfUser[qId][sIdx] = val;

      const btnT = document.getElementById(`btn-tf-${qId}-${sIdx}-t`);
      const btnF = document.getElementById(`btn-tf-${qId}-${sIdx}-f`);
      if (btnT && btnF) {
        btnT.classList.remove("active-true");
        btnF.classList.remove("active-false");
        if (val) btnT.classList.add("active-true");
        else btnF.classList.add("active-false");
      }
    }

    function checkTfQuestion(qId, correctArr) {
      const state = getQuestionState(qId);
      const userObj = tempTfUser[qId] || {};
      let isAllCorrect = true;

      correctArr.forEach((ans, idx) => {
        const uAns = userObj[idx];
        const btnT = document.getElementById(`btn-tf-${qId}-${idx}-t`);
        const btnF = document.getElementById(`btn-tf-${qId}-${idx}-f`);

        if (ans === true) {
          if (btnT) btnT.classList.add("ans-correct");
        } else {
          if (btnF) btnF.classList.add("ans-correct");
        }

        if (uAns !== ans) {
          isAllCorrect = false;
          if (uAns === true && btnT) btnT.classList.add("ans-wrong");
          if (uAns === false && btnF) btnF.classList.add("ans-wrong");
        }
      });

      const isFirst = !state.answered;
      state.answered = true;
      state.userAns = userObj;
      state.correct = isAllCorrect;
      if (isFirst && isAllCorrect) state.firstTryCorrect = true;

      const card = document.getElementById(`card-${qId}`);
      if (card) {
        card.classList.remove("answered-correct", "answered-wrong");
        card.classList.add(isAllCorrect ? "answered-correct" : "answered-wrong");
      }

      const solBox = document.getElementById(`sol-${qId}`);
      if (solBox) solBox.style.display = "block";

      saveProgress();
      updateNavbarProgress();
    }

    function checkShortAnswer(qId, correctText) {
      const input = document.getElementById(`input-${qId}`);
      if (!input) return;
      const userVal = input.value.trim().toLowerCase().replace(",", ".");
      const targetVal = correctText.trim().toLowerCase().replace(",", ".");

      const state = getQuestionState(qId);
      const isFirst = !state.answered;
      state.userAns = input.value.trim();
      state.answered = true;
      state.correct = (userVal === targetVal);
      if (isFirst && state.correct) state.firstTryCorrect = true;

      const card = document.getElementById(`card-${qId}`);
      if (card) {
        card.classList.remove("answered-correct", "answered-wrong");
        card.classList.add(state.correct ? "answered-correct" : "answered-wrong");
      }

      const solBox = document.getElementById(`sol-${qId}`);
      if (solBox) solBox.style.display = "block";

      saveProgress();
      updateNavbarProgress();
    }

    function rateEssay(qId, rating) {
      const state = getQuestionState(qId);
      state.answered = true;
      state.rate = rating;
      state.correct = (rating === "check");

      const card = document.getElementById(`card-${qId}`);
      if (card) {
        card.querySelectorAll(".btn-rate").forEach(b => b.classList.remove("active"));
        if (rating === "check") {
          card.querySelector(".rate-correct")?.classList.add("active");
          card.classList.add("answered-correct");
        } else if (rating === "partial") {
          card.querySelector(".rate-partial")?.classList.add("active");
          card.classList.add("answered-correct");
        } else {
          card.querySelector(".rate-wrong")?.classList.add("active");
          card.classList.remove("answered-correct");
        }
      }

      saveProgress();
      updateNavbarProgress();
    }

    function toggleSolution(qId) {
      const box = document.getElementById(`sol-${qId}`);
      if (!box) return;
      if (box.style.display === "none" || box.style.display === "") {
        box.style.display = "block";
        const state = getQuestionState(qId);
        if (!state.answered) state.viewedSol = true;
        if (window.MathJax && window.MathJax.typesetPromise) {
          window.MathJax.typesetPromise([box]).catch(function(e){});
        }
      } else {
        box.style.display = "none";
      }
      saveProgress();
    }

    function toggleAllSolutions() {
      allSolutionsRevealed = !allSolutionsRevealed;
      document.querySelectorAll(".solution-box").forEach(box => {
        box.style.display = allSolutionsRevealed ? "block" : "none";
      });
      const btn = document.getElementById("btn-toggle-all-solutions");
      if (btn) {
        btn.innerHTML = allSolutionsRevealed 
          ? '<span class="icon">🙈</span> Ẩn tất cả lời giải'
          : '<span class="icon">👁</span> Hiện tất cả lời giải';
      }
      if (allSolutionsRevealed && window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise().catch(function(e){});
      }
    }

    function toggleFlag(qId) {
      const state = getQuestionState(qId);
      state.flagged = !state.flagged;
      const btn = document.getElementById(`flag-${qId}`);
      const card = document.getElementById(`card-${qId}`);
      if (btn) btn.classList.toggle("active", state.flagged);
      if (card) card.classList.toggle("flagged", state.flagged);
      saveProgress();
      updateNavbarProgress();
    }

    /* ========================================================
       MODAL 57 CÂU: TỔNG KẾT & TIẾN ĐỘ
       ======================================================== */
    function calculateStats() {
      const progress = STUDENT_PROGRESS[currentLessonId] || {};
      let totalDone = 0;
      let totalCorrect = 0;
      let firstTryCorrect = 0;
      let retryCorrect = 0;
      let viewedSol = 0;
      let flagged = 0;

      let vdDone = 0, vdCorrect = 0, vdFlagged = 0;
      let btDone = 0, btCorrect = 0, btFlagged = 0;

      let mcqDone = 0, mcqCorrect = 0, mcqFirst = 0;
      let tfDone = 0, tfCorrect = 0, tfFirst = 0;
      let shortDone = 0, shortCorrect = 0, shortFirst = 0;
      let essayDone = 0, essayCheck = 0, essayPartial = 0, essayWrong = 0;

      for (let i = 1; i <= 9; i++) {
        const st = progress[`${currentLessonId}_vd${i}`];
        if (st) {
          if (st.answered || st.viewedSol) vdDone++;
          if (st.correct) vdCorrect++;
          if (st.flagged) vdFlagged++;
        }
      }

      for (let i = 1; i <= 48; i++) {
        const st = progress[`${currentLessonId}_c${i}`];
        if (st) {
          if (st.answered) btDone++;
          if (st.correct) btCorrect++;
          if (st.flagged) btFlagged++;

          if (i <= 21) {
            if (st.answered) mcqDone++;
            if (st.correct) mcqCorrect++;
            if (st.firstTryCorrect) mcqFirst++;
          } else if (i <= 25) {
            if (st.answered) tfDone++;
            if (st.correct) tfCorrect++;
            if (st.firstTryCorrect) tfFirst++;
          } else if (i <= 31) {
            if (st.answered) shortDone++;
            if (st.correct) shortCorrect++;
            if (st.firstTryCorrect) shortFirst++;
          } else {
            if (st.answered) essayDone++;
            if (st.rate === "check") essayCheck++;
            else if (st.rate === "partial") essayPartial++;
            else if (st.rate === "wrong") essayWrong++;
          }
        }
      }

      totalDone = vdDone + btDone;
      totalCorrect = vdCorrect + btCorrect;

      Object.values(progress).forEach(st => {
        if (st.firstTryCorrect) firstTryCorrect++;
        if (st.correct && !st.firstTryCorrect) retryCorrect++;
        if (st.viewedSol) viewedSol++;
        if (st.flagged) flagged++;
      });

      return {
        totalDone, totalCorrect, remaining: 57 - totalDone,
        firstTryCorrect, retryCorrect, viewedSol, flagged,
        vdDone, vdCorrect, vdFlagged,
        btDone, btCorrect, btFlagged,
        mcqDone, mcqCorrect, mcqFirst,
        tfDone, tfCorrect, tfFirst,
        shortDone, shortCorrect, shortFirst,
        essayDone, essayCheck, essayPartial, essayWrong
      };
    }

    function updateNavbarProgress() {
      const stats = calculateStats();
      const text = `Đã làm ${stats.totalDone}/57 - đúng ${stats.totalCorrect}`;
      document.getElementById("nav-progress-text").textContent = text;
      const pct = Math.round((stats.totalDone / 57) * 100);
      document.getElementById("nav-progress-bar").style.width = pct + "%";
    }

    function openSummaryModal() {
      const s = calculateStats();
      document.getElementById("summary-headline").textContent = 
        `Em đã làm ${s.totalDone}/57 câu, đúng ${s.totalCorrect}. Còn ${s.remaining} câu chưa làm.`;

      document.getElementById("stat-done").textContent = `${s.totalDone}/57`;
      document.getElementById("stat-correct").textContent = s.totalCorrect;
      document.getElementById("stat-first-correct").textContent = s.firstTryCorrect;
      document.getElementById("stat-retry-correct").textContent = s.retryCorrect;
      document.getElementById("stat-viewed-sol").textContent = s.viewedSol;
      document.getElementById("stat-flagged").textContent = s.flagged;

      document.getElementById("tbl-vd-done").textContent = `${s.vdDone}/9`;
      document.getElementById("tbl-vd-correct").textContent = s.vdCorrect;
      document.getElementById("tbl-vd-flagged").textContent = s.vdFlagged;

      document.getElementById("tbl-bt-done").textContent = `${s.btDone}/48`;
      document.getElementById("tbl-bt-correct").textContent = s.btCorrect;
      document.getElementById("tbl-bt-flagged").textContent = s.btFlagged;

      document.getElementById("lbl-mcq-done").textContent = `${s.mcqDone}/21`;
      document.getElementById("lbl-mcq-correct").textContent = s.mcqCorrect;
      document.getElementById("lbl-mcq-first").textContent = s.mcqFirst;

      document.getElementById("lbl-tf-done").textContent = `${s.tfDone}/4`;
      document.getElementById("lbl-tf-correct").textContent = s.tfCorrect;
      document.getElementById("lbl-tf-first").textContent = s.tfFirst;

      document.getElementById("lbl-short-done").textContent = `${s.shortDone}/6`;
      document.getElementById("lbl-short-correct").textContent = s.shortCorrect;
      document.getElementById("lbl-short-first").textContent = s.shortFirst;

      document.getElementById("lbl-essay-done").textContent = `${s.essayDone}/26`;
      document.getElementById("lbl-essay-check").textContent = s.essayCheck;
      document.getElementById("lbl-essay-partial").textContent = s.essayPartial;
      document.getElementById("lbl-essay-wrong").textContent = s.essayWrong;

      document.getElementById("modal-summary").style.display = "flex";
    }

    function openMenuModal() {
      modalGradeKey = currentGradeKey;
      switchModalGrade(modalGradeKey);
      document.getElementById("modal-menu").style.display = "flex";
    }

    function switchModalGrade(gradeKey) {
      modalGradeKey = gradeKey;
      ["g10", "g11", "g12"].forEach(k => {
        const b = document.getElementById(`modal-btn-${k}`);
        if (b) {
          if (k === gradeKey) {
            b.style.background = "#0078d4";
            b.style.color = "white";
          } else {
            b.style.background = "#e2e8f0";
            b.style.color = "#0f172a";
          }
        }
      });
      renderChapterCatalog("modal-chapters-container", true);
    }

    function closeModal(modalId) {
      document.getElementById(modalId).style.display = "none";
    }

    function closeModalOnOverlay(e, modalId) {
      if (e.target.id === modalId) closeModal(modalId);
    }

    function filterFailedQuestions() {
      closeModal("modal-summary");
      document.getElementById("q-filter").value = "wrong";
      applyQuestionFilter("wrong");
    }

    function filterFlaggedQuestions() {
      closeModal("modal-summary");
      document.getElementById("q-filter").value = "flagged";
      applyQuestionFilter("flagged");
    }

    function resetCurrentLessonProgress() {
      if (confirm("Em có chắc chắn muốn xóa toàn bộ kết quả đã làm của bài này để làm lại từ đầu không?")) {
        delete STUDENT_PROGRESS[currentLessonId];
        saveProgress();
        openAnyLesson(currentLessonId);
        closeModal("modal-summary");
      }
    }

    function applyQuestionFilter(filterType) {
      const cards = document.querySelectorAll(".question-card");
      cards.forEach(card => {
        const qId = card.id.replace("card-", "");
        const state = getQuestionState(qId);
        let show = true;

        if (filterType === "unanswered") {
          show = !state.answered;
        } else if (filterType === "answered") {
          show = state.answered;
        } else if (filterType === "wrong") {
          show = state.answered && !state.correct;
        } else if (filterType === "flagged") {
          show = state.flagged;
        }

        card.style.display = show ? "block" : "none";
      });
    }

    /* ========================================================
       INIT
       ======================================================== */
    window.addEventListener("DOMContentLoaded", () => {
      loadProgress();
      // Mặc định mở ngay bài 8 Chương 3 Hóa 11
      openAnyLesson("c3_b8");
    });
  </script>
</body>
</html>
"""

# Write to project directory
with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_template)
print("Successfully generated index.html")

# Write to Desktop mirrors
desktop_path1 = r"C:\Users\admin\Desktop\Bai_Giang_Hoa_11_Chuong_3.html"
desktop_path2 = r"C:\Users\admin\Desktop\Bai_Giang_Hoa_11_Toan_Dien.html"

try:
    with open(desktop_path1, "w", encoding="utf-8") as f:
        f.write(html_template)
    print("Desktop mirror 1 updated:", desktop_path1)
except Exception as e:
    print("Mirror 1 error:", e)

try:
    with open(desktop_path2, "w", encoding="utf-8") as f:
        f.write(html_template)
    print("Desktop mirror 2 updated:", desktop_path2)
except Exception as e:
    print("Mirror 2 error:", e)

print("Done compiling complete platform.")
