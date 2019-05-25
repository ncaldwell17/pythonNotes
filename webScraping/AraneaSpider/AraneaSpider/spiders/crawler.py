from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# this program extracts links from a site following rules I set

class HorseSpider(CrawlSpider):

    name = 'Whirlaway'

    allowed_domains = ['treehouse-projects.github.io']

    start_urls = ['http://treehouse-projects.github.io/horse-land']

    rules = [Rule(LinkExtractor(allow=r'.*'),
                  callback = 'parse_horses',
                  follow = True)]

    def parse_horses(self, response):
        url = response.url
        title = response.css('title::text').extract()
        print('Page URL: {}'.format(url))
        print('Page title: {}'.format(title))
