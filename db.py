from tinydb import TinyDB
from threading import RLock

from consts import PUMP_LOG
from consts import CHARGE_LOG
from consts import FAN_LOG
from consts import SERVICE_LOG

from datetime import datetime

pumpDB = TinyDB(PUMP_LOG)
fanDB = TinyDB(FAN_LOG)
chargeDB = TinyDB(CHARGE_LOG)
serviceDB = TinyDB(SERVICE_LOG)

rlock = RLock()

def logPumpRun(entry):
	with rlock:
		pumpDB.insert(entry)

def getLatestPumpRun():
	with rlock:
		if (len(pumpDB.all()) > 0):
			return pumpDB.all()[-1]
		else:
			return None

def logFanRun(entry):
	with rlock:
		fanDB.insert(entry)

def logChargeRun(entry):
	with rlock:
		chargeDB.insert(entry)