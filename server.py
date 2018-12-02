# CSCI 3800 Final Project
# Group: ScrapeyDo
# Group leader: Yuzhe Lu
# Group members: Yuzhe Lu, David Oligney, Prinn Prinyanut, Eric Slick, Patrick Tate

# first run server.py, then run client.py to connect as many different clients to the Server as you want

from socket import socket, AF_INET, SOCK_STREAM # because we need sockets to connect to clients
import threading # multi-thread the clients
#import sys not sure if we will need this or not, works with it uncommented so...
from User import User # because Server has a list of users


# Server class to handle multiple clients
# file is run by instantiating a Server object and calling member function run() at the bottom of this file
# Server object stays open and listens for clients
# Server object can handle multiple clients and takes advantage of multi-threading
# ********************************************************************************
# run() method calls the handler method which takes the connection and address as paramters
# from there, a client is greeted with an inital menu screen to create and account or login
class Server:

    # *** member variables ***

    # socket to bind and listen for clients
    serversocket = socket(AF_INET, SOCK_STREAM)
    # list of client connections, when client chooses to disconnect, connection is removed from list and connection is closed
    connections = []
    # list of User objects, will be a dictionary {} that is serialized and read in
    clients = []

    # *** member variables ***

    # default initializer, listen for clients on socket 5000
    def __init__(self):
        self.serversocket.bind(('localhost', 5000))
        self.serversocket.listen(5)
        self.connections = []
        self.clients = []

    # only function we need to call to start the server while it waits for clients
    # will run this in a main/App file later, but for now just runs at the bottom of this file
    def run(self):
        # wait for clients, need to figure out the best way to end this loop other than pressing the "stop" button
        while True:
            # accept connection from client
            connection, address = self.serversocket.accept()
            # add connection to the list of connections self.connections
            self.connections.append(connection)
            # thread for this connection, call self.handler() function
            cthread = threading.Thread(target=self.handler, args=(connection, address))
            cthread.daemon = True
            cthread.start()
            # print the address for reference
            print(str(address[0]) + ':' + str(address[1]) + " connected")

    # calls initialMenu(connection, address) function to display the first menu to the user
    def handler(self, connection, address):
        self.initialMenu(connection, address)

    # first menu client/user sees when connecting to server
    # takes connection and address variables from serversocket.accept() function in run(self)
    def initialMenu(self, connection, address):
        while True:
            # initial menu message for user/client
            initialMsg = "Welcome to the Scraping Server\n" \
                         "Choose an option\n" \
                         "1: create account\n" \
                         "2: sign in\n" \
                         "3: disconnect"
            # send itial menu message to user
            connection.send(bytes(initialMsg, 'utf-8'))
            # receive input from the user on which option
            data = connection.recv(1024)

            # convert client input to string
            clientOption1 = str(data, 'utf-8')

            # switch on user input option
            # 1 = create account
            # calls createAccount() function
            # account user name must not already exist in self.clients list
            if clientOption1 == "1":
                # print message on server for reference
                print("client chose create account")
                # call createAccount function with connection, address info
                self.createAccount(connection, address)
                # can delete lines below, printing on the server the user names in self.clients just for reference
                for user in self.clients:
                    print(user.name)

            # client wants to sign in
            # password needs to be validated in list/dictionary of users
            # *** need to write this function ***
            elif clientOption1 == "2":
                print("client chose sign in")

            # client wants to disconnect
            # remove client from list of connections and close connection
            # *** need to add this as a case, and have last else as default catch bad input ***
            else:
                self.connections.remove(connection)
                print(str(address[0]) + ':' + str(address[1]) + " disconnected")
                connection.close()
                break

            # this is a catch if there is no more connections of data incoming
            if not data:
                self.connections.remove(connection)
                print(str(address[0]) + ':' + str(address[1]) + " disconnected")
                connection.close()
                break

    # void function to create a user account
    # creates a User object based on client input and adds user to self.clients list/dictionary
    # user is prompted to enter another name if user name alerady exists in self.clients
    def createAccount(self, connection, address):
        # msg to send client
        chooseName = "Enter a username (must not be taken)\n"
        # send msg to client
        connection.send(bytes(chooseName, 'utf-8'))
        # receive name
        name = connection.recv(1024)
        # convert name to a string, always utf-8 encoding
        sname = str(name, 'utf-8')
        print(sname) # print for reference

        # check if name exists in self.clients
        valid = self.isValid(sname)
        # if name is valid, prompt for a password, create a User object and add to self.clients
        if valid:
            successMsg = "valid username"
            connection.send(bytes(successMsg, 'utf-8'))
            choosePassword = "Enter a password: \n"
            connection.send(bytes(choosePassword, 'utf-8'))
            password = connection.recv(1024)
            spassword = str(password, 'utf-8')
            print(spassword)
            user = User(sname, spassword)
            self.clients.append(user)
        # else prompt user to enter another name
        else:
            errMsg = "Name taken, try again"
            connection.send(bytes(errMsg, 'utf-8'))

    # returns True if name isn't in self.clients
    # returns False if name is equal to user.name in self.clients
    def isValid(self, name):
        validName = True
        # if self.clients list is empty, no user names exist yet, return True
        if len(self.clients) == 0:
            print("zero size")
            return True

        # check list of users to see if user name already exists
        # return False if user name already exists
        for user in self.clients:
            if user.name == name:
                return False

        # return True is all above checks passed
        return validName

# instantiate Server object
server = Server()
# run the whole party
server.run()
