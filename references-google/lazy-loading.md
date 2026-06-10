# 懒加载内容修复

> 来源：Google Search Central (https://developers.google.com/search/docs/crawling-indexing-javascript-lazy-loading.txt)

---

# Fix lazy-loaded content

Deferring loading of non-critical or non-visible content, also commonly known as "lazy-loading", is a common performance and UX best practice. For more information, see [web.dev's resources on lazy-loading images and video](https://web.dev/fast#lazy-load-images-and-video). However, if not implemented correctly, this technique can inadvertently hide content from Google. This document explains how to make sure Google can crawl and index lazy-loaded content. 

## Load content when it's visible in the viewport

To ensure that Google sees all content on your page, make sure that your lazy-loading implementation loads all relevant content whenever it is visible in the viewport. Here are a few methods to implement lazy-loading:

  **Browser built-in lazy-loading** for images and iframes
  **IntersectionObserver API** and [a polyfill](https://github.com/GoogleChromeLabs/intersection-observer)
  * A JavaScript library that supports loading data when it enters the viewport

The methods mentioned don't rely on user actions, such as scrolling or clicking, to load content, which is important as Google Search does not interact with your page.

Don't add lazy-loading to content that is likely to be immediately visible when a user opens a page. That might cause content to take longer to load and show up in the browser, which will be very noticeable to the user.

Make sure to test your implementation.

## Support paginated loading for infinite scroll

At a high level, infinite scroll is a technique that loads more content, more distinct pages, as the user scrolls down a long page. This could be one long article that's split into multiple chunks, or a collection of items that's similarly split into chunks. To implement infinite scroll in an indexable way, make sure your website supports paginated loading of these chunks by doing the following: 

  * Give each chunk its own persistent, unique URL.
  * Ensure that the content shown on each URL remains the same every time it's loaded in a browser. One way this can be done is to use absolute page numbers in the URL, for example by using `?page=12` as a query parameter.
  * Avoid using relative elements like `?date=yesterday` in these URLs. This allows search engines and users to consistently find the same content under a given URL, making it easier for search engines to properly index the content, and allowing users to share and reengage with that part of your content.
  * Link sequentially to the individual URLs so that search engines can discover the URLs in a paginated set. Find out more about [best practices when implementing pagination](/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading#best-practices-when-implementing-pagination).
  * When a new page chunk is loaded in response to the user scrolling, and it becomes the primary visible element for the user, update the displayed URL using the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API). This allows the user to refresh, share, and link to the current URL displayed in the browser.

## Test

After you set up your implementation, make sure it works correctly. You can use the [URL Inspection Tool](https://support.google.com/webmasters/answer/9012289) in Search Console to see if all content was loaded. Check the rendered HTML to make sure your content is in the rendered HTML by looking for it in URL Inspection Tool. If your image or video URLs appear in the `src` attribute on the `<img>` or `<video>` elements in the rendered HTML, your setup works correctly.

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
