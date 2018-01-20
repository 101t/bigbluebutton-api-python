
from .base import BaseParameters

class IsMeetingRunningParameters(BaseParameters):
	def __init__(self, meetingID):
		self.meetingID = meetingID
	def getMeetingId(self):
		return self.meetingID
	def getHTTPQuery(self):
		return self.buildHTTPQuery({"meetingID": self.meetingID})