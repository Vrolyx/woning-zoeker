import scrapy


class PapariusSpider(scrapy.Spider):
    name = "PapariusSpider"
    allowed_domains = ['paparius.nl']
    start_urls = [
        'https://www.pararius.com/apartments/breda/0-1500/3-bedrooms'
    ]

    def parse(self, response, **kwargs):
        residences = response.xpath('/html/body/main/div[2]/div[1]/div[3]/ul').get()
        print(residences)
        self.logger.info('Found %s residences', len(residences))

