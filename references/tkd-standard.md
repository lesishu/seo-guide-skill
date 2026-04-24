# TKD 写作规范（Title / Keywords / Description）
# 全面整合版

> 来源：Google Search Central 官方文档（title-link / snippet） + Moz Beginner's Guide + Ahrefs Academy 课程
> 更新时间：2026-04-24
> 整合来源：Google 官方文档（2025-12 / 2026-04）+ Moz 10章指南 + Ahrefs 11课关键词研究课程

---

## 速查表

| | Title（标题链接） | Description（元描述） | Keywords |
|---|---|---|---|
| **长度** | 50-60 字符（移动端 ~40） | 150-160 字符（移动端 120-130） | **不写** |
| **排名影响** | ✅ 直接排名因素 | ❌ 不影响排名，但影响点击 | ❌ Google 不使用 |
| **CTR 影响** | ✅ 极高 | ✅ 高 | — |
| **每页唯一** | ✅ 必须 | ✅ 必须 | — |
| **关键词** | 自然融入 1-2 个主词 | 自然融入 1-3 个，搜索词会加粗 | — |
| **Google 重写** | 经常（用 H1/锚文本/外链替代） | 经常（用页面内容片段替代） | — |
| **语言匹配** | 必须与页面主语言一致 | 建议与页面一致 | — |

---

## 一、Title 标签（标题链接）

### 1.1 长度规范

| 平台 | 字符数 | 像素 | 说明 |
|------|--------|------|------|
| 桌面端 | 50-60 字符 | ≤ 600px | 超出将被截断 |
| 移动端 | ~40 字符 | ≤ 450px | 移动端显示空间更少 |
| 中文页面 | 25-30 个汉字 | 中文字符占像素更宽 | 中文比英文更占空间 |

> **Google 官方说明：** "There's no limit on how long a `<title>` element can be, but the title link is truncated in Google Search results as needed, typically to fit the device width."（来源：Google Title Link 文档，2025-12 更新）

### 1.2 Google 生成 Title 的优先级来源

Google 按以下顺序自动选择/修改 Title（来源：Google 官方）：

1. `<title>` 元素内容
2. 页面主视觉标题（H1 元素）
3. 其他大号醒目文本（通过样式突出）
4. 页面正文内容
5. 页面锚文本（页面内链接文字）
6. 指向该页的外链锚文本（外部网站的链接文字）
7. `og:title` meta 标签
8. `WebSite` 结构化数据

> **Google 官方提示：** "Google has to recrawl and reprocess the page to notice updates to these sources, which may take a few days to a few weeks." — 修改后需主动请求 Google 重新抓取。

### 1.3 Google 重写 Title 的 6 大触发条件

| 问题类型 | 原因 | Google 行为 |
|---------|------|------------|
| **半空 Title** | `<title>` 只写了品牌名，缺少页面主题 | 用 H1 + 品牌名替代 |
| **过期 Title** | 年份/日期与页面实际内容不符 | 用页面可见的最新标题替代 |
| **不准确 Title** | Title 与页面实际内容不匹配 | 用页面正文/锚文本生成新 Title |
| **微样板 Title** | 页面集合中 Title 几乎相同，只有一小部分不同 | Google 自动补全差异部分 |
| **无明确主标题** | 页面有多个同等醒目的大标题 | 使用第一个醒目标题 |
| **语言/文字系统不匹配** | Title 语言与页面主内容语言不一致 | 用页面主语言重写 |

> **来源：** Google Search Central Title Link 文档（2025-12）

### 1.4 结构模式

| 页面类型 | 推荐结构 | 示例（中文站） | 示例（英文站） |
|----------|----------|--------------|--------------|
| 首页 | `品牌名 - 一句话定位` | `Aroha - 夏威夷衬衫艺术品牌` | `Aroha - Premium Hawaiian Aloha Shirts` |
| 分类页 | `分类关键词 - 品牌名` | `浮世绘风格衬衫 - Aroha` | `Ukiyo-e Aloha Shirts - Aroha` |
| 产品页 | `产品名 - 分类名 - 品牌名` | `神奈川冲浪里衬衫 - 艺术系列 - Aroha` | `The Great Wave Shirt - Art Collection - Aroha` |
| 博客文章 | `文章标题 - 品牌名` | `夏威夷衬衫穿搭指南 - Aroha 博客` | `How to Style Aloha Shirts - Aroha Blog` |
| 关于页 | `About 品牌名` 或 `品牌故事` | `关于 Aroha` | `About Aroha` |
| 服务/工具页 | `工具名 - 核心功能 - 品牌名` | `免费 SEO 检测工具 - 网站健康度分析` | `Free SEO Audit Tool - Website Health Checker` |

**分隔符建议：** 优先用 `-`（英文半角减号），次选用 `|` 或 `:`。避免用 `,` 或 `>>` 等容易与内容混淆的符号。

### 1.5 品牌名位置与规则

**规则：**
- 品牌名只出现一次，不要重复
- Google 可能在 SERP 中自动补全站点名称（已有站点名称时可能省略品牌名）
- 品牌名要简洁，不要写 `品牌名 - The Best XXX - Sign up - Create Account`

**最佳实践：**
- 品牌名放末尾：`产品名 - 分类 - 品牌名`
- 或放开头（首页/品牌词页面）：`品牌名：核心定位`
- 不要全站所有页面都写 `品牌名 - 关键词`，重复太多

### 1.6 关键词融入原则（Ahrefs + Moz）

**来自 Ahrefs 关键词研究课程的核心洞察：**
> "如果不能匹配搜索意图，你就不会排名。" — Ahrefs Lesson 1

- 每个 Title 只包含 **1 个主关键词** + 1 个次要关键词（可选）
- 主关键词尽量靠左（英文）或靠前（中文）
- 不要同一个词出现多次（如 `项目管理软件, 项目管理工具, 项目管理软件`）
- 关键词要与页面内容完全匹配，否则 Google 会重写

**3C 法则与 Title 的关系（Ahrefs）：**

| 意图类型 | Title 应体现 | 示例 |
|---------|------------|------|
| 信息型（Informational） | 回答性质、疑问词 | `项目管理是什么？完整入门指南` |
| 商业型（Commercial） | 对比/评测角度 | `2025年最佳项目管理软件TOP10对比` |
| 交易型（Transactional） | 产品/购买词 | `购买项目管理软件 - 免费试用` |
| 导航型（Navigational） | 品牌词为主 | `Aroha 官网 - 夏威夷衬衫` |

### 1.7 H1 与 Title 的协同

Google 官方建议："Consider ensuring that your main title is distinctive from other text on a page and stands out as being the most prominent on the page."

- **Title ≠ H1**，但两者应高度一致
- H1 是 Title 的最重要后备来源
- H1 要包含主关键词，与 Title 形成呼应
- 不要让 H2/H3 比 H1 更醒目

### 1.8 常见错误与修复方案

| 错误类型 | 错误示例 | 正确写法 | 修复优先级 |
|---------|---------|---------|----------|
| 超过 60 字符 | `2025年最新最好用的项目管理软件推荐排行榜（免费/付费）完整对比` | `2025年最佳项目管理软件TOP10对比` | P1 |
| 关键词堆砌 | `项目管理软件, 项目管理工具, 任务管理, 团队协作` | `项目管理软件哪个好？2025 TOP10对比` | P1 |
| 每页相同 Title | 所有页面都是 `品牌名 - 官网` | 按页面类型定制（见结构模式） | P0 |
| Title 与 H1 完全不同 | Title: `产品列表` / H1: `浮世绘系列` | 保持一致或互补 | P1 |
| Title 语言与页面不一致 | 页面是中文，Title 写英文 | 用同一种语言 | P0 |
| 半空 Title | `<title>品牌名</title>`（无产品名） | `<title>产品名 - 品牌名</title>` | P0 |
| 微样板 Title | `剧名 S1` / `剧名 S2`（缺季数） | `Season 1 - 剧名`（在 Title 里体现差异） | P1 |

---

## 二、Description（元描述）

### 2.1 长度规范

| 平台 | 字符数 | 说明 |
|------|--------|------|
| 桌面端 | 150-160 字符 | 超出 160 字符大概率被截断 |
| 移动端 | 120-130 字符 | 移动端显示空间更少 |
| 通用建议 | 120-155 字符 | 最安全的范围 |

> **Google 官方说明：** "There's no limit on how long a meta description can be, but the snippet is truncated in Google Search results as needed, typically to fit the device width."（来源：Google Snippet 文档，2026-04 更新）
>
> **关键原则：** meta description 是**建议**，不是**命令**。Google 会根据用户搜索词动态选择最相关的片段，不一定会使用你的 Description。

### 2.2 Google 何时使用你的 Description

| 使用条件 | 说明 |
|---------|------|
| Description 包含用户搜索的关键词 | 搜索词会在 SERP 中**加粗显示** |
| Description 比自动提取的片段更准确地描述页面 | Google 认为你的描述更有用 |
| Description 与页面内容高度匹配 | 不匹配则被忽略 |

### 2.3 Google 何时忽略你的 Description

| 忽略原因 | 说明 |
|---------|------|
| Description 与页面内容不匹配 | Google 认为描述不准确 |
| Description 是样板/重复的 | 所有页面用同一个 Description |
| Description 不包含用户搜索的关键词 | 自动提取的片段更相关 |
| 页面有大量关键词堆砌的 Description | 违反质量准则 |
| 自动提取的片段更相关 | Google 选择更匹配的页面内容 |

### 2.4 Google Snippet 控制手段

| 方法 | 代码 | 作用 |
|------|------|------|
| 完全禁用 Snippet | `<meta name="robots" content="nosnippet">` | Google 不显示任何描述 |
| 限制 Snippet 长度 | `<meta name="robots" content="max-snippet:[数字]">` | 最大字符数（建议 160） |
| 禁止特定内容出现在 Snippet | `<span data-nosnippet>内容</span>` | 指定内容不出现在摘要中 |

### 2.5 写作技巧（Moz + Google + Ahrefs 整合）

| 技巧 | 说明 | 示例 |
|------|------|------|
| **包含目标关键词** | 搜索词会在 SERP 中**加粗**显示，是最重要的技巧 | "想找**项目管理软件**？这篇 TOP10 评测帮你选。" |
| **添加 CTA（行动号召）** | 提升点击率，CTA 词要具体 | "立即免费试用"、"下载领取"、"查看完整对比" |
| **突出 USP（独特卖点）** | 与竞品差异化 | "100%纯棉"、"30天无理由退换"、"支持中文" |
| **匹配搜索意图** | 信息型用"了解/学习"，交易型用"购买/试用" | 信息型：`了解如何选择...` / 交易型：`立即购买...` |
| **包含关键数据** | 价格、数量、评分等具体数据 | "价格$19.99起"、"收录500+教程"、"评分4.8/5" |
| **避免引号 `"`** | Google 在引号处会截断 Description | ❌ `"Best" Shirts` → ✅ `Best Shirts` |
| **每页唯一** | 重复 Description 浪费 SEO 机会 | 不同产品/文章不同描述 |
| **自然语言优先** | 不要像关键词列表，要像对人说话 | ✅ `Aroha creates wearable art...` / ❌ `夏威夷衬衫, 印花, 纯棉...` |

### 2.6 搜索意图与 Description 匹配

| 意图类型 | Description 重点 | 示例 |
|---------|-----------------|------|
| **信息型** | 价值承诺 + 内容概要 + 吸引力 | `了解项目管理的基本原理和最佳实践。本文涵盖 5 种方法、10+ 模板下载，适合团队负责人阅读。` |
| **商业型** | 对比角度 + 评分/排名 + CTA | `2025年8款最佳项目管理软件对比评测。涵盖功能、价格、优缺点，帮你找到最适合团队的工具。` |
| **交易型** | 产品特点 + 促销信息 + 紧迫感 | `The Great Wave Aloha Shirt 现价$89，100%纯棉面料，现货秒发，满$100免运费。立即选购。` |
| **导航型** | 品牌承诺 + 核心价值 | `Aroha 官方中文站。精选 500+ 款夏威夷衬衫，支持全球配送，30天退换。` |

### 2.7 不同页面的 Description 模板

| 页面类型 | 结构 | 示例 |
|----------|------|------|
| **首页** | 品牌定位 + 核心卖点 + 差异化 + CTA | `Aroha 创造可穿戴的艺术品。精选 500+ 款夏威夷衬衫，涵盖浮世绘、梵高、蒙德里安经典艺术图案。100%纯棉，宽松剪裁，全球配送，30天无理由退换。立即探索。` |
| **分类页** | 分类定位 + 产品数量 + 筛选亮点 + CTA | `探索浮世绘艺术系列衬衫——收录 50+ 款以葛饰北斋、梵高等大师作品 为灵感的独家设计。宽松廓形，适合日常与度假穿着。满$80免运费。` |
| **产品页** | 产品名 + 核心特点/材质/规格 + 差异化 + CTA | `The Great Wave Aloha Shirt 复刻葛饰北斋《神奈川冲浪里》经典图案。100%纯棉斜纹布，椰壳纽扣，宽松版型。$89起，现货秒发。立即购买。` |
| **博客文章** | 文章价值主张 + 核心内容预告 + 目标读者 | `夏威夷衬衫怎么穿搭？本指南涵盖 7 种场合的完整穿搭方案，从海滩派对到职场商务。含图片教程，适合所有体型。立即阅读。` |
| **关于页** | 品牌故事 + 价值观 + 差异化 + 信任元素 | `Aroha 成立于2019年，专注将世界艺术经典带入日常生活。我们与艺术家合作，每件产品均是正版授权。坚持可持续生产，碳足迹减少40%。` |

### 2.8 程序化生成 Description（大数据站）

**Google 官方推荐：**
> "For larger database-driven sites, like product aggregators, hand-written descriptions can be impossible. In the latter case, however, programmatic generation of the descriptions can be appropriate and are encouraged."（来源：Google Snippet 文档）

**程序化生成规则：**
- 使用页面特有数据拼接：`品牌 + 产品名 + 核心参数 + 价格 + CTA`
- 示例：`[产品名] - [材质/规格] - [价格] - [品牌名] | [CTA]`
- 确保生成内容是自然语言，不是纯关键词列表
- 每个生成的 Description 都要去重（不要所有产品都是一样的描述）

### 2.9 "Read More" 深度链接（Google 2026 新增）

Google 可以显示指向页面特定章节的 "Read more" 链接。优化建议：
- 确保内容对用户立即可见（不要隐藏在折叠/标签页后面）
- 页面加载时不要强制滚动位置（不要用 JS 控制滚动）
- 使用语义化 HTML（H2/H3 标题结构清晰）

### 2.10 常见错误与修复方案

| 错误类型 | 错误示例 | 正确写法 | 修复优先级 |
|---------|---------|---------|----------|
| 不写 Description | 完全缺失 | 每页必须写独特 Description | P0 |
| 每页相同 Description | 所有产品页用同一个描述 | 按产品/页面定制 | P0 |
| 纯关键词列表 | `衬衫, 夏威夷, 纯棉, 宽松, 艺术` | 自然语言描述 | P1 |
| 与内容不匹配 | Description 说"免费"但页面要付费 | 确保描述反映实际内容 | P0 |
| 包含引号 `"` | `"Best" shirt for summer | Best shirt for summer（去掉引号）| P2 |
| 太短（< 100字符） | `项目管理工具。` | 扩展到 150+ 字符 | P1 |
| 太长（> 160字符） | 超过 160 字符 | 精简到 155 以内 | P1 |
| 关键词堆砌 | 同一关键词出现 5 次以上 | 自然融入 1-3 个关键词 | P1 |

---

## 三、Keywords（元关键词标签）

**结论：不要写。**

| 搜索引擎 | 对 Meta Keywords 的态度 |
|---------|----------------------|
| Google | 2009 年正式宣布不使用，忽略该标签 |
| Bing | 可能轻微参考，但权重极低 |
| Yandex | 曾用作垃圾信号，已弃用 |

**为什么不要写：**
1. 暴露关键词策略给竞争对手
2. 对 SEO 无任何帮助
3. 代码冗余，影响页面整洁度

```html
<!-- ❌ 不要写 -->
<meta name="keywords" content="hawaiian shirts, aloha shirts, ukiyo-e">

<!-- ✅ 正确：不写任何 keywords 标签 -->
```

---

## 四、Title + Description 的协同优化（CTR 提升）

### 4.1 影响 CTR 的元素

| 元素 | CTR 影响 | 优化建议 |
|------|---------|---------|
| Title 关键词位置 | 左侧关键词 CTR 更高 | 主关键词尽量靠左 |
| Description 搜索词加粗 | 关键词匹配时加粗显示 | Description 包含目标搜索词 |
| 数字和年份 | 数字吸引注意力 | `TOP10`、`2025`、`7天` |
| 疑问词 | 引发好奇心 | `为什么...`、`如何...`、`哪个...` |
| 情感词 | 引发情绪反应 | `惊人`、`独家`、`免费`、`完整` |
| 品牌知名度 | 知名品牌 CTR 更高 | 品牌名出现在 Title 末尾 |
| Sitelinks | 占据更多 SERP 空间 | 优化导航结构，触发 Sitelinks |
| 结构化数据 | 富媒体展示 | 添加 Organization/Product Schema |

### 4.2 Ahrefs 3C 法则在 TKD 中的应用

| C | 对 Title 的影响 | 对 Description 的影响 |
|---|--------------|---------------------|
| **Content Type（内容类型）** | 信息型用问句/指南，商业型用对比/评测，交易型用产品名 | 描述要体现内容是什么类型的（评测/教程/产品页） |
| **Content Format（内容格式）** | 列表型用 `TOP10`，教程型用 `指南/教程`，对比型用 `对比` | 说明格式（图文教程、视频、清单等） |
| **Content Angle（内容角度）** | 体现差异化卖点（新鲜度、品牌、独家） | 突出独特角度（为什么选这个而不是那个） |

### 4.3 Featured Snippets 对 TKD 的影响

如果页面有潜力获得 Featured Snippets（精选摘要），TKD 应额外注意：
- **Title**：用问句形式，Google 更倾向从中提取答案
- **Description**：直接回答问题，给出明确结论
- **页面内容**：在 H2 中直接用问题作为标题，答案紧随其后

---

## 五、TKD 完整代码示例

### 5.1 标准 HTML 模板

```html
<head>
  <!-- ✅ 标准写法 -->
  <title>2025年最佳项目管理软件TOP10对比评测 | WorkTool</title>
  <meta name="description" content="想找一款好用的项目管理软件？本文对比2025年最受欢迎的10款工具，涵盖功能、价格、适用场景，帮你快速选到合适的。立即查看完整评测。">

  <!-- ❌ 不要写 keywords -->
  <!-- <meta name="keywords" content="项目管理软件, 任务管理工具, 团队协作"> -->

  <!-- 可选：Open Graph -->
  <meta property="og:title" content="2025年最佳项目管理软件TOP10对比评测">
  <meta property="og:description" content="想找一款好用的项目管理软件？本文对比2025年最受欢迎的10款工具。">
  <meta property="og:type" content="article">
</head>
```

### 5.2 产品页示例

```html
<!-- 产品页 -->
<title>浮世绘神奈川冲浪里 Aloha 衬衫 | 艺术系列 - Aroha</title>
<meta name="description" content="The Great Wave Aloha Shirt 复刻葛饰北斋《神奈川冲浪里》经典图案。100%纯棉斜纹布，椰壳纽扣，宽松版型，男女同款。$89起，现货秒发，满$100免运费。立即选购。">
```

### 5.3 博客文章示例

```html
<!-- 博客文章 -->
<title>夏威夷衬衫怎么穿搭？7种场合完整指南 | Aroha 博客</title>
<meta name="description" content="夏威夷衬衫只能去海滩穿？本指南教你 7 种夏威夷衬衫穿搭方案，涵盖海滩派对、城市休闲、职场商务、约会等场合。含图片教程，适合所有体型。立即阅读。">
```

### 5.4 分类页示例

```html
<!-- 分类页 -->
<title>浮世绘艺术系列衬衫 | 50+ 款经典图案 - Aroha</title>
<meta name="description" content="探索浮世绘艺术系列——收录 50+ 款以葛饰北斋、梵高、莫奈等大师作品为灵感的独家 Aloha 衬衫。宽松廓形，100%纯棉，全球配送。满$80免运费。">
```

---

## 六、TKD 审核清单

### 每次发布前检查

- [ ] **Title 长度：** 桌面端 50-60 字符，移动端 ~40 字符
- [ ] **Description 长度：** 155 字符以内
- [ ] **Title 唯一性：** 每页 Title 都不一样
- [ ] **Description 唯一性：** 每页 Description 都不一样
- [ ] **关键词匹配：** Title 和 Description 中的关键词与页面内容一致
- [ ] **品牌名：** Title 中品牌名只出现一次，放末尾或开头
- [ ] **无关键词堆砌：** Title 和 Description 中同一词不出现超过 2 次
- [ ] **无引号：** Description 中不包含英文双引号 `"`
- [ ] **语言一致：** Title 语言与页面内容语言一致
- [ ] **搜索意图匹配：** Title 和 Description 符合该页面的搜索意图
- [ ] **CTA 存在：** Description 包含明确的行动号召
- [ ] **无过期信息：** Title/Description 中没有过期的年份/日期/价格
- [ ] **H1 与 Title 一致：** H1 与 Title 高度一致，不矛盾

---

## 七、三来源对比总结

| 维度 | Google 官方文档 | Moz Beginner's Guide | Ahrefs Academy |
|------|----------------|---------------------|----------------|
| **Title 长度** | 按像素截断（~600px桌面端） | 50-60 字符 | 与 Google 一致 |
| **Description 长度** | 按设备宽度截断 | 150-160 字符 | 与 Google 一致 |
| **Keywords** | 2009年废弃，不使用 | 不推荐使用 | 不推荐使用 |
| **关键词密度** | 无硬性规定，不要堆砌 | 2-5%，自然出现 | 无硬性规定，匹配意图即可 |
| **Title 重写原因** | 6 大具体原因（官方文档） | 提及但未详细分类 | 未明确提及 |
| **Description 使用条件** | 官方明确：匹配搜索词+内容一致 | 提及吸引力原则 | 强调匹配搜索意图 |
| **Brand 品牌名** | 简洁，不要全站重复 | 放末尾 | 放末尾 |
| **程序化生成** | 官方推荐（大数据站） | 提及 | 提及 |
| **Snippet 控制** | nosnippet/max-snippet/data-nosnippet | 未提及 | 未提及 |

**结论：** 以 Google 官方文档为准，Moz 作为实操补充，Ahrefs 作为意图分析框架。三者不冲突，互补使用。

---

## 八、相关文件索引

| 文件 | 来源 | 与 TKD 相关的内容 |
|------|------|-----------------|
| `references-google/title-link.md` | Google 官方 | Title 生成机制、6大重写原因 |
| `references-google/snippet.md` | Google 官方 | Description 使用条件、Snippet 控制 |
| `references/tkd-standard.md` | 本文档 | TKD 综合规范 |
| `references/keyword-research.md` | 内部整理 | 关键词研究流程、搜索意图分类 |
| `references/on-page-seo.md` | 内部整理 | H1-H6 层级、关键词融入 |
| `references-ahrefs/AHREFS-KEYWORD-RESEARCH-SUMMARY.md` | Ahrefs 课程 | 3C 法则、搜索意图分析 |
| `references-moz/MOZ-LEARNING-SUMMARY.md` | Moz 指南 | Title/Description 长度、页面元素最佳实践 |
