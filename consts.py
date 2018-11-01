PUMP_LOG = "cache/pumplog.json"
CHARGE_LOG = "cache/chargelog.json"
FAN_LOG = "cache/fanlog.json"
SYSCONFIG = "cache/config.json"
SERVICE_LOG = "cache/servicelog.json"

PUMP_GPIO = 3
PUMP_RUNTIME = 15
PUMP_RUN_INTERVAL = 86000 # Slightly less than 1 day

FAN_GPIO = 4
TEMP_POLL_INTERVAL = 60
TEMP_UPPER_LIMIT = 55
TEMP_COOLDOWN = 45

CHARGER_GPIO = 2
CHARGER_RUNTIME = 10800 # 3 Hours
CHARGER_OFFTIME = 10800 # 3 Hours