from .base import BaseResponse

class CreateMeetingResponse(BaseResponse):
	def getMeetingID(self):
		return self.meetingID
	def getAttendeePassword(self):
		return self.rawXml.attendeePW
	def getModeratorPassword(self):
		return self.rawXml.moderatorPW
	def getCreationTime(self):
		return float(self.rawXml.createTime)
	def getVoiceBridge(self):
		return int(self.rawXml.voiceBridge)
	def getDialNumber(self):
		return self.rawXml.dialNumber
	def getCreationDate(self):
		'Creation date at the format "Sun Jan 17 18:20:07 EST 2016".'
		return self.rawXml.createDate
	def hasUserJoined(self):
		return self.rawXml.hasUserJoined == "true"
	def getDuration(self):
		return self.rawXml.duration
	def hasBeenForciblyEnded(self):
		return self.rawXml.hasBeenForciblyEnded == "true"