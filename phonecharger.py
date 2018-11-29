#
#
#
import gpiozero
import time

chargeRelay = gpiozero.OutputDevice(1, active_high = False,
                                  initial_value = False)

while True:
	# Charge it for 3 hours
	chargeRelay.on()
	time.sleep(10800)
	# Switch off power for 20 minutes
	chargeRelay.off()
	time.sleep(1200)
