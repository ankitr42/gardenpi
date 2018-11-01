#
#
#

import os
import time
import gpiozero
import db
import threading

from datetime import datetime
from consts import FAN_GPIO
from consts import TEMP_POLL_INTERVAL
from consts import TEMP_UPPER_LIMIT
from consts import TEMP_COOLDOWN

fanRelay = gpiozero.OutputDevice(FAN_GPIO, active_high = False,
                                  initial_value = False)

def heartbeat():
	entry = { 'timestamp': str(datetime.now().timestamp()),
		'event': 'Heartbeat', 'Temp': 'Dummy'}
	db.logFanRun(entry)
	threading.Timer(600, heartbeat).start()

def measure_temp():
        temp = os.popen('vcgencmd measure_temp').readline()
        return temp[5:-3]

heartbeat()

fanState = False
while True:
	currTemp = float(measure_temp())
	if (currTemp > TEMP_UPPER_LIMIT and fanState is False):
		fanRelay.on()
		fanState = True
		# Log this run
		entry = { 'timestamp': str(datetime.now().timestamp()),
			'event': 'Switch On', 'Temp': str(currTemp)}
		db.logFanRun(entry)

	elif (currTemp < TEMP_COOLDOWN and fanState is True):
		fanRelay.off()
		fanState = False
		entry = { 'timestamp': str(datetime.now().timestamp()),
			'event': 'Switch Off', 'Temp': str(currTemp)}
	
	time.sleep(TEMP_POLL_INTERVAL)
