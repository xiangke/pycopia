# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from RFC_1212 import OBJECT_TYPE
from RFC1213_MIB import PhysAddress
from RFC1155_SMI import experimental, Counter

class CLNS_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/CLNS-MIB'
	conformance = 2
	name = 'CLNS-MIB'
	language = 1

# nodes
class clns(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1])
	name = 'clns'

class clnp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1])
	name = 'clnp'

class error(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2])
	name = 'error'

class echo(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 3])
	name = 'echo'

class es_is(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 4])
	name = 'es-is'


# macros
# types 

class ClnpAddress(pycopia.SMI.Basetypes.OctetString):
	ranges = Ranges(Range(1, 21))

# scalars 
class clnpForwarding(ScalarObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'is'), Enum(2, 'es')]


class clnpDefaultLifeTime(ScalarObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpInReceives(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInHdrErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInAddrErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpForwPDUs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInUnknownNLPs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInUnknownULPs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInDiscards(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInDelivers(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutRequests(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutDiscards(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutNoRoutes(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpReasmTimeout(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpReasmReqds(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpReasmOKs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpReasmFails(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpSegOKs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpSegFails(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpSegCreates(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInOpts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 25])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutOpts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 26])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpRoutingDiscards(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 27])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrors(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrUnspecs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrProcs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrCksums(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrCongests(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrHdrs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrSegs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrIncomps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrDups(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrUnreachDsts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrUnknownDsts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrSRUnspecs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrSRSyntaxes(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrSRUnkAddrs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrSRBadPaths(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrHops(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrHopReassms(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrUnsOptions(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrUnsVersions(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrUnsSecurities(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 21])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrUnsSRs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 22])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrUnsRRs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 23])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpInErrInterferences(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 24])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrUnspecs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 25])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrProcs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 26])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrCksums(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 27])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrCongests(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 28])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrHdrs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 29])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrSegs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 30])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrIncomps(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 31])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrDups(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 32])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrUnreachDsts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 33])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrUnknownDsts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 34])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrSRUnspecs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 35])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrSRSyntaxes(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 36])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrSRUnkAddrs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 37])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrSRBadPaths(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 38])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrHops(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 39])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrHopReassms(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 40])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrUnsOptions(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 41])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrUnsVersions(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 42])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrUnsSecurities(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 43])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrUnsSRs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 44])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrUnsRRs(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 45])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class clnpOutErrInterferences(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 2, 46])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class esisESHins(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 4, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class esisESHouts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 4, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class esisISHins(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 4, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class esisISHouts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 4, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class esisRDUins(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 4, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class esisRDUouts(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 4, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# columns
class clnpAdEntAddr(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 21, 1, 1])
	syntaxobject = ClnpAddress


class clnpAdEntIfIndex(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 21, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpAdEntReasmMaxSize(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 21, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpRouteDest(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1, 1])
	syntaxobject = ClnpAddress


class clnpRouteIfIndex(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpRouteMetric1(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpRouteMetric2(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpRouteMetric3(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpRouteMetric4(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpRouteNextHop(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1, 7])
	syntaxobject = ClnpAddress


class clnpRouteType(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'invalid'), Enum(3, 'direct'), Enum(4, 'remote')]


class clnpRouteProto(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'local'), Enum(3, 'netmgmt'), Enum(9, 'is-is'), Enum(11, 'ciscoIgrp'), Enum(12, 'bbnSpfIgp'), Enum(13, 'ospf'), Enum(14, 'bgp')]


class clnpRouteAge(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpRouteMetric5(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpRouteInfo(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class clnpNetToMediaIfIndex(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 23, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpNetToMediaPhysAddress(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 23, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.PhysAddress


class clnpNetToMediaNetAddress(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 23, 1, 3])
	syntaxobject = ClnpAddress


class clnpNetToMediaType(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 23, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'invalid'), Enum(3, 'dynamic'), Enum(4, 'static')]


class clnpNetToMediaAge(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 23, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpNetToMediaHoldTime(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 23, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpMediaToNetIfIndex(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 24, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpMediaToNetAddress(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 24, 1, 2])
	syntaxobject = ClnpAddress


class clnpMediaToNetPhysAddress(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 24, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.PhysAddress


class clnpMediaToNetType(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 24, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'invalid'), Enum(3, 'dynamic'), Enum(4, 'static')]


class clnpMediaToNetAge(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 24, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class clnpMediaToNetHoldTime(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 24, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class clnpAddrEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([clnpAdEntAddr], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 21, 1])
	access = 2
	columns = {'clnpAdEntAddr': clnpAdEntAddr, 'clnpAdEntIfIndex': clnpAdEntIfIndex, 'clnpAdEntReasmMaxSize': clnpAdEntReasmMaxSize}


class clnpRouteEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([clnpRouteDest], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 22, 1])
	access = 2
	columns = {'clnpRouteDest': clnpRouteDest, 'clnpRouteIfIndex': clnpRouteIfIndex, 'clnpRouteMetric1': clnpRouteMetric1, 'clnpRouteMetric2': clnpRouteMetric2, 'clnpRouteMetric3': clnpRouteMetric3, 'clnpRouteMetric4': clnpRouteMetric4, 'clnpRouteNextHop': clnpRouteNextHop, 'clnpRouteType': clnpRouteType, 'clnpRouteProto': clnpRouteProto, 'clnpRouteAge': clnpRouteAge, 'clnpRouteMetric5': clnpRouteMetric5, 'clnpRouteInfo': clnpRouteInfo}


class clnpNetToMediaEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([clnpNetToMediaIfIndex, clnpNetToMediaNetAddress], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 23, 1])
	access = 2
	columns = {'clnpNetToMediaIfIndex': clnpNetToMediaIfIndex, 'clnpNetToMediaPhysAddress': clnpNetToMediaPhysAddress, 'clnpNetToMediaNetAddress': clnpNetToMediaNetAddress, 'clnpNetToMediaType': clnpNetToMediaType, 'clnpNetToMediaAge': clnpNetToMediaAge, 'clnpNetToMediaHoldTime': clnpNetToMediaHoldTime}


class clnpMediaToNetEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([clnpMediaToNetIfIndex, clnpMediaToNetPhysAddress], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 3, 1, 1, 24, 1])
	access = 2
	columns = {'clnpMediaToNetIfIndex': clnpMediaToNetIfIndex, 'clnpMediaToNetAddress': clnpMediaToNetAddress, 'clnpMediaToNetPhysAddress': clnpMediaToNetPhysAddress, 'clnpMediaToNetType': clnpMediaToNetType, 'clnpMediaToNetAge': clnpMediaToNetAge, 'clnpMediaToNetHoldTime': clnpMediaToNetHoldTime}


# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
