from .base import BaseResponse

class DeleteRecordingsResponse(BaseResponse):
	def isDeleted(self):
		return self.rawXml.delete == "true"