
from .base import BaseResponse

class ApiVersionResponse(BaseResponse):
	def getVersion(self):
		return self.rawXml.version
		