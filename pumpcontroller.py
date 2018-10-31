#
#
#

import sys
import gpiozero
import time
from datetime import datetime
import db

from consts import PUMP_GPIO
from consts import PUMP_RUNTIME
from consts import PUMP_RUN_INTERVAL

pumpRelay = gpiozero.OutputDevice(PUMP_GPIO, active_high = False,
                                  initial_value = False)

def poll():
    lastLog = db.getLatestPumpRun()
    lastTimestamp = datetime.fromtimestamp(float(lastLog['timestamp']))
    interval = (datetime.now() - lastTimestamp).total_seconds()
    
    if (interval > consts.RUN_INTERVAL):
        runPump()

def runPump():
    pumpRelay.on()
    time.sleep(PUMP_RUNTIME) # Keep pump running for PUMP_RUNTIME seconds.
    pumpRelay.off()
    
    # Log this run
    entry = { 'timestamp': str(datetime.now().timestamp()),
                  'duration': str(PUMP_RUNTIME)}
    
    db.logPumpRun(entry)
    

if __name__ == "__main__":
    poll()