import socket
import threading
import time
from .player import Player
from .game import Game
from queue import Queue

class Server(object):
    PLAYERS=8
    def __int__(self):
        self.connection_queue=[]


    def player_thread(self,conn,player):
        """
        handles in game communication betweeen clients
        :param conn: connection object
        :param ip: str
        :param name: str
        :return:None
        """
        while True:
            try:

            except Exception as e:
                print(f"[EXCEPTION] {player.get_name()} disconnected",e)

    def handle_queue(self,player):
        """
        adds player to queue and creates new game if enough players
        :param player:
        :return:
        """
        self.connection_queue.append(player)
        if len(self.connection_queue)>=self.PLAYERS:
            game=Game(self.connection_queue)



    def authentication(self,conn, addr):
        """
        authentication here
        :param conn:
        :param addr:
        :return:
        """

        try:
            data = conn.recv(16)
            name = str(data.decode())
            if not name:
                raise Exception("No name received")
            conn.sendall("1".encode()) #if the exception isn't raise say that this was successful

            player=Player(addr,name)
            threading.Thread(target=self.player_thread, args=(conn, player))
        except Exception as e:
            print("[EXCEPTION]", e)
            conn.close()


    def connection_thread(self):
        server = ""
        port = 5555
    #AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((server, port)) # is used to associate the socket with a specific network interface and port number
        except socket.error as e:
            str(e)

        s.listen()
        print("Waiting for a connection. Server Started")
        #if connection found w8ing for authentication
        while True:
            conn, adr = s.accept()#returns a new socket object representing the connection and a tuple holding the address of the client
            print("[CONNECT] New cnnection")
            self.authentication(conn, adr)


if __name__ == "__main__":
    s=Server()
    threading.Thread(target=s.connection_thread)
