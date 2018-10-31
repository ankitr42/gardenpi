import pump
import threading
import time
import db
import consts
from datetime import datetime

def runPumpTimer():
    lastLog = db.getLatestEntry()
    lastTimestamp = datetime.fromtimestamp(float(lastLog['timestamp']))
    interval = (datetime.now() - lastTimestamp).total_seconds()
    
    if (interval > consts.RUN_INTERVAL):
        pump.runPump()
   
    threading.Timer(consts.RUN_INTERVAL, runPumpTimer).start()

if __name__ == "__main__":
    runPumpTimer()
