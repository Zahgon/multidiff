from multidiff.Ansi import Ansi
import binascii
import html
class Render():
	def __init__(self, encoder='hexdump', color='ansi'):
		'''Configure the output encoding and coloring method of this rendering object'''
		if   color == 'ansi':
			self.highligther = ansi_colored
		elif color == 'html':
			self.highligther = html_colored
		if   encoder == 'hexdump':
			self.encoder = HexdumpEncoder
		elif encoder == 'hex':
			self.encoder = HexEncoder
		elif encoder == 'utf8':
			self.encoder = Utf8Encoder
			
	def render(self, model, diff):
		pass
	def dumps(self, model):
		'''Dump all diffs in a model. Mostly good for debugging'''
		pass
class Utf8Encoder():
	'''A string (utf8) encoder for the data'''
	def __init__(self, highligther):
		self.highligther = highligther
		self.output = ''
	def append(self, data, color):
		pass
	
	def final(self):
		pass
class HexEncoder():
	'''A hex encoder for the data'''
	def __init__(self, highligther):
		self.highligther = highligther
		self.output = ''
	def append(self, data, color):
		pass
	
	def final(self):
		pass
class HexdumpEncoder():
	'''A hexdump encoder for the data'''
	def __init__(self, highligther):
		self.highligther = highligther
		self.body = ''
		self.addr = 0
		self.rowlen = 0
		self.hexrow = ''
		self.skipspace = False
		self.asciirow = ''
	def append(self, data, color):
		pass
	def _append(self, data, color):
		pass
	def _newrow(self):
		pass
	def _add_hex_space(self):
		pass
	def final(self):
		pass
def ansi_colored(string, op):
	pass
def html_colored(string, op):
	pass
