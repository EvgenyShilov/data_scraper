import scrapy


class MySpider(scrapy.Spider): # More info on Spider class, its attributes
    # and methods https://doc.scrapy.org/en/master/topics/spiders.html
    name = "fortexgroup_2"
    start_urls = ["http://fortexgroup.ru/bc/"]

    def parse(self, response):
        for href in response.xpath('//div[contains(@class, '
                                   '"pageBuildContent")]//a['
                                   '1]/@href').extract():
            yield scrapy.Request(href, callback=self.parse_building)

    def parse_building(self, response):
        yield {
            'name': response.xpath('//div[contains(@class, "buildContent")]//div[contains(@class, "col cLeft")]/h2').extract_first(),
            'address': response.xpath('//div[contains(@class, "address")]').extract_first(),
            'okrug': response.xpath('//table[contains(@class, "params")]//tr[2]/td[2]').extract_first(),
            'description': response.xpath('//div[contains(@class, '
                                          '"text")]').extract_first(),
            'area_gross': response.xpath('//table[contains(@class, "params")]//tr[10]/td[2]').extract_first(),
        }

        for title in response.xpath('//table[contains(@class, "rent")]//tr'):
            yield {
                'area_specific': title.xpath('td[1]//a/text()').extract_first(),
                'price': title.xpath('td[2]/text()').extract_first(),
            }