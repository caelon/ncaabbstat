from scrapy.spider import BaseSpider

class D1BBSpider(BaseSpider):
    name = "D1BB"
    allowed_domains = ["d1baseball.com"]
    start_urls = [
        "http://www.d1baseball.com/2012/daily/0407.htm"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
