# Scrapy settings for ncaabbstat project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'ncaabbstat'

SPIDER_MODULES = ['ncaabbstat.spiders']
NEWSPIDER_MODULE = 'ncaabbstat.spiders'
DEFAULT_ITEM_CLASS = 'ncaabbstat.items.DailylinksItem'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ncaabbstat (+http://www.yourdomain.com)'
