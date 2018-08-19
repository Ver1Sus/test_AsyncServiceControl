from aiohttp import web
import asyncio, aiohttp
import aiohttp_jinja2
from switchService import ServiceControl

serviceControl = ServiceControl("python_telegramCheckInIvcBot")
serviceControl = ServiceControl("bluetooth")

ioloop = asyncio.get_event_loop()

async def index(request):
	return web.Response(text='Hello world!')
	
@aiohttp_jinja2.template('index.html')
async def index2(request):
	#return web.Response(text='Hello world2!')
	return {
			'title':'Service Control Panel',
			'description':'This is page to control the service',
			'serviceStatus':serviceControl.findStatus("status"),
			'serviceName': serviceControl.serviceName,
			'checked':'',
		}
		
	
	
async def switch(request):
	#button = request.match_info['button']
	data = await request.post()
	serviceSwitch = data['serviceSwitch']
	print(serviceSwitch)
	
	if serviceSwitch == 'on':
		print('try to start')
		serviceControl.startService()
	elif serviceSwitch == 'off':
		print('try to stop')
		serviceControl.stopService()
	elif serviceSwitch == 'restart':
		print('try to restart')
		serviceControl.restartService()
	
	print (serviceControl.getStatus())
	
	return web.HTTPFound('/')
	
async def switch2(request):
	#button = request.match_info['button']
	data = await request.post()
	serviceSwitch = data['serviceSwitch']
	print(serviceSwitch)	
		
	if serviceSwitch == 'on':
		print('try to start')
		task = [ioloop.create_task(serviceControl.startService2())]			
	elif serviceSwitch == 'off':
		print('try to stop')
		task = [ioloop.create_task(serviceControl.stopService2())]
	elif serviceSwitch == 'restart':
		print('try to restart')
		task = [ioloop.create_task(serviceControl.restartService2())]
	
	wait_tasks = asyncio.wait(task)
	#ioloop.ensure_future(task)
	#ioloop.run_until_complete(wait_tasks)
	#ioloop.close()
		
	#print (serviceControl.getStatus())
	
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