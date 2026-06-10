# 更新 robots.txt

> 来源：Google Search Central

---

# Update your robots.txt file

To update the rules in your existing robots.txt file, download a copy of your robots.txt file from your site and make the necessary edits. Then, upload the updated file to your site. 

If you use a site hosting service, such as Wix or Blogger, you might not need to (or be able to) edit your robots.txt file directly. Instead, your provider might expose a search settings page or some other mechanism to tell search engines whether or not to crawl your page. 

If you want to hide or unhide one of your pages from search engines, search for instructions about modifying your page visibility in search engines on your hosting service, for example, search for "wix hide page from search engines". 

## Download your robots.txt file

You can download your robots.txt file various ways, for example: 

  * Navigate to your robots.txt file, for example `https://example.com/robots.txt` and copy its contents into a new text file on computer. Make sure you follow the guidelines related to the [file format](/crawling/docs/robots-txt/create-robots-txt#format_location) when creating the new local file. 
  * Download an actual copy of your robots.txt file with a tool like curl. For example: 
    
        curl https://example.com/robots.txt -o robots.txt

  * Use the [robots.txt report](https://support.google.com/webmasters/answer/6062598) in Search Console to copy the content of your robots.txt file, which you can then paste into a file on your computer. 

## Edit your robots.txt file

Open the robots.txt file you downloaded from your site in a text editor and make the necessary edits to the rules. Make sure you use the [correct syntax](/crawling/docs/robots-txt/create-robots-txt#create_rules) and that you save the file with UTF-8 encoding. 

## Upload your robots.txt file

Upload your new robots.txt file to the root directory of your site as a text file named robots.txt. The way you upload a file to your site is highly platform and server dependent. Check out our tips for finding help with [uploading a robots.txt file to your site](/crawling/docs/robots-txt/create-robots-txt#upload). 

If you do not have permission to upload files to the root directory of your site, contact your domain manager to make changes.

For example, if your site home page resides under `subdomain.example.com/site/example/`, you likely cannot update the robots.txt file at `subdomain.example.com/robots.txt`. In this case, contact the owner of `example.com/` to make any necessary changes to the robots.txt file. 

## Refresh Google's robots.txt cache

During the automatic crawling process, Google's crawlers notice changes you made to your robots.txt file and update the cached version every 24 hours. If you need to update the cache faster, use the Request a recrawl function of the [robots.txt report](https://support.google.com/webmasters/answer/6062598).

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-21 UTC.
