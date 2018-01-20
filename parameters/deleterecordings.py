
from .base import BaseParameters

class DeleteRecordingsParameters(BaseParameters):
	def __init__(self, recordingId):
		self.recordingId = recordingId

	def getRecordingId(self):
		return self.recordingId
	def getHTTPQuery(self):
		return self.buildHTTPQuery({"recordID": self.recordingId})