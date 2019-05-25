import scrapy


# the CrawlSpider class is different from the Spider class below
#   However, instead of a start_requests method, I define
#   an allowed_domains & start_urls method, then I define a
#   set of rules for the spider to follow.


# this class is used to inherit from scrapy.Spider
"""
class HorseSpider(scrapy.Spider):

    name = 'ike'

    # defines the initial request to be made, and if applicable, how to
    #   follow lengths
    def start_requests(self):
        urls = ['https://treehouse-projects.github.io/horse-land/index.html',
                'https://treehouse-projects.github.io/horse-land/mustang.html']

        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    # tells the spider how extracted data is to be processed
    def parse(self, response):
        url = response.url
        page = url.split('/')[-1]
        filename = 'horses-%s' % page
        print('URL is: {}'.format(url))
        with open(filename, 'wb') as file:
            file.write(response.body)
        print('Saved file %s' % filename)
"""
