# Server AioHTTP to async control service on the server

Turn the service using the web-interface.
Using asyncio to send command on server asyncronous.

Using PostgreSQL to save the status of checkox-active. If it off - you can't switch service.

To get all requirenments, run:
	<b>source env2/bin/activate</b>
To deactivate virtualenv, run:
	<b>deactivate</b>
	
Requirenments:
	- python 3.5
	- aiohttp
	- aiopg
	- aiohttp_jinja2
	- jinja2
	- subprocess
	- yaml