# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Counter32, Integer32, IpAddress, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus, MacAddress, TruthValue, TimeStamp
from IF_MIB import ifIndex

class VRRP_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/VRRP-MIB'
	conformance = 5
	name = 'VRRP-MIB'
	language = 2
	description = 'This MIB describes objects used for managing Virtual Router\nRedundancy Protocol (VRRP) routers.'

# nodes
class vrrpMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68])
	name = 'vrrpMIB'

class vrrpNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 0])
	name = 'vrrpNotifications'

class vrrpOperations(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1])
	name = 'vrrpOperations'

class vrrpStatistics(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2])
	name = 'vrrpStatistics'

class vrrpConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 3])
	name = 'vrrpConformance'

class vrrpMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 3, 1])
	name = 'vrrpMIBCompliances'

class vrrpMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 3, 2])
	name = 'vrrpMIBGroups'


# macros
# types 

class VrId(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(1, 255))

# scalars 
class vrrpNodeVersion(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class vrrpNotificationCntl(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class vrrpTrapPacketSrc(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class vrrpTrapAuthErrorType(ScalarObject):
	status = 1
	access = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'invalidAuthType'), Enum(2, 'authTypeMismatch'), Enum(3, 'authFailure')]


class vrrpRouterChecksumErrors(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpRouterVersionErrors(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpRouterVrIdErrors(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# columns
class vrrpOperVrId(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 1])
	syntaxobject = VrId


class vrrpOperVirtualMacAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class vrrpOperState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'initialize'), Enum(2, 'backup'), Enum(3, 'master')]


class vrrpOperAdminState(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down')]


class vrrpOperPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class vrrpOperIpAddrCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class vrrpOperMasterIpAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class vrrpOperPrimaryIpAddr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class vrrpOperAuthType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noAuthentication'), Enum(2, 'simpleTextPassword'), Enum(3, 'ipAuthenticationHeader')]


class vrrpOperAuthKey(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class vrrpOperAdvertisementInterval(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class vrrpOperPreemptMode(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class vrrpOperVirtualRouterUpTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class vrrpOperProtocol(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ip'), Enum(2, 'bridge'), Enum(3, 'decnet'), Enum(4, 'other')]


class vrrpOperRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class vrrpAssoIpAddr(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class vrrpAssoIpAddrRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class vrrpStatsBecomeMaster(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpStatsAdvertiseRcvd(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpStatsAdvertiseIntervalErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpStatsAuthFailures(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpStatsIpTtlErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpStatsPriorityZeroPktsRcvd(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpStatsPriorityZeroPktsSent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpStatsInvalidTypePktsRcvd(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpStatsAddressListErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpStatsInvalidAuthType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpStatsAuthTypeMismatch(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class vrrpStatsPacketLengthErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
class vrrpOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, vrrpOperVrId], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 3, 1])
	access = 2
	rowstatus = vrrpOperRowStatus
	columns = {'vrrpOperVrId': vrrpOperVrId, 'vrrpOperVirtualMacAddr': vrrpOperVirtualMacAddr, 'vrrpOperState': vrrpOperState, 'vrrpOperAdminState': vrrpOperAdminState, 'vrrpOperPriority': vrrpOperPriority, 'vrrpOperIpAddrCount': vrrpOperIpAddrCount, 'vrrpOperMasterIpAddr': vrrpOperMasterIpAddr, 'vrrpOperPrimaryIpAddr': vrrpOperPrimaryIpAddr, 'vrrpOperAuthType': vrrpOperAuthType, 'vrrpOperAuthKey': vrrpOperAuthKey, 'vrrpOperAdvertisementInterval': vrrpOperAdvertisementInterval, 'vrrpOperPreemptMode': vrrpOperPreemptMode, 'vrrpOperVirtualRouterUpTime': vrrpOperVirtualRouterUpTime, 'vrrpOperProtocol': vrrpOperProtocol, 'vrrpOperRowStatus': vrrpOperRowStatus}


class vrrpAssoIpAddrEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, vrrpOperVrId, vrrpAssoIpAddr], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 1, 4, 1])
	access = 2
	rowstatus = vrrpAssoIpAddrRowStatus
	columns = {'vrrpAssoIpAddr': vrrpAssoIpAddr, 'vrrpAssoIpAddrRowStatus': vrrpAssoIpAddrRowStatus}


from IF_MIB import ifIndex
from VRRP_MIB import vrrpOperVrId
class vrrpRouterStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, vrrpOperVrId], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 2, 4, 1])
	access = 2
	columns = {'vrrpStatsBecomeMaster': vrrpStatsBecomeMaster, 'vrrpStatsAdvertiseRcvd': vrrpStatsAdvertiseRcvd, 'vrrpStatsAdvertiseIntervalErrors': vrrpStatsAdvertiseIntervalErrors, 'vrrpStatsAuthFailures': vrrpStatsAuthFailures, 'vrrpStatsIpTtlErrors': vrrpStatsIpTtlErrors, 'vrrpStatsPriorityZeroPktsRcvd': vrrpStatsPriorityZeroPktsRcvd, 'vrrpStatsPriorityZeroPktsSent': vrrpStatsPriorityZeroPktsSent, 'vrrpStatsInvalidTypePktsRcvd': vrrpStatsInvalidTypePktsRcvd, 'vrrpStatsAddressListErrors': vrrpStatsAddressListErrors, 'vrrpStatsInvalidAuthType': vrrpStatsInvalidAuthType, 'vrrpStatsAuthTypeMismatch': vrrpStatsAuthTypeMismatch, 'vrrpStatsPacketLengthErrors': vrrpStatsPacketLengthErrors}


# notifications (traps) 
class vrrpTrapNewMaster(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 0, 1])

class vrrpTrapAuthFailure(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 0, 2])

# groups 
class vrrpOperGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 3, 2, 1])
	group = [vrrpNodeVersion, vrrpNotificationCntl, vrrpOperVirtualMacAddr, vrrpOperState, vrrpOperAdminState, vrrpOperPriority, vrrpOperIpAddrCount, vrrpOperMasterIpAddr, vrrpOperPrimaryIpAddr, vrrpOperAuthType, vrrpOperAuthKey, vrrpOperAdvertisementInterval, vrrpOperPreemptMode, vrrpOperVirtualRouterUpTime, vrrpOperProtocol, vrrpOperRowStatus, vrrpAssoIpAddrRowStatus]

class vrrpStatsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 3, 2, 2])
	group = [vrrpRouterChecksumErrors, vrrpRouterVersionErrors, vrrpRouterVrIdErrors, vrrpStatsBecomeMaster, vrrpStatsAdvertiseRcvd, vrrpStatsAdvertiseIntervalErrors, vrrpStatsAuthFailures, vrrpStatsIpTtlErrors, vrrpStatsPriorityZeroPktsRcvd, vrrpStatsPriorityZeroPktsSent, vrrpStatsInvalidTypePktsRcvd, vrrpStatsAddressListErrors, vrrpStatsInvalidAuthType, vrrpStatsAuthTypeMismatch, vrrpStatsPacketLengthErrors]

class vrrpTrapGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 3, 2, 3])
	group = [vrrpTrapPacketSrc, vrrpTrapAuthErrorType]

class vrrpNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 68, 3, 2, 4])
	group = [vrrpTrapNewMaster, vrrpTrapAuthFailure]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
