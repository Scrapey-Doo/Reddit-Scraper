class Post:
    def __init__(self, title_, author_, likes_):
        self.title = title_
        self.likes = likes_
        self.author = author_


    def getTitle(self):
        return self.title

    def getLikes(self):
        return self.likes

    def getAuthor(self):
        return self.author

    def __repr__(self):
        return "Title: " + str(self.getTitle()) + " Author: " + str(self.getAuthor()) + " Likes: " + str(self.getLikes())

