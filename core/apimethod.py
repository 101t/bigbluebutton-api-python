import sys
if sys.version_info[0] == 2:
    "2.x"
    from abc import ABCMeta
    class ApiMethod:
        __metaclass__ = ABCMeta
        VERSION                = ''
        CREATE                 = 'create'
        JOIN                   = 'join'
        END                    = 'end'
        IS_MEETING_RUNNING     = 'isMeetingRunning'
        GET_MEETING_INFO       = 'getMeetingInfo'
        GET_MEETINGS           = 'getMeetings'
        GET_DEFAULT_CONFIG_XML = 'getDefaultConfigXML'
        SET_CONFIG_XML         = 'setConfigXML'
        GET_RECORDINGS         = 'getRecordings'
        PUBLISH_RECORDINGS     = 'publishRecordings'
        DELETE_RECORDINGS      = 'deleteRecordings'
        UPDATE_RECORDINGS      = 'updateRecordings'

else:
    "3.x"
    from abc import ABC
    class ApiMethod(ABC):
        VERSION                = ''
        CREATE                 = 'create'
        JOIN                   = 'join'
        END                    = 'end'
        IS_MEETING_RUNNING     = 'isMeetingRunning'
        GET_MEETING_INFO       = 'getMeetingInfo'
        GET_MEETINGS           = 'getMeetings'
        GET_DEFAULT_CONFIG_XML = 'getDefaultConfigXML'
        SET_CONFIG_XML         = 'setConfigXML'
        GET_RECORDINGS         = 'getRecordings'
        PUBLISH_RECORDINGS     = 'publishRecordings'
        DELETE_RECORDINGS      = 'deleteRecordings'
        UPDATE_RECORDINGS      = 'updateRecordings'