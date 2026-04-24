# Google 爬虫总览

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

# Overview of Google crawlers and fetchers (user agents)

Google uses crawlers and fetchers to perform actions for its products, either automatically or triggered by user request. Crawler (sometimes also called a "robot" or "spider") is a generic term for any program that is used to [automatically discover and scan websites](/search/docs/fundamentals/how-search-works#crawling). Fetchers act as a program like [wget](https://www.gnu.org/software/wget/) that typically make a single request on behalf of a user. Google's clients fall into three categories: 

Looking for the latest updates to this page? See our [updates to our documentation](/crawling/docs/changelog).  [Common crawlers](/crawling/docs/crawlers-fetchers/google-common-crawlers) |  The common crawlers used for Google's products (such as [Googlebot](/search/docs/crawling-indexing/googlebot)). They always respect robots.txt rules for automatic crawls.   
---|---  
[Special-case crawlers](/crawling/docs/crawlers-fetchers/google-special-case-crawlers) |  Special-case crawlers are similar to common crawlers, however are used by specific products where there's an agreement between the crawled site and the Google product about the crawl process. For example, `AdsBot` ignores the global robots.txt user agent (`*`) with the ad publisher's permission.   
[User-triggered fetchers](/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) |  User-triggered fetchers are part of tools and product functions where the end user triggers a fetch. For example, [Google Site Verifier](https://support.google.com/webmasters/answer/9008080) acts on the request of a user.   
  
## Technical properties of Google's crawlers and fetchers

Google's crawlers and fetchers are designed to be run simultaneously by thousands of machines to improve performance and scale as the web grows. To optimize bandwidth usage, these clients are distributed across many datacenters across the world so they're located near the sites that they might access. Therefore, your logs may show visits from several IP addresses. Google egresses primarily from IP addresses in the United States. In case Google detects that a site is blocking requests from the United States, it may attempt to crawl from IP addresses located in other countries. 

### Supported transfer protocols

Google's crawlers and fetchers support HTTP/1.1 and [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2). The crawlers will use the protocol version that provides the best crawling performance and may switch protocols between crawling sessions depending on previous crawling statistics. The default protocol version used by Google's crawlers is HTTP/1.1; crawling over HTTP/2 may save computing resources (for example, CPU, RAM) for your site and Googlebot, but otherwise there's no Google-product specific benefit to the site (for example, no ranking boost in Google Search). To opt out from crawling over HTTP/2, instruct the server that's hosting your site to respond with a `421` HTTP status code when Google attempts to access your site over HTTP/2. If that's not feasible, you [can send a message to the Crawling team](https://www.google.com/webmasters/tools/googlebot-report) (however this solution is temporary). 

Google's crawler infrastructure also supports crawling through FTP (as defined by [RFC959](https://datatracker.ietf.org/doc/html/rfc959) and its updates) and FTPS (as defined by [RFC4217](https://datatracker.ietf.org/doc/html/rfc4217) and its updates), however crawling through these protocols is rare. 

### Supported content encodings

Google's crawlers and fetchers support the following content encodings (compressions): [gzip](https://en.wikipedia.org/wiki/Gzip), [deflate](https://en.wikipedia.org/wiki/Deflate), and [Brotli (br)](https://en.wikipedia.org/wiki/Brotli). The content encodings supported by each Google user agent is advertised in the `Accept-Encoding` header of each request they make. For example, `Accept-Encoding: gzip, deflate, br`. 

### File size limits

By default, Google's crawlers and fetchers only crawl the first 15MB of a file, and any content beyond this limit is ignored. However, individual projects may set different limits for their crawlers and fetchers, and also for different file types. For example, a Google crawler [like Googlebot](/search/docs/crawling-indexing/googlebot) may have a smaller size limit (for example, 2MB), or specify a larger file size limit for a PDF than for HTML. 

### Crawl rate and host load

Our goal is to crawl as many pages from your site as we can on each visit without overwhelming your server. If your site is having trouble keeping up with Google's crawling requests, you can [reduce the crawl rate](/crawling/docs/crawlers-fetchers/reduce-crawl-rate). Note that sending the inappropriate [HTTP response code](/search/docs/crawling-indexing/http-network-errors) to Google's crawlers may affect how your site appears in Google products. 

### HTTP Caching

Google's crawling infrastructure supports heuristic HTTP caching as defined by the [HTTP caching standard](https://httpwg.org/specs/rfc9111.html), specifically through the `ETag` response- and `If-None-Match` request header, and the `Last-Modified` response- and `If-Modified-Since` request header. 

Note: Consider setting both the `Etag` and `Last-Modified` values regardless of the preference of Google's crawlers. These headers are also used by other applications such as CMSes. 

If both `ETag` and `Last-Modified` response header fields are present in the HTTP response, Google's crawlers use the `ETag` value as [required by the HTTP standard](https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.3). For Google's crawlers specifically, we recommend using [`ETag`](https://www.rfc-editor.org/rfc/rfc9110#name-etag) instead of the `Last-Modified` header to indicate caching preference as `ETag` doesn't have date formatting issues. 

Other HTTP caching directives aren't supported. 

Individual Google crawlers and fetchers may or may not make use of caching, depending on the needs of the product they're associated with. For example, `Googlebot` supports caching when re-crawling URLs for Google Search, and `Storebot-Google` only supports caching in certain conditions. 

To implement HTTP caching for your site, get in touch with your hosting or content management system provider. 

#### `ETag` and `If-None-Match`

Google's crawling infrastructure supports `ETag` and `If-None-Match` as defined by the [HTTP Caching standard](https://httpwg.org/specs/rfc9111.html). Learn more about the [`ETag`](https://www.rfc-editor.org/rfc/rfc9110#name-etag) response header and its request header counterpart, [`If-None-Match`](https://www.rfc-editor.org/rfc/rfc9110#name-if-none-match). 

#### Last-Modified and If-Modified-Since

Google's crawling infrastructure supports `Last-Modified` and `If-Modified-Since` as defined by the [HTTP Caching standard](https://httpwg.org/specs/rfc9111.html) with the following caveats: 

  * The date in the `Last-Modified` header must be formatted according to the [HTTP standard](https://www.rfc-editor.org/rfc/rfc9110.html). To avoid parsing issues, we recommend using the following date format: "Weekday, DD Mon YYYY HH:MM:SS Timezone". For example, "Fri, 4 Sep 1998 19:15:56 GMT". 
  * While not required, consider also setting the [`max-age` field of the `Cache-Control` response header](https://www.rfc-editor.org/rfc/rfc9111.html#name-max-age-2) to help crawlers determine when to recrawl the specific URL. Set the value of the `max-age` field to the expected number of seconds the content will be unchanged. For example, `Cache-Control: max-age=94043`. 

Learn more about the [`Last-Modified`](https://www.rfc-editor.org/rfc/rfc9110#name-last-modified) response header and its request header counterpart, [`If-Modified-Since`](https://www.rfc-editor.org/rfc/rfc9110#name-if-modified-since). 

## Verify Google's crawlers and fetchers

Google's crawlers identify themselves in three ways: 

  1. The HTTP `user-agent` request header. 
  2. The source IP address of the request. 
  3. The reverse DNS hostname of the source IP. 

Learn how to use these details to [verify Google's crawlers and fetchers](/crawling/docs/crawlers-fetchers/verify-google-requests). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 

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
