from .base import BaseResponse
from datetime import datetime

class CreateMeetingResponse(BaseResponse):
    def get_meetingid(self):
        return self.get_text("meetingID")

    def get_attendee_pw(self):
        return self.get_text("attendeePW")

    def get_moderator_pw(self):
        return self.get_text("moderatorPW")

    def get_create_time(self):
        return datetime.fromtimestamp(int(self.get_text("createTime")) / 1e3).strftime('%Y-%m-%d %H:%M:%S')

    def has_been_forcibly_ended(self):
        return self.get_text("hasBeenForciblyEnded") == "true"

    def get_voice_bridge(self):
        return self.get_text("voiceBridge")

    def get_dial_number(self):
        return self.get_text("dialNumber")