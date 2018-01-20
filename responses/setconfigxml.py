from .base import BaseResponse

class SetConfigXMLResponse(BaseResponse):
	def getToken(self):
		return self.rawXml.token