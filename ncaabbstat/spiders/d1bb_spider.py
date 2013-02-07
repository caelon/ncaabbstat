from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class D1BBSpider(BaseSpider):
    name = "D1BB"
    allowed_domains = ["d1baseball.com"]
    start_urls = [
        "http://www.d1baseball.com/2012/daily/0407.htm"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//a[contains(., "Box Score")]')
        for site in sites:
            #title = site.select('a/text()').extract()
            link = site.select('@href').extract()
            desc = site.select('text()').extract()
#            print title, link, desc
            print link, desc
