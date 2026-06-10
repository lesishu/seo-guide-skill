# 多地区网站管理

> 来源：Google Search Central

---

Managing multi-regional and multilingual sites If your site offers different content to users in different languages, countries, or regions, you can optimize Google Search results for your site. What's the difference between multilingual and multi-regional? 

  * A multilingual website is any website that offers content in more than one language. For example, a Canadian business with English and French versions of its site. Google Search tries to find pages that match the language of the searcher.
  * A multi-regional website is one that explicitly targets users in different countries. For example, a product manufacturer that ships to both Canada and the United States. Google Search tries to find the right locale page for the searcher.

Some sites are both multi-regional and multilingual: for example, a site might have different versions for the USA and for Canada, and both French and English versions of the Canadian content. Managing multilingual versions of your site If you have identical content in multiple languages on your site, here are some tips for helping users (and Google Search) find the right page: Use different URLs for different language versions Google recommends using different URLs for each language version of a page rather than using cookies or browser settings to adjust the content language on the page. If you use different URLs for different languages, use [`hreflang` annotations](/search/docs/specialty/international/localized-versions) to help Google Search results link to the correct language version of a page. If you prefer to dynamically change content or reroute the user based on language settings, be aware that Google might not find and crawl all your variations. This is because the Googlebot crawler usually originates from the USA. In addition, the crawler sends HTTP requests without setting `Accept-Language` in the request header. Tell Google about your different language versions [Google supports several different methods for labeling language or region variants of a page](/search/docs/specialty/international/localized-versions), including `hreflang` annotations and sitemaps. Mark your pages appropriately. Make sure the page language is obvious Google uses the visible content of your page to determine its language. We don't use any code-level language information such as `lang` attributes, or the URL. You can help Google determine the language correctly by using a single language for content and navigation on each page, and by avoiding side-by-side translations. Translating only the boilerplate text of your pages while keeping the bulk of your content in a single language (as often happens on pages featuring user-generated content) can create a bad user experience if the same content appears multiple times in search results with various boilerplate languages. Let the user switch the page language If you have multiple versions of a page:

  * Avoid automatically redirecting users from one language version of a site to a different language version of a site. For example, don't redirect based on what you think the user's language may be. These redirections could prevent users (and search engines) from viewing all the versions of your site.
  * Consider adding hyperlinks to other language versions of a page. That way users can click to choose a different language version of the page.

Use language-specific URLs It's fine to use localized words in the URL, or to use an [Internationalized Domain Name (IDN)](https://en.wikipedia.org/wiki/Internationalized_domain_name). However, be sure to use UTF-8 encoding in the URL (in fact, we recommend using UTF-8 wherever possible) and remember to escape the URLs properly when linking to them. Targeting site content to a specific country (geotargeting) You can target your website or parts of it to users in a single specific country that speaks a specific language. This can improve your page rankings in the target country, but at the expense of results in other locales or languages. To geotarget your site on Google:

  * Page or site level: Use locale-specific URLs for your site or page.
  * Page level: [Use `hreflang` or sitemaps](/search/docs/specialty/international/localized-versions) to tell Google which pages apply to which locations or languages.

Remember that geotargeting isn't an exact science, so it's important to consider users who land on the "wrong" version of your site. One way to do this could be to show links on all pages for users to select their region and/or language of choice. Don't use IP analysis to adapt your content. IP location analysis is difficult and generally not reliable. Furthermore, Google may not be able to crawl variations of your site properly. Most, but not all, Google crawls originate from the US, and we don't attempt to vary the location to detect site variations. Use one of the explicit methods shown here (`hreflang`, alternate URLs, and explicit links). Using locale-specific URLs Consider using a URL structure that makes it easy to geotarget your site, or parts of it, to different regions. The following table describes your options: URL structure options   
---  
Country-specific domain `example.de` |  |  Pros:

  * Clear geotargeting
  * Server location irrelevant
  * Easy separation of sites

|  Cons:

  * Expensive (can have limited availability)
  * Requires more infrastructure
  * Strict ccTLD requirements (sometimes)
  * Can only target a single country

  
---|---  
Subdomains with gTLD `de.example.com` |  |  Pros:

  * Easy to set up
  * Allows different server locations
  * Easy separation of sites

|  Cons:

  * Users might not recognize geotargeting from the URL alone (is "de" the language or country?)

  
---|---  
Subdirectories with gTLD `example.com/de/` |  |  Pros:

  * Easy to set up
  * Low maintenance (same host)

|  Cons:

  * Users might not recognize geotargeting from the URL alone
  * Single server location
  * Separation of sites harder

  
---|---  
URL parameters `site.com?loc=de` |  |  Not recommended.  |  Cons:

  * URL-based segmentation difficult
  * Users might not recognize geotargeting from the URL alone

  
---|---  
How does Google determine a target locale? Google relies on a number of signals to determine the best target audience for a page:

  * Country-code top-level domain names (ccTLDs). These are tied to a specific country (for example .de for Germany, .cn for China), and therefore provide a strong signal to both users and search engines that your site is explicitly intended for a certain country. Some countries have restrictions on who can use ccTLDs, so be sure to do your research first. We also treat some vanity ccTLDs (such as .tv and .me) as gTLDs, as we've found that users and website owners frequently see these as being more generic than country-targeted. See Google's list of gTLDs. 
  **`hreflang` statements**, whether in tags, headers, or sitemaps. 
  * Server location (through the IP address of the server). The server location is often physically near your users and can be a signal about your site's intended audience. Some websites use distributed content delivery networks (CDNs) or are hosted in a country with better webserver infrastructure, so it is not a definitive signal. 
  * Other signals. Other signals to identify the intended audience of your site can include local addresses and phone numbers on the pages, the use of local language and currency, links from other local sites, or signals from your [Business Profile](https://www.google.com/business/) (where available). 

What Google doesn't do:

  * Google crawls the web from different locations around the world. We do not attempt to vary the crawler source used for a single site in order to find any possible variations in a page. Therefore, make sure you explicitly tell Google about any locale or language variation that your site exposes, using one of the methods shown here (such as `hreflang` entries, ccTLDs, or explicit links).
  * Google ignores locational `meta` tags (like `geo.position` or `distribution`) or geotargeting HTML attributes.

Handling duplicate pages with multilingual/multi-regional sites If you provide similar or duplicate content on different URLs in the same language as part of a multi-regional site (for instance, if both `example.de/` and `example.com/de/` show similar German language content), pick a preferred version and use the [`rel="canonical"` element](/search/docs/crawling-indexing/consolidate-duplicate-urls) and [`hreflang`](/search/docs/specialty/international/localized-versions) tags to make sure that the correct language or regional URL is served to searchers. Generic top-level domains Generic top-level domains (gTLDs) are domains that aren't associated with specific locations. If your site has a generic top-level domain such as .com, .org, or any of the following domains, and wants to target users in a particular geographic location, explicitly set a country target using one of the methods described previously. Google treats the following top level domains as gTLDs:

  * Generic Top Level Domains: Unless ICANN lists a top-level domain as a [country code top-level domain](https://www.iana.org/domains/root/db) (ccTLD), Google will treat any TLD that resolves through the IANA DNS root zone as a gTLD. Examples:
    * .com
    * .org
    * .edu
    * .gov
    * and many more...
  * Generic regional top-level domains: Although these domains are associated with a geographical region, they are generally treated as generic top-level domains (much like .com or .org): 
    * .eu
    * .asia
  * Generic Country Code Top Level Domains (ccTLDs): Google treats some ccTLDs (such as .tv and .me) as gTLDs, as we've found that users and website owners frequently see these more generic than country-targeted. Here is a list of those ccTLDs (this list may change). 
    * .ad
    * .ai
    * .as
    * .bz
    * .cc
    * .cd
    * .co
    * .dj
    * .fm
    * .io
    * .la
    * .me
    * .ms
    * .nu
    * .sc
    * .sr
    * .su
    * .tv
    * .tk
    * .ws
