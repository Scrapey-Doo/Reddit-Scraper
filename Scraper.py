# CSCI 3800 Final Project
# Group: ScrapeyDo
# Group leader: Yuzhe Lu
# Group members: Yuzhe Lu, David Oligney, Prinn Prinyanut, Eric Slick, Patrick Tate

#! usr/bin/env python3
from __future__ import print_function
import datetime as dt
import pandas as pd
import praw
import pickle

from Post import Post # Post object to hold the Reddit or Twitter post info

# parent class for Reddit and Twitter scrapers
class Scraper:

    # *** need to add some private member variables like these, will do later
    #self.__searchTerm # term to scrape for
    #self.__submissions # list of submissions

    # term = "gaming" or any other keyword the user wants search for
    # initialize empty list submissions
    def __init__(self, term_):

        # private member variables
        self.searchTerm = term_ # save search term. For reddit, this is the subreddit. For twitter, this is the user(?)
        self.submissions = list() # list of submissions

    # abstract function
    # to be defined in sub classes RedditScraper and TwitterScraper
    def runScrapper(self):
        self.message = "No Scraper defined"
        return print(self.message)

    # print the submissions
    def printSubmissions(self, a):
        #print(self.submissions, sep='\n')
        print(*a, sep='\n')



# subclass of Scraper base class
# I think it makes sense to have the reddit api variables as member variables,
# so the RedditScraper class can be differentiated from the Scraper base class.
# Needs to have all these member variables as private
class RedditScraper(Scraper):

    # hold pickle file of reddit submissions
    pickledSubs: bytes

    # default initializer takes 1 parameter
    # term =  "gaming" string variable to serach for
    # construct RedditScraper object
    def __init__(self, term_):
        # call Scraper constructor
        super().__init__(term_) #use parent search term
        # instantiate blank string to hold  pickled file
        self.pickledSubs = ""

    # returns a pickled file of reddit submissions
    # overridden function from Scraper base class
    # connect to Reddit via praw api
    # append hot_subreddit submissions to member variable submissions
    def runScrapper(self):
        print(self.searchTerm)

        # api variables and login info
        # might be good to have these as member variables
        personalUseScript = 'Xg1TzmCGtbHcQQ'
        secret = '0HnIVUpJwOAp_-R0vVwt55Js5ds'
        reddit = praw.Reddit(client_id=personalUseScript,
                             client_secret=secret,
                             user_agent='PyScraper',
                             username='Arsenal4891',
                             password='javapython')

        # get top 10 subreddit and hotsubreddit submissions
        subreddit = reddit.subreddit(self.searchTerm)
        hot_subreddit = subreddit.hot(limit=10)

        # append reddit submissions to self.submissions
        for submission in hot_subreddit:
            onesub = Post(submission.title, submission.author, submission.ups)
            self.submissions.append(onesub)

            # print submission
            print(submission.title, submission.id)
        self.printSubmissions(self.submissions) #prints to console the submissions found

        # send submissions to pickled file
        print("pickling submissions")
        self.pickledSubs = pickle.dumps(self.submissions)

        print("pickled submissions")

        # load pickled submissions, keeping comments here for reference
        # but moved these two lines of logic to test.py
        #print("unpickling submissions")
        #unpickled_subs = pickle.loads(self.pickleSubs)

        # return the pickled file of reddit submissions
        return self.pickledSubs
