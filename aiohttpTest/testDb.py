import asyncio
import aiopg
from settings import config

config = config['postgres']
dsn = 'dbname={} user={} password={} host={}'.format(config['database'], config['user'], config['password'], config['host'])

async def getStatus():
	pool = await aiopg.create_pool(dsn)
	async with pool.acquire() as conn:
		async with conn.cursor() as cur:
			await cur.execute("SELECT * from test_table order by test_table.click_time desc limit 1")
			async for row in cur:
				print (row)
				return(row)		

			

async def insert(check, click_time):
	pool = await aiopg.create_pool(dsn)
	async with pool.acquire() as conn:
		async with conn.cursor() as cur:
			await cur.execute("INSERT INTO test_table VALUES({}, '{}')".format(check, str(click_time)))
	
			
# loop = asyncio.get_event_loop()
# loop.run_until_complete(go())