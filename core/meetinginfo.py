
from .meeting import Meeting

class MeetingInfo(Meeting):
	def __init__(self, xml):
		super(self.__class__, self).__init__(xml)
		self.internalMeetingId 	= xml.internalMeetingID
		self.isRecording 		= xml.recording == 'true'
		self.startTime 			= float(xml.startTime)
		self.endTime 			= float(xml.endTime)
		self.maxUsers 			= xml.maxUsers
		self.moderatorCount 	= xml.moderatorCount
	def getInternalMeetingId(self):
		return self.internalMeetingId
	def getStartTime(self):
		return self.startTime
	def getEndTime(self):
		return self.endTime
	def getMaxUsers(self):
		return self.maxUsers
	def getModeratorCount(self):
		return self.moderatorCount