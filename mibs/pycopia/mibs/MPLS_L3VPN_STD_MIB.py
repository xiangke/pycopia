# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from VPN_TC_STD_MIB import VPNIdOrZero
from IF_MIB import InterfaceIndex, InterfaceIndexOrZero
from SNMP_FRAMEWORK_MIB import SnmpAdminString
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Integer32, Counter32, Unsigned32, Gauge32
from MPLS_TC_STD_MIB import mplsStdMIB
from IANA_RTPROTO_MIB import IANAipRouteProtocol
from INET_ADDRESS_MIB import InetAddress, InetAddressType, InetAddressPrefixLength, InetAutonomousSystemNumber
from MPLS_LSR_STD_MIB import MplsIndexType
from SNMPv2_TC import TEXTUAL_CONVENTION, TruthValue, RowStatus, TimeStamp, StorageType

class MPLS_L3VPN_STD_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/MPLS-L3VPN-STD-MIB'
	conformance = 3
	name = 'MPLS-L3VPN-STD-MIB'
	language = 2
	description = 'This MIB contains managed object definitions for the\nLayer-3 Multiprotocol Label Switching Virtual\nPrivate Networks.\n\nCopyright (C) The Internet Society (2006).  This\nversion of this MIB module is part of RFC4382; see\nthe RFC itself for full legal notices.'

# nodes
class mplsL3VpnMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11])
	name = 'mplsL3VpnMIB'

class mplsL3VpnNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 0])
	name = 'mplsL3VpnNotifications'

class mplsL3VpnObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1])
	name = 'mplsL3VpnObjects'

class mplsL3VpnScalars(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1])
	name = 'mplsL3VpnScalars'

class mplsL3VpnConf(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2])
	name = 'mplsL3VpnConf'

class mplsL3VpnPerf(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3])
	name = 'mplsL3VpnPerf'

class mplsL3VpnRoute(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4])
	name = 'mplsL3VpnRoute'

class mplsL3VpnConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 2])
	name = 'mplsL3VpnConformance'

class mplsL3VpnGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1])
	name = 'mplsL3VpnGroups'

class mplsL3VpnCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 2])
	name = 'mplsL3VpnCompliances'


# macros
# types 

class MplsL3VpnName(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 31))


class MplsL3VpnRouteDistinguisher(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 256))


class MplsL3VpnRtType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'import'), Enum(2, 'export'), Enum(3, 'both')]

# scalars 
class mplsL3VpnConfiguredVrfs(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class mplsL3VpnActiveVrfs(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class mplsL3VpnConnectedInterfaces(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class mplsL3VpnNotificationEnable(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class mplsL3VpnVrfConfMaxPossRts(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class mplsL3VpnVrfConfRteMxThrshTime(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 4
	units = 'seconds'


class mplsL3VpnIllLblRcvThrsh(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


# columns
class mplsL3VpnIfConfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1, 1, 1])
	syntaxobject = InterfaceIndex


class mplsL3VpnIfVpnClassification(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'carrierOfCarrier'), Enum(2, 'enterprise'), Enum(3, 'interProvider')]


class mplsL3VpnIfVpnRouteDistProtocol(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class mplsL3VpnIfConfStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class mplsL3VpnIfConfRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class mplsL3VpnVrfName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 1])
	syntaxobject = MplsL3VpnName


class mplsL3VpnVrfVpnId(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 2])
	syntaxobject = VPNIdOrZero


class mplsL3VpnVrfDescription(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 3])
	syntaxobject = SnmpAdminString


class mplsL3VpnVrfRD(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 4])
	syntaxobject = MplsL3VpnRouteDistinguisher


class mplsL3VpnVrfCreationTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class mplsL3VpnVrfOperStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down')]


class mplsL3VpnVrfActiveInterfaces(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class mplsL3VpnVrfAssociatedInterfaces(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class mplsL3VpnVrfConfMidRteThresh(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class mplsL3VpnVrfConfHighRteThresh(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class mplsL3VpnVrfConfMaxRoutes(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class mplsL3VpnVrfConfLastChanged(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class mplsL3VpnVrfConfRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class mplsL3VpnVrfConfAdminStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down'), Enum(3, 'testing')]


class mplsL3VpnVrfConfStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class mplsL3VpnVrfRTIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class mplsL3VpnVrfRTType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1, 3])
	syntaxobject = MplsL3VpnRtType


class mplsL3VpnVrfRT(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1, 4])
	syntaxobject = MplsL3VpnRouteDistinguisher


class mplsL3VpnVrfRTDescr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1, 5])
	syntaxobject = SnmpAdminString


class mplsL3VpnVrfRTRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class mplsL3VpnVrfRTStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class mplsL3VpnVrfSecIllegalLblVltns(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 6, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mplsL3VpnVrfSecDiscontinuityTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class mplsL3VpnVrfPerfRoutesAdded(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mplsL3VpnVrfPerfRoutesDeleted(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mplsL3VpnVrfPerfCurrNumRoutes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class mplsL3VpnVrfPerfRoutesDropped(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mplsL3VpnVrfPerfDiscTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class mplsL3VpnVrfRteInetCidrDestType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 1])
	syntaxobject = InetAddressType


class mplsL3VpnVrfRteInetCidrDest(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 2])
	syntaxobject = InetAddress


class mplsL3VpnVrfRteInetCidrPfxLen(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 3])
	syntaxobject = InetAddressPrefixLength


class mplsL3VpnVrfRteInetCidrPolicy(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class mplsL3VpnVrfRteInetCidrNHopType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 5])
	syntaxobject = InetAddressType


class mplsL3VpnVrfRteInetCidrNextHop(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 6])
	syntaxobject = InetAddress


class mplsL3VpnVrfRteInetCidrIfIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 7])
	syntaxobject = InterfaceIndexOrZero


class mplsL3VpnVrfRteInetCidrType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'reject'), Enum(3, 'local'), Enum(4, 'remote'), Enum(5, 'blackhole')]


class mplsL3VpnVrfRteInetCidrProto(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 9])
	syntaxobject = IANAipRouteProtocol


class mplsL3VpnVrfRteInetCidrAge(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class mplsL3VpnVrfRteInetCidrNextHopAS(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 11])
	syntaxobject = InetAutonomousSystemNumber


class mplsL3VpnVrfRteInetCidrMetric1(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mplsL3VpnVrfRteInetCidrMetric2(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mplsL3VpnVrfRteInetCidrMetric3(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mplsL3VpnVrfRteInetCidrMetric4(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mplsL3VpnVrfRteInetCidrMetric5(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mplsL3VpnVrfRteXCPointer(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 17])
	syntaxobject = MplsIndexType


class mplsL3VpnVrfRteInetCidrStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class mplsL3VpnIfConfEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsL3VpnVrfName, mplsL3VpnIfConfIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1, 1])
	access = 2
	rowstatus = mplsL3VpnIfConfRowStatus
	columns = {'mplsL3VpnIfConfIndex': mplsL3VpnIfConfIndex, 'mplsL3VpnIfVpnClassification': mplsL3VpnIfVpnClassification, 'mplsL3VpnIfVpnRouteDistProtocol': mplsL3VpnIfVpnRouteDistProtocol, 'mplsL3VpnIfConfStorageType': mplsL3VpnIfConfStorageType, 'mplsL3VpnIfConfRowStatus': mplsL3VpnIfConfRowStatus}


class mplsL3VpnVrfEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsL3VpnVrfName], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1])
	access = 2
	rowstatus = mplsL3VpnVrfConfRowStatus
	columns = {'mplsL3VpnVrfName': mplsL3VpnVrfName, 'mplsL3VpnVrfVpnId': mplsL3VpnVrfVpnId, 'mplsL3VpnVrfDescription': mplsL3VpnVrfDescription, 'mplsL3VpnVrfRD': mplsL3VpnVrfRD, 'mplsL3VpnVrfCreationTime': mplsL3VpnVrfCreationTime, 'mplsL3VpnVrfOperStatus': mplsL3VpnVrfOperStatus, 'mplsL3VpnVrfActiveInterfaces': mplsL3VpnVrfActiveInterfaces, 'mplsL3VpnVrfAssociatedInterfaces': mplsL3VpnVrfAssociatedInterfaces, 'mplsL3VpnVrfConfMidRteThresh': mplsL3VpnVrfConfMidRteThresh, 'mplsL3VpnVrfConfHighRteThresh': mplsL3VpnVrfConfHighRteThresh, 'mplsL3VpnVrfConfMaxRoutes': mplsL3VpnVrfConfMaxRoutes, 'mplsL3VpnVrfConfLastChanged': mplsL3VpnVrfConfLastChanged, 'mplsL3VpnVrfConfRowStatus': mplsL3VpnVrfConfRowStatus, 'mplsL3VpnVrfConfAdminStatus': mplsL3VpnVrfConfAdminStatus, 'mplsL3VpnVrfConfStorageType': mplsL3VpnVrfConfStorageType}


class mplsL3VpnVrfRTEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsL3VpnVrfName, mplsL3VpnVrfRTIndex, mplsL3VpnVrfRTType], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1])
	access = 2
	rowstatus = mplsL3VpnVrfRTRowStatus
	columns = {'mplsL3VpnVrfRTIndex': mplsL3VpnVrfRTIndex, 'mplsL3VpnVrfRTType': mplsL3VpnVrfRTType, 'mplsL3VpnVrfRT': mplsL3VpnVrfRT, 'mplsL3VpnVrfRTDescr': mplsL3VpnVrfRTDescr, 'mplsL3VpnVrfRTRowStatus': mplsL3VpnVrfRTRowStatus, 'mplsL3VpnVrfRTStorageType': mplsL3VpnVrfRTStorageType}


from MPLS_L3VPN_STD_MIB import mplsL3VpnVrfName
class mplsL3VpnVrfSecEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsL3VpnVrfName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 6, 1])
	access = 2
	columns = {'mplsL3VpnVrfSecIllegalLblVltns': mplsL3VpnVrfSecIllegalLblVltns, 'mplsL3VpnVrfSecDiscontinuityTime': mplsL3VpnVrfSecDiscontinuityTime}


from MPLS_L3VPN_STD_MIB import mplsL3VpnVrfName
class mplsL3VpnVrfPerfEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsL3VpnVrfName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1, 1])
	access = 2
	columns = {'mplsL3VpnVrfPerfRoutesAdded': mplsL3VpnVrfPerfRoutesAdded, 'mplsL3VpnVrfPerfRoutesDeleted': mplsL3VpnVrfPerfRoutesDeleted, 'mplsL3VpnVrfPerfCurrNumRoutes': mplsL3VpnVrfPerfCurrNumRoutes, 'mplsL3VpnVrfPerfRoutesDropped': mplsL3VpnVrfPerfRoutesDropped, 'mplsL3VpnVrfPerfDiscTime': mplsL3VpnVrfPerfDiscTime}


class mplsL3VpnVrfRteEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsL3VpnVrfName, mplsL3VpnVrfRteInetCidrDestType, mplsL3VpnVrfRteInetCidrDest, mplsL3VpnVrfRteInetCidrPfxLen, mplsL3VpnVrfRteInetCidrPolicy, mplsL3VpnVrfRteInetCidrNHopType, mplsL3VpnVrfRteInetCidrNextHop], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1])
	access = 2
	rowstatus = mplsL3VpnVrfRteInetCidrStatus
	columns = {'mplsL3VpnVrfRteInetCidrDestType': mplsL3VpnVrfRteInetCidrDestType, 'mplsL3VpnVrfRteInetCidrDest': mplsL3VpnVrfRteInetCidrDest, 'mplsL3VpnVrfRteInetCidrPfxLen': mplsL3VpnVrfRteInetCidrPfxLen, 'mplsL3VpnVrfRteInetCidrPolicy': mplsL3VpnVrfRteInetCidrPolicy, 'mplsL3VpnVrfRteInetCidrNHopType': mplsL3VpnVrfRteInetCidrNHopType, 'mplsL3VpnVrfRteInetCidrNextHop': mplsL3VpnVrfRteInetCidrNextHop, 'mplsL3VpnVrfRteInetCidrIfIndex': mplsL3VpnVrfRteInetCidrIfIndex, 'mplsL3VpnVrfRteInetCidrType': mplsL3VpnVrfRteInetCidrType, 'mplsL3VpnVrfRteInetCidrProto': mplsL3VpnVrfRteInetCidrProto, 'mplsL3VpnVrfRteInetCidrAge': mplsL3VpnVrfRteInetCidrAge, 'mplsL3VpnVrfRteInetCidrNextHopAS': mplsL3VpnVrfRteInetCidrNextHopAS, 'mplsL3VpnVrfRteInetCidrMetric1': mplsL3VpnVrfRteInetCidrMetric1, 'mplsL3VpnVrfRteInetCidrMetric2': mplsL3VpnVrfRteInetCidrMetric2, 'mplsL3VpnVrfRteInetCidrMetric3': mplsL3VpnVrfRteInetCidrMetric3, 'mplsL3VpnVrfRteInetCidrMetric4': mplsL3VpnVrfRteInetCidrMetric4, 'mplsL3VpnVrfRteInetCidrMetric5': mplsL3VpnVrfRteInetCidrMetric5, 'mplsL3VpnVrfRteXCPointer': mplsL3VpnVrfRteXCPointer, 'mplsL3VpnVrfRteInetCidrStatus': mplsL3VpnVrfRteInetCidrStatus}


# notifications (traps) 
class mplsL3VpnVrfUp(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 0, 1])

class mplsL3VpnVrfDown(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 0, 2])

class mplsL3VpnVrfRouteMidThreshExceeded(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 0, 3])

class mplsL3VpnVrfNumVrfRouteMaxThreshExceeded(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 0, 4])

class mplsL3VpnNumVrfSecIllglLblThrshExcd(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 0, 5])

class mplsL3VpnNumVrfRouteMaxThreshCleared(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 0, 6])

# groups 
class mplsL3VpnScalarGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 1])
	group = [mplsL3VpnConfiguredVrfs, mplsL3VpnActiveVrfs, mplsL3VpnConnectedInterfaces, mplsL3VpnNotificationEnable, mplsL3VpnVrfConfMaxPossRts, mplsL3VpnVrfConfRteMxThrshTime, mplsL3VpnIllLblRcvThrsh]

class mplsL3VpnVrfGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 2])
	group = [mplsL3VpnVrfVpnId, mplsL3VpnVrfDescription, mplsL3VpnVrfRD, mplsL3VpnVrfCreationTime, mplsL3VpnVrfOperStatus, mplsL3VpnVrfActiveInterfaces, mplsL3VpnVrfAssociatedInterfaces, mplsL3VpnVrfConfMidRteThresh, mplsL3VpnVrfConfHighRteThresh, mplsL3VpnVrfConfMaxRoutes, mplsL3VpnVrfConfLastChanged, mplsL3VpnVrfConfRowStatus, mplsL3VpnVrfConfAdminStatus, mplsL3VpnVrfConfStorageType]

class mplsL3VpnIfGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 3])
	group = [mplsL3VpnIfVpnClassification, mplsL3VpnIfVpnRouteDistProtocol, mplsL3VpnIfConfStorageType, mplsL3VpnIfConfRowStatus]

class mplsL3VpnPerfGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 4])
	group = [mplsL3VpnVrfPerfRoutesAdded, mplsL3VpnVrfPerfRoutesDeleted, mplsL3VpnVrfPerfCurrNumRoutes]

class mplsL3VpnPerfRouteGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 5])
	group = [mplsL3VpnVrfPerfRoutesDropped, mplsL3VpnVrfPerfDiscTime]

class mplsL3VpnSecGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 7])
	group = [mplsL3VpnVrfSecIllegalLblVltns, mplsL3VpnVrfSecDiscontinuityTime]

class mplsL3VpnVrfRteGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 8])
	group = [mplsL3VpnVrfRteInetCidrIfIndex, mplsL3VpnVrfRteInetCidrType, mplsL3VpnVrfRteInetCidrProto, mplsL3VpnVrfRteInetCidrAge, mplsL3VpnVrfRteInetCidrNextHopAS, mplsL3VpnVrfRteInetCidrMetric1, mplsL3VpnVrfRteInetCidrMetric2, mplsL3VpnVrfRteInetCidrMetric3, mplsL3VpnVrfRteInetCidrMetric4, mplsL3VpnVrfRteInetCidrMetric5, mplsL3VpnVrfRteXCPointer, mplsL3VpnVrfRteInetCidrStatus]

class mplsL3VpnVrfRTGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 9])
	group = [mplsL3VpnVrfRTDescr, mplsL3VpnVrfRT, mplsL3VpnVrfRTRowStatus, mplsL3VpnVrfRTStorageType]

class mplsL3VpnNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 10])
	group = [mplsL3VpnVrfUp, mplsL3VpnVrfDown, mplsL3VpnVrfRouteMidThreshExceeded, mplsL3VpnVrfNumVrfRouteMaxThreshExceeded, mplsL3VpnNumVrfSecIllglLblThrshExcd, mplsL3VpnNumVrfRouteMaxThreshCleared]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
