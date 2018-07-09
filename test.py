
from bigbluebutton import BigBlueButton
from lxml import etree
bbb = BigBlueButton("http://10.169.68.16/bigbluebutton/", "dff43c4faf419b0cd2471dd1d1523e61")
# print(bbb.get_api_version().get_version())

# response = bbb.create_meeting("abcefghi", {"moderatorPW": "0wYWDlAY"}, {"test": "val", "second_meta": "second_val"})
# print(response.get_moderator_pw())

print(bbb.get_join_meeting_url("jwang", "abcefg", "0wYWDlAY"))
print(bbb.get_join_meeting_url("test", "abcefg", "0wYWDlAY"))
# print(bbb.is_meeting_running("abcefghi").is_meeting_running())
# print(bbb.end_meeting("12", "0wYWDlAY").get_message())
# meetingInfo = bbb.get_meeting_info("abcefghi")


# attendees = meetingInfo.get_attendees()
# for attendee in attendees:
#     print("Attendee " + attendee.get_fullname() + " " + attendee.get_role() + " " + str(attendee.is_presenter()))

# meetings = bbb.get_meetings().get_meetings()
# for meeting in meetings:
#     print("Meeting: " + str(meeting.get_meetingid()) + " " + meeting.get_createdate())



# recordID = "f918576d108dd335180050096551eb92c107ebae-1527878116563"
# print(bbb.publish_recordings(recordID).is_published())
# print(bbb.publish_recordings(recordID, False).is_published())
#
# print(bbb.delete_recordings(recordID).is_deleted())

config='<config><localeversion suppressWarning="false">0.9.0</localeversion><version>879</version><help url="http://10.169.68.16/help.html"/><javaTest url="http://10.169.68.16/testjava.html"/>' \
       '<porttest host="rtmp://10.169.68.16" application="video/portTest" timeout="10000"/><bwMon server="rtmp://10.169.68.16" application="video/bwTest"/><application uri="rtmp://10.169.68.16/bigbluebutton"' \
       'host="http://10.169.68.16/bigbluebutton/api/enter" reconnWaitTime="2000"/><language userSelectionEnabled="true" rtlEnabled="false"/><skinning url="http://10.169.68.16/client/branding/css/V2Theme.css.swf?v=879"/>' \
       '<branding logo="logos/logo.swf" copyright="&#169; 2018 &lt;u&gt;&lt;a href=&quot;http://10.169.68.16/home.html&quot; target=&quot;_blank&quot;&gt;BigBlueButton Inc.&lt;/a&gt;&lt;/u&gt; (build {0})" background=""' \
       'toolbarColor="" showQuote="true"/><shortcutKeys showButton="true"/><browserVersions chrome="62" firefox="56" flash="23"/><layout showLogButton="false" defaultLayout="bbb.layout.name.defaultlayout" showToolbar="true"' \
       'showFooter="true" showMeetingName="true" showHelpButton="true" showLogoutWindow="true" showLayoutTools="true" confirmLogout="true" showNetworkMonitor="false" showRecordingNotification="true" logoutOnStopRecording="false"' \
       'askForFeedbackOnLogout="false"/><breakoutRooms enabled="true" record="false" privateChateEnabled="true"/><logging enabled="true" logTarget="trace" level="info" format="{dateUTC} {timeUTC} :: {name} :: [{logLevel}] {message}"' \
       'uri="http://10.169.68.16/log" logPattern=".*"/><lock disableCam="false" disableMic="false" disablePrivateChat="false" disablePublicChat="false" lockedLayout="false" lockOnJoin="true" lockOnJoinConfigurable="false"/><modules>' \
       '<module name="ChatModule" url="http://10.169.68.16/client/ChatModule.swf?v=879" uri="rtmp://10.169.68.16/bigbluebutton" dependsOn="UsersModule" privateEnabled="true" fontSize="14" baseTabIndex="801" colorPickerIsVisible="false"' \
       'maxMessageLength="1024"/><module name="UsersModule" url="http://10.169.68.16/client/UsersModule.swf?v=879" uri="rtmp://10.169.68.16/bigbluebutton" allowKickUser="true" enableEmojiStatus="true" enableSettingsButton="true"' \
       'enableGuestUI="false" moderatorUnmute="true" baseTabIndex="301"/><module name="ScreenshareModule" url="http://10.169.68.16/client/ScreenshareModule.swf?v=879" uri="rtmp://10.169.68.16/screenshare" showButton="true" enablePause="true"' \
       'offerWebRTC="false" shareRegionDefault="false" chromeExtensionLink="" chromeExtensionKey="" chromeWin10Help="http://10.169.68.16/client/help/webrtc-screenshare-help.html" baseTabIndex="201"' \
       'help="http://10.169.68.16/client/help/screenshare-help.html"/><module name="PhoneModule" url="http://10.169.68.16/client/PhoneModule.swf?v=879" uri="rtmp://10.169.68.16/sip" dependsOn="UsersModule" autoJoin="true"' \
       'listenOnlyMode="true" forceListenOnly="false" skipCheck="false" showButton="true" enabledEchoCancel="true" useWebRTCIfAvailable="true" showPhoneOption="false" showWebRTCStats="false" showWebRTCMOS="false" echoTestApp="9196"/>' \
       '<module name="VideoconfModule" url="http://10.169.68.16/client/VideoconfModule.swf?v=879" uri="rtmp://10.169.68.16/video" dependsOn="UsersModule" baseTabIndex="401" autoStart="false" skipCamSettingsCheck="false" showButton="true"' \
       'applyConvolutionFilter="false" convolutionFilter="-1, 0, -1, 0, 6, 0, -1, 0, -1" filterBias="0" filterDivisor="4" displayAvatar="false" priorityRatio="0.67"/><module name="WhiteboardModule" url="http://10.169.68.16/client/WhiteboardModule.swf?v=879"' \
       'uri="rtmp://10.169.68.16/bigbluebutton" dependsOn="PresentModule" baseTabIndex="601" keepToolbarVisible="false"/><module name="PollingModule" url="http://10.169.68.16/client/PollingModule.swf?v=879" uri="rtmp://10.169.68.16/bigbluebutton"' \
       'dependsOn="PresentModule"/><module name="PresentModule" url="http://10.169.68.16/client/PresentModule.swf?v=879" uri="rtmp://10.169.68.16/bigbluebutton" dependsOn="UsersModule" host="http://10.169.68.16" showPresentWindow="true"' \
       'showWindowControls="true" openExternalFileUploadDialog="false" baseTabIndex="501" maxFileSize="30" enableDownload="true" disableFirefoxF60Upload="true"/><module name="CaptionModule" url="http://10.169.68.16/client/CaptionModule.swf?v=879"' \
       'uri="rtmp://10.169.68.16/bigbluebutton" dependsOn="UsersModule" maxPasteLength="1024" baseTabIndex="701"/><module name="LayoutModule" url="http://10.169.68.16/client/LayoutModule.swf?v=879" uri="rtmp://10.169.68.16/bigbluebutton"' \
       'layoutConfig="http://10.169.68.16/client/conf/layout.xml" enableEdit="false"/><module name="SharedNotesModule" url="http://10.169.68.16/client/SharedNotesModule.swf?v=879" uri="rtmp://10.169.68.16/bigbluebutton" dependsOn="UsersModule"' \
       'refreshDelay="500" toolbarVisibleByDefault="false" showToolbarButton="true" fontSize="14" maxMessageLength="5000" maxNoteLength="10000" enableDeleteNotes="false" hideAdditionalNotes="false"/><!--<module name="NotesModule"' \
       'url="http://10.169.68.16/client/NotesModule.swf?v=879"saveURL="http://10.169.68.16"position="top-left"/><module name="BroadcastModule" url="http://10.169.68.16/client/BroadcastModule.swf?v=879" uri="rtmp://10.169.68.16/bigbluebutton"' \
       'streamsUri="http://10.169.68.16/streams.xml" position="top-left" showStreams="true" autoPlay="false" dependsOn="UsersModule"/>--></modules></config>'


# bbb.get_default_config_xml("/home/first/Desktop/test.xml")
print(etree.tostring(bbb.set_config_xml("12345", "test")))

