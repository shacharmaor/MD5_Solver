from .client import Client

class Client_Allocator:
    """
    keep track of existing clients, add and remove clients if necessary
    """

    def __init__(self):
        self.clients = []
        self.threads = []
    
    def add_client(conn, addr):
        new_client = Client(addr, conn)
        self.clients.add(new_client)
        self.threads.add(client.thread)
        client.thread.start()

    def remove_client(client):
        client.shutdown()
        self.clients.remove(client)
