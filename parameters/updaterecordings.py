
from .meta import MetaParameters


class UpdateRecordingsParameters(MetaParameters):
	def __init__(self, recordingID):
		self.recordingID = recordingID
	def getRecordingID(self):
		return self.recordingID
	def getHTTPQuery(self):
		queries = {"recordID": self.recordingID}
		self.buildMeta(queries)
		return self.buildHTTPQuery(queries)