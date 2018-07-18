import sys
from .meeting import Meeting


class MeetingInfo(Meeting):
    def __init__(self, xml):
        if sys.version_info[0] == 2:
            super(MeetingInfo, self).__init__(xml)
        else:
            super().__init__(xml)

        self.__internalMeetingId = xml["internalMeetingID"]
        self.__recording = xml["recording"] == 'true'
        self.__startTime = float(xml["startTime"])
        self.__endTime = float(xml["endTime"])
        self.__maxUsers = xml["maxUsers"]
        self.__moderatorCount = xml["moderatorCount"]

    def get_internal_meetingid(self):
        return self.__internalMeetingId

    def get_start_time(self):
        return self.__startTime

    def get_end_time(self):
        return self.__endTime

    def get_max_users(self):
        return self.__maxUsers

    def get_moderator_count(self):
        return self.__moderatorCount

    def is_recording(self):
        return self.__recording
