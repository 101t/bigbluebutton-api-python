from .base import BaseResponse
from core.meetinginfo import MeetingInfo
from core.attendee import Attendee

class GetMeetingInfoResponse(BaseResponse):
	def __init__(self):
		self.meetingInfo = None
		self.attendees = []
		self.metadata = []
	def getMeetingInfo(self):
		if not self.meetingInfo:
			self.meetingInfo = MeetingInfo(xml=self.rawXml)
		return self.meetingInfo
	def getAttendees(self):
		if not self.attendees:
			for attendeeXml in self.rawXml.attendees.attendee:
				self.attendees.append(Attendee(xml=self.attendeeXml))
		return self.attendees