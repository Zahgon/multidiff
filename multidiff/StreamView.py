from multidiff import Render, Ansi
import html
class StreamView():
	'''A class for building UIs. Has some pretty serious side effects.
	Use Render instead if you're not making a long-running UI'''
	def __init__(self, model, encoding='hexdump', mode='sequence', color='ansi'):
		self.color = color
		self.render = Render(color=color, encoder=encoding)
		self.mode = mode
		self.model = model
		model.add_listener(self)
	def object_added(self, index):
		pass
	def diff_added(self, diff):
		pass
