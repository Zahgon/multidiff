import sys
import binascii
import re
class StdinController:
	def __init__(self, model, informat):
		if informat not in ['utf8', 'hex']:
			raise NotImplementedError('"{}" is not a valid input format for this controller'.format(informat))
		self.informat = informat
		self.model = model
		self.spaceregex = re.compile(r'\s+')
	def read_lines(self):
		pass
