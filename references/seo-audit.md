# SEO 诊断与审计

两个视角：**Part A 快速诊断**（单页/首页速查）和 **Part B 全面审计**（全站体检）。单页优化先看 A，全站 SEO 体检用 B。

---

## Part A：快速诊断（单页速查）

> 适用于诊断单个页面或首页，快速定位常见 SEO 问题。

### 必查 11 项

1. **Title** — 60字符以内，包含核心关键词，避免重复
2. **Meta Description** — 150-160字符，自然语言，含 CTA
3. **H1** — 每页1个，包含主关键词，注意拼写
4. **Canonical URL** — 必须声明，避免 index.html 等重复
5. **Viewport meta** — 移动端适配必需
6. **HTTPS** — 现在是基本要求
7. **OG 标签** — og:title、og:description、og:image、og:site_name
8. **JSON-LD 结构化数据** — Product/Article/Organization 按需添加
9. **图片** — 至少1张带 alt 属性
10. **内链** — 每页至少3-5个内部链接
11. **hreflang** — 多语言站点必须声明

### 常见踩坑

- AggregateRating 样本量过少（如9条）会被 Google 视为刷评风险
- URL 含 index.html 会分散权重，应301重定向
- og:type 漏填会导致社交分享异常
- datePublished/dateModified 未声明影响时效性内容排名

---

## Part B：全面审计（全站体检）

> 适用于全站 SEO 体检，涵盖技术、页面、内容、站外、本地、监控六大维度。

### 一、技术 SEO
> 诊断与修复方法详见 [technical-seo.md](technical-seo.md)

### 爬虫与索引
- [ ] 网站可正常访问，无 500/502/503 错误
- [ ] robots.txt 存在且配置正确（未被意外屏蔽）
- [ ] XML Sitemap 存在、格式正确、已提交到 GSC
- [ ] 核心页面均被 Google 索引（用 `site:example.com` 搜索验证）
- [ ] 无意外 noindex 或 canonical 错误排除

### 页面速度（Core Web Vitals）
- [ ] LCP ≤ 2.5s
- [ ] INP ≤ 200ms（或 FID ≤ 100ms）
- [ ] CLS ≤ 0.1
- [ ] 移动端页面速度达标（PageSpeed Insights 绿色）

### 移动端
- [ ] 全站响应式设计
- [ ] 移动端可正常访问所有内容（无隐藏内容）
- [ ] 通过 Google Mobile-Friendly Test

### 安全与协议
- [ ] 全站 HTTPS
- [ ] 无混合内容问题（HTTP 资源已替换为 HTTPS）

### 结构化数据
- [ ] 重要页面已添加对应 Schema（Article/Product/FAQ 等）
- [ ] 结构化数据通过 Google Rich Results Test 验证
- [ ] 无 Schema 错误

### 重复内容
- [ ] 无大量重复的 Title / Meta Description
- [ ] 正确使用 canonical 处理重复/参数页面
- [ ] HTTP/HTTPS 版本、WWW/非WWW 版本已统一

---

## 二、页面 SEO（On-Page）
> 优化方法详见 [on-page-seo.md](on-page-seo.md)

### 标题与描述
- [ ] 每个页面有唯一且描述性的 Title（50-60 字符）
- [ ] 每个页面有唯一且有吸引力的 Meta Description（150-160 字符）
- [ ] Title 和 Meta Description 均包含目标关键词

### 内容质量
- [ ] 内容满足用户搜索意图
- [ ] 无大量低质量/薄内容页面（< 100 字、无实质内容）
- [ ] 定期更新重要文章（内容不过时）
- [ ] E-E-A-T 信号明确（作者信息、引用来源、联系方式）

### 结构与格式
- [ ] 每个页面有且仅有一个 H1
- [ ] 标题层级清晰（H1 → H2 → H3 不跳级）
- [ ] URL 简短、描述性、含关键词
- [ ] 适当使用项目符号、表格、图片

### 图片
- [ ] 所有图片有描述性 Alt 文本
- [ ] 图片已压缩（< 100KB，WebP/AVIF 优先）
- [ ] 添加了 `loading="lazy"`
- [ ] 响应式图片尺寸（`srcset`）

### 内链
- [ ] 每个页面有 2+ 内链（导航或正文）
- [ ] 内链锚文本描述目标页面内容
- [ ] 无死链（404）

---

## 三、内容 SEO
> 关键词策略详见 [keyword-research.md](keyword-research.md)，内容策略详见 [content-strategy.md](content-strategy.md)

### 关键词策略
- [ ] 有明确的目标关键词（每个重要页面）
- [ ] 主要关键词在 Title、H1、首段中出现
- [ ] 长尾关键词有对应页面覆盖
- [ ] 无关键词堆砌（密度 2-5%）

### 内容深度
- [ ] 核心主题内容深度足够（完整回答用户问题）
- [ ] 涵盖相关子主题（内链结构体现）
- [ ] 定期增加/更新内容（内容新鲜度）

### 新内容
- [ ] 有持续的内容发布计划
- [ ] 新内容覆盖用户真实搜索需求
- [ ] 有针对长尾关键词的内容布局

---

## 四、站外 SEO（Off-Page）
> 外链建设方法详见 [link-building.md](link-building.md)

### 外链
- [ ] 有持续的外链建设策略
- [ ] 无垃圾/黑帽外链
- [ ] 定期监控外链变化（新链/丢失）
- [ ] 外链来源多样化（非单一渠道）

### 品牌信号
- [ ] 社交媒体有品牌存在（微博/微信/抖音/小红书等）
- [ ] 品牌提及（无链接的提及）持续增长
- [ ] Google 品牌词搜索结果正面

---

## 五、本地 SEO（如适用）
> 本地 SEO 详解详见 [local-seo.md](local-seo.md)

- [ ] Google Business Profile 已创建并验证
- [ ] GBP 信息完整（名称、地址、电话、服务、营业时间）
- [ ] NAP（名称、地址、电话）全网一致
- [ ] 有真实客户评价，定期回复
- [ ] 本地关键词有对应落地页

---

## 六、分析与监控

### 数据设置
- [ ] Google Analytics 4（GA4）已安装并正常工作
- [ ] Google Search Console（GSC）已验证并连接
- [ ] Conversion Tracking 配置正确

### 定期监控
- [ ] 月度检查：GSC 覆盖率、核心指标变化
- [ ] 月度检查：关键词排名变化（前 20 关键词）
- [ ] 季度检查：外链变化（新增/丢失）
- [ ] 季度检查：内容更新（过时内容刷新）
- [ ] 监控异常：流量/排名大幅下降（可能受惩罚）

---

> 🔧 **审计工具一览** → 详见 [seo-tools.md](seo-tools.md)
