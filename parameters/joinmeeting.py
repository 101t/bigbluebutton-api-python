
from .base import BaseParameters

class JoinMeetingParameters(BaseParameters):
	def __init__(self, meetingID, username, password):
		self.meetingID = meetingID
		self.username = username
		self.password = password
		self.userID = ""
		self.webVoiceConf = ""
		self.creationTime = ""
		self.configToken = ""
		self.avatarURL = ""
		self.redirect = ""
		self.clientURL = ""

	def getMeetingID(self):
		return self.meetingID
	def getUsername(self):
		return self.username
	def getPassword(self):
		return self.password
	def getUserID(self):
		return self.userID
	def getWebVoiceConf(self):
		return self.webVoiceConf
	def getCreationTime(self):
		return self.creationTime
	def getConfigToken(self):
		return self.configToken
	def getAvatarURL(self):
		return self.avatarURL
	def isRedirect(self):
		return self.redirect
	def getClientURL(self):
		return self.clientURL
	def getHTTPQuery(self):
		return self.buildHTTPQuery({
				"meetingID": self.meetingID,
				"fullName": self.username,
				"password": self.password,
				"userID": self.userID,
				"webVoiceConf": self.webVoiceConf,
				"createTime": self.creationTime,
				"configToken": self.configToken,
				"avatarURL": self.avatarURL,
				"redirect": "true" if self.redirect else "false",
				"clientURL": self.clientURL,
			})