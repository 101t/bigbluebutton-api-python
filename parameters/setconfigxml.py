
from .base import BaseParameters
import sys
if sys.version_info[0] == 2:
	"2.x"
	from urllib import urlencode
else:
	"3.x"
	from urllib.parse import urlencode

from xml.etree import ElementTree as ET

class SetConfigXMLParameters(BaseParameters):
	def __init__(self, meetingID):
		self.meetingID = meetingID
		self.rawXml = None

	def getMeetingId(self):
		return self.meetingID
	def getRawXml(self):
		return self.rawXml

	def getHTTPQuery(self):
		return self.buildHTTPQuery({
				"configXML": urlencode(ET.tostring(self.rawXml, pretty_print=True)),
				"meetingID": self.meetingID
			})