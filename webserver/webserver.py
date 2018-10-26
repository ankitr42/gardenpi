import web

urls = ('/', 'index', '/logs', 'logs')
html = web.template.render('webtemplates')
json = web.template.render('../cache')

class index:
    def GET(self):
        return html.index()

class logs:
	def GET(self):
		return json.logs()

def startServer():
    app = web.application(urls, globals())
    app.run()
    
if __name__ == "__main__":
    startServer()
