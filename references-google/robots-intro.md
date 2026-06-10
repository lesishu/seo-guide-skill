# robots.txt 入门

> 来源：Google Search Central (https://developers.google.com/search/docs/crawling-indexing-robots-intro.txt)

---

# Introduction to robots.txt

A robots.txt file tells search engine crawlers which URLs the crawler can access on your site. This is used mainly to avoid overloading your site with requests; it is not a mechanism for keeping a web page out of Google. To keep a web page out of Google, [block indexing with `noindex`](/search/docs/crawling-indexing/block-indexing) or password-protect the page. 

If you use a CMS, such as Wix or Blogger, you might not need to (or be able to) edit your robots.txt file directly. Instead, your CMS might expose a search settings page or some other mechanism to tell search engines whether or not to crawl your page. 

If you want to hide or unhide one of your pages from search engines, search for instructions about modifying your page visibility in search engines on your CMS (for example, search for "wix hide page from search engines"). 

## What is a robots.txt file used for?

A robots.txt file is used primarily to manage crawler traffic to your site, and usually to keep a file off Google, depending on the file type: 

robots.txt effect on different file types  
---  
Web page |  You can use a robots.txt file for web pages (HTML, PDF, or other [non-media formats that Google can read](/search/docs/crawling-indexing/indexable-file-types)), to manage crawling traffic if you think your server will be overwhelmed by requests from Google's crawler, or to avoid crawling unimportant or similar pages on your site.  Warning: Don't use a robots.txt file as a means to hide your web pages (including PDFs and other text-based formats supported by Google) from Google Search results.  If other pages point to your page with descriptive text, Google could still index the URL without visiting the page. If you want to block your page from search results, use another method such as password protection or [`noindex`](/search/docs/crawling-indexing/block-indexing).  If your web page is blocked with a robots.txt file, its URL can still appear in search results, but the search result [won't have a description](https://support.google.com/webmasters/answer/7489871). Image files, video files, PDFs, and other non-HTML files embedded in the blocked page will be excluded from crawling, too, unless they're referenced by other pages that are allowed for crawling. If you see this search result for your page and want to fix it, remove the robots.txt entry blocking the page. If you want to hide the page completely from Search, use [another method](/search/docs/crawling-indexing/remove-information#i-control-the-web-page).   
Media file |  Use a robots.txt file to manage crawl traffic, and also to prevent image, video, and audio files from appearing in Google Search results. This won't prevent other pages or users from linking to your image, video, or audio file. 

  **Read more about preventing images from appearing on Google.**
  **Read more about how to remove or restrict your video files from appearing on Google.**

  
Resource file |  You can use a robots.txt file to block resource files such as unimportant image, script, or style files, if you think that pages loaded without these resources won't be significantly affected by the loss. However, if the absence of these resources make the page harder for Google's crawler to understand the page, don't block them, or else Google won't do a good job of analyzing pages that depend on those resources.   
  
## Understand the limitations of a robots.txt file

Before you create or edit a robots.txt file, you should know the limits of this URL blocking method. Depending on your goals and situation, you might want to consider other mechanisms to ensure your URLs are not findable on the web. 

  * robots.txt rules may not be supported by all search engines.  
The instructions in robots.txt files cannot enforce crawler behavior to your site; it's up to the crawler to obey them. While Googlebot and other respectable web crawlers obey the instructions in a robots.txt file, other crawlers might not. Therefore, if you want to keep information secure from web crawlers, it's better to use other blocking methods, such as [password-protecting private files on your server](/search/docs/crawling-indexing/control-what-you-share). 
  * Different crawlers interpret syntax differently.  
Although respectable web crawlers follow the rules in a robots.txt file, each crawler might interpret the rules differently. You should know the [proper syntax](/search/docs/crawling-indexing/robots/robots_txt#syntax) for addressing different web crawlers as some might not understand certain instructions. 
  * A page that's disallowed in robots.txt can still be indexed if linked to from other sites.  
While Google won't crawl or index the content blocked by a robots.txt file, we might still find and index a disallowed URL if it is linked from other places on the web. As a result, the URL address and, potentially, other publicly available information such as anchor text in links to the page can still appear in Google Search results. To properly prevent your URL from appearing in Google Search results, [password-protect the files on your server](/search/docs/crawling-indexing/control-what-you-share), [use the `noindex` `meta` tag or response header](/search/docs/crawling-indexing/block-indexing), or remove the page entirely. 

Caution: Combining multiple crawling and indexing rules might cause some rules to counteract other rules. Learn how to [combine crawling with indexing and serving rules](/search/docs/crawling-indexing/robots-meta-tag#combining). 

## Create or update a robots.txt file

If you decided that you need one, learn how to [create a robots.txt file](/search/docs/crawling-indexing/robots/create-robots-txt). Or if you already have one, learn how to [update it](/search/docs/crawling-indexing/robots/submit-updated-robots-txt). 

Want to learn more? Check out the following resources: 

  **How to write and submit a robots.txt file**
  **Update your robots.txt file**
  **How Google interprets the robots.txt specification**

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
