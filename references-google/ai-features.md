# AI 功能与网站

> 来源：Google Search Central

---

# AI features and your website

This guide covers how AI features like AI Overviews and AI Mode work in Google Search from a site owner's perspective and how to approach your content's inclusion in these experiences. 

The best practices for SEO remain relevant for AI features in Google Search (such as AI Overviews and AI Mode). There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary. That said, it's always good to review the [fundamental SEO best practices](/search/docs/essentials). 

## How AI features work in Search

As with Search overall, the AI features [AI Overviews](https://support.google.com/websearch/answer/14901683) and [AI Mode](https://support.google.com/websearch/answer/16011537) surface relevant links to help people find the information they're looking for quickly and reliably, as well as to help them explore content they may not have discovered before. These features offer unique opportunities for more types of sites to appear. 

AI Overviews help people get to the gist of a complicated topic or question more quickly, and provide a jumping off point to explore links to learn more. They were designed to show up on queries where they can add additional benefits beyond what people might already get on Search. With AI Overviews, people have been visiting a greater diversity of websites for help with more complex questions. 

AI Mode is particularly helpful for queries where further exploration, reasoning, or complex comparisons are needed. People can ask nuanced questions that might have previously taken multiple searches — from exploring a new concept, to comparing options, and beyond — and get a comprehensive AI-powered response with links to supporting websites. 

Both AI Overviews and AI Mode may use a "query fan-out" technique — issuing multiple related searches across subtopics and data sources — to develop a response. While responses are being generated, our advanced models identify more supporting web pages, allowing us to display a wider and more diverse set of helpful links associated with the response than with a classic web search, enabling new opportunities for exploration. 

AI Mode and AI Overviews may use different models and techniques, so the set of responses and links they show will vary. AI Overviews are only shown when our systems determine that it is additive to classic Search, and as such, often don't trigger. 

## How to appear in AI features

You can apply the same [foundational SEO best practices](/search/docs/essentials) for AI features as you do for Google Search overall: making sure the page meets the [technical requirements for Google Search](/search/docs/essentials/technical), following [Search policies](https://support.google.com/websearch/answer/10622781), and focusing on the [key best practices](/search/docs/essentials#key-best-practices), such as [creating helpful, reliable, people-first content](/search/docs/fundamentals/creating-helpful-content). 

### Technical requirements for appearing in AI features

To be eligible to be shown as a supporting link in AI Overviews or AI Mode, a page must be indexed and eligible to be shown in Google Search with a snippet, fulfilling the [Search technical requirements](/search/docs/essentials/technical). There are no additional technical requirements. 

Just because a page meets all requirements, best practices, and complies with the policies, doesn't mean that Google will crawl, index, or serve its content. Indexing and serving isn't guaranteed. Learn more about [How Search Works](/search/docs/fundamentals/how-search-works). 

### SEO best practices

While specific optimization isn't required for AI Overviews and AI Mode, all existing [SEO fundamentals](/search/docs/fundamentals/seo-starter-guide) continue to be worthwhile, for example: 

  * Ensuring that crawling is allowed in robots.txt, and by any CDN or hosting infrastructure
  * Making your content easily findable through [internal links](/search/docs/crawling-indexing/links-crawlable#internal-links) on your website
  * Providing a great [page experience](/search/docs/appearance/page-experience) for users
  * Making sure that important content is available in textual form
  * Supporting your textual content with high-quality [images](/search/docs/appearance/google-images) and [videos](/search/docs/appearance/video), when applicable
  * Making sure your [structured data](/search/docs/appearance/structured-data/sd-policies) matches the visible text on the page
  * Checking that your [Merchant Center](https://support.google.com/merchants/answer/12159157) and [Business Profile](/search/docs/appearance/establish-business-details) information is up-to-date

You don't need to create new machine readable files, AI text files, or markup to appear in these features. There's also no special schema.org structured data that you need to add. 

To discover and diagnose potential technical issues quickly, [verify your site in Search Console](https://support.google.com/webmasters/answer/9008080). 

## Measuring the performance of your site

Just like the rest of the search results page, sites appearing in AI features (such as AI Overviews and AI Mode) are included in the overall search traffic in [Search Console](https://search.google.com/search-console/about). In particular, they're reported on in the [Performance report](https://support.google.com/webmasters/answer/7576553), within the ["Web" search type](https://support.google.com/webmasters/answer/7576553#by_search_type). Learn more about how [AI Overviews](https://support.google.com/webmasters/answer/7042828#ai-overviews&zippy=%2Ct%2Cai-overviews) and [AI Mode](https://support.google.com/webmasters/answer/7042828#ai-mode&zippy=%2Ct%2Cai-mode) are counted towards the overall data in Search Console, how to [analyze traffic changes](/search/docs/monitor-debug/debugging-search-traffic-drops) overall, and how to [combine Search Console and Analytics data](/search/docs/monitor-debug/google-analytics-search-console). 

In addition to Search Console, you could also track conversions and time spent on your site in other tools, such as Google Analytics. We've seen that when people click from search results pages with AI Overviews, these clicks are higher quality (meaning, users are more likely to spend more time on the site). 

## Controlling your content in AI features in Search

AI is built into Search and integral to how Search functions, which is why robots.txt directives for [Googlebot](/search/docs/crawling-indexing/overview-google-crawlers) is the control for site owners to manage access to how their sites are crawled for Search. To limit the information shown from your pages in Search, use [`nosnippet`, `data-nosnippet`, `max-snippet`](/search/docs/crawling-indexing/robots-meta-tag), or [`noindex`](/search/docs/crawling-indexing/block-indexing) controls. 

To limit AI training and grounding in some of Google's other systems, read more [about Google-Extended](/search/docs/crawling-indexing/google-common-crawlers#google-extended). 

### Troubleshooting preview controls

If you implemented [preview controls](/search/docs/appearance/snippet#nosnippet) and you're still seeing your content appear in AI features on Search, try the following steps: 

  1. Make sure that the preview control is correct and visible to Googlebot. To test if your implementation is correct, use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to see the HTML that Googlebot received while crawling the page.
  2. Allow time for Google to recrawl and process the change in preview controls. Remember that crawling can take anywhere from several days to several months, depending on how often our systems determine a page needs to be refreshed. If you've made changes, you can [request that Google recrawl your pages](/search/docs/crawling-indexing/ask-google-to-recrawl). 

If you tried the troubleshooting steps and still find issues, post in the [Google Search Central Help Community](https://support.google.com/webmasters/thread/227739087).

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
