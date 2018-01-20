from .base import BaseResponse
from ..core.meeting import Meeting

class GetMeetingsResponse(BaseResponse):
	def __init__(self):
		self.meetings = []

	def getMeetings(self):
		if not self.meetings:
			# self.rawXml.meetings.getchildren() does not work in python2.7
			for meetingXml in self.rawXml.meetings.xpath(".//*"):
				self.meetings.append(Meeting(meetingXml))
		return self.meetings