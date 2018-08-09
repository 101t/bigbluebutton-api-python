class Attendee:
    def __init__(self, xml):
        self.__userID = xml["userID"]
        self.__fullName = xml["fullName"]
        self.__role = xml["role"]
        self.__isPresenter = xml["isPresenter"] == 'true'
        self.__isListeningOnly = xml["isListeningOnly"] == 'true'
        self.__hasJoinedVoice = xml["hasJoinedVoice"] == 'true'
        self.__hasVideo = xml["hasVideo"] == 'true'

    def get_userid(self):
        return self.__userID

    def get_fullname(self):
        return self.__fullName

    def get_role(self):
        return self.__role

    def is_presenter(self):
        return self.__isPresenter

    def is_listening_only(self):
        return self.__isListeningOnly

    def has_joined_voice(self):
        return self.__hasJoinedVoice

    def has_video(self):
        return self.__hasVideo
