from .base import BaseResponse
from datetime import datetime

class CreateMeetingResponse(BaseResponse):
    def get_meetingid(self):
        return self.get_field("meetingID")

    def get_attendee_pw(self):
        return self.get_field("attendeePW")

    def get_moderator_pw(self):
        return self.get_field("moderatorPW")

    def get_create_time(self):
        return datetime.fromtimestamp(int(self.get_field("createTime")) / 1e3).strftime('%Y-%m-%d %H:%M:%S')

    def has_been_forcibly_ended(self):
        field = self.get_field("hasBeenForciblyEnded")
        return field == "true" or (isinstance(field, bool) and field)

    def get_voice_bridge(self):
        return self.get_field("voiceBridge")

    def get_dial_number(self):
        return self.get_field("dialNumber")