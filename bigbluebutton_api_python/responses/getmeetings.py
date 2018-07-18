from .base import BaseResponse
from ..core.meeting import Meeting

class GetMeetingsResponse(BaseResponse):
    def get_meetings(self):
        meetings = []

        try:
            if self.get_message_key() == "noMeetings":
                return []
        except KeyError:
            pass

        for meetingXml in self.get_field("meetings")["meeting"]:
            meetings.append(Meeting(meetingXml))
        return meetings