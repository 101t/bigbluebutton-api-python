from .metaData import MetaData


class Record:
    def __init__(self, xml):
        self.__recordId = xml["recordID"]
        self.__meetingId = xml["meetingID"]
        self.__name = xml["name"]
        self.__isPublished = xml["published"] == 'true'
        self.__state = xml["state"]
        self.__startTime = xml["startTime"]

        self.__endTime = xml["endTime"]
        self.__playbackType = xml["playback"]["format"]["type"]
        self.__playbackUrl = xml["playback"]["format"]["url"]
        self.__playbackLength = xml["playback"]["format"]["length"]
        self.meta = MetaData(xml["metadata"])

    def get_recordid(self):
        return self.__recordId

    def get_meetingid(self):
        return self.__meetingId

    def is_published(self):
        return self.__isPublished

    def get_name(self):
        return self.__name

    def get_state(self):
        return self.__state

    def get_starttime(self):
        return self.__startTime

    def get_endtime(self):
        return self.__endTime

    def get_playbacktype(self):
        return self.__playbackType

    def get_playbackurl(self):
        return self.__playbackUrl

    def get_playbacklength(self):
        return self.__playbackLength

    def get_meta(self, name):
        return self.meta.get_meta(name)
