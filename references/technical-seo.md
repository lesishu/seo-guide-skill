# 技术SEO诊断与修复

## 技术SEO检查优先级

### P0 — 影响收录（立即修复）
- robots.txt 屏蔽了重要页面
- canonical 指向错误页面
- 网站完全无法访问（500错误）
- 大量404错误

### P1 — 影响排名（尽快修复）
- 页面速度慢（LCP > 4s）
- 移动端体验差
- HTTPS 未配置
- 缺少 canonical / Open Graph 标签

### P2 — 优化空间（计划修复）
- XML Sitemap 缺失或不完整
- 结构化数据错误
- 图片未压缩/无 Alt
- 缺少面包屑

## 爬虫与索引

### robots.txt
```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /checkout/
Disallow: /cart/

Sitemap: https://example.com/sitemap.xml
```

**检查项：**
- 没有意外 Disallow 核心内容页面
- Sitemap 路径正确

### XML Sitemap

**生成工具：** Screaming Frog / Yoast SEO / Rank Math / 自定义脚本

**规范：**
- 每个 sitemap.xml ≤ 50000 条 URL
- 超过需拆分成多个 sitemap 并用 sitemap-index.xml 聚合
- 包含 `<lastmod>`（最后更新时间）

### Canonical 标签

**使用场景：**
- 动态参数页面（`?page=2`、`?sort=price`）
- HTTP/HTTPS 混合内容
- WWW/非WWW 版本

```html
<link rel="canonical" href="https://example.com/canonical-url/" />
```

### 索引覆盖率

**在 Google Search Console（GSC）检查：**
- 覆盖率报告 → 找出"已排除"的页面（被 canonical/robots 排除的是否符合预期）
- "未编入索引"的原因：重复内容、无内容、软 404

## 页面速度（Core Web Vitals）

### 检测工具
- **PageSpeed Insights**（page-speed.insights.google.com）— 推荐，兼顾实验室数据+真实数据
- **GTmetrix** — 详细瀑布图
- **WebPageTest** — 深度诊断
- **GSC 核心 Web Vitals 报告** — 真实用户体验数据

### 常见优化

| 问题 | 解决方案 |
|------|---------|
| 大图片 | WebP/AVIF 格式，压缩工具：Squoosh、TinyPNG |
| 渲染阻塞资源 | async/defer 加载 JS，内联关键 CSS |
| 服务器响应慢 | 升级主机、使用 CDN（Cloudflare/AWS CloudFront）|
| 未压缩 | 启用 GZIP/Brotli（服务器配置）|
| 字体过大 | 预加载字体子集，使用 `font-display: swap` |
| 第三方脚本 | 延迟加载（广告/分析/聊天工具）|

### 关键指标
```
LCP（最大内容绘制）：目标 < 2.5s
INP（交互到下一绘制）：目标 < 200ms（2024年3月取代FID）
CLS（累积布局偏移）：目标 < 0.1
```

## 移动优先

- 确保 Googlebot- Smartphone 能正常抓取
- 所有内容在移动端可访问（不隐藏）
- 字体大小和按钮间距适配触摸操作（正文 ≥ 16px，按钮间距足够点击）
- 响应式设计，无横向滚动
- 使用 Chrome DevTools 设备模拟测试

## 结构化数据（Schema Markup）

### 验证工具
- **Google Rich Results Test**（search.google.com/test/rich-results）
- **Schema.org Validator**（validator.schema.org）

### 常见错误修复
- `priceCurrency` 缺失 → 添加 ISO 4217 货币代码（如 CNY/USD）
- `image` URL 不正确 → 确保图片可公开访问
- `aggregateRating` 无对应评价内容 → 删除，避免欺骗性结构化数据惩罚

## HTTPS

- 全站 HTTPS（不仅是登录页）
- HTTP → HTTPS 301 重定向
- HSTS 响应头（`Strict-Transport-Security`）配置
- 混合内容（Mixed Content）修复：所有资源走 HTTPS

## 爬虫预算（Crawl Budget）

**大型网站（>1000页）需关注：**
- GSC 中设置抓取速率上限
- 减少重复/低价值页面的抓取（用 canonical/noindex）
- 确保重要页面在 sitemap 中优先

> 🔧 工具一览 → 详见 [seo-tools.md](seo-tools.md)
