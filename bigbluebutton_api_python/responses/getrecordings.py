from .base import BaseResponse
from ..core.record import Record


class GetRecordingsResponse(BaseResponse):

    def get_recordings(self):
        recordings = []
        for recordXml in self.rawXml.recordings.getchildren():
            recordings.append(Record(recordXml))

        return recordings
