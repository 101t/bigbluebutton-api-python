from .metaData import MetaData

class Meeting(object):
    def __init__(self, xml):
        self.__meetingId = xml["meetingID"]
        self.__meetingName = xml["meetingName"]
        self.__creationTime = float(xml["createTime"])
        self.__creationDate = xml["createDate"]
        self.__voiceBridge = xml["voiceBridge"]
        self.__dialNumber = xml["dialNumber"]
        self.__attendeePassword = xml["attendeePW"]
        self.__moderatorPassword = xml["moderatorPW"]
        self.__hasBeenForciblyEnded = xml["hasBeenForciblyEnded"] == 'true'
        self.__isRunning = xml["running"] == 'true'
        self.__participantCount = int(xml["participantCount"])
        self.__listenerCount = int(xml["listenerCount"])
        self.__voiceParticipantCount = int(xml["voiceParticipantCount"])
        self.__videoCount = int(xml["videoCount"])
        self.__duration = int(xml["duration"])
        self.__hasUserJoined = xml["hasUserJoined"] == 'true'
        self.__meta = MetaData(xml["metadata"])

    def get_meetingid(self):
        return self.__meetingId

    def get_meetingname(self):
        return self.__meetingName

    def get_createtime(self):
        return self.__creationTime

    def get_createdate(self):
        return self.__creationDate

    def get_voicebridge(self):
        return self.__voiceBridge

    def get_dialnumber(self):
        return self.__dialNumber

    def get_attendeepw(self):
        return self.__attendeePassword

    def get_moderatorpw(self):
        return self.__moderatorPassword

    def get_participantcount(self):
        return self.__participantCount

    def get_listenercount(self):
        return self.__listenerCount

    def get_voiceparticipantcount(self):
        return self.__voiceParticipantCount

    def get_videocount(self):
        return self.__videoCount

    def get_duration(self):
        return self.__duration

    def has_user_joined(self):
        return self.__hasUserJoined

    def has_been_forcibly_ended(self):
        return self.__hasBeenForciblyEnded
