from aiohttp import web
import asyncio, aiohttp
import aiohttp_jinja2
from switchService import ServiceControl
from syslog import syslog as printToSyslog
import testDb 
from datetime import datetime


serviceControl = ServiceControl("bluetooth")
ioloop = asyncio.get_event_loop()


@aiohttp_jinja2.template('index.html')
async def index(request):	
	printAndLog("Connect to ./index.html")
	
	#---connect to PostgreS and get status of checkBox
	postgreBase = testDb.postgreDB()
	res = asyncio.gather(postgreBase.getStatus())
	
	checked = ''
	if res:
		checked = 'checked'
	
	return {
			'title':'Service Control Panel',
			'description':'This is page to control the service',
			'serviceStatus':serviceControl.findStatus("status"),
			'serviceName': serviceControl.serviceName,
			'checked':checked,
		}

		
async def websocket_handler(request):
	##---- use websocket to update chekBox status on the Base
	ws = web.WebSocketResponse()
	await ws.prepare(request)
	
	postgreBase = testDb.postgreDB()
	
	async for msg in ws:				
		if msg.data == 'true':			
			res = asyncio.gather(postgreBase.insert('True', datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
			printAndLog("Change checkbox to True")
		elif msg.data == 'false':
			res = asyncio.gather(postgreBase.insert('False', datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
			printAndLog("Change checkbox to False")
		
	return ws

	
	
async def switch(request):
	##--- switch service - in case of post request
	data = await request.post()
	serviceSwitch = data['serviceSwitch']
	printAndLog("Get post: {}".format(serviceSwitch))
		
	if serviceSwitch == 'on':
		printAndLog('try to start')
		task = [ioloop.create_task(serviceControl.startService())]			
	elif serviceSwitch == 'off':
		printAndLog('try to stop')
		task = [ioloop.create_task(serviceControl.stopService())]
	elif serviceSwitch == 'restart':
		printAndLog('try to restart')
		task = [ioloop.create_task(serviceControl.restartService())]
	
	#--- asyncronous run the shell (start, stop, restart service)
	asyncio.wait(task)
		
	return web.HTTPFound('/')
	
			

def printAndLog(msg):
	##-- logging all in syslog
	msg = "aioHttpTest_msg: {}".format(msg)
	printToSyslog(msg)
	print(msg)
	
	