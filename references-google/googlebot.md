# Googlebot 指南

> 来源：Google Search Central (https://developers.google.com/search/docs/crawling-indexing-googlebot.txt)

---

# Googlebot

Googlebot is the generic name for two types of [web crawlers](/search/docs/fundamentals/how-search-works) used by Google Search: 

  **Googlebot Smartphone**: a mobile crawler that simulates a user on a mobile device. 
  **Googlebot Desktop**: a desktop crawler that simulates a user on desktop. 

You can identify the subtype of Googlebot by looking at the [HTTP `user-agent` request header](/search/docs/crawling-indexing/overview-google-crawlers) in the request. However, both crawler types obey the same product token (user agent token) in robots.txt, and so you cannot selectively target either Googlebot Smartphone or Googlebot Desktop using robots.txt. 

For most sites Google Search primarily [indexes the mobile version](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) of the content. As such the majority of Googlebot crawl requests will be made using the mobile crawler, and a minority using the desktop crawler. 

## How Googlebot accesses your site

For most sites, Googlebot shouldn't access your site more than once every few seconds on average. However, due to delays it's possible that the rate will appear to be slightly higher over short periods. If your site is having trouble keeping up with Google's crawling requests, you can [reduce the crawl rate.](/search/docs/crawling-indexing/reduce-crawl-rate)

When crawling for Google Search, Googlebot crawls the first 2MB of a [supported file type](/search/docs/crawling-indexing/indexable-file-types), and the first 64MB of a PDF file. From a rendering perspective, each resource referenced in the HTML (such as CSS and JavaScript) is fetched separately, and each resource fetch is bound by the same file size limit that applies to other files (except PDF files).  
Once the cutoff limit is reached, Googlebot stops the fetch and only sends the already downloaded part of the file for indexing consideration. The file size limit is applied on the uncompressed data. Other Google crawlers, for example Googlebot Video and Googlebot Image, may have [different limits](/crawling/docs/crawlers-fetchers/overview-google-crawlers#file-size-limits). 

When crawling from IP addresses in the US, the timezone of Googlebot is [Pacific Time](https://g.co/kgs/WSf8oR). 

Other [technical properties of Googlebot](/search/docs/crawling-indexing/overview-google-crawlers#crawl-technical-props) are described in the overview of Google's crawlers. 

## Blocking Googlebot from visiting your site

Googlebot discovers new URLs to crawl primarily from links embedded in previously crawled pages. It's almost impossible to keep a site secret by not publishing links to it. For example, as soon as someone clicks a link from your "secret" site to another site, your "secret" site URL may appear in the referrer tag and can be stored and published by the other site in its referrer log. 

If you want to prevent Googlebot from crawling content on your site, you have a [number of options](/search/docs/crawling-indexing/control-what-you-share). Remember there's a difference between crawling and indexing; blocking Googlebot from crawling a page doesn't prevent the URL of the page from appearing in search results: 

  * Prevent Googlebot from crawling a page? Use a [robots.txt file](/search/docs/crawling-indexing/robots/intro). 
  * Don't want Google to index a page? Use [`noindex`](/search/docs/crawling-indexing/block-indexing). 
  * Prevent a page from being accessible at all by both crawlers or users? Use [another method, such as password protection](/search/docs/crawling-indexing/control-what-you-share). 

Blocking Googlebot affects Google Search (including Discover and all Google Search features), as well as other products such as Google Images, Google Video, and Google News. 

## Verifying Googlebot

Before you decide to block Googlebot, be aware that the HTTP `user-agent` request header used by Googlebot is often spoofed by other crawlers. It's important to verify that a problematic request actually comes from Google. The best way to verify that a request actually comes from Googlebot is to [use a reverse DNS lookup](/search/docs/crawling-indexing/verifying-googlebot#manual) on the source IP of the request, or to match the source IP against the [Googlebot IP ranges](/search/docs/crawling-indexing/verifying-googlebot#use-automatic-solutions).

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-03 UTC.
