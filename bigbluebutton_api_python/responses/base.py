
import sys

def recursive_dict(element):
    if element.text == None and len(element.attrib):
        return element.tag, element.attrib

    return element.tag, \
            dict(map(recursive_dict, element.getchildren())) or element.text


if sys.version_info[0] == 2:
    from abc import ABCMeta

    class BaseResponse(dict):
        __metaclass__ = ABCMeta

        def __init__(self, rawXml):
            dict.__init__(self, xml=recursive_dict(rawXml)[1])
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

    class BaseResponse(ABC, dict):
        def __init__(self, rawXml):
            dict.__init__(self, xml=recursive_dict(rawXml)[1])
            self.rawXml = rawXml

        def get_text(self, label):
            return self.rawXml[label]

        def get_return_code(self):
            return self.get_text("returncode")

        def get_message_key(self):
            return self.get_text("messageKey")

        def get_message(self):
            return self.get_text("message")