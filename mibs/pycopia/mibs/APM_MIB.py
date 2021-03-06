# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from SNMP_FRAMEWORK_MIB import SnmpAdminString
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Counter32, Unsigned32
from RMON2_MIB import protocolDirLocalIndex
from RMON_MIB import rmon, OwnerString
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus, TimeStamp, TimeInterval, TruthValue, DateAndTime, StorageType

class APM_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/APM-MIB'
	conformance = 4
	name = 'APM-MIB'
	language = 2
	description = 'The MIB module for measuring application performance\nas experienced by end-users.\n\nCopyright (C) The Internet Society (2004). This version of\nthis MIB module is part of RFC 3729; see the RFC itself for\nfull legal notices.'

# nodes
class apm(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23])
	name = 'apm'

class apmNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 0])
	name = 'apmNotifications'

class apmMibObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1])
	name = 'apmMibObjects'

class apmConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 2])
	name = 'apmConformance'

class apmCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 2, 1])
	name = 'apmCompliances'

class apmGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 2, 2])
	name = 'apmGroups'


# macros
# types 

class AppLocalIndex(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(1, 2147483647))


class ProtocolDirNetworkAddress(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 255))


class DataSourceOrZero(pycopia.SMI.Basetypes.ObjectIdentifier):
	status = 1


class RmonClientID(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	ranges = Ranges(Range(0, -1))


class TransactionAggregationType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'flows'), Enum(2, 'clients'), Enum(3, 'servers'), Enum(4, 'applications')]

# scalars 
class apmBucketBoundaryLastChange(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class apmAppDirID(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class apmHttpIgnoreUnregisteredURLs(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class apmHttp4xxIsFailure(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class apmTransactionsRequestedHistorySize(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmThroughputExceptionMinTime(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class apmNotificationMaxRate(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


# columns
class apmAppDirAppLocalIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 1])
	syntaxobject = AppLocalIndex


class apmAppDirResponsivenessType(ColumnObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'transactionOriented'), Enum(2, 'throughputOriented'), Enum(3, 'streamingOriented')]


class apmAppDirConfig(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'off'), Enum(2, 'on')]


class apmAppDirResponsivenessBoundary1(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmAppDirResponsivenessBoundary2(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmAppDirResponsivenessBoundary3(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmAppDirResponsivenessBoundary4(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmAppDirResponsivenessBoundary5(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmAppDirResponsivenessBoundary6(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmHttpFilterIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmHttpFilterAppLocalIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 2])
	syntaxobject = AppLocalIndex


class apmHttpFilterServerProtocol(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmHttpFilterServerAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 4])
	syntaxobject = ProtocolDirNetworkAddress


class apmHttpFilterURLPath(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class apmHttpFilterMatchType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'exact'), Enum(2, 'stripTrailingSlash'), Enum(3, 'prefix')]


class apmHttpFilterOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 7])
	syntaxobject = OwnerString


class apmHttpFilterStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class apmHttpFilterRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class apmUserDefinedAppParentIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 7, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmUserDefinedAppApplication(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 7, 1, 2])
	syntaxobject = SnmpAdminString


class apmNameClientID(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 8, 1, 1])
	syntaxobject = RmonClientID


class apmNameClientAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 8, 1, 2])
	syntaxobject = ProtocolDirNetworkAddress


class apmNameMappingStartTime(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 8, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class apmNameMachineName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 8, 1, 4])
	syntaxobject = SnmpAdminString


class apmNameUserName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 8, 1, 5])
	syntaxobject = SnmpAdminString


class apmReportControlIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportControlDataSource(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 2])
	syntaxobject = DataSourceOrZero


class apmReportControlAggregationType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 3])
	syntaxobject = TransactionAggregationType


class apmReportControlInterval(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'Seconds'


class apmReportControlRequestedSize(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportControlGrantedSize(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportControlRequestedReports(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportControlGrantedReports(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportControlStartTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class apmReportControlReportNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportControlDeniedInserts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class apmReportControlDroppedFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class apmReportControlOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 13])
	syntaxobject = OwnerString


class apmReportControlStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class apmReportControlStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class apmReportIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportServerAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 2])
	syntaxobject = ProtocolDirNetworkAddress


class apmReportTransactionCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportSuccessfulTransactions(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportResponsivenessMean(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportResponsivenessMin(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportResponsivenessMax(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportResponsivenessB1(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportResponsivenessB2(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportResponsivenessB3(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportResponsivenessB4(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportResponsivenessB5(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportResponsivenessB6(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmReportResponsivenessB7(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmTransactionServerAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 11, 1, 1])
	syntaxobject = ProtocolDirNetworkAddress


class apmTransactionID(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 11, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmTransactionResponsiveness(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 11, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmTransactionAge(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 11, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class apmTransactionSuccess(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 11, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class apmExceptionIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmExceptionResponsivenessComparison(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'greater'), Enum(3, 'less')]


class apmExceptionResponsivenessThreshold(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class apmExceptionUnsuccessfulException(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'off'), Enum(2, 'on')]


class apmExceptionResponsivenessEvents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class apmExceptionUnsuccessfulEvents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class apmExceptionOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 7])
	syntaxobject = OwnerString


class apmExceptionStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class apmExceptionStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class apmAppDirEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([apmAppDirAppLocalIndex, apmAppDirResponsivenessType], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1])
	access = 2
	columns = {'apmAppDirAppLocalIndex': apmAppDirAppLocalIndex, 'apmAppDirResponsivenessType': apmAppDirResponsivenessType, 'apmAppDirConfig': apmAppDirConfig, 'apmAppDirResponsivenessBoundary1': apmAppDirResponsivenessBoundary1, 'apmAppDirResponsivenessBoundary2': apmAppDirResponsivenessBoundary2, 'apmAppDirResponsivenessBoundary3': apmAppDirResponsivenessBoundary3, 'apmAppDirResponsivenessBoundary4': apmAppDirResponsivenessBoundary4, 'apmAppDirResponsivenessBoundary5': apmAppDirResponsivenessBoundary5, 'apmAppDirResponsivenessBoundary6': apmAppDirResponsivenessBoundary6}


class apmHttpFilterEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([apmHttpFilterIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1])
	access = 2
	rowstatus = apmHttpFilterRowStatus
	columns = {'apmHttpFilterIndex': apmHttpFilterIndex, 'apmHttpFilterAppLocalIndex': apmHttpFilterAppLocalIndex, 'apmHttpFilterServerProtocol': apmHttpFilterServerProtocol, 'apmHttpFilterServerAddress': apmHttpFilterServerAddress, 'apmHttpFilterURLPath': apmHttpFilterURLPath, 'apmHttpFilterMatchType': apmHttpFilterMatchType, 'apmHttpFilterOwner': apmHttpFilterOwner, 'apmHttpFilterStorageType': apmHttpFilterStorageType, 'apmHttpFilterRowStatus': apmHttpFilterRowStatus}


class apmUserDefinedAppEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([apmAppDirAppLocalIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 7, 1])
	access = 2
	columns = {'apmUserDefinedAppParentIndex': apmUserDefinedAppParentIndex, 'apmUserDefinedAppApplication': apmUserDefinedAppApplication}


class apmNameEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([apmNameClientID, protocolDirLocalIndex, apmNameClientAddress, apmNameMappingStartTime], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 8, 1])
	access = 2
	columns = {'apmNameClientID': apmNameClientID, 'apmNameClientAddress': apmNameClientAddress, 'apmNameMappingStartTime': apmNameMappingStartTime, 'apmNameMachineName': apmNameMachineName, 'apmNameUserName': apmNameUserName}


class apmReportControlEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([apmReportControlIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1])
	access = 2
	rowstatus = apmReportControlStatus
	columns = {'apmReportControlIndex': apmReportControlIndex, 'apmReportControlDataSource': apmReportControlDataSource, 'apmReportControlAggregationType': apmReportControlAggregationType, 'apmReportControlInterval': apmReportControlInterval, 'apmReportControlRequestedSize': apmReportControlRequestedSize, 'apmReportControlGrantedSize': apmReportControlGrantedSize, 'apmReportControlRequestedReports': apmReportControlRequestedReports, 'apmReportControlGrantedReports': apmReportControlGrantedReports, 'apmReportControlStartTime': apmReportControlStartTime, 'apmReportControlReportNumber': apmReportControlReportNumber, 'apmReportControlDeniedInserts': apmReportControlDeniedInserts, 'apmReportControlDroppedFrames': apmReportControlDroppedFrames, 'apmReportControlOwner': apmReportControlOwner, 'apmReportControlStorageType': apmReportControlStorageType, 'apmReportControlStatus': apmReportControlStatus}


class apmReportEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([apmReportControlIndex, apmReportIndex, apmAppDirAppLocalIndex, apmAppDirResponsivenessType, protocolDirLocalIndex, apmReportServerAddress, apmNameClientID], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1])
	access = 2
	columns = {'apmReportIndex': apmReportIndex, 'apmReportServerAddress': apmReportServerAddress, 'apmReportTransactionCount': apmReportTransactionCount, 'apmReportSuccessfulTransactions': apmReportSuccessfulTransactions, 'apmReportResponsivenessMean': apmReportResponsivenessMean, 'apmReportResponsivenessMin': apmReportResponsivenessMin, 'apmReportResponsivenessMax': apmReportResponsivenessMax, 'apmReportResponsivenessB1': apmReportResponsivenessB1, 'apmReportResponsivenessB2': apmReportResponsivenessB2, 'apmReportResponsivenessB3': apmReportResponsivenessB3, 'apmReportResponsivenessB4': apmReportResponsivenessB4, 'apmReportResponsivenessB5': apmReportResponsivenessB5, 'apmReportResponsivenessB6': apmReportResponsivenessB6, 'apmReportResponsivenessB7': apmReportResponsivenessB7}


class apmTransactionEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([apmAppDirAppLocalIndex, apmAppDirResponsivenessType, protocolDirLocalIndex, apmTransactionServerAddress, apmNameClientID, apmTransactionID], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 11, 1])
	access = 2
	columns = {'apmTransactionServerAddress': apmTransactionServerAddress, 'apmTransactionID': apmTransactionID, 'apmTransactionResponsiveness': apmTransactionResponsiveness, 'apmTransactionAge': apmTransactionAge, 'apmTransactionSuccess': apmTransactionSuccess}


class apmExceptionEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([apmAppDirAppLocalIndex, apmAppDirResponsivenessType, apmExceptionIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1])
	access = 2
	rowstatus = apmExceptionStatus
	columns = {'apmExceptionIndex': apmExceptionIndex, 'apmExceptionResponsivenessComparison': apmExceptionResponsivenessComparison, 'apmExceptionResponsivenessThreshold': apmExceptionResponsivenessThreshold, 'apmExceptionUnsuccessfulException': apmExceptionUnsuccessfulException, 'apmExceptionResponsivenessEvents': apmExceptionResponsivenessEvents, 'apmExceptionUnsuccessfulEvents': apmExceptionUnsuccessfulEvents, 'apmExceptionOwner': apmExceptionOwner, 'apmExceptionStorageType': apmExceptionStorageType, 'apmExceptionStatus': apmExceptionStatus}


# notifications (traps) 
class apmTransactionResponsivenessAlarm(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 0, 1])

class apmTransactionUnsuccessfulAlarm(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 0, 2])

# groups 
class apmAppDirGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 2, 2, 1])
	group = [apmAppDirConfig, apmAppDirResponsivenessBoundary1, apmAppDirResponsivenessBoundary2, apmAppDirResponsivenessBoundary3, apmAppDirResponsivenessBoundary4, apmAppDirResponsivenessBoundary5, apmAppDirResponsivenessBoundary6, apmBucketBoundaryLastChange, apmAppDirID, apmNameMachineName, apmNameUserName]

class apmUserDefinedApplicationsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 2, 2, 2])
	group = [apmHttpFilterAppLocalIndex, apmHttpFilterServerProtocol, apmHttpFilterServerAddress, apmHttpFilterURLPath, apmHttpFilterMatchType, apmHttpFilterOwner, apmHttpFilterStorageType, apmHttpFilterRowStatus, apmHttpIgnoreUnregisteredURLs, apmHttp4xxIsFailure, apmUserDefinedAppParentIndex, apmUserDefinedAppApplication]

class apmReportGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 2, 2, 3])
	group = [apmReportControlDataSource, apmReportControlAggregationType, apmReportControlInterval, apmReportControlRequestedSize, apmReportControlGrantedSize, apmReportControlRequestedReports, apmReportControlGrantedReports, apmReportControlStartTime, apmReportControlReportNumber, apmReportControlDeniedInserts, apmReportControlDroppedFrames, apmReportControlOwner, apmReportControlStorageType, apmReportControlStatus, apmReportTransactionCount, apmReportSuccessfulTransactions, apmReportResponsivenessMean, apmReportResponsivenessMin, apmReportResponsivenessMax, apmReportResponsivenessB1, apmReportResponsivenessB2, apmReportResponsivenessB3, apmReportResponsivenessB4, apmReportResponsivenessB5, apmReportResponsivenessB6, apmReportResponsivenessB7]

class apmTransactionGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 2, 2, 4])
	group = [apmTransactionResponsiveness, apmTransactionAge, apmTransactionSuccess, apmTransactionsRequestedHistorySize]

class apmExceptionGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 2, 2, 5])
	group = [apmExceptionResponsivenessComparison, apmExceptionResponsivenessThreshold, apmExceptionUnsuccessfulException, apmExceptionResponsivenessEvents, apmExceptionUnsuccessfulEvents, apmExceptionOwner, apmExceptionStorageType, apmExceptionStatus, apmThroughputExceptionMinTime, apmNotificationMaxRate]

class apmNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 23, 2, 2, 6])
	group = [apmTransactionResponsivenessAlarm, apmTransactionUnsuccessfulAlarm]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
