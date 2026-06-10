# 避免侵入式插页广告

> 来源：Google Search Central (https://developers.google.com/search/docs/appearance-avoid-intrusive-interstitials.txt)

---

# Avoid intrusive interstitials and dialogs

Intrusive [interstitials](https://en.wikipedia.org/wiki/Interstitial_webpage) and dialogs are page elements that obstruct users' view of the content, usually for promotional purposes. Interstitials are overlays on the whole page and dialogs are overlays only on a part of the page, sometimes also obfuscating the underlying content. 

Websites often need to show dialogs for various reasons; however, interrupting users with intrusive interstitials may frustrate them and erode their trust in your website. 

Intrusive dialogs and interstitials make it hard for Google and other search engines to understand your content, which may lead to poor search performance. Equally, if users find your site hard to use, they are unlikely to want to visit those websites again, including through search engines. 

## Create unintrusive dialogs

Creating unintrusive dialogs means that users can access your content without being interrupted by a dialog. This applies to all kinds of promotional dialogs, including app install prompts. Following these best practices will help your users have a good experience on your site, in addition to helping Google Search understand the content and structure of your site. 

### Use banners instead of interstitials

Instead of full page interstitials, use banners that take up only a small fraction of the screen to grab your users' attention. Banners ensure that users and search engines can get to the content as soon as they land on the page. 

These can be implemented in various ways. For example, for app install banners, you can use a browser-supported banner, such as [Smart App Banners](https://developer.apple.com/library/ios/#documentation/AppleApplications/Reference/SafariWebContent/PromotingAppswithAppBanners/PromotingAppswithAppBanners.html) for Safari or [in-app install experience](/web/fundamentals/app-install-banners/native) for Chrome. Another option is to create an HTML banner, similar to a typical small advertisement, that links to the correct app store for download. You can reuse these small containers for other kinds of notifications, such as newsletter sign-up prompts. 

### Use common libraries

Many CMSes have plugins that create standard dialogs and interstitials for the most common use cases, such as newsletter sign-up prompts. For example, if you are using WordPress, search for "newsletter signup wordpress". Using such plugins can be helpful for Google, other search engines, and the internet in general, as the plugin developers can deploy improvements at scale. 

### Avoid common mistakes

Unless they're legally mandatory, avoid the following common mistakes when designing a dialog or interstitial to help Google Search crawl and understand your content: 

  * Don't obscure the entire page with interstitials.
  * Don't redirect the user to a separate page for their consent or input.

## Mandatory interstitials

Certain sites are required to show an interstitial due to the kind of content they are publishing. For example, a casino site may need to show an age gate, which is a type of interstitial where the user must provide their age before accessing the content. 

Mandatory interstitials are exempted from the guidelines discussed in this document; however, if possible, we recommend that sites follow these best practices: 

  * Ensure that the content is overlaid with the interstitial. This will ensure that Google can still at least index some of the content and potentially show it in search results. 
  * Don't redirect the incoming HTTP requests to a different page for collecting consent or providing data. Redirecting all URLs to a single page will remove all but that one page from search results, as Googlebot can only fetch that page. 

For content behind a mandatory age gate for adult users, we recommend allowing Googlebot to crawl your content without triggering the age gate. You can do this by [verifying Googlebot requests](/search/docs/crawling-indexing/verifying-googlebot) and serving the content without age gate.

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
