from browser.generic_crawler import GenericBrowserCrawler
from request.generic_crawler import GenericRequestCrawler


ml = GenericBrowserCrawler("Ml").crawl('Nintendo Switch')
az = GenericBrowserCrawler("Amazon").crawl('Playstation')

ml2 = GenericRequestCrawler("Ml").crawl('Xbox')
az2 = GenericRequestCrawler("Amazon").crawl('Sega')

print(az2)