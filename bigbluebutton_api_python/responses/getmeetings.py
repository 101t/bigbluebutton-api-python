from .base import BaseResponse
from ..core.meeting import Meeting
import jxmlease

class GetMeetingsResponse(BaseResponse):
    def get_meetings(self):
        meetings = []

        try:
            if self.get_message_key() == "noMeetings":
                return []
        except KeyError:
            pass

        meetings_data = self.get_field("meetings")["meeting"]
        if isinstance(meetings_data, jxmlease.dictnode.XMLDictNode):
            meetings.append(Meeting(meetings_data))
        else:
            for meetingXml in self.get_field("meetings")["meeting"]:
                meetings.append(Meeting(meetingXml))
        return meetings
