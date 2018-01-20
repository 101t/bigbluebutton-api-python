
import sys
if sys.version_info[0] == 2:
	"2.x"
	from urllib import urlencode
	from abc import ABCMeta, abstractmethod

	class BaseParameters:
		__metaclass__ = ABCMeta
		def buildHTTPQuery(self, array):
			return urlencode(dict(array))
		@abstractmethod
		def getHTTPQuery(self):
			pass
else:
	"3.x"
	from urllib.parse import urlencode
	from abc import ABC, abstractmethod

	class BaseParameters(ABC):
		def buildHTTPQuery(self, array):
			return urlencode(dict(array))
		@abstractmethod
		def getHTTPQuery(self):
			pass