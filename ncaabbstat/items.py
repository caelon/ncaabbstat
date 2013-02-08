# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DailylinksItem(Item):
    # define the fields for your item here like:
    # name = Field()
    visitor = Field()
    home = Field()
    boxscorelink = Field()

    def __str__(self):
        return "%s at %s - %s" % (self.get('visitor'), self.get('home'), self.get('boxscorelink'))

class PlayerstatItem(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    position = Field()
    atbats = Field()
    runs = Field()
    hits = Field()
    rbi = Field()
    basesonballs = Field()
    strikeouts = Field()
    putouts = Field()
    assists = Field()
    leftonbase = Field()

    def __str__(self):
        return "%s %s went %i for %i with %i runs, %i RBI, %i walks, %i strikeouts and left %i runners on base. He had %i putouts and %i assists." % (self.get('position'), self.get('name'), self.get('hits'), self.get('atbats'), self.get('runs'), self.get('rbi'), self.get('basesonballs'), self.get('strikeouts'), self.get('leftonbase'), self.get('putouts'), self.get('assists'))
