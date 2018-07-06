
from .meta import MetaParameters

class GetRecordingsParameters(MetaParameters):
	def __init__(self):
		self.meetingID = ""
		self.recordID = ""
		self.state = ""
	def getHTTPQuery(self):
		queries = {
			"meetingID": self.meetingID,
			"recordID": self.recordID,
			"recordID": self.recordID,
			"state": self.state
		}
		self.buildMeta(queries)
		return self.buildHTTPQuery(queries)