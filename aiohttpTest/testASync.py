from aiohttp import web
import aiohttp
import asyncio





###----------------------- ZONE OPEN --------------
import asyncio
import subprocess, re

async def foo():
	print('foo start')
	p = await asyncio.create_subprocess_shell("sudo service bluetooth start", stdout=asyncio.subprocess.PIPE)
	print(p)
	print('Foo end')
	
# def proc():
	# p = await 	asyncio.create_subprocess_exec("sudo service bluetooth status")
	# # p = subprocess.Popen(["sudo", "service", "bluetooth", "status"], stdout=subprocess.PIPE)
	# out, err = p.communicate()
	# res = re.findall(r'Active:.(\w*)', str(out))

async def bar():
	print('bar start')
	await asyncio.sleep(0)
	print('bar end')
	
ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
tasks = [ioloop.create_task(foo()) ]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()


###----------------------- ZONE CLOSE --------------











async def handle(request):
	name = request.match_info.get('name', "Anonymous")
	text = "Hello, " + name
	return web.Response(text=text)
	
	
async def post_handle(request):
	name = request.match_info.post('name', "Anonymous")
	text = "Hello, " + name
	return web.Response(text=text)
	
async def wshandle(request):
	print ("tes2t")
	ws = web.WebSocketResponse()	
	await ws.prepare(request)
	
	print ("test")
	print(ws)
	async for msg in ws:
		print (msg)
		if msg.type == web.WSMsgType.text:
			await ws.send_str("Hello, {}".format(msg.data))
		elif msg.type == web.WSMsgType.binary:
			await ws.send_bytes(msg.data)
		elif msg.type == web.WSMsgType.close:
			break
	return ws
	
import aiohttp_jinja2, jinja2

@aiohttp_jinja2.template('index2.html')
async def index2(request):
	#return web.Response(text='Hello world2!')
	return {
			'title':'Service Control Panel',
			'description':'This is page to control the service',
			'serviceStatus':'what',
			'serviceName': 'yes',
			'checked':'',
		}

	
app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('templatesModule', 'templates'))
app.add_routes([web.get('/', handle),
                web.post('/post', post_handle),
                web.get('/a', index2, name='switch'),
                web.get('/{name}', handle)])
				
#web.run_app(app)



###----------------------- ZONE OPEN --------------
print("start")
async def hello(url):
	async with aiohttp.ClientSession() as session:
		async with session.get('http://httpbin.org/get') as resp:
			print(resp.status)
			print(await resp.text())
	
	
loop = asyncio.get_event_loop()
#loop.run_until_complete(hello("http://httpbin.org/headers"))


###----------------------- ZONE CLOSE --------------






