# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Counter32, Integer32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoExperiment
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus, DisplayString
from IF_MIB import ifIndex

class CISCO_6400_CHASSIS_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-6400-CHASSIS-MIB'
	conformance = 3
	name = 'CISCO-6400-CHASSIS-MIB'
	language = 2
	description = '6400 Chassis MIB.'

# nodes
class cisco6400ChassisMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27])
	name = 'cisco6400ChassisMIB'

class cisco6400ChassisMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1])
	name = 'cisco6400ChassisMIBObjects'

class c64RedundantGroup(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1])
	name = 'c64RedundantGroup'

class c64ChassisGroup(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2])
	name = 'c64ChassisGroup'

class c64TelcoAlarmMgmt(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1])
	name = 'c64TelcoAlarmMgmt'

class cisco6400ChassisMIBNotificationPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 2])
	name = 'cisco6400ChassisMIBNotificationPrefix'

class cisco6400ChassisMIBNotification(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 2, 0])
	name = 'cisco6400ChassisMIBNotification'

class cisco6400ChassisMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 3])
	name = 'cisco6400ChassisMIBConformance'

class cisco6400ChassisMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 1])
	name = 'cisco6400ChassisMIBCompliances'

class cisco6400ChassisMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 2])
	name = 'cisco6400ChassisMIBGroups'


# macros
# types 

class APSEventStatus(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'good'), Enum(2, 'noHardware'), Enum(3, 'doNotRevert'), Enum(4, 'manualSwitch'), Enum(5, 'signgalDegrade'), Enum(6, 'forceSwitch'), Enum(7, 'lockOut'), Enum(8, 'adminDown')]

# scalars 
class c64MainCPUConfigAutoSync(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64MainCPUSwitchOver(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ok'), Enum(2, 'forceOver')]


class c64ChassisFacilityAlarmStatus(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64ChassisClearAlarms(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(0, 'done'), Enum(1, 'all'), Enum(2, 'minor'), Enum(3, 'major'), Enum(4, 'critical')]


class c64ChassisTempIntakeMinorThreshold(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64ChassisTempIntakeMajorThreshold(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64ChassisTempCoreMinorThreshold(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64ChassisTempCoreMajorThreshold(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64ChassisTempThresholdAdmin(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# columns
class c64SlotConfigModule1Index(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SlotConfigModule2Index(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64Slot1Name(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class c64Slot2Name(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class c64SlotConfigPrefIndex(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'primarySlot'), Enum(2, 'secondarySlot')]


class c64SlotSwitchOver(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ok'), Enum(2, 'forceOver')]


class c64SlotConfigStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class c64SubSlotRedundantIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SubSlotConfigModule1Index(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SubSlotConfigSubModule1Index(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SubSlotConfigModule2Index(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SubSlotConfigSubModule2Index(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SubSlot1Name(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class c64SubSlot2Name(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class c64SubSlotConfigPrefIndex(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'primarySubslot'), Enum(2, 'secondarySubslot')]


class c64SubSlotSwitchOver(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ok'), Enum(2, 'forceOver')]


class c64SubSlotConfigStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class c64PortConfigModule1Index(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64PortConfigSubModule1Index(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64PortConfigPort1Index(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64PortConfigModule2Index(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64PortConfigSubModule2Index(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64PortConfigPort2Index(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64Port1Name(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class c64Port2Name(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class c64PortConfigPrefIndex(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'primaryPort'), Enum(2, 'secondaryPort')]


class c64PortSwitchOver(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ok'), Enum(2, 'forceOver')]


class c64PortConfigStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class c64SonetAPSMode(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'linear'), Enum(2, 'yCable'), Enum(3, 'disable')]


class c64SonetAPSBERThreshold(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SonetAPSSwitchCmd(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'lockOut'), Enum(2, 'forceWorking'), Enum(3, 'forceProtect'), Enum(4, 'manualWorking'), Enum(5, 'manualProtect'), Enum(6, 'clear')]


class c64SonetAPSWorkSectionStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SonetAPSWorkLineStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SonetAPSWorkPathStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SonetAPSWorkSectionBIPE(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class c64SonetAPSWorkLineBIPE(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class c64SonetAPSWorkLineFEBE(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class c64SonetAPSWorkPathBIPE(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class c64SonetAPSWorkPathFEBE(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class c64SonetAPSWorkPortStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 9])
	syntaxobject = APSEventStatus


class c64SonetAPSProtectSectionStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SonetAPSProtectLineStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SonetAPSProtectPathStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64SonetAPSProtectSectionBIPE(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class c64SonetAPSProtectLineBIPE(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class c64SonetAPSProtectLineFEBE(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class c64SonetAPSProtectPathBIPE(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class c64SonetAPSProtectPathFEBE(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class c64SonetAPSProtectPortStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 18])
	syntaxobject = APSEventStatus


class c64SonetAPSChannelStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 19])
	syntaxobject = APSEventStatus


class c64ChassisAlarmIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class c64ChassisAlarmSource(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class c64ChassisAlarmType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'coreTemp'), Enum(2, 'inletTemp'), Enum(3, 'totalFanFail'), Enum(4, 'partialFanFail'), Enum(5, 'fanMissing'), Enum(6, 'pem0Fail'), Enum(7, 'pem1Fail'), Enum(8, 'sonetLineFail'), Enum(9, 'cardOIRAlarm'), Enum(10, 'cardFail'), Enum(11, 'cardPartialFail'), Enum(12, 'linkDownAlarm'), Enum(13, 'networkClockAlarm'), Enum(14, 'nrpSARFail'), Enum(15, 'nrpPAMDataError')]


class c64ChassisAlarmSeverity(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'minor'), Enum(2, 'major'), Enum(3, 'critical')]


class c64ChassisAlarmACOStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'normal'), Enum(2, 'cutoff')]


# rows 
class c64SlotConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([c64SlotConfigModule1Index, c64SlotConfigModule2Index], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1])
	access = 2
	rowstatus = c64SlotConfigStatus
	columns = {'c64SlotConfigModule1Index': c64SlotConfigModule1Index, 'c64SlotConfigModule2Index': c64SlotConfigModule2Index, 'c64Slot1Name': c64Slot1Name, 'c64Slot2Name': c64Slot2Name, 'c64SlotConfigPrefIndex': c64SlotConfigPrefIndex, 'c64SlotSwitchOver': c64SlotSwitchOver, 'c64SlotConfigStatus': c64SlotConfigStatus}


class c64SubSlotConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([c64SubSlotConfigModule1Index, c64SubSlotConfigSubModule1Index, c64SubSlotConfigModule2Index, c64SubSlotConfigSubModule2Index, c64SubSlotRedundantIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1])
	access = 2
	rowstatus = c64SubSlotConfigStatus
	columns = {'c64SubSlotRedundantIndex': c64SubSlotRedundantIndex, 'c64SubSlotConfigModule1Index': c64SubSlotConfigModule1Index, 'c64SubSlotConfigSubModule1Index': c64SubSlotConfigSubModule1Index, 'c64SubSlotConfigModule2Index': c64SubSlotConfigModule2Index, 'c64SubSlotConfigSubModule2Index': c64SubSlotConfigSubModule2Index, 'c64SubSlot1Name': c64SubSlot1Name, 'c64SubSlot2Name': c64SubSlot2Name, 'c64SubSlotConfigPrefIndex': c64SubSlotConfigPrefIndex, 'c64SubSlotSwitchOver': c64SubSlotSwitchOver, 'c64SubSlotConfigStatus': c64SubSlotConfigStatus}


class c64PortConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([c64PortConfigModule1Index, c64PortConfigSubModule1Index, c64PortConfigPort1Index, c64PortConfigModule2Index, c64PortConfigSubModule2Index, c64PortConfigPort2Index, c64SubSlotRedundantIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1])
	access = 2
	rowstatus = c64PortConfigStatus
	columns = {'c64PortConfigModule1Index': c64PortConfigModule1Index, 'c64PortConfigSubModule1Index': c64PortConfigSubModule1Index, 'c64PortConfigPort1Index': c64PortConfigPort1Index, 'c64PortConfigModule2Index': c64PortConfigModule2Index, 'c64PortConfigSubModule2Index': c64PortConfigSubModule2Index, 'c64PortConfigPort2Index': c64PortConfigPort2Index, 'c64Port1Name': c64Port1Name, 'c64Port2Name': c64Port2Name, 'c64PortConfigPrefIndex': c64PortConfigPrefIndex, 'c64PortSwitchOver': c64PortSwitchOver, 'c64PortConfigStatus': c64PortConfigStatus}


class c64SonetAPSConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1])
	access = 2
	columns = {'c64SonetAPSMode': c64SonetAPSMode, 'c64SonetAPSBERThreshold': c64SonetAPSBERThreshold, 'c64SonetAPSSwitchCmd': c64SonetAPSSwitchCmd}


class c64SonetAPSStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1])
	access = 2
	columns = {'c64SonetAPSWorkSectionStatus': c64SonetAPSWorkSectionStatus, 'c64SonetAPSWorkLineStatus': c64SonetAPSWorkLineStatus, 'c64SonetAPSWorkPathStatus': c64SonetAPSWorkPathStatus, 'c64SonetAPSWorkSectionBIPE': c64SonetAPSWorkSectionBIPE, 'c64SonetAPSWorkLineBIPE': c64SonetAPSWorkLineBIPE, 'c64SonetAPSWorkLineFEBE': c64SonetAPSWorkLineFEBE, 'c64SonetAPSWorkPathBIPE': c64SonetAPSWorkPathBIPE, 'c64SonetAPSWorkPathFEBE': c64SonetAPSWorkPathFEBE, 'c64SonetAPSWorkPortStatus': c64SonetAPSWorkPortStatus, 'c64SonetAPSProtectSectionStatus': c64SonetAPSProtectSectionStatus, 'c64SonetAPSProtectLineStatus': c64SonetAPSProtectLineStatus, 'c64SonetAPSProtectPathStatus': c64SonetAPSProtectPathStatus, 'c64SonetAPSProtectSectionBIPE': c64SonetAPSProtectSectionBIPE, 'c64SonetAPSProtectLineBIPE': c64SonetAPSProtectLineBIPE, 'c64SonetAPSProtectLineFEBE': c64SonetAPSProtectLineFEBE, 'c64SonetAPSProtectPathBIPE': c64SonetAPSProtectPathBIPE, 'c64SonetAPSProtectPathFEBE': c64SonetAPSProtectPathFEBE, 'c64SonetAPSProtectPortStatus': c64SonetAPSProtectPortStatus, 'c64SonetAPSChannelStatus': c64SonetAPSChannelStatus}


class c64ChassisAlarmEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([c64ChassisAlarmIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1])
	access = 2
	columns = {'c64ChassisAlarmIndex': c64ChassisAlarmIndex, 'c64ChassisAlarmSource': c64ChassisAlarmSource, 'c64ChassisAlarmType': c64ChassisAlarmType, 'c64ChassisAlarmSeverity': c64ChassisAlarmSeverity, 'c64ChassisAlarmACOStatus': c64ChassisAlarmACOStatus}


# notifications (traps) 
class cisco6400ChassisFailureNotification(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 2, 0, 1])

# groups 
class cisco6400RedundantGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 2, 1])
	group = [c64MainCPUConfigAutoSync, c64MainCPUSwitchOver, c64Slot1Name, c64Slot2Name, c64SlotConfigPrefIndex, c64SlotSwitchOver, c64SlotConfigStatus, c64SubSlot1Name, c64SubSlot2Name, c64SubSlotConfigPrefIndex, c64SubSlotSwitchOver, c64SubSlotConfigStatus, c64Port1Name, c64Port2Name, c64PortConfigPrefIndex, c64PortSwitchOver, c64PortConfigStatus, c64SonetAPSMode, c64SonetAPSBERThreshold, c64SonetAPSSwitchCmd, c64SonetAPSWorkSectionStatus, c64SonetAPSWorkLineStatus, c64SonetAPSWorkPathStatus, c64SonetAPSWorkSectionBIPE, c64SonetAPSWorkLineBIPE, c64SonetAPSWorkLineFEBE, c64SonetAPSWorkPathBIPE, c64SonetAPSWorkPathFEBE, c64SonetAPSWorkPortStatus, c64SonetAPSProtectSectionStatus, c64SonetAPSProtectLineStatus, c64SonetAPSProtectPathStatus, c64SonetAPSProtectSectionBIPE, c64SonetAPSProtectLineBIPE, c64SonetAPSProtectLineFEBE, c64SonetAPSProtectPathBIPE, c64SonetAPSProtectPathFEBE, c64SonetAPSProtectPortStatus, c64SonetAPSChannelStatus]

class cisco6400ChassisMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 2, 2])
	group = [c64ChassisFacilityAlarmStatus, c64ChassisClearAlarms, c64ChassisTempIntakeMinorThreshold, c64ChassisTempIntakeMajorThreshold, c64ChassisTempCoreMinorThreshold, c64ChassisTempCoreMajorThreshold, c64ChassisTempThresholdAdmin, c64ChassisAlarmIndex, c64ChassisAlarmSource, c64ChassisAlarmType, c64ChassisAlarmSeverity, c64ChassisAlarmACOStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
