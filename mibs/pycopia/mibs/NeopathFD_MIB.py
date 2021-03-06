# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import enterprises, Integer32, Counter64, MODULE_IDENTITY, NOTIFICATION_TYPE
from RFC_1212 import OBJECT_TYPE
from SNMPv2_TC import DisplayString
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP

class NeopathFD_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/NeopathFD-MIB'
	conformance = 3
	name = 'NeopathFD-MIB'
	language = 2
	description = 'NeoPath Networks File Director MIB version 1'

# nodes
class neopath(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011])
	name = 'neopath'

class mngdproducts(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1])
	name = 'mngdproducts'

class npFileDirectorMIB(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1])
	name = 'npFileDirectorMIB'

class npFDVersion1(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1])
	name = 'npFDVersion1'

class neopathTrapPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000])
	name = 'neopathTrapPrefix'

class neopathTrapHardware(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 1])
	name = 'neopathTrapHardware'

class neopathTrapBackendServer(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 2])
	name = 'neopathTrapBackendServer'

class neopathTrapServices(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 3])
	name = 'neopathTrapServices'

class neopathTrapResources(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 4])
	name = 'neopathTrapResources'

class neopathFDV1MIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 10000])
	name = 'neopathFDV1MIBConformance'

class neopathFDV1MIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 10000, 1])
	name = 'neopathFDV1MIBCompliances'

class neopathFDV1Groups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 10000, 2])
	name = 'neopathFDV1Groups'


# macros
# types 
# scalars 
class npDomainName(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNameServerNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npSystemClock(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npSysServiceNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npFileServerNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npFileServerSameNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npFileServerVServerNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npFileServerVShareNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npNSSDNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npNSDSNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 24])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npNSSLNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 26])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npNSUDNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 28])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npMGServiceNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 30])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npSWNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 36])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npStatInUdp(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 41])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class npStatInTcp(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 42])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class npStatOutUdp(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 43])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class npStatOutTcp(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 44])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class npTrapExtraDescription(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 1001])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


# columns
class npNameServerIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npNameServerName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npSysSIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 11, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npSysServiceName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 11, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npSysServiceDescr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 11, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npSysServiceStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 11, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npFSFilerName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSFilerProtocol(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSFilerIp(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSFilerLocalIp(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSFilerCifsPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSFilerCifsProxyName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSFilerCifsProxyIp(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSFilerCifsDomain(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSFilerCifsWinsServerAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSFilerCifsDnsServerAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSFilerNfsPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSFilerNfsVersions(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSFilerNfsServerType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSSameIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 17, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npFSSameName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 17, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSSameCifsShareName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 17, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSSameNfsExportName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 17, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVServerIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 19, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npFSVServerName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 19, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVServerIpAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 19, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVServerProtocol(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 19, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVServerComment(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 19, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVServerDefaultServerName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 19, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVServerDomain(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 19, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVServerWinsServerIp(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 19, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVServerIsNetBiosEnabled(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 19, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVServerIsSmbDrtHEnabled(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 19, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVShareIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 21, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npFSVShareShareName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 21, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVShareProtocol(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 21, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVShareIsSynthetic(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 21, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVShareFilerName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 21, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npFSVShareExportName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 21, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSSDIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 23, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npNSSDName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 23, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSSDProtocol(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 23, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSDSIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 25, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npNSDSName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 25, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSDSServiceName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 25, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSDSSharedDir(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 25, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSDSPrimary(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 25, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSSLIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 27, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npNSSLSDirectoryName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 27, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSSLPath(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 27, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSSLServerName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 27, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSSLShareDir(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 27, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSUDIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 29, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npNSUDSDirectoryName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 29, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSUDPath(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 29, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSUDServerName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 29, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npNSUDShareDir(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 29, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npMGEntryId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGPid(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGFailure(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGProtocol(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGCreationTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGStartTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGEndTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGElapsedTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGSrcServer(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGSrcShare(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGSrcPath(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGDstServer(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGDstShare(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npMGDstPath(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npSWIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 37, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class npSWComponent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 37, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npSWVersion(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 37, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class npSWBuildDate(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 37, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


# rows 
class npNameServerEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([npNameServerIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 5, 1])
	access = 2
	columns = {'npNameServerIndex': npNameServerIndex, 'npNameServerName': npNameServerName}


class npSysServiceEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([npSysSIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 11, 1])
	access = 2
	columns = {'npSysSIndex': npSysSIndex, 'npSysServiceName': npSysServiceName, 'npSysServiceDescr': npSysServiceDescr, 'npSysServiceStatus': npSysServiceStatus}


class npFileServerEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([npFSIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 13, 1])
	access = 2
	columns = {'npFSIndex': npFSIndex, 'npFSFilerName': npFSFilerName, 'npFSFilerProtocol': npFSFilerProtocol, 'npFSFilerIp': npFSFilerIp, 'npFSFilerLocalIp': npFSFilerLocalIp, 'npFSFilerCifsPort': npFSFilerCifsPort, 'npFSFilerCifsProxyName': npFSFilerCifsProxyName, 'npFSFilerCifsProxyIp': npFSFilerCifsProxyIp, 'npFSFilerCifsDomain': npFSFilerCifsDomain, 'npFSFilerCifsWinsServerAddr': npFSFilerCifsWinsServerAddr, 'npFSFilerCifsDnsServerAddr': npFSFilerCifsDnsServerAddr, 'npFSFilerNfsPort': npFSFilerNfsPort, 'npFSFilerNfsVersions': npFSFilerNfsVersions, 'npFSFilerNfsServerType': npFSFilerNfsServerType}


class npFileServerSameEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([npFSSameIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 17, 1])
	access = 2
	columns = {'npFSSameIndex': npFSSameIndex, 'npFSSameName': npFSSameName, 'npFSSameCifsShareName': npFSSameCifsShareName, 'npFSSameNfsExportName': npFSSameNfsExportName}


class npFileServerVServerEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([npFSVServerIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 19, 1])
	access = 2
	columns = {'npFSVServerIndex': npFSVServerIndex, 'npFSVServerName': npFSVServerName, 'npFSVServerIpAddress': npFSVServerIpAddress, 'npFSVServerProtocol': npFSVServerProtocol, 'npFSVServerComment': npFSVServerComment, 'npFSVServerDefaultServerName': npFSVServerDefaultServerName, 'npFSVServerDomain': npFSVServerDomain, 'npFSVServerWinsServerIp': npFSVServerWinsServerIp, 'npFSVServerIsNetBiosEnabled': npFSVServerIsNetBiosEnabled, 'npFSVServerIsSmbDrtHEnabled': npFSVServerIsSmbDrtHEnabled}


class npFileServerVShareEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([npFSVShareIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 21, 1])
	access = 2
	columns = {'npFSVShareIndex': npFSVShareIndex, 'npFSVShareShareName': npFSVShareShareName, 'npFSVShareProtocol': npFSVShareProtocol, 'npFSVShareIsSynthetic': npFSVShareIsSynthetic, 'npFSVShareFilerName': npFSVShareFilerName, 'npFSVShareExportName': npFSVShareExportName}


class npNSSDEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([npNSSDIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 23, 1])
	access = 2
	columns = {'npNSSDIndex': npNSSDIndex, 'npNSSDName': npNSSDName, 'npNSSDProtocol': npNSSDProtocol}


class npNSDSEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([npNSDSIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 25, 1])
	access = 2
	columns = {'npNSDSIndex': npNSDSIndex, 'npNSDSName': npNSDSName, 'npNSDSServiceName': npNSDSServiceName, 'npNSDSSharedDir': npNSDSSharedDir, 'npNSDSPrimary': npNSDSPrimary}


class npNSSLEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([npNSSLIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 27, 1])
	access = 2
	columns = {'npNSSLIndex': npNSSLIndex, 'npNSSLSDirectoryName': npNSSLSDirectoryName, 'npNSSLPath': npNSSLPath, 'npNSSLServerName': npNSSLServerName, 'npNSSLShareDir': npNSSLShareDir}


class npNSUDEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([npNSUDIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 29, 1])
	access = 2
	columns = {'npNSUDIndex': npNSUDIndex, 'npNSUDSDirectoryName': npNSUDSDirectoryName, 'npNSUDPath': npNSUDPath, 'npNSUDServerName': npNSUDServerName, 'npNSUDShareDir': npNSUDShareDir}


class npMGEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([npMGIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 31, 1])
	access = 2
	columns = {'npMGIndex': npMGIndex, 'npMGEntryId': npMGEntryId, 'npMGPid': npMGPid, 'npMGStatus': npMGStatus, 'npMGFailure': npMGFailure, 'npMGProtocol': npMGProtocol, 'npMGCreationTime': npMGCreationTime, 'npMGStartTime': npMGStartTime, 'npMGEndTime': npMGEndTime, 'npMGElapsedTime': npMGElapsedTime, 'npMGSrcServer': npMGSrcServer, 'npMGSrcShare': npMGSrcShare, 'npMGSrcPath': npMGSrcPath, 'npMGDstServer': npMGDstServer, 'npMGDstShare': npMGDstShare, 'npMGDstPath': npMGDstPath}


class npSWEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([npSWIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 37, 1])
	access = 2
	columns = {'npSWIndex': npSWIndex, 'npSWComponent': npSWComponent, 'npSWVersion': npSWVersion, 'npSWBuildDate': npSWBuildDate}


# notifications (traps) 
class npTrapHardwareDiskFailure(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 1, 1])

class npTrapHardwareNetworkCardFailure(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 1, 2])

class npTrapHardwareTemperatureHigh(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 1, 4])

class npTrapHardwarePowerSupplyFailure(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 1, 5])

class npTrapBackendServerAvailable(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 2, 1])

class npTrapBackendServerUnavailable(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 2, 2])

class npTrapSvcMigrationSuccessful(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 3, 1])

class npTrapSvcMigrationUnsuccessful(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 3, 2])

class npTrapSvcDBResyncError(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 3, 3])

class npTrapResourcesLocalFSFull(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 4, 1])

class npTrapResourcesDBFull(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 2000, 4, 2])

# groups 
class neopathFDV1Group(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 10000, 2, 1])
	group = [npDomainName, npNameServerNumber, npNameServerName, npSystemClock, npSysServiceNumber, npSysServiceName, npSysServiceDescr, npSysServiceStatus, npFileServerNumber, npFSFilerName, npFSFilerProtocol, npFSFilerIp, npFSFilerLocalIp, npFSFilerCifsPort, npFSFilerCifsProxyName, npFSFilerCifsProxyIp, npFSFilerCifsDomain, npFSFilerCifsWinsServerAddr, npFSFilerCifsDnsServerAddr, npFSFilerNfsPort, npFSFilerNfsVersions, npFSFilerNfsServerType, npFileServerSameNumber, npFSSameName, npFSSameCifsShareName, npFSSameNfsExportName, npFileServerVServerNumber, npFSVServerName, npFSVServerIpAddress, npFSVServerProtocol, npFSVServerComment, npFSVServerDefaultServerName, npFSVServerDomain, npFSVServerWinsServerIp, npFSVServerIsNetBiosEnabled, npFSVServerIsSmbDrtHEnabled, npFileServerVShareNumber, npFSVShareShareName, npFSVShareProtocol, npFSVShareIsSynthetic, npFSVShareFilerName, npFSVShareExportName, npNSSDNumber, npNSSDName, npNSSDProtocol, npNSDSNumber, npNSDSName, npNSDSServiceName, npNSDSSharedDir, npNSDSPrimary, npNSSLNumber, npNSSLSDirectoryName, npNSSLPath, npNSSLServerName, npNSSLShareDir, npNSUDNumber, npNSUDSDirectoryName, npNSUDPath, npNSUDServerName, npNSUDShareDir, npMGServiceNumber, npMGEntryId, npMGPid, npMGStatus, npMGFailure, npMGProtocol, npMGCreationTime, npMGStartTime, npMGEndTime, npMGElapsedTime, npMGSrcServer, npMGSrcShare, npMGSrcPath, npMGDstServer, npMGDstShare, npMGDstPath, npSWNumber, npSWComponent, npSWVersion, npSWBuildDate, npStatInUdp, npStatInTcp, npStatOutUdp, npStatOutTcp, npTrapExtraDescription]

class neopathFDV1NotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 17011, 1, 1, 1, 10000, 2, 2])
	group = [npTrapHardwareDiskFailure, npTrapHardwareNetworkCardFailure, npTrapHardwareTemperatureHigh, npTrapHardwarePowerSupplyFailure, npTrapBackendServerAvailable, npTrapBackendServerUnavailable, npTrapSvcMigrationSuccessful, npTrapSvcMigrationUnsuccessful, npTrapSvcDBResyncError, npTrapResourcesLocalFSFull, npTrapResourcesDBFull]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
