# 结构化数据入门

> 来源：Google Search Central (https://developers.google.com/search/docs/appearance-structured-data-intro-structured-data.txt)

---

# Introduction to structured data markup in Google Search

Google Search works hard to understand the content of a page. You can help us by providing explicit clues about the meaning of a page to Google by including structured data on the page. Structured data is a standardized format for providing information about a page and classifying the page content; for example, on a recipe page, what are the ingredients, the cooking time and temperature, the calories, and so on.

## Why add structured data to a page?

Adding structured data can enable search results that are more engaging to users and might encourage them to interact more with your website, which are called rich results. Here are some case studies of websites that have implemented structured data for their site:

  * Rotten Tomatoes added structured data to 100,000 unique pages and measured a 25% higher click-through rate for pages enhanced with structured data, compared to pages without structured data.
  * The Food Network has converted 80% of their pages to enable search features, and has seen a 35% increase in visits.
  * Rakuten has found that users spend 1.5x more time on pages that implemented structured data than on non-structured data pages, and have a 3.6x higher interaction rate on AMP pages with search features vs non-feature AMP pages.
  * Nestlé has measured pages that show as rich results in search have an 82% higher click through rate than non-rich result pages.

Read more [case studies from sites that have implemented structured data](/search/case-studies). 

## How structured data works in Google Search

Google uses structured data that it finds on the web to understand the content of the page, as well as to gather information about the web and the world in general, such as information about the people, books, or companies that are included in the markup. For example, when a recipe page has [JSON-LD](https://json-ld.org) structured data (describing the title of the recipe, the author of the recipe, and other details), Google Search can use that information to display a rich result for the recipe: 

Because the structured data labels each individual element of the recipe, users can search for your recipe by ingredient, calorie count, cook time, and so on.

If you use a CMS, such as Wix, WordPress, or Shopify, you might not be able to edit your HTML directly. Instead, your CMS may have a search engine settings page, or you may be able to install a plugin that allows you to specify structured data. Search for instructions about adding structured data to your CMS (for example, search for "wix structured data" or "wordpress structured data plugin").

Structured data is coded using in-page markup on the page that the information applies to. The structured data on the page describes the content of that page. Don't create blank or empty pages just to hold structured data, and don't add structured data about information that is not visible to the user, even if the information is accurate. For more technical and quality guidelines, see the [Structured data general guidelines](/search/docs/guides/sd-policies). 

The [Rich Results Test](https://search.google.com/test/rich-results) is an easy and useful tool for validating your structured data, and in some cases, previewing a feature in Google Search. Try it out: 

<html> <head> <title>Non-Alcoholic Piña Colada</title> <script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Recipe", "name": "Non-Alcoholic Piña Colada", "image": [ "https://example.com/photos/1x1/photo.jpg", "https://example.com/photos/4x3/photo.jpg", "https://example.com/photos/16x9/photo.jpg" ], "author": { "@type": "Person", "name": "Mary Stone" }, "datePublished": "2024-03-10", "description": "This non-alcoholic pina colada is everyone's favorite!", "recipeCuisine": "American", "prepTime": "PT1M", "cookTime": "PT2M", "totalTime": "PT3M", "keywords": "non-alcoholic", "recipeYield": "4 servings", "recipeCategory": "Drink", "nutrition": { "@type": "NutritionInformation", "calories": "120 calories" }, "aggregateRating": { "@type": "AggregateRating", "ratingValue": 5, "ratingCount": 18 }, "recipeIngredient": [ "400ml of pineapple juice", "100ml cream of coconut", "ice" ], "recipeInstructions": [ { "@type": "HowToStep", "name": "Blend", "text": "Blend 400ml of pineapple juice and 100ml cream of coconut until smooth.", "url": "https://example.com/non-alcoholic-pina-colada#step1", "image": "https://example.com/photos/non-alcoholic-pina-colada/step1.jpg" }, { "@type": "HowToStep", "name": "Fill", "text": "Fill a glass with ice.", "url": "https://example.com/non-alcoholic-pina-colada#step2", "image": "https://example.com/photos/non-alcoholic-pina-colada/step2.jpg" }, { "@type": "HowToStep", "name": "Pour", "text": "Pour the pineapple juice and coconut mixture over ice.", "url": "https://example.com/non-alcoholic-pina-colada#step3", "image": "https://example.com/photos/non-alcoholic-pina-colada/step3.jpg" } ], "video": { "@type": "VideoObject", "name": "How to Make a Non-Alcoholic Piña Colada", "description": "This is how you make a non-alcoholic piña colada.", "thumbnailUrl": [ "https://example.com/photos/1x1/photo.jpg", "https://example.com/photos/4x3/photo.jpg", "https://example.com/photos/16x9/photo.jpg" ], "contentUrl": "https://www.example.com/video123.mp4", "embedUrl": "https://www.example.com/videoplayer?video=123", "uploadDate": "2024-02-05T08:00:00+08:00", "duration": "PT1M33S", "interactionStatistic": { "@type": "InteractionCounter", "interactionType": { "@type": "WatchAction" }, "userInteractionCount": 2347 }, "expires": "2024-02-05T08:00:00+08:00" } } </script> </head> <body> </body> </html>

## Structured data vocabulary and format

This documentation describes which properties are required, recommended, or optional for structured data with special meaning to Google Search. Most Search structured data uses [schema.org](https://schema.org/) vocabulary, but you should rely on the Google Search Central documentation as definitive for Google Search behavior, rather than the schema.org documentation. There are more attributes and objects on schema.org that aren't required by Google Search; they may be useful for other search engines, services, tools, and platforms.

Data-vocabulary.org markup is no longer eligible for Google rich result features. Learn more about [sunsetting support for data-vocabulary](/search/blog/2020/01/data-vocabulary).

Be sure to check your structured data using the [Rich Results Test](https://search.google.com/test/rich-results) during development, and the [Rich result status reports](https://support.google.com/webmasters/answer/7552505) after deployment, to monitor the validity of your pages, which might break after deployment due to templating or serving issues.

You must include all the required properties for an object to be eligible for appearance in Google Search with enhanced display. In general, defining more recommended features can make it more likely that your information can appear in Search results with enhanced display. However, it is more important to supply fewer but complete and accurate recommended properties rather than trying to provide every possible recommended property with less complete, badly-formed, or inaccurate data.

In addition to the properties and objects documented here, Google can make general use of the [`sameAs`](https://schema.org/sameAs) property and other [schema.org](https://schema.org/) structured data. Some of these elements may be used to enable future Search features, if they are deemed useful.

###  Supported formats 

Google Search supports structured data in the following formats, unless documented otherwise. In general, we recommend using a format that's easiest for you to implement and maintain (in most cases, that's JSON-LD); all 3 formats are equally fine for Google, as long as the markup is valid and properly implemented per the feature's documentation. 

Formats  
---  
[JSON-LD](https://json-ld.org/)* (Recommended) | A JavaScript notation embedded in a `<script>` tag in the `<head>` and `<body>` elements of an HTML page. The markup is not interleaved with the user-visible text, which makes nested data items easier to express, such as the `Country` of a `PostalAddress` of a `MusicVenue` of an `Event`. Also, Google can read JSON-LD data when it is [dynamically injected into the page's contents](/search/docs/guides/generate-structured-data-with-javascript), such as by JavaScript code or embedded widgets in your content management system.  
[Microdata](https://html.spec.whatwg.org/multipage/microdata.html#microdata) | An open-community HTML specification used to nest structured data within HTML content. Like RDFa, it uses HTML tag attributes to name the properties you want to expose as structured data. It is typically used in the `<body>` element, but can be used in the `<head>` element.  
[RDFa](https://rdfa.info/) | An HTML5 extension that supports linked data by introducing [HTML tag attributes](https://www.w3.org/TR/rdfa-lite/#the-attributes) that correspond to the user-visible content that you want to describe for search engines. RDFa is commonly used in both the `<head>` and `<body>` sections of the HTML page.  
In general, Google recommends using JSON-LD for structured data if your site's setup allows it, as it's the easiest solution for website owners to implement and maintain at scale (in other words, less prone to user errors). 

## Structured data guidelines

Be sure to follow the [general structured data guidelines](/search/docs/appearance/structured-data/sd-policies), as well as any guidelines specific to your structured data type; otherwise your structured data might be ineligible for rich result display in Google Search.

## Get started with structured data

If you're new to structured data, check out [schema.org beginner's guide to structured data](https://schema.org/docs/gs.html). While the guide focuses on Microdata, the basic ideas are relevant for JSON-LD and RDFa.

Once you're comfortable with the basics of structured data, explore the [list of structured data features in Google Search](/search/docs/appearance/structured-data/search-gallery) and pick a feature to implement. Each guide goes into detail on how to implement the structured data in a way that makes your site eligible for a rich result appearance on Google Search.

[Choose a feature](/search/docs/appearance/structured-data/search-gallery)

## Measuring the effect of structured data

You probably want to compare performance of your pages with structured data with those pages that don't have structured data, in order to decide if it's worth your effort. The best way to do that is to run a [before and after test on a few pages on your site](/search/docs/crawling-indexing/website-testing). This can be a little tricky, since page views can vary for a single page for various reasons.

  1. Take some pages on your site that are not using any structured data, and have several months of data in Search Console. Be sure to choose pages that won't be affected by the time of year or timeliness of the page content; use pages that won't change much, but are still popular enough to be read often enough to generate meaningful data.
  2. Add structured data or other features to your pages. Confirm that your markup is valid, and that Google has found your structured data using the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) on your page.
  3. Record the performance for a few months in the [Performance report](https://support.google.com/webmasters/answer/7576553#by_search_appearance), and filter by URL to compare performance of your page.

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
