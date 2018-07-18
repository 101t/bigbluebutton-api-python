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

        field = self.get_field("attendees")
        if field == "":
            return []

        obj = field["attendee"]
        if isinstance(obj, list):
            for attendeeXml in obj:
                attendees.append(Attendee(xml=attendeeXml))
        else:
            attendees.append(Attendee(xml=obj))

        return attendees
