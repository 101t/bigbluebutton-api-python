
from .base import BaseResponse

class ApiVersion(BaseResponse):
	def getVersion(self):
		return self.rawXml.version
		