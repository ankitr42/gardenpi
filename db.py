from tinydb import TinyDB

from consts import PUMP_LOG
from consts import CHARGE_LOG
from consts import FAN_LOG

pumpDB = TinyDB(PUMP_LOG)
fanDB = TinyDB(FAN_LOG)
chargeDB = TinyDB(CHARGE_LOG)

def logPumpRun(entry):
    pumpDB.insert(entry)

def getLatestPumpRun():
    return pumpDB.all()[-1]

def logFanRun(entry):
    fanDB.insert(entry)

def logChargeRun(entry):
    chargeDB.insert(entry)