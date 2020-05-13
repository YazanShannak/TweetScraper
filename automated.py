from scrapy.crawler import CrawlerProcess
from TweetScraper.spiders.TweetCrawler import TweetScraper

process = CrawlerProcess()
process.crawl(TweetScraper, query="(corona OR virus OR pandemic OR coronavirus OR covid-19 OR covid19) near:nyc until:2020-03-31 since:2020-03-10")
process.start()


