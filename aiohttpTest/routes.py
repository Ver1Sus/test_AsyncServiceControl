from views import index, switch, websocket_handler, printAndLog
from aiohttp import web
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent

def setup_routes(app):
	app.router.add_get('/', index)
	app.router.add_get('/ws', websocket_handler, name='sockets')
	app.router.add_post('/switch/', switch, name='switch')
			
	setup_static_routes(app)
			
			
def setup_static_routes(app):
    app.router.add_static('/static/',
        path=PROJECT_ROOT / 'static',
		name='static')