# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class NcaabbstatItem(Item):
    # define the fields for your item here like:
    # name = Field()
    visitor = Field()
    home = Field()
    boxscorelink = Field()

    def __str__(self):
        return "%s at %s - %s" % (self.get('visitor'), self.get('home'), self.get('boxscorelink'))
