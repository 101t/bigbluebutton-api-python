from .core import ApiMethod
from .responses import (
    ApiVersionResponse,
    CreateMeetingResponse,
    DeleteRecordingsResponse,
    EndMeetingResponse,
    GetMeetingInfoResponse,
    GetMeetingsResponse,
    GetRecordingsResponse,
    IsMeetingRunningResponse,
    PublishRecordingsResponse,
    SetConfigXMLResponse,
    UpdateRecordingsResponse,
)
from .exception import BBBException
from .util import UrlBuilder
from .parameters import BBBModule
import sys
from jxmlease import parse
from hashlib import sha1
if sys.version_info[0] == 2:
    from urllib import urlencode, urlopen
    from urllib import quote
else:
    from urllib.request import urlopen
    from urllib.parse import urlencode
    from urllib.request import quote


class BigBlueButton:

    def __init__(self, bbbServerBaseUrl, securitySalt):
        self.__urlBuilder = UrlBuilder(bbbServerBaseUrl, securitySalt)

    def get_api_version(self):
        response = self.__send_api_request(ApiMethod.VERSION)
        return ApiVersionResponse(response)

    def create_meeting(self, meeting_id, params={}, meta={}, slides=None):
        params["meetingID"] = meeting_id
        if meta != {}:
            for key, val in meta.items():
                params["meta_" + key] = val
        if slides and isinstance(slides, BBBModule):
            response = self.__send_api_request(ApiMethod.CREATE, params, slides.to_xml())
        else:
            response = self.__send_api_request(ApiMethod.CREATE, params)
        return CreateMeetingResponse(response)

    def get_join_meeting_url(self, full_name, meeting_id, password, params={}):
        params["fullName"] = full_name
        params["meetingID"] = meeting_id
        params["password"] = password
        response = self.__urlBuilder.buildUrl(ApiMethod.JOIN, params)
        return response

    def is_meeting_running(self, meeting_id):
        params = {"meetingID": meeting_id}
        response = self.__send_api_request(ApiMethod.IS_MEETING_RUNNING, params)
        return IsMeetingRunningResponse(response)

    def end_meeting(self, meeting_id, password):
        params = {"meetingID": meeting_id, "password": password}
        response = self.__send_api_request(ApiMethod.END, params)
        return EndMeetingResponse(response)

    def get_meeting_info(self, meeting_id):
        params = {"meetingID": meeting_id}
        response = self.__send_api_request(ApiMethod.GET_MEETING_INFO, params)
        return GetMeetingInfoResponse(response)

    def get_meetings(self):
        response = self.__send_api_request(ApiMethod.GET_MEETINGS)
        return GetMeetingsResponse(response)

    def get_recordings(self, meeting_id="", recording_id="", states=None, meta=None):
        if states:
            for state in states:
                if state not in ["processing", "processed", "published", "unpublished", "deleted"]:
                    raise BBBException("invalidRecordingState", "Invalid recording state given.")
        params = {"meetingID": meeting_id, "recordID": recording_id}
        if meta:
            for key, val in meta.items():
                params["meta_" + key] = val

        response = self.__send_api_request(ApiMethod.GET_RECORDINGS, params)
        return GetRecordingsResponse(response)

    def publish_recordings(self, recording_id, publish=True):
        params = {"recordID": recording_id, "publish": "true" if publish else "false"}
        response = self.__send_api_request(ApiMethod.PUBLISH_RECORDINGS, params)
        return PublishRecordingsResponse(response)

    def delete_recordings(self, recording_id):
        params = {"recordID": recording_id}
        response = self.__send_api_request(ApiMethod.DELETE_RECORDINGS, params)
        return DeleteRecordingsResponse(response)

    def update_recordings(self, recording_id, meta={}):
        params = {"recordID": recording_id}
        if meta != {}:
            for key, val in meta.items():
                params["meta_" + key] = val
        response = self.__send_api_request(ApiMethod.UPDATE_RECORDINGS, params)
        return UpdateRecordingsResponse(response)

    # get default config.xml, if file_path is not given, this function will return response
    # as ElementTree.Element, otherwise it saves the response to the specific file path
    def get_default_config_xml(self, file_path=None):
        url = self.__urlBuilder.buildUrl(ApiMethod.GET_DEFAULT_CONFIG_XML)
        response = urlopen(url).read()
        if file_path is None:
            return response
        else:
            with open(file_path, 'w') as f:
                f.write(response.decode('utf-8'))

    def set_config_xml(self, meeting_id, xml):
        secret = ApiMethod.SET_CONFIG_XML + "configXML=" + quote(xml)
        secret += "&meetingID=" + meeting_id
        secret += self.__urlBuilder.securitySalt

        securityStr = sha1(secret.encode('utf-8')).hexdigest()

        response = self.__send_api_request(ApiMethod.SET_CONFIG_XML, data={"checksum": securityStr,
                                                                           "configXML": quote(xml),
                                                                           "meetingID": meeting_id})
        return SetConfigXMLResponse(response)

    def __send_api_request(self, api_call, params={}, data=None):
        url = self.__urlBuilder.buildUrl(api_call, params)

        # if data is none, then we send a GET request, if not, then we send a POST request
        if data is None:
            response = urlopen(url).read()
        else:
            response = urlopen(url, data=urlencode(data).encode()).read()

        try:
            rawXml = parse(response)["response"]
        except Exception as e:
            raise BBBException("XMLSyntaxError", e.message)

        # get default config xml request will simply return the xml file without
        # returncode, so it will cause an error when try to check the return code
        if api_call != ApiMethod.GET_DEFAULT_CONFIG_XML:
            if rawXml["returncode"] == "FAILED":
                raise BBBException(rawXml["messageKey"],
                                   rawXml["message"])

        return rawXml
