from .base import BaseResponse
from ..core.meeting import Meeting

class GetMeetingsResponse(BaseResponse):
    def get_meetings(self):
        meetings = []
        for meetingXml in self.rawXml.meetings.getchildren():
            meetings.append(Meeting(meetingXml))
        return meetings