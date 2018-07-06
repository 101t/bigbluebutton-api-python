
from core import ApiMethod
from responses import (
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
from util import UrlBuilder
from xml.etree import ElementTree as ET
import requests, re
import sys
if sys.version_info[0] == 2:
	from urllib2 import Request
	from urllib import urlencode, urlopen
else:
	from urllib.request import urlopen, Request
	from urllib.parse import urlencode


class BigBlueButton:

	def __init__(self, bbbServerBaseUrl, securitySalt):
		self.__urlBuilder = UrlBuilder(bbbServerBaseUrl, securitySalt)

	def get_api_version(self):
		response = self.__send_api_request(ApiMethod.VERSION)
		return response.find("version").text

	def create_meeting(self, meeting_id, params={}):
		params["meetingID"] = meeting_id
		response = self.__send_api_request(ApiMethod.CREATE, params)
		return response

	def get_join_meeting_url(self, full_name, meeting_id, password, params={}):
		params["fullName"] = full_name
		params["meetingID"] = meeting_id
		params["password"] = password
		response = self.__format_url(ApiMethod.JOIN, params)
		return response

	def is_meeting_running(self, meeting_id):
		params = {"meetingID": meeting_id}
		response = self.__send_api_request(ApiMethod.IS_MEETING_RUNNING, params)
		return True if response.find("running").text == "true" else False

	def end_meeting(self, meeting_id, password):
		params = {"meetingID": meeting_id, "password": password}
		response = self.__send_api_request(ApiMethod.END, params)
		return True if response.find("returncode").text == "SUCCESS" else False

	# TO DO
	def get_meeting_info(self):
		pass

	# TO DO
	def get_meetings(self):
		pass

	# TO DO
	def get_recordings(self):
		pass

	# TO DO
	def publish_recordings(self):
		pass

	# TO DO
	def delete_recordings(self):
		pass

	# TO DO
	def update_recordings(self):
		pass

	# get default config.xml, if file_path is not given, this function will return response
	# as ElementTree.Element, otherwise it saves the response to the specific file path
	def get_default_config_xml(self, file_path=None):
		response = self.__send_api_request(ApiMethod.GET_DEFAULT_CONFIG_XML)
		if file_path is None:
			return response
		else:
			with open(file_path, 'w') as file:
				file.write(ET.tostring(response).decode())

	# TO DO
	def set_config_xml(self, meeting_id, xml):
		pass


	def __send_api_request(self, api_call, params={}, data=None):
		url = self.__urlBuilder.buildUrl(api_call, params)

		# if data is none, then we send a GET request, if not, then we send a POST request
		if data is None:
			response = urlopen(url).read()
		else:
			request = Request(url, urlencode(data).encode())
			response = urlopen(request).read()

		tree = ET.fromstring(response)

		# get default config xml request will simply return the xml file without
		# returncode, so it will cause an error when try to check the return code
		if api_call != ApiMethod.GET_DEFAULT_CONFIG_XML:
			if tree.find("returncode").text == "FAILED":
				raise BBBException(tree.find("messageKey").text,
								   tree.find("message").text)

		return tree



	'''
	seperate
	'''


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
		# url = "{}{}".format(self.schema, host)
		headers = {
			"Host": host,
			"Content-Type": contentType,
			"Content-Length": str(len(payload)),
		}
		# response = requests.post(url, headers=headers, data=payload, verify=False)
		response = requests.get(url)

		return objectify.fromstring(response.text) if response.status_code == 200 else None

