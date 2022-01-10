import scrapy


class FundaSpider(scrapy.Spider):
    name = "FundaSpider"
    allowed_domains = ['funda.nl']
    start_urls = [
        'https://www.funda.nl/huur/breda/0-1500/3+slaapkamers/p1/'
    ]

    def parse(self, response, **kwargs):
        residences = response.xpath('//*[@id="content"]/form/div/div/div/ol[contains(@class, "search-results")]/li').getall()
        self.logger.info('Found %s residences', len(residences))

        for residence in residences:
            print('test')

