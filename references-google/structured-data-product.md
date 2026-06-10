# Product 产品结构化数据

> 来源：Google Search Central (https://developers.google.com/search/docs/appearance-structured-data-product.txt)

---

# Introduction to `Product` structured data

When you add structured data to your product pages, your product information can appear in richer ways in Google Search results (including [Google Images](https://images.google.com/) and [Google Lens](https://lens.google/)). For example, users can see price, availability, review ratings, shipping information, and more right in search results. 

## Deciding which markup to use

There are two main classes of product structured data. Follow the requirements for the type that best suits your use case: 

  **Product snippets**: For product pages where people can't directly purchase the product. This markup has more options for specifying review information, like [pros and cons](/search/docs/appearance/structured-data/product-snippet#pros-cons-example) on an editorial product review page. 
  **Merchant listings**: For pages where customers can purchase products from you. This markup has more options for specifying detailed product information, like [apparel sizing](/search/docs/appearance/structured-data/merchant-listing#size-specification-properties), [shipping details](/search/docs/appearance/structured-data/merchant-listing#shipping), and [return policy](/search/docs/appearance/structured-data/merchant-listing#returns) information. 

Note that there is some overlap between the two product features. In general, adding the [required product information properties](/search/docs/appearance/structured-data/merchant-listing#product-information) for merchant listings means that your product pages can also be eligible for product snippets. Both features have their own enhancements, so be sure to review both when deciding which markup makes sense in the context of your site (the more properties you can add, the more enhancements your page can be eligible for). 

Do you offer variants of your products? Adding [product variant structured data](/search/docs/appearance/structured-data/product-variants) can help Google better understand which products are variations of the same parent product. Both product snippets and merchant listings support product variants. 

In addition to structured data for the individual products that you sell, we also recommend you add structured data defining the policies of your ecommerce business, nested under `Organization` markup:

  **Merchant return policy**: Specify the return policy (or policies) for your business.
  **Loyalty Program**: Specify the loyalty program that you offer.

## How shopping experiences can appear on Google Search

Here's how shopping experiences can appear in Google Search results. This list is not exhaustive—Google Search is constantly exploring new and better ways to help people find what they're looking for, and the experiences may change over time. 

##### Product snippet

A [text result](/search/docs/appearance/visual-elements-gallery#text-result) that includes additional product information such as ratings, review information, price, and availability  |   
---|---  
  
##### Popular products

Visually rich presentation of products for sale  |   
  
##### Shopping knowledge panel

Detailed product information with a list of sellers (using details such as product identifiers)  |   
  
##### Google Images

Annotated images of products available for sale  |   
  
### Result enhancements

Search result enhancements are shown at the discretion of each experience, and may change over time. For this reason, it is recommended to provide as much rich product information as available, without concern for the exact experiences that will use it. Here are some examples of how product rich results may be enhanced: 

  * Ratings: Enhance the appearance of your search result by providing [customer reviews and ratings](/search/docs/appearance/structured-data/product-snippet#product-reviews).
  * Pros and Cons: Identify [pros and cons](/search/docs/appearance/structured-data/product-snippet#pros-cons) in your product review description so they can be highlighted in search results.
  * Shipping: Share [shipping costs](/search/docs/appearance/structured-data/merchant-listing#shipping), especially free shipping, so shoppers understand the total cost.
  * Availability: Provide [availability](/search/docs/appearance/structured-data/merchant-listing#availability) data to help customers know when you have a product in stock.
  * Price drop: Price drops are computed by Google by observing price changes for the product over time. Price drops are not guaranteed to be shown.
  * Returns: Share [return information](/search/docs/appearance/structured-data/merchant-listing#returns), such as your return policy, fees involved in returns, and how many days customers have to return a product.

## Providing product data to Google Search

To provide rich product data to Google Search you can add `Product` structured data to your web pages, upload data feeds with Google Merchant Center and opt into free listings within the Merchant Center console, or both. The Search Central documentation focuses on structured data on web pages. 

Providing both structured data on web pages and a Merchant Center feed maximizes your eligibility to experiences and helps Google correctly understand and verify your data. Some experiences combine data from structured data and Google Merchant Center feeds if both are available. For example, product snippets may use pricing data from your merchant feed if it's not present in the structured data on the page. The [Google Merchant Center feed documentation](https://support.google.com/merchants/answer/7052112) includes additional recommendations and requirements for feed attributes. 

In addition to Google Search, learn more about eligibility to the [Google Shopping tab](https://support.google.com/merchants/answer/9826670) by reading the [data and eligibility requirements in Google Merchant Center](https://support.google.com/merchants/answer/9199328).

---
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.
