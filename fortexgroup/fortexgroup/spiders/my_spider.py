import scrapy


class MySpider(scrapy.Spider): # More info on Spider class, its attributes
    # and methods https://doc.scrapy.org/en/master/topics/spiders.html
    name = "fortexgroup_1"
    start_urls = ["http://fortexgroup.ru/biznes-centr/"]

    def parse(self, response):
        for title in response.xpath("//div[contains(@class, 'pageBuild')]//div[contains(@class, 'pageBuildContent')]"):
            yield {
                'title': title.xpath("a[contains(@class, 'buildLink')]/text("
                                     ")").extract_first()
            }
