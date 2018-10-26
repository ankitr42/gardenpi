import web
import re
import base64

urls = ('/', 'Index', '/logs', 'Logs', '/login', 'Login')
html = web.template.render('webtemplates')
json = web.template.render('../cache')
users = ( ('admin', 'admin') )

class Index:
	def GET(self):
		if web.ctx.env.get('HTTP_AUTHORIZATION') is None:
			web.seeother('/login')
		else:
			html.index()

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
            web.header('WWW-Authenticate','Basic realm="Auth example"')
            web.ctx.status = '401 Unauthorized'
            return

def startServer():
    app = web.application(urls, globals())
    app.run()
    
if __name__ == "__main__":
    startServer()
