class Command:
	def __init__(self, *args):
		self.args=args


	def code(self):
		return "echo Base command"


class Chain(Command):

	def code(self):
		return f"chain {self.args[0]}"

class Echo(Command):
	def code(self):
		return f"echo {self.args[0]}"


class Item(Command):
	def function(self, fn):
		self.func=fn

	def func(self):
		return [Echo("No function!")]

	def func_data(self):
		return f":{self.func.__name__}"+"\n"+'\n'.join([i.code() for i in self.func()])

	def code(self):
		return f'item {self.func.__name__} {self.args[0]}'



class Menu(Command):
	items=[]
	def item(self, item:Item):
		self.items.append(item)

	def code(self):
		x="menu "+self.args[0]+"\n"
		x+='\n'.join([item.code() for item in self.items])+"\nchoose item\ngoto ${item}\n" 
		x+='\n'.join([item.func_data() for item in self.items])+"\n"
		return x


class Loader(Command):
	def __init__(self, *args):
		self.args=[]
		self.initrds=[]
		self.kernel_path=""

	def initrd(self, path):
		self.initrds.append(path)

	def kernel(self, path):
		self.kernel_path=path

	def code(self):
		return f"kernel {self.kernel_path} "+" ".join([f"initrd={i.split("/")[-1]}" for i in self.initrds])+"\n"+'\n'.join([f"initrd {i}" for i in self.initrds])+"\nboot\n"
