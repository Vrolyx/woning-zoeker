import scrapy


class RotsvastSpider(scrapy.Spider):
    name = "RotsvastSpider"
    allowed_domains = ['rotsvast.nl']
    start_urls = [
        'https://www.rotsvast.nl/woningaanbod/?type=2&city=Breda&office=0&maximumPrice[2]=1500&minimumBedrooms=3&count=30'
    ]

    def parse(self, response, **kwargs):
        residences = response.xpath(
            '//*[@id="viewOther"]/div/div/div/div[contains(@class, "residence-street")]/text()').getall()
        self.logger.info('Found %s residences', len(residences))

        for residence in residences:
            print(residence)
