# CSCI 3800 Final Project
# Group: ScrapeyDo
# Group leader: Yuzhe Lu
# Group members: Yuzhe Lu, David Oligney, Prinn Prinyanut, Eric Slick, Patrick Tate

# very rough class to model a User object on but works for now
# need to make member variables private
class User:
    name = ""
    password = ""
    searchHistory = []

    def __init__(self, name, password):
        self.name = name
        self.password = password