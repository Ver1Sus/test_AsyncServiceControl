import subprocess, re

class ServiceControl():
	def __init__(self, serviceName):
		self.serviceName = serviceName
		
	def getStatus(self):
		p = subprocess.Popen(["service", self.serviceName, "status"], stdout=subprocess.PIPE)
		out, err = p.communicate()
		res = re.findall(r'Active:.(\w*)', str(out))
		return res

	def stopService(self):
		p = subprocess.Popen(["sudo", "service", self.serviceName, "stop"], stdout=subprocess.PIPE)
		out, err = p.communicate()
		res = re.findall(r'Active:.(\w*)', str(out))
		return 0
		
	def startService(self):
		p = subprocess.Popen(["sudo", "service", self.serviceName, "start"])
		out, err = p.communicate()
		res = re.findall(r'Active:.(\w*)', str(out))
		return res