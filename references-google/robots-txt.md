# robots.txt 完整指南

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

# How Google interprets the robots.txt specification

Google's automated [crawlers](/crawling/docs/crawlers-fetchers/overview-google-crawlers) support the [Robots Exclusion Protocol (REP)](https://www.rfc-editor.org/rfc/rfc9309.html). This means that before crawling a site, Google's crawlers download and parse the site's robots.txt file to extract information about which parts of the site may be crawled. The REP isn't applicable to Google's crawlers that are controlled by users (for example, feed subscriptions), or crawlers that are used to increase user safety (for example, malware analysis). 

This page describes Google's interpretation of the REP. For the original standard, check [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html). 

## What is a robots.txt file

If you don't want crawlers to access sections of your site, you can create a robots.txt file with appropriate rules. A robots.txt file is a text file containing rules about which crawlers may access which parts of a site. For example, the robots.txt file for example.com may look like this: 
    
    
    # This robots.txt file controls crawling of URLs under https://example.com.
    # All crawlers are disallowed to crawl files in the "includes" directory, such
    # as .css, .js, but Google needs them for rendering, so Googlebot is allowed
    # to crawl them.
    User-agent: *
    Disallow: /includes/
    
    User-agent: Googlebot
    Allow: /includes/
    
    Sitemap: https://example.com/sitemap.xml

If you're new to robots.txt, start with our [intro to robots.txt](/search/docs/crawling-indexing/robots/intro). You can also find [tips for creating a robots.txt file](/crawling/docs/robots-txt/create-robots-txt). 

## File location and range of validity

You must place the robots.txt file in the top-level directory of a site, on a supported protocol. The URL for the robots.txt file is (like other URLs) case-sensitive. In case of Google Search, the supported protocols are HTTP, HTTPS, and FTP. On HTTP and HTTPS, crawlers fetch the robots.txt file with an HTTP non-conditional `GET` request; on FTP, crawlers use a standard `RETR (RETRIEVE)` command, using anonymous login. 

The rules listed in the robots.txt file apply only to the host, protocol, and port number where the robots.txt file is hosted. 

## Examples of valid robots.txt URLs

The following table contains examples of robots.txt URLs and what URL paths they're valid for. Column one contains the URL of a robots.txt file, and column two contains domains that that robots.txt file would and wouldn't apply to.

Robots.txt URL examples  
---  
`https://example.com/robots.txt` |  This is the general case. It's not valid for other subdomains, protocols, or port numbers. It's valid for all files in all subdirectories on the same host, protocol, and port number.  Valid for:

  * `https://example.com/`
  * `https://example.com/folder/file`

Not valid for:

  * `https://other.example.com/`
  * `http://example.com/`
  * `https://example.com:8181/`

  
`https://www.example.com/robots.txt` |  A robots.txt on a subdomain is only valid for that subdomain.  Valid for: `https://www.example.com/` Not valid for:

  * `https://example.com/`
  * `https://shop.www.example.com/`
  * `https://www.shop.example.com/`

  
`https://example.com/folder/robots.txt` |  Not a valid robots.txt file. Crawlers don't check for robots.txt files in subdirectories.   
`https://www.exämple.com/robots.txt` |  IDNs are equivalent to their punycode versions. See also [RFC 3492](https://www.ietf.org/rfc/rfc3492.txt).  Valid for:

  * `https://www.exämple.com/`
  * `https://xn--exmple-cua.com/`

Not valid for: `https://www.example.com/`  
`ftp://example.com/robots.txt` |  Valid for: `ftp://example.com/` Not valid for: `https://example.com/`  
`https://212.96.82.21/robots.txt` |  A robots.txt with an IP-address as the hostname is only valid for crawling of that IP address as the hostname. It isn't automatically valid for all websites hosted on that IP address (though it's possible that the robots.txt file is shared, in which case it would also be available under the shared hostname).  Valid for: `https://212.96.82.21/` Not valid for: `https://example.com/` (even if hosted on `212.96.82.21`)   
`https://example.com:443/robots.txt` |  Standard port numbers (`80` for HTTP, `443` for HTTPS, `21` for FTP) are equivalent to their default hostnames.  Valid for:

  * `https://example.com:443/`
  * `https://example.com/`

Not valid for: `https://example.com:444/`  
`https://example.com:8181/robots.txt` |  Robots.txt files on non-standard port numbers are only valid for content made available through those port numbers.  Valid for: `https://example.com:8181/` Not valid for: `https://example.com/`  
  
## Handling of errors and HTTP status codes

When requesting a robots.txt file, the HTTP status code of the server's response affects how the robots.txt file will be used by Google's crawlers. The following table summarizes how Googlebot treats robots.txt files for different HTTP status codes. 

Handling of errors and HTTP status codes  
---  
`2xx (success)` |  HTTP status codes that signal success prompt Google's crawlers to process the robots.txt file as provided by the server.   
`3xx (redirection)` |  Google follows at least five redirect hops as defined by [RFC 1945](https://www.ietf.org/rfc/rfc1945.txt) and then stops and treats it as a `404` for the robots.txt file. This also applies to any disallowed URLs in the redirect chain, since the crawler couldn't fetch rules due to the redirects.  Google doesn't follow logical redirects in robots.txt files (frames, JavaScript, or meta refresh-type redirects).   
`4xx (client errors)` |  Google's crawlers treat all `4xx` errors, except `429`, as if a valid robots.txt file didn't exist. This means that Google assumes that there are no crawl restrictions.  Don't use `401` and `403` status codes for limiting the crawl rate. The `4xx` status codes, except `429`, have no effect on crawl rate. [Learn how to limit your crawl rate](/crawling/docs/crawlers-fetchers/reduce-crawl-rate).   
`5xx (server errors)` |  If Google finds a robots.txt file but can't fetch it, Google follows this behavior: 

  1. For the first 12 hours, Google stops crawling the site but keeps trying to fetch the robots.txt file. 
  2. If Google can't fetch a new version, for the next 30 days Google will use the last good version, while still trying to fetch a new version. A `503 (service unavailable)` error results in fairly frequent retrying. If there's no cached version available, Google assumes there's no crawl restrictions. 
  3. If the errors are still not fixed after 30 days: 
     * If the site is generally available to Google, Google will behave as if there is no robots.txt file (but still keep checking for a new version). 
     * If the site has general availability problems, Google will stop crawling the site, while still periodically requesting a robots.txt file. 

  
Other errors |  A robots.txt file which cannot be fetched due to DNS or networking issues, such as timeouts, invalid responses, reset or interrupted connections, and HTTP chunking errors, is treated as a server error.   
  
## Caching

Google generally caches the contents of robots.txt file for up to 24 hours, but may cache it longer in situations where refreshing the cached version isn't possible (for example, due to timeouts or `5xx` errors). The cached response may be shared by different crawlers. Google may increase or decrease the cache lifetime based on [max-age Cache-Control](https://www.rfc-editor.org/rfc/rfc9110.html) HTTP headers. 

## File format

The robots.txt file must be a [UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoded plain text file and the lines must be separated by `CR`, `CR/LF`, or `LF`. 

Google ignores invalid lines in robots.txt files, including the Unicode [Byte Order Mark](https://en.wikipedia.org/wiki/Byte_order_mark) (BOM) at the beginning of the robots.txt file, and use only valid lines. For example, if the content downloaded is HTML instead of robots.txt rules, Google will try to parse the content and extract rules, and ignore everything else. 

Similarly, if the character encoding of the robots.txt file isn't UTF-8, Google may ignore characters that are not part of the UTF-8 range, potentially rendering robots.txt rules invalid. 

Google enforces a robots.txt file size limit of 500 [kibibytes](https://en.wikipedia.org/wiki/Kibibyte) (KiB). Content which is after the maximum file size is ignored. You can reduce the size of the robots.txt file by consolidating rules that would result in an oversized robots.txt file. For example, place excluded material in a separate directory. 

## Syntax

A valid robots.txt line consists of a field, a colon, and a value. Field names are case-insensitive (for example, `User-agent` and `user-agent` are treated the same). Spaces are optional, but recommended to improve readability. Space at the beginning and at the end of the line is ignored. To include comments, precede your comment with the `#` character. Keep in mind that everything after the `#` character will be ignored. The general format is `<field>:<value><#optional-comment>`. 

Google supports the following fields (other fields such as `crawl-delay` aren't supported): 

  * `user-agent`: identifies which crawler the rules apply to.
  * `allow`: a URL path that may be crawled.
  * `disallow`: a URL path that may not be crawled.
  * `sitemap`: the complete URL of a sitemap.

The `allow` and `disallow` fields are also called rules (also known as directives). These rules are always specified in the form of `rule: [path]` where `[path]` is optional. By default, there are no restrictions for crawling for the designated crawlers. Crawlers ignore rules without a `[path]`. 

The `[path]` value, if specified, is relative to the root of the website from where the robots.txt file was fetched (using the same protocol, port number, host and domain names). The path value must start with `/` to designate the root and the value is case-sensitive. Learn more about URL matching based on path values. 

### `user-agent`

The `user-agent` line identifies which crawler rules apply to. See [Google's crawlers and user-agent strings](/crawling/docs/crawlers-fetchers/overview-google-crawlers) for a comprehensive list of user-agent strings you can use in your robots.txt file. 

Both the `user-agent` field name and its value are case-insensitive. 

### `disallow`

The `disallow` rule specifies paths that must not be accessed by the crawlers identified by the `user-agent` line the `disallow` rule is grouped with. Crawlers ignore the rule without a path. 

Google can't index the content of pages which are disallowed for crawling, but it may still index the URL and show it in search results without a snippet. Learn how to [block indexing](/search/docs/crawling-indexing/block-indexing). 

The field name (`disallow`) is case-insensitive, but its value is case-sensitive. 

Usage:
    
    
    disallow: [path]
    

### `allow`

The `allow` rule specifies paths that may be accessed by the designated crawlers. When no path is specified, the rule is ignored. 

The field name (`allow`) is case-insensitive, but its value is case-sensitive. 

Usage:
    
    
    allow: [path]
    

### `sitemap`

Google, Bing, and other major search engines support the `sitemap` field in robots.txt, as defined by [sitemaps.org](https://sitemaps.org). 

The field name (`sitemap`) is case-insensitive, but its value is case-sensitive. 

Usage:
    
    
    sitemap: [absoluteURL]

The `[absoluteURL]` line points to the location of a sitemap or sitemap index file. It must be a fully qualified URL, including the protocol and host, and doesn't have to be URL-encoded. The URL doesn't have to be on the same host as the robots.txt file. You can specify multiple `sitemap` fields. The sitemap field isn't tied to any specific user agent and may be followed by all crawlers, provided it isn't disallowed for crawling. 

For example:
    
    
    user-agent: otherbot
    disallow: /kale
    
    sitemap: https://example.com/sitemap.xml
    sitemap: https://cdn.example.org/other-sitemap.xml
    sitemap: https://ja.example.org/テスト-サイトマップ.xml

## Grouping of lines and rules

You can group together rules that apply to multiple user agents by repeating `user-agent` lines for each crawler. 

For example:
    
    
    user-agent: a
    disallow: /c
    
    user-agent: b
    disallow: /d
    
    user-agent: e
    user-agent: f
    disallow: /g
    
    user-agent: h
    

In this example there are four distinct rule groups:

  * One group for user agent "a".
  * One group for user agent "b".
  * One group for both "e" and "f" user agents.
  * One group for user agent "h".

For the technical description of a group, see [section 2.1 of the REP](https://www.rfc-editor.org/rfc/rfc9309.html#section-2.1-2.4). 

## Order of precedence for user agents

Only one group is valid for a particular crawler. Google's crawlers determine the correct group of rules by finding in the robots.txt file the group with the most specific user agent that matches the crawler's user agent. Other groups are ignored. All non-matching text is ignored (for example, both `googlebot/1.2` and `googlebot*` are equivalent to `googlebot`). The order of the groups within the robots.txt file is irrelevant. 

If there's more than one specific group declared for a user agent, all the rules from the groups applicable to the specific user agent are combined internally into a single group. User agent specific groups and global groups (`*`) are not combined. 

### Examples

#### Matching of `user-agent` fields
    
    
    user-agent: googlebot-news
    (group 1)
    
    user-agent: *
    (group 2)
    
    user-agent: googlebot
    (group 3)
    

This is how the crawlers would choose the relevant group:

Group followed per crawler  
---  
Googlebot News |  `googlebot-news` follows group 1, because group 1 is the most specific group.   
Googlebot (web) | `googlebot` follows group 3.  
Googlebot Storebot |  `Storebot-Google` follows group 2, because there is no specific `Storebot-Google` group.   
Googlebot News (when crawling images) |  When crawling images, `googlebot-news` follows group 1. `googlebot-news` doesn't crawl the images for Google Images, so it only follows group 1.   
Otherbot (web) | Other Google crawlers follow group 2.  
Otherbot (news) |  Other Google crawlers that crawl news content, but don't identify as `googlebot-news` follow group 2. Even if there is an entry for a related crawler, it is only valid if it's specifically matching.   
  
#### Grouping of rules

If there are multiple groups in a robots.txt file that are relevant to a specific user agent, Google's crawlers internally merge the groups. For example: 
    
    
    user-agent: googlebot-news
    disallow: /fish
    
    user-agent: *
    disallow: /carrots
    
    user-agent: googlebot-news
    disallow: /shrimp
    

The crawlers internally group the rules based on user agent, for example:
    
    
    user-agent: googlebot-news
    disallow: /fish
    disallow: /shrimp
    
    user-agent: *
    disallow: /carrots
    

Rules other than `allow`, `disallow`, and `user-agent` are ignored by the robots.txt parser. This means that the following robots.txt snippet is treated as one group, and thus both `user-agent` `a` and `b` are affected by the `disallow: /` rule: 
    
    
    user-agent: a
    sitemap: https://example.com/sitemap.xml
    
    user-agent: b
    disallow: /

When the crawlers process the robots.txt rules, they ignore the `sitemap` line. For example, this is how the crawlers would understand the previous robots.txt snippet: 
    
    
    user-agent: a
    user-agent: b
    disallow: /

## URL matching based on path values

Google uses the path value in the `allow` and `disallow` rules as a basis to determine whether or not a rule applies to a specific URL on a site. This works by comparing the rule to the path component of the URL that the crawler is trying to fetch. Non-7-bit ASCII characters in a path may be included as UTF-8 characters or as percent-escaped UTF-8 encoded characters per [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt). 

Google, Bing, and other major search engines support a limited form of wildcards for path values. These wildcard characters are: 

  * `*` designates 0 or more instances of any valid character.
  * `$` designates the end of the URL.

The following table shows how the different wildcard characters affect parsing: 

Example path matches  
---  
`/` | Matches the root and any lower level URL.  
`/*` | Equivalent to `/`. The trailing wildcard is ignored.  
`/$` | Matches only the root. Any lower level URL is allowed for crawling.  
`/fish` |  Matches any path that starts with `/fish`. Note that the matching is case-sensitive.  Matches:

  * `/fish`
  * `/fish.html`
  * `/fish/salmon.html`
  * `/fishheads`
  * `/fishheads/yummy.html`
  * `/fish.php?id=anything`

Doesn't match:

  * `/Fish.asp`
  * `/catfish`
  * `/?id=fish`
  * `/desert/fish`

  
`/fish*` |  Equivalent to `/fish`. The trailing wildcard is ignored.  Matches:

  * `/fish`
  * `/fish.html`
  * `/fish/salmon.html`
  * `/fishheads`
  * `/fishheads/yummy.html`
  * `/fish.php?id=anything`

Doesn't match:

  * `/Fish.asp`
  * `/catfish`
  * `/?id=fish`
  * `/desert/fish`

  
`/fish/` |  Matches anything in the `/fish/` folder.  Matches:

  * `/fish/`
  * `/fish/?id=anything`
  * `/fish/salmon.htm`

Doesn't match:

  * `/fish`
  * `/fish.html`
  * `/animals/fish/`
  * `/Fish/Salmon.asp`

  
`/*.php` |  Matches any path that contains `.php`.  Matches:

  * `/index.php`
  * `/filename.php`
  * `/folder/filename.php`
  * `/folder/filename.php?parameters`
  * `/folder/any.php.file.html`
  * `/filename.php/`

Doesn't match:

  * `/` (even if it maps to /index.php)
  * `/windows.PHP`

  
`/*.php$` |  Matches any path that ends with `.php`.  Matches:

  * `/filename.php`
  * `/folder/filename.php`

Doesn't match:

  * `/filename.php?parameters`
  * `/filename.php/`
  * `/filename.php5`
  * `/windows.PHP`

  
`/fish*.php` |  Matches any path that contains `/fish` and `.php`, in that order.  Matches:

  * `/fish.php`
  * `/fishheads/catfish.php?parameters`

Doesn't match: `/Fish.PHP`  
  
## Order of precedence for rules

When matching robots.txt rules to URLs, crawlers use the most specific rule based on the length of the rule path. In case of conflicting rules, including those with wildcards, Google uses the least restrictive rule. 

The following examples demonstrate which rule Google's crawlers will apply on a given URL. 

Sample situations  
---  
`https://example.com/page` | 
    
    
    allow: /p
    disallow: /

Applicable rule: `allow: /p`, because it's more specific.   
`https://example.com/folder/page` | 
    
    
    allow: /folder
    disallow: /folder

Applicable rule: `allow: /folder`, because in case of conflicting rules, Google uses the least restrictive rule.   
`https://example.com/page.htm` | 
    
    
    allow: /page
    disallow: /*.htm

Applicable rule: `disallow: /*.htm`, because the rule path is longer and it matches more characters in the URL, so it's more specific.   
`https://example.com/page.php5` | 
    
    
    allow: /page
    disallow: /*.ph

Applicable rule: `allow: /page`, because in case of conflicting rules, Google uses the least restrictive rule.   
`https://example.com/` | 
    
    
    allow: /$
    disallow: /

Applicable rule: `allow: /$`, because it's more specific.   
`https://example.com/page.htm` | 
    
    
    allow: /$
    disallow: /

Applicable rule: `disallow: /`, because the `allow` rule only applies on the root URL.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 

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
