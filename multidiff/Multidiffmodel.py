import difflib

class Diff():
	"""A diff result of a diff of two objects"""
	def __init__(self, source, target, opcodes):
		self.source = source
		self.target = target
		self.opcodes = opcodes

class DiffObject():
	"""A diffable object. Raw byte data and some metadata."""
	def __init__(self, data, info='', identifier=0):
		self.data = data
		self.info = info

class MultidiffModel():

	def __init__(self, datas = []):
		"""Create a MultiDiffModel for a set of objects"""
		self.listeners = []
		self.clear()
		self.add_all(datas)

	def add_listener(self, listener):
		"""Adds an object that listens to events. Views add themselves."""
		pass

	def add(self, data, info=''):
		"""Add a single data object to the model"""
		obj = DiffObject(data, info=info)
		self.objects.append(obj)
		for listener in self.listeners:
			listener.object_added(len(self.objects) - 1)

	def add_all(self, datas):
		"""Add a list of byte datas"""
		pass
		
	def clear(self):
		"""Clears all object and diff data"""
		pass

	def diff_sequence(self):
		"""Diff all objects to the next one in the list"""
		pass

	def diff_baseline(self, baseline=0):
		"""Diff all objects against a common baseline"""
		pass

	def diff(self, source, target):
		"""Diff two objects of the model and store the result"""
		sm = difflib.SequenceMatcher()
		sm.set_seqs(self.objects[source].data, self.objects[target].data)
		diff = Diff(source, target, sm.get_opcodes())
		self.diffs.append(diff)
		for listener in self.listeners:
			listener.diff_added(diff)

	def diff_last_pair(self):
		"""Diff the two most recently added objects"""
		pass

	def diff_first_to_last(self):
		"""Diff the most recently added object with the first one"""
		pass
