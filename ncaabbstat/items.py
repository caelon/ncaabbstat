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
    inningsp = Field()
    hitsp = Field()
    runsp = Field()
    earnedrunsp = Field()
    walksp = Field()
    strikeoutsp = Field()
    wildpitchesp = Field()
    balksp = Field()
    hbp = Field()
    ibbp = Field()
    atbatsp = Field()
    battersfacedp = Field()
    flyoutsp = Field()
    groundoutsp = Field()

    def __str__(self):
        return "%s %s went %i for %i with %i runs, %i RBI, %i walks, %i strikeouts and left %i runners on base. He had %i putouts and %i assists. He pitched %f innings. He gave up %i hits and %i runs with %i earned. He had %i walks (%i intentional), %i stikeouts, %i wild pitches, %i balks and hit %i batters. There were %i at-bats and he faced %i batters. He forced %i flyouts and %i groundouts." % (self.get('position'), self.get('name'), self.get('hits'), self.get('atbats'), self.get('runs'), self.get('rbi'), self.get('basesonballs'), self.get('strikeouts'), self.get('leftonbase'), self.get('putouts'), self.get('assists'), self.get('inningsp'), self.get('hitsp'), self.get('runsp'), self.get('earnedrunsp'), self.get('walksp'), self.get('ibbp'), self.get('strikeoutsp'), self.get('wildpitchesp'), self.get('balksp'), self.get('hbp'), self.get('atbatsp'), self.get('battersfacedp'), self.get('flyoutsp'), self.get('groundoutsp'))
