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
    
    if (interval > consts.SECONDS_IN_DAY):
        pump.runPump()
   
    threading.Timer(consts.SECONDS_IN_DAY, runPumpTimer).start()

if __name__ == "__main__":
    runPumpTimer()
