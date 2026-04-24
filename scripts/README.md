# SEO 诊断 PDF 报告生成

> **规则：只在用户明确要求时才生成 PDF，不要主动生成。**

SEO 诊断完成后可生成格式化 PDF 报告，完全自包含，不依赖其他技能。

## 依赖

```bash
pip3 install reportlab    # Python 3.8 需锁定 reportlab<4.3
```

## 调用方式

**方式 1：Python 调用**
```python
import sys, os
sys.path.insert(0, os.path.expanduser("~/.qclaw/skills/seo-guide/scripts"))
from generate_seo_report import generate_seo_pdf

data = {
    "url": "https://example.com",
    "date": "2026-04-22",
    "scores": {"title_meta": {"stars": 2, "label": "标题/描述"}},
    "issues": [{"priority": "high", "title": "...", "detail": "...", "fix": "..."}],
    "good_points": [{"title": "...", "detail": "..."}],
    "recommendations": [{"priority": "high", "issue": "...", "solution": "...", "impact": "..."}],
    "summary": "一句话总结"
}
generate_seo_pdf(data, "~/Downloads/seo-report.pdf")
```

**方式 2：命令行**
```bash
python3 ~/.qclaw/skills/seo-guide/scripts/generate_seo_report.py \
  --data report_data.json --output ~/Downloads/seo-report.pdf
```

## data 字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| url | 是 | 网站 URL |
| date | 是 | 分析日期 |
| scores | 是 | 各维度评分（stars 1-5 + label） |
| issues | 否 | 问题列表（priority: high/medium/low） |
| good_points | 否 | 优点列表 |
| recommendations | 否 | 优化建议（priority + issue + solution + impact） |
| summary | 否 | 一句话总结 |
