# 临时关闭或暂停网站

> 来源：Google Search Central

---

# Temporarily pause or disable a website

If you're unable to fulfill orders or many of your products out of stock, you may be considering temporarily closing your online business. If the situation is temporary, meaning you expect to be able to sell products in the coming weeks or months, we recommend that you take action that preserves as much of your site's standing in Search as possible. This guide explains how you can safely pause your online business. 

##  Limit your site's functionality (recommended) 

If your situation is temporary and you plan to reopen your online business, we recommend that you keep your site online and limit the functionality. This is the recommended approach since it minimizes any negative effects on your site's presence in Search. People can still find your products, read reviews, or add wishlists so they can purchase at a later time. We recommend doing the following: 

  * Disable the cart functionality: Disabling the cart functionality is the simplest approach, and doesn't change anything for your site's visibility in Search.
  * Display a banner or popup: A banner or popup div on all pages including the landing page quickly makes the status clear to users. Mention any known and unusual delays, shipping times, pick-up or delivery options, so that users continue with the right expectations. To prevent the content in the banner or popup from being shown in a snippet in Search results, use the [`data-nosnippet` HTML attribute](/search/docs/crawling-indexing/robots-meta-tag#data-nosnippet-attr). Make sure to follow our [guidelines on popups and banners](/search/docs/appearance/avoid-intrusive-interstitials).
  * Update your structured data: If your site uses structured data (for example, [`Product`](/search/docs/appearance/structured-data/product), [`Book`](/search/docs/appearance/structured-data/book), [`Event`](/search/docs/appearance/structured-data/event)), make sure to adjust it appropriately (reflecting the current product availability, or changing events to cancelled). If your business has a physical storefront, update [Local Business structured data](/search/docs/appearance/structured-data/local-business) to reflect current opening hours.
  * Check your Merchant Center feed: If you use Merchant Center, follow the [best practices for the availability attribute](https://support.google.com/merchants/answer/6324448).
  * Tell Google about your updates: To ask Google to recrawl a limited number of pages (for example, the home page), use [Search Console](/search/docs/crawling-indexing/ask-google-to-recrawl). For a larger number of pages (for example, all of your product pages), [use sitemaps](/search/docs/guides/submit-URLs).

## Not recommended: Disable the whole website 

Warning: Google's systems are designed to be robust and to help websites recover from temporary issues. However, removing a site completely from Google's index is a significant change that can take quite some time to recover from. There's no fixed time for a recovery from a complete removal, and there's no mechanism to speed that up. This is why we strongly recommend limiting functionality instead of removing the site from Search.

You may decide to disable the whole website. This is an extreme measure that should only be taken for a very short period of time (a few days at most), as it will otherwise have significant effects on the website in Search, even when implemented properly. 

Make sure that you consider the following side effects of disabling your entire site: 

  * Your customers won't know what's happening with your business if they can't find your business online at all.
  * Your customers can't find or read first-hand information about your business and its example, reviews, specs, repair guides, or manuals won't be findable. Third-party information may not be as correct or comprehensive as what you can provide. This often also affects future purchase decisions. 
  * Knowledge Panels may lose information, like contact phone numbers and your site's logo.
  * Search Console verification will fail, and you will lose all access to information about your business in Search. Aggregate reports in Search Console will lose data as pages are dropped from the index.
  * Ramping back up after a prolonged period of time will be significantly harder if your website needs to be reindexed first. Additionally, it's uncertain how long this would take, and whether the site would appear similarly in Search afterwards.

If you decide that you need to do this (again, not recommended), here are some options:

  * If you need to urgently disable the site for 1-2 days, then return an informational error page with a [`503` HTTP response status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) instead of all content. Make sure to follow the best practices for disabling a site.
  * If you need to disable the site for a longer time, then provide an indexable home page as a placeholder for users to find in Search by using the `200` HTTP status code.
  * If you quickly need to hide your site in Search while you consider the options, you can [temporarily remove a website from Search](https://support.google.com/webmasters/answer/9689846).

###  Best practices for disabling a site 

Warning: Keep in mind that it's not possible for Google's systems to refresh titles, descriptions, metadata, or structured data included on a website if a page returns a `503` HTTP response status code.

While we don't recommend disabling your site, here are some best practices if you decide to do this: 

  * Continue to allow crawling through the robots.txt file. Don't return a `503` HTTP response status code for the robots.txt file because this blocks all crawling. 
  * Confirm a `503` HTTP response status code locally by using [curl](https://curl.haxx.se/docs/manpage.html) or a similar tool. For example: 
    
        curl -I -X GET "https://www.example.com/"
    HTTP/1.1 503 Service Unavailable
    Mime-Version: 1.0
    Content-Type: text/html
    (...)

  * To minimize the server-side and client-side load of a `503` error page, follow these best practices: 
    * Use the [`retry-after` HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) with a best effort date or duration.
    * Use static HTML.
    * Minimize off-page resources; use inline CSS stylesheets and base-64-encoded images.
  * Give your users clear guidance on future steps within the content of the error page. This could include: 
    * Links to more information
    * The date when you expect the website to be online again, or when the information will be updated
    * How to contact customer service
  * Don't disallow all crawling in the robots.txt file. Returning a valid robots.txt file that disallows all crawling may remove the website's content, and potentially its URLs, from Google Search.
  * Don't block the website by returning `403`, `404`, `410` HTTP status codes, or with a `noindex` robots `meta` tag or x-robots-tag HTTP header. This will remove the website's URLs from Google Search.
  * Don't use the temporary website removal tool in Search Console for closures. Doing so will make it impossible for users to find your website so that they can learn its status. Also, potential resellers or affiliates of your business's products may continue to be shown in Search.
  * Don't block your robots.txt file with a `503` HTTP response status code.

##  FAQs 

###  What if I only close the site for a few weeks? 

Completely closing a site even for just a few weeks can have negative consequences on Google's indexing of your site. We recommend limiting the site functionality instead. Keep in mind that users may also want to find information about your products, your services, and your company, even if you're currently not selling anything. 

###  What if I want to exclude all non-essential products? 

That's fine. Make sure that people can't buy the non-essential products by limiting the site functionality. 

###  Can I ask Google to crawl less while my site is temporarily closed? 

Yes, you can [reduce the Googlebot crawl rate](/search/docs/guides/reduce-crawl-rate), though it's not recommended for most cases. This may have some impact on the freshness of your results in Search. For example, it may take longer for Search to reflect that all of your products are currently not available. On the other hand, if Googlebot's crawling causes critical server resource issues, this is a valid approach. We recommend setting a reminder for yourself to reset the crawl rate once you're ready to go back in business. 

###  How do I get a page indexed or updated quickly? 

To ask Google to recrawl a limited number of pages (for example, the home page), use [Search Console](/search/docs/crawling-indexing/ask-google-to-recrawl). For a larger number of pages (for example, all of your product pages), [use sitemaps](/search/docs/guides/submit-URLs). 

###  What if I block a specific region from accessing my site? 

Google generally crawls from the US. If you block the US, Google Search won't be able to access your site at all. We don't recommend that you block an entire region from temporarily accessing your site; instead, we recommend limiting the site functionality for that region. 

###  Should I use the [Removals Tool](https://support.google.com/webmasters/answer/9689846) to remove out-of-stock products? 

No. If you do this, customers won't be able to find first-hand information about your products on Search, and there might still be third-party information for the product that may be incorrect or incomplete. It's better to still allow that page, and mark it out of stock. That way people can still understand what's going on, even if they can't purchase the item. If you remove the product from Search, people don't know why it's gone.

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
