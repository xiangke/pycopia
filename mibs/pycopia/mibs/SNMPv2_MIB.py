# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, TimeTicks, Counter32, snmpModules, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from SNMPv2_TC import DisplayString, TestAndIncr, TimeStamp

class SNMPv2_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/SNMPv2-MIB'
	conformance = 5
	name = 'SNMPv2-MIB'
	language = 2
	description = 'The MIB module for SNMP entities.\n\nCopyright (C) The Internet Society (2002). This\nversion of this MIB module is part of RFC 3418;\nsee the RFC itself for full legal notices.'

# nodes
class system(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1])
	name = 'system'

class snmp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11])
	name = 'snmp'

class snmpMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1])
	name = 'snmpMIB'

class snmpMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 1])
	name = 'snmpMIBObjects'

class snmpTrap(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 1, 4])
	name = 'snmpTrap'

class snmpTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 1, 5])
	name = 'snmpTraps'

class snmpSet(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 1, 6])
	name = 'snmpSet'

class snmpMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 2])
	name = 'snmpMIBConformance'

class snmpMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 2, 1])
	name = 'snmpMIBCompliances'

class snmpMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 2, 2])
	name = 'snmpMIBGroups'


# macros
# types 
# scalars 
class sysDescr(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sysObjectID(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class sysUpTime(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class sysContact(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sysName(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sysLocation(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sysServices(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sysORLastChange(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class snmpInPkts(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInBadVersions(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInBadCommunityNames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInBadCommunityUses(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpInASNParseErrs(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpEnableAuthenTraps(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 30])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class snmpSilentDrops(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 31])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpProxyDrops(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 11, 32])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snmpTrapOID(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 1, 4, 1])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class snmpTrapEnterprise(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 1, 4, 3])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class snmpSetSerialNo(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 1, 6, 1])
	syntaxobject = pycopia.SMI.Basetypes.TestAndIncr


# columns
class sysORIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 9, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sysORID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 9, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class sysORDescr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 9, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sysORUpTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 9, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


# rows 
class sysOREntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([sysORIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 1, 9, 1])
	access = 2
	columns = {'sysORIndex': sysORIndex, 'sysORID': sysORID, 'sysORDescr': sysORDescr, 'sysORUpTime': sysORUpTime}


# notifications (traps) 
class coldStart(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 1, 5, 1])

class warmStart(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 1, 5, 2])

class authenticationFailure(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 1, 5, 5])

# groups 
class snmpSetGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 2, 2, 5])
	group = [snmpSetSerialNo]

class systemGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 2, 2, 6])
	group = [sysDescr, sysObjectID, sysUpTime, sysContact, sysName, sysLocation, sysServices, sysORLastChange, sysORID, sysORUpTime, sysORDescr]

class snmpBasicNotificationsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 2, 2, 7])
	group = [coldStart, authenticationFailure]

class snmpGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 2, 2, 8])
	group = [snmpInPkts, snmpInBadVersions, snmpInASNParseErrs, snmpSilentDrops, snmpProxyDrops, snmpEnableAuthenTraps]

class snmpCommunityGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 2, 2, 9])
	group = [snmpInBadCommunityNames, snmpInBadCommunityUses]

class snmpWarmStartNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 2, 2, 11])
	group = [warmStart]

class snmpNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 1, 2, 2, 12])
	group = [snmpTrapOID, snmpTrapEnterprise]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
