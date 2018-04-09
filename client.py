# Sky Hoffert
# April 9, 2018
# client.py
# Sandbox client for transferring data

import pickle
import utils
import signal
import random
import time
import threading
import sys

# function to handle the ctrl-c signal
exit_flag = False
def signal_handler(signal, frame):
    exit_flag = True
# set up the signal catcher
signal.signal(signal.SIGINT, signal_handler)

# set up reciever client
rx = utils.client()
rx.connect( '127.0.0.1', 5005 )

# thread the handles receiving data
def t_recv():
    while True:
        # check for exit flag
        if exit_flag: break
        
        # blocking call to wait for data
        data = rx.recv( 1024 )
        
        # attempt to unpickle the data (could be corrupted)
        try:    data = pickle.loads( data )
        except: break
        
        print( '[ Client ] Received data: {}'.format( data ) )
        sys.stdout.flush()

# spin up the receive thread
rx_thread = threading.Thread( target=t_recv )
rx_thread.start()
    
# start the telemetry thread
while True:
    # first check for the exit flag
    if exit_flag:
        break
    
    # next, form some data to be sent
    data = ( random.random(), random.random(), random.random() )
    
    # try to send the pickled data
    if not rx.send( pickle.dumps(data) ):
        break
    
    # manually sleep for one second
    time.sleep( 1 )

# join threads
rx_thread.join()

# if the telemetry loop was broken, close the connection
rx.close()












