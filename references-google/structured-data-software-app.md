* [ Home ](https://developers.google.com/)
  * [ Search Central ](https://developers.google.com/search)
  * [ Documentation ](https://developers.google.com/search/docs)

Send feedback

# Software app (`SoftwareApplication`) structured data

Mark up software application information in the body of a web page to better display your app details in Google Search results.

![Software application rich result in Google Search results](/static/search/docs/images/software-apps.png) **Note** : The actual appearance in search results might be different. You can preview most features with the [Rich Results Test](https://support.google.com/webmasters/answer/7445569).

##  How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/search/docs/appearance/structured-data/intro-structured-data).

Here's an overview of how to build, test, and release structured data.

  1. Add the required properties. Based on the format you're using, learn where to [insert structured data on the page](/search/docs/appearance/structured-data/intro-structured-data#format-placement).  **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.
**Using JavaScript?** Learn how to [generate structured data with JavaScript](/search/docs/appearance/structured-data/generate-structured-data-with-javascript).
  2. Follow the guidelines.
  3. Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).
  4. Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/search/docs/crawling-indexing/ask-google-to-recrawl). **Note** : Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.
  5. To keep Google informed of future changes, we recommend that you [submit a sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap). You can automate this with the [Search Console Sitemap API](/webmaster-tools/v1/sitemaps).

## Examples

JSON-LD

Here's an example of a software app in JSON-LD:

<html> <head> <title>Angry Birds</title> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Angry Birds", "operatingSystem": "ANDROID", "applicationCategory": "GameApplication", "aggregateRating": { "@type": "AggregateRating", "ratingValue": 4.6, "ratingCount": 8864 }, "offers": { "@type": "Offer", "price": 1.00, "priceCurrency": "USD" } } </script> </head> <body> </body> </html>

    <html>
      <head>
        <title>Angry Birds</title>
        <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "SoftwareApplication",
          "name": "Angry Birds",
          "operatingSystem": "ANDROID",
          "applicationCategory": "GameApplication",
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": 4.6,
            "ratingCount": 8864
          },
          "offers": {
            "@type": "Offer",
            "price": 1.00,
            "priceCurrency": "USD"
          }
        }
        </script>
      </head>
      <body>
      </body>
    </html>