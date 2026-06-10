# Web Stories SEO 最佳实践

> 来源：Google Search Central

---

# Best practices for creating Web Stories

To keep your readers engaged, follow our best practices for creating [Web Stories](/search/docs/appearance/enable-web-stories). We recommend focusing on the critical tasks first. If you have more time, follow the recommended best practices too. 

##  Storytelling 

Critical storytelling best practices |  Video first  |  Video is more engaging than text or images. Use as much video as possible, and supplement with images and text.   
---|---  
  
### More storytelling best practices

Recommended storytelling best practices |  Bring your perspective  |  Go beyond the facts. Share your opinions. Be the protagonist of your own story. Make it relatable.   
---|---  
Have a narrative arc  |  Create suspense in your story from one page to another. Bring the user along in the journey by providing context and narrative. Deliver payoff for sticking with you to the end.   
  
##  Design 

Critical design best practices |  Reduce your character count  |  Avoid including multiple pages with walls of text. Consider reducing text to approximately 280 characters per page (the length of a tweet).   
---|---  
Don't block text  |  Make sure text is not blocked by other content on the page. Avoid burned in text; by not using burned in text, you prevent text from being blocked when it gets resized to fit various device sizes.   
Keep text within bounds  |  Ensure that all text in your Web Story is visible to the reader. Avoid burned in text; by not using burned in text, you prevent text from overflowing when it gets resized to fit various device sizes.   
Use animations mindfully  |  Bring your stories to life with animations. Avoid distracting or repetitive animations which can cause fatigue.   
  
### More design best practices

Recommended design best practices |  Use Web Stories-specific call to action  |  When re-creating stories that were originally created for a social platform like Instagram, Snapchat or YouTube, be sure to remove any reader call-to-action specific to a certain platform. Make sure that users are able to follow any actions suggested in your Web Story.   
---|---  
Use full bleed videos and images  |  Include full bleed assets in your stories to create a more immersive experience for readers.   
Avoid low resolution or distorted images and videos  |  Use high-quality images, and take care when resizing images to portrait.   
Add a logo to your cover page  |  Include a high-resolution logo that represents your brand.   
Shorten video length  |  We recommend videos that are less than 15 seconds per page, or 60 seconds maximum.   
Include audio  |  Use high-quality audio clips that are at least 5 seconds long with balanced volume, and ensure speech is audible.   
Consider auto advance for video-only stories  |  Auto-advanced experience for video-based Web Stories could work well for a laid back experience.   
  
##  SEO 

Note: The same [SEO best practices](/search/docs/fundamentals/seo-starter-guide) for web pages also apply to [Web Stories](/search/docs/appearance/enable-web-stories). A Web Story is still a web page. Critical SEO best practices |  Provide high-quality content  |  Like any web page, providing high-quality content that is useful and interesting to your readers the most important thing you can do. Include a complete narrative and follow the storytelling best practices to keep your readers engaged.   
---|---  
Keep the title short  |  Keep titles shorter than 90 characters. We recommend using a descriptive title that is shorter than 70 characters.   
Make sure Google Search can find your story  |  Don't include a `noindex` attribute in your story; this attribute blocks Google from indexing the page and prevents it from appearing on Google. Additionally, add your Web Stories to your sitemap. You can check to see if Google can find your Web Stories with the [Index Coverage Report](https://support.google.com/webmasters/answer/7440203) and [Sitemaps Report](https://support.google.com/webmasters/answer/7451001) in Search Console.   
Make the story self-canonical  |  All Web Stories must be canonical. Make sure that each Web Story has a [`link rel="canonical"`](https://amp.dev/documentation/guides-and-tutorials/optimize-and-measure/discovery/) to itself. For example: `<link rel="canonical" href="https://www.example.com/url/to/webstory.html">` Note: If there are multiple versions of the same story in different languages, make sure to [tell Google about localized versions](/search/docs/specialty/international/localized-versions).   
Attach metadata  |  Make sure that your Web Stories follow the [AMP story metadata guidelines](https://amp.dev/documentation/components/amp-story/#metadata-guidelines). Include markup that you would normally include on a web page, such as:

  **`title`** and [`description`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta) `meta` tags
  **Structured data**
  **OGP**
  **Twitter card**

  
  
### More SEO best practices

Recommended SEO best practices |  Include structured data  |  We recommend [including structured data](/search/docs/appearance/structured-data/article#amp-sd) in your Web Story to help Google Search understand the structure and content of your Web Story.   
---|---  
Include alt text on images  |  We recommend including alt text on your images to improve your story's discoverability.   
Integrate stories into your website  |  We recommend integrating Web Stories into your website, such as linking them from your home page or category pages where applicable. For example, if your Web Story is about a travel destination and you have a page that lists all your travel articles, then also link the Web Stories on that category page. An additional special landing page like `www.example.com/stories` (which would then be linked from key pages like your home page) might also make sense.  There is no need to indicate in the URL of a Web Story that it is using the Web Stories format or AMP Stories technology. Ideally, your Web Stories are integrated into a wider URL strategy. For example, if your "New York Travel" articles are using a format like `"/new-york/travel/title-of-article.html"`, then consider using the exact same directory structure and URL format for your Web Stories.  
Use AMP story page attachments  |  [AMP story page attachments](https://amp.dev/documentation/components/amp-story-page-attachment/) can be used to present additional information alongside your Web Story. This can be useful to provide extra detail, deep dives, or onward journeys for the content presented in your Web Story.   
Include subtitles on video  |  Add [captions to your video](https://developer.mozilla.org/en-US/docs/Web/Guide/Audio_and_video_delivery/Adding_captions_and_subtitles_to_HTML5_video) to help readers better understand your story. Avoid captions that are burned into the video to ensure that they don't overlap with other content or flow off the screen.   
Optimize video-only stories  |  We recommend that you use semantic HTML to build your Web Story. However, some Web Story editor tools may instead export a story that formats each slide as a video file that bakes in all the text into the video. In this case, we recommend that you add the precise text displayed inside of the video as a `title` attribute on the [`amp-video`](https://amp.dev/documentation/components/amp-video/?format=stories) element. Again, only do this if you can't use semantic markup in your Web Stories.   
Add support for landscape displays  |  To enable Web Stories to appear in desktop Google Search results, add [support for landscape displays](https://amp.dev/documentation/examples/style-layout/desktop_and_landscape_mode_support/).   
  
##  Technical 

Critical technical best practices |  Make the story valid  |  Web Stories must be valid AMP pages. To avoid invalid AMP issues, test your Story using the [AMP Validator tool](https://validator.ampproject.org/) and fix any detected errors.   
---|---  
Don't include text in the poster image  |  Avoid using images that contain burned in text, as this could obstruct the title of your story when users preview your story in Search results. If users are unable to clearly read the title, they may be less likely to continue reading.   
Include the right poster image size and aspect ratio  |  Make sure that the image linked to your `<amp-story> poster-portrait-src` attribute is at least 640x853px and use an aspect ratio of 3:4.   
Include the right aspect ratio for the logo  |  Make sure that the logo image linked to your `<amp-story> publisher-logo-src` attribute is at least 96x96 px and aspect ratio of 1:1.   
  
### More technical best practices

Recommended technical best practices |  Include `og:image` |  We recommend including `og:image` in your `<meta>` tags to improve your story's discoverability.   
---|---  
  
##  Other resources 

  **Web Stories on Google**: Creator-focused resources to making Web Stories.
  **Enable Web Stories on Google Search**: Developer-oriented guide on building Web Stories that meet the technical guidelines required to appear on Google Search.
  **AMP stories website**: Developer-focused Web Stories format capabilities.
  **Web accessibility**: Tips to help ensure your Web Story is accessible to all users.
  **Structured data guidelines**: Details on adding structured data to help Google Search understand your content.

[ Previous arrow_back  Enable Web Stories on Google  ](/search/docs/appearance/enable-web-stories)

[ Next Web Story content policy  arrow_forward  ](/search/docs/appearance/web-stories-content-policy)

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-02 UTC.
