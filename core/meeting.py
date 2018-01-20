

class Meeting:
	def __init__(self, xml):
		self.meetingID				= xml.meetingID
		self.meetingName			= xml.meetingName
		self.creationTime			= float(xml.createTime)
		self.creationDate			= xml.createDate
		self.voiceBridge			= xml.voiceBridge
		self.dialNumber				= int(xml.dialNumber)
		self.attendeePassword		= xml.attendeePW
		self.moderatorPassword		= xml.moderatorPW
		self.hasBeenForciblyEnded	= xml.hasBeenForciblyEnded == 'true'
		self.isRunning				= xml.running == 'true'
		self.participantCount		= int(xml.participantCount)
		self.listenerCount			= int(xml.listenerCount)
		self.voiceParticipantCount	= int(xml.voiceParticipantCount)
		self.videoCount				= int(xml.videoCount)
		self.duration				= int(xml.duration)
		self.hasUserJoined			= xml.hasUserJoined == 'true'

	def getMeetingId(self):
		return self.meetingId
	def getMeetingName(self):
		return self.meetingName
	def getCreationTime(self):
		return self.creationTime
	def getCreationDate(self):
		return self.creationDate
	def getVoiceBridge(self):
		return self.voiceBridge
	def getDialNumber(self):
		return self.dialNumber
	def getAttendeePassword(self):
		return self.attendeePassword
	def getModeratorPassword(self):
		return self.moderatorPassword
	def getParticipantCount(self):
		return self.participantCount
	def getListenerCount(self):
		return self.listenerCount
	def getVoiceParticipantCount(self):
		return self.voiceParticipantCount
	def getVideoCount(self):
		return self.videoCount
	def getDuration(self):
		return self.duration