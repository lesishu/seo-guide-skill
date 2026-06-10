# Google 排名系统完全指南

> 来源：Google Search Central

---

# A guide to Google Search ranking systems

Google uses automated ranking systems that [look at many factors and signals](https://www.google.com/search/howsearchworks/how-search-works/ranking-results/) about hundreds of billions of web pages and other content in our Search index to present the most relevant, useful results, all in a fraction of a second. This page is a guide to understanding some of our more notable ranking systems. It covers some systems that are part of our core ranking systems, which are the underlying technologies that produce search results in response to queries. It also covers some systems involved with specific ranking needs. 

Our ranking systems are designed to work on the page level, using a variety of signals and systems to understand how to rank individual pages. Site-wide signals and classifiers are also used and contribute to our understanding of pages. Having some good site-wide signals does not mean that all content from a site will always rank highly, just as having some poor site-wide signals does not mean all the content from a site will rank poorly. 

We regularly improve our ranking systems through [rigorous testing and evaluation](https://www.google.com/search/howsearchworks/how-search-works/rigorous-testing/) and provide notice of [updates to our ranking systems](https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history) when those might be useful to content creators and others. 

You can also visit our [How Search Works site](https://www.google.com/search/howsearchworks/) to understand how our [ranking systems](https://www.google.com/search/howsearchworks/how-search-works/ranking-results/), combined with other processes, work together so that Google Search delivers on our mission to organize the world's information and make it universally accessible and useful. 

## BERT

Bidirectional Encoder Representations from Transformers ([BERT](https://blog.google/products/search/how-ai-powers-great-search-results/)) is an AI system Google uses that allows us to understand how combinations of words express different meanings and intent. 

## Crisis information systems

Google has developed systems to provide helpful and timely information during times of crisis, whether those involve personal crisis situations, natural disasters, or other wide-spread crisis situations: 

  * Personal crisis: Our systems work to understand when people are seeking information about personal crisis situations to display hotlines and content from trusted organizations for certain queries related to suicide, sexual assault, poison ingestion, gender-based violence, or drug addiction. Learn more about how [personal crisis information is displayed in Google Search](https://support.google.com/websearch/answer/9988513).
  * SOS Alerts: During times of natural disasters or wide-spread crisis situations, our SOS Alerts system works to show updates from local, national, or international authorities. These updates may include emergency phone numbers and websites, maps, translations of useful phrases, donation opportunities, and more. Learn more about [how SOS Alerts work](https://support.google.com/sosalerts/) and how they're part of Google's [crisis alerts](https://crisisresponse.google/forecasting-and-alerts/) that help in times of floods, wildfires, earthquakes, hurricanes, and other disasters.

## Deduplication systems

Searches on Google may find thousands or even millions of matching web pages. Some of these may be very similar to each other. In such cases, our systems show only the most relevant results to avoid unhelpful duplication. Learn more about [how deduplication works and how to see omitted results](https://support.google.com/websearch/answer/9603785) if desired, when deduplication happens. 

Deduplication also happens with [featured snippets](https://support.google.com/websearch/answer/9351707). If a web page listing is elevated to become a featured snippet, we don't repeat the listing later on the first page of results. This declutters the results and helps people locate relevant information more easily. 

## Exact match domain system

Our ranking systems consider the words in domain names as one of many factors to determine if content is relevant to a search. However, our exact match domain system works to ensure we don't give too much credit for content hosted under domains designed to exactly match particular queries. For example, someone might create a domain name containing the words "best-places-to-eat-lunch" in hopes all those words in the domain name would propel content high in the rankings. Our system adjusts for this. 

## Freshness systems

We have various "query deserves freshness" systems designed to show fresher content for queries where it would be expected. For example, if someone is searching about a movie that's just been released, they probably want recent reviews rather than older articles from when production began. For another example, ordinarily a search for "earthquake" might bring back material about preparation and resources. However, if an earthquake happened recently, then news articles and fresher content might appear. 

## Link analysis systems and PageRank

We have various systems that understand how pages link to each other as a way to determine what pages are about and which might be most helpful in response to a query. Among these is PageRank, one of our core ranking systems used when Google first launched. Those curious can learn more by reading the original [PageRank research paper](http://infolab.stanford.edu/~backrub/google.html) and [patent](https://patents.google.com/patent/US6285999). How PageRank works has evolved a lot since then, and it continues to be part of our core ranking systems. 

## Local news systems

We have systems that work to identify and surface local sources of news whenever relevant, [such as through](https://blog.google/products/news/local-news-update-census-mapper/) our "Top stories" and "Local news" features. 

## MUM

Multitask Unified Model ([MUM](https://blog.google/products/search/how-ai-powers-great-search-results/)) is an AI system capable of both understanding and generating language. It's not currently used for general ranking in Search but rather for some specific applications such as to [improve searches for COVID-19 vaccine information](https://blog.google/products/search/how-mum-improved-google-searches-vaccine-information/) and to [improve featured snippet callouts we display](https://blog.google/products/search/information-literacy/). 

## Neural matching

[Neural matching](https://blog.google/products/search/how-ai-powers-great-search-results/) is an AI system that Google uses to understand representations of concepts in queries and pages and match them to one another. 

## Original content systems

We have systems to help ensure we are showing original content prominently in search results, [including original reporting](https://blog.google/products/search/original-reporting/), ahead of those who merely cite it. This includes support of a special [canonical markup](/search/docs/crawling-indexing/consolidate-duplicate-urls) creators can use to help us better understand what is the primary page if a page has been duplicated in several places. 

## Removal-based demotion systems

Google has policies that allow the removal of certain types of content. If we process a significant volume of such removals involving a particular site, we use that as a signal to improve our results. In particular: 

  * Legal removals: When we receive a significant volume of [valid copyright removal requests](https://support.google.com/transparencyreport/answer/7347743) involving a given site, [we are able to use that](https://search.googleblog.com/2012/08/an-update-to-our-search-algorithms.html) to demote other content from the site in our results. This way, if there is other infringing content, people are less likely to encounter it versus the original content. We apply similar demotion signals to complaints involving defamation, counterfeit goods, and court-ordered removals. In the case of child sexual abuse material (CSAM), we always remove such content when it is identified and we demote all content from sites with a significant proportion of CSAM content. 
  * Personal information removals: If we process a significant volume of personal information removals involving a site with [exploitative removal practices](https://support.google.com/websearch/answer/9172218), we demote other content from the site in our results. [We also look to see](https://blog.google/products/search/improving-search-better-protect-people-harassment/) if the same pattern of behavior is happening with other sites and, if so, apply demotions to content on those sites. We may apply similar demotion practices for sites that receive a significant volume of removals of content involving [doxxing content](https://support.google.com/websearch/answer/9673730), [explicit personal imagery created or shared without consent](https://support.google.com/websearch/answer/6302812), or [explicit non-consensual fake content](https://support.google.com/websearch/answer/9116649). 

## Passage ranking system

[Passage ranking](https://www.blog.google/products/search/search-on/) is an AI system we use to identify individual sections or "passages" of a web page to better understand how relevant a page is to a search. 

## RankBrain

[RankBrain](https://blog.google/products/search/how-ai-powers-great-search-results/) is an AI system that helps us understand how words are related to concepts. It means we can better return relevant content even if it doesn't contain all the exact words used in a search, by understanding the content is related to other words and concepts. 

## Reliable information systems

Multiple systems work in various ways to show the most reliable information possible, such as to [help surface more authoritative pages and demote low-quality content](https://blog.google/products/search/our-latest-quality-improvements-search/) and [to elevate quality journalism](https://blog.google/outreach-initiatives/google-news-initiative/elevating-quality-journalism/). In cases where reliable information might be lacking, our systems automatically display [content advisories](https://blog.google/products/search/information-literacy/) about rapidly-changing topics or when our systems don't have high confidence in the overall quality of the results available for the search. These provide tips on how to search in ways that might lead to more helpful results. Learn more about our [approach to delivering high-quality information in Search](https://blog.google/products/search/how-google-delivers-reliable-information-search/). 

## Reviews system

The [reviews system](/search/updates/reviews-update) aims to better reward high quality reviews, content that provides insightful analysis and original research, and is written by experts or enthusiasts who know the topic well. 

## Site diversity system

Our site diversity system works so that we generally won't show more than two web page listings from the same site in our top results, so that no single site tends to dominate all the top results. However, we may still show more than two listings in cases where our systems determine it's especially relevant to do so for a particular search. Site diversity generally treats subdomains as part of a root domain. IE: listings from a subdomain (subdomain.example.com) and the root domain (example.com) will all be considered from the same single site. However, sometimes subdomains are treated as separate sites for diversity purposes when deemed relevant to do so. 

## Spam detection systems

No one wants their email inbox filled with spam, which is why spam filters are so helpful. Search faces a similar challenge, because the internet includes huge amounts of spam that, if not dealt with, would prevent us from showing the most helpful and relevant results. We employ a range of [spam detection systems](https://www.google.com/search/howsearchworks/how-search-works/detecting-spam/), including [SpamBrain](/search/blog/2022/04/webspam-report-2021), to deal with content and behaviors that violate our [spam policies](/search/docs/essentials/spam-policies). These systems are constantly [updated](/search/updates/spam-updates) to keep up with the latest ways that the spam threat evolves. 

## Retired systems

The following systems are noted for historical purposes. They've either been incorporated into successor systems or made part of our core ranking systems. 

### Helpful content system

[Announced in 2022](/search/blog/2022/08/helpful-content-update) as the "Helpful Content Update", this was a system designed to better ensure people see original, helpful content written by people, for people, in search results, rather than content made primarily to gain search engine traffic. In March 2024, it evolved and [became part of](/search/blog/2024/03/core-update-spam-policies) our core ranking systems, as our systems use a variety of signals and systems to present helpful results to users. 

### Hummingbird

This was a major improvement to our overall ranking systems made in August 2013. Our ranking systems have continued to evolve since then, just as they had been evolving before. 

### Panda system

This was a system designed to better ensure high-quality and original content was appearing in our search results. [Announced in 2011](https://googleblog.blogspot.com/2011/02/finding-more-high-quality-sites-in.html) and given the nickname of the "Panda," it evolved and became part of our core ranking systems in 2015. 

### Penguin system

This was a system designed to combat link spam. [Announced in 2012](/search/blog/2012/04/another-step-to-reward-high-quality) and given the nickname of the "Penguin Update", it was [integrated](/search/blog/2016/09/penguin-is-now-part-of-our-core) into our core ranking systems in 2016.

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
