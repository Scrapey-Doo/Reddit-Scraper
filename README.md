# Scraper
Project Repository

## Project Description
This program will collect data from an online webpage and store it in a database. Users will be able to sign-up, login, and access their own stored data. 

Application functionality:
1. User needs to be able to sign in /create an account - > if the application can directly sign into reddit/twitter
2. User needs to be able to input what they want to scrape for: input a key term, key terms, time frame, POST and/or COMMENTS.
3. The application will take user information, key term, time frame and "scrape" the data.
4. Application will take each Post/comment and create an object based off of it.
5. Application will send created object to a database/server
6. GUI should display the objects stored in the database.
7. Users should be able to search/sort/delete the contents in the database
8. Users should be able to click on the post/comment (object will have a link) in the object to access the post from the source.



## Project Parts
### Front-End:
Database side of things. 
Stores Users. Accepts input from GUI(login, search terms, etc)
User signs in to reddit/twitter here.
Displays database. Allows user to 
Takes scrapper output and stores in a database


### Back-End
Scrapper side of things
Accepts data from Front-End
Connects to reddit/twitter
Searches through posts/comments
Takes post/comment data, parse, and store into an object.
Sends found object into a database

### GUI
Integrate with front end
Displays to users login/signup screen - need to login to Reddit/Twitter account.
Once logged in, user can choose between searching, or looking at previous search results
For searching, ask for key-term/key-terms, POST and/or COMMENTS, time frame (for starters, do one day)


## Project Milestones

Web Server - Server can Listen
Web Server - Server creates processes from Listen
Web Server - Server can differentiate between post from scraper and user request
Web Server - Server will produce results from user query

Scraper - Scraper class implemented
Scraper - Reddit scrapper subclass implemented
Scraper - Successfully connects to web server for post.
Scraper - Successfully output Post object data 


## Member Roles
David - Web Server

Eric - Scraper

Prin - Web Server

Van - Web Server

Yuzhe - Project Management, Scraper

