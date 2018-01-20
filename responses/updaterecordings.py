from .base import BaseResponse

class UpdateRecordingsResponse(BaseResponse):
	def isUpdated(self):
		return self.rawXml.updated == "true"