

import sys
if sys.version_info[0] == 2:
	"2.x"
	from urllib import urlencode
	from abc import ABCMeta, abstractmethod

	class BaseResponse:
		__metaclass__ = ABCMeta
		def __init__(self, xml):
			self.rawXml = xml
		def getRawXml(self):
			return self.rawXml
		def getReturnCode(self):
			return self.rawXml.returncode
		def getMessageKey(self):
			return self.rawXml.messageKey
		def getMessage(self):
			return self.rawXml.message
else:
	"3.x"
	from urllib.parse import urlencode
	from abc import ABC, abstractmethod

	class BaseResponse(ABC):
		def __init__(self, xml):
			self.rawXml = xml
		def getRawXml(self):
			return self.rawXml
		def getReturnCode(self):
			return self.rawXml.returncode
		def getMessageKey(self):
			return self.rawXml.messageKey
		def getMessage(self):
			return self.rawXml.message