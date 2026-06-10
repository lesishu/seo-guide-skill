# 如何构建和提交 Sitemap

> 来源：Google Search Central (https://developers.google.com/search/docs/crawling-indexing-sitemaps-build-sitemap.txt)

---

# Build and submit a sitemap

This page describes how to build a sitemap and make it available to Google. If you're new to sitemaps, [read our introduction first](/search/docs/crawling-indexing/sitemaps/overview). 

Google supports the sitemap formats defined by the [sitemaps protocol](https://www.sitemaps.org/protocol.html#otherformats). Each format has its own benefits and shortcomings; choose the one that is the most appropriate for your site and setup (Google doesn't have a preference). The following table compares the different sitemap formats: 

Sitemaps comparison  
---  
XML sitemap |  XML sitemaps are the most versatile of the sitemaps formats. It's extensible and can be used to supply additional data about [images](/search/docs/crawling-indexing/sitemaps/image-sitemaps), [video](/search/docs/crawling-indexing/sitemaps/video-sitemaps), and [news](/search/docs/crawling-indexing/sitemaps/news-sitemap) content, as well as the [localized versions](/search/docs/specialty/international/localized-versions) of your pages.  |  Pros:

  * Extensible and versatile.
  * It can provide the most information about your URLs.
  * Most content management systems (CMS) automatically generate sitemaps or CMS users can find plenty of sitemap plugins.

|  Cons:

  * Can be cumbersome to work with.
  * Can be complex to maintain the mapping on larger sites, or sites where the URLs change often. 

  
---|---  
RSS, mRSS, and Atom 1.0 |  RSS, mRSS, and Atom 1.0 sitemaps are similar in structure to XML sitemaps, however they are often the easiest to provide because CMSes automatically create them.  |  Pros:

  * Most CMSes automatically generate RSS and Atom feeds.
  * Can be used to provide Google information about your videos.

|  Cons:

  * Besides [HTML and other indexable textual content](/search/docs/crawling-indexing/indexable-file-types), it can only provide information about videos, not images or news. 
  * Can be cumbersome to work with.

  
---|---  
Text sitemap |  The simplest of sitemap formats, it can only list URLs to HTML and other indexable pages.  |  Pros:

  * Simple to do and maintain, especially on large sites.

|  Cons:

  * Limited to HTML and other indexable textual content. 

  
---|---  
  
## Sitemap best practices

The best practices for sitemaps are defined by the [sitemaps protocol](https://www.sitemaps.org/protocol.html). The most overlooked best practices are related to the size limits, sitemap location, and the URLs included in the sitemaps. 

Sitemap size limits: All formats limit a single sitemap to 50MB (uncompressed) or 50,000 URLs. If you have a larger file or more URLs, you must break your sitemap into multiple sitemaps. You can optionally create a [sitemap index](/search/docs/crawling-indexing/sitemaps/large-sitemaps) file and submit that single index file to Google. You can submit multiple sitemaps and sitemap index files to Google. This may be useful if you want to track the search performance of each individual sitemap in Search Console. 

Sitemap file encoding and location: The sitemap file must be UTF-8 encoded. You can host your sitemaps anywhere on your site, but unless you submit your sitemap through Search Console, a sitemap affects only descendants of the parent directory. Therefore, a sitemap posted at the site root can affect all files on the site, which is where we recommend posting your sitemaps. 

Referenced URLs' properties: Use fully-qualified, absolute URLs in your sitemaps. Google will attempt to crawl your URLs exactly as listed. For example, if your site is at `https://www.example.com/`, don't specify a URL such as `/mypage.html` (a relative URL), use the complete, absolute URL: `https://www.example.com/mypage.html`. 

Include the URLs in your sitemap that you want to see in Google's search results. Google generally shows the [canonical URLs](/search/docs/crawling-indexing/consolidate-duplicate-urls) in its search results, which you can influence with sitemaps. If you have different URLs for mobile and desktop versions of a page, we recommend pointing to only one version in a sitemap. However, if you want to point to both URLs, [annotate](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#additional-best-practices) your URLs to indicate the desktop and mobile versions. 

For a complete list of best practices, check out the [sitemaps protocol](https://www.sitemaps.org/protocol.html). 

## XML sitemap

The XML sitemap format is the most versatile of the supported formats. Using the Google supported sitemap extensions, you can also provide additional information about your [images](/search/docs/crawling-indexing/sitemaps/image-sitemaps), [video](/search/docs/crawling-indexing/sitemaps/video-sitemaps), and [news](/search/docs/crawling-indexing/sitemaps/news-sitemap) content, as well as the [localized versions](/search/docs/specialty/international/localized-versions) of your pages. 

Here is a very basic XML sitemap that includes the location of a single URL:
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url>
        <loc>https://www.example.com/foo.html</loc>
        <lastmod>2022-06-04</lastmod>
      </url>
    </urlset>

You can find more complex examples and full documentation at [sitemaps.org](https://www.sitemaps.org/protocol.html). 

### Additional notes about XML sitemaps

  * As with all XML files, all tag values must be [entity escaped](https://www.sitemaps.org/protocol.html#escaping). 
  * Google ignores `<priority>` and `<changefreq>` values. 
  * Google uses the `<lastmod>` value if it's consistently and verifiably (for example by comparing to the last modification of the page) accurate.  The `<lastmod>` value should reflect the date and time of the last significant update to the page. For example, an update to the main content, the structured data, or links on the page is generally considered significant, however an update to the copyright date is not. 

## RSS, mRSS, and Atom 1.0

If your CMS generates an RSS or Atom feed, you can submit the feed's URL as a sitemap. Most CMSes create a feed for you, however keep in mind that this feed only provides information on recent URLs. 

### Additional notes about RSS, mRSS, and Atom 1.0

  * Google accepts RSS 2.0 and Atom 1.0 feeds. 
  * You can use an [mRSS (media RSS) feed](/search/docs/crawling-indexing/sitemaps/video-sitemaps) to provide Google details about video content on your site. 
  * As with all XML files, all tag values must be [entity escaped](https://www.sitemaps.org/protocol.html#escaping). 

## Text sitemap

If you only want to provide web page URLs, you can create a common text file that contains one URL per line and submit that to Google. For example, if you have two pages on your site, you could add them to your text sitemap located at `https://www.example.com/sitemap.txt` as follows: 
    
    
    https://www.example.com/file1.html
    https://www.example.com/file2.html

### Additional notes for text file sitemaps

  * Don't put anything other than URLs in the sitemap file.
  * You can name the text file anything you want, provided it has a `.txt` extension (for instance, sitemap.txt). 

## How to create a sitemap

When creating a sitemap, you're telling search engines about which URLs you prefer to show in search results. These are the [canonical URLs](/search/docs/crawling-indexing/consolidate-duplicate-urls). If you have the same content accessible under different URLs, choose the URL you prefer and include that in the sitemap instead of all URLs that lead to the same content. 

Once you've decided which URLs to include in the sitemap, pick one of the following ways to create a sitemap, depending on your site architecture and size: 

  * Let your CMS generate a sitemap for you. 
  * For sitemaps with less than a few dozen URLs, you can manually create a sitemap. 
  * For sitemaps with more than a few dozen URLs, automatically generate a sitemap.

### Let your CMS generate a sitemap for you

If you're using a CMS such as WordPress, Wix, or Blogger, it's likely that your CMS has already made a sitemap available to search engines. Try searching for information about how your CMS generates sitemaps, or how to create a sitemap if your CMS doesn't generate a sitemap automatically. For example, in case of Wix, search for "wix sitemap", or in case of Blogger, search for "Blogger RSS". 

### Manually create a sitemap

For sitemaps with less than a few dozen URLs, you may be able to manually create a sitemap. For this, open a text editor such as [Windows Notepad](https://www.microsoft.com/en-us/search?q=windows+notepad) or [Nano (Linux, MacOS)](https://www.nano-editor.org/), and follow a syntax described in the Sitemap Formats section. You can name the file anything you like as long as [the characters are allowed in a URL](/maps/url-encoding). 

You can manually create larger sitemaps, but it's a tedious process and hard to maintain long term. 

### Automatically generate a sitemap with tools

For sitemaps with more than a few dozen URLs, you will need to generate the sitemap. There are various tools that can [generate a sitemap](https://www.google.com/search?q=generate+sitemap). However, the best way is to have your website software generate it for you. For example, you can extract your site's URLs from your website's database and then export the URLs to either the screen or actual file on your web server. Talk to your developers or server manager about this solution. If you need inspiration for the code, check out our old, unmaintained collection of [third-party sitemap generators](http://code.google.com/p/sitemap-generators/wiki/SitemapGenerators). 

You don't have to worry about the order of the URLs in your sitemap, it doesn't matter to Google. Note the size requirements for sitemaps; if the sitemap becomes too large, you must split it into smaller sitemaps. Learn more about [managing large sitemaps](/search/docs/crawling-indexing/sitemaps/large-sitemaps). 

## Submit your sitemap to Google

Keep in mind that submitting a sitemap is merely a hint: it doesn't guarantee that Google will download the sitemap or use the sitemap for crawling URLs on the site. There are a few different ways to make your sitemap available to Google. 

  * Submit a sitemap in Search Console using the [Sitemaps report](https://support.google.com/webmasters/answer/7451001). This will allow you to see when Googlebot accessed the sitemap and also potential processing errors. 
  * Use the Search Console API to programmatically [submit a sitemap](/webmaster-tools/v1/sitemaps/submit). 
  * Insert the following line anywhere in your robots.txt file, specifying the path to your sitemap. We will find it the next time we crawl your robots.txt file: 
    
        Sitemap: https://example.com/my_sitemap.xml

  * If you use Atom or RSS, you can use [WebSub](https://www.w3.org/TR/websub/) to broadcast your changes to search engines, including Google. 

## How to cross-submit sitemaps for multiple sites

If you have multiple websites, you can simplify the submission process by creating one or more sitemaps that include URLs for all your verified sites, and saving the sitemaps to a single location. You can choose to use: 

  * A single sitemap that includes URLs for multiple websites, including sites from different domains. For example, the sitemap located at `https://host1.example.com/sitemap.xml` can include the following URLs. 
    * `https://host1.example.com`
    * `https://host2.example.com`
    * `https://host3.example.com`
    * `https://host1.example1.com`
    * `https://host1.example.ch`
  * Individual sitemaps (one for each site) that all reside in a single location. For example, `https://host1.example.com` may host all of these sitemaps: 
    * `https://host1.example.com/host1-example-sitemap.xml`
    * `https://host1.example.com/host2-example-sitemap.xml`
    * `https://host1.example.com/host3-example-sitemap.xml`
    * `https://host1.example.com/host1-example1-sitemap.xml`
    * `https://host1.example.com/host1-example-ch-sitemap.xml`

To submit cross-site sitemaps that are hosted in a single location, you can either use Search Console or robots.txt. 

### Sitemap cross-submission with Search Console

  1. Make sure that you have [verified ownership](https://support.google.com/webmasters/answer/35181) of all the sites that you will add in the sitemap. 
  2. Create a sitemap (or more if you prefer) that includes URLs from all the sites that you want to cover. You can include the sitemaps in a [sitemap index](/search/docs/crawling-indexing/sitemaps/large-sitemaps) file if you prefer and work with that sitemap index from here on. 
  3. Using Google Search Console, [submit your sitemaps or sitemap index file](https://support.google.com/webmasters/answer/7451001). 

### Sitemap cross-submission with robots.txt

  1. Create one or more sitemaps for each individual site. For each individual sitemap file, make sure you include only URLs from that particular site. 
  2. Upload all sitemaps to a single site you have control over, for example `https://sitemaps.example.com`. 
  3. For each individual site, make sure that the robots.txt file references the sitemap for that individual site. For example, if you created a sitemap for `https://example.com/` and you're hosting the sitemap at `https://sitemaps.example.com/sitemap-example-com.xml`, reference the sitemap in the robots.txt file at `https://example.com/robots.txt`. 
    
        # robots.txt file of https://example.com/
    sitemap: https://sitemaps.example.com/sitemap-example-com.xml

## Troubleshooting sitemaps

If you're having trouble with your sitemap, you can investigate the errors with Google Search Console. See Search Console's [sitemaps troubleshooting guide](https://support.google.com/webmasters/answer/7451001#errors) for help.

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
