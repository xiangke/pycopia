# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from ALARM_MIB import alarmListName, alarmModelIndex, alarmActiveDateAndTime, alarmActiveIndex
from RMON2_MIB import ZeroBasedCounter32
from SNMP_FRAMEWORK_MIB import SnmpAdminString
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Gauge32, mib_2
from IANA_ITU_ALARM_TC_MIB import IANAItuProbableCause, IANAItuEventType
from ITU_ALARM_TC_MIB import ItuPerceivedSeverity, ItuTrendIndication
from SNMPv2_TC import AutonomousType, RowPointer

class ITU_ALARM_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/ITU-ALARM-MIB'
	conformance = 132
	name = 'ITU-ALARM-MIB'
	language = 2
	description = 'The MIB module describes ITU Alarm information\nas defined in ITU Recommendation M.3100 [M.3100],\nX.733 [X.733] and X.736 [X.736].\n\nCopyright (C) The Internet Society (2004).  The\ninitial version of this MIB module was published\nin RFC 3877.  For full legal notices see the RFC\nitself.  Supplementary information may be available on:\nhttp://www.ietf.org/copyrights/ianamib.html'

# nodes
class ituAlarmMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121])
	name = 'ituAlarmMIB'

class ituAlarmObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1])
	name = 'ituAlarmObjects'

class ituAlarmModel(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 1])
	name = 'ituAlarmModel'

class ituAlarmActive(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2])
	name = 'ituAlarmActive'

class ituAlarmConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 2])
	name = 'ituAlarmConformance'

class ituAlarmCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 2, 1])
	name = 'ituAlarmCompliances'

class ituAlarmGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 2, 2])
	name = 'ituAlarmGroups'


# macros
# types 
# scalars 
# columns
class ituAlarmPerceivedSeverity(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 1, 1, 1, 1])
	syntaxobject = ItuPerceivedSeverity


class ituAlarmEventType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 1, 1, 1, 2])
	syntaxobject = IANAItuEventType


class ituAlarmProbableCause(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 1, 1, 1, 3])
	syntaxobject = IANAItuProbableCause


class ituAlarmAdditionalText(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 1, 1, 1, 4])
	syntaxobject = SnmpAdminString


class ituAlarmGenericModel(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class ituAlarmActiveTrendIndication(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 1, 1, 1])
	syntaxobject = ItuTrendIndication


class ituAlarmActiveDetector(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.AutonomousType


class ituAlarmActiveServiceProvider(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.AutonomousType


class ituAlarmActiveServiceUser(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.AutonomousType


class ituAlarmActiveStatsIndeterminateCurrent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class ituAlarmActiveStatsCriticalCurrent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class ituAlarmActiveStatsMajorCurrent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class ituAlarmActiveStatsMinorCurrent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class ituAlarmActiveStatsWarningCurrent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class ituAlarmActiveStatsIndeterminates(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 6])
	syntaxobject = ZeroBasedCounter32


class ituAlarmActiveStatsCriticals(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 7])
	syntaxobject = ZeroBasedCounter32


class ituAlarmActiveStatsMajors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 8])
	syntaxobject = ZeroBasedCounter32


class ituAlarmActiveStatsMinors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 9])
	syntaxobject = ZeroBasedCounter32


class ituAlarmActiveStatsWarnings(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 10])
	syntaxobject = ZeroBasedCounter32


# rows 
class ituAlarmEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([alarmListName, alarmModelIndex, ituAlarmPerceivedSeverity], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 1, 1, 1])
	access = 2
	columns = {'ituAlarmPerceivedSeverity': ituAlarmPerceivedSeverity, 'ituAlarmEventType': ituAlarmEventType, 'ituAlarmProbableCause': ituAlarmProbableCause, 'ituAlarmAdditionalText': ituAlarmAdditionalText, 'ituAlarmGenericModel': ituAlarmGenericModel}


class ituAlarmActiveEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([alarmListName, alarmActiveDateAndTime, alarmActiveIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 1, 1])
	access = 2
	columns = {'ituAlarmActiveTrendIndication': ituAlarmActiveTrendIndication, 'ituAlarmActiveDetector': ituAlarmActiveDetector, 'ituAlarmActiveServiceProvider': ituAlarmActiveServiceProvider, 'ituAlarmActiveServiceUser': ituAlarmActiveServiceUser}


class ituAlarmActiveStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([alarmListName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1])
	access = 2
	columns = {'ituAlarmActiveStatsIndeterminateCurrent': ituAlarmActiveStatsIndeterminateCurrent, 'ituAlarmActiveStatsCriticalCurrent': ituAlarmActiveStatsCriticalCurrent, 'ituAlarmActiveStatsMajorCurrent': ituAlarmActiveStatsMajorCurrent, 'ituAlarmActiveStatsMinorCurrent': ituAlarmActiveStatsMinorCurrent, 'ituAlarmActiveStatsWarningCurrent': ituAlarmActiveStatsWarningCurrent, 'ituAlarmActiveStatsIndeterminates': ituAlarmActiveStatsIndeterminates, 'ituAlarmActiveStatsCriticals': ituAlarmActiveStatsCriticals, 'ituAlarmActiveStatsMajors': ituAlarmActiveStatsMajors, 'ituAlarmActiveStatsMinors': ituAlarmActiveStatsMinors, 'ituAlarmActiveStatsWarnings': ituAlarmActiveStatsWarnings}


# notifications (traps) 
# groups 
class ituAlarmGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 2, 2, 1])
	group = [ituAlarmEventType, ituAlarmProbableCause, ituAlarmGenericModel]

class ituAlarmServiceUserGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 2, 2, 2])
	group = [ituAlarmAdditionalText, ituAlarmActiveTrendIndication]

class ituAlarmSecurityGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 2, 2, 3])
	group = [ituAlarmActiveDetector, ituAlarmActiveServiceProvider, ituAlarmActiveServiceUser]

class ituAlarmStatisticsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 121, 2, 2, 4])
	group = [ituAlarmActiveStatsIndeterminateCurrent, ituAlarmActiveStatsCriticalCurrent, ituAlarmActiveStatsMajorCurrent, ituAlarmActiveStatsMinorCurrent, ituAlarmActiveStatsWarningCurrent, ituAlarmActiveStatsIndeterminates, ituAlarmActiveStatsCriticals, ituAlarmActiveStatsMajors, ituAlarmActiveStatsMinors, ituAlarmActiveStatsWarnings]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
