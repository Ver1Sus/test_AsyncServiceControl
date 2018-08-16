from aiohttp import web
from routes import setup_routes
from settings import config
import aiohttp_jinja2
import jinja2

app = web.Application()
app['config'] = config

# env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'),
    # autoescape=jinja2.select_autoescape(['html', 'xml']),
	# )
	
	
# env = jinja2.Environment(loader=jinja2.PackageLoader('aiohttpTest', 'templates'))
# template = env.get_template('index.html')	

#--- here error when try search package (module) 'aiohttpTest'. Add inner module to fix it
aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('templatesModule', 'templates'))

setup_routes(app)
#print (config)
web.run_app(app)
