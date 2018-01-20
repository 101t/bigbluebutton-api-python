from .base import BaseResponse

class IsMeetingRunningResponse(BaseResponse):
	def isRunning(self):
		return self.rawXml.running == "true"