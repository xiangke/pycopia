# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from RFC_1212 import OBJECT_TYPE
from HP_ICF_OID import hpSwitch
from RFC1213_MIB import DisplayString
from HP_ICF_TC import HpSwitchPortType
from RFC1155_SMI import Counter, IpAddress

class STATISTICS_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/STATISTICS-MIB'
	conformance = 2
	name = 'STATISTICS-MIB'
	language = 1

# nodes
class hpSwitchStatistics(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9])
	name = 'hpSwitchStatistics'

class hpSwitchIpxStat(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1])
	name = 'hpSwitchIpxStat'

class hpSwitchIpStat(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2])
	name = 'hpSwitchIpStat'

class hpSwitchFdbInfo(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4])
	name = 'hpSwitchFdbInfo'

class hpSwitchStpStat(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 5])
	name = 'hpSwitchStpStat'

class hpSwitchMiscStat(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 6])
	name = 'hpSwitchMiscStat'

class hpSwitchFddiIpFragStat(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7])
	name = 'hpSwitchFddiIpFragStat'

class hpSwitchFddiSystemStat(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8])
	name = 'hpSwitchFddiSystemStat'

class hpABCStats(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9])
	name = 'hpABCStats'

class hpIgmpStats(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10])
	name = 'hpIgmpStats'

class hpLdbalStats(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11])
	name = 'hpLdbalStats'

class hpSwitchMacStats(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 12])
	name = 'hpSwitchMacStats'

class hpSwitchFlowControlStatus(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 13])
	name = 'hpSwitchFlowControlStatus'

class hpFECStatsTrunk(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14])
	name = 'hpFECStatsTrunk'

class hpFECStatsPort(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15])
	name = 'hpFECStatsPort'

class hpGvrpStats(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16])
	name = 'hpGvrpStats'

class hpSshStats(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17])
	name = 'hpSshStats'

class hpSwitchPhysicalPort(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 18])
	name = 'hpSwitchPhysicalPort'


# macros
# types 
MacAddress = pycopia.SMI.Basetypes.MacAddress

class VlanID(pycopia.SMI.Basetypes.Integer32):
	ranges = Ranges(Range(1, 65535))

# scalars 
class hpSwitchStpStatAdminStatus(ScalarObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 5, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enable'), Enum(2, 'disable')]


class hpSwitchCpuStat(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 6, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpSwitchFdbAddressCount(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 12, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# columns
class hpSwitchIpxStatIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1, 1, 1])
	syntaxobject = VlanID


class hpSwitchIpxStatNodeAddr(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class hpSwitchIpxStatGatewayAddr(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class hpSwitchIpxStatGatewayEncap(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ethernetII'), Enum(2, 'ieee8022'), Enum(3, 'snap'), Enum(4, 'ieee8023Raw'), Enum(5, 'noGateway')]


class hpSwitchIpxStatAdminStatus(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enable'), Enum(2, 'disable')]


class hpSwitchIpStatIndex(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 4, 1, 1])
	syntaxobject = VlanID


class hpSwitchIpStatAddr(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class hpSwitchIpStatMask(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class hpSwitchIpStatGatewayAddr(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class hpSwitchIpStatAdminStatus(ColumnObject):
	status = 5
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 2, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enable'), Enum(2, 'disable'), Enum(3, 'bootp')]


class hpSwitchVlanFdbId(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 1, 1, 1])
	syntaxobject = VlanID


class hpSwitchVlanFdbAddress(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class hpSwitchVlanFdbPort(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpSwitchPortFdbId(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpSwitchPortFdbAddress(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class hpSwitchFddiIpFragStatIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpSwitchFddiIpFragFramesFragmented(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpSwitchFddiIpFragFramesCreated(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpSwitchFddiIpFragFrameErrors(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpSwitchFddiSystemStatIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpSwitchFddiSystemOsVersion(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpSwitchFddiSystemRomVersion(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpSwitchFddiSystemMemoryTotal(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpSwitchFddiSystemMemoryFree(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpSwitchFddiSystemCpuUtil(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpSwitchFddiSystemBuildDirectory(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class hpSwitchFddiSystemBuildDate(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class hpSwitchFddiSystemBuildNumber(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class hpABCStatsVlanIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 1])
	syntaxobject = VlanID


class hpABCStatsPortIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpABCStatsPortType(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 3])
	syntaxobject = HpSwitchPortType


class hpABCStatsArpReplies(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpABCStatsIpxReplies(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpABCStatsIpRipControl(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'forwarding'), Enum(2, 'notforwarding')]


class hpABCStatsIpxRipSapControl(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'forwarding'), Enum(2, 'notforwarding')]


class hpIgmpStatsVlanIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1, 1, 1])
	syntaxobject = VlanID


class hpIgmpStatsActiveGroupAddr(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class hpIgmpStatsReports(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpIgmpStatsQueries(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpIgmpStatsQuerierAccessPort(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpIgmpStatsPortIndex(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpIgmpStatsPortType(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 2, 1, 2])
	syntaxobject = HpSwitchPortType


class hpIgmpStatsPortAccess(ColumnObject):
	status = 5
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'host'), Enum(2, 'router'), Enum(3, 'host-router')]


class hpIgmpStatsPortIndex2(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpIgmpStatsPortType2(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3, 1, 2])
	syntaxobject = HpSwitchPortType


class hpIgmpStatsPortAccess2(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'host'), Enum(2, 'router'), Enum(3, 'host-router')]


class hpIgmpStatsPortAgeTimer2(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpIgmpStatsPortLeaveTimer2(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpLdbalStatsPortIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpLdbalStatsPortState(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'disabled'), Enum(2, 'error'), Enum(3, 'initial'), Enum(4, 'notEstablished'), Enum(5, 'established'), Enum(6, 'topologyError')]


class hpLdbalStatsAdjacentSwitch(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class hpLdbalStatsPeerPort(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class hpSwitchFlowControlStatusPortIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 13, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpSwitchFlowControlState(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 13, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'off'), Enum(2, 'on'), Enum(3, 'on-rx'), Enum(4, 'on-tx')]


class hpFECStatsTrunkIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpFECStatsTrunkName(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpFECStatsTrunkNegotiationStatus(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'successful'), Enum(2, 'failed'), Enum(3, 'initialized')]


class hpFECStatsTrunkForwardingMode(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'sa-only'), Enum(2, 'sa-da'), Enum(3, 'none')]


class hpFECStatsTrunkFlushPktsEchoed(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpFECStatsPortIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpFECStatsPortTrunkNumber(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpFECStatsPortTrunkName(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpFECStatsPortMode(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'down'), Enum(2, 'forwarding'), Enum(3, 'blocking'), Enum(4, 'up')]


class hpFECStatsPortNegotiationStatus(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'successful'), Enum(2, 'failed'), Enum(3, 'initialized')]


class hpFECStatsPortHellosSent(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpFECStatsPortHellosReceived(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpFECStatsPortMySlowHello(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'fast'), Enum(2, 'slow')]


class hpFECStatsPortMyAutoMode(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'desirable'), Enum(2, 'auto')]


class hpFECStatsPortPartner(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class hpFECStatsPortFlushPktsEchoed(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpGvrpStatsVlanIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1, 1, 1])
	syntaxobject = VlanID


class hpGvrpStatsPortIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpGvrpStatsPortVlanMember(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'pending'), Enum(2, 'yes'), Enum(3, 'no')]


class hpGvrpPortIfOperStatus(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down')]


class hpPortGvrpCtrlStatus(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'learn'), Enum(2, 'block')]


class hpSshStatsSesIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpSshStatsSesType(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'console'), Enum(2, 'telnet'), Enum(3, 'ssh'), Enum(4, 'inactive')]


class hpSshStatsSourceIpPort(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpSshStatsSesVersion(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'version1'), Enum(2, 'version2'), Enum(255, 'noConnect')]


class hpSwitchPhysicalPortIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 18, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpSwitchPhysicalPortType(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 18, 1, 1, 2])
	syntaxobject = HpSwitchPortType


# rows 
class hpSwitchIpxStatEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpSwitchIpxStatIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 1, 1, 1])
	access = 2
	columns = {'hpSwitchIpxStatIndex': hpSwitchIpxStatIndex, 'hpSwitchIpxStatNodeAddr': hpSwitchIpxStatNodeAddr, 'hpSwitchIpxStatGatewayAddr': hpSwitchIpxStatGatewayAddr, 'hpSwitchIpxStatGatewayEncap': hpSwitchIpxStatGatewayEncap, 'hpSwitchIpxStatAdminStatus': hpSwitchIpxStatAdminStatus}


class hpSwitchVlanFdbAddrEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpSwitchVlanFdbId, hpSwitchVlanFdbAddress], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 1, 1])
	access = 2
	columns = {'hpSwitchVlanFdbId': hpSwitchVlanFdbId, 'hpSwitchVlanFdbAddress': hpSwitchVlanFdbAddress, 'hpSwitchVlanFdbPort': hpSwitchVlanFdbPort}


class hpSwitchPortFdbAddrEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpSwitchPortFdbId, hpSwitchPortFdbAddress], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 4, 2, 1])
	access = 2
	columns = {'hpSwitchPortFdbId': hpSwitchPortFdbId, 'hpSwitchPortFdbAddress': hpSwitchPortFdbAddress}


class hpSwitchFddiIpFragStatEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpSwitchFddiIpFragStatIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 7, 1, 1])
	access = 2
	columns = {'hpSwitchFddiIpFragStatIndex': hpSwitchFddiIpFragStatIndex, 'hpSwitchFddiIpFragFramesFragmented': hpSwitchFddiIpFragFramesFragmented, 'hpSwitchFddiIpFragFramesCreated': hpSwitchFddiIpFragFramesCreated, 'hpSwitchFddiIpFragFrameErrors': hpSwitchFddiIpFragFrameErrors}


class hpSwitchFddiSystemStatEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpSwitchFddiSystemStatIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 8, 1, 1])
	access = 2
	columns = {'hpSwitchFddiSystemStatIndex': hpSwitchFddiSystemStatIndex, 'hpSwitchFddiSystemOsVersion': hpSwitchFddiSystemOsVersion, 'hpSwitchFddiSystemRomVersion': hpSwitchFddiSystemRomVersion, 'hpSwitchFddiSystemMemoryTotal': hpSwitchFddiSystemMemoryTotal, 'hpSwitchFddiSystemMemoryFree': hpSwitchFddiSystemMemoryFree, 'hpSwitchFddiSystemCpuUtil': hpSwitchFddiSystemCpuUtil, 'hpSwitchFddiSystemBuildDirectory': hpSwitchFddiSystemBuildDirectory, 'hpSwitchFddiSystemBuildDate': hpSwitchFddiSystemBuildDate, 'hpSwitchFddiSystemBuildNumber': hpSwitchFddiSystemBuildNumber}


class hpABCStatsEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpABCStatsVlanIndex, hpABCStatsPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 9, 1, 1])
	access = 2
	columns = {'hpABCStatsVlanIndex': hpABCStatsVlanIndex, 'hpABCStatsPortIndex': hpABCStatsPortIndex, 'hpABCStatsPortType': hpABCStatsPortType, 'hpABCStatsArpReplies': hpABCStatsArpReplies, 'hpABCStatsIpxReplies': hpABCStatsIpxReplies, 'hpABCStatsIpRipControl': hpABCStatsIpRipControl, 'hpABCStatsIpxRipSapControl': hpABCStatsIpxRipSapControl}


class hpIgmpStatsEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpIgmpStatsVlanIndex, hpIgmpStatsActiveGroupAddr], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 1, 1])
	access = 2
	columns = {'hpIgmpStatsVlanIndex': hpIgmpStatsVlanIndex, 'hpIgmpStatsActiveGroupAddr': hpIgmpStatsActiveGroupAddr, 'hpIgmpStatsReports': hpIgmpStatsReports, 'hpIgmpStatsQueries': hpIgmpStatsQueries, 'hpIgmpStatsQuerierAccessPort': hpIgmpStatsQuerierAccessPort}


class hpIgmpStatsPortEntry2(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpIgmpStatsVlanIndex, hpIgmpStatsActiveGroupAddr, hpIgmpStatsPortIndex2], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 10, 3, 1])
	access = 2
	columns = {'hpIgmpStatsPortIndex2': hpIgmpStatsPortIndex2, 'hpIgmpStatsPortType2': hpIgmpStatsPortType2, 'hpIgmpStatsPortAccess2': hpIgmpStatsPortAccess2, 'hpIgmpStatsPortAgeTimer2': hpIgmpStatsPortAgeTimer2, 'hpIgmpStatsPortLeaveTimer2': hpIgmpStatsPortLeaveTimer2}


class hpLdbalStatsPortEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpLdbalStatsPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 11, 1, 1])
	access = 2
	columns = {'hpLdbalStatsPortIndex': hpLdbalStatsPortIndex, 'hpLdbalStatsPortState': hpLdbalStatsPortState, 'hpLdbalStatsAdjacentSwitch': hpLdbalStatsAdjacentSwitch, 'hpLdbalStatsPeerPort': hpLdbalStatsPeerPort}


class hpSwitchFlowControlStatusEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpSwitchFlowControlStatusPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 13, 1, 1])
	access = 2
	columns = {'hpSwitchFlowControlStatusPortIndex': hpSwitchFlowControlStatusPortIndex, 'hpSwitchFlowControlState': hpSwitchFlowControlState}


class hpFECStatsTrunkEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpFECStatsTrunkIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 14, 1, 1])
	access = 2
	columns = {'hpFECStatsTrunkIndex': hpFECStatsTrunkIndex, 'hpFECStatsTrunkName': hpFECStatsTrunkName, 'hpFECStatsTrunkNegotiationStatus': hpFECStatsTrunkNegotiationStatus, 'hpFECStatsTrunkForwardingMode': hpFECStatsTrunkForwardingMode, 'hpFECStatsTrunkFlushPktsEchoed': hpFECStatsTrunkFlushPktsEchoed}


class hpFECStatsPortEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpFECStatsPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 15, 1, 1])
	access = 2
	columns = {'hpFECStatsPortIndex': hpFECStatsPortIndex, 'hpFECStatsPortTrunkNumber': hpFECStatsPortTrunkNumber, 'hpFECStatsPortTrunkName': hpFECStatsPortTrunkName, 'hpFECStatsPortMode': hpFECStatsPortMode, 'hpFECStatsPortNegotiationStatus': hpFECStatsPortNegotiationStatus, 'hpFECStatsPortHellosSent': hpFECStatsPortHellosSent, 'hpFECStatsPortHellosReceived': hpFECStatsPortHellosReceived, 'hpFECStatsPortMySlowHello': hpFECStatsPortMySlowHello, 'hpFECStatsPortMyAutoMode': hpFECStatsPortMyAutoMode, 'hpFECStatsPortPartner': hpFECStatsPortPartner, 'hpFECStatsPortFlushPktsEchoed': hpFECStatsPortFlushPktsEchoed}


class hpGvrpStatsEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpGvrpStatsVlanIndex, hpGvrpStatsPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 16, 1, 1])
	access = 2
	columns = {'hpGvrpStatsVlanIndex': hpGvrpStatsVlanIndex, 'hpGvrpStatsPortIndex': hpGvrpStatsPortIndex, 'hpGvrpStatsPortVlanMember': hpGvrpStatsPortVlanMember, 'hpGvrpPortIfOperStatus': hpGvrpPortIfOperStatus, 'hpPortGvrpCtrlStatus': hpPortGvrpCtrlStatus}


class hpSshStatsEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpSshStatsSesIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 17, 1, 1])
	access = 2
	columns = {'hpSshStatsSesIndex': hpSshStatsSesIndex, 'hpSshStatsSesType': hpSshStatsSesType, 'hpSshStatsSourceIpPort': hpSshStatsSourceIpPort, 'hpSshStatsSesVersion': hpSshStatsSesVersion}


class hpSwitchPhysicalPortEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([hpSwitchPhysicalPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 18, 1, 1])
	access = 2
	columns = {'hpSwitchPhysicalPortIndex': hpSwitchPhysicalPortIndex, 'hpSwitchPhysicalPortType': hpSwitchPhysicalPortType}


# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
