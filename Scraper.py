#! usr/bin/env python3

import datetime as dt
import pandas as pd
import praw

from Post import Post


class Scraper:
    def __init__(self, term_):
        self.searchTerm = term_ # save search term. For reddit, this is the subreddit. For twitter, this is the user(?)

    def runScrapper(self): # function to override for polymorphism
        self.message = "Running Program"


class RedditScraper(Scraper):
    def __init__(self, term_):
        super().__init__(term_) #use parent search term

    def runScrapper(self):
        print(self.searchTerm)

        personalUseScript = 'Xg1TzmCGtbHcQQ'
        secret = '0HnIVUpJwOAp_-R0vVwt55Js5ds'

        reddit = praw.Reddit(client_id=personalUseScript,
                             client_secret=secret,
                             user_agent='PyScraper',
                             username='Arsenal4891',
                             password='javapython')

        subreddit = reddit.subreddit(self.searchTerm)
        hot_subreddit = subreddit.hot(limit=10)

        for submission in hot_subreddit:
            print(submission.title, submission.id)



sc = RedditScraper('Games')
sc.runScrapper()
