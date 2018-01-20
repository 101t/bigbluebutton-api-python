from .base import BaseResponse

class PublishRecordingsResponse(BaseResponse):
	def isPublished(self):
		return self.rawXml.published == "true"