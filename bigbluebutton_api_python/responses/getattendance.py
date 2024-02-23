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
        meetings = self.get_field("meetings")["meeting"]
        if type(meetings) != list:
            meetings = [meetings]
        for meeting in meetings:
            attendances.append(Attendance(xml=meeting))
        return attendances
