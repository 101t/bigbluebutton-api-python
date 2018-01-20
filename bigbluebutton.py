
from .core import ApiMethod
from .parameters import (
	CreateMeetingParameters,
	DeleteRecordingsParameters,
	EndMeetingParameters,
	GetMeetingInfoParameters,
	GetRecordingsParameters,
	IsMeetingRunningParameters,
	JoinMeetingParameters,
	PublishRecordingsParameters,
	UpdateRecordingsParameters,
)
from .responses import (
	ApiVersionResponse,
	CreateMeetingResponse,
	DeleteRecordingsResponse,
	EndMeetingResponse,
	GetDefaultConfigXMLResponse,
	GetMeetingInfoResponse,
	GetMeetingsResponse,
	GetRecordingsResponse,
	IsMeetingRunningResponse,
	JoinMeetingResponse,
	PublishRecordingsResponse,
	SetConfigXMLResponse,
	UpdateRecordingsResponse,
)
from .util import UrlBuilder
from lxml import objectify
from xml.etree import ElementTree as ET
import requests, re

class BigBlueButton:

	def __init__(self, securitySalt, bbbServerBaseUrl, ssl=False, DEBUG=False):
		self.securitySalt = securitySalt
		self.bbbServerBaseUrl = bbbServerBaseUrl
		self.urlBuilder = UrlBuilder(self.securitySalt, self.bbbServerBaseUrl)
		self.ssl = ssl
		self.schema = "https://" if self.ssl else "http://"
		self.DEBUG = DEBUG
		self.status = False

	def getApiVersion(self):
		''' 
		returns: 
			ApiVersionResponse
		'''
		xml = self.processXmlResponse(self.urlBuilder.buildUrl())
		return ApiVersionResponse(xml)
	'''
	__________________ BBB ADMINISTRATION METHODS _________________

	The methods in the following section support the following categories of the BBB API:
    -- create
    -- getDefaultConfigXML
    -- join
    -- end

	'''

	def getCreateMeetingUrl(self, createMeetingParams):
		return self.urlBuilder.buildUrl(ApiMethod.CREATE, createMeetingParams.getHTTPQuery())
	def createMeeting(self, createMeetingParams):
		xml = self.processXmlResponse(self.getCreateMeetingUrl(createMeetingParams), createMeetingParams.getPresentationsAsXML())
		return CreateMeetingResponse(xml)
	
	def getDefaultConfigXMLUrl(self):
		return self.urlBuilder.buildUrl(ApiMethod.GET_DEFAULT_CONFIG_XML)
	def getDefaultConfigXML(self):
		xml = self.processXmlResponse(self.getDefaultConfigXMLUrl())
		return GetDefaultConfigXMLResponse(xml)
	
	def setConfigXMLUrl(self):
		return self.urlBuilder.buildUrl(ApiMethod.SET_CONFIG_XML, "", False)
	def setConfigXML(self, setConfigXMLParams):
		setConfigXMLPayload = self.urlBuilder.buildQs(ApiMethod.SET_CONFIG_XML, setConfigXMLParams.getHTTPQuery())
		xml = self.processXmlResponse(self.setConfigXMLUrl(), setConfigXMLPayload, "application/x-www-form-urlencoded")
		return SetConfigXMLResponse(xml)

	def getJoinMeetingURL(self, joinMeetingParams):
		return self.urlBuilder.buildUrl(ApiMethod.JOIN, joinMeetingParams.getHTTPQuery())
	def joinMeeting(self, joinMeetingParams):
		xml = self.processXmlResponse(self.getJoinMeetingURL(joinMeetingParams))
		return JoinMeetingResponse(xml)

	def getEndMeetingURL(self, endParams):
		return self.urlBuilder.buildUrl(ApiMethod.END, endParams.getHTTPQuery())
	def endMeeting(self, endParams):
		xml = self.processXmlResponse(self.getEndMeetingURL(endParams))
		return EndMeetingResponse(xml)
	
	'''
	__________________ BBB MONITORING METHODS _________________ 

	The methods in the following section support the following categories of the BBB API:
    -- isMeetingRunning
    -- getMeetings
    -- getMeetingInfo

	'''

	def getIsMeetingRunningUrl(self, meetingParams):
		return self.urlBuilder.buildUrl(ApiMethod.IS_MEETING_RUNNING, meetingParams.getHTTPQuery())
	def isMeetingRunning(self, meetingParams):
		xml = self.processXmlResponse(self.getIsMeetingRunningUrl(meetingParams))
		return IsMeetingRunningResponse(xml)

	def getMeetingsUrl(self):
		return self.urlBuilder.buildUrl(ApiMethod.GET_MEETINGS)
	def getMeetings(self):
		xml = self.processXmlResponse(self.getMeetingsUrl())
		return GetMeetingsResponse(xml)

	def getMeetingInfoUrl(self, meetingParams):
		return self.urlBuilder.buildUrl(ApiMethod.GET_MEETING_INFO, meetingParams.getHTTPQuery())
	def getMeetingInfo(self, meetingParams):
		xml = self.processXmlResponse(self.getMeetingInfoUrl(meetingParams))
		return GetMeetingInfoResponse(xml)
	'''
	__________________ BBB RECORDING METHODS _________________

	The methods in the following section support the following categories of the BBB API:
    -- getRecordings
    -- publishRecordings
    -- deleteRecordings

	'''
	def getRecordingsUrl(self, recordingsParams):
		return self.urlBuilder.buildUrl(ApiMethod.GET_RECORDINGS, recordingsParams.getHTTPQuery())
	def getRecordings(self, recordingsParams):
		xml = self.processXmlResponse(self.getRecordingsUrl(recordingsParams))
		return GetRecordingsResponse(xml)
	def getPublishRecordingsUrl(self, recordingParams):
		return self.urlBuilder.buildUrl(ApiMethod.PUBLISH_RECORDINGS, recordingParams.getHTTPQuery())
	def publishRecordings(self, recordingParams):
		xml = self.processXmlResponse(self.getPublishRecordingsUrl(recordingParams))
		return PublishRecordingsResponse(xml)
	def getDeleteRecordingsUrl(self, recordingParams):
		return self.urlBuilder.buildUrl(ApiMethod.DELETE_RECORDINGS, recordingParams.getHTTPQuery())
	def deleteRecordings(self, recordingParams):
		xml = self.processXmlResponse(self.getDeleteRecordingsUrl(recordingParams))
		return DeleteRecordingsResponse(xml)
	def getUpdateRecordingsUrl(self, recordingParams):
		return self.urlBuilder.buildUrl(ApiMethod.UPDATE_RECORDINGS, recordingParams.getHTTPQuery())
	def updateRecordings(self, recordingParams):
		xml = self.processXmlResponse(self.getUpdateRecordingsUrl(recordingParams))
		return UpdateRecordingsResponse(xml)
	'''
	____________________ INTERNAL CLASS METHODS ___________________

	A private utility method used by other public methods to process XML responses.
	Args:
		url (str)
		payload (str)
	Returns:
		ElementTree

	'''


	def processXmlResponse(self, url, payload = "", contentType = "application/xml"):
		host = re.sub(re.compile(r"http(s?)\:\/\/"), "", self.bbbServerBaseUrl)
		url = "{}{}".format(self.schema, host)
		headers = {
			"Host": host,
			"Content-Type": contentType,
			"Content-Length": len(payload),
		}
		response = requests.post(url, headers=headers, data=payload, verify=False)
		if self.DEBUG:
			print("[DEBUG] Header: %s" % headers)
			print("[DEBUG] Request: %s" % payload)
			print("[DEBUG] Response: %s" % response)
		return objectify.fromstring(response.text) if response.status_code == 200 else None