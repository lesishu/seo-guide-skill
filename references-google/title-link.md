# 标题链接（Title Link）优化

> 来源：Google Search Central (https://developers.google.com/search/docs/appearance-title-link.txt)

---

# Influencing your title links in search results

A title link is the title of a search result on Google Search and other properties (for example, Google News) that links to the web page. Google uses a number of different sources to automatically determine the title link, but you can indicate your preferences by following our best practices for influencing title links. 

An illustration of a text result in Google Search, with a highlighted box around the title link part

[How to make crispy fried eggs](https://wikipedia.org/wiki/Fried_egg)

##  Best practices for influencing title links 

Title links are critical to giving users a quick insight into the content of a result and why it's relevant to their query. It's often the primary piece of information people use to decide which result to click, so it's important to use high-quality title text on your web pages.

  * Make sure every page on your site has a title specified in the `<title>` element.
  * Write descriptive and concise text for your `<title>` elements. Avoid vague descriptors like "Home" for your home page, or "Profile" for a specific person's profile.   
Also avoid unnecessarily long or verbose text in your `<title>` elements. While there's no limit on how long a `<title>` element can be, the title link is truncated in Google Search results as needed, typically to fit the device width. 
  * Avoid keyword stuffing. It's sometimes helpful to have a few descriptive terms in the `<title>` element, but there's no reason to have the same words or phrases appear multiple times. Title text like "Foobar, foo bar, foobars, foo bars" doesn't help the user, and this kind of [keyword stuffing](/search/docs/essentials/spam-policies#keyword-stuffing) can make your results look spammy to Google and to users.
  * Avoid repeated or boilerplate text in `<title>` elements. It's important to have distinct text that describes the content of the page in the `<title>` element for each page on your site. Titling every page on a commerce site "Cheap products for sale", for example, makes it impossible for users to distinguish between two pages. Long text in the `<title>` element that varies by only a single piece of information ("boilerplate" titles) is also bad; for example, a common `<title>` element for all pages with text like "Band Name - See videos, lyrics, posters, albums, reviews and concerts" contains a lot of uninformative text. 

One solution is to dynamically update the `<title>` element to better reflect the actual content of the page. For example, include the words "video" and "lyrics" only if that particular page contains video or lyrics. 

  * Brand your titles concisely. The `<title>` element on your site's home page is a reasonable place to include some additional information about your site. For example: 

> <title>ExampleSocialSite, a place for people to meet and mingle</title>

But displaying that text in the `<title>` element of every single page on your site will look repetitive if several pages from your site are returned for the same query. In this case, consider including just your [site name](/search/docs/appearance/site-names) at the beginning or end of each `<title>` element, separated from the rest of the text with a delimiter such as a hyphen, colon, or pipe, like this: 

> <title>ExampleSocialSite: Sign up for a new account.</title>

  * Make it clear which text is the main title for the page. Google looks at various sources when creating title links, including the main visual title, heading elements, and other large and prominent text, and it can be confusing if multiple headings carry the same visual weight and prominence. Consider ensuring that your main title is distinctive from other text on a page and stands out as being the most prominent on the page (for example, using a larger font, putting the title text in the first visible `<h1>` element on the page, etc).
  * Be careful about disallowing search engines from crawling your pages. Using the [robots.txt](/search/reference/robots_txt) protocol on your site can stop Google from crawling your pages, but it may not always prevent them from being indexed. For example, Google may index your page if we discover it by following a link from someone else's site. If we don't have access to the content on your page, we will rely on off-page content to generate the title link, such as anchor text from other sites. To prevent a URL from being indexed, you can use the [`noindex` rule](/search/docs/crawling-indexing/block-indexing).
  * Use the same language and writing system (meaning, the script or alphabet for a given language) as the primary content on your pages. For example, if a page is written in Hindi, make sure to also write the `<title>` element in Hindi (don't write title text in English or transliterate the title into Latin characters).   
Google tries to show a title link that matches the primary language and writing system of a page. If Google determines that a `<title>` element does not match the writing system or language of the page's primary content, we may choose a different text as the title link.
  * Avoid including flight price information in `<title>` elements. Our systems will likely not show price information when generating title links for flight pages. This is because pricing for flights can change so fast (sometimes every few minutes), that what's shown in title links may not correspond to the actual price on the landing page. 

## How title links in Google Search are created

Google's generation of title links on the Google Search results page is completely automated and takes into account both the content of a page and references to it that appear on the web. The goal of the title link is to best represent and describe each result.

Google Search uses the following sources to automatically determine title links:

  * Content in `<title>` elements
  * Main visual title shown on the page
  * Heading elements, such as `<h1>` elements
  * Content in `og:title` `meta` tags
  * Other content that's large and prominent through the use of style treatments
  * Other text contained in the page
  * Anchor text on the page
  * Text within links that point to the page
  **`WebSite` structured data**

Keep in mind that Google has to recrawl and reprocess the page to notice updates to these sources, which may take a few days to a few weeks. If you've made changes, you can [request that Google recrawl your pages](/search/docs/crawling-indexing/ask-google-to-recrawl). 

While we can't manually change title links for individual sites, we're always working to make them as relevant as possible. You can help improve the quality of the title link that's displayed for your page by following the best practices. 

## Common issues and how Google manages them

Why the title link in search results might differ from the page's `<title>` element or main heading: If we've detected an issue on the page, we may try to generate an improved title link from anchors, on-page text, or other sources. 

Here are the most common issues we see with title links in search results. To avoid these issues, follow the best practices for influencing title links. 

Common issues  
---  
  
###  Half-empty `<title>` elements 

|  When part of the title text is missing. For example: 

> <title>| Site Name</title>

Google Search looks at information in header elements or other large and prominent text on the page to produce a title link: 

> Product Name | Site Name  
  
###  Obsolete `<title>` elements 

|  When the same page is used year-after-year for recurring information, but the `<title>` element didn't get updated to reflect the latest date. For example: 

> <title>2020 admissions criteria - University of Awesome</title>

In this example, the page has a large, visible title that says "2021 admissions criteria", and the `<title>` element wasn't updated to the current date. Google Search may detect this inconsistency and uses the right date from the visible title on the page in the title link: 

> 2021 admissions criteria - University of Awesome  
  
###  Inaccurate `<title>` elements 

|  When the `<title>` elements don't accurately reflect what the page is about. For example, the page could have dynamic content with the following `<title>` element: 

> `<title>`Giant stuffed animals, teddy bears, polar bears - Site Name</title>

Google Search tries to determine if the `<title>` element isn't accurately showing what a page is about. Google Search might modify the title link to better help users if it determines that the page title doesn't reflect the page content. For example: 

> Stuffed animals - Site Name  
  
###  Micro-boilerplate text in `<title>` elements 

|  When there are repeated boilerplate text in `<title>` elements for a subset of pages within a site. For example, a television website has multiple pages that share the same `<title>` element that omits the season numbers, and it's not clear which page is for what season. That produces duplicate `<title>` elements like this: 

> <title>My so-called amazing TV show</title>

> <title>My so-called amazing TV show</title>

> <title>My so-called amazing TV show</title>

Google Search can detect the season number used in large, prominent title text and insert the season number in the title link: 

> Season 1 - My so-called amazing TV show

> Season 2 - My so-called amazing TV show

> Season 3 - My so-called amazing TV show  
  
###  No clear main title 

|  When there's more than one large, prominent heading, and it isn't clear which text is the main title of the page. For example, a page has two or more headings that use the same styling or heading level. If Google Search detects that there are multiple large, prominent headings, it may use the first heading as the text for the title link. Consider ensuring that your main heading is distinctive from other text on a page and stands out as being the most prominent on the page (for example, using a larger font, putting the title text in the first visible `<h1>` element on the page, etc).   
  
###  Mismatch of writing system or language used in `<title>` elements 

|  When the writing system or language of the text in `<title>` elements doesn't match the writing system or language of the primary text on a page. For example, when a page is in written in Hindi, but the title includes text in English or is transliterated into Latin characters. If Google detects a mismatch, it may generate a title link that better matches the primary content. Consider ensuring that the script and language matches what is most prominent on the page.   
  
###  Duplication of the [site name](/search/docs/appearance/site-names) in the `<title>` element 

|  In the case of domain-level site names, Google may omit the site name from the title link, if it's repetitive with the [site name that's already shown in the search result](/search/docs/appearance/site-names).   
  
##  Submitting feedback about title links 

If you're seeing your pages appear in the search results with modified title links, check whether your page has one of the issues that Google adjusts for. If not, consider whether the title link in search results is a better fit for the query. To discuss your pages' title links and get feedback about your pages from other site owners, join our [Google Search Central Help Community](https://support.google.com/webmasters/community).

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
