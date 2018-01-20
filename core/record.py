
class Record:
	def __init__(self, xml):
		self.recordId 		= xml.recordID
		self.meetingId 		= xml.meetingID
		self.name 			= xml.name
		self.isPublished 	= xml.published == 'true'
		self.state 			= xml.state
		self.startTime 		= xml.startTime
		self.endTime 		= xml.endTime
		self.playbackType 	= xml.playback.format.type
		self.playbackUrl 	= xml.playback.format.url
		self.playbackLength = xml.playback.format.length
		for meta in xml.metadata.children:
			self.metas[meta.getName()] = meta

	def getRecordId(self):
		return self.recordId
	def getMeetingId(self):
		return self.meetingId
	def getName(self):
		return self.name
	def getState(self):
		return self.state
	def getStartTime(self):
		return self.startTime
	def getEndTime(self):
		return self.endTime
	def getPlaybackType(self):
		return self.playbackType
	def getPlaybackUrl(self):
		return self.playbackUrl
	def getPlaybackLength(self):
		return self.playbackLength
	def getMetas(self):
		return self.metas