#!/usr/bin/env python
# coding: utf-8

'''
After running this script, create and run an HTTP client from the Tools menu.
Set the localhost (you can leave as it is) and the port which will be used (5555 in this case)
'''
# imports
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler

import socket
import json

# set the twitter API credentials
consumer_key='XoR1QAkGcUsdhRcJ6yRw2jSfM'
consumer_secret='jRIB9OBHjzUF7roMA6Eu3y8vuJQ9sOCgZPtFcAyuYQZRxwbBUy'
access_token = '835776335381417984-xKyW6eTmYivSCsZ30XrtaPqQyG1lBis'
access_secret='NEGX0ZfcFW6xBQ6xUgURFAEqSiZv2HGykNydcHqECItNV'


class TweetsListener(StreamListener):
    # tweet object listens for the tweets
    def __init__(self, csocket):
        self.client_socket = csocket
    def on_data(self, data):
        try:
            msg = json.loads(data)
            print("new message")
            # add at the end of each tweet "t_end"
            self.client_socket\
                .send(str(msg['text']+"t_end")\
                .encode('utf-8'))
            print(msg['text'])
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    def on_error(self, status):
        print(status)
        return True
'''
Bounding coordinates can be found using this link: https://boundingbox.klokantech.com/
In this case the coordinates are for UK
'''
def sendData(c_socket, keyword):
    print('start sending data from Twitter to socket')
    # authentication based on the credentials
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # start sending data from the Streaming API 
    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(locations=[-7.24, 49.93, 1.85, 58.98], track = keyword, languages=["en"])

if __name__ == "__main__":
    # server (local machine) creates listening socket
    s = socket.socket()
    host = "127.0.0.1"    
    port = 4444
    s.bind((host, port))
    print('socket is ready')
    # server (local machine) listens for connections
    s.listen(4)
    print('socket is listening')
    # return the socket and the address on the other side of the connection (client side)
    c_socket, addr = s.accept()
    print("Received request from: " + str(addr))
    # select here the keyword for the tweet data
    sendData(c_socket, keyword = ['covid'])





