from .base import BaseResponse

class IsMeetingRunningResponse(BaseResponse):
    def is_meeting_running(self):
        field = self.get_field("running")
        return field == "true" or (isinstance(field, bool) and field)