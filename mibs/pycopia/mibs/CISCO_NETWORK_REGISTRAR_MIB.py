# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, IpAddress
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import TEXTUAL_CONVENTION, DisplayString
from CISCO_TC import Unsigned32

class CISCO_NETWORK_REGISTRAR_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-NETWORK-REGISTRAR-MIB'
	conformance = 2
	name = 'CISCO-NETWORK-REGISTRAR-MIB'
	language = 2
	description = 'MIB for Cisco Network Registrar (CNR)'

# nodes
class ciscoNetworkRegistrarMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120])
	name = 'ciscoNetworkRegistrarMIB'

class ciscoNetworkRegistrarMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1])
	name = 'ciscoNetworkRegistrarMIBObjects'

class cnrDHCP(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1])
	name = 'cnrDHCP'

class cnrNotifObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2])
	name = 'cnrNotifObjects'

class ciscoNetRegMIBNotificationPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2])
	name = 'ciscoNetRegMIBNotificationPrefix'

class ciscoNetRegMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0])
	name = 'ciscoNetRegMIBNotifications'

class ciscoNetworkRegistrarMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 1])
	name = 'ciscoNetworkRegistrarMIBCompliances'

class ciscoNetworkRegistrarMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 2])
	name = 'ciscoNetworkRegistrarMIBGroups'


# macros
# types 

class CnrPhysAddress(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(1, 32))

# scalars 
class cnrNotifDupIpAddress(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class cnrNotifMACAddress(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 2])
	syntaxobject = CnrPhysAddress


class cnrNotifServer(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 3])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class cnrNotifServerType(ScalarObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'dns'), Enum(2, 'dhcp'), Enum(3, 'ldap')]


class cnrNotifDupIpAddressDetectedBy(ScalarObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'dhcpClient'), Enum(2, 'dhcpServer')]


class cnrNotifContestedIpAddress(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 6])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


# columns
class cnrDHCPScopeName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cnrDHCPScopeFreeAddrLowThreshold(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cnrDHCPScopeFreeAddrHighThreshold(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cnrDHCPScopeFreeAddrValue(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cnrDHCPScopeFreeAddrUnits(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'value'), Enum(2, 'percent')]


# rows 
class cnrDHCPScopeEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cnrDHCPScopeName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1, 1])
	access = 2
	columns = {'cnrDHCPScopeName': cnrDHCPScopeName, 'cnrDHCPScopeFreeAddrLowThreshold': cnrDHCPScopeFreeAddrLowThreshold, 'cnrDHCPScopeFreeAddrHighThreshold': cnrDHCPScopeFreeAddrHighThreshold, 'cnrDHCPScopeFreeAddrValue': cnrDHCPScopeFreeAddrValue, 'cnrDHCPScopeFreeAddrUnits': cnrDHCPScopeFreeAddrUnits}


# notifications (traps) 
class ciscoNetRegFreeAddressLow(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 1])

class ciscoNetRegFreeAddressHigh(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 2])

class ciscoNetRegServerStart(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 3])

class ciscoNetRegServerStop(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 4])

class ciscoNetRegDNSQueueTooBig(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 5])

class ciscoNetRegOtherServerNotResponding(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 6])

class ciscoNetRegDuplicateAddress(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 7])

class ciscoNetRegAddressConflict(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 8])

class ciscoNetRegOtherServerResponding(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 9])

class ciscoNetRegFailoverConfigMismatch(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 10])

# groups 
class ciscoNetworkRegistrarDHCPScopeObjectsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 2, 1])
	group = [cnrDHCPScopeFreeAddrLowThreshold, cnrDHCPScopeFreeAddrHighThreshold, cnrDHCPScopeFreeAddrValue, cnrDHCPScopeFreeAddrUnits]

class ciscoNetworkRegistrarNotifObjectsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 2, 2])
	group = [cnrNotifDupIpAddress, cnrNotifMACAddress, cnrNotifDupIpAddressDetectedBy, cnrNotifServer, cnrNotifServerType, cnrNotifContestedIpAddress]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
