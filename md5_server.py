import socket
from sys import exit
import timer
from queue import Queue

from .allocator import Client_Allocator

"""
client functionality:
recieve 10 character long string which represents md5 range, using threading+multiprocessing brute-force every md5 combination. 
if desired string is found, send to server and shutdown.

server functionality:
give ranges to clients
allocate clients dynamically (oh god)
if client finds correct string, print and shut down everyone else

(attempt minimal crying)
"""

#CONSTS:
STOP_MESSAGE = 'STOP'
PORT = 8200
ADDRESS = '127.0.0.1'
BUFFER = 64
FORMAT = 'utf-8'
START = 10000000000
END = 9999999999

class Server:
    def __init__(self, port, address, start, end):
        self.port = port
        self.address = address
        self.start = start
        self.end = end
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((address, port))
        
    
    def start():
        manager = Client_Allocator()
        while True:
            self.server_socket.listen()
            manager.add_client(self.server_socket.accept())
            for client in manager.clients:
                if client.found:
                    manager.shutdown()
                    server_socket.close()
                    exit()


if __name__ == "__main__":
    server = Server(PORT, ADDRESS, START, END)
    server.start()