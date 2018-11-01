#
#
#

import sys
import gpiozero
import time
from datetime import datetime
import db
import threading

from consts import PUMP_GPIO
from consts import PUMP_RUNTIME
from consts import PUMP_RUN_INTERVAL

pumpRelay = gpiozero.OutputDevice(PUMP_GPIO, active_high = False,
                                  initial_value = False)

def poll():
    lastLog = db.getLatestPumpRun()
    interval = 0

    if (lastLog is not None):
        lastTimestamp = datetime.fromtimestamp(float(lastLog['timestamp']))
        interval = (datetime.now() - lastTimestamp).total_seconds()
    else:
        interval = PUMP_RUN_INTERVAL + 1
    
    if (interval > PUMP_RUN_INTERVAL):
        runPump()

def runPump():
    pumpRelay.on()
    time.sleep(PUMP_RUNTIME) # Keep pump running for PUMP_RUNTIME seconds.
    pumpRelay.off()
    
    # Log this run
    entry = { 'timestamp': str(datetime.now().timestamp()),
                  'event': 'Pump Run', 'duration': str(PUMP_RUNTIME)}
    
    db.logPumpRun(entry)

def heartbeat():
    entry = { 'timestamp': str(datetime.now().timestamp()),
                  'event': 'Heartbeat', 'duration': '1'}
    
    db.logPumpRun(entry)
    # threading.Timer(600, heartbeat).start() - Handled by crontab
    
if __name__ == "__main__":
	if (len(sys.argv) == 2 and sys.argv[1] == 'runnow'):
		runPump()
	else:
		heartbeat()
		poll()
