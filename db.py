from tinydb import TinyDB, Query
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
		pumpRun = Query()
		if (len(pumpDB.search(pumpRun.event == 'Pump Run')) > 0):
			return pumpDB.all()[-1]
		else:
			return None

def logFanRun(entry):
	with rlock:
		fanDB.insert(entry)

def logChargeRun(entry):
	with rlock:
		chargeDB.insert(entry)

def getRecentPumpRuns():
	logs = pumpDB.all()
	if (len(logs) > 25):
		return logs[-25]
	else:
		return logs

def getRecentFanRuns():
	logs = fanDB.all()
	if (len(logs) > 25):
		return logs[-25]
	else:
		return logs

def getRecentChargeRuns():
	logs = chargeDB.all()
	if (len(logs) > 25):
		return logs[-25]
	else:
		return logs
