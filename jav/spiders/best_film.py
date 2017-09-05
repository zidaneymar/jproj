
import scrapy
from jav.items import JavItem

class BestFilm(scrapy.Spider):
    name = "bestfilm"
    allowed_domains = ["j12lib.com"]
    start_urls = ["http://j12lib.com/cn/vl_bestrated.php"]

    def parse(self, response):
        for unit in response.xpath('//div[@class="videos"]/div[@class="video"]'):
            item = JavItem()
            i = 0
            item["mv_id"] = unit.xpath(".//div[@class='id']/text()").extract()[i]
            item["mv_name"] = unit.xpath(".//div[@class='title']/text()").extract()[i]
            item["mv_pic"] = unit.xpath(".//img/@src").extract()[i]
            i = i + 1
            yield item

        next_page = response.xpath("//a[@class='page next']/@href")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)


