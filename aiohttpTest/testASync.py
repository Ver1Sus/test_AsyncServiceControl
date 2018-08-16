from aiohttp import web

async def handle(request):
	name = request.match_info.get('name', "Anonymous")
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
	
	
app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/echo', wshandle),
                web.get('/{name}', handle)])
				
web.run_app(app)