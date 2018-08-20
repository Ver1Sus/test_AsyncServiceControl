from aiohttp import web
import asyncio
from routes import setup_routes, printAndLog
import aiohttp_jinja2
import jinja2

app = web.Application()

aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('templatesModule', 'templates'))

setup_routes(app)
printAndLog("Start")
web.run_app(app)


