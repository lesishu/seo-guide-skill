# 外链限定（rel=sponsored/ugc/nofollow）

> 来源：Google Search Central (https://developers.google.com/search/docs/crawling-indexing-qualify-outbound-links.txt)

---

# Qualify your outbound links to Google

For certain links on your site, you might want to tell Google your relationship with the linked page. In order to do that, use one of the following `rel` attribute values in the `<a>` tag.

For regular links that you expect Google to fetch and parse without any qualifications, you don't need to add a `rel` attribute. For example:
    
    
    <p>My favorite horse is the <a href="https://horses.example.com/Palomino">palomino</a>.</p>

For other links, use one or more of the following values:

`rel` values  
---  
  
### `rel="sponsored"`

|  Mark links that are advertisements or paid placements (commonly called paid links) with the `sponsored` value. Read more about [Google's stance on paid links](/search/docs/essentials/spam-policies#link-spam).
    
    
    <a rel="sponsored" href="https://cheese.example.com/Appenzeller_cheese">Appenzeller</a>

Note: The `nofollow` attribute was [previously recommended](/search/blog/2019/09/evolving-nofollow-new-ways-to-identify) for these types of links and is still an acceptable way to flag them, though `sponsored` is preferred.   
  
### `rel="ugc"`

|  We recommend marking user-generated content (UGC) links, such as comments and forum posts, with the `ugc` value.
    
    
    <a rel="ugc" href="https://cheese.example.com/Appenzeller_cheese">Appenzeller</a>

If you want to recognize and reward trustworthy contributors, you might remove this attribute from links posted by members or users who have consistently made high-quality contributions over time. Read more about how to [prevent user-generated spam on your site and platform](/search/docs/monitor-debug/prevent-abuse).  
  
### `rel="nofollow"`

|  Use the `nofollow` value when other values don't apply, and you'd rather Google not associate your site with, or crawl the linked page from, your site. For links within your own site, use the [robots.txt `disallow` rule](/search/docs/crawling-indexing/robots/robots_txt#disallow).
    
    
    <a rel="nofollow" href="https://cheese.example.com/Appenzeller_cheese">Appenzeller</a>  
  
### Multiple values

|  You may specify multiple `rel` values as a space- or comma-separated list. Examples:
    
    
    <p>I love <a rel="ugc nofollow" href="https://cheese.example.com/Appenzeller_cheese">Appenzeller</a> cheese.</p>
    
    
    <p>I hate <a rel="ugc,nofollow" href="https://cheese.example.com/blue_cheese">Blue</a> cheese.</p>  
  
Links marked with these `rel` attributes will generally not be followed. Remember that the linked pages may be found through other means, such as sitemaps or links from other sites, and thus they may still be crawled. These `rel` attributes are used only in [`<a>` elements that Google can crawl](/search/docs/crawling-indexing/links-crawlable#crawlable-links), except `nofollow`, which is also available as [robots `meta` tag](/search/docs/crawling-indexing/special-tags).

If you need to prevent Google from fetching a link to a page on your own site, use the [robots.txt `disallow` rule](/search/docs/crawling-indexing/robots/robots_txt#disallow).

To prevent Google from indexing a page, allow crawling and use the [`noindex` robots rule](/search/docs/crawling-indexing/block-indexing).

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
