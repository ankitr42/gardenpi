import sys
import gpiozero
import time
from datetime import datetime
from tinydb import TinyDB

from consts import PUMP_RELAY_PIN
from consts import PUMP_LOG
from consts import PUMP_RUNTIME

pumpRelay = gpiozero.OutputDevice(PUMP_RELAY_PIN, active_high = False,
                                  initial_value = False)

def 

def runPump():
    pumpRelay.on()
    time.sleep(PUMP_RUNTIME) # Keep pump running for PUMP_RUNTIME seconds.
    pumpRelay.off()
    
    # Log this run
    entry = { 'timestamp': str(datetime.now().timestamp()),
                  'duration': str(PUMP_RUNTIME)}
    
    db.insertEntry(entry)
    

if __name__ == "__main__":
    runPump()
