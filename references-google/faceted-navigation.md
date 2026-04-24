# 分面导航（Faceted Navigation）管理

> 来源：Google Search Central

---

** Crawling infrastructure **

  ** Home  **
  ** Docs  **

  **Intro**
  **About Google's web crawling**
  * How to...

  **Verify requests from Google**
  **Reduce Google's crawl rate**
  * Use robots.txt to manage crawling

    **Create and submit a robots.txt file**
    **How Google interprets the robots.txt specification**
    **Update your robots.txt file**
    **List of useful robots.txt rules**

  * Optimize crawling performance

    **Optimize your crawl budget**
    **Myths about crawling**
    **Improve crawling of faceted navigation URLs**

  * Reference

  **Common crawlers**
  **Special case crawlers**
  **User-triggered fetchers**
  * Specific crawlers and user-triggered fetchers

    **APIs-Google**
    **Feedfetcher**
    **Googlebot**
    **Google Read Aloud**

  * Troubleshooting

  **HTTP status codes**
  **Network and DNS errors**
  * What's new

  **Changelog**

  ** Home **
  ** Crawling infrastructure **
  ** Docs **

Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managing crawling of faceted navigation URLs

Faceted navigation is a common feature of websites that allows its visitors to change how items (for example, products, articles, or events) are displayed on a page. It's a popular and useful feature, however its most common implementation, which is based on URL parameters, can generate infinite URL spaces which harms the website in a couple ways: 

  * Overcrawling: Because the URLs created for the faceted navigation seem to be novel and crawlers can't determine whether the URLs are going to be useful without crawling first, the crawlers will typically access a very large number of faceted navigation URLs before the crawlers' processes determine the URLs are in fact useless. 
  * Slower discovery crawls: Stemming from the previous point, if crawling is spent on useless URLs, the crawlers have less time to spend on new, useful URLs. 

A typical faceted navigation URL may contain various parameters in the query string related to the properties of items they filter for. For example: 
    
    
    https://example.com/items.shtm?products=fish&color;=radioactive_green&size;=tiny

Changing any of the URL parameters `products`, `color`, and `size` would show a different set of items on the underlying page. This often means a very large number of possible combinations of filters, which translates to a very large number of possible URLs. To save your resources, we recommend dealing with these URLs one of the following ways: 

  * If you don't need the faceted navigation URLs potentially indexed, prevent crawling of these URLs. 
  * If you need the faceted navigation URLs potentially indexed, ensure that the URLs follow our best practices outlined in the following section. Keep in mind that crawling faceted URLs tends to cost sites large amounts of computing resources due to the sheer amount of URLs and operations needed to render those pages. 

## Prevent crawling of faceted navigation URLs

If you want to save server resources and you don't need your faceted navigation URLs to show up in Google Search or other Google products, you can prevent crawling of these URLs with one of the following ways. 

  * Use [robots.txt](/crawling/docs/robots-txt/create-robots-txt) to disallow crawling of faceted navigation URLs. Oftentimes there's no good reason to allow crawling of filtered items, as it consumes server resources for no or negligible benefit; instead, allow crawling of just the individual items' pages along with a dedicated listing page that shows all products without filters applied. 
    
        user-agent: Googlebot
    disallow: /*?*products=
    disallow: /*?*color=
    disallow: /*?*size=
    allow: /*?products=all$
    

  * Use URL fragments to specify filters. [Google Search generally doesn't support URL fragments in crawling and indexing](/search/docs/crawling-indexing/url-structure#fragments). If your filtering mechanism is based on URL fragments, it will have no impact on crawling (positive or negative). For example, instead of URL parameters, use URL fragments: 
    
        https://example.com/items.shtm#products=fish&color;=radioactive_green&size;=tiny

Other ways to signal a preference of which faceted navigation URLs (not) to crawl is using `rel="canonical"` `link` element and the `rel="nofollow"` anchor attribute. However, these methods are generally less effective in the long term than the previously mentioned methods. 

  * Using [`rel="canonical"`](/search/docs/crawling-indexing/consolidate-duplicate-urls#rel-canonical-link-method) to specify which URL is the canonical version of a faceted navigation URL may, over time, decrease the crawl volume of non-canonical versions of those URLs. For example, if you have 3 filtered page types, consider pointing the `rel="canonical"` to the unfiltered version: `https://example.com/items.shtm?products=fish&color;=radioactive_green&size;=tiny` specifies `<link rel="canonical" href="https://example.com/items.shtm?products=fish" >`. 
  * Using [`rel="nofollow"`](/search/docs/crawling-indexing/qualify-outbound-links#nofollow) attributes on anchors pointing to filtered results pages may be beneficial, however keep in mind that every anchor pointing to a specific URL must have the `rel="nofollow"` attribute in order for it to be effective. 

## Ensure the faceted navigation URLs are optimal for the web

If you need your faceted navigation URLs to be potentially crawled and indexed, ensure you're following these best practices to minimize the negative effects of crawling the large number of potential URLs on your site: 

Keep in mind that having these URLs crawled means an increased resource usage on your server and, potentially, slower discovery of new URLs on your site. 

  1. Use the industry standard URL parameter separator '`&`'. Characters like comma (`,`), semicolon (`;`), and brackets (`[` and `]`) are hard for crawlers to detect as parameter separators (because most often they're not separators). 
  2. If you're encoding filters in the URL path, such as `/products/fish/green/tiny`, ensure that the logical order of the filters always stays the same and that no duplicate filters can exist. 
  3. Return an HTTP `404` status code when a filter combination doesn't return results. If there are no green fish in the site's inventory, users as well as crawlers should receive a "not found" error with the proper HTTP status code (`404`). This should also be the case if the URL contains duplicate filters or otherwise nonsensical filter combinations, and nonexistent pagination URLs. Similarly, if a filter combination has no results, don't redirect to a common "not found" error page. Instead, serve a "not found" error with the `404` HTTP status code under the URL where it was encountered.  If [you have a single-page app](/search/docs/crawling-indexing/javascript/javascript-seo-basics#avoid-soft-404s) this might not be possible. Follow the best practices for single page apps. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-18 UTC."],[],[]] 

  * ### Connect

    ** Blog **
    ** Bluesky **
    ** Instagram **
    ** LinkedIn **
    ** X (Twitter) **
    ** YouTube **
  * ### Programs

    ** Google Developer Program **
    ** Google Developer Groups **
    ** Google Developer Experts **
    ** Accelerators **
    ** Google Cloud & NVIDIA **
  * ### Developer consoles

    ** Google API Console **
    ** Google Cloud Platform Console **
    ** Google Play Console **
    ** Firebase Console **
    ** Actions on Google Console **
    ** Cast SDK Developer Console **
    ** Chrome Web Store Dashboard **
    ** Google Home Developer Console **

[ ](https://developers.google.com/)

  ** Android **
  ** Chrome **
  ** Firebase **
  ** Google Cloud Platform **
  ** Google AI **
  ** All products **

  ** Terms **
  ** Privacy **
  * Manage cookies 

  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Polski
  * Português – Brasil
  * Tiếng Việt
  * Türkçe
  * Русский
  * العربيّة
  * हिंदी
  * ภาษาไทย
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어
