# URL 结构最佳实践

> 来源：Google Search Central (https://developers.google.com/search/docs/crawling-indexing-url-structure.txt)

---

# URL structure best practices for Google Search

To make sure Google Search can crawl your site effectively, use a crawlable URL structure that meets the following requirements. If your URLs don't meet the following criteria, Google Search will likely crawl your site inefficiently — including but not limited to extremely high crawl rates, or not at all. 

## Requirements for a crawlable URL structure  
  
---  
  
### Follow [IETF STD 66](https://datatracker.ietf.org/doc/std66/)

|  Google Search supports URLs as defined by [IETF STD 66](https://datatracker.ietf.org/doc/std66/). Characters defined by the standard as [reserved](https://www.rfc-editor.org/rfc/rfc3986#section-2.2) must be [percent encoded](https://developer.mozilla.org/docs/Glossary/Percent-encoding).   
  
### Don't use URL fragments to change content

|  Don't use [fragments](https://wikipedia.org/wiki/URI_fragment) to change the content of a page, as Google Search generally doesn't support URL fragments. Here's an example of a URL fragment: 
    
    
    https://example.com/#/potatoes

If you're using JavaScript to change content, [use the History API](/search/docs/crawling-indexing/javascript/javascript-seo-basics#use-history-api) instead.   
  
### Use a common encoding for URL parameters

|  When specifying URL parameters, use the following common encoding: an equal sign (`=`) to separate key-value pairs and add additional parameters with an ampersand (`&`). To list multiple values for the same key within a key-value pair, you can use any character that doesn't conflict with [IETF STD 66](https://datatracker.ietf.org/doc/std66/), such as a comma (`,`).  |  Recommended  |  Not recommended   
---|---  
Using an equal sign (`=`) to separate key-value pairs and an ampersand (`&`) to add additional parameters: 
    
    
    https://example.com/category?category=dresses&sort;=low-to-high&sid;=789

|  Using a colon (`:`) to separate key-value pairs and brackets (`[ ]`) to add additional parameters: 
    
    
    https://example.com/category?[category:dresses][sort:price-low-to-high][sid:789]  
  
Using a comma (`,`) to list multiple values for the same key, an equal sign (`=`) to separate key-value pairs, and an ampersand (`&`) to add additional parameters: 
    
    
    https://example.com/category?category=dresses&color;=purple,pink,salmon&sort;=low-to-high&sid;=789

|  Using a single comma (`,`) to separate key-value pairs and double commas (`,,`) to add additional parameters: 
    
    
    https://example.com/category?category,dresses,,sort,lowtohigh,,sid,789  
  
## Make it easy to understand your URL structure

To help Google Search (and your users) better understand your site, we recommend creating a simple URL structure, applying the following best practices when possible. 

Consider organizing your content so that URLs are constructed logically and in a manner that is most intelligible to humans. For information on structuring your site as a whole, check out [this section of the SEO Starter Guide](/search/docs/fundamentals/seo-starter-guide#group-topically).  Best practices  
---  
  
### Use descriptive URLs

|  When possible, use readable words rather than long ID numbers in your URLs. |  Recommended (simple, descriptive words)  |  Not recommended (unreadable, long ID numbers)   
---|---  
      
    
    https://example.com/wiki/Aviation

| 
    
    
    https://example.com/index.php?topic=42&area;=3a5ebc944f41daa6f849f730f1  
  
### Use your audience's language

|  Use words in your audience's language in the URL (and, if applicable, transliterated words). For example, if your audience is searching in German, use German words in the URL: 
    
    
    https://example.com/lebensmittel/pfefferminz

Or if your audience is searching in Japanese, use Japanese words in the URL: 
    
    
    https://example.com/ペパーミント  
  
### Use percent encoding as necessary

|  When [linking to pages on your site](/search/docs/crawling-indexing/links-crawlable), use percent encoding in your links's `href` attributes as necessary. Unreserved ASCII characters may be left in the non-encoded form. Additionally, characters in the non-ASCII range should be percent encoded. For example:  | Recommended (percent encoding) | Not recommended (non-ASCII characters)  
---|---  
      
    
    https://example.com/%D9%86%D8%B9%D9%86%D8%A7%D8%B9/%D8%A8%D9%82%D8%A7%D9%84%D8%A9

| 
    
    
    https://example.com/نعناع  
      
    
    https://example.com/%E6%9D%82%E8%B4%A7/%E8%96%84%E8%8D%B7

| 
    
    
    https://example.com/杂货/薄荷  
      
    
    https://example.com/gem%C3%BCse

| 
    
    
    https://example.com/gemüse  
      
    
    https://example.com/%F0%9F%A6%99%E2%9C%A8

| 
    
    
    https://example.com/🦙✨  
  
### Use hyphens to separate words

|  We recommend separating words in your URLs, when possible. Specifically, we recommend using hyphens (`-`) instead of underscores (`_`) to separate words in your URLs, as it helps users and search engines better identify concepts in the URL. For historical reasons, we don't recommend using underscores, as this style is already commonly used for denoting concepts that should be kept together, for example, by various programming languages to name functions (such as `format_date`).  |  Recommended  |  Not recommended   
---|---  
Using hyphens (`-`) to separate words:
    
    
    https://example.com/summer-clothing/filter?color-profile=dark-grey

|  Using underscores (`_`) to separate words:
    
    
    https://example.com/summer_clothing/filter?color_profile=dark_grey

Joining words together in the URL:
    
    
    https://example.com/greendress  
  
### Use as few parameters as you can

| Whenever possible, shorten URLs by trimming unnecessary parameters (meaning, parameters that don't change the content).   
  
### Be aware that URLs are case sensitive

| Like any other HTTP client following IETF STD 66, Google Search's URL handling is case sensitive (for example, Google treats both `/APPLE` and `/apple` as distinct URLs with their own content). If upper and lower case text in a URL is treated the same by your web server, convert all text to the same case so it's easier for Google to determine that URLs reference the same page.   
  
### For multi-regional sites

|  If your site is multi-regional, consider using a URL structure that makes it easy to geotarget your site. For more examples of how you can structure your URLs, refer to [using locale-specific URLs](/search/docs/specialty/international/managing-multi-regional-sites#locale-specific-urls).  Recommended (using a country-specific domain): 
    
    
    https://example.de

Recommended (using a country-specific subdirectory with gTLD): 
    
    
    https://example.com/de/  
  
## Avoid common issues related to URLs

Overly complex URLs, especially those containing multiple parameters, can cause problems for crawlers by creating unnecessarily high numbers of URLs that point to identical or similar content on your site. As a result, Googlebot may consume much more bandwidth than necessary, or Google Search may be unable to completely index all the content on your site. 

Unnecessarily high numbers of URLs can be caused by a number of issues. These include: 

Common issues  
---  
  
### Additive filtering of a set of items

|  Many sites provide different views of the same set of items or search results, often allowing the user to filter this set using defined criteria (for example: show me hotels on the beach). When filters can be combined in an additive manner (for example: hotels on the beach and with a fitness center), the number of URLs (views of data) in the sites explodes. Creating a large number of slightly different lists of hotels is redundant, as Googlebot only needs to see a small number of lists from which it can reach the page for each hotel. For example: 

  * Hotel properties at "value rates": 
    
        https://example.com/hotel-search-results.jsp?Ne=292&N;=461

  * Hotel properties at "value rates" on the beach: 
    
        https://example.com/hotel-search-results.jsp?Ne=292&N;=461+4294967240

  * Hotel properties at "value rates" on the beach and with a fitness center: 
    
        https://example.com/hotel-search-results.jsp?Ne=292&N;=461+4294967240+4294967270

  
  
### Irrelevant parameters

|  Irrelevant parameters in the URL can cause a large number of URLs, such as:

  * Referral parameters: 
    
        https://example.com/search/noheaders?click=6EE2BF1AF6A3D705D5561B7C3564D9C2&clickPage;=OPD+Product+Page&cat;=79
    
        https://example.com/discuss/showthread.php?referrerid=249406&threadid;=535913
    
        https://example.com/products/products.asp?N=200063&Ne;=500955&ref;=foo%2Cbar&Cn;=Accessories

  * Shopping sorting parameters: 
    
        https://example.com/results?search_type=search_videos&search;_query=tpb&search;_sort=relevance&search;_category=25

  * Session IDs: 
    
        https://example.com/search/noheaders?sessionid=6EE2BF1AF6A3D705D5561B7C3564D9C2

Wherever possible, avoid the use of session IDs in URLs and consider using cookies instead.

Consider using a [robots.txt file](/search/docs/crawling-indexing/robots/intro) to block Googlebot's access to these problematic URLs.  
  
### Calendar issues

|  A dynamically generated calendar might generate links to future and previous dates with no restrictions on start or end dates. For example:
    
    
    https://example.com/calendar.php?d=13&m;=8&y;=2011

If your site has an infinite calendar, add a `[nofollow](/search/docs/crawling-indexing/qualify-outbound-links#nofollow)` attribute to links to dynamically created future calendar pages.   
  
### Broken relative links

| Placing a [parent-relative link](https://developer.mozilla.org/en-US/docs/Web/API/URL_API/Resolving_relative_references#parent-directory_relative) on the wrong page may create infinite spaces if your server doesn't respond with the right HTTP status code for nonexistent pages. For example, a parent-relative link such as `<a href="../../category/stuff">...</a>` on `https://example.com/category/community/070413/html/FAQ.htm` may lead to bogus URLs such as `https://example.com/category/community/category/stuff`. To fix, use root-relative URLs in your links (instead of parent-relative).   
  
## Fixing crawling-related URL structure problems

If you notice that Google Search is crawling these problematic URLs, we recommend the following: 

  * Consider using a [robots.txt file](/search/docs/crawling-indexing/robots/intro) to block Googlebot's access to problematic URLs. Typically, consider blocking dynamic URLs, such as URLs that generate search results, or URLs that can create infinite spaces, such as calendars, and ordering and filtering functions. 
  * If your site has faceted navigation, learn how to [manage crawling of those faceted navigation URLs](/search/docs/crawling-indexing/crawling-managing-faceted-navigation#prevent-crawling-of-faceted-navigation-urls).

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
