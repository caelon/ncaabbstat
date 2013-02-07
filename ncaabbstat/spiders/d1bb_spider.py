from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from ncaabbstat.items import NcaabbstatItem

class D1BBSpider(BaseSpider):
    name = "D1BB"
    allowed_domains = ["d1baseball.com"]
    start_urls = [
        "http://www.d1baseball.com/2012/daily/0407.htm"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
#        sites = hxs.select('//a[contains(., "Box Score")]')  # park this while we try to get the whole line
        sites = hxs.select('//tr')
        items = []

        for site in sites:
            if site.select('td[3]/a/text()').extract():
                item = NcaabbstatItem()
                visitor = str(site.select('td[3]/a/text()').extract())
                visitor = visitor[3:]
                item['visitor'] = visitor[:-2]
                home = str(site.select('td[6]/a/text()').extract())
                home = home[3:]
                item['home'] = home[:-2]
                boxscorelink = str(site.select('td[9]/a/@href').extract())
                boxscorelink = boxscorelink[5:]
                item['boxscorelink'] = boxscorelink[:-4]
                items.append(item)

        return items

# gets all team names: hxs.select('//td[descendant::a[contains(., "Box Score")]]/preceding-sibling::td//a/text()').extract()

