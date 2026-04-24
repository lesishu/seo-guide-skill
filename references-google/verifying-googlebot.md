# 验证 Googlebot 身份

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

# Verify requests from Google crawlers and fetchers

You can verify if a request to your server really is [from Google](/crawling/docs/crawlers-fetchers/overview-google-crawlers). Verification is possible for crawlers such as Googlebot, as well as other requests. This is useful if you're concerned that spammers or other troublemakers are accessing your site while claiming to be from Google. 

Google's crawlers and fetchers fall into three categories:

Type | Description | Reverse DNS mask | IP ranges  
---|---|---|---  
[Common crawlers](/crawling/docs/crawlers-fetchers/google-common-crawlers) |  The common crawlers used for Google's products (such as Googlebot). They always respect robots.txt rules for automatic crawls.  |  `crawl-***-***-***-***.googlebot.com` or `geo-crawl-***-***-***-***.geo.googlebot.com` | [common-crawlers.json](/static/crawling/ipranges/common-crawlers.json)  
[Special-case crawlers](/crawling/docs/crawlers-fetchers/google-special-case-crawlers) |  Crawlers or fetchers that perform specific functions for Google products (such as AdsBot) where there's an agreement between the crawled site and the product about the access or for abuse-specific crawling or fetching. These crawlers or fetchers may or may not respect robots.txt rules.  | `rate-limited-proxy-***-***-***-***.google.com` | [special-crawlers.json](/static/crawling/ipranges/special-crawlers.json)  
[User-triggered fetchers](/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) |  Tools and product functions where the end user triggers a fetch. For example, [Google Site Verifier](https://support.google.com/webmasters/answer/9008080) acts on the request of a user. Because the fetch was requested by a user, these fetchers ignore robots.txt rules.  
Fetchers controlled by Google originate from IPs in the `user-triggered-fetchers-google.json` object and resolve to a `google.com` hostname. IPs in the `user-triggered-fetchers.json` object resolve to `gae.googleusercontent.com` hostnames. These IPs are used, for example, if a site running on Google Cloud (GCP) has a feature that requires fetching external RSS feeds on the request of the user of that site.  |  `***-***-***-***.gae.googleusercontent.com` or `google-proxy-***-***-***-***.google.com` |  [user-triggered-fetchers.json](/static/crawling/ipranges/user-triggered-fetchers.json), [user-triggered-fetchers-google.json](/static/crawling/ipranges/user-triggered-fetchers-google.json), and [user-triggered-agents.json](/static/crawling/ipranges/user-triggered-agents.json)  
  
There are two methods for verifying requests from Google:

  * Manually: For one-off lookups, use command line tools. This method is sufficient for most use cases. 
  * Automatically: For large scale lookups, use an automatic solution to match a crawler's IP address against the list of published Google IP addresses. 

## Use command line tools

  1. Run a reverse DNS lookup on the accessing IP address from your logs, using the `host` command. 
  2. Verify that the domain name is either `googlebot.com`, `google.com`, or `googleusercontent.com`. 
  3. Run a forward DNS lookup on the domain name retrieved in step 1 using the `host` command on the retrieved domain name. 
  4. Verify that it's the same as the original accessing IP address from your logs.

Example 1:
    
    
    host 66.249.66.1
    1.66.249.66.in-addr.arpa domain name pointer crawl-66-249-66-1.googlebot.com.
    
    host crawl-66-249-66-1.googlebot.com
    crawl-66-249-66-1.googlebot.com has address 66.249.66.1

Example 2:
    
    
    host 35.247.243.240
    240.243.247.35.in-addr.arpa domain name pointer geo-crawl-35-247-243-240.geo.googlebot.com.
    
    host geo-crawl-35-247-243-240.geo.googlebot.com
    geo-crawl-35-247-243-240.geo.googlebot.com has address 35.247.243.240

Example 3:
    
    
    host 66.249.90.77
    77.90.249.66.in-addr.arpa domain name pointer rate-limited-proxy-66-249-90-77.google.com.
    
    host rate-limited-proxy-66-249-90-77.google.com
    rate-limited-proxy-66-249-90-77.google.com has address 66.249.90.77

## Use automatic solutions

Alternatively, you can identify Googlebot by IP address by matching the crawler's IP address to the lists of Google crawlers' and fetchers' IP ranges: 

  **Common crawlers like Googlebot**
  **Special crawlers like AdsBot**
  **User-triggered fetchers (users)**
  **User-triggered fetchers (Google)**
  **User-triggered agents**

For other Google IP addresses from where your site may be accessed (for example, [Apps Scripts](/apps-script)), match the accessing IP address against the general [list of Google IP addresses](https://www.gstatic.com/ipranges/goog.json). Note that the IP addresses in the JSON files are represented in [CIDR format](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-20 UTC."],[],[]] 

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
