import os
import binascii
import re
class FileController:
	def __init__(self, model, informat):
		if informat not in ['raw', 'utf8', 'hex']:
			raise NotImplementedError('"{}" is not a valid input format for this controller'.format(informat))
		self.informat = informat
		self.model = model
		self.spaceregex = re.compile(r'\s+')
	def add_paths(self, paths):
		pass
	def add_path(self, path):
		pass
