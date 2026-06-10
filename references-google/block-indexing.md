# 阻止索引（noindex）

> 来源：Google Search Central (https://developers.google.com/search/docs/crawling-indexing-block-indexing.txt)

---

# Block Search indexing with `noindex`

`noindex` is a rule set with either a `<meta>` tag or HTTP response header and is used to prevent indexing content by search engines that support the `noindex` rule, such as Google. When Googlebot crawls that page and extracts the tag or header, Google will drop that page entirely from Google Search results, regardless of whether other sites link to it. 

Important: For the `noindex` rule to be effective, the page or resource must not be blocked by a robots.txt file, and it has to be otherwise accessible to the crawler. If the page is blocked by a robots.txt file or the crawler can't access the page, the crawler will never see the `noindex` rule, and the page can still appear in search results, for example if other pages link to it. 

Using `noindex` is useful if you don't have root access to your server, as it allows you to control access to your site on a page-by-page basis. 

## Implementing `noindex`

There are two ways to implement `noindex`: as a `<meta>` tag and as an HTTP response header. They have the same effect; choose the method that is more convenient for your site and appropriate for the content type. Specifying the `noindex` rule in the robots.txt file is not supported by Google. 

You can also combine the `noindex` rule with other rules that control indexing. For example, you can join a `nofollow` hint with a `noindex` rule: `<meta name="robots" content="noindex, nofollow" />`. 

### `<meta>` tag

To prevent all search engines that support the `noindex` rule from indexing a page on your site, place the following `<meta>` tag into the `<head>` section of your page: 
    
    
    <meta name="robots" content="noindex">

To prevent only Google web crawlers from indexing a page:
    
    
    <meta name="googlebot" content="noindex">

Be aware that some search engines might interpret the `noindex` rule differently. As a result, it is possible that your page might still appear in results from other search engines. 

[Read more about the `noindex` `<meta>` tag](/search/docs/crawling-indexing/robots-meta-tag#robotsmeta). 

If you use a CMS, such as Wix, WordPress, or Blogger, you might not be able to edit your HTML directly, or you might prefer not to. Instead, your CMS might have a search engine settings page or some other mechanism to tell search engines about `meta` tags. 

If you want to add a `meta` tag to your website, search for instructions about modifying the `<head>` of your page on your CMS (for example, search for "wix add meta tags"). 

### HTTP response header

Instead of a `<meta>` tag, you can return an `X-Robots-Tag` HTTP header with a value of either `noindex` or `none` in your response. A response header can be used for non-HTML resources, such as PDFs, video files, and image files. Here's an example of an HTTP response with an `X-Robots-Tag` header instructing search engines not to index a page: 
    
    
    HTTP/1.1 200 OK
    (...)
    X-Robots-Tag: noindex
    (...)

[Read more about the `noindex` response header](/search/docs/crawling-indexing/robots-meta-tag#xrobotstag). 

### Debugging `noindex` issues

We have to crawl your page in order to see `<meta>` tags and HTTP headers. If a page is still appearing in results, it's probably because we haven't crawled the page since you added the `noindex` rule. Depending on the importance of the page on the internet, it may take months for Googlebot to revisit a page. You can request that Google recrawl a page using the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289). 

If you need to remove a page of your site quickly from Google's search results, see our [documentation about removals](/search/docs/crawling-indexing/remove-information). 

Another reason could also be that the robots.txt file is blocking the URL from Google web crawlers, so they can't see the tag. To unblock your page from Google, you must [edit your robots.txt file](/search/docs/crawling-indexing/robots/submit-updated-robots-txt). 

Finally, make sure that the `noindex` rule is visible to Googlebot. To test if your `noindex` implementation is correct, use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to see the HTML that Googlebot received while crawling the page. You can also use the [Page Indexing report](https://support.google.com/webmasters/answer/7440203) in Search Console to monitor the pages on your site from which Googlebot extracted a `noindex` rule.

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
