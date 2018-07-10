import sys
from .base import BaseResponse
from ..core.meetinginfo import MeetingInfo
from ..core.attendee import Attendee


class GetMeetingInfoResponse(BaseResponse):
    def __init__(self, xml):
        if sys.version_info[0] == 2:
            super(GetMeetingInfoResponse, self).__init__(xml)
        else:
            super().__init__(xml)

    def get_meetinginfo(self):
        return MeetingInfo(xml=self.rawXml)

    def get_attendees(self):
        attendees = []
        for attendeeXml in self.rawXml.attendees.getchildren():
            attendees.append(Attendee(xml=attendeeXml))
        return attendees
