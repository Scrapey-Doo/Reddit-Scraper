# Scraper
Project Repository

## Project Description
This program will collect data from an online webpage and store it in a database. Users will be able to sign-up, login, and access their own stored data. 

Application functionality:
1. User needs to be able to sign in /create an account to use this client application
2. User needs to be able to input what they want to scrape for: Twitter or Reddit, as well as what to scrape for(Reddit subreddit, Twitter User's posts(?), into the client and the client will send that information to the server
3. The server will take the search term and type and "scrape" the data.
4. Server will take each Post/comment and create an object based off of it.
5. Server will save post object into a data structure (linked list)
6. Server will serialize the data structure into a file and send it back to the client
7. Client will take the serialized data and deserialize it.
8. Users should be able access the data structure and search through it and display information



## Project Parts
### Client:
On boot:
Asks user to log in/sign up
sends user credentials to verify/add
waits for server to respond with valid/invalid credentials.
Once valid:
Asks user what site to scrape (reddit/twitter)
Asks what to scrape for(reddit - Subreddits, twitter - certain users posts)
waits for erver to respond with data
Asks user what they want to do with data (search posts, list all posts)

### Server
Listens for connection
Once a connection is made, create new thread

On thread,
verify user information or logs them in
waits for user to send what they want to scrape for
run scraping method
serialize found data
sends back to user
Disconnects from user


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
David - Help set up client server connection. Help build multi-threading

Eric - Scraper, server functionalities

Prin - Set up user sign up functions for both client and server side

Van - Multi-threading and synchronization

Yuzhe - Project Management, Scraper, server functionalities

