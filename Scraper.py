#! usr/bin/env python3
from __future__ import print_function
import datetime as dt
import pandas as pd
import praw
import pickle

from Post import Post


class Scraper:
    def __init__(self, term_):
        self.searchTerm = term_ # save search term. For reddit, this is the subreddit. For twitter, this is the user(?)
        self.submissions = list() # list of submissions

    def runScrapper(self): # function to override for polymorphism
        self.message = "No Scraper defined"
        return print(self.message)

    def printSubmissions(self, a):
        print(*a, sep='\n')




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
            onesub = Post(submission.title, submission.author, submission.ups)
            self.submissions.append(onesub)

            #print(submission.title, submission.id)
        #self.printSubmissions() #prints to console the submissions found

        print("picking submissions")
        pickled_subs = pickle.dumps(self.submissions)

        print("pickled submissions")
        print("unpickling submissions")

        unpickled_subs = pickle.loads(pickled_subs)

        self.printSubmissions(unpickled_subs)





