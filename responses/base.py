

import sys
if sys.version_info[0] == 2:
    from abc import ABCMeta

    class BaseResponse:
        __metaclass__ = ABCMeta

        def __init__(self, rawXml):
            self.rawXml = rawXml

        def get_text(self, label):
            return self.rawXml[label]

        def get_return_code(self):
            return self.get_text("returncode")

        def get_message_key(self):
            return self.get_text("messageKey")

        def get_message(self):
            return self.get_text("message")
else:
    from abc import ABC

    class BaseResponse(ABC):
        def __init__(self, rawXml):
            self.rawXml = rawXml

        def get_text(self, label):
            return self.rawXml[label]

        def get_return_code(self):
            return self.get_text("returncode")

        def get_message_key(self):
            return self.get_text("messageKey")

        def get_message(self):
            return self.get_text("message")