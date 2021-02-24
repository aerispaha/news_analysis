import datetime
import logging

import feedparser
# import pymongo

logging.basicConfig(filename='news.log', level=logging.INFO)

# grab the headlines
feeds = dict(
    nyt=r'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    fox=r'http://feeds.foxnews.com/foxnews/most-popular',
    wsj_opinion=r'http://www.wsj.com/xml/rss/3_7041.xml',
    wsj_business=r'http://www.wsj.com/xml/rss/3_7014.xml',
    wsj_world=r'http://www.wsj.com/xml/rss/3_7085.xml',
    wapo_national=r'http://feeds.washingtonpost.com/rss/national',
    cnn=r'http://rss.cnn.com/rss/cnn_topstories.rss',
    cnn_us=r'http://rss.cnn.com/rss/cnn_us.rss',
    breitbart=r'http://feeds.feedburner.com/breitbart',
    cnbc=r'http://www.cnbc.com/id/100003114/device/rss/rss.html',
    abc=r'http://feeds.abcnews.com/abcnews/topstories',
    bbc=r'http://feeds.bbci.co.uk/news/rss.xml',
    wired=r'https://www.wired.com/feed/',
    upi=r'http://rss.upi.com/news/top_news.rss',
    # reuters=r'http://feeds.reuters.com/reuters/topNews',
    usa_today=r'http://rssfeeds.usatoday.com/usatoday-NewsTopStories',
    ap=r'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a96b4ad082fe88aa0db04305',
    npr=r'http://www.npr.org/rss/rss.php?id=1001',
    democracy_now=r'https://www.democracynow.org/democracynow.rss',
)


def main():
    dt = datetime.datetime.utcnow()
    # headlines_per_source = 10
    data = []

    for feed, url in feeds.items():
        logging.debug(f'parsing {feed}...')
        rss_parsed = feedparser.parse(url)
        titles = [art['title'] for art in rss_parsed['items']]  # [:headlines_per_source]]
        d = {
            'source': feed,
            'stories': titles,
            'datetime': dt
        }
        data.append(d)

    # 1. Connect to MongoDB instance running on localhost
    # client = pymongo.MongoClient()

    # Access the 'restaurants' collection in the 'test' database
    # collection = client.news.headlines

    # insert the data
    # collection.insert_many(data)

    logging.debug('inserted headlines')


if __name__ == "__main__":
    main()
