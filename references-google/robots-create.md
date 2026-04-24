# 如何编写 robots.txt

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

# How to write and submit a robots.txt file

If you use a site hosting service, such as Wix or Blogger, you might not need to (or be able to) edit your robots.txt file directly. Instead, your provider might expose a search settings page or some other mechanism to tell search engines whether or not to crawl your page. 

If you want to hide or unhide one of your pages from search engines, search for instructions about modifying your page visibility in search engines on your hosting service, for example, search for "wix hide page from search engines". 

You can [control which files crawlers may access](/search/docs/crawling-indexing/robots/intro) on your site with a robots.txt file. 

A robots.txt file lives at the root of your site. So, for site `www.example.com`, the robots.txt file lives at `www.example.com/robots.txt`. robots.txt is a plain text file that follows the [Robots Exclusion Standard](https://en.wikipedia.org/wiki/Robots_exclusion_standard#About_the_standard). A robots.txt file consists of one or more rules. Each rule blocks or allows access for all or a specific crawler to a specified file path on the domain or subdomain where the robots.txt file is hosted. Unless you specify otherwise in your robots.txt file, all files are implicitly allowed for crawling. 

Here is a simple robots.txt file with two rules:
    
    
    User-agent: Googlebot
    Disallow: /nogooglebot/
    
    User-agent: *
    Allow: /
    
    Sitemap: https://www.example.com/sitemap.xml

Here's what that robots.txt file means:

  1. The user agent named Googlebot is not allowed to crawl any URL that starts with `https://example.com/nogooglebot/`. 
  2. All other user agents are allowed to crawl the entire site. This could have been omitted and the result would be the same; the default behavior is that user agents are allowed to crawl the entire site. 
  3. The site's [sitemap file](/search/docs/crawling-indexing/sitemaps/overview) is located at `https://www.example.com/sitemap.xml`. 

See the syntax section for more examples.

## Basic guidelines for creating a robots.txt file

Creating a robots.txt file and making it generally accessible and useful involves four steps: 

  1. Create a file named robots.txt.
  2. Add rules to the robots.txt file.
  3. Upload the robots.txt file to the root of your site.
  4. Test the robots.txt file.

## Create a robots.txt file

You can use almost any text editor to create a robots.txt file. For example, Notepad, TextEdit, vi, and emacs can create valid robots.txt files. Don't use a word processor; word processors often save files in a proprietary format and can add unexpected characters, such as curly quotes, which can cause problems for crawlers. Make sure to save the file with UTF-8 encoding if prompted during the save file dialog. 

Format and location rules:

  * The file must be named robots.txt.
  * Your site can have only one robots.txt file.
  * The robots.txt file must be located at the root of the site host to which it applies. For instance, to control crawling on all URLs below `https://www.example.com/`, the robots.txt file must be located at `https://www.example.com/robots.txt`. It cannot be placed in a subdirectory (for example, at `https://example.com/pages/robots.txt`). If you're unsure about how to access your site root, or need permissions to do so, contact your web hosting service provider. If you can't access your site root, use an alternative blocking method such as [`meta` tags](/search/docs/crawling-indexing/block-indexing). 
  * A robots.txt file can be posted on a subdomain (for example, `https://site.example.com/robots.txt`) or on non-standard ports (for example, `https://example.com:8181/robots.txt`). 
  * A robots.txt file applies only to paths within the protocol, host, and port where it is posted. That is, rules in `https://example.com/robots.txt` apply only to files in `https://example.com/`, not to subdomains such as `https://m.example.com/`, or alternate protocols, such as `http://example.com/`. 
  * A robots.txt file must be a UTF-8 encoded text file (which includes ASCII). Google may ignore characters that are not part of the UTF-8 range, potentially rendering robots.txt rules invalid. 

## How to write robots.txt rules

Rules are instructions for crawlers about which parts of your site they can crawl. Follow these guidelines when adding rules to your robots.txt file: 

  * A robots.txt file consists of one or more groups (set of rules).
  * Each group consists of multiple rules (also known as directives), one rule per line. Each group begins with a `User-agent` line that specifies the target of the groups. 
  * A group gives the following information: 
    * Who the group applies to (the user agent).
    * Which directories or files that agent can access.
    * Which directories or files that agent cannot access.
  * Crawlers process groups from top to bottom. A user agent can match only one rule set, which is the first, most specific group that matches a given user agent. If there are multiple groups for the same user agent, the groups will be combined into a single group before processing. 
  * The default assumption is that a user agent can crawl any page or directory not blocked by a `disallow` rule. 
  * Rules are case-sensitive. For instance, `disallow: /file.asp` applies to `https://www.example.com/file.asp`, but not `https://www.example.com/FILE.asp`. 
  * The `#` character marks the beginning of a comment. Comments are ignored during processing. 

Google's crawlers support the following rules in robots.txt files:

  * `user-agent:` [Required, one or more per group] The rule specifies the name of the automatic client known as search engine crawler that the rule applies to. This is the first line for any rule group. Google user agent names are listed in the [Google list of user agents](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers). Using an asterisk (`*`) matches all crawlers except the various AdsBot crawlers, which must be named explicitly. For example: 
    
        # Example 1: Block only Googlebot
    User-agent: Googlebot
    Disallow: /
    
    # Example 2: Block Googlebot and Adsbot
    User-agent: Googlebot
    User-agent: AdsBot-Google
    Disallow: /
    
    # Example 3: Block all crawlers except AdsBot (AdsBot crawlers must be named explicitly)
    User-agent: *
    Disallow: /

  * `disallow:` [At least one or more `disallow` or `allow` entries per rule] A directory or page, relative to the root domain, that you don't want the user agent to crawl. If the rule refers to a page, it must be the full page name as shown in the browser. It must start with a `/` character and if it refers to a directory, it must end with the `/` mark. 
  * `allow:` [At least one or more `disallow` or `allow` entries per rule] A directory or page, relative to the root domain, that may be crawled by the user agent just mentioned. This is used to override a `disallow` rule to allow crawling of a subdirectory or page in a disallowed directory. For a single page, specify the full page name as shown in the browser. It must start with a `/` character and if it refers to a directory, it must end with the `/` mark. 
  * `sitemap:` [Optional, zero or more per file] The location of a sitemap for this site. The sitemap URL must be a fully-qualified URL; Google doesn't assume or check http/https/www.non-www alternates. Sitemaps are a good way to indicate which content Google should crawl, as opposed to which content it can or cannot crawl. [Learn more about sitemaps.](/search/docs/crawling-indexing/sitemaps/overview) Example:
    
        Sitemap: https://example.com/sitemap.xml
    Sitemap: https://www.example.com/sitemap.xml

All rules, except `sitemap`, support the `*` wildcard for a path prefix, suffix, or entire string. 

Lines that don't match any of these rules are ignored.

Read our page about [Google's interpretation of the robots.txt specification](/crawling/docs/robots-txt/robots-txt-spec) for the complete description of each rule. 

## Upload the robots.txt file

Once you saved your robots.txt file to your computer, you're ready to make it available to search engine crawlers. There's no one tool that can help you with this, because how you upload the robots.txt file to your site depends on your site and server architecture. Get in touch with your hosting company or search the documentation of your hosting company; for example, search for "upload files infomaniak". 

After you upload the robots.txt file, test whether it's publicly accessible and if Google can parse it. 

##  Test robots.txt markup 

To test whether your newly uploaded robots.txt file is publicly accessible, open a [private browsing window](https://support.google.com/chrome/answer/95464) (or equivalent) in your browser and navigate to the location of the robots.txt file. For example, `https://example.com/robots.txt`. If you see the contents of your robots.txt file, you're ready to test the markup. 

Google offers two options for fixing issues with robots.txt markup:

  1. The [ robots.txt report](https://support.google.com/webmasters/answer/6062598) in Search Console. You can only use this report for robots.txt files that are already accessible on your site. 
  2. If you're a developer, check out and build [Google's open source robots.txt library](https://github.com/google/robotstxt), which is also used in Google Search. You can use this tool to test robots.txt files locally on your computer. 

## Submit robots.txt file to Google

Once you uploaded and tested your robots.txt file, Google's crawlers will automatically find and start using your robots.txt file. You don't have to do anything. If you updated your robots.txt file and you need to refresh Google's cached copy as soon as possible, learn [how to submit an updated robots.txt file](/crawling/docs/robots-txt/submit-updated-robots-txt). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-21 UTC."],[],[]] 

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
