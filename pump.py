import sys
import gpiozero
import time
from datetime import datetime

import db

from consts import PUMP_RELAY_PIN
from consts import LOG_FILE_PATH
from consts import PUMP_RUNTIME

pumpRelay = gpiozero.OutputDevice(PUMP_RELAY_PIN, active_high = False,
                                  initial_value = False)

def runPump():
    pumpRelay.on()
    time.sleep(PUMP_RUNTIME) # Keep pump running for PUMP_RUNTIME seconds.
    pumpRelay.off()
    
    # Log this run
    # datetime.utcnow().strftime("%d-%b-%y %I:%M%p")
    entry = { 'timestamp': str(datetime.now().timestamp()),
                  'duration': str(PUMP_RUNTIME)}
    
    db.insertEntry(entry)
    

if __name__ == "__main__":
    runPump()
