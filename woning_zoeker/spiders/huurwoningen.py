import scrapy


class HuurwoningenSpider(scrapy.Spider):
    name = "HuurwoningenSpider"
    allowed_domains = ['huurwoningen.nl']
    start_urls = [
        'https://www.huurwoningen.nl/in/breda/?max_price=1500&number_of_rooms=35&sort=datetime_modified&direction=desc&page=1'
    ]

    def parse(self, response, **kwargs):
        residences = response.xpath('//*[@id="listings"]/section[contains(@class, "listing")]').getall()
        self.logger.info('Found %s residences', len(residences))

        # for residence in residences:
        #     print(residence)