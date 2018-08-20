from aiohttp import web
import asyncio, aiohttp
import aiohttp_jinja2
from switchService import ServiceControl
from syslog import syslog as printToSyslog
import testDb


serviceControl = ServiceControl("bluetooth")
ioloop = asyncio.get_event_loop()

async def index(request):
	return web.Response(text='Hello world!')
	
	
def got_result(future):
	print(future.result())

@aiohttp_jinja2.template('index.html')
async def index2(request):

	# ioloop = asyncio.get_event_loop()
	res = ''
	# res = asyncio.ensure_future(testDb.getStatus())
	# print (res)
	
	res = asyncio.gather(testDb.getStatus())
	
	# future1 = asyncio.Future()
	# future1.add_done_callback(got_result)
	# ioloop.run_until_complete(asyncio.wait(testDb.func_normal(future1)))
	# ioloop.close()
	
	# ioloop = asyncio.get_event_loop()
	# res, res2 = ioloop.run_until_complete(testDb.getStatus())
	
	
	
	res = (testDb.getStatus())
	print(res)
	# res = await ioloop.run_fetch(testDb.getStatus())
	# print (res)
	
	checked = ''
	if res:
		print ('a')
		checked = 'checked'
	
	printAndLog("User connect")
	#return web.Response(text='Hello world2!')
	return {
			'title':'Service Control Panel',
			'description':'This is page to control the service',
			'serviceStatus':serviceControl.findStatus("status"),
			'serviceName': serviceControl.serviceName,
			'checked':checked,
		}

async def websocket_handler(request):
	# session = aiohttp.ClientSession()
	# ws = await session.ws_connect('http://5.166.41.52:50001/')

	ws = web.WebSocketResponse()
	await ws.prepare(request)
	async for msg in ws:
		print(msg.type)
		print(msg.data)
		if msg.data == "OFF":
			task = [ioloop.create_task(serviceControl.stopService2())]	
			wait_tasks = asyncio.wait(task)
			status = (serviceControl.getStatus())
			print(status)
		
			# await ws.send_str(status);
		elif msg.data == "ON":
			task = [ioloop.create_task(serviceControl.startService2())]	
			wait_tasks = asyncio.wait(task)
			status = (serviceControl.getStatus())
			print(status)
			
		
			
		# if msg.type == WSMsgType.TEXT:
		#     if msg.data == 'close':
		#         await ws.close()
		#     else:
		#         ws.send_str(msg.data + '/answer')
		# elif msg.type == WSMsgType.ERROR:
		#     print('ws connection closed with exception %s' %
		#           ws.exception())

	print('websocket connection closed')

	return ws

	
	

	
async def switch2(request):
	
	#button = request.match_info['button']
	data = await request.post()
	serviceSwitch = data['serviceSwitch']
	print(serviceSwitch)	
		
	if serviceSwitch == 'on':
		printAndLog('try to start')
		task = [ioloop.create_task(serviceControl.startService2())]			
	elif serviceSwitch == 'off':
		printAndLog('try to stop')
		task = [ioloop.create_task(serviceControl.stopService2())]
	elif serviceSwitch == 'restart':
		printAndLog('try to restart')
		task = [ioloop.create_task(serviceControl.restartService2())]
	
	asyncio.wait(task)
	
	#wait_tasks = asyncio.gather(task[0])
	#print (wait_tasks)
	#ioloop.ensure_future(task)
	#ioloop.run_until_complete(wait_tasks)
	#ioloop.close()
		
	# print ("as",serviceControl.getStatus())
	
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
	
	

def printAndLog(msg):
	printToSyslog(msg)
	print(msg)
	
	
async def test(request):
	return web.Response(text='This is Test!')
	
	
async def with_name(request):
	return web.Response(text="Hello, {}".format(request.match_info['name']))