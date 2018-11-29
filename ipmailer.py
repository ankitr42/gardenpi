import smtplib
import json
import urllib.request

config = {}
ip = urllib.request.urlopen("https://api.ipify.org").read().decode("utf-8") 

try:
	with open("../config.json", "r") as configJson:
		config = json.load(configJson)
finally:
	if ("wanip" in config) is False or config["wanip"] != ip:
		#Update IP
		urllib.request.urlopen("https://www.randomgarage.com/postip.php?ip=" + ip)
		config["wanip"] = ip

	with open("../config.json", "w") as configJson:
		json.dump(fp = configJson, obj = config)
