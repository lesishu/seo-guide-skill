# 语言自适应页面

> 来源：Google Search Central

---

How Google crawls locale-adaptive pages If your site has locale-adaptive pages (that is, your site returns different content based on the perceived country or preferred language of the visitor), Google might not crawl, index, or rank all your content for different locales. This is because the default IP addresses of the Googlebot crawler appear to be based in the USA. In addition, the crawler sends HTTP requests without setting `Accept-Language` in the request header. Important: We recommend using separate locale URL configurations and annotating them with [`rel="alternate"` hreflang annotations](/search/docs/specialty/international/localized-versions). Geo-distributed crawling Googlebot crawls with IP addresses based outside the USA, in addition to the US-based IP addresses. As we have always recommended, when Googlebot appears to come from a certain country, treat it like you would treat any other user from that country. This means that if you block USA-based users from accessing your content, but allow visitors from Australia to see it, your server should block Googlebot if it appears to be coming from the USA, but allow access to Googlebot if it appears to come from Australia. Other considerations

  * Googlebot uses the same user agent string for all crawling configurations. Learn more about the [user agent strings used by Google crawlers](/search/docs/crawling-indexing/overview-google-crawlers).
  * You can [verify Googlebot geo-distributed crawls](/search/docs/crawling-indexing/verifying-googlebot) using reverse DNS lookups.
  * If your site is using the [robots exclusion protocol](https://www.rfc-editor.org/rfc/rfc9309.html), make sure you apply it consistently across locales. This means that [robots `meta` tags](/search/docs/crawling-indexing/robots-meta-tag) and the [robots.txt file](/search/docs/crawling-indexing/robots/create-robots-txt) must specify the same rules in each locale.
