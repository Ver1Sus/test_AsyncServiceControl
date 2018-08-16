from views import index, test, with_name, index2, switch, switchPost, switch2
from aiohttp import web
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent

def setup_routes(app):
	app.router.add_get('/', index2)
	app.router.add_post('/switch/{button}', switch, name='switch'),
	#app.router.add_get('/off', switchPost, name='switchPost'),
	app.router.add_post('/switch/{button}', switch, name='switchPost'),
	app.router.add_post('/switch2/', switch2, name='switch2'),
	app.add_routes([web.get('/test', test),
			web.get('/{name}',with_name)])
			
	setup_static_routes(app)
			
			
def setup_static_routes(app):
    app.router.add_static('/static/',
        path=PROJECT_ROOT / 'static',
		name='static')