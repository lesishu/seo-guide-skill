# 结构化数据通用指南

> 来源：Google Search Central (https://developers.google.com/search/docs/appearance-structured-data-sd-policies.txt)

---

# General structured data guidelines

To be eligible for rich result appearance in Google Search results, structured data shouldn't violate the [Content policies for Google Search](https://support.google.com/websearch/answer/10622781) (which include our [spam policies](/search/docs/essentials/spam-policies)). In addition, this page details the general guidelines that apply to all structured data: they must be followed in order to be eligible for appearance as a rich result in Google Search. 

If your page contains a [structured data issue](https://support.google.com/webmasters/answer/9044175#spammy-structured-markup), it can result in a manual action. A structured data manual action means that a page loses eligibility for appearance as a rich result; it doesn't affect how the page ranks in Google web search. To check if you have a manual action, open the [Manual Actions report in Search Console](https://search.google.com/search-console/manual-actions).

Important: Google does not guarantee that your structured data will show up in search results, even if your page is marked up correctly according to the [Rich Results Test](https://search.google.com/test/rich-results). Here are some common reasons why:

  * Using structured data enables a feature to be present, it does not guarantee that it will be present. The Google algorithm tailors search results to create what it thinks is the best search experience for a user, depending on many variables, including search history, location, and device type. In some cases it may determine that one feature is more appropriate than another, or even that a [text result](/search/docs/appearance/visual-elements-gallery#text-result) is best.
  * The structured data is not representative of the main content of the page, or is potentially misleading.
  * The structured data is incorrect in a way that the Rich Results Test was not able to catch.
  * The content referred to by the structured data is hidden from the user.
  * The page doesn't meet the guidelines for structured data described on this page, the guidelines for a specific structured data feature, the [Search Essentials](/search/docs/essentials), or the [Content policies for Google Search](https://support.google.com/websearch/answer/10622781).

## Technical guidelines

You can test compliance with technical guidelines using the [Rich Results Test](https://search.google.com/test/rich-results) and the [ URL Inspection tool](https://support.google.com/webmasters/answer/9012289), which catch most technical errors.

### Format

In order to be eligible for rich results, mark up your site's pages using one of [three supported formats](/search/docs/appearance/structured-data/intro-structured-data#structured-data-format):

  * JSON-LD (recommended)
  * Microdata
  * RDFa

### Access

Don't block your structured data pages to Googlebot using robots.txt, [`noindex`](/search/docs/crawling-indexing/block-indexing), or any other access control methods.

## Quality guidelines

These quality guidelines are not easily testable using an automated tool. Violating a quality guideline can prevent syntactically correct structured data from being displayed as a rich result in Google Search, or possibly cause it to be [marked as spam](https://support.google.com/webmasters/answer/3498001).

### Content

  * Follow the [spam policies for Google web search](/search/docs/essentials/spam-policies).
  * Provide up-to-date information. We won't show a rich result for time-sensitive content that is no longer relevant.
  * Provide original content that you or your users have generated.
  * Don't mark up content that is not visible to readers of the page. For example, if the JSON-LD markup describes a performer, the HTML body must describe that same performer.
  * Don't mark up irrelevant or misleading content, such as fake reviews or content unrelated to the focus of a page.
  * Don't use structured data to deceive or mislead users. Don't impersonate any person or organization, or misrepresent your ownership, affiliation, or primary purpose.
  * Content in structured data must also follow the additional content guidelines or policies, as documented in the specific feature guide. For example, content in `JobPosting` structured data must follow the [job posting content policies](/search/docs/appearance/structured-data/job-posting#content-policies).

### Relevance

Your structured data must be a true representation of the page content. Here are some examples of irrelevant data:

  * A sports live streaming site labeling broadcasts as local events.
  * A woodworking site labeling instructions as recipes.

### Completeness

  * Specify all required properties listed in the [documentation for your specific rich result type](/search/docs/appearance/structured-data/search-gallery). Items that are missing required properties are not eligible for rich results.
  * The more recommended properties that you provide, the higher quality the result is to users. For example: users prefer job postings with explicitly stated salaries than those without; users prefer recipes with actual user reviews and genuine star ratings (note that reviews or ratings not by actual users may result in [manual action](https://support.google.com/webmasters/answer/3498001)). Rich result ranking takes extra information into consideration.

### Location

  * Put the structured data on the page that it describes, unless specified otherwise by the documentation.
  * If you have duplicate pages for the same content, we recommend placing the same structured data on all page duplicates, not just on the canonical page.

### Specificity

  * Try to use the most specific applicable type and property names defined by schema.org for your markup.
  * Follow all additional guidelines given in the [ documentation for your specific rich result type](/search/docs/guides/search-gallery).

### Images

  * When specifying an image as a structured data property, make sure that the image is relevant to the page that it's on. For example, if you define the `image` property of `NewsArticle`, the image must be relevant to that news article.
  * All image URLs specified in structured data must be crawlable and indexable. Otherwise, Google Search can't find and display them on the search results page. To check if Google can access your URLs, use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289).

### Multiple items on a page

Multiple items on a page means that there is more than one kind of thing on a page. For example, a page could contain a recipe, a video that shows how to make that recipe, and breadcrumb information for how people can discover that recipe. All of this user-visible information can also be marked up with structured data, which makes it easier for search engines like Google Search to understand the information on a page. When you add more items that apply to a page, Google Search has a fuller picture of what the page is about and can display that page in different search features. 

Google Search understands multiple items on a page, whether you nest the items or specify each item individually: 

  * Nesting: When there is one main item, and additional items are grouped under the main item. This is particularly helpful when grouping related items (for example, a recipe with a video and reviews).
  * Individual items: When each item is a separate block on the same page. If there are items that are more helpful when they are linked together (for example, a recipe and a video), use `@id` in both the recipe and the video items to specify that the video is about the recipe on the page. If you didn't link the items together, Google Search may not know that it can show the video as a Recipe rich result.

These examples are trimmed for brevity, and they don't include all the required and recommended properties for the features. For a full example, refer to the [specific structured data type documentation](/search/docs/guides/search-gallery).

### Nesting

Here's an example of nested structured data, where `Recipe` is the main item, and `aggregateRating` and `video` are nested in the `Recipe`. 
    
    
    <html>
      <head>
        <title>How To Make Banana Bread</title>
        <script type="application/ld+json">
        {
          "@context": "https://schema.org/",
          "@type": "Recipe",
          "name": "Banana Bread Recipe",
          "description": "The best banana bread recipe you'll ever find! Learn how to use up all those extra bananas.",
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": 4.7,
            "ratingCount": 123
          },
          "video": {
            "@type": "VideoObject",
            "name": "How To Make Banana Bread",
            "description": "This is how you make banana bread, in 5 easy steps.",
            "contentUrl": "https://www.example.com/video123.mp4"
           }
        }
        </script>
      </head>
      <body>
      </body>
    </html>

### Individual items

Here's an example of individual items of structured data. There are two, distinct items: `Recipe` and `BreadcrumbList`. 
    
    
    <html>
      <head>
        <title>How To Make Banana Bread</title>
        <script type="application/ld+json">
        [{
          "@context": "https://schema.org/",
          "@type": "Recipe",
          "name": "Banana Bread Recipe",
          "description": "The best banana bread recipe you'll ever find! Learn how to use up all those extra bananas."
        },
        {
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [{
            "@type": "ListItem",
            "position": 1,
            "name": "Recipes",
            "item": "https://example.com/recipes"
          },{
            "@type": "ListItem",
            "position": 2,
            "name": "Bread recipes",
            "item": "https://example.com/recipes/bread-recipes"
          },{
            "@type": "ListItem",
            "position": 3,
            "name": "How To Make Banana Bread"
          }]
        }]
        </script>
      </head>
      <body>
      </body>
    </html>

####  Additional tips 

  * To make sure that Google Search understands what the main purpose of the page is, include the main type of structured data that reflects the main focus of the page. For example, if a page is mainly about a recipe, make sure to include [Recipe structured data](/search/docs/appearance/structured-data/recipe) in addition to [Video](/search/docs/appearance/structured-data/video) and [Review](/search/docs/appearance/structured-data/review-snippet) structured data. This is an opportunity for that page to be eligible for multiple search appearances (recipe rich results, video search, and review snippets). If the page only contained Video structured data, Google Search wouldn't know enough about the page to also display it as a recipe rich result.
  * To ensure that the page fully represents the content that's visible to users, make sure all structured data items are complete. For example, if you include multiple reviews, make sure that you include all of the reviews that are visible to people on the page. If a page didn't mark up all of the reviews on a page, this would be misleading for people who expect to see all of those reviews, based on the appearance of the page in Search results.

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-06 UTC.
