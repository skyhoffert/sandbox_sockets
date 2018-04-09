# Sky Hoffert
# April 9, 2018
# utils.py
# utilities for server communication

import socket

##############################################################################################################
class server():
    '''Basic server for a connection.'''
    
    # constructor
    def __init__(self):
        self.sock        = None
        self.connection  = None
        self.client_addr = None
        
    # connect - bind to a given ip, port combo. Listen for connections
    #   @param ip, ip address
    #   @param port, port for connection
    def connect(self, ip, port):
        self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.sock.bind( (ip, port) )
        self.sock.listen( 1 )
    
    # t_accept_client - wait for a client to connect to this server. Can be run as a thread
    def t_accept_client(self):
        self.connection, self.client_addr = self.sock.accept()
    
    # is_client_connected - returns True if a client has connected
    def is_client_connected(self):
        return self.connection is not None
        
    # close - close the client and socket connections
    def close(self):
        self.connection.close()
        self.sock.close()
    
    # send - send a given message
    #   @param message, message to be sent
    def send(self, message):
        if self.connection is None: return
        self.connection.send( message )
    
    # recv - receive data
    #   @param buffer_size, size of the receive buffer
    def recv(self, buffer_size):
        if self.connection is None: return
        
        # try to receive
        try:    val = self.connection.recv( buffer_size )
        except: val = False
        
        return val

##############################################################################################################
class client():
    '''Basic Client for a connection.'''
    
    # constructor
    def __init__(self):
        self.sock = None
        
    # connect - connect to a given ip, port combo
    #   @param ip, ip address
    #   @param port, port for connection
    def connect(self, ip, port):
        self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.sock.connect( (ip, port) )
        
    # close - close the socket connection
    def close(self):
        if self.sock is None: return
        self.sock.close()
    
    # send - send a given message
    #   @param message, message to be sent
    def send(self, message):
        if self.sock is None: return
        try:
            self.sock.send( message )
            return True
        except:
            return False
    
    # recv - receives data
    #   @param buffer_size, size of the receive buffer
    def recv(self, buffer_size):
        if self.sock is None: return
        return self.sock.recv( buffer_size )