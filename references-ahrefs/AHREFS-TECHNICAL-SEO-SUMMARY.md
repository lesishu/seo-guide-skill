# Ahrefs Technical SEO Course 学习总结

> 学习时间：2026-04-22
> 来源：Ahrefs Academy (YouTube 视频字幕)
> 共 8 课，约 1.5 小时

---

## Lesson 1: What is Technical SEO and Why is it Important?

### Technical SEO 定义

**Technical SEO = 优化网站让搜索引擎能够发现、理解和索引你的页面**

### 为什么重要

- 如果搜索引擎无法访问、阅读、理解或索引你的页面，你就不会排名
- 避免无意的错误（如把自己从 Google 索引中移除）

### 四个关键问题

#### 1. Noindex Meta Tag

```html
<meta name="robots" content="noindex">
```

- 告诉搜索引擎不要索引该页面
- **常见错误：** 开发阶段添加 noindex，上线后忘记移除
- **检查方法：** 查看页面源代码，搜索 "noindex"

#### 2. Diluting Backlinks（稀释反向链接）

- 同一内容有多个 URL 导致链接权重分散
- **解决方案：** 使用 301 重定向或 canonical 标签

#### 3. Blocked Resources

- robots.txt 阻止了重要资源
- **常见错误：** 阻止 CSS/JS 文件导致 Google 无法正确渲染页面

#### 4. Slow Page Speed

- 页面加载速度影响排名
- 影响用户体验和爬虫效率

---

## Lesson 2: Technical SEO Best Practices for Beginners

### 基础实践清单

#### 1. 使用 HTTPS

- Google 的排名因素
- 浏览器显示"安全"标志
- 用户体验更好

#### 2. 确保 Crawlability（可爬取性）

- 检查 robots.txt
- 确保 important 页面不被阻止
- 使用 GSC 的 robots.txt Testing Tool

#### 3. 确保 Indexability（可索引性）

- 检查 noindex 标签
- 检查 canonical 标签
- 使用 GSC URL Inspection Tool

#### 4. 优化网站结构

- 扁平化结构（3-4 层深度）
- 清晰的导航
- 内部链接

---

## Lesson 3: HTTP vs. HTTPS - How SSL/TLS Encryption Works

### HTTPS 的重要性

- **安全性：** 加密用户数据
- **排名因素：** Google 2014 年宣布为排名信号
- **浏览器警告：** Chrome 对 HTTP 页面显示"不安全"
- **信任度：** 用户更信任 HTTPS 网站

### SSL/TLS 工作原理

1. **握手：** 浏览器请求安全连接
2. **证书验证：** 服务器发送 SSL 证书
3. **密钥交换：** 创建加密会话密钥
4. **加密通信：** 所有数据加密传输

### 如何迁移到 HTTPS

1. 购买 SSL 证书（或使用 Let's Encrypt 免费）
2. 安装证书
3. 设置 301 重定向 HTTP → HTTPS
4. 更新内部链接
5. 更新 sitemap
6. 在 GSC 中添加 HTTPS 版本

---

## Lesson 4: A Basic Technical SEO Audit for Beginners

### 审计清单

#### 1. 可爬取性检查

- **robots.txt 检查：** 确保 important 页面不被阻止
- **sitemap.xml 检查：** 确保所有重要页面都在其中
- **GSC Coverage Report：** 查看索引状态

#### 2. 可索引性检查

- **noindex 标签：** 搜索页面源代码
- **canonical 标签：** 确保指向正确的 URL
- **meta robots：** 检查是否有意外设置

#### 3. 重复内容检查

- **www vs non-www：** 选择一个，重定向另一个
- **HTTP vs HTTPS：** 确保重定向到 HTTPS
- **trailing slash：** 统一 URL 格式

#### 4. 页面速度检查

- 使用 Google PageSpeed Insights
- 优化图片、CSS、JavaScript

---

## Lesson 5: How to Speed Up Your WordPress Website

### WordPress 优化清单

#### 1. 选择好的主机

- 共享主机 vs VPS vs 专用服务器
- 选择响应速度快的主机

#### 2. 使用缓存插件

- WP Rocket（付费）
- W3 Total Cache（免费）
- WP Super Cache（免费）

#### 3. 图片优化

- 压缩图片（TinyPNG, Smush）
- 使用 WebP 格式
- 懒加载（Lazy Loading）

#### 4. 数据库优化

- 清理修订版本
- 删除 spam 评论
- 优化数据库表

#### 5. 减少插件

- 删除不使用的插件
- 避免功能重复的插件
- 使用轻量级主题

#### 6. CDN 使用

- Cloudflare（免费）
- 减少服务器响应时间
- 全球分布式缓存

---

## Lesson 6: How to Use Internal Links to Rank Higher in Google

### 内部链接的重要性

- 帮助 Google 发现和索引页面
- 传递页面权重（PageRank）
- 帮助用户导航

### 内部链接最佳实践

#### 1. 建立清晰的层级结构

- 首页 → 分类页 → 文章页
- 每个页面应该能从首页在 3-4 次点击内到达

#### 2. 使用描述性锚文本

- ❌ "点击这里"
- ✅ "关键词研究完整指南"

#### 3. 链接到重要页面

- 从高权重页面链接到需要提升的页面
- 相关内容之间互相链接

#### 4. 避免孤立页面

- 确保每个页面至少有一个内部链接
- 使用 sitemap 帮助发现

#### 5. 修复断链

- 定期检查 404 错误
- 使用 301 重定向

---

## Lesson 7: SEO Audit - How to Fix Your Website's Technical SEO Issues

### 技术SEO审计流程

#### Step 1: Crawl Your Site

- 使用 Ahrefs Site Audit
- 或 Screaming Frog
- 发现所有技术问题

#### Step 2: 分析关键问题

**高优先级：**
- noindex 页面
- 被 robots.txt 阻止的页面
- 404 错误
- 重复内容

**中优先级：**
- 缺少 title tag
- 缺少 meta description
- 图片缺少 alt text

**低优先级：**
- 长标题
- 短标题
- 次要页面的重复内容

#### Step 3: 修复问题

- 按优先级排序
- 逐个修复
- 验证修复结果

---

## Lesson 8: Core Web Vitals - How to Optimize Them for SEO

### 什么是 Core Web Vitals

Google 的三个核心页面体验指标：

#### 1. LCP (Largest Contentful Paint)

- **定义：** 最大内容元素加载时间
- **目标：** < 2.5 秒
- **优化方法：**
  - 优化服务器响应时间
  - 使用 CDN
  - 优化图片
  - 移除阻塞渲染的资源

#### 2. INP (Interaction to Next Paint)

- **定义：** 页面交互响应速度（原 FID 已被 INP 取代）
- **目标：** < 200 毫秒
- **优化方法：**
  - 减少 JavaScript 执行时间
  - 分解长任务
  - 使用 Web Workers
  - **JavaScript 加载优化：**
    - `async` - 异步下载，下载后立即执行（可能阻塞 LCP）
    - `defer` - 异步下载，HTML 解析完成后执行（推荐）
    - 移除未使用的 JS/CSS
    - 压缩（Minify）代码

#### 3. CLS (Cumulative Layout Shift)

- **定义：** 页面布局稳定性
- **目标：** < 0.1
- **优化方法：**
  - 为图片设置尺寸
  - 预留广告位空间
  - 避免在现有内容上方插入内容

### 如何测量 Core Web Vitals

- **PageSpeed Insights：** https://pagespeed.web.dev/
- **Chrome DevTools：** Lighthouse 面板
- **Google Search Console：** Core Web Vitals 报告

### 优化策略

1. **优先修复移动端：** Mobile-first indexing
2. **关注最差的页面：** 从 GSC 中找出 "Poor" 页面
3. **持续监控：** 使用 GSC 或其他工具定期检查

---

## Ahrefs vs Moz vs Google 对比

| 维度 | Google SEO Guide | Moz Guide | Ahrefs Technical SEO |
|------|------------------|-----------|---------------------|
| **Core Web Vitals** | 有文档 | 提及 | **详细优化指南** |
| **审计流程** | 分散在各章节 | 有清单 | **完整演示** |
| **WordPress 优化** | 无 | 无 | **专门课程** |
| **内部链接策略** | 有提及 | 有 | **专门课程** |
| **SSL/HTTPS** | 有 | 有 | **详细原理解释** |

### Ahrefs 独特贡献

1. **Core Web Vitals 实战指南：** 具体指标、目标值、优化方法
2. **WordPress 专门优化：** 实用的 WordPress SEO
3. **审计演示：** 完整的审计流程
4. **内部链接策略：** 如何用内链提升排名

---

## 文件清单

- `techseo-01-what-is-technical-seo.txt` — Lesson 1 字幕
- `techseo-02-technical-seo-best-practices.txt` — Lesson 2 字幕
- `techseo-03-http-vs-https.txt` — Lesson 3 字幕
- `techseo-04-technical-seo-audit.txt` — Lesson 4 字幕
- `techseo-05-speed-up-wordpress.txt` — Lesson 5 字幕
- `techseo-06-internal-links.txt` — Lesson 6 字幕
- `techseo-07-seo-audit-fix-issues.txt` — Lesson 7 字幕
- `techseo-08-core-web-vitals.txt` — Lesson 8 字幕
- `tech_seo_videos.json` — 视频 ID 列表
- `AHREFS-TECHNICAL-SEO-SUMMARY.md` — 本总结文档

---

## 视频链接

| 课次 | 标题 | YouTube ID | 时长 |
|------|------|-----------|------|
| 1 | What is Technical SEO and Why is it Important | _bewU9AvKwU | 7:43 |
| 2 | Technical SEO Best Practices for Beginners | RFlpwKQ0bEs | 6:04 |
| 3 | HTTP vs. HTTPS: How SSL/TLS Encryption Works | AB0VMbvEz7g | 8:11 |
| 4 | A Basic Technical SEO Audit for Beginners | oJPGa0J6p5Q | 8:13 |
| 5 | How to Speed Up Your WordPress Website | BrY6a-lsLp8 | 14:02 |
| 6 | How to Use Internal Links to Rank Higher | 3tbDkc3k48E | 6:02 |
| 7 | SEO Audit: How to Fix Technical SEO Issues | G_9-AkZch4k | 11:54 |
| 8 | Core Web Vitals: How to Optimize Them | LCZzLmIp0H0 | 17:48 |

## 字幕原文索引

> 课程目录：`technical_seo/` (8个文件)

| # | 文件 |
|---|------|
| 1 | [Techseo 01 What Is Technical Seo](technical_seo/techseo-01-what-is-technical-seo.txt) |
| 2 | [Techseo 02 Technical Seo Best Practices](technical_seo/techseo-02-technical-seo-best-practices.txt) |
| 3 | [Techseo 03 Http Vs Https](technical_seo/techseo-03-http-vs-https.txt) |
| 4 | [Techseo 04 Technical Seo Audit](technical_seo/techseo-04-technical-seo-audit.txt) |
| 5 | [Techseo 05 Speed Up Wordpress](technical_seo/techseo-05-speed-up-wordpress.txt) |
| 6 | [Techseo 06 Internal Links](technical_seo/techseo-06-internal-links.txt) |
| 7 | [Techseo 07 Seo Audit Fix Issues](technical_seo/techseo-07-seo-audit-fix-issues.txt) |
| 8 | [Techseo 08 Core Web Vitals](technical_seo/techseo-08-core-web-vitals.txt) |