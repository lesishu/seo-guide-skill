# 修复 JavaScript SEO 问题

> 来源：Google Search Central (https://developers.google.com/search/docs/crawling-indexing-javascript-fix-search-javascript.txt)

---

# Fix Search-related JavaScript problems

This guide helps you identify and fix JavaScript issues that may be blocking your page, or specific content on JavaScript powered pages, from showing up in Google Search. While Google Search does run JavaScript, there are some differences and limitations that you need to account for when designing your pages and applications to accommodate how crawlers access and render your content. Our [guide on JavaScript SEO basics](/search/docs/guides/javascript-seo-basics) has more information on how you can optimize your JavaScript site for Google Search. 

Googlebot is designed to be a good citizen of the web. Crawling is its [main priority](/search/blog/2017/01/what-crawl-budget-means-for-googlebot), while making sure it doesn't degrade the experience of users visiting the site. Googlebot and its Web Rendering Service (WRS) component continuously analyze and identify resources that don't contribute to essential page content and may not fetch such resources. For example, reporting and error requests that don't contribute to essential page content, and other similar types of requests are unused or unnecessary to extract essential page content. Client-side analytics may not provide a full or accurate representation of Googlebot and WRS activity on your site. Use [the crawl stats report in Google Search Console](https://support.google.com/webmasters/answer/9679690) to monitor Googlebot and WRS activity and feedback on your site.

If you suspect that JavaScript issues might be blocking your page, or specific content on JavaScript powered pages, from showing up in Google Search, follow these steps. If you're not sure if JavaScript is the main cause, follow our [general debugging guide](/search/docs/guides/debug) to determine the specific issue. 

  1. To test how Google crawls and renders a URL, use the [Rich Results Test](https://search.google.com/test/rich-results) or the [URL Inspection Tool](https://support.google.com/webmasters/answer/9012289) in Search Console. You can see loaded resources, JavaScript console output and exceptions, rendered DOM, and more information. 

Optionally, we also recommend collecting and auditing JavaScript errors encountered by users, including Googlebot, on your site to identify potential issues that may affect how content is rendered. Here's an example that shows how to log JavaScript errors that are logged in the [global onerror handler](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onerror). Note that some types of JavaScript errors, such as a parse error, cannot be logged with this method. 
    
        window.addEventListener('error', function(e) {
        var errorText = [
            e.message,
            'URL: ' + e.filename,
            'Line: ' + e.lineno + ', Column: ' + e.colno,
            'Stack: ' + (e.error && e.error.stack || '(no stack trace)')
        ].join('\n');
    
        // Example: log errors as visual output into the host page.
        // Note: you probably don't want to show such errors to users, or
        //       have the errors get indexed by Googlebot; however, it may
        //       be a useful feature while actively debugging the page.
        var DOM_ID = 'rendering-debug-pre';
        if (!document.getElementById(DOM_ID)) {
            var log = document.createElement('pre');
            log.id = DOM_ID;
            log.style.whiteSpace = 'pre-wrap';
            log.textContent = errorText;
            if (!document.body) document.body = document.createElement('body');
            document.body.insertBefore(log, document.body.firstChild);
        } else {
            document.getElementById(DOM_ID).textContent += '\n\n' + errorText;
        }
    
        // Example: log the error to remote service.
        // Note: you can log errors to a remote service, to understand
        //       and monitor the types of errors encountered by regular users,
        //       Googlebot, and other crawlers.
        var client = new XMLHttpRequest();
        client.open('POST', 'https://example.com/logError');
        client.setRequestHeader('Content-Type', 'text/plain;charset=UTF-8');
        client.send(errorText);
    
    });

  2. Make sure to prevent [`soft 404` errors](/search/docs/crawling-indexing/troubleshoot-crawling-errors#soft-404-errors). In a single-page application (SPA), this can be especially difficult. To prevent error pages from being indexed, you can use one or both of the following strategies: 
     * Redirect to a URL where the server responds with a `404` status code. 
        
                fetch(`https://api.kitten.club/cats/${id}`)
         .then(res => res.json())
         .then((cat) => {
           if (!cat.exists) {
             // redirect to page that gives a 404
             window.location.href = '/not-found';
           }
         });

     * Add or change the robots `meta` tag to `noindex`. 
        
                fetch(`https://api.kitten.club/cats/${id}`)
         .then(res => res.json())
         .then((cat) => {
           if (!cat.exists) {
             const metaRobots = document.createElement('meta');
             metaRobots.name = 'robots';
             metaRobots.content = 'noindex';
             document.head.appendChild(metaRobots);
           }
         });

When a SPA is using client-side JavaScript to handle errors they often report a `200` HTTP status code instead of the [appropriate status code](/search/docs/crawling-indexing/javascript/javascript-seo-basics#use-meaningful-http-status-codes). This can lead to error pages being indexed and possibly shown in search results. 

  3. Expect Googlebot to decline [ user permission requests](https://w3c.github.io/permissions/#permission-registry).   
Features that require user permission don't make sense for Googlebot, or for all users. For example, if you make the `Camera API` required, Googlebot can't provide a camera to you. Instead, provide a way for users to access your content without being forced to allow camera access. 
  4. Don't use URL fragments to load different content.   
A SPA may use URL fragments (for example https://example.com/#/products) for loading different views. The [AJAX-crawling scheme has been deprecated](/search/blog/2015/10/deprecating-our-ajax-crawling-scheme) since 2015, so you can't rely on URL fragments to work with Googlebot. We recommend using the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History) to load different content based on the URL in a SPA. 
  5. Don't rely on data persistence to serve content.   
WRS loads each URL (refer to [How Google Search Works](/search/docs/fundamentals/how-search-works) for an overview of how Google discovers content), following server and client redirects, same as a regular browser. However, WRS does not retain state across page loads: 
     * Local Storage and Session Storage data are cleared across page loads.
     * HTTP Cookies are cleared across page loads. 
  6. Use content fingerprinting to avoid caching issues with Googlebot.   
Googlebot caches aggressively in order to reduce network requests and resource usage. WRS may ignore caching headers. This may lead WRS to use outdated JavaScript or CSS resources. Content fingerprinting avoids this problem by making a fingerprint of the content part of the filename, like `main.2bb85551.js`. The fingerprint depends on the content of the file, so updates generate a different filename every time. Check out the [web.dev guide on long-lived caching strategies](https://web.dev/articles/http-cache#versioned-urls) to learn more. 
  7. Ensure that your application uses [feature detection](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Feature_detection) for all critical APIs that it needs and provide a fallback behavior or polyfill where applicable.   
Some web features may not yet be adopted by all user agents and some may intentionally disable certain features. For example, if you use WebGL to render photo effects in the browser, feature detection shows that Googlebot doesn't support WebGL. To fix this, you could skip the photo effect or decide to use server-side rendering to prerender the photo effects, which makes your content accessible to everyone, including Googlebot. 
  8. Make sure your content works with HTTP connections.   
Googlebot uses HTTP requests to retrieve content from your server. It does not support other types of connections, such as `[WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)` or `[WebRTC](https://developer.mozilla.org/en-US/docs/Glossary/WebRTC)` connections. To avoid problems with such connections, make sure to provide an HTTP fallback to retrieve content and use robust error handling and feature detection. 
  9. Make sure your web components render as expected. Use the [Rich Results Test](https://search.google.com/test/rich-results) or the [URL Inspection Tool](https://support.google.com/webmasters/answer/9012289) to check if the rendered HTML has all content you expect.   
WRS flattens the [light DOM and shadow DOM](/web/fundamentals/web-components/shadowdom#lightdom). If the web components you use aren't using [`<slot>` mechanism](/web/fundamentals/web-components/shadowdom#slots) for light DOM content, consult the documentation of the web component for further information or use another web component instead. For more information, see [best practices for web components](/search/docs/guides/javascript-seo-basics#web-components). 
  10. If you're using a JavaScript-based paywall, consider the implementation.   
Some JavaScript paywall solutions include the full content in the server response, then use JavaScript to hide it until subscription status is confirmed. This isn't a reliable way to limit access to the content. Make sure your paywall only provides the full content once the subscription status is confirmed. 
  11. After you fix the items in this checklist, test your page with the [Rich Results Test](https://search.google.com/test/rich-results) or the [URL inspection tool](https://search.google.com/search-console) in Search Console again.   
If you fixed the issue, a green check mark appears and no errors display. If you still see errors, post in the [Search Central help community](https://support.google.com/webmasters/community).

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-18 UTC.
