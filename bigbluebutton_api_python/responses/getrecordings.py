from .base import BaseResponse
from ..core.record import Record


class GetRecordingsResponse(BaseResponse):

    def get_recordings(self):
        recordings = []

        try:
            if self.get_message_key() == "noRecordings":
                return []
        except KeyError:
            pass

        for recordXml in self.get_field("recordings")["recording"]:
            recordings.append(Record(recordXml))

        return recordings
