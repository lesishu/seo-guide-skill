# FAQPage 结构化数据

> 来源：Google Search Central (https://developers.google.com/search/docs/appearance-structured-data-faqpage.txt)

---

# FAQ (`FAQPage`, `Question`, `Answer`) structured data

Does your site allow users to submit answers to a single question? Use [`QAPage`](/search/docs/appearance/structured-data/qapage) structured data instead.

If your government-focused or health-focused site has a list of questions and answers, you can use `FAQPage` structured data to help people find that information on Google. Properly marked up FAQ pages may be eligible to have a rich result on Search and an [Action on the Google Assistant](/assistant/content/overview), which can help your site reach the right users. 

## Feature availability

FAQ rich results are only available for well-known, authoritative websites that are government-focused or health-focused. The feature is available on desktop and mobile devices in all countries and languages where Google Search is available. 

##  How to add structured data 

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/search/docs/appearance/structured-data/intro-structured-data). 

Here's an overview of how to build, test, and release structured data.

  1. Add the required properties. Based on the format you're using, learn where to [insert structured data on the page](/search/docs/appearance/structured-data/intro-structured-data#format-placement).  Using a CMS? It may be easier to use a plugin that's integrated into your CMS.   
Using JavaScript? Learn how to [generate structured data with JavaScript](/search/docs/appearance/structured-data/generate-structured-data-with-javascript).
  2. Follow the guidelines.
  3. Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results). 
  4. Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/search/docs/crawling-indexing/ask-google-to-recrawl). Note: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.
  5. To keep Google informed of future changes, we recommend that you [submit a sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap). You can automate this with the [Search Console Sitemap API](/webmaster-tools/v1/sitemaps).

## Examples

JSON-LD

Here's an example of `FAQPage` in JSON-LD:

<html> <head> <title>Finding an apprenticeship - Frequently Asked Questions(FAQ)</title> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{ "@type": "Question", "name": "How to find an apprenticeship?", "acceptedAnswer": { "@type": "Answer", "text": "<p>We provide an official service to search through available apprenticeships. To get started, create an account here, specify the desired region, and your preferences. You will be able to search through all officially registered open apprenticeships.</p>" } }, { "@type": "Question", "name": "Whom to contact?", "acceptedAnswer": { "@type": "Answer", "text": "You can contact the apprenticeship office through our official phone hotline above, or with the web-form below. We generally respond to written requests within 7-10 days." } }] } </script> </head> <body> </body> </html>   

    
    
    <html>
      <head>
        <title>Finding an apprenticeship - Frequently Asked Questions(FAQ)</title>
        <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [{
            "@type": "Question",
            "name": "How to find an apprenticeship?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "<p>We provide an official service to search through available apprenticeships. To get started, create an account here, specify the desired region, and your preferences. You will be able to search through all officially registered open apprenticeships.</p>"
            }
          }, {
            "@type": "Question",
            "name": "Whom to contact?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "You can contact the apprenticeship office through our official phone hotline above, or with the web-form below. We generally respond to written requests within 7-10 days."
            }
          }]
        }
        </script>
      </head>
      <body>
      </body>
    </html>

Microdata

Here's an example of `FAQPage` in Microdata:

<html itemscope itemtype="https://schema.org/FAQPage"> <head></head> <body> <h1> Frequently Asked Questions(FAQ) </h1> <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"> <h2 itemprop="name">How to find an apprenticeship?</h2> <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"> <div itemprop="text"> We provide an official service to search through available apprenticeships. To get started, create an account here, specify the desired region, and your preferences. You will be able to search through all officially registered open apprenticeships. </div> </div> </div> <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"> <h2 itemprop="name">Whom to contact?</h2> <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"> <div itemprop="text"> You can contact the apprenticeship office through our official phone hotline above, or with the web-form below. We generally respond to written requests within 7-10 days. </div> </div> </div> </body> </html>   

    
    
    <html itemscope itemtype="https://schema.org/FAQPage">
    <head></head>
    <body>
      <h1>
        Frequently Asked Questions(FAQ)
      </h1>
      <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <h2 itemprop="name">How to find an apprenticeship?</h2>
        <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <div itemprop="text">
            We provide an official service to search through available apprenticeships. To get started, create an account here, specify the desired region, and your preferences. You will be able to search through all officially registered open apprenticeships.
          </div>
        </div>
      </div>
      <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <h2 itemprop="name">Whom to contact?</h2>
        <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <div itemprop="text">
            You can contact the apprenticeship office through our official phone hotline above, or with the web-form below. We generally respond to written requests within 7-10 days.
          </div>
        </div>
      </div>
    </body>
    </html>

## Guidelines

For your FAQ page to be eligible for FAQ rich results, you must follow these guidelines:

  **General structured data guidelines**
  **Search Essentials**
  * Content guidelines

### Content guidelines

  * Your site must be a health or government site. It must also be well-known and authoritative.
  * Only use `FAQPage` if your page contains FAQs where there's a single answer to each question. If your page has a single question and users can submit alternative answers, use [`QAPage`](/search/docs/appearance/structured-data/qapage) instead. Here are some examples: 

Valid use cases:

    * An FAQ page written by the health site itself, with no way for users to submit alternative answers
    * A government agency's support page that lists FAQs, with no way for users to submit alternative answers

Invalid use cases:

    * A forum page where users can submit answers to a single question
    * A product support page where users can submit answers to a single question
    * A product page where users can submit multiple questions and answers on a single page
  * Don't use `FAQPage` for advertising purposes.
  * Make sure each `Question` includes the entire text of the question and make sure each `Answer` includes the entire text of the answer. The entire question text and answer text may be displayed.
  * Question and answer content may not be displayed as a rich result if it contains any of the following types of content: obscene, profane, sexually explicit, graphically violent, promotion of dangerous or illegal activities, or hateful or harassing language.
  * All `FAQ` content must be visible to the user on the source page. Here are some examples: 

Valid use cases:

    * Both the question and answer are visible on the page.
    * The question is visible on the page, and the answer is hidden behind an expandable section. The user is able to access the answer by clicking the expandable section.

Invalid use cases: The user can't find the FAQ content on the page at all.

  * If you have FAQ content that is repetitive on your site (meaning, the same question and answer appear on multiple pages on your site), mark up only one instance of that FAQ for your entire site.

## Structured data type definitions

You must include the required properties for your content to be eligible for display as a rich result. You can also include the recommended properties to add more information to your structured data, which could provide a better user experience.

### `FAQPage`

The full definition of [FAQPage](https://schema.org/FAQPage) is provided on schema.org.

The `FAQPage` type indicates that the page is an FAQ with answered questions. There must be one `FAQPage` type definition per page. 

The Google-supported properties are the following:

Required properties  
---  
`mainEntity` | `[Question](https://schema.org/Question)` An array of `Question` elements which contain the list of answered questions that this `FAQPage` is about. You must specify at least one valid `Question` item. A `Question` item includes both the question and answer.   
  
### `Question`

The full definition of `[Question](https://schema.org/Question)` is provided on schema.org.

The `Question` type defines a single answered question within the FAQ. Every `Question` instance must be contained within the `mainEntity` property array of the `schema.org/FAQPage`. 

The Google-supported properties are the following:

Required properties  
---  
`acceptedAnswer` | `[Answer](https://schema.org/Answer)` The answer to the question. There must be one answer per question.  
`name` | `[Text](https://schema.org/Text)` The full text of the question. For example, "How long does it take to process a refund?".  
  
### `Answer`

The full definition of `[Answer](https://schema.org/Answer)` is provided on schema.org.

The `Answer` type defines the `acceptedAnswer` to each of the `Question` on this page.

The Google-supported properties are the following:

Required properties  
---  
`text` | `[Text](https://schema.org/Text)` The full answer to the question. The answer may contain HTML content such as links and lists. Google Search displays the following HTML tags: `<h1>` through `<h6>`, `<br>`, `<ol>`, `<ul>`, `<li>`, `<a>`, `<p>`, `<div>`, `<b>`, `<strong>`, `<i>`, and `<em>`. All other tags are ignored.  
  
## Monitor rich results with Search Console

Search Console is a tool that helps you monitor how your pages perform in Google Search. You don't have to sign up for Search Console to be included in Google Search results, but it can help you understand and improve how Google sees your site. We recommend checking Search Console in the following cases: 

  1. After deploying structured data for the first time
  2. After releasing new templates or updating your code
  3. Analyzing traffic periodically

###  After deploying structured data for the first time 

After Google has indexed your pages, look for issues using the relevant [Rich result status report](https://support.google.com/webmasters/answer/7552505). Ideally, there will be an increase of valid items, and no increase in invalid items. If you find issues in your structured data:

  1. Fix the invalid items.
  2. [Inspect a live URL](https://support.google.com/webmasters/answer/9012289#test_live_page) to check if the issue persists.
  3. [Request validation](https://support.google.com/webmasters/answer/13300208) using the status report.

###  After releasing new templates or updating your code 

When you make significant changes to your website, monitor for increases in structured data invalid items. 

  * If you see an increase in invalid items, perhaps you rolled out a new template that doesn't work, or your site interacts with the existing template in a new and bad way.
  * If you see a decrease in valid items (not matched by an increase in invalid items), perhaps you are no longer embedding structured data in your pages. Use the [ URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to learn what is causing the issue.

###  Analyzing traffic periodically 

Analyze your Google Search traffic using the [Performance Report](https://support.google.com/webmasters/answer/7576553). The data will show you how often your page appears as a rich result in Search, how often users click on it and what is the average position you appear on search results. You can also automatically pull these results with the [Search Console API](/webmaster-tools/search-console-api-original/v3/how-tos/search_analytics). 

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

Last updated 2026-04-08 UTC.
