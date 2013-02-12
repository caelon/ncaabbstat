from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from operator import itemgetter

from ncaabbstat.items import DailylinksItem, BattingstatItem, PitchingstatItem

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
                item = DailylinksItem()
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

class BoxscoreStyle1Spider(BaseSpider):
    name = "bx1"
    allowed_domains = ["lsusports.com"]
    start_urls = [
        "http://www.lsusports.net/fls/5200/assets/docs/bb/12stats/lsu407.htm"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        lines = hxs.select('//tr[@bgcolor="#ffffff"]')
        items = []

        for line in lines:
            if str(line.select('td[11]').extract()) == "[]":
                item = BattingstatItem()
                namepos = str(line.select('td[1]/font/text()').extract())
                namepos = namepos[3:-6]
                namepos = namepos.replace("\\xa0","")
                if namepos != "":
                    if namepos[:1] == " ":
                        namepos = namepos[1:]
                    if namepos[:6] != "Totals":
                        if namepos[-1:] == 'p' or namepos[-1:] == 'c':
                            item['position'] = namepos[-1:]
                            item['name'] = namepos[:-2]
                        else:
                            item['position'] = namepos[-2:]
                            item['name'] = namepos[:-3]
                        atbats = str(line.select('td[2]/font/text()').extract())
                        item['atbats'] = int(atbats[3:-6])
                        runs = str(line.select('td[3]/font/text()').extract())
                        item['runs'] = int(runs[3:-6])
                        hits = str(line.select('td[4]/font/text()').extract())
                        item['hits'] = int(hits[3:-6])
                        rbi = str(line.select('td[5]/font/text()').extract())
                        item['rbi'] = int(rbi[3:-6])
                        basesonballs = str(line.select('td[6]/font/text()').extract())
                        item['basesonballs'] = int(basesonballs[3:-6])
                        strikeouts = str(line.select('td[7]/font/text()').extract())
                        item['strikeouts'] = int(strikeouts[3:-6])
                        putouts = str(line.select('td[8]/font/text()').extract())
                        item['putouts'] = int(putouts[3:-6])
                        assists = str(line.select('td[9]/font/text()').extract())
                        item['assists'] = int(assists[3:-6])
                        leftonbase = str(line.select('td[10]/font/text()').extract())
                        item['leftonbase'] = int(leftonbase[3:-6])
                        items.append(item)
            elif str(line.select('td[11]').extract()) != "[]":
                item = PitchingstatItem()
                namepos = str(line.select('td[1]/font/text()').extract())
                namepos = namepos[3:-6]
                namepos = namepos.replace("\\xa0","")
                if namepos != "":
                    if namepos[:1] == " ":
                        namepos = namepos[1:]
                    if namepos[:6] != "Totals":
                        item['position'] = 'p'
                        item['name'] = namepos
                        ips = str(line.select('td[2]/font/text()').extract())
                        item['inningsp'] = float(ips[3:-6])
                        hitsp = str(line.select('td[3]/font/text()').extract())
                        item['hitsp'] = int(hitsp[3:-6])
                        runsp = str(line.select('td[4]/font/text()').extract())
                        item['runsp'] = int(runsp[3:-6])
                        earnedrunsp = str(line.select('td[5]/font/text()').extract())
                        item['earnedrunsp'] = int(earnedrunsp[3:-6])
                        walksp = str(line.select('td[6]/font/text()').extract())
                        item['walksp'] = int(walksp[3:-6])
                        strikeoutsp = str(line.select('td[7]/font/text()').extract())
                        item['strikeoutsp'] = int(strikeoutsp[3:-6])
                        wildpitchesp = str(line.select('td[8]/font/text()').extract())
                        item['wildpitchesp'] = int(wildpitchesp[3:-6])
                        balksp = str(line.select('td[9]/font/text()').extract())
                        item['balksp'] = int(balksp[3:-6])
                        hbp = str(line.select('td[10]/font/text()').extract())
                        item['hbp'] = int(hbp[3:-6])
                        ibbp = str(line.select('td[11]/font/text()').extract())
                        item['ibbp'] = int(ibbp[3:-6])
                        atbatsp = str(line.select('td[12]/font/text()').extract())
                        item['atbatsp'] = int(atbatsp[3:-6])
                        battersfacedp = str(line.select('td[13]/font/text()').extract())
                        item['battersfacedp'] = int(battersfacedp[3:-6])
                        flyoutsp = str(line.select('td[14]/font/text()').extract())
                        item['flyoutsp'] = int(flyoutsp[3:-6])
                        groundoutsp = str(line.select('td[15]/font/text()').extract())
                        item['groundoutsp'] = int(groundoutsp[3:-6])
                        items.append(item)
        combinedstats = str(hxs.select('//table[@width="555"]/tr/td/font/text()').extract())
        combinedstats = combinedstats.replace("\\r\\n","")
        combinedstats = combinedstats[3:-2]
        statcategories = ['E','LOB','2B','3B','HR','HBP','SH','SF','SB','Win','Loss','Save','WP']
        catstart = {}
        for statcategory in statcategories:
            withhyphen = statcategory+' -'
            catstart[statcategory] = int(combinedstats.find(withhyphen))
        catstart = sorted(catstart.iteritems(), key=itemgetter(1), reverse=False)
        catend = {}
        for (index, elem) in catstart:
            currentstart = int(elem)
            if currentstart != 0:
                catend[previousindex] = int(elem)-1
            previousindex = index
        catend[index] = len(combinedstats)
        statstring = {}
        for (index, elem) in catstart:
            currentend = catend[index]
            statstring[index] = combinedstats[elem:currentend]
        for (index, elem) in statstring:
            #parse through character by character
        print combinedstats, statstring
        
        return items
