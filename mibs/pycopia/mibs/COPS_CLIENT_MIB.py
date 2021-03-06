# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Integer32, Unsigned32, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from INET_ADDRESS_MIB import InetAddressType, InetAddress
from SNMPv2_TC import TimeStamp, TimeInterval, RowStatus, TEXTUAL_CONVENTION

class COPS_CLIENT_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/COPS-CLIENT-MIB'
	conformance = 5
	name = 'COPS-CLIENT-MIB'
	language = 2
	description = 'The COPS Client MIB module'

# nodes
class copsClientMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89])
	name = 'copsClientMIB'

class copsClientMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1])
	name = 'copsClientMIBObjects'

class copsClientCapabilitiesGroup(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 1])
	name = 'copsClientCapabilitiesGroup'

class copsClientStatusGroup(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2])
	name = 'copsClientStatusGroup'

class copsClientConfigGroup(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 3])
	name = 'copsClientConfigGroup'

class copsClientConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 2])
	name = 'copsClientConformance'

class copsClientGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 2, 1])
	name = 'copsClientGroups'

class copsClientCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 2, 2])
	name = 'copsClientCompliances'


# macros
# types 

class CopsClientState(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'copsClientInvalid'), Enum(2, 'copsClientTcpconnected'), Enum(3, 'copsClientAuthenticating'), Enum(4, 'copsClientSecAccepted'), Enum(5, 'copsClientAccepted'), Enum(6, 'copsClientTimingout')]


class CopsServerEntryType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'copsServerStatic'), Enum(2, 'copsServerRedirect')]


class CopsErrorCode(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(0, 'errorOther'), Enum(1, 'errorBadHandle'), Enum(2, 'errorInvalidHandleReference'), Enum(3, 'errorBadMessageFormat'), Enum(4, 'errorUnableToProcess'), Enum(5, 'errorMandatoryClientSiMissing'), Enum(6, 'errorUnsupportedClientType'), Enum(7, 'errorMandatoryCopsObjectMissing'), Enum(8, 'errorClientFailure'), Enum(9, 'errorCommunicationFailure'), Enum(10, 'errorUnspecified'), Enum(11, 'errorShuttingDown'), Enum(12, 'errorRedirectToPreferredServer'), Enum(13, 'errorUnknownCopsObject'), Enum(14, 'errorAuthenticationFailure'), Enum(15, 'errorAuthenticationMissing')]


class CopsTcpPort(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 65535))


class CopsAuthType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(0, 'authNone'), Enum(1, 'authOther'), Enum(2, 'authIpSecAh'), Enum(3, 'authIpSecEsp'), Enum(4, 'authTls'), Enum(5, 'authCopsIntegrity')]

# scalars 
class copsClientCapabilities(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class copsClientServerConfigRetryAlgrm(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 3, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'sequential'), Enum(3, 'roundRobin')]


class copsClientServerConfigRetryCount(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 3, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class copsClientServerConfigRetryIntvl(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 3, 4])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval
	access = 5
	units = 'centi-seconds'


# columns
class copsClientServerAddressType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 1])
	syntaxobject = InetAddressType


class copsClientServerAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 2])
	syntaxobject = InetAddress


class copsClientServerClientType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class copsClientServerTcpPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 4])
	syntaxobject = CopsTcpPort


class copsClientServerType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 5])
	syntaxobject = CopsServerEntryType


class copsClientServerAuthType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 6])
	syntaxobject = CopsAuthType


class copsClientServerLastConnAttempt(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class copsClientState(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 8])
	syntaxobject = CopsClientState


class copsClientServerKeepaliveTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class copsClientServerAccountingTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class copsClientInPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientOutPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientInErrs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientLastError(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 14])
	syntaxobject = CopsErrorCode


class copsClientTcpConnectAttempts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientTcpConnectFailures(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientOpenAttempts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientOpenFailures(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientErrUnsupportClienttype(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientErrUnsupportedVersion(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientErrLengthMismatch(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientErrUnknownOpcode(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientErrUnknownCnum(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 23])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientErrBadCtype(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 24])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientErrBadSends(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 25])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientErrWrongObjects(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 26])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientErrWrongOpcode(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 27])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientKaTimedoutClients(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 28])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientErrAuthFailures(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 29])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientErrAuthMissing(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 30])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class copsClientServerConfigAddrType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 1])
	syntaxobject = InetAddressType


class copsClientServerConfigAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 2])
	syntaxobject = InetAddress


class copsClientServerConfigClientType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class copsClientServerConfigAuthType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 4])
	syntaxobject = CopsAuthType


class copsClientServerConfigTcpPort(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 5])
	syntaxobject = CopsTcpPort


class copsClientServerConfigPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class copsClientServerConfigRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class copsClientServerCurrentEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([copsClientServerAddressType, copsClientServerAddress, copsClientServerClientType], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1])
	access = 2
	columns = {'copsClientServerAddressType': copsClientServerAddressType, 'copsClientServerAddress': copsClientServerAddress, 'copsClientServerClientType': copsClientServerClientType, 'copsClientServerTcpPort': copsClientServerTcpPort, 'copsClientServerType': copsClientServerType, 'copsClientServerAuthType': copsClientServerAuthType, 'copsClientServerLastConnAttempt': copsClientServerLastConnAttempt, 'copsClientState': copsClientState, 'copsClientServerKeepaliveTime': copsClientServerKeepaliveTime, 'copsClientServerAccountingTime': copsClientServerAccountingTime, 'copsClientInPkts': copsClientInPkts, 'copsClientOutPkts': copsClientOutPkts, 'copsClientInErrs': copsClientInErrs, 'copsClientLastError': copsClientLastError, 'copsClientTcpConnectAttempts': copsClientTcpConnectAttempts, 'copsClientTcpConnectFailures': copsClientTcpConnectFailures, 'copsClientOpenAttempts': copsClientOpenAttempts, 'copsClientOpenFailures': copsClientOpenFailures, 'copsClientErrUnsupportClienttype': copsClientErrUnsupportClienttype, 'copsClientErrUnsupportedVersion': copsClientErrUnsupportedVersion, 'copsClientErrLengthMismatch': copsClientErrLengthMismatch, 'copsClientErrUnknownOpcode': copsClientErrUnknownOpcode, 'copsClientErrUnknownCnum': copsClientErrUnknownCnum, 'copsClientErrBadCtype': copsClientErrBadCtype, 'copsClientErrBadSends': copsClientErrBadSends, 'copsClientErrWrongObjects': copsClientErrWrongObjects, 'copsClientErrWrongOpcode': copsClientErrWrongOpcode, 'copsClientKaTimedoutClients': copsClientKaTimedoutClients, 'copsClientErrAuthFailures': copsClientErrAuthFailures, 'copsClientErrAuthMissing': copsClientErrAuthMissing}


class copsClientServerConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([copsClientServerConfigAddrType, copsClientServerConfigAddress, copsClientServerConfigClientType, copsClientServerConfigAuthType], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1])
	access = 2
	rowstatus = copsClientServerConfigRowStatus
	columns = {'copsClientServerConfigAddrType': copsClientServerConfigAddrType, 'copsClientServerConfigAddress': copsClientServerConfigAddress, 'copsClientServerConfigClientType': copsClientServerConfigClientType, 'copsClientServerConfigAuthType': copsClientServerConfigAuthType, 'copsClientServerConfigTcpPort': copsClientServerConfigTcpPort, 'copsClientServerConfigPriority': copsClientServerConfigPriority, 'copsClientServerConfigRowStatus': copsClientServerConfigRowStatus}


# notifications (traps) 
# groups 
class copsDeviceStatusGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 2, 1, 1])
	group = [copsClientCapabilities, copsClientServerTcpPort, copsClientServerType, copsClientServerAuthType, copsClientServerLastConnAttempt, copsClientState, copsClientServerKeepaliveTime, copsClientServerAccountingTime, copsClientInPkts, copsClientOutPkts, copsClientInErrs, copsClientLastError, copsClientTcpConnectAttempts, copsClientTcpConnectFailures, copsClientOpenAttempts, copsClientOpenFailures, copsClientErrUnsupportClienttype, copsClientErrUnsupportedVersion, copsClientErrLengthMismatch, copsClientErrUnknownOpcode, copsClientErrUnknownCnum, copsClientErrBadCtype, copsClientErrBadSends, copsClientErrWrongObjects, copsClientErrWrongOpcode, copsClientKaTimedoutClients, copsClientErrAuthFailures, copsClientErrAuthMissing]

class copsDeviceConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 89, 2, 1, 2])
	group = [copsClientServerConfigTcpPort, copsClientServerConfigPriority, copsClientServerConfigRowStatus, copsClientServerConfigRetryAlgrm, copsClientServerConfigRetryCount, copsClientServerConfigRetryIntvl]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
