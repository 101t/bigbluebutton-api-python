
from .base import BaseParameters

class PublishRecordingsParameters(BaseParameters):
	def __init__(self, recordingID, publish):
		self.recordingID = recordingID
		self.publish = publish
	def getRecordingID(self):
		return self.recordingID
	def isPublish(self):
		return self.publish
	def getHTTPQuery(self):
		return self.buildHTTPQuery({
			"recordID": self.recordingID,
			"publish": "true" if self.publish else "false",
			})