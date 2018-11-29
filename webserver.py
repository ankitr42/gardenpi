import web
import re
import os
import base64
import db
import json

urls = ('/', 'Index', '/logs/(.*)/(.*)', 'Logs', '/login', 'Login', '/operation/(.*)', 'Operations')
html = web.template.render('webtemplates')
logs = web.template.render('cache')

users = (
    ('admin','admin'),
)

class Index:
	def GET(self):
		auth = web.ctx.env.get('HTTP_AUTHORIZATION')
		if auth is None or validateUser(auth) is False:
			web.seeother('/login')
		else:
			temp = os.popen("vcgencmd measure_temp").readline().replace('temp=', '')
			return html.index(temp)

class Logs:
	def GET(self, logcat, since):
		auth = web.ctx.env.get('HTTP_AUTHORIZATION')
		if auth is None or validateUser(auth) is False:
			web.seeother('/login')
		elif(logcat == 'pump'):
			if (since == 'all'):
				return logs.pumplog()
			else:
				return json.dumps(db.getRecentPumpRuns())
		elif(logcat == 'thermal'):
			if (since == 'all'):
				return logs.fanlog()
			else:
				return json.dumps(db.getRecentFanRuns())
		elif(logcat == 'charge'):
			if (since == 'all'):
				return logs.chargelog()
			else:
				return json.dumps(db.getRecentChargeRuns())

class Login:
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        authreq = False
        if auth is None:
            authreq = True
        else:
			if validateUser(auth):
				raise web.seeother('/')
			else:
				authreq = True
        if authreq:
            web.header('WWW-Authenticate','Basic realm="WaterPI"')
            web.ctx.status = '401 Unauthorized'
            return
            
class Operations:
	def GET(self, operation):
		auth = web.ctx.env.get('HTTP_AUTHORIZATION')
		if auth is None or validateUser(auth) is False:
			web.seeother('/login')
		elif(operation == 'runpump'):
			os.popen("python3 pumpcontroller.py runnow &")
			return "Success"
			
def validateUser(auth):
	auth = re.sub('^Basic ','',auth)
	username,password = base64.decodestring(auth).split(':')
	if (username, password) in users:
		return True
	else:
		return False

def startServer():
    app = web.application(urls, globals())
    app.run()
    
if __name__ == "__main__":
    startServer()
