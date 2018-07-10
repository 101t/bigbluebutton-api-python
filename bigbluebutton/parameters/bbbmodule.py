
import os, base64

class BBBModule:
    URL = "url"
    FILE = "file"
    base64s = "base64s"

    def __init__(self):
        self.__urls = []
        self.__files = []
        self.__base64s = []

    def add_slide(self, type, value, name = None):
        if type == self.URL:
            self.__urls.append(value)
        elif type == self.files:
            self.__files.append(value)
        elif type == self.base64s:
            self.__base64s.append([name, value])

    def has_slides(self):
        return len(self.__urls) != 0 or len(self.__files) != 0 or len(self.__base64s) != 0

    def to_xml(self):
        if self.has_slides():
            xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><modules>"
            xml += self.__slides_to_xml()
            xml += "</modules>"
            return xml
        else:
            return ""

    def __slides_to_xml(self):
        xml = "<module name=\"presentation\">"
        for url in self.__urls:
            xml += "<document url=\"" + url + "\" />"

        for [name, value] in self.__base64s:
            xml += "<document name=\"" + name + "\">" + value + "</document>"

        for single_file in self.__files:
            if os.path.exists(single_file):
                xml += "<document name=\"" + os.path.basename(single_file) + "\">"
                with open(single_file, 'r') as f:
                    xml += base64.encodestring(f.read())
                xml += "</document>"

        return xml