# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, transmission, Integer32, IpAddress, Counter32, Gauge32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from IP_MIB import ipNetToMediaNetAddress, ipNetToMediaIfIndex, ipNetToMediaPhysAddress, ipAdEntAddr
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus
from IF_MIB import InterfaceIndex, InterfaceIndexOrZero

class IPOA_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/IPOA-MIB'
	conformance = 3
	name = 'IPOA-MIB'
	language = 2
	description = 'This module defines a portion of the management\ninformation base (MIB) for managing Classical IP and\nARP over ATM entities.'

# nodes
class ipoaMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46])
	name = 'ipoaMIB'

class ipoaObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1])
	name = 'ipoaObjects'

class ipoaNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 2])
	name = 'ipoaNotifications'

class ipoaTrapPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 2, 0])
	name = 'ipoaTrapPrefix'

class ipoaConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 3])
	name = 'ipoaConformance'

class ipoaGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 3, 1])
	name = 'ipoaGroups'

class ipoaCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 3, 2])
	name = 'ipoaCompliances'


# macros
# types 

class IpoaEncapsType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'llcSnap'), Enum(2, 'vcMuxed'), Enum(3, 'other')]


class IpoaVpiInteger(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 255))


class IpoaVciInteger(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 65535))


class IpoaAtmAddr(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 40))
	format = '1x'


class IpoaAtmConnKind(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'pvc'), Enum(2, 'svcIncoming'), Enum(3, 'svcOutgoing'), Enum(4, 'spvcInitiator'), Enum(5, 'spvcTarget')]

# scalars 
class ipoaLisTrapEnable(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


# columns
class ipoaLisSubnetAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class ipoaLisDefaultMtu(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipoaLisDefaultEncapsType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 3])
	syntaxobject = IpoaEncapsType


class ipoaLisInactivityTimer(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class ipoaLisMinHoldingTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class ipoaLisQDepth(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'packets'


class ipoaLisMaxCalls(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipoaLisCacheEntryAge(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class ipoaLisRetries(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipoaLisTimeout(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class ipoaLisDefaultPeakCellRate(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipoaLisActiveVcs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class ipoaLisRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class ipoaLisIfMappingIfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 3, 1, 1])
	syntaxobject = InterfaceIndex


class ipoaLisIfMappingRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class ipoaArpClientAtmAddr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 1])
	syntaxobject = IpoaAtmAddr


class ipoaArpClientSrvrInUse(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 2])
	syntaxobject = IpoaAtmAddr


class ipoaArpClientInArpInReqs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientInArpOutReqs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientInArpInReplies(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientInArpOutReplies(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientInArpInvalidInReqs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientInArpInvalidOutReqs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientArpInReqs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientArpOutReqs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientArpInReplies(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientArpOutReplies(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientArpInNaks(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientArpOutNaks(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientArpUnknownOps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientArpNoSrvrResps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpClientRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class ipoaArpSrvrAddr(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 1])
	syntaxobject = IpoaAtmAddr


class ipoaArpSrvrLis(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class ipoaArpSrvrInArpInReqs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpSrvrInArpOutReqs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpSrvrInArpInReplies(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpSrvrInArpOutReplies(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpSrvrInArpInvalidInReqs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpSrvrInArpInvalidOutReqs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpSrvrArpInReqs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpSrvrArpOutReplies(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpSrvrArpOutNaks(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpSrvrArpDupIpAddrs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpSrvrArpUnknownOps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class ipoaArpSrvrRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class ipoaArpRemoteSrvrAtmAddr(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 1])
	syntaxobject = IpoaAtmAddr


class ipoaArpRemoteSrvrRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class ipoaArpRemoteSrvrIfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 3])
	syntaxobject = InterfaceIndexOrZero


class ipoaArpRemoteSrvrIpAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class ipoaArpRemoteSrvrAdminStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down')]


class ipoaArpRemoteSrvrOperStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down')]


class ipoaVcVpi(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 1])
	syntaxobject = IpoaVpiInteger


class ipoaVcVci(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 2])
	syntaxobject = IpoaVciInteger


class ipoaVcType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 3])
	syntaxobject = IpoaAtmConnKind


class ipoaVcNegotiatedEncapsType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 4])
	syntaxobject = IpoaEncapsType


class ipoaVcNegotiatedMtu(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipoaConfigPvcIfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 1])
	syntaxobject = InterfaceIndex


class ipoaConfigPvcVpi(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 2])
	syntaxobject = IpoaVpiInteger


class ipoaConfigPvcVci(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 3])
	syntaxobject = IpoaVciInteger


class ipoaConfigPvcDefaultMtu(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ipoaConfigPvcRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class ipoaLisEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ipoaLisSubnetAddr], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1])
	access = 2
	rowstatus = ipoaLisRowStatus
	columns = {'ipoaLisSubnetAddr': ipoaLisSubnetAddr, 'ipoaLisDefaultMtu': ipoaLisDefaultMtu, 'ipoaLisDefaultEncapsType': ipoaLisDefaultEncapsType, 'ipoaLisInactivityTimer': ipoaLisInactivityTimer, 'ipoaLisMinHoldingTime': ipoaLisMinHoldingTime, 'ipoaLisQDepth': ipoaLisQDepth, 'ipoaLisMaxCalls': ipoaLisMaxCalls, 'ipoaLisCacheEntryAge': ipoaLisCacheEntryAge, 'ipoaLisRetries': ipoaLisRetries, 'ipoaLisTimeout': ipoaLisTimeout, 'ipoaLisDefaultPeakCellRate': ipoaLisDefaultPeakCellRate, 'ipoaLisActiveVcs': ipoaLisActiveVcs, 'ipoaLisRowStatus': ipoaLisRowStatus}


class ipoaLisIfMappingEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ipoaLisSubnetAddr, ipoaLisIfMappingIfIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 3, 1])
	access = 2
	rowstatus = ipoaLisIfMappingRowStatus
	columns = {'ipoaLisIfMappingIfIndex': ipoaLisIfMappingIfIndex, 'ipoaLisIfMappingRowStatus': ipoaLisIfMappingRowStatus}


class ipoaArpClientEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ipAdEntAddr], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1])
	access = 2
	rowstatus = ipoaArpClientRowStatus
	columns = {'ipoaArpClientAtmAddr': ipoaArpClientAtmAddr, 'ipoaArpClientSrvrInUse': ipoaArpClientSrvrInUse, 'ipoaArpClientInArpInReqs': ipoaArpClientInArpInReqs, 'ipoaArpClientInArpOutReqs': ipoaArpClientInArpOutReqs, 'ipoaArpClientInArpInReplies': ipoaArpClientInArpInReplies, 'ipoaArpClientInArpOutReplies': ipoaArpClientInArpOutReplies, 'ipoaArpClientInArpInvalidInReqs': ipoaArpClientInArpInvalidInReqs, 'ipoaArpClientInArpInvalidOutReqs': ipoaArpClientInArpInvalidOutReqs, 'ipoaArpClientArpInReqs': ipoaArpClientArpInReqs, 'ipoaArpClientArpOutReqs': ipoaArpClientArpOutReqs, 'ipoaArpClientArpInReplies': ipoaArpClientArpInReplies, 'ipoaArpClientArpOutReplies': ipoaArpClientArpOutReplies, 'ipoaArpClientArpInNaks': ipoaArpClientArpInNaks, 'ipoaArpClientArpOutNaks': ipoaArpClientArpOutNaks, 'ipoaArpClientArpUnknownOps': ipoaArpClientArpUnknownOps, 'ipoaArpClientArpNoSrvrResps': ipoaArpClientArpNoSrvrResps, 'ipoaArpClientRowStatus': ipoaArpClientRowStatus}


class ipoaArpSrvrEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ipAdEntAddr, ipoaArpSrvrAddr], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1])
	access = 2
	rowstatus = ipoaArpSrvrRowStatus
	columns = {'ipoaArpSrvrAddr': ipoaArpSrvrAddr, 'ipoaArpSrvrLis': ipoaArpSrvrLis, 'ipoaArpSrvrInArpInReqs': ipoaArpSrvrInArpInReqs, 'ipoaArpSrvrInArpOutReqs': ipoaArpSrvrInArpOutReqs, 'ipoaArpSrvrInArpInReplies': ipoaArpSrvrInArpInReplies, 'ipoaArpSrvrInArpOutReplies': ipoaArpSrvrInArpOutReplies, 'ipoaArpSrvrInArpInvalidInReqs': ipoaArpSrvrInArpInvalidInReqs, 'ipoaArpSrvrInArpInvalidOutReqs': ipoaArpSrvrInArpInvalidOutReqs, 'ipoaArpSrvrArpInReqs': ipoaArpSrvrArpInReqs, 'ipoaArpSrvrArpOutReplies': ipoaArpSrvrArpOutReplies, 'ipoaArpSrvrArpOutNaks': ipoaArpSrvrArpOutNaks, 'ipoaArpSrvrArpDupIpAddrs': ipoaArpSrvrArpDupIpAddrs, 'ipoaArpSrvrArpUnknownOps': ipoaArpSrvrArpUnknownOps, 'ipoaArpSrvrRowStatus': ipoaArpSrvrRowStatus}


class ipoaArpRemoteSrvrEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ipoaLisSubnetAddr, ipoaArpRemoteSrvrAtmAddr, ipoaArpRemoteSrvrIfIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1])
	access = 2
	rowstatus = ipoaArpRemoteSrvrRowStatus
	columns = {'ipoaArpRemoteSrvrAtmAddr': ipoaArpRemoteSrvrAtmAddr, 'ipoaArpRemoteSrvrRowStatus': ipoaArpRemoteSrvrRowStatus, 'ipoaArpRemoteSrvrIfIndex': ipoaArpRemoteSrvrIfIndex, 'ipoaArpRemoteSrvrIpAddr': ipoaArpRemoteSrvrIpAddr, 'ipoaArpRemoteSrvrAdminStatus': ipoaArpRemoteSrvrAdminStatus, 'ipoaArpRemoteSrvrOperStatus': ipoaArpRemoteSrvrOperStatus}


class ipoaVcEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ipNetToMediaIfIndex, ipNetToMediaNetAddress, ipoaVcVpi, ipoaVcVci], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1])
	access = 2
	columns = {'ipoaVcVpi': ipoaVcVpi, 'ipoaVcVci': ipoaVcVci, 'ipoaVcType': ipoaVcType, 'ipoaVcNegotiatedEncapsType': ipoaVcNegotiatedEncapsType, 'ipoaVcNegotiatedMtu': ipoaVcNegotiatedMtu}


class ipoaConfigPvcEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ipoaConfigPvcIfIndex, ipoaConfigPvcVpi, ipoaConfigPvcVci], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1])
	access = 2
	rowstatus = ipoaConfigPvcRowStatus
	columns = {'ipoaConfigPvcIfIndex': ipoaConfigPvcIfIndex, 'ipoaConfigPvcVpi': ipoaConfigPvcVpi, 'ipoaConfigPvcVci': ipoaConfigPvcVci, 'ipoaConfigPvcDefaultMtu': ipoaConfigPvcDefaultMtu, 'ipoaConfigPvcRowStatus': ipoaConfigPvcRowStatus}


# notifications (traps) 
class ipoaMtuExceeded(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 1])

class ipoaDuplicateIpAddress(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 2])

class ipoaLisCreate(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 3])

class ipoaLisDelete(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 4])

# groups 
class ipoaGeneralGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 1])
	group = [ipoaVcType, ipoaVcNegotiatedEncapsType, ipoaVcNegotiatedMtu, ipoaConfigPvcDefaultMtu, ipoaConfigPvcRowStatus]

class ipoaClientGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 2])
	group = [ipoaArpClientAtmAddr, ipoaArpClientSrvrInUse, ipoaArpClientInArpInReqs, ipoaArpClientInArpOutReqs, ipoaArpClientInArpInReplies, ipoaArpClientInArpOutReplies, ipoaArpClientInArpInvalidInReqs, ipoaArpClientInArpInvalidOutReqs, ipoaArpClientArpInReqs, ipoaArpClientArpOutReqs, ipoaArpClientArpInReplies, ipoaArpClientArpOutReplies, ipoaArpClientArpInNaks, ipoaArpClientArpOutNaks, ipoaArpClientArpUnknownOps, ipoaArpClientArpNoSrvrResps, ipoaArpClientRowStatus]

class ipoaSrvrGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 3])
	group = [ipoaArpSrvrLis, ipoaArpSrvrInArpInReqs, ipoaArpSrvrInArpOutReqs, ipoaArpSrvrInArpInReplies, ipoaArpSrvrInArpOutReplies, ipoaArpSrvrInArpInvalidInReqs, ipoaArpSrvrInArpInvalidOutReqs, ipoaArpSrvrArpInReqs, ipoaArpSrvrArpOutReplies, ipoaArpSrvrArpOutNaks, ipoaArpSrvrArpDupIpAddrs, ipoaArpSrvrArpUnknownOps, ipoaArpSrvrRowStatus]

class ipoaBasicNotificationsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 4])
	group = [ipoaMtuExceeded]

class ipoaSrvrNotificationsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 5])
	group = [ipoaDuplicateIpAddress]

class ipoaLisNotificationsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 6])
	group = [ipoaLisCreate, ipoaLisDelete]

class ipoaLisTableGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 7])
	group = [ipoaLisTrapEnable, ipoaLisSubnetAddr, ipoaLisDefaultMtu, ipoaLisDefaultEncapsType, ipoaLisInactivityTimer, ipoaLisMinHoldingTime, ipoaLisQDepth, ipoaLisMaxCalls, ipoaLisCacheEntryAge, ipoaLisRetries, ipoaLisTimeout, ipoaLisDefaultPeakCellRate, ipoaLisActiveVcs, ipoaLisRowStatus, ipoaLisIfMappingRowStatus, ipoaArpRemoteSrvrRowStatus, ipoaArpRemoteSrvrIpAddr, ipoaArpRemoteSrvrAdminStatus, ipoaArpRemoteSrvrOperStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
