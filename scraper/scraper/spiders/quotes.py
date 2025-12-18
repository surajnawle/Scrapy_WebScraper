import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        # extract quote data
        for q in response.css("div.quote"):
            yield {
                "quote": q.css("span.text::text").get(),
                "author": q.css("small.author::text").get(),
            }

        # pagination logic (same indentation as for-loop)
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
