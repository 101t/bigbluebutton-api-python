
from .base import BaseParameters

class GetMeetingInfoParameters(BaseParameters):
	def __init__(self, meetingId, password):
		self.meetingId 	= meetingId
		self.password 	= password
	def getMeetingId(self):
		return self.meetingId
	def getPassword(self):
		return self.password
	def getHTTPQuery(self):
		return self.buildHTTPQuery({"meetingID": self.meetingId,"password": self.password})