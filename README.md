# seo-guide-skill
SEO 全流程技能：网站诊断、页面优化、技术SEO、内容策略、外链建设。

# 1、说明
严格来说这不是一个技能，是学习了3大权威指南，构建出的一个SEO指南。

可以用于大多数Agent，按后面我提供的方法，训练成适合自己的SEO技能。

# 2、学习资源

---

## Google Search Central 官方文档（86 篇）

| 分类 | 篇数 | 覆盖内容 |
|------|------|---------|
| 🔰 SEO 基础 | 5 | SEO 入门指南、技术要求总览、搜索原理、是否需要 SEO |
| 🕷️ 爬取与索引 | 26 | robots.txt、sitemap、canonical、301/302 重定向、移动优先索引、JavaScript SEO、分面导航、网站迁移 |
| 🎨 搜索结果外观 | 13 | Title Link 优化、Meta Description、Featured Snippets、图片/视频 SEO、Core Web Vitals、Google Discover、Web Stories |
| 🗂️ 结构化数据 | 11 | Article、FAQPage、Product、Recipe、LocalBusiness、SoftwareApp、Video 等 Schema 完整指南 |
| 🔴 排名系统与更新 | 2 | Google 排名系统完全指南、核心更新应对策略 |
| 🛒 电商 SEO | 9 | 电商 URL 结构、产品数据、结构化数据、高质量评论写法 |
| 🌐 国际化 SEO | 4 | 多语言/多地区网站管理、语言自适应页面 |
| 📊 监控与调试 | 2 | Search Console 入门、排查搜索流量下降 |
| 🚫 垃圾政策 | 9 | 付费链接、伪装 Cloaking、隐藏重定向、网站被黑 |
| ⚙️ 其他 | 4 | 移动端 SEO 完整指南、临时关闭网站、Web Stories 内容政策、Google 评价系统 |

---

## Moz Beginner's Guide to SEO（10 章）

| # | 章节 | 核心内容 |
|---|------|---------|
| 1 | Introduction | SEO 基础概念与核心价值 |
| 2 | How Search Engines Operate | 搜索引擎抓取、索引、排名原理 |
| 3 | Keyword Research | 关键词研究方法与工具选择 |
| 4 | On-Page SEO | 页面要素优化（Title/Description/URL/内链） |
| 5 | Technical SEO | 站点架构、HTTPS、速度、结构化数据 |
| 6 | Growing Popularity and Links | 外链建设策略与链接质量评估 |
| 7 | Why Search Engine Marketing Is Necessary | SEO 与 SEM 的区别与协同 |
| 8 | Measuring and Tracking Success | 关键指标、追踪工具、报告方法 |
| 9 | SEO Glossary | SEO 行业术语权威词典 |
| 10 | Quick Start Guide | 7 步 SEO 执行清单 |

**核心方法论：** SEO 金字塔模型 + 7 步检查清单 + E-E-A-T 评估框架

---

## Ahrefs Academy（7 门课 · 58 课时）

| 课程 | 课时 | 核心收获 |
|------|------|---------|
| Keyword Research | 11 | 五点关键词评估清单、3C 意图分析法、Traffic Potential 优先于搜索量、长尾词批量挖掘 |
| Technical SEO | 8 | Core Web Vitals 优化（LCP/CLS/FID）、WordPress 加速实战、内部链接树状策略 |
| Advanced Link Building | 15 | Seed Prospects 四步法、Lookalike 扩展、Blitz List 快速外链列表、Hybrid Outreach 混合 outreach |
| Local SEO | 4 | Google Business Profile 完整优化、本地引用 NAP 一致性策略 |
| Content Marketing | 9 | Product-led Content 产品驱动内容、内容中心（Content Hubs）建设方法 |
| Digital Marketing | 5 | 七大数字营销策略、渠道优先级决策框架 |
| Video Marketing | 6 | YouTube SEO 完整流程、Video Schema 实施技巧 |

---

# 技能产出物（示例）

| 文件 | 说明 |
|------|------|
| `references/tkd-standard.md` | Title / Description / Keywords 写作规范（长度规格 + 场景模板 + 最佳实践） |
| `references/keyword-research.md` | 关键词研究完整工作流（工具链 + 意图分类 + 筛选漏斗） |

# 3、文件结构

```
seo-guide/
├── SKILL.md                          ← 技能入口说明（本文档主入口）
│
├── references/                        ← ⭐ 自研精炼指南（主工作区）
│   ├── tkd-standard.md               ← Title / Description / Keywords 写作规范
│   ├── keyword-research.md            ← 关键词研究完整工作流
│   ├── on-page-seo.md                 ← 页面优化执行指南
│   ├── technical-seo.md               ← 技术 SEO 检查清单
│   ├── content-strategy.md            ← 内容策略与规划
│   ├── link-building.md               ← 外链建设方法论
│   ├── local-seo.md                   ← 本地 SEO 操作指南
│   ├── seo-principles.md              ← 核心原则 + 常见误区辟谣
│   ├── seo-audit.md                   ← SEO 诊断与审计流程
│   └── seo-tools.md                   ← 常用工具推荐与用法
│
├── references-google/                 ← Google Search Central 官方文档（86篇）
│   ├── INDEX.md                       ← 按主题分类的完整索引
│   ├── seo-starter-guide.md           ← SEO 入门指南原文
│   ├── essentials.md                  ← 技术要求总览
│   ├── title-link.md                  ← Title Link 优化（Google 官方）
│   ├── snippet.md                     ← Meta Description / Snippet 优化
│   ├── featured-snippets.md           ← Featured Snippets 攻略
│   ├── core-web-vitals.md             ← Core Web Vitals 详解
│   ├── robots-txt.md                  ← robots.txt 完整指南
│   ├── sitemap.md                     ← Sitemap 入门
│   ├── canonicalization.md            ← URL 规范化
│   ├── structured-data-*.md           ← 11种结构化数据完整指南
│   ├── ecommerce-*.md                ← 电商 SEO 专项（9篇）
│   ├── international-seo.md            ← 国际化 / 多语言 SEO
│   ├── mobile-first-indexing.md       ← 移动优先索引
│   ├── javascript-seo-basics.md       ← JavaScript SEO 基础
│   ├── search-ranking-systems.md      ← Google 排名系统完全指南
│   ├── core-updates.md                ← 核心更新应对策略
│   ├── search-console-start.md        ← Search Console 入门
│   ├── debugging-traffic-drops.md     ← 排查流量下降
│   ├── spam-policies-*.md             ← 垃圾政策详解（3篇）
│   └── [其他 50+ 篇]                  ← 图片 SEO、视频 SEO、AI 功能等
│
├── references-moz/                   ← Moz Beginner's Guide to SEO（10章）
│   ├── INDEX.md                       ← 章节索引 + 使用提示
│   ├── MOZ-LEARNING-SUMMARY.md        ← 10 章核心要点总结
│   ├── introduction.txt               ← 第1章原文
│   ├── how-search-engines-operate.txt ← 第2章原文
│   ├── keyword-research.txt           ← 第3章原文
│   ├── on-page-seo.txt                ← 第4章原文
│   ├── technical-seo.txt              ← 第5章原文
│   ├── growing-popularity-and-links.txt← 第6章原文
│   ├── why-search-engine-marketing-is-necessary.txt
│   ├── measuring-and-tracking-success.txt
│   ├── seo-glossary.txt               ← SEO 术语词典
│   └── quick-start-guide.txt         ← 快速入门
│
├── references-ahrefs/                ← Ahrefs Academy 课程（7门58课）
│   ├── INDEX.md                        ← 课程索引 + SUMMARY 入口
│   ├── AHREFS-KEYWORD-RESEARCH-SUMMARY.md
│   ├── AHREFS-TECHNICAL-SEO-SUMMARY.md
│   ├── AHREFS-LINK-BUILDING-SUMMARY.md
│   ├── AHREFS-LOCAL-SEO-SUMMARY.md
│   ├── AHREFS-CONTENT-MARKETING-SUMMARY.md
│   ├── AHREFS-DIGITAL-MARKETING-SUMMARY.md
│   ├── AHREFS-VIDEO-MARKETING-SUMMARY.md
│   ├── keyword_research/               ← 11课字幕原文
│   │   ├── 01-what-are-keywords.txt
│   │   ├── 02-analyze-searcher-intent.txt
│   │   ├── 03-find-keywords-for-website.txt
│   │   ├── 04-understanding-ranking-difficulty.txt
│   │   ├── 05-keyword-research-tutorial.txt
│   │   ├── 06-keyword-research-new-website.txt
│   │   ├── 07-low-competition-keywords.txt
│   │   ├── 08-long-tail-keywords.txt
│   │   ├── 09-keyword-difficulty-scores.txt
│   │   ├── 10-advanced-keyword-tips.txt
│   │   └── 11-fractured-search-intent.txt
│   ├── technical_seo/                 ← 8课字幕原文
│   │   ├── techseo-01-what-is-technical-seo.txt
│   │   ├── techseo-02-technical-seo-best-practices.txt
│   │   ├── techseo-03-http-vs-https.txt
│   │   ├── techseo-04-technical-seo-audit.txt
│   │   ├── techseo-05-speed-up-wordpress.txt
│   │   ├── techseo-06-internal-links.txt
│   │   ├── techseo-07-seo-audit-fix-issues.txt
│   │   └── techseo-08-core-web-vitals.txt
│   ├── link_building/                 ← 15课字幕原文
│   │   ├── linkbuild-01-advanced-link-building-fundamentals.txt
│   │   ├── linkbuild-02-outreach.txt
│   │   ├── linkbuild-03-team-building-systems.txt
│   │   ├── m2l1_seed_prospects.txt
│   │   ├── m2l2_lookalike_prospects.txt
│   │   ├── m2l3_segment_prospects.txt
│   │   ├── m3l1_vetting_prospects.txt
│   │   ├── m3l2_who_to_pitch.txt
│   │   ├── m3l3_blitz_list.txt
│   │   ├── m4l2_hybrid_outreach.txt
│   │   ├── m4l3_email_templates.txt
│   │   ├── m5l2_link_building_system.txt
│   │   └── m5l3_team_workflow.txt
│   ├── local_seo/                     ← 4课字幕原文
│   │   ├── 01_how_to_do_local_seo.txt
│   │   ├── 02_local_keyword_research.txt
│   │   ├── 03_link_building_for_local_seo.txt
│   │   └── 04_find_citations_for_local_seo.txt
│   ├── content_marketing/             ← 9课字幕原文
│   ├── digital_marketing/             ← 5课字幕原文
│   └── video_marketing/               ← 6课字幕原文
│
└── scripts/                           ← 自动化脚本
    ├── README.md                      ← 脚本使用说明
    ├── generate_seo_report.py         ← SEO 诊断报告生成器
    └── setup_chinese_pdf.py           ← 中文 PDF 环境配置
```

# 4、使用方法

可以让Agent读所有指南，精炼某一项技能；

也可以遵循指南，定制SEO流程、方法。

核心要点就一个：让AI做SEO时，有权威、标准的参考。
