import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
        'https://www.ptt.cc/bbs/ONE_PIECE/M.1594909632.A.CC1.html',
        'https://www.ptt.cc/bbs/ONE_PIECE/M.1594959115.A.C2C.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('PTTCrawler', start_urls=target_urls, filename='test.json')
    process.start()

if __name__ == '__main__':
    main()
