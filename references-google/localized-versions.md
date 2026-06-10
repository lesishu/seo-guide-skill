# 本地化版本页面指南

> 来源：Google Search Central

---

Tell Google about localized versions of your page If you have multiple versions of a page for different languages or regions, tell Google about these different variations. Doing so will help Google Search point users to the most appropriate version of your page by language or region. Note that even without taking action, Google might still find alternate language versions of your page, but it is usually best for you to explicitly indicate your language- or region-specific pages. Some example scenarios where indicating alternate pages is recommended:

  * If you keep the main content in a single language and translate only the template, such as the navigation and footer. Pages that feature user-generated content, like forums, typically do this.
  * If your content has small regional variations with similar content, in a single language. For example, you might have English-language content targeted to the US, GB, and Ireland.
  * If your site content is fully translated into multiple languages. For example, you have both German and English versions of each page.

Localized versions of a page are only considered [duplicates](/search/docs/crawling-indexing/consolidate-duplicate-urls) if the main content of the page remains untranslated. Methods for indicating your alternate pages There are three ways to indicate multiple language/locale versions of a page to Google:

  * HTML
  * HTTP Headers
  * Sitemap

The three methods are equivalent from Google's perspective and you can choose the method that's the most convenient for your site. While you can use all three methods at the same time, there's no benefit in Search (in fact, it maybe be much harder to manage three implementations instead of just picking one).  Use `hreflang` to tell Google about the variations of your content, so that we can understand that these pages are localized variations of the same content. Google doesn't use `hreflang` or the HTML `lang` attribute to detect the language of a page; instead, we use algorithms to determine the language.  Guidelines for all methods

  * Each language version must list itself as well as all other language versions.
  * Alternate URLs must be fully-qualified, including the transport method (http/https), so:  
`https://example.com/foo`, not `//example.com/foo` or `/foo`
  * Alternate URLs do not need to be in the same domain.
  * If you have several alternate URLs targeted at users with the same language but in different locales, it's a good idea to also provide a catchall URL for geographically unspecified users of that language. For example, if you have specific URLs for English speakers in Ireland (`en-ie`), Canada (`en-ca`), and Australia (`en-au`), provide a generic English (`en`) page for searchers in the US, UK, and all other English-speaking locations. It can be one of the specific pages, if you choose. 
  * If two pages don't both point to each other, the tags will be ignored. This is so that someone on another site can't arbitrarily create a tag naming itself as an alternative version of one of your pages.
  * If it becomes difficult to maintain a complete set of bidirectional links for every language, you can omit some languages on some pages; Google will still process the ones that point to each other. However, it is important to link newly expanded language pages bidirectionally to the originating/dominant language(s). For example, if your site was originally created in French with URLs on `.fr`, it's more important to bidirectionally link newer Mexican (`.mx`) and Spanish (`.es`) pages to your strong `.fr` presence, rather than to bidirectionally link your new Spanish language variant pages (`.mx` and `.es`) to each other.
  * Consider adding a fallback page for unmatched languages, especially on language/country selectors or auto-redirecting home pages. Use the the `x-default` value:  
`<link rel="alternate" href="https://example.com/" hreflang="x-default" />`

HTML tags Add `<link rel="alternate" hreflang="lang_code"... >` elements to your page header to tell Google all of the language and region variants of a page. This is useful if you don't have a sitemap or the ability to specify HTTP response headers for your site.  For each variation of the page, include a set of `<link>` elements in the `<head>` element, one link for each page variant including itself. The set of links is identical for every version of the page. See the additional guidelines. Here is the syntax of each `link` element:
    
    
    <link rel="alternate" hreflang="lang_code" href="url_of_page" />

Syntax  
---  
`lang_code` |  A supported language/region code targeted by this version of the page, or `x-default` to match any language not explicitly listed by an `hreflang` tag on the page.   
`url_of_page` |  The fully-qualified URL for the version of this page for the specified language/region.   
The `<link>` tags must be inside a [well-formed `<head>` section](/search/docs/crawling-indexing/valid-page-metadata) of the HTML. If in doubt, paste code from your rendered page into an [HTML validator](https://validator.w3.org/) to ensure that the links are inside the `<head>` element. Additionally, don't combine `link` tags for alternate representations of the document; for example don't combine `hreflang` annotations with other attributes such as `media` in a single `<link>` tag.  Example Example Widgets, Inc has a website that serves users in the USA, UK, and Germany. The following URLs contain substantially the same content, but with regional variations: URLs with regional variations  
---  
`https://en.example.com/page.html` | Generic English language home page that contains information about fees for shipping internationally from the USA.  
`https://en-gb.example.com/page.html` | UK home page that displays prices in pounds sterling.  
`https://en-us.example.com/page.html` | US home page that displays prices in US dollars.  
`https://de.example.com/page.html` | German language home page.  
`https://www.example.com/` | Default page that doesn't target any language or locale; it has selectors to let users pick their language and region.  
Note that the language-specific subdomains in these URLs (`en`, `en-gb`, `en-us`, `de`) are not used by Google to determine the target audience for the page; you must explicitly map the target audience. Here is the HTML that would be in the `<head>` section of all the pages listed in the URLs with regional variations table. It would direct US, UK, generic English speakers, and German speakers to localized pages, and all others to a generic home page. Google Search returns the appropriate result for the user, according to their browser settings.
    
    
    <head>
     <title>Widgets, Inc</title>
      <link rel="alternate" hreflang="en-gb"
           href="https://en-gb.example.com/page.html" />
      <link rel="alternate" hreflang="en-us"
           href="https://en-us.example.com/page.html" />
      <link rel="alternate" hreflang="en"
           href="https://en.example.com/page.html" />
      <link rel="alternate" hreflang="de"
           href="https://de.example.com/page.html" />
     <link rel="alternate" hreflang="x-default"
           href="https://www.example.com/" />
    </head>

HTTP Headers You can return an [HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) with your page's GET response to tell Google about all of the language and region variants of a page. This is useful for non-HTML files (like PDFs). Here is the format of the header:
    
    
    Link: <url1>; rel="alternate"; hreflang="lang_code_1", <url2>; rel="alternate"; hreflang="lang_code_2", ...

Syntax  
---  
`<url_x>` | The fully-qualified URL of the alternate page corresponding to the locale string assigned to the associated `hreflang` attribute. The URL must include surrounding `<` and `>` marks. Example: `<https://www.google.com>`  
`lang_code_x` | A supported language/region code targeted by this version of the page, or `x-default` to matches any language not explicitly listed by an `hreflang` tag on the page.  
You must specify a set of `<url>`, `rel="alternate"`, and `hreflang` values for every version of the page including the requested version, separated by a comma as shown in the following example. The `Link:` header returned for every version of a page is identical. See the additional guidelines. Example Here is an example `Link:` header returned by a site that has three versions of a PDF file: one for English speakers, one for German speakers from Switzerland, and one for all other German speakers:
    
    
    Link: <https://example.com/file.pdf>; rel="alternate"; hreflang="en",
          <https://de-ch.example.com/file.pdf>; rel="alternate"; hreflang="de-ch",
          <https://de.example.com/file.pdf>; rel="alternate"; hreflang="de"

Sitemap You can use an [XML sitemap](/search/docs/crawling-indexing/sitemaps/overview) to tell Google all of the language and region variants for each URL. To do so, add a `<loc>` element specifying a single URL, with child `<xhtml:link>` entries listing every language/locale variant of the page including itself. Therefore if you have 3 versions of a page, your sitemap will have entries for the URLs of each version, and each entry will have 3 identical child entries.  Sitemap rules:

  * Specify the xhtml namespace as follows: 
    
        xmlns:xhtml="http://www.w3.org/1999/xhtml"

  * Create a separate `<url>` element for each URL as you would with any other sitemap. 
  * Each `<url>` element must include a `<loc>` child indicating the page URL. 
  * Each `<url>` element must have a child element `<xhtml:link rel="alternate" hreflang="supported_language-code">` that lists every alternate version of the page, including itself. The order of these child `<xhtml:link>` elements doesn't matter, though you might want to keep them in the same order to make them easier for you to check for mistakes. Child elements don't count towards the URL limit for sitemaps. 
  * Upload the sitemap to a directory on your site that the sitemap is applicable to. Keep in mind that a sitemap can only contain descendant URLs of the directory where the sitemap is hosted from. 
  * Our [documentation on sitemaps](/search/docs/crawling-indexing/sitemaps/build-sitemap) also applies to the sitemap extensions. Make sure to follow [general sitemap guidelines](/search/docs/crawling-indexing/sitemaps/build-sitemap#general-guidelines).
  * See the additional guidelines.

Example Here is an English language page targeted at English speakers worldwide, with equivalent versions of this page targeted at German speakers worldwide and German speakers located in Switzerland. Here are all the URLs present on your site:

  * `www.example.com/english/page.html` targeted at English speakers.
  * `www.example.de/deutsch/page.html` targeted at German speakers.
  * `www.example.de/schweiz-deutsch/page.html` targeted at German speakers in Switzerland.

Here is the sitemap for those three pages:
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:xhtml="http://www.w3.org/1999/xhtml">
      <url>
        <loc>https://www.example.com/english/page.html</loc>
        <xhtml:link
                   rel="alternate"
                   hreflang="de"
                   href="https://www.example.de/deutsch/page.html"/>
        <xhtml:link
                   rel="alternate"
                   hreflang="de-ch"
                   href="https://www.example.de/schweiz-deutsch/page.html"/>
        <xhtml:link
                   rel="alternate"
                   hreflang="en"
                   href="https://www.example.com/english/page.html"/>
      </url>
      <url>
        <loc>https://www.example.de/deutsch/page.html</loc>
        <xhtml:link
                   rel="alternate"
                   hreflang="de"
                   href="https://www.example.de/deutsch/page.html"/>
        <xhtml:link
                   rel="alternate"
                   hreflang="de-ch"
                   href="https://www.example.de/schweiz-deutsch/page.html"/>
        <xhtml:link
                   rel="alternate"
                   hreflang="en"
                   href="https://www.example.com/english/page.html"/>
      </url>
      <url>
        <loc>https://www.example.de/schweiz-deutsch/page.html</loc>
        <xhtml:link
                   rel="alternate"
                   hreflang="de"
                   href="https://www.example.de/deutsch/page.html"/>
        <xhtml:link
                   rel="alternate"
                   hreflang="de-ch"
                   href="https://www.example.de/schweiz-deutsch/page.html"/>
        <xhtml:link
                   rel="alternate"
                   hreflang="en"
                   href="https://www.example.com/english/page.html"/>
      </url>
    </urlset>

Supported language and region codes The `hreflang` attribute's value is comprised of one or optionally two values, separated by a dash. For example, `en-US`. The first code of the `hreflang` attribute is the language code (in [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format) followed by an optional second code that represents the region code (in [ISO 3166-1 Alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format) of an alternate URL. Only language codes listed in ISO 639-1 and region codes listed in ISO 3166-1 Alpha 2 are supported; other codes that aren't listed in those standards, such as es-419, aren't supported. Warning: You can't specify the country code by itself. The first code stands for the language and Google doesn't automatically derive the language from a country code.  To target different language speakers in Belgium, you might use the following language and region codes:

  * Good (German for users in Belgium): `de-be`
  * Good (Dutch for users in Belgium): `nl-be`
  * Good (French for users in Belgium): `fr-be`
  * Bad because the first code is for language (`be` is the Belarusian language code): `be`

To simplify your labeling, you can specify a language code by itself. For example:

  * `de`: German language content, independent of region
  * `en-GB`: English language content, for users in the UK
  * `de-ES`: German language content, for users in Spain

For language script variations, the proper script is derived from the country. For example, when using `zh-TW` for users in Taiwan, the language script is automatically derived (in this example: Chinese-Traditional). You can also specify the script itself explicitly using [ISO 15924](https://unicode.org/iso15924/iso15924-codes.html), like this:

  * `zh-Hant`: Chinese (Traditional)
  * `zh-Hans`: Chinese (Simplified)

Like with other language codes, you can also specify an optional region. For example, use `zh-Hans-US` to specify Chinese (Simplified) for users in the United States.  Use the `x-default` value for unmatched languages The reserved `x-default` value is used when no other language/region matches the user's browser setting. This value is recommended for specifying the fallback page for users whose language settings don't match any of your site's localized versions. While you can use the `x-default` value for any page, it was designed for language selector pages and so it will work best with those.  There's no need to specify a language code for the `x-default` value; the page is targeted to users whose language settings are unmatched on your site, thus the language of the page is irrelevant.  To implement the `hreflang="x-default"` annotation, add an additional `link` tag to the existing `hreflang` annotations, and set the `href` attribute to the URL where you want your users to land if your site doesn't support their language. For example, an HTML implementation may look like this: 
    
    
    <link rel="alternate" href="https://example.com/en-gb" hreflang="en-gb" />
    <link rel="alternate" href="https://example.com/en-us" hreflang="en-us" />
    <link rel="alternate" href="https://example.com/en-au" hreflang="en-au" />
    <link rel="alternate" href="https://example.com/country-selector" hreflang="x-default" />

Troubleshooting Common Mistakes Here are the most common mistakes with `hreflang` usage:

  * Missing return links: If page X links to page Y, page Y must link back to page X. If this is not the case for all pages that use `hreflang` annotations, those annotations may be ignored or not interpreted correctly. For example, considering this link on `https://de.example.com/index.html`: 
    
        <link rel="alternate" hreflang="en-gb" href="https://en-gb.example.com/index.html" />

You must also have a `hreflang` link on `https://en-gb.example.com/index.html` that points back to the `de` version of the content: 
    
        <link rel="alternate" hreflang="de" href="https://de.example.com/index.html" />

  * Incorrect language codes: Make sure that all language codes you use identify the language (in ISO 639-1 format) and optionally the region (in ISO 3166-1 Alpha 2 format) of an alternate URL. Specifying the region alone is not valid. 
  * Incorrect region codes: Make sure you're using officially assigned code elements for the regions you're trying to identify (in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). If you use codes that are listed as reserved for something else, Google Search ignores that part of the annotation (for example, using `EU`, `UN`, or `UK` in `hreflang` annotations doesn't have an effect on Google Search). 

Debugging `hreflang` errors There are many third-party tools available that you can use to debug `hreflang` annotations. Here are a few popular tools. These tools are not maintained or checked by Google. 

  **Aleyda Solis's `hreflang` tags generator tool** for generating or modifying `hreflang` tags. 
  **Merkle SEO `hreflang` tag testing tool** for validating `hreflang` tags on a single live page.
