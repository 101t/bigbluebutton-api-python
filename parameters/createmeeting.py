
import sys
if sys.version_info[0] == 2:
	"2.x"
	from urllib import urlencode
else:
	"3.x"
	from urllib.parse import urlencode

from .meta import MetaParameters
import base64

class CreateMeetingParameters(MetaParameters):
	def __init__(self, meetingId, meetingName):
		self.meetingId 		= meetingId
		self.meetingName 	= meetingName
	def getMeetingId(self):
		return self.meetingId
	def getMeetingName(self):
		return self.meetingName
	def getAttendeePassword(self):
		return self.attendeePassword
	def getModeratorPassword(self):
		return self.moderatorPassword
	def getDialNumber(self):
		return self.dialNumber
	def getVoiceBridge(self):
		return self.voiceBridge
	def getWebVoice(self):
		return self.webVoice
	def getLogoutUrl(self):
		return self.logoutUrl
	def getMaxParticipants(self):
		return self.maxParticipants
	def isRecorded(self):
		return self.record
	def isAutoStartRecording(self):
		return self.autoStartRecording
	def isAllowStartStopRecording(self):
		return self.allowStartStopRecording
	def getDuration(self):
		return self.duration
	def getWelcomeMessage(self):
		return self.welcomeMessage
	def getModeratorOnlyMessage(self):
		return self.moderatorOnlyMessage
	def getPresentations(self):
		return self.presentations
	def addPresentation(self, nameOrUrl, content=None):
		self.presentations[nameOrUrl] = base64.b64encode(bytes(content, "utf-8")) if content else b""
	def getPresentationsAsXML(self):
		result = ""
		# if self.presentations:
		# 	xml = ET.Element("modules")
		# 	module = ET.SubElement(xml, "module")
		# 	module.set("name", "presentation")
		# 	for nameOrUrl, content in self.presentations:
		# 		if self.presentations[nameOrUrl] == True:
		# 			ET.SubElement(module, "document").set("url", urlencode(nameOrUrl))
		# 		else:
		# 			document = ET.SubElement(module, "document")
		# 			document.set("name", nameOrUrl)
		# 			document[0] = content
		# 	result = ET.tostring(xml, pretty_print=True)
		return result
	def getHTTPQuery(self):
		queries = {
			'name'                    : self.meetingName,
            'meetingID'               : self.meetingId
            # 'attendeePW'              : self.attendeePassword,
            # 'moderatorPW'             : self.moderatorPassword,
            # 'dialNumber'              : self.dialNumber,
            # 'voiceBridge'             : self.voiceBridge,
            # 'webVoice'                : self.webVoice,
            # 'logoutURL'               : self.logoutUrl,
            # 'record'                  : 'true' if self.record else 'false',
            # 'duration'                : self.duration,
            # 'maxParticipants'         : self.maxParticipants,
            # 'autoStartRecording'      : 'true' if self.autoStartRecording else 'false',
            # 'allowStartStopRecording' : 'true' if self.allowStartStopRecording else 'false',
            # 'welcome'                 : self.welcomeMessage.strip(),
            # 'moderatorOnlyMessage'    : self.moderatorOnlyMessage.strip(),
		}
		self.buildMeta(queries)
		return self.buildHTTPQuery(queries)