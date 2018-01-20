import sys
if sys.version_info[0] == 2:
	"2.x"
	from abc import ABCMeta, abstractmethod
	class ApiMethod:
		__metaclass__ = ABCMeta
		CREATE                 = 'create'
		JOIN                   = 'join'
		ENTER                  = 'enter'
		END                    = 'end'
		IS_MEETING_RUNNING     = 'isMeetingRunning'
		GET_MEETING_INFO       = 'getMeetingInfo'
		GET_MEETINGS           = 'getMeetings'
		GET_DEFAULT_CONFIG_XML = 'getDefaultConfigXML'
		SET_CONFIG_XML         = 'setConfigXML'
		CONFIG_XML             = 'configXML'
		SIGN_OUT               = 'signOut'
		GET_RECORDINGS         = 'getRecordings'
		PUBLISH_RECORDINGS     = 'publishRecordings'
		DELETE_RECORDINGS      = 'deleteRecordings'
		UPDATE_RECORDINGS      = 'updateRecordings'

else:
	"3.x"
	from abc import ABC, abstractmethod
	class ApiMethod(ABC):
		CREATE                 = 'create'
		JOIN                   = 'join'
		ENTER                  = 'enter'
		END                    = 'end'
		IS_MEETING_RUNNING     = 'isMeetingRunning'
		GET_MEETING_INFO       = 'getMeetingInfo'
		GET_MEETINGS           = 'getMeetings'
		GET_DEFAULT_CONFIG_XML = 'getDefaultConfigXML'
		SET_CONFIG_XML         = 'setConfigXML'
		CONFIG_XML             = 'configXML'
		SIGN_OUT               = 'signOut'
		GET_RECORDINGS         = 'getRecordings'
		PUBLISH_RECORDINGS     = 'publishRecordings'
		DELETE_RECORDINGS      = 'deleteRecordings'
		UPDATE_RECORDINGS      = 'updateRecordings'