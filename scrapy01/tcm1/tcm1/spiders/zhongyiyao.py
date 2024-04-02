import scrapy


class ZhongyiyaoSpider(scrapy.Spider):
    name = "zhongyiyao"
    allowed_domains = ["www.zhzyw.com"]
    start_urls = ["http://www.zhzyw.com/"]

    def parse(self, response):
        print("测试！")
        pass
