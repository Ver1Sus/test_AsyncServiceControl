import subprocess, re
import asyncio 

class ServiceControl():
	def __init__(self, serviceName):
		self.serviceName = serviceName

	def getStatus(self):
		return self.findStatus("status")

	def stopService(self):
		return self.findStatus("stop")
		
	def startService(self):
		return self.findStatus("start")
		
	def restartService(self):
		return self.findStatus("restart")
		
	def findStatus(self, command):
		p = subprocess.Popen(["sudo", "service", self.serviceName, command], stdout=subprocess.PIPE)
		out, err = p.communicate()
		res = re.findall(r'Active:.(\w*)', str(out))
		return res
		
	async def startService2(self):
		await self.runShell("start")
		# p = await asyncio.create_subprocess_shell("sudo service {} start".format(self.serviceName), stdout=asyncio.subprocess.PIPE)
		
	async def stopService2(self):
		await self.runShell("stop")
		
	async def restartService2(self):
		await self.runShell("restart")
		
	async def runShell(self, command):
		await asyncio.create_subprocess_shell("sudo service {} {}".format(self.serviceName, command), stdout=asyncio.subprocess.PIPE)
		