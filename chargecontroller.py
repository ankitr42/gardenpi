#
#
#

import os
import time
import gpiozero
import db
import threading
from datetime import datetime

from consts import CHARGER_GPIO
from consts import CHARGER_RUNTIME
from consts import CHARGER_OFFTIME

chargeRelay = gpiozero.OutputDevice(CHARGER_GPIO, active_high = True,
                                  initial_value = False)
                                  
def heartbeat():
	entry = { 'timestamp': str(datetime.now().timestamp()),
                'event': 'Heartbeat'}
	db.logChargeRun(entry)
	threading.Timer(600, heartbeat).start()

heartbeat()

chargeState = False
while True:
    # Start charging
    chargeRelay.on()
    entry = { 'timestamp': str(datetime.now().timestamp()),
                'event': 'Switch On'}
    db.logChargeRun(entry)

    time.sleep(CHARGER_RUNTIME)

    # Stop charging charging
    chargerRelay.off()
    entry = { 'timestamp': str(datetime.now().timestamp()),
                'event': 'Switch Off'}
    db.logChargeRun(entry)

    time.sleep(CHARGER_OFFTIME)