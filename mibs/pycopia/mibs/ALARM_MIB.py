# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from SNMP_FRAMEWORK_MIB import SnmpAdminString
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Integer32, Unsigned32, Gauge32, TimeTicks, Counter32, Counter64, IpAddress, Opaque, mib_2, zeroDotZero
from RMON2_MIB import ZeroBasedCounter32
from INET_ADDRESS_MIB import InetAddressType, InetAddress
from SNMPv2_TC import DateAndTime, RowStatus, RowPointer, TEXTUAL_CONVENTION

class ALARM_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/ALARM-MIB'
	conformance = 4
	name = 'ALARM-MIB'
	language = 2
	description = 'The MIB module describes a generic solution\nto model alarms and to store the current list\nof active alarms.\n\nCopyright (C) The Internet Society (2004).  The\ninitial version of this MIB module was published\nin RFC 3877.  For full legal notices see the RFC\nitself.  Supplementary information may be available on:\nhttp://www.ietf.org/copyrights/ianamib.html'

# nodes
class alarmMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118])
	name = 'alarmMIB'

class alarmNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 0])
	name = 'alarmNotifications'

class alarmObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1])
	name = 'alarmObjects'

class alarmModel(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1])
	name = 'alarmModel'

class alarmActive(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2])
	name = 'alarmActive'

class alarmClear(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3])
	name = 'alarmClear'

class alarmConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 2])
	name = 'alarmConformance'

class alarmCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 2, 1])
	name = 'alarmCompliances'

class alarmGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 2, 2])
	name = 'alarmGroups'


# macros
# types 

class ResourceId(pycopia.SMI.Basetypes.ObjectIdentifier):
	status = 1


class LocalSnmpEngineOrZeroLenStr(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 0), Range(5, 32))

# scalars 
class alarmModelLastChanged(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class alarmActiveLastChanged(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class alarmActiveOverflow(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'active alarms'


class alarmClearMaximum(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


# columns
class alarmModelIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class alarmModelState(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class alarmModelNotificationId(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class alarmModelVarbindIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class alarmModelVarbindValue(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class alarmModelDescription(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 6])
	syntaxobject = SnmpAdminString


class alarmModelSpecificPointer(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class alarmModelVarbindSubtree(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class alarmModelResourcePrefix(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class alarmModelRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class alarmListName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 1])
	syntaxobject = SnmpAdminString


class alarmActiveDateAndTime(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class alarmActiveIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class alarmActiveEngineID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 4])
	syntaxobject = LocalSnmpEngineOrZeroLenStr


class alarmActiveEngineAddressType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 5])
	syntaxobject = InetAddressType


class alarmActiveEngineAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 6])
	syntaxobject = InetAddress


class alarmActiveContextName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 7])
	syntaxobject = SnmpAdminString


class alarmActiveVariables(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class alarmActiveNotificationID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class alarmActiveResourceId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 10])
	syntaxobject = ResourceId


class alarmActiveDescription(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 11])
	syntaxobject = SnmpAdminString


class alarmActiveLogPointer(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class alarmActiveModelPointer(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class alarmActiveSpecificPointer(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class alarmActiveVariableIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class alarmActiveVariableID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class alarmActiveVariableValueType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'counter32'), Enum(2, 'unsigned32'), Enum(3, 'timeTicks'), Enum(4, 'integer32'), Enum(5, 'ipAddress'), Enum(6, 'octetString'), Enum(7, 'objectId'), Enum(8, 'counter64'), Enum(9, 'opaque')]


class alarmActiveVariableCounter32Val(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class alarmActiveVariableUnsigned32Val(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class alarmActiveVariableTimeTicksVal(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class alarmActiveVariableInteger32Val(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class alarmActiveVariableOctetStringVal(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class alarmActiveVariableIpAddressVal(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class alarmActiveVariableOidVal(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class alarmActiveVariableCounter64Val(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class alarmActiveVariableOpaqueVal(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Opaque


class alarmActiveStatsActiveCurrent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class alarmActiveStatsActives(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1, 2])
	syntaxobject = ZeroBasedCounter32


class alarmActiveStatsLastRaise(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class alarmActiveStatsLastClear(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class alarmClearIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class alarmClearDateAndTime(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class alarmClearEngineID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 3])
	syntaxobject = LocalSnmpEngineOrZeroLenStr


class alarmClearEngineAddressType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 4])
	syntaxobject = InetAddressType


class alarmClearEngineAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 5])
	syntaxobject = InetAddress


class alarmClearContextName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 6])
	syntaxobject = SnmpAdminString


class alarmClearNotificationID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class alarmClearResourceId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 8])
	syntaxobject = ResourceId


class alarmClearLogIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class alarmClearModelPointer(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


# rows 
class alarmModelEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([alarmListName, alarmModelIndex, alarmModelState], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1])
	access = 2
	rowstatus = alarmModelRowStatus
	columns = {'alarmModelIndex': alarmModelIndex, 'alarmModelState': alarmModelState, 'alarmModelNotificationId': alarmModelNotificationId, 'alarmModelVarbindIndex': alarmModelVarbindIndex, 'alarmModelVarbindValue': alarmModelVarbindValue, 'alarmModelDescription': alarmModelDescription, 'alarmModelSpecificPointer': alarmModelSpecificPointer, 'alarmModelVarbindSubtree': alarmModelVarbindSubtree, 'alarmModelResourcePrefix': alarmModelResourcePrefix, 'alarmModelRowStatus': alarmModelRowStatus}


class alarmActiveEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([alarmListName, alarmActiveDateAndTime, alarmActiveIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1])
	access = 2
	columns = {'alarmListName': alarmListName, 'alarmActiveDateAndTime': alarmActiveDateAndTime, 'alarmActiveIndex': alarmActiveIndex, 'alarmActiveEngineID': alarmActiveEngineID, 'alarmActiveEngineAddressType': alarmActiveEngineAddressType, 'alarmActiveEngineAddress': alarmActiveEngineAddress, 'alarmActiveContextName': alarmActiveContextName, 'alarmActiveVariables': alarmActiveVariables, 'alarmActiveNotificationID': alarmActiveNotificationID, 'alarmActiveResourceId': alarmActiveResourceId, 'alarmActiveDescription': alarmActiveDescription, 'alarmActiveLogPointer': alarmActiveLogPointer, 'alarmActiveModelPointer': alarmActiveModelPointer, 'alarmActiveSpecificPointer': alarmActiveSpecificPointer}


class alarmActiveVariableEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([alarmListName, alarmActiveIndex, alarmActiveVariableIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1])
	access = 2
	columns = {'alarmActiveVariableIndex': alarmActiveVariableIndex, 'alarmActiveVariableID': alarmActiveVariableID, 'alarmActiveVariableValueType': alarmActiveVariableValueType, 'alarmActiveVariableCounter32Val': alarmActiveVariableCounter32Val, 'alarmActiveVariableUnsigned32Val': alarmActiveVariableUnsigned32Val, 'alarmActiveVariableTimeTicksVal': alarmActiveVariableTimeTicksVal, 'alarmActiveVariableInteger32Val': alarmActiveVariableInteger32Val, 'alarmActiveVariableOctetStringVal': alarmActiveVariableOctetStringVal, 'alarmActiveVariableIpAddressVal': alarmActiveVariableIpAddressVal, 'alarmActiveVariableOidVal': alarmActiveVariableOidVal, 'alarmActiveVariableCounter64Val': alarmActiveVariableCounter64Val, 'alarmActiveVariableOpaqueVal': alarmActiveVariableOpaqueVal}


class alarmActiveStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([alarmListName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1])
	access = 2
	columns = {'alarmActiveStatsActiveCurrent': alarmActiveStatsActiveCurrent, 'alarmActiveStatsActives': alarmActiveStatsActives, 'alarmActiveStatsLastRaise': alarmActiveStatsLastRaise, 'alarmActiveStatsLastClear': alarmActiveStatsLastClear}


class alarmClearEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([alarmListName, alarmClearDateAndTime, alarmClearIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1])
	access = 2
	columns = {'alarmClearIndex': alarmClearIndex, 'alarmClearDateAndTime': alarmClearDateAndTime, 'alarmClearEngineID': alarmClearEngineID, 'alarmClearEngineAddressType': alarmClearEngineAddressType, 'alarmClearEngineAddress': alarmClearEngineAddress, 'alarmClearContextName': alarmClearContextName, 'alarmClearNotificationID': alarmClearNotificationID, 'alarmClearResourceId': alarmClearResourceId, 'alarmClearLogIndex': alarmClearLogIndex, 'alarmClearModelPointer': alarmClearModelPointer}


# notifications (traps) 
class alarmActiveState(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 0, 2])

class alarmClearState(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 0, 3])

# groups 
class alarmModelGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 2, 2, 1])
	group = [alarmModelLastChanged, alarmModelNotificationId, alarmModelVarbindIndex, alarmModelVarbindValue, alarmModelDescription, alarmModelSpecificPointer, alarmModelVarbindSubtree, alarmModelResourcePrefix, alarmModelRowStatus]

class alarmActiveGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 2, 2, 2])
	group = [alarmActiveLastChanged, alarmActiveOverflow, alarmActiveEngineID, alarmActiveEngineAddressType, alarmActiveEngineAddress, alarmActiveContextName, alarmActiveVariables, alarmActiveNotificationID, alarmActiveResourceId, alarmActiveDescription, alarmActiveLogPointer, alarmActiveModelPointer, alarmActiveSpecificPointer, alarmActiveVariableID, alarmActiveVariableValueType, alarmActiveVariableCounter32Val, alarmActiveVariableUnsigned32Val, alarmActiveVariableTimeTicksVal, alarmActiveVariableInteger32Val, alarmActiveVariableOctetStringVal, alarmActiveVariableIpAddressVal, alarmActiveVariableOidVal, alarmActiveVariableCounter64Val, alarmActiveVariableOpaqueVal]

class alarmActiveStatsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 2, 2, 3])
	group = [alarmActiveStatsActives, alarmActiveStatsActiveCurrent, alarmActiveStatsLastRaise, alarmActiveStatsLastClear]

class alarmClearGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 2, 2, 4])
	group = [alarmClearMaximum, alarmClearEngineID, alarmClearEngineAddressType, alarmClearEngineAddress, alarmClearContextName, alarmClearNotificationID, alarmClearResourceId, alarmClearLogIndex, alarmClearModelPointer]

class alarmNotificationsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 118, 2, 2, 6])
	group = [alarmActiveState, alarmClearState]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
