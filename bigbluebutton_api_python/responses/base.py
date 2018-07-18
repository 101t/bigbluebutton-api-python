
import sys

if sys.version_info[0] == 2:
    from abc import ABCMeta

    class BaseResponse(dict):
        __metaclass__ = ABCMeta

        def __init__(self, rawXml):
            dict.__init__(self, xml=rawXml)
            self.rawXml = rawXml

        def get_field(self, label):
            return self.rawXml[label]

        def get_return_code(self):
            return self.get_field("returncode")

        def get_message_key(self):
            return self.get_field("messageKey")

        def get_message(self):
            return self.get_field("message")
else:
    from abc import ABC

    class BaseResponse(ABC, dict):
        def __init__(self, rawXml):
            dict.__init__(self, xml=rawXml)
            self.rawXml = rawXml

        def get_field(self, label):
            return self.rawXml[label]

        def get_return_code(self):
            return self.get_field("returncode")

        def get_message_key(self):
            return self.get_field("messageKey")

        def get_message(self):
            return self.get_field("message")