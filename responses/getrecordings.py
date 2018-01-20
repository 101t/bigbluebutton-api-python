from .base import BaseResponse
from ..core.record import Record

class GetRecordingsResponse(BaseResponse):
	def __init__(self):
		self.records = []
	def getRecords(self):
		if not self.records:
			for recordXml in self.rawXml.recordings.xpath(".//*"):
				self.records.append(recordXml)
		return self.records