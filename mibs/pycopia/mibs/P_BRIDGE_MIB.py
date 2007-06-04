# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Integer32, Counter64
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from BRIDGE_MIB import dot1dTp, dot1dTpPort, dot1dBridge, dot1dBasePortEntry, dot1dBasePort
from SNMPv2_TC import TruthValue, TimeInterval, MacAddress, TEXTUAL_CONVENTION

class P_BRIDGE_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/P-BRIDGE-MIB'
	conformance = 4
	name = 'P-BRIDGE-MIB'
	language = 2
	description = 'The Bridge MIB Extension module for managing Priority\nand Multicast Filtering, defined by IEEE 802.1D-1998,\nincluding Restricted Group Registration defined by\nIEEE 802.1t-2001.\n\nCopyright (C) The Internet Society (2006).  This version of\nthis MIB module is part of RFC 4363; See the RFC itself for\nfull legal notices.'

# nodes
class pBridgeMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6])
	name = 'pBridgeMIB'

class pBridgeMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1])
	name = 'pBridgeMIBObjects'

class dot1dExtBase(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 1])
	name = 'dot1dExtBase'

class dot1dPriority(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 2])
	name = 'dot1dPriority'

class dot1dGarp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 3])
	name = 'dot1dGarp'

class dot1dGmrp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 4])
	name = 'dot1dGmrp'

class pBridgeConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2])
	name = 'pBridgeConformance'

class pBridgeGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1])
	name = 'pBridgeGroups'

class pBridgeCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 2])
	name = 'pBridgeCompliances'


# macros
# types 

class EnabledStatus(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]

# scalars 
class dot1dDeviceCapabilities(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class dot1dTrafficClassesEnabled(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class dot1dGmrpStatus(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 3])
	syntaxobject = EnabledStatus


# columns
class dot1dTpHCPortInFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 4, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class dot1dTpHCPortOutFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 4, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class dot1dTpHCPortInDiscards(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 4, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class dot1dTpPortInOverflowFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 4, 6, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot1dTpPortOutOverflowFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 4, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot1dTpPortInOverflowDiscards(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 4, 6, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot1dPortCapabilities(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class dot1dPortDefaultUserPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot1dPortNumTrafficClasses(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot1dUserPriority(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot1dRegenUserPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot1dTrafficClassPriority(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot1dTrafficClass(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot1dPortOutboundAccessPriority(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot1dPortGarpJoinTime(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class dot1dPortGarpLeaveTime(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class dot1dPortGarpLeaveAllTime(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class dot1dPortGmrpStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 1])
	syntaxobject = EnabledStatus


class dot1dPortGmrpFailedRegistrations(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot1dPortGmrpLastPduOrigin(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class dot1dPortRestrictedGroupRegistration(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


# rows 
class dot1dTpHCPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot1dTpPort], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 4, 5, 1])
	access = 2
	columns = {'dot1dTpHCPortInFrames': dot1dTpHCPortInFrames, 'dot1dTpHCPortOutFrames': dot1dTpHCPortOutFrames, 'dot1dTpHCPortInDiscards': dot1dTpHCPortInDiscards}


class dot1dTpPortOverflowEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot1dTpPort], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 4, 6, 1])
	access = 2
	columns = {'dot1dTpPortInOverflowFrames': dot1dTpPortInOverflowFrames, 'dot1dTpPortOutOverflowFrames': dot1dTpPortOutOverflowFrames, 'dot1dTpPortInOverflowDiscards': dot1dTpPortInOverflowDiscards}


from BRIDGE_MIB import dot1dBasePort
class dot1dPortCapabilitiesEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot1dBasePort], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 4, 1])
	access = 2
	columns = {'dot1dPortCapabilities': dot1dPortCapabilities}


from BRIDGE_MIB import dot1dBasePort
class dot1dPortPriorityEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot1dBasePort], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1, 1])
	access = 2
	columns = {'dot1dPortDefaultUserPriority': dot1dPortDefaultUserPriority, 'dot1dPortNumTrafficClasses': dot1dPortNumTrafficClasses}


class dot1dUserPriorityRegenEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot1dBasePort, dot1dUserPriority], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2, 1])
	access = 2
	columns = {'dot1dUserPriority': dot1dUserPriority, 'dot1dRegenUserPriority': dot1dRegenUserPriority}


class dot1dTrafficClassEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot1dBasePort, dot1dTrafficClassPriority], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3, 1])
	access = 2
	columns = {'dot1dTrafficClassPriority': dot1dTrafficClassPriority, 'dot1dTrafficClass': dot1dTrafficClass}


class dot1dPortOutboundAccessPriorityEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot1dBasePort, dot1dRegenUserPriority], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 4, 1])
	access = 2
	columns = {'dot1dPortOutboundAccessPriority': dot1dPortOutboundAccessPriority}


from BRIDGE_MIB import dot1dBasePort
class dot1dPortGarpEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot1dBasePort], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1])
	access = 2
	columns = {'dot1dPortGarpJoinTime': dot1dPortGarpJoinTime, 'dot1dPortGarpLeaveTime': dot1dPortGarpLeaveTime, 'dot1dPortGarpLeaveAllTime': dot1dPortGarpLeaveAllTime}


from BRIDGE_MIB import dot1dBasePort
class dot1dPortGmrpEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot1dBasePort], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1])
	access = 2
	columns = {'dot1dPortGmrpStatus': dot1dPortGmrpStatus, 'dot1dPortGmrpFailedRegistrations': dot1dPortGmrpFailedRegistrations, 'dot1dPortGmrpLastPduOrigin': dot1dPortGmrpLastPduOrigin, 'dot1dPortRestrictedGroupRegistration': dot1dPortRestrictedGroupRegistration}


# notifications (traps) 
# groups 
class pBridgeExtCapGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 1])
	group = [dot1dDeviceCapabilities, dot1dPortCapabilities]

class pBridgeDeviceGmrpGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 2])
	group = [dot1dGmrpStatus]

class pBridgeDevicePriorityGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 3])
	group = [dot1dTrafficClassesEnabled]

class pBridgeDefaultPriorityGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 4])
	group = [dot1dPortDefaultUserPriority]

class pBridgeRegenPriorityGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 5])
	group = [dot1dRegenUserPriority]

class pBridgePriorityGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 6])
	group = [dot1dPortNumTrafficClasses, dot1dTrafficClass]

class pBridgeAccessPriorityGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 7])
	group = [dot1dPortOutboundAccessPriority]

class pBridgePortGarpGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 8])
	group = [dot1dPortGarpJoinTime, dot1dPortGarpLeaveTime, dot1dPortGarpLeaveAllTime]

class pBridgePortGmrpGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 9])
	group = [dot1dPortGmrpStatus, dot1dPortGmrpFailedRegistrations, dot1dPortGmrpLastPduOrigin]

class pBridgeHCPortGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 10])
	group = [dot1dTpHCPortInFrames, dot1dTpHCPortOutFrames, dot1dTpHCPortInDiscards]

class pBridgePortOverflowGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 11])
	group = [dot1dTpPortInOverflowFrames, dot1dTpPortOutOverflowFrames, dot1dTpPortInOverflowDiscards]

class pBridgePortGmrpGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 12])
	group = [dot1dPortGmrpStatus, dot1dPortGmrpFailedRegistrations, dot1dPortGmrpLastPduOrigin, dot1dPortRestrictedGroupRegistration]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
