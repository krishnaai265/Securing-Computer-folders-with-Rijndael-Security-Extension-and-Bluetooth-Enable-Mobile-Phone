import threading
import sqlite3
import time
from bluetooth import *

def abc():
    def handshake():
    
            
        global entries
        global n
        global m
        entries = []
        n = []
        m = []
        
        print("performing inquiry...")

        nearby_devices = discover_devices(lookup_names = True)

        print("found %d devices" % len(nearby_devices))

        for name, addr in nearby_devices:
            print(" %s - %s" % (addr, name))
            m.append(str(addr))
            n.append(str(name))
        if "04:D1:3A:02:ED:C4" in n:         
            print("Correct mac")
        else:
            print("Wrong mac")
        
    while True:
        try:
            print("I am sleeping1")
            time.sleep(30)
            print("I am running1")
            threading.Thread(target=handshake).start()
        except Exception as e:
            print(e)
try:
    print("I am sleeping")                
    threading.Thread(target=abc).start()
    print("I am running")
except Exception as e:
    print(e)