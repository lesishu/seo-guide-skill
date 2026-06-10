# Sitemap 入门

> 来源：Google Search Central (https://developers.google.com/search/docs/crawling-indexing-sitemaps-overview.txt)

---

# Learn about sitemaps

A sitemap is a file where you provide information about the pages, videos, and other files on your site, and the relationships between them. Search engines like Google read this file to crawl your site more efficiently. A sitemap tells search engines which pages and files you think are important in your site, and also provides valuable information about these files. For example, when the page was last updated and any alternate language versions of the page. 

You can use a sitemap to provide information about specific types of content on your pages, including [video](/search/docs/crawling-indexing/sitemaps/video-sitemaps), [image](/search/docs/crawling-indexing/sitemaps/image-sitemaps), and [news](/search/docs/crawling-indexing/sitemaps/news-sitemap) content. For example: 

  * A sitemap video entry can specify the video running time, rating, and age-appropriateness rating. 
  * A sitemap image entry can include the location of the images included in a page. 
  * A sitemap news entry can include the article title and publication date. 

If you're using a CMS such as WordPress, Wix, or Blogger, it's likely that your CMS has already [made a sitemap available to search engines](/search/docs/crawling-indexing/sitemaps/build-sitemap#cmssitemap) and you don't have to do anything. 

## Do I need a sitemap?

If your site's pages are properly linked, Google can usually discover most of your site. Proper linking means that all pages that you deem important can be reached through some form of navigation, be that your site's menu or links that you placed on pages. Even so, a sitemap can improve the crawling of larger or more complex sites, or more specialized files. 

A sitemap helps search engines discover URLs on your site, but it doesn't guarantee that all the items in your sitemap will be crawled and indexed. However, in most cases, your site will benefit from having a sitemap. 

You might need a sitemap if:

  * Your site is large. Generally, on large sites it's more difficult to make sure that every page is linked by at least one other page on the site. As a result, it's more likely [Googlebot](/search/docs/crawling-indexing/googlebot) might not discover some of your new pages. 
  * Your site is new and has few external links to it. Googlebot and other web crawlers crawl the web by accessing URLs found in previously crawled pages. As a result, Googlebot might not discover your pages if no other sites link to them. 
  * Your site has a lot of rich media content (video, images) or is shown in Google News. Google can take additional information from sitemaps into account for Search. 

You might not need a sitemap if:

  * Your site is "small". By small, we mean about 500 pages or fewer on your site. Only pages that you think need to be in search results count toward this total. 
  * Your site is comprehensively linked internally. This means that Googlebot can find all the important pages on your site by following links starting from the home page. 
  * You don't have many media files (video, image) or news pages that you want to show in search results. Sitemaps can help Google find and understand video and image files, or news articles, on your site. If you don't need these results to appear in Search you might not need a sitemap. 

## Build a sitemap

If you decided that you need a sitemap, [learn more about how to create one](/search/docs/crawling-indexing/sitemaps/build-sitemap).

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
