import subprocess, re
import asyncio 

class ServiceControl():
	def __init__(self, serviceName):
		self.serviceName = serviceName
				
	def findStatus(self, command):
		##-- syncronous return the status
		p = subprocess.Popen(["sudo", "service", self.serviceName, command], stdout=subprocess.PIPE)
		out, err = p.communicate()
		res = re.findall(r'Active:.(\w*)', str(out))
		return res
		
	async def startService(self):
		data = await self.runShell("start")
		
	async def stopService(self):
		await self.runShell("stop")
		
	async def restartService(self):
		await self.runShell("restart")
		
	async def runShell(self, command):
		p = await asyncio.create_subprocess_shell("sudo service {0} {1}; sudo service {0} status;".format(self.serviceName, command), stdout=asyncio.subprocess.PIPE)
		for i in range(10):
			data = await p.stdout.readline()
			if 'Active:' in str(data):
				data = re.findall(r'Active:.(\w*)', str(data))
				break
		print(data)
		
	async def getStatus2(self):
		p = await asyncio.create_subprocess_shell("sudo service {} status".format(self.serviceName), stdout=asyncio.subprocess.PIPE)

		##--- get status of service in first 10 line
		for i in range(10):
			data = await p.stdout.readline()
			if 'Active:' in str(data):
				data = re.findall(r'Active:.(\w*)', str(data))
				break
		
		return(data)