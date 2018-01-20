


class Attendee:
	def __init__(self, xml):
		self.userID 		= xml.userID
		self.fullName 		= xml.fullName
		self.role 			= xml.role
		self.isPresenter 	= xml.isPresenter == 'true'
		self.isListeningOnly = xml.isListeningOnly == 'true'
		self.hasJoinedVoice = xml.hasJoinedVoice == 'true'
		self.hasVideo 		= xml.hasVideo == 'true'
	def getUserID(self):
		return self.userID
	def getFullName(self):
		return self.fullName
	def getRole(self):
		return self.role