from .base import BaseResponse

class IsMeetingRunningResponse(BaseResponse):
    def is_meeting_running(self):
        return self.get_text("running") == "true" or self.get_text("running")