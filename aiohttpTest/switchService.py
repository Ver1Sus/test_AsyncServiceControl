import subprocess, re

class ServiceControl():
	def __init__(self, serviceName):
		self.serviceName = serviceName
		
	def getStatus(self):
		p = subprocess.Popen(["service", self.serviceName, "status"], stdout=subprocess.PIPE)
		return self.findStatus(p)

	def stopService(self):
		p = subprocess.Popen(["sudo", "service", self.serviceName, "stop"], stdout=subprocess.PIPE)
		return self.findStatus(p)
		
	def startService(self):
		p = subprocess.Popen(["sudo", "service", self.serviceName, "start"])
		return self.findStatus(p)
		
	def restartService(self):
		p = subprocess.Popen(["sudo", "service", self.serviceName, "restart"])
		return self.findStatus(p)
		
	def findStatus(self, process):
		out, err = process.communicate()
		res = re.findall(r'Active:.(\w*)', str(out))
		return res