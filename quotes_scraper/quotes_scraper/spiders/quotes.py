import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/page/1'
    ]
    def parse(self, response):
        print('***********')
        print(response.status)
        print('\n\n')
        print('***********')
        print(response.headers)
