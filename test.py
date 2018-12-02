# test for reading in from pickled file

from Scraper import RedditScraper
import pickle


sc = RedditScraper('Games')
#sc.runScrapper()

unpickled_subs = pickle.loads(sc.runScrapper())
print()
for line in unpickled_subs:
    print(line)