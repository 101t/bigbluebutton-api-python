
from .base import BaseParameters

class MetaParameters(BaseParameters):
	meta = []
	@property
	def getMeta(self, key):
		return self.meta[key]
	@meta.setter
	def addMeta(self, key, value):
		self.meta[key] = value
	def buildMeta(*queries):
		if len(self.meta) > 0:
			for key, value in self.meta.items():
				queries['meta_{}'.format(key)] = value