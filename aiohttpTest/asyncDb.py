import asyncio
import aiopg
			
class postgreDB():
	def __init__(self):
		from settings import config
		config = config['postgres']
		self.dsn = dsn = 'dbname={} user={} password={} host={}'.format(config['database'], config['user'], config['password'], config['host'])

	async def getStatus(self):
		##-- get last status of checkbox 
		pool = await aiopg.create_pool(self.dsn)
		async with pool.acquire() as conn:
			async with conn.cursor() as cur:
				await cur.execute("SELECT * from test_table order by test_table.click_time desc limit 1")
				async for row in cur:
					print(row[0])
					self.statusActive = row[0]
					# print (row)
					return(row)		

	async def insert(self, check, click_time):
		#-- update status of checkbox
		pool = await aiopg.create_pool(self.dsn)
		async with pool.acquire() as conn:
			async with conn.cursor() as cur:
				await cur.execute("INSERT INTO test_table VALUES({}, '{}')".format(check, str(click_time)))
	
	
	
	
			