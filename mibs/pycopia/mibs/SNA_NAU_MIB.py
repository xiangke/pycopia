# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import Counter32, Gauge32, Integer32, mib_2, OBJECT_TYPE, MODULE_IDENTITY, NOTIFICATION_TYPE
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import DisplayString, RowStatus, TimeStamp, InstancePointer

class SNA_NAU_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/SNA-NAU-MIB'
	conformance = 2
	name = 'SNA-NAU-MIB'
	language = 2
	description = 'This is the MIB module for objects used to\nmanage SNA devices.'

# nodes
class snanauMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34])
	name = 'snanauMIB'

class snanauObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1])
	name = 'snanauObjects'

class snaNode(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1])
	name = 'snaNode'

class snaNodeTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 10])
	name = 'snaNodeTraps'

class snaLu(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2])
	name = 'snaLu'

class snaLuTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 5])
	name = 'snaLuTraps'

class snaMgtTools(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3])
	name = 'snaMgtTools'

class snanauConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 2])
	name = 'snanauConformance'

class snanauCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 2, 1])
	name = 'snanauCompliances'

class snanauGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 2, 2])
	name = 'snanauGroups'


# macros
# types 
# scalars 
class snaNodeAdminTableLastChange(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class snaNodeOperTableLastChange(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class snaNodeLinkAdminTableLastChange(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class snaNodeLinkOperTableLastChange(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


# columns
class snaNodeAdminIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaNodeAdminName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaNodeAdminType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'pu10'), Enum(3, 'pu20'), Enum(4, 't21len'), Enum(5, 'endNode'), Enum(6, 'networkNode')]


class snaNodeAdminXidFormat(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'format0'), Enum(2, 'format1'), Enum(3, 'format3')]


class snaNodeAdminBlockNum(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaNodeAdminIdNum(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaNodeAdminEnablingMethod(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'startup'), Enum(3, 'demand'), Enum(4, 'onlyMS')]


class snaNodeAdminLuTermDefault(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unbind'), Enum(2, 'termself'), Enum(3, 'rshutd'), Enum(4, 'poweroff')]


class snaNodeAdminMaxLu(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaNodeAdminHostDescription(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaNodeAdminStopMethod(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'normal'), Enum(3, 'immed'), Enum(4, 'force')]


class snaNodeAdminState(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'inactive'), Enum(2, 'active')]


class snaNodeAdminRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class snaNodeOperName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaNodeOperType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'pu10'), Enum(3, 'pu20'), Enum(4, 't21LEN'), Enum(5, 'endNode'), Enum(6, 'networkNode')]


class snaNodeOperXidFormat(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'format0'), Enum(2, 'format1'), Enum(3, 'format3')]


class snaNodeOperBlockNum(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaNodeOperIdNum(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaNodeOperEnablingMethod(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'startup'), Enum(3, 'demand'), Enum(4, 'onlyMS')]


class snaNodeOperLuTermDefault(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unbind'), Enum(2, 'termself'), Enum(3, 'rshutd'), Enum(4, 'poweroff')]


class snaNodeOperMaxLu(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaNodeOperHostDescription(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaNodeOperStopMethod(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'normal'), Enum(3, 'immed'), Enum(4, 'force')]


class snaNodeOperState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'inactive'), Enum(2, 'active'), Enum(3, 'waiting'), Enum(4, 'stopping')]


class snaNodeOperHostSscpId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class snaNodeOperStartTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class snaNodeOperLastStateChange(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class snaNodeOperActFailures(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaNodeOperActFailureReason(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'linkFailure'), Enum(3, 'noResources'), Enum(4, 'badConfiguration'), Enum(5, 'internalError')]


class snaPu20StatsSentBytes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaPu20StatsReceivedBytes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaPu20StatsSentPius(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaPu20StatsReceivedPius(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaPu20StatsSentNegativeResps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaPu20StatsReceivedNegativeResps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaPu20StatsActLus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class snaPu20StatsInActLus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class snaPu20StatsBindLus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class snaNodeLinkAdminIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaNodeLinkAdminSpecific(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.InstancePointer


class snaNodeLinkAdminMaxPiu(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaNodeLinkAdminRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class snaNodeLinkOperSpecific(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 8, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.InstancePointer


class snaNodeLinkOperMaxPiu(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 8, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuAdminLuIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuAdminName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaLuAdminSnaName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaLuAdminType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'lu0'), Enum(3, 'lu1'), Enum(4, 'lu2'), Enum(5, 'lu3'), Enum(6, 'lu4'), Enum(7, 'lu62'), Enum(8, 'lu7')]


class snaLuAdminDepType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'dependent'), Enum(2, 'independent')]


class snaLuAdminLocalAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class snaLuAdminDisplayModel(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'invalid'), Enum(2, 'model2A'), Enum(3, 'model2B'), Enum(4, 'model3A'), Enum(5, 'model3B'), Enum(6, 'model4A'), Enum(7, 'model4B'), Enum(8, 'model5A'), Enum(9, 'model5B'), Enum(10, 'dynamic')]


class snaLuAdminTerm(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unbind'), Enum(2, 'termself'), Enum(3, 'rshutd'), Enum(4, 'poweroff')]


class snaLuAdminRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class snaLuOperName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaLuOperSnaName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaLuOperType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'lu0'), Enum(3, 'lu1'), Enum(4, 'lu2'), Enum(5, 'lu3'), Enum(6, 'lu4'), Enum(7, 'lu62'), Enum(8, 'lu7')]


class snaLuOperDepType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'dependent'), Enum(2, 'independent')]


class snaLuOperLocalAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class snaLuOperDisplayModel(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'invalid'), Enum(2, 'model2A'), Enum(3, 'model2B'), Enum(4, 'model3A'), Enum(5, 'model3B'), Enum(6, 'model4A'), Enum(7, 'model4B'), Enum(8, 'model5A'), Enum(9, 'model5B'), Enum(10, 'dynamic')]


class snaLuOperTerm(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unbind'), Enum(2, 'termself'), Enum(3, 'rshutd'), Enum(4, 'poweroff')]


class snaLuOperState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'inactive'), Enum(2, 'active')]


class snaLuOperSessnCount(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class snaLuSessnRluIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuSessnIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuSessnLocalApplName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaLuSessnRemoteLuName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class snaLuSessnMaxSndRuSize(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuSessnMaxRcvRuSize(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuSessnSndPacingSize(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuSessnRcvPacingSize(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuSessnActiveTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class snaLuSessnAdminState(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unbound'), Enum(3, 'bound')]


class snaLuSessnOperState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unbound'), Enum(2, 'pendingBind'), Enum(3, 'bound'), Enum(4, 'pendingUnbind')]


class snaLuSessnSenseData(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class snaLuSessnTerminationRu(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'bindFailure'), Enum(3, 'unbind')]


class snaLuSessnUnbindType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class snaLuSessnLinkIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuSessnStatsSentBytes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaLuSessnStatsReceivedBytes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaLuSessnStatsSentRus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaLuSessnStatsReceivedRus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaLuSessnStatsSentNegativeResps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaLuSessnStatsReceivedNegativeResps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaLuRtmPuIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuRtmLuIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuRtmState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'off'), Enum(2, 'on')]


class snaLuRtmStateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class snaLuRtmDef(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'firstChar'), Enum(2, 'kb'), Enum(3, 'cdeb')]


class snaLuRtmBoundary1(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuRtmBoundary2(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuRtmBoundary3(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuRtmBoundary4(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuRtmCounter1(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaLuRtmCounter2(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaLuRtmCounter3(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaLuRtmCounter4(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaLuRtmOverFlows(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class snaLuRtmObjPercent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuRtmObjRange(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'range1'), Enum(3, 'range2'), Enum(4, 'range3'), Enum(5, 'range4'), Enum(6, 'range5')]


class snaLuRtmNumTrans(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuRtmLastRspTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class snaLuRtmAvgRspTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class snaNodeAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([snaNodeAdminIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1])
	access = 2
	rowstatus = snaNodeAdminRowStatus
	columns = {'snaNodeAdminIndex': snaNodeAdminIndex, 'snaNodeAdminName': snaNodeAdminName, 'snaNodeAdminType': snaNodeAdminType, 'snaNodeAdminXidFormat': snaNodeAdminXidFormat, 'snaNodeAdminBlockNum': snaNodeAdminBlockNum, 'snaNodeAdminIdNum': snaNodeAdminIdNum, 'snaNodeAdminEnablingMethod': snaNodeAdminEnablingMethod, 'snaNodeAdminLuTermDefault': snaNodeAdminLuTermDefault, 'snaNodeAdminMaxLu': snaNodeAdminMaxLu, 'snaNodeAdminHostDescription': snaNodeAdminHostDescription, 'snaNodeAdminStopMethod': snaNodeAdminStopMethod, 'snaNodeAdminState': snaNodeAdminState, 'snaNodeAdminRowStatus': snaNodeAdminRowStatus}


from SNA_NAU_MIB import snaNodeAdminIndex
class snaNodeOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([snaNodeAdminIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1])
	access = 2
	columns = {'snaNodeOperName': snaNodeOperName, 'snaNodeOperType': snaNodeOperType, 'snaNodeOperXidFormat': snaNodeOperXidFormat, 'snaNodeOperBlockNum': snaNodeOperBlockNum, 'snaNodeOperIdNum': snaNodeOperIdNum, 'snaNodeOperEnablingMethod': snaNodeOperEnablingMethod, 'snaNodeOperLuTermDefault': snaNodeOperLuTermDefault, 'snaNodeOperMaxLu': snaNodeOperMaxLu, 'snaNodeOperHostDescription': snaNodeOperHostDescription, 'snaNodeOperStopMethod': snaNodeOperStopMethod, 'snaNodeOperState': snaNodeOperState, 'snaNodeOperHostSscpId': snaNodeOperHostSscpId, 'snaNodeOperStartTime': snaNodeOperStartTime, 'snaNodeOperLastStateChange': snaNodeOperLastStateChange, 'snaNodeOperActFailures': snaNodeOperActFailures, 'snaNodeOperActFailureReason': snaNodeOperActFailureReason}


class snaPu20StatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([snaNodeAdminIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1])
	access = 2
	columns = {'snaPu20StatsSentBytes': snaPu20StatsSentBytes, 'snaPu20StatsReceivedBytes': snaPu20StatsReceivedBytes, 'snaPu20StatsSentPius': snaPu20StatsSentPius, 'snaPu20StatsReceivedPius': snaPu20StatsReceivedPius, 'snaPu20StatsSentNegativeResps': snaPu20StatsSentNegativeResps, 'snaPu20StatsReceivedNegativeResps': snaPu20StatsReceivedNegativeResps, 'snaPu20StatsActLus': snaPu20StatsActLus, 'snaPu20StatsInActLus': snaPu20StatsInActLus, 'snaPu20StatsBindLus': snaPu20StatsBindLus}


class snaNodeLinkAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([snaNodeAdminIndex, snaNodeLinkAdminIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1])
	access = 2
	rowstatus = snaNodeLinkAdminRowStatus
	columns = {'snaNodeLinkAdminIndex': snaNodeLinkAdminIndex, 'snaNodeLinkAdminSpecific': snaNodeLinkAdminSpecific, 'snaNodeLinkAdminMaxPiu': snaNodeLinkAdminMaxPiu, 'snaNodeLinkAdminRowStatus': snaNodeLinkAdminRowStatus}


from SNA_NAU_MIB import snaNodeAdminIndex
from SNA_NAU_MIB import snaNodeLinkAdminIndex
class snaNodeLinkOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([snaNodeAdminIndex, snaNodeLinkAdminIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 8, 1])
	access = 2
	columns = {'snaNodeLinkOperSpecific': snaNodeLinkOperSpecific, 'snaNodeLinkOperMaxPiu': snaNodeLinkOperMaxPiu}


class snaLuAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([snaNodeAdminIndex, snaLuAdminLuIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1])
	access = 2
	rowstatus = snaLuAdminRowStatus
	columns = {'snaLuAdminLuIndex': snaLuAdminLuIndex, 'snaLuAdminName': snaLuAdminName, 'snaLuAdminSnaName': snaLuAdminSnaName, 'snaLuAdminType': snaLuAdminType, 'snaLuAdminDepType': snaLuAdminDepType, 'snaLuAdminLocalAddress': snaLuAdminLocalAddress, 'snaLuAdminDisplayModel': snaLuAdminDisplayModel, 'snaLuAdminTerm': snaLuAdminTerm, 'snaLuAdminRowStatus': snaLuAdminRowStatus}


from SNA_NAU_MIB import snaNodeAdminIndex
from SNA_NAU_MIB import snaLuAdminLuIndex
class snaLuOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([snaNodeAdminIndex, snaLuAdminLuIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1])
	access = 2
	columns = {'snaLuOperName': snaLuOperName, 'snaLuOperSnaName': snaLuOperSnaName, 'snaLuOperType': snaLuOperType, 'snaLuOperDepType': snaLuOperDepType, 'snaLuOperLocalAddress': snaLuOperLocalAddress, 'snaLuOperDisplayModel': snaLuOperDisplayModel, 'snaLuOperTerm': snaLuOperTerm, 'snaLuOperState': snaLuOperState, 'snaLuOperSessnCount': snaLuOperSessnCount}


class snaLuSessnEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([snaNodeAdminIndex, snaLuAdminLuIndex, snaLuSessnRluIndex, snaLuSessnIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1])
	access = 2
	columns = {'snaLuSessnRluIndex': snaLuSessnRluIndex, 'snaLuSessnIndex': snaLuSessnIndex, 'snaLuSessnLocalApplName': snaLuSessnLocalApplName, 'snaLuSessnRemoteLuName': snaLuSessnRemoteLuName, 'snaLuSessnMaxSndRuSize': snaLuSessnMaxSndRuSize, 'snaLuSessnMaxRcvRuSize': snaLuSessnMaxRcvRuSize, 'snaLuSessnSndPacingSize': snaLuSessnSndPacingSize, 'snaLuSessnRcvPacingSize': snaLuSessnRcvPacingSize, 'snaLuSessnActiveTime': snaLuSessnActiveTime, 'snaLuSessnAdminState': snaLuSessnAdminState, 'snaLuSessnOperState': snaLuSessnOperState, 'snaLuSessnSenseData': snaLuSessnSenseData, 'snaLuSessnTerminationRu': snaLuSessnTerminationRu, 'snaLuSessnUnbindType': snaLuSessnUnbindType, 'snaLuSessnLinkIndex': snaLuSessnLinkIndex}


from SNA_NAU_MIB import snaNodeAdminIndex
from SNA_NAU_MIB import snaLuAdminLuIndex
from SNA_NAU_MIB import snaLuSessnRluIndex
from SNA_NAU_MIB import snaLuSessnIndex
class snaLuSessnStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([snaNodeAdminIndex, snaLuAdminLuIndex, snaLuSessnRluIndex, snaLuSessnIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1])
	access = 2
	columns = {'snaLuSessnStatsSentBytes': snaLuSessnStatsSentBytes, 'snaLuSessnStatsReceivedBytes': snaLuSessnStatsReceivedBytes, 'snaLuSessnStatsSentRus': snaLuSessnStatsSentRus, 'snaLuSessnStatsReceivedRus': snaLuSessnStatsReceivedRus, 'snaLuSessnStatsSentNegativeResps': snaLuSessnStatsSentNegativeResps, 'snaLuSessnStatsReceivedNegativeResps': snaLuSessnStatsReceivedNegativeResps}


class snaLuRtmEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([snaLuRtmPuIndex, snaLuRtmLuIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1])
	access = 2
	columns = {'snaLuRtmPuIndex': snaLuRtmPuIndex, 'snaLuRtmLuIndex': snaLuRtmLuIndex, 'snaLuRtmState': snaLuRtmState, 'snaLuRtmStateTime': snaLuRtmStateTime, 'snaLuRtmDef': snaLuRtmDef, 'snaLuRtmBoundary1': snaLuRtmBoundary1, 'snaLuRtmBoundary2': snaLuRtmBoundary2, 'snaLuRtmBoundary3': snaLuRtmBoundary3, 'snaLuRtmBoundary4': snaLuRtmBoundary4, 'snaLuRtmCounter1': snaLuRtmCounter1, 'snaLuRtmCounter2': snaLuRtmCounter2, 'snaLuRtmCounter3': snaLuRtmCounter3, 'snaLuRtmCounter4': snaLuRtmCounter4, 'snaLuRtmOverFlows': snaLuRtmOverFlows, 'snaLuRtmObjPercent': snaLuRtmObjPercent, 'snaLuRtmObjRange': snaLuRtmObjRange, 'snaLuRtmNumTrans': snaLuRtmNumTrans, 'snaLuRtmLastRspTime': snaLuRtmLastRspTime, 'snaLuRtmAvgRspTime': snaLuRtmAvgRspTime}


# notifications (traps) 
class snaNodeStateChangeTrap(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 10, 1])

class snaNodeActFailTrap(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 1, 10, 2])

class snaLuStateChangeTrap(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 5, 1])

class snaLuSessnBindFailTrap(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 1, 2, 5, 2])

# groups 
class snaNodeGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 2, 2, 1])
	group = [snaNodeAdminName, snaNodeAdminType, snaNodeAdminXidFormat, snaNodeAdminBlockNum, snaNodeAdminIdNum, snaNodeAdminEnablingMethod, snaNodeAdminLuTermDefault, snaNodeAdminMaxLu, snaNodeAdminHostDescription, snaNodeAdminStopMethod, snaNodeAdminState, snaNodeAdminRowStatus, snaNodeAdminTableLastChange, snaNodeOperName, snaNodeOperType, snaNodeOperXidFormat, snaNodeOperBlockNum, snaNodeOperIdNum, snaNodeOperEnablingMethod, snaNodeOperLuTermDefault, snaNodeOperMaxLu, snaNodeOperHostDescription, snaNodeOperStopMethod, snaNodeOperState, snaNodeOperHostSscpId, snaNodeOperStartTime, snaNodeOperLastStateChange, snaNodeOperActFailures, snaNodeOperActFailureReason, snaNodeOperTableLastChange, snaNodeLinkAdminSpecific, snaNodeLinkAdminMaxPiu, snaNodeLinkAdminRowStatus, snaNodeLinkAdminTableLastChange, snaNodeLinkOperSpecific, snaNodeLinkOperMaxPiu, snaNodeLinkOperTableLastChange]

class snaLuGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 2, 2, 2])
	group = [snaLuAdminName, snaLuAdminSnaName, snaLuAdminType, snaLuAdminDepType, snaLuAdminLocalAddress, snaLuAdminDisplayModel, snaLuAdminTerm, snaLuAdminRowStatus, snaLuOperName, snaLuOperSnaName, snaLuOperType, snaLuOperDepType, snaLuOperLocalAddress, snaLuOperDisplayModel, snaLuOperTerm, snaLuOperState, snaLuOperSessnCount]

class snaSessionGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 2, 2, 3])
	group = [snaLuSessnRluIndex, snaLuSessnIndex, snaLuSessnLocalApplName, snaLuSessnRemoteLuName, snaLuSessnMaxSndRuSize, snaLuSessnMaxRcvRuSize, snaLuSessnSndPacingSize, snaLuSessnRcvPacingSize, snaLuSessnActiveTime, snaLuSessnAdminState, snaLuSessnOperState, snaLuSessnSenseData, snaLuSessnTerminationRu, snaLuSessnUnbindType, snaLuSessnLinkIndex, snaLuSessnStatsSentBytes, snaLuSessnStatsReceivedBytes, snaLuSessnStatsSentRus, snaLuSessnStatsReceivedRus, snaLuSessnStatsSentNegativeResps, snaLuSessnStatsReceivedNegativeResps]

class snaPu20Group(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 2, 2, 4])
	group = [snaPu20StatsSentBytes, snaPu20StatsReceivedBytes, snaPu20StatsSentPius, snaPu20StatsReceivedPius, snaPu20StatsSentNegativeResps, snaPu20StatsReceivedNegativeResps, snaPu20StatsActLus, snaPu20StatsInActLus, snaPu20StatsBindLus]

class snaMgtToolsRtmGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 2, 2, 5])
	group = [snaLuRtmState, snaLuRtmStateTime, snaLuRtmDef, snaLuRtmBoundary1, snaLuRtmBoundary2, snaLuRtmBoundary3, snaLuRtmBoundary4, snaLuRtmCounter1, snaLuRtmCounter2, snaLuRtmCounter3, snaLuRtmCounter4, snaLuRtmOverFlows, snaLuRtmObjPercent, snaLuRtmObjRange, snaLuRtmNumTrans, snaLuRtmLastRspTime, snaLuRtmAvgRspTime]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
