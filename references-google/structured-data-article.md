# Article 结构化数据

> 来源：Google Search Central (https://developers.google.com/search/docs/appearance-structured-data-article.txt)

---

# Article (`Article`, `NewsArticle`, `BlogPosting`) structured data

Adding `Article` structured data to your news, blog, and sports article pages can help Google understand more about the web page and show better [title text](/search/docs/appearance/title-link), images, and [date information](/search/docs/appearance/publication-dates) for the article in search results on Google Search and other properties (for example, Google News and the [Google Assistant](/assistant/content/overview)). While there's no markup requirement to be eligible for Google News features like [Top stories](https://support.google.com/news/publisher-center/answer/9607026), you can add `Article` to more explicitly tell Google what your content is about (for example, that it's a news article, who the author is, or what the title of the article is). 

## Example

Here's an example of a page with `Article` structured data. 

#### JSON-LD

<html> <head> <title>Title of a News Article</title> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "NewsArticle", "headline": "Title of a News Article", "image": [ "https://example.com/photos/1x1/photo.jpg", "https://example.com/photos/4x3/photo.jpg", "https://example.com/photos/16x9/photo.jpg" ], "datePublished": "2024-01-05T08:00:00+08:00", "dateModified": "2024-02-05T09:20:00+08:00", "author": [{ "@type": "Person", "name": "Jane Doe", "url": "https://example.com/profile/janedoe123" },{ "@type": "Person", "name": "John Doe", "url": "https://example.com/profile/johndoe123" }] } </script> </head> <body> </body> </html>   

    
    
    <html>
      <head>
        <title>Title of a News Article</title>
        <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "NewsArticle",
          "headline": "Title of a News Article",
          "image": [
            "https://example.com/photos/1x1/photo.jpg",
            "https://example.com/photos/4x3/photo.jpg",
            "https://example.com/photos/16x9/photo.jpg"
           ],
          "datePublished": "2024-01-05T08:00:00+08:00",
          "dateModified": "2024-02-05T09:20:00+08:00",
          "author": [{
              "@type": "Person",
              "name": "Jane Doe",
              "url": "https://example.com/profile/janedoe123"
            },{
              "@type": "Person",
              "name": "John Doe",
              "url": "https://example.com/profile/johndoe123"
          }]
        }
        </script>
      </head>
      <body>
      </body>
    </html>

#### Microdata

<html> <head> <title>Title of a News Article</title> </head> <body> <div itemscope itemtype="https://schema.org/NewsArticle"> <div itemprop="headline">Title of News Article</div> <meta itemprop="image" content="https://example.com/photos/1x1/photo.jpg" /> <meta itemprop="image" content="https://example.com/photos/4x3/photo.jpg" /> <img itemprop="image" src="https://example.com/photos/16x9/photo.jpg" /> <div> <span itemprop="datePublished" content="2024-01-05T08:00:00+08:00"> January 5, 2024 at 8:00am </span> (last modified <span itemprop="dateModified" content="2024-02-05T09:20:00+08:00"> February 5, 2024 at 9:20am </span> ) </div> <div> by <span itemprop="author" itemscope itemtype="https://schema.org/Person"> <a itemprop="url" href="https://example.com/profile/janedoe123"> <span itemprop="name">Jane Doe</span> </a> </span> and <span itemprop="author" itemscope itemtype="https://schema.org/Person"> <a itemprop="url" href="https://example.com/profile/johndoe123"> <span itemprop="name">John Doe</span> </a> </span> </div> </div> </body> </html>   

    
    
    <html>
      <head>
        <title>Title of a News Article</title>
      </head>
      <body>
        <div itemscope itemtype="https://schema.org/NewsArticle">
          <div itemprop="headline">Title of News Article</div>
          <meta itemprop="image" content="https://example.com/photos/1x1/photo.jpg" />
          <meta itemprop="image" content="https://example.com/photos/4x3/photo.jpg" />
          <img itemprop="image" src="https://example.com/photos/16x9/photo.jpg" />
          <div>
            <span itemprop="datePublished" content="2024-01-05T08:00:00+08:00">
              January 5, 2024 at 8:00am
            </span>
            (last modified
            <span itemprop="dateModified" content="2024-02-05T09:20:00+08:00">
              February 5, 2024 at 9:20am
            </span>
            )
          </div>
          <div>
            by
            <span itemprop="author" itemscope itemtype="https://schema.org/Person">
              <a itemprop="url" href="https://example.com/profile/janedoe123">
                <span itemprop="name">Jane Doe</span>
              </a>
            </span>
            and
            <span itemprop="author" itemscope itemtype="https://schema.org/Person">
              <a itemprop="url" href="https://example.com/profile/johndoe123">
                <span itemprop="name">John Doe</span>
              </a>
            </span>
          </div>
        </div>
      </body>
    </html>

##  How to add structured data 

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/search/docs/appearance/structured-data/intro-structured-data). 

Here's an overview of how to build, test, and release structured data.

  1. Add as many recommended properties that apply to your web page. There are no required properties; instead, add the properties that apply to your content. Based on the format you're using, learn where to [insert structured data on the page](/search/docs/appearance/structured-data/intro-structured-data#format-placement).  Using a CMS? It may be easier to use a plugin that's integrated into your CMS.   
Using JavaScript? Learn how to [generate structured data with JavaScript](/search/docs/appearance/structured-data/generate-structured-data-with-javascript).
  2. Follow the guidelines.
  3. Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results). 
  4. Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/search/docs/crawling-indexing/ask-google-to-recrawl). Note: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.
  5. To keep Google informed of future changes, we recommend that you [submit a sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap). You can automate this with the [Search Console Sitemap API](/webmaster-tools/v1/sitemaps).

## Guidelines

You must follow these guidelines to enable structured data to be eligible for inclusion in Google Search results.

Warning: If your site violates one or more of these guidelines, then Google may take [manual action](https://support.google.com/webmasters/answer/2604824) against it. Once you have remedied the problem, you can submit your site for [reconsideration](https://support.google.com/webmasters/answer/35843).

  **Search Essentials**
  **General structured data guidelines**
  * Technical guidelines

### Technical guidelines

  * For multi-part articles, make sure that the `rel=canonical` points at either each individual page or a "view-all" page (and not to page 1 of a multi-part series). Learn more about [canonicalization](/search/docs/crawling-indexing/consolidate-duplicate-urls).
  * If you offer subscription-based access to your website content, or if users must register for access, consider adding structured data for [subscription and paywalled content](/search/docs/appearance/structured-data/paywalled-content).

## Structured data type definitions

To help Google better understand your page, include as many recommended properties that apply to your web page. There are no required properties; instead, add the properties that apply to your content. 

### `Article` objects

Article objects must be based on one of the following schema.org types: [`Article`](https://schema.org/Article), [`NewsArticle`](https://schema.org/NewsArticle), [`BlogPosting`](https://schema.org/BlogPosting).

The Google-supported properties are the following:

Recommended properties  
---  
`author` | `[Person](https://schema.org/Person)` or `[Organization](https://schema.org/Organization)` The author of the article. To help Google best understand authors across various features, we recommend following the author markup best practices.   
`author.name` | `[Text](https://schema.org/Text)` The name of the author.  
`author.url` | `[URL](https://schema.org/URL)` A link to a web page that uniquely identifies the author of the article. For example, the author's social media page, an "about me" page, or a bio page. If the URL is an internal profile page, we recommend marking up that author using [profile page structured data](/search/docs/appearance/structured-data/profile-page). You can use the `sameAs` property as an alternative. Google can understand both `sameAs` and `url` when disambiguating authors.  
`dateModified` | `[DateTime](https://schema.org/DateTime)` The date and time the article was most recently modified, in [ISO 8601 format](https://wikipedia.org/wiki/ISO_8601). We recommend that you provide timezone information; otherwise, we will default to [the timezone used by Googlebot](/search/docs/crawling-indexing/googlebot#timezone). Add the `dateModified` property if you want to provide more accurate date information to Google. The [Rich Results Test](https://search.google.com/test/rich-results) doesn't show a warning for this property, as it's only recommended if you decide that it's applicable to your site.  
`datePublished` | `[DateTime](https://schema.org/DateTime)` The date and time the article was first published, in [ISO 8601 format](https://wikipedia.org/wiki/ISO_8601). We recommend that you provide timezone information; otherwise, we will default to [the timezone used by Googlebot](/search/docs/crawling-indexing/googlebot#timezone). Add the `datePublished` property if you want to provide more accurate date information to Google. The [Rich Results Test](https://search.google.com/test/rich-results) doesn't show a warning for this property, as it's only recommended if you decide that it's applicable to your site.  
`headline` | `[Text](https://schema.org/Text)` The title of the article. Consider using a concise title, as long titles may be truncated on some devices.  
`image` | Repeated `[ImageObject](https://schema.org/ImageObject)` or `[URL](https://schema.org/URL)` The URL to an image that is representative of the article. Use images that are relevant to the article, rather than logos or captions. Additional image guidelines: 

  * Image URLs must be crawlable and indexable. To check if Google can access your URLs, use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289).
  * Images must represent the marked up content.
  * Images must be in a file format that's [supported by Google Images](/search/docs/appearance/google-images#supported-image-formats).
  * For best results, we recommend providing multiple high-resolution images (minimum of 50K pixels when multiplying width and height) with the following aspect ratios: 16x9, 4x3, and 1x1.

For example:
    
    
    "image": [
      "https://example.com/photos/1x1/photo.jpg",
      "https://example.com/photos/4x3/photo.jpg",
      "https://example.com/photos/16x9/photo.jpg"
    ]  
  
## Author markup best practices

To help Google best understand and represent the author of the content, we recommend following these best practices when specifying authors in markup: 

Best practices for author markup  
---  
  
###  Include all authors in the markup 

|  Make sure that all the authors that are presented as authors on the web page are also included in markup.   
  
###  Specifying multiple authors 

|  When specifying multiple authors, list each author in their own `author` field: 
    
    
    "author": [
      {"name": "Willow Lane"},
      {"name": "Regula Felix"}
    ]

Don't merge multiple authors in the same `author` field: 
    
    
    "author": {
      "name": "Willow Lane, Regula Felix"
    }  
  
###  Use additional fields 

|  To help Google better understand who the author is, we strongly recommend using the `type` and `url` (or `sameAs`) properties. Use valid URLs for the `url` or `sameAs` properties.  For example, if the author is a person, you could link to an author's page that provides more information about the author: 
    
    
    "author": [
      {
        "@type": "Person",
        "name": "Willow Lane",
        "url": "https://www.example.com/staff/willow_lane"
      }
    ]

If the author is an organization, you could link to the organization's home page. 
    
    
    "author":
      [
        {
          "@type":"Organization",
          "name": "Some News Agency",
          "url": "https://www.example.com/"
      }
    ]  
  
###  Only specify the author's name in the `author.name` property 

|  In the `author.name` property, only specify the name of the author. Don't add any other piece of information. More specifically, don't add the following information: 

  * The name of the publisher. Instead, use the `publisher` property.
  * The author's job title. Instead, use the appropriate property if you want to specify that information ([`jobTitle`](https://schema.org/jobTitle)).
  * Honorific prefix or suffix. Instead, use the appropriate property if you want to specify that information ([`honorificPrefix`](https://schema.org/honorificPrefix) or [`honorificSuffix`](https://schema.org/honorificSuffix)).
  * Introductory words (for example, don't include words like "posted by").

    
    
    "author":
      [
        {
          "@type": "Person",
          "name": "Echidna Jones",
          "honorificPrefix": "Dr",
          "jobTitle": "Editor in Chief"
        }
      ],
    "publisher":
      [
        {
          "@type": "Organization",
          "name": "Bugs Daily"
        }
      ]
    }  
  
###  Use the appropriate `Type`

|  Use the `Person` type for people, and the `Organization` type for organizations. Don't use the `Thing` type, and don't use the wrong type (for example, using the `Organization` type for a person).  
  
Here's an example that applies the author markup best practices: 
    
    
    "author":
      [
        {
          "@type": "Person",
          "name": "Willow Lane",
          "jobTitle": "Journalist",
          "url": "https://www.example.com/staff/willow-lane"
        },
        {
          "@type": "Person",
          "name": "Echidna Jones",
          "jobTitle": "Editor in Chief",
          "url": "https://www.example.com/staff/echidna-jones"
        }
      ],
    "publisher":
      {
        "@type": "Organization",
        "name": "The Daily Bug",
        "url": "https://www.example.com"
      },
      // + Other fields related to the article...
    }

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you. 

  * If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
  * Google does not guarantee that features that consume structured data will show up in search results. For a list of common reasons why Google may not show your content in a rich result, see the [General Structured Data Guidelines](/search/docs/appearance/structured-data/sd-policies).
  * You might have an error in your structured data. Check the [list of structured data errors](https://support.google.com/webmasters/answer/13300873) and the [Unparsable structured data report](https://support.google.com/webmasters/answer/9166415).
  * If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results). To fix [structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the [Manual Actions report](https://support.google.com/webmasters/answer/9044175). 
  * Review the guidelines again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues. 
  **Troubleshoot missing rich results / drop in total rich results**.
  * Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](/search/help/crawling-index-faq). 
  * Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
