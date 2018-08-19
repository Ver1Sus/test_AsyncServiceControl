from views import index, test, with_name, index2, switch, switch2
from aiohttp import web
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent

def setup_routes(app):
	app.router.add_get('/', index2)
	app.router.add_post('/switch/', switch2, name='switch'),
	app.add_routes([web.get('/{name}',with_name),])
			
	setup_static_routes(app)
			
			
def setup_static_routes(app):
    app.router.add_static('/static/',
        path=PROJECT_ROOT / 'static',
		name='static')