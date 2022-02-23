from . import Command

class Builder:
	commands=[]
	def __init__(self):
		pass

	def add(self, command:Command):
		self.commands.append(command)

	def build(self):
		return "#!ipxe"+"\n".join([i.code() for i in self.commands]) 
