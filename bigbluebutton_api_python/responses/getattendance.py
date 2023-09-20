import sys
from .base import BaseResponse
from ..core.attendance import Attendance

class GetAttendanceResponse(BaseResponse):
    def __init__(self, xml):
        if sys.version_info[0] == 2:
            super(GetAttendanceResponse, self).__init__(xml)
        else:
            super().__init__(xml)
    def get_attendance(self):
        attendances = []
        for meeting in self.get_field("meetings")["meeting"]:
            attendances.append(Attendance(xml=meeting))
        return attendances
