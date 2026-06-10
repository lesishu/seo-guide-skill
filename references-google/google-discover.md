# Google Discover 指南

> 来源：Google Search Central

---

# Discover and your website

[Discover](https://support.google.com/websearch/answer/2819496) is a part of Google Search that shows people content related to their interests, based on their [Web and App Activity](https://support.google.com/websearch/answer/54068). This page explains more about how content may appear in Discover and best practices for site owners to consider.

## How content appears in Discover

Content is automatically eligible to appear in Discover if it is [indexed by Google](/search/docs/essentials/technical) and meets Discover's [content policies](https://support.google.com/websearch/answer/9982767). No special tags or structured data are required. Note that being eligible to appear in Discover is not a guarantee of appearing.

Content that may appear in Discover includes a wide range of topics that aligns with a person's interests. Older content may appear if it's helpful and relevant to individuals based on their interests. 

If your site violates one or more Discover content policies, Discover manual actions may appear in your Search Console under Security and Manual actions. Learn more about the [types of violations and how to fix them](https://support.google.com/webmasters/answer/9044175#news_discover&zippy=%2Cnews-and-discover-policy-violations).

As part of Google Search, Discover makes use of many of the same signals and [systems](/search/docs/appearance/ranking-systems-guide) used by Search to determine what is helpful, people-first content. Given this, those looking for success with Discover should review our advice on [creating helpful, reliable, people-first content](/search/docs/fundamentals/creating-helpful-content). 

To increase the likelihood of your content appearing in Discover, we recommend the following:

  * Avoid clickbait and similar tactics to artificially inflate engagement by using misleading or exaggerated details in preview content (title, snippets, or images) to increase appeal, or by withholding crucial information required to understand what the content is about.
  * Use page titles and headlines that capture the essence of the content.
  * Avoid sensationalism tactics that manipulate appeal by catering to morbid curiosity, titillation, or outrage.
  * Provide content that's timely for current interests, tells a story well, or provides unique insights.
  * Include compelling, high-quality images in your content that are relevant, especially large images that are more likely to generate visits from Discover. We recommend using images that meet the following specifications: 
    * At least 1200 px wide
    * High resolution of more than 300,000 total pixels (for example, a 16:9 image that's 1280x720 pixels would have 921,600 total pixels and satisfies this specification)
    * 16x9 aspect ratio  Google tries to automatically crop the image for use in Discover. If you choose to crop your images yourself, be sure your images are well-cropped and positioned for landscape usage, and avoid automatically applying an aspect ratio. For example, if you crop a vertical image into 16x9 aspect ratio, be sure the important details are included in the cropped version that you specify in the `og:image` `meta` tag). 
    * Enabled by the [`max-image-preview:large` setting](/search/docs/crawling-indexing/robots-meta-tag#max-image-preview), or by using [AMP](https://www.ampproject.org/)
  * Use either [schema.org markup](/search/docs/appearance/google-images#schema-primary-image-of-page) or the `og:image` `meta` tag to specify a large image that's relevant and representative of the web page, as this can influence which image is chosen as the thumbnail in Discover. Learn [more about how to specify your preferred image](/search/docs/appearance/google-images#specify-preferred-image). 
    * Avoid using generic images (for example, your site logo) in the schema.org markup or `og:image` `meta` tag.
    * For best results, avoid using text-heavy images in the schema.org markup or `og:image` `meta` tag.
  * Provide an overall great page experience. For more advice, check out our help page on [Understanding page experience in Google Search results](/search/docs/appearance/page-experience).

To deliver a good user experience, Discover seeks to present content that's suitable for interest-based feeds, such as articles and videos, as well as filter out content that's not wanted or that might confuse readers. For example, Discover might not recommend job applications, petitions, forms, code repositories, or satirical content without any context. Discover makes use of [SafeSearch](/search/docs/crawling-indexing/safesearch) but beyond that filters out content that might be seen as shocking or unexpected.

## Why Discover traffic might change over time

Traffic from Discover is less predictable or dependable when compared to keyword-driven search visits. Given its serendipitous nature, you should consider traffic from Discover as supplemental to your keyword-driven search traffic. Here are some reasons why Discover traffic may fluctuate: 

  * Changing interests: Discover is designed and always improving to show content aligned with what someone is interested in, which in part can be based on their search activity. If someone is no longer as interested in a particular topic—perhaps reflected by a decline in searching for it—their Discover feed might show other content they're more interested in. In turn, this may cause changes in traffic for publishers. 
  * Content types: Discover has and continues to adjust the types of content that might appear on the feed to better align with what people are looking for. Discover regularly shows content including but not limited to sports, health, entertainment, and lifestyle content from across the open web. 
  * Updates to Google Search: Periodically, we also make [updates to Search](https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history) designed to better provide people with links to helpful content. Because Discover is an extension of Search, updates can sometimes produce traffic changes. If you notice changes to your website's performance after an update, it may be useful to review our documentation on [Google Search's core updates and your website](/search/docs/appearance/core-updates).  However, it may be that there's nothing you need to do after an update. Our ongoing work to improve Discover's user experience means sites may see changes in their traffic that are unrelated to the quality or publishing frequency of their content. 

## Monitor your performance on Discover

If you have content on Discover, you can monitor your performance using the [Performance report for Discover](https://support.google.com/webmasters/answer/9216516). This report shows impressions, clicks, and CTR for any of your content that has appeared on Discover in the last 16 months, as long as your data reaches a minimum threshold of impressions. The Discover performance report [includes traffic from Chrome](/search/blog/2021/02/search-console-performance-discover-chrome), and fully tracks a site's Discover traffic across all surfaces where users interact with Discover.

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.
