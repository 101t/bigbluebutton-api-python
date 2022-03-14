from .base import BaseResponse
from ..core.record import Record
import jxmlease



class GetRecordingsResponse(BaseResponse):

    def get_recordings(self):
        recordings = []

        try:
            if self.get_message_key() == "noRecordings":
                return []
        except KeyError:
            pass
            
        recordings_data = self.get_field("recordings")["recording"]
        if isinstance(recordings_data, jxmlease.dictnode.XMLDictNode):
            recordings.append(Record(recordings_data))
        else:
            for recordingXml in self.get_field("recordings")["recording"]:
                recordings.append(Record(recordingXml))           
        return recordings
