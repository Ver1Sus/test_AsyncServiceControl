from aiohttp import web
import asyncio, aiohttp
import aiohttp_jinja2
from switchService import ServiceControl

serviceControl = ServiceControl("python_telegramCheckInIvcBot")
serviceControl = ServiceControl("bluetooth")

async def index(request):
	return web.Response(text='Hello world!')
	
@aiohttp_jinja2.template('index.html')
async def index2(request):
	#return web.Response(text='Hello world2!')
	return {
			'title':'Service Control Panel',
			'description':'This is page to control the service',
		}
		
	
async def switch(request):
	button = request.match_info['button']
	
	if button == 'on':
		print('try to start')
		serviceControl.startService()
	elif button == 'off':
		print('try to stop')
		serviceControl.stopService()
	
	print (serviceControl.getStatus())
	return web.HTTPFound('/')
	
	
async def switchPost(r):
	#response = await aiohttp.request('GET', 'http://192.168.1.127:8080/switch/off')
	response = await asyncio.sleep(1)
	return 'a'
	return web.HTTPFound('/')
	
	
	
# print('Asynchronous:')
# ioloop = asyncio.get_event_loop()
# tasks = [ioloop.create_task(switchPost(1))]
# ioloop.run_until_complete(asyncio.wait(tasks))
# ioloop.close()
	
	
	
async def test(request):
	return web.Response(text='This is Test!')
	
	
async def with_name(request):
	return web.Response(text="Hello, {}".format(request.match_info['name']))