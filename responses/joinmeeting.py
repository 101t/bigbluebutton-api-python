from .base import BaseResponse

class JoinMeetingResponse(BaseResponse):
	def getMeetingID(self):
		return self.rawXml.meeting_id
	def getUserId(self):
		return self.rawXml.user_id
	def getAuthToken(self):
		return self.rawXml.auth_token