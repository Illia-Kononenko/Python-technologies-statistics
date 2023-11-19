import scrapy
from scrapy.http import Response


class DjinniSpider(scrapy.Spider):
    name = "djinni"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python"]

    def parse(self, response: Response, **kwargs):
        for job in response.css(".list-jobs__item"):
            yield {
                "Title": job.css("a.h3.job-list-item__link::text").get().strip(),
                "Description": job.css("span[data-original-text]::attr(data-original-text)").get().strip(),
            }

        next_page = response.css(".pagination > li")[-1].css("a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
