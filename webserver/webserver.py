import web
import re
import os
import base64

urls = ('/', 'Index', '/logs', 'Logs', '/login', 'Login')
html = web.template.render('webtemplates')
json = web.template.render('../cache')
users = (
    ('admin','admin'),
    ('dummy','dummy67171412314681465746844')
)

class Index:
	def GET(self):
		if web.ctx.env.get('HTTP_AUTHORIZATION') is None:
			web.seeother('/login')
		else:
			temp = os.popen("vcgencmd measure_temp").readline().replace('temp=', '')
			return html.index(temp)

class Logs:
	def GET(self):
		if web.ctx.env.get('HTTP_AUTHORIZATION') is None:
			web.seeother('/login')
		else:
			return json.logs()

class Login:
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        authreq = False
        if auth is None:
            authreq = True
        else:
            auth = re.sub('^Basic ','',auth)
            username,password = base64.decodestring(auth).split(':')
            if (username,password) in users:
                raise web.seeother('/')
            else:
                authreq = True
        if authreq:
            web.header('WWW-Authenticate','Basic realm="WaterPI"')
            web.ctx.status = '401 Unauthorized'
            return

def startServer():
    app = web.application(urls, globals())
    app.run()
    
if __name__ == "__main__":
    startServer()
