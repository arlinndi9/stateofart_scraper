import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class Jacketsspiderscrape(scrapy.Spider):
    name = "jackets"
    allowed_domains = ["stateofart.com"]
    start_urls = ["https://www.stateofart.com/en/clothing/jackets"]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)


    def parse(self, response):
        product_links = response.css('li.product-item a.product-item-link::attr(href)').getall()
        for link in product_links:
            yield response.follow(link, self.parse_product)

    def parse_product(self, response):
        loader = ItemLoader(item={}, response=response)
        loader.default_output_processor = TakeFirst()

        loader.add_css('name', 'strong.product-item-name a::text')
        loader.add_css('url', 'link[rel="canonical"]::attr(href)')
        loader.add_css('price', 'span.price-wrapper span.price::text')
        loader.add_css('image_url', 'div.product-image-photo::attr(src)')
        sizes = response.css('div.swatch-attribute-options .swatch-option::text').getall()
        quantities = response.css('div.swatch-attribute-options .swatch-option::attr(option-qty)').getall()
        size_quantity = dict(zip(sizes, quantities))
        loader.add_value('sizes', size_quantity)

        yield loader.load_item()

    def handle_error(self, failure):
        self.logger.error(f"failed: {failure.request.url}")
        if failure.value.response.status == 429:
            self.logger.info("try")


def run_spider():
    process = CrawlerProcess()
    process.crawl(Jacketsspiderscrape)
    process.start()


if __name__ == '__main__':
    run_spider()
