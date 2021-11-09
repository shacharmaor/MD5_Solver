import socket
from threading import Thread
import timer
from queue import Queue

#CONSTS:
STOP_MESSAGE = 'STOP'
PORT = 8200
ADDRESS = '127.0.0.1'
BUFFER = 64
FORMAT = 'utf-8'
START = 10000000000
END = 9999999999
REQUEST_QUEUE = Queue()


class Client:
    """
    DaClient
    """

    def track_progress(): #track client progress
        """
        listen to client, recieve message once range is finished:
        0. I didn't find it, give me a new range
        1. I found it, stop searching
        """
        while True:
            message_len = int(self.socket.recv(BUFFER).decode(FORMAT))
            message = self.socket.recv(message_len).decode(FORMAT)

            REQUEST_QUEUE.put(message) #'0' for not found, '1' for found
    
    def shutdown(): #sutdown thread and socket
        self.socket.close()
        self.thread.stop()
    
    def __init__(self, address, socket):
        self.address = address
        self.socket = socket
        self.found = False
        self.start = 0
        self.end = 0

        self.thread = Thread(target=self.track_progress)