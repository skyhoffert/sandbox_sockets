# Sky Hoffert
# April 9, 2018
# server.py
# Sandbox server for transferring data

import pickle
import utils
import signal
import sys
import threading
import logging

# function to handle the ctrl-c signal
exit_flag = False
def signal_handler(signal, frame):
    exit_flag = True
# set up the signal catcher
signal.signal(signal.SIGINT, signal_handler)

# create the logger
logger = logging.getLogger()
logger.setLevel( logging.DEBUG )

# set up the server
tx = utils.server()
tx.connect( '127.0.0.1', 5005 )
tx.t_accept_client()

# thread to recieve data
def t_recv():    
    # continuously wait for recieve messages
    while True:
        # check for exit flag
        if exit_flag: break
        
        # get the data
        data = tx.recv(1024)
        if not data: break
        
        # unpickle the tlm data
        data = pickle.loads(data)
        
        # print some updates to the user
        print( '[ Server ] Received: {}'.format(data) )
        sys.stdout.flush()

# spin up the rx thread
rx_thread = threading.Thread( target=t_recv )
rx_thread.start()
        
# main program loop!
# handle commands from the user
command = ''
while 'quit' not in command.lower():
    command = input()
    
    if exit_flag: break
    
    # log
    print( '[ Server ] Command Entered: {}'.format(command) )
    
    # break input into tokens
    tokens = command.split(' ')
    
    if 'test' in tokens[0]:
        if len(tokens) > 1:
            tx.send( pickle.dumps( tokens[1] ) )
        else:
            tx.send( pickle.dumps( 'exit' ) )

exit_flag = True

# join threads
rx_thread.join()

# close the connection
tx.close()










