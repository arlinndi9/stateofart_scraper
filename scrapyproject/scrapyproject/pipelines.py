# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import psycopg2

class PostgresPipeline:
    def open_spider(self, spider):
        self.conn = psycopg2.connect(
            host=spider.settings.get('POSTGRES_HOST'),
            port=spider.settings.get('POSTGRES_PORT'),
            dbname=spider.settings.get('POSTGRES_DB'),
            user=spider.settings.get('POSTGRES_USER'),
            password=spider.settings.get('POSTGRES_PASSWORD')
        )
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        try:
            self.conn.commit()
        except Exception as e:
            spider.logger.error(f"error commit: {e}")
        finally:
            self.cursor.close()
            self.conn.close()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """
                INSERT INTO jackets (product_name, product_url, price, sizes, image_url) 
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    item["name"],
                    (item["url"]),
                    item["price"],
                    item["sizes"],
                    item["image_urls"]
                )
            )
        except Exception as e:
            spider.logger.error(f"error: {e}")
        return item

class ScrapyprojectPipeline:
    def process_item(self, item, spider):
        return item
