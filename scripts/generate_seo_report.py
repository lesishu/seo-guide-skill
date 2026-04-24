#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_seo_report.py — SEO 诊断报告 PDF 生成器
属于 seo-guide，完全自包含，不依赖其他 skill。

用法：
    python generate_seo_report.py --data report_data.json --output ~/Downloads/seo-report.pdf

或在 Python 中调用：
    from generate_seo_report import generate_seo_pdf
    generate_seo_pdf(data, output_path)

data 结构（dict）：
{
    "url": "https://example.com",
    "date": "2026-04-22",
    "site_type": "Shopify 电商",
    "scores": {
        "title_meta":    {"stars": 2, "label": "标题/描述"},
        "technical":     {"stars": 4, "label": "技术SEO"},
        "images":        {"stars": 2, "label": "图片SEO"},
        "structured":    {"stars": 4, "label": "结构化数据"},
        "social":        {"stars": 2, "label": "社交分享"},
        "mobile":        {"stars": 4, "label": "移动适配"},
    },
    "issues": [
        {
            "priority": "high",   # high / medium / low
            "title": "Title 超长（204字符）",
            "detail": "当前内容过长，建议精简至 50-60 字符。",
            "fix": "Aroha® - Premium Hawaiian Aloha Shirts | Unique Hand-Painted Designs",
            "table": [  # 可选，附加对比表格
                {"项目": "字符长度", "当前值": "204 字符", "建议值": "50-60 字符", "状态": "⚠️ 超长"},
            ]
        },
    ],
    "good_points": [
        {"title": "Canonical URL 正确声明", "detail": "https://www.example.com/ — 有效防止重复内容"},
    ],
    "recommendations": [
        {
            "priority": "high",
            "issue": "Title 超长",
            "solution": "精简至 50-60 字符",
            "impact": "搜索展示改善，CTR 提升"
        },
    ],
    "summary": "技术 SEO 扎实，但标题和社交分享标签是明显短板。",
}
"""

import argparse
import json
import os
import sys

# ── 自包含：从同目录加载 setup_chinese_pdf ──
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from setup_chinese_pdf import setup_chinese_pdf

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

# ── 优先级配置 ──
PRIORITY_CONFIG = {
    "high":   {"emoji": "🔴", "label": "高",  "color": "#e74c3c", "row_bg": "#fdf2f2"},
    "medium": {"emoji": "🟡", "label": "中",  "color": "#e67e22", "row_bg": "#fffbf0"},
    "low":    {"emoji": "🟢", "label": "低",  "color": "#27ae60", "row_bg": "#f0fff4"},
}

# ── 星级 → 颜色 ──
STAR_COLORS = {1: "#e74c3c", 2: "#e74c3c", 3: "#e67e22", 4: "#27ae60", 5: "#27ae60"}


def _star_str(n):
    return "⭐" * n + "☆" * (5 - n)


def _hex(h):
    return colors.HexColor(h)


def build_pdf(data: dict, output_path: str):
    """核心构建函数，接收 data dict，输出 PDF 到 output_path。"""

    # ── 1. 初始化字体和样式 ──
    cn_font, base_styles = setup_chinese_pdf()

    def S(name, **kw):
        """快速创建继承 CJK 字体的 ParagraphStyle。"""
        parent = kw.pop("parent", "Normal")
        return ParagraphStyle(name, parent=base_styles[parent], **kw)

    title_style    = S("ReportTitle",  parent="Title",   fontSize=22, spaceAfter=4,
                       alignment=TA_CENTER, textColor=_hex("#1a3a5c"))
    subtitle_style = S("Subtitle",     fontSize=13, spaceAfter=3,
                       alignment=TA_CENTER, textColor=_hex("#555555"))
    meta_style     = S("Meta",         fontSize=9,  spaceAfter=2,
                       alignment=TA_CENTER, textColor=_hex("#888888"))
    h2_style       = S("H2",  parent="Heading1", fontSize=14, spaceBefore=14, spaceAfter=5,
                       textColor=_hex("#1a3a5c"))
    h3_style       = S("H3",  parent="Heading2", fontSize=11.5, spaceBefore=8, spaceAfter=3,
                       textColor=_hex("#2c5f8a"))
    body_style     = S("Body",  fontSize=10.5, leading=17, spaceAfter=3)
    good_style     = S("Good",  fontSize=10.5, leading=17, spaceAfter=3,
                       textColor=_hex("#27ae60"))
    warn_style     = S("Warn",  fontSize=10.5, leading=17, spaceAfter=3,
                       textColor=_hex("#c0392b"))
    footer_style   = S("Footer", fontSize=8, alignment=TA_CENTER,
                       textColor=_hex("#999999"))
    badge_style    = S("Badge",  fontSize=9,  alignment=TA_CENTER, textColor=colors.white)
    summary_style  = S("SummaryText", fontSize=11, leading=18, spaceAfter=4,
                       textColor=_hex("#1a3a5c"))

    def P(text, style=None):
        return Paragraph(text, style or body_style)

    def HR():
        return HRFlowable(width="100%", thickness=1, color=_hex("#dddddd"), spaceAfter=4)

    # ── 2. 评分徽章 ──
    def score_badge(stars, label):
        bg = _hex(STAR_COLORS.get(stars, "#888888"))
        cell = Paragraph(
            f'<b>{_star_str(stars)}</b><br/><font size="8">{label}</font>',
            badge_style
        )
        t = Table([[cell]], colWidths=[2.6 * cm], rowHeights=[1.5 * cm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), bg),
            ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
            ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING",  (0, 0), (-1, -1), 2),
            ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ]))
        return t

    # ── 3. 通用表格构建 ──
    def build_table(rows, col_widths, header_color="#2E4057", row_bg_colors=None):
        """rows[0] 为表头（字符串列表），rows[1:] 为数据行。"""
        table_data = []
        for i, row in enumerate(rows):
            table_data.append([P(cell, base_styles["Normal"]) for cell in row])

        t = Table(table_data, colWidths=col_widths)
        row_bgs = row_bg_colors or [_hex("#f9f9f9"), colors.white]
        t.setStyle(TableStyle([
            ("BACKGROUND",   (0, 0), (-1, 0),  _hex(header_color)),
            ("TEXTCOLOR",    (0, 0), (-1, 0),  colors.white),
            ("FONTNAME",     (0, 0), (-1, -1), cn_font),
            ("FONTSIZE",     (0, 0), (-1, -1), 9.5),
            ("GRID",         (0, 0), (-1, -1), 0.5, colors.grey),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), row_bgs),
            ("ALIGN",        (0, 0), (-1, -1), "LEFT"),
            ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING",  (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING",   (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        ]))
        return t

    # ── 4. 开始构建 story ──
    story = []
    url       = data.get("url", "")
    date_str  = data.get("date", "")
    site_type = data.get("site_type", "")

    # ── 封面 ──
    story.append(Spacer(1, 0.4 * cm))
    story.append(P(url or "SEO 分析报告", title_style))
    story.append(P("SEO 诊断报告", subtitle_style))
    story.append(Spacer(1, 0.2 * cm))
    story.append(HRFlowable(width="80%", thickness=2, color=_hex("#1a3a5c"), spaceAfter=4))
    if site_type:
        story.append(P(f"网站类型：{site_type}", meta_style))
    if date_str:
        story.append(P(f"分析时间：{date_str}  |  数据来源：网站首页 HTML 抓取", meta_style))
    story.append(Spacer(1, 0.4 * cm))

    # ── 评分卡片行 ──
    scores = data.get("scores", {})
    if scores:
        badges = [score_badge(v["stars"], v["label"]) for v in scores.values()]
        # 每行最多 6 个
        chunk_size = 6
        for i in range(0, len(badges), chunk_size):
            chunk = badges[i:i + chunk_size]
            row_table = Table([chunk], colWidths=[2.6 * cm] * len(chunk), hAlign="CENTER")
            row_table.setStyle(TableStyle([
                ("ALIGN",  (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING",  (0, 0), (-1, -1), 2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ]))
            story.append(row_table)
        story.append(Spacer(1, 0.4 * cm))

    # ── 严重问题 ──
    issues = data.get("issues", [])
    if issues:
        story.append(HR())
        story.append(P("❌  严重问题（优先修复）", h2_style))
        for idx, issue in enumerate(issues, 1):
            cfg = PRIORITY_CONFIG.get(issue.get("priority", "medium"), PRIORITY_CONFIG["medium"])
            story.append(P(f"{idx}. {issue['title']}", h3_style))
            if issue.get("detail"):
                story.append(P(issue["detail"], body_style))
            # 可选对比表格
            if issue.get("table"):
                tbl = issue["table"]
                headers = list(tbl[0].keys())
                rows = [headers] + [[str(row.get(h, "")) for h in headers] for row in tbl]
                col_w = [A4[0] / len(headers) - 1.5 * cm] * len(headers)
                story.append(build_table(rows, col_w,
                    header_color=cfg["color"],
                    row_bg_colors=[_hex(cfg["row_bg"]), colors.white]))
                story.append(Spacer(1, 0.15 * cm))
            if issue.get("fix"):
                story.append(P(f"<b>建议修复：</b>", body_style))
                story.append(P(issue["fix"], body_style))
            story.append(Spacer(1, 0.2 * cm))

    # ── 做得好的地方 ──
    good_points = data.get("good_points", [])
    if good_points:
        story.append(HR())
        story.append(P("✅  做得好的地方", h2_style))
        for gp in good_points:
            story.append(P(gp["title"], h3_style))
            if gp.get("detail"):
                story.append(P(f"✅ {gp['detail']}", good_style))
        story.append(Spacer(1, 0.2 * cm))

    # ── 优化建议汇总 ──
    recs = data.get("recommendations", [])
    if recs:
        story.append(HR())
        story.append(P("📋  优化建议汇总", h2_style))
        headers = ["优先级", "问题", "解决方案", "预计影响"]
        col_w   = [2 * cm, 4 * cm, 6 * cm, 4 * cm]
        rows = [headers]
        for r in recs:
            cfg = PRIORITY_CONFIG.get(r.get("priority", "medium"), PRIORITY_CONFIG["medium"])
            rows.append([
                f"{cfg['emoji']} {cfg['label']}",
                r.get("issue", ""),
                r.get("solution", ""),
                r.get("impact", ""),
            ])
        story.append(build_table(rows, col_w, header_color="#2980b9",
            row_bg_colors=[_hex("#f0f8ff"), colors.white]))
        story.append(Spacer(1, 0.2 * cm))

    # ── 总结 ──
    summary_scores = data.get("scores", {})
    if summary_scores or data.get("summary"):
        story.append(HR())
        story.append(P("📝  总结", h2_style))
        if summary_scores:
            headers = ["维度", "评分", "状态"]
            col_w   = [6 * cm, 3.5 * cm, 6.5 * cm]
            rows = [headers]
            for v in summary_scores.values():
                stars = v["stars"]
                status = "✅ 良好" if stars >= 4 else ("⚠️ 需改善" if stars == 3 else "❌ 问题较多")
                rows.append([v["label"], _star_str(stars), status])
            story.append(build_table(rows, col_w, header_color="#1a3a5c",
                row_bg_colors=[_hex("#f4f6f9"), colors.white]))
            story.append(Spacer(1, 0.3 * cm))
        if data.get("summary"):
            story.append(P(f"<b>{data['summary']}</b>", summary_style))
        story.append(Spacer(1, 0.4 * cm))

    # ── 页脚 ──
    story.append(HRFlowable(width="100%", thickness=0.5, color=_hex("#cccccc"), spaceAfter=3))
    footer_parts = ["Generated by QClaw SEO Skill"]
    if date_str:
        footer_parts.append(f"Date: {date_str}")
    if url:
        footer_parts.append(f"Source: {url}")
    story.append(P("  |  ".join(footer_parts), footer_style))

    # ── 5. 构建 PDF ──
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )
    doc.build(story)
    print(f"✅ PDF 已生成: {output_path}")
    return output_path


def generate_seo_pdf(data: dict, output_path: str = None) -> str:
    """
    对外接口。
    data: SEO 诊断数据 dict（见模块文档）
    output_path: 输出路径，默认 ~/Downloads/seo-report.pdf
    返回实际输出路径。
    """
    if output_path is None:
        output_path = os.path.expanduser("~/Downloads/seo-report.pdf")
    output_path = os.path.expanduser(output_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    build_pdf(data, output_path)
    return output_path


# ── CLI 入口 ──
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SEO 诊断报告 PDF 生成器")
    parser.add_argument("--data",   required=True, help="JSON 数据文件路径")
    parser.add_argument("--output", default="~/Downloads/seo-report.pdf", help="输出 PDF 路径")
    args = parser.parse_args()

    with open(args.data, "r", encoding="utf-8") as f:
        report_data = json.load(f)

    generate_seo_pdf(report_data, args.output)
