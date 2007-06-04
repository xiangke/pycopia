# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Integer32, Counter64, Gauge32, TimeTicks
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoExperiment
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus, DisplayString, TimeStamp
from IF_MIB import ifIndex, OwnerString

class ATM_RMON_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/ATM-RMON-MIB'
	conformance = 3
	name = 'ATM-RMON-MIB'
	language = 2
	description = 'The MIB module for managing remote monitoring device\nimplementations for ATM networks.'

# nodes
class atmRmon(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16])
	name = 'atmRmon'

class atmRmonMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1])
	name = 'atmRmonMIBObjects'

class portSelect(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1])
	name = 'portSelect'

class atmStats(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2])
	name = 'atmStats'

class atmHost(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3])
	name = 'atmHost'

class atmMatrix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4])
	name = 'atmMatrix'

class atmConfig(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 5])
	name = 'atmConfig'

class atmRmonNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 2])
	name = 'atmRmonNotifications'

class atmRmonConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 3])
	name = 'atmRmonConformance'

class atmRmonMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 1])
	name = 'atmRmonMIBCompliances'

class atmRmonMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2])
	name = 'atmRmonMIBGroups'


# macros
# types 

class ZeroBasedCounter32(pycopia.SMI.Basetypes.Gauge32):
	status = 1


class LastCreateTime(pycopia.SMI.Basetypes.TimeTicks):
	status = 1


class AtmAddr(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 0), Range(8, 8), Range(13, 13), Range(20, 20))


class ServiceClass(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'cbrAndVbr'), Enum(2, 'abrAndUbr')]


class ResourcePriority(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'lowPriority'), Enum(2, 'normalPriority'), Enum(3, 'highPriority')]


class AddressCollectScope(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'prefix'), Enum(2, 'prefixAndEsi'), Enum(3, 'entireAddr')]


class ConnectTime(pycopia.SMI.Basetypes.Gauge32):
	status = 1

# scalars 
class atmRmonDataCollectMode(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 5, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'active'), Enum(2, 'inactive')]


# columns
class portSelGrpIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class portSelGrpDescr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class portSelGrpCreateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1, 1, 3])
	syntaxobject = LastCreateTime


class portSelGrpOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1, 1, 4])
	syntaxobject = OwnerString


class portSelGrpStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class portSelCollectGroup(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class portSelCreateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 2, 1, 2])
	syntaxobject = LastCreateTime


class portSelOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 2, 1, 3])
	syntaxobject = OwnerString


class portSelStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class atmStatsControlDropEvents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmStatsControlOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 1, 1, 2])
	syntaxobject = OwnerString


class atmStatsControlStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class atmStatsSClass(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 1])
	syntaxobject = ServiceClass


class atmStatsCreateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 2])
	syntaxobject = LastCreateTime


class atmStatsCells(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmStatsCellsRollovers(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmStatsHCCells(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class atmStatsNumCallAttempts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmStatsNumCalls(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmStatsConnTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 8])
	syntaxobject = ConnectTime
	access = 4
	units = 'seconds'


class atmHostControlInserts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmHostControlDeletes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmHostControlMaxDesiredEntries(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmHostControlPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 4])
	syntaxobject = ResourcePriority


class atmHostControlAddrCollectScope(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 5])
	syntaxobject = AddressCollectScope


class atmHostControlDropEvents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmHostControlOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 7])
	syntaxobject = OwnerString


class atmHostControlStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class atmHostAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 1])
	syntaxobject = AtmAddr


class atmHostSClass(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 2])
	syntaxobject = ServiceClass


class atmHostCreateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 3])
	syntaxobject = LastCreateTime


class atmHostInCells(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 4])
	syntaxobject = ZeroBasedCounter32


class atmHostInCellsRollovers(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 5])
	syntaxobject = ZeroBasedCounter32


class atmHostInHCCells(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class atmHostOutCells(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 7])
	syntaxobject = ZeroBasedCounter32


class atmHostOutCellsRollovers(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 8])
	syntaxobject = ZeroBasedCounter32


class atmHostOutHCCells(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class atmHostInNumCallAttempts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 10])
	syntaxobject = ZeroBasedCounter32


class atmHostInNumCalls(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 11])
	syntaxobject = ZeroBasedCounter32


class atmHostOutNumCallAttempts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 12])
	syntaxobject = ZeroBasedCounter32


class atmHostOutNumCalls(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 13])
	syntaxobject = ZeroBasedCounter32


class atmHostInConnTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 14])
	syntaxobject = ConnectTime
	access = 4
	units = 'seconds'


class atmHostOutConnTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 15])
	syntaxobject = ConnectTime
	access = 4
	units = 'seconds'


class atmMatrixControlInserts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmMatrixControlDeletes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmMatrixControlMaxDesiredEntries(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmMatrixControlPriority(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 4])
	syntaxobject = ResourcePriority


class atmMatrixControlAddrCollectScope(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 5])
	syntaxobject = AddressCollectScope


class atmMatrixControlDropEvents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmMatrixControlOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 7])
	syntaxobject = OwnerString


class atmMatrixControlStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class atmMatrixSDSrcAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 1])
	syntaxobject = AtmAddr


class atmMatrixSDDstAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 2])
	syntaxobject = AtmAddr


class atmMatrixSDSClass(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 3])
	syntaxobject = ServiceClass


class atmMatrixSDCreateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 4])
	syntaxobject = LastCreateTime


class atmMatrixSDCells(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 5])
	syntaxobject = ZeroBasedCounter32


class atmMatrixSDCellsRollovers(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 6])
	syntaxobject = ZeroBasedCounter32


class atmMatrixSDHCCells(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class atmMatrixSDNumCallAttempts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 8])
	syntaxobject = ZeroBasedCounter32


class atmMatrixSDNumCalls(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 9])
	syntaxobject = ZeroBasedCounter32


class atmMatrixSDConnTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 10])
	syntaxobject = ConnectTime
	access = 4
	units = 'seconds'


class atmMatrixDSSrcAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 1])
	syntaxobject = AtmAddr


class atmMatrixDSDstAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 2])
	syntaxobject = AtmAddr


class atmMatrixDSSClass(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 3])
	syntaxobject = ServiceClass


class atmMatrixDSCreateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 4])
	syntaxobject = LastCreateTime


class atmMatrixDSCells(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 5])
	syntaxobject = ZeroBasedCounter32


class atmMatrixDSCellsRollovers(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 6])
	syntaxobject = ZeroBasedCounter32


class atmMatrixDSHCCells(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class atmMatrixDSNumCallAttempts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 8])
	syntaxobject = ZeroBasedCounter32


class atmMatrixDSNumCalls(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 9])
	syntaxobject = ZeroBasedCounter32


class atmMatrixDSConnTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 10])
	syntaxobject = ConnectTime
	access = 4
	units = 'seconds'


class atmMatrixTopNControlIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmMatrixTopNControlRateBase(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'atmMatrixTopNCells'), Enum(2, 'atmMatrixTopNNumCallAttempts'), Enum(3, 'atmMatrixTopNNumCalls'), Enum(4, 'atmMatrixTopNConnTime')]


class atmMatrixTopNControlSClass(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 3])
	syntaxobject = ServiceClass


class atmMatrixTopNControlTimeRemaining(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmMatrixTopNControlGeneratedReports(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmMatrixTopNControlDuration(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmMatrixTopNControlRequestedSize(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmMatrixTopNControlGrantedSize(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmMatrixTopNControlStartTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class atmMatrixTopNControlOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 10])
	syntaxobject = OwnerString


class atmMatrixTopNControlStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class atmMatrixTopNIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmMatrixTopNSrcAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5, 1, 2])
	syntaxobject = AtmAddr


class atmMatrixTopNDstAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5, 1, 3])
	syntaxobject = AtmAddr


class atmMatrixTopNRate(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmMatrixTopNReverseRate(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class portSelGrpEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([portSelGrpIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1, 1])
	access = 2
	rowstatus = portSelGrpStatus
	columns = {'portSelGrpIndex': portSelGrpIndex, 'portSelGrpDescr': portSelGrpDescr, 'portSelGrpCreateTime': portSelGrpCreateTime, 'portSelGrpOwner': portSelGrpOwner, 'portSelGrpStatus': portSelGrpStatus}


class portSelEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 2, 1])
	access = 2
	rowstatus = portSelStatus
	columns = {'portSelCollectGroup': portSelCollectGroup, 'portSelCreateTime': portSelCreateTime, 'portSelOwner': portSelOwner, 'portSelStatus': portSelStatus}


class atmStatsControlEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([portSelGrpIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 1, 1])
	access = 2
	rowstatus = atmStatsControlStatus
	columns = {'atmStatsControlDropEvents': atmStatsControlDropEvents, 'atmStatsControlOwner': atmStatsControlOwner, 'atmStatsControlStatus': atmStatsControlStatus}


class atmStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([portSelGrpIndex, atmStatsSClass], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1])
	access = 2
	columns = {'atmStatsSClass': atmStatsSClass, 'atmStatsCreateTime': atmStatsCreateTime, 'atmStatsCells': atmStatsCells, 'atmStatsCellsRollovers': atmStatsCellsRollovers, 'atmStatsHCCells': atmStatsHCCells, 'atmStatsNumCallAttempts': atmStatsNumCallAttempts, 'atmStatsNumCalls': atmStatsNumCalls, 'atmStatsConnTime': atmStatsConnTime}


class atmHostControlEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([portSelGrpIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1])
	access = 2
	rowstatus = atmHostControlStatus
	columns = {'atmHostControlInserts': atmHostControlInserts, 'atmHostControlDeletes': atmHostControlDeletes, 'atmHostControlMaxDesiredEntries': atmHostControlMaxDesiredEntries, 'atmHostControlPriority': atmHostControlPriority, 'atmHostControlAddrCollectScope': atmHostControlAddrCollectScope, 'atmHostControlDropEvents': atmHostControlDropEvents, 'atmHostControlOwner': atmHostControlOwner, 'atmHostControlStatus': atmHostControlStatus}


class atmHostEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([portSelGrpIndex, atmHostAddress, atmHostSClass], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1])
	access = 2
	columns = {'atmHostAddress': atmHostAddress, 'atmHostSClass': atmHostSClass, 'atmHostCreateTime': atmHostCreateTime, 'atmHostInCells': atmHostInCells, 'atmHostInCellsRollovers': atmHostInCellsRollovers, 'atmHostInHCCells': atmHostInHCCells, 'atmHostOutCells': atmHostOutCells, 'atmHostOutCellsRollovers': atmHostOutCellsRollovers, 'atmHostOutHCCells': atmHostOutHCCells, 'atmHostInNumCallAttempts': atmHostInNumCallAttempts, 'atmHostInNumCalls': atmHostInNumCalls, 'atmHostOutNumCallAttempts': atmHostOutNumCallAttempts, 'atmHostOutNumCalls': atmHostOutNumCalls, 'atmHostInConnTime': atmHostInConnTime, 'atmHostOutConnTime': atmHostOutConnTime}


class atmMatrixControlEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([portSelGrpIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1])
	access = 2
	rowstatus = atmMatrixControlStatus
	columns = {'atmMatrixControlInserts': atmMatrixControlInserts, 'atmMatrixControlDeletes': atmMatrixControlDeletes, 'atmMatrixControlMaxDesiredEntries': atmMatrixControlMaxDesiredEntries, 'atmMatrixControlPriority': atmMatrixControlPriority, 'atmMatrixControlAddrCollectScope': atmMatrixControlAddrCollectScope, 'atmMatrixControlDropEvents': atmMatrixControlDropEvents, 'atmMatrixControlOwner': atmMatrixControlOwner, 'atmMatrixControlStatus': atmMatrixControlStatus}


class atmMatrixSDEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([portSelGrpIndex, atmMatrixSDSrcAddress, atmMatrixSDDstAddress, atmMatrixSDSClass], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1])
	access = 2
	columns = {'atmMatrixSDSrcAddress': atmMatrixSDSrcAddress, 'atmMatrixSDDstAddress': atmMatrixSDDstAddress, 'atmMatrixSDSClass': atmMatrixSDSClass, 'atmMatrixSDCreateTime': atmMatrixSDCreateTime, 'atmMatrixSDCells': atmMatrixSDCells, 'atmMatrixSDCellsRollovers': atmMatrixSDCellsRollovers, 'atmMatrixSDHCCells': atmMatrixSDHCCells, 'atmMatrixSDNumCallAttempts': atmMatrixSDNumCallAttempts, 'atmMatrixSDNumCalls': atmMatrixSDNumCalls, 'atmMatrixSDConnTime': atmMatrixSDConnTime}


class atmMatrixDSEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([portSelGrpIndex, atmMatrixDSDstAddress, atmMatrixDSSrcAddress, atmMatrixDSSClass], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1])
	access = 2
	columns = {'atmMatrixDSSrcAddress': atmMatrixDSSrcAddress, 'atmMatrixDSDstAddress': atmMatrixDSDstAddress, 'atmMatrixDSSClass': atmMatrixDSSClass, 'atmMatrixDSCreateTime': atmMatrixDSCreateTime, 'atmMatrixDSCells': atmMatrixDSCells, 'atmMatrixDSCellsRollovers': atmMatrixDSCellsRollovers, 'atmMatrixDSHCCells': atmMatrixDSHCCells, 'atmMatrixDSNumCallAttempts': atmMatrixDSNumCallAttempts, 'atmMatrixDSNumCalls': atmMatrixDSNumCalls, 'atmMatrixDSConnTime': atmMatrixDSConnTime}


class atmMatrixTopNControlEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([portSelGrpIndex, atmMatrixTopNControlIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1])
	access = 2
	rowstatus = atmMatrixTopNControlStatus
	columns = {'atmMatrixTopNControlIndex': atmMatrixTopNControlIndex, 'atmMatrixTopNControlRateBase': atmMatrixTopNControlRateBase, 'atmMatrixTopNControlSClass': atmMatrixTopNControlSClass, 'atmMatrixTopNControlTimeRemaining': atmMatrixTopNControlTimeRemaining, 'atmMatrixTopNControlGeneratedReports': atmMatrixTopNControlGeneratedReports, 'atmMatrixTopNControlDuration': atmMatrixTopNControlDuration, 'atmMatrixTopNControlRequestedSize': atmMatrixTopNControlRequestedSize, 'atmMatrixTopNControlGrantedSize': atmMatrixTopNControlGrantedSize, 'atmMatrixTopNControlStartTime': atmMatrixTopNControlStartTime, 'atmMatrixTopNControlOwner': atmMatrixTopNControlOwner, 'atmMatrixTopNControlStatus': atmMatrixTopNControlStatus}


class atmMatrixTopNEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([portSelGrpIndex, atmMatrixTopNControlIndex, atmMatrixTopNIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5, 1])
	access = 2
	columns = {'atmMatrixTopNIndex': atmMatrixTopNIndex, 'atmMatrixTopNSrcAddress': atmMatrixTopNSrcAddress, 'atmMatrixTopNDstAddress': atmMatrixTopNDstAddress, 'atmMatrixTopNRate': atmMatrixTopNRate, 'atmMatrixTopNReverseRate': atmMatrixTopNReverseRate}


# notifications (traps) 
# groups 
class portSelectGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 1])
	group = [portSelGrpDescr, portSelGrpCreateTime, portSelGrpOwner, portSelGrpStatus, portSelCollectGroup, portSelCreateTime, portSelOwner, portSelStatus]

class atmStatsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 2])
	group = [atmStatsControlDropEvents, atmStatsControlOwner, atmStatsControlStatus, atmStatsCreateTime, atmStatsCells, atmStatsCellsRollovers, atmStatsNumCallAttempts, atmStatsNumCalls, atmStatsConnTime]

class atmStatsHCGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 3])
	group = [atmStatsHCCells]

class atmHostGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 4])
	group = [atmHostControlInserts, atmHostControlDeletes, atmHostControlMaxDesiredEntries, atmHostControlPriority, atmHostControlAddrCollectScope, atmHostControlDropEvents, atmHostControlOwner, atmHostControlStatus, atmHostCreateTime, atmHostInCells, atmHostInCellsRollovers, atmHostOutCells, atmHostOutCellsRollovers, atmHostInNumCallAttempts, atmHostInNumCalls, atmHostOutNumCallAttempts, atmHostOutNumCalls, atmHostInConnTime, atmHostOutConnTime]

class atmHostHCGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 5])
	group = [atmHostInHCCells, atmHostOutHCCells]

class atmMatrixGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 6])
	group = [atmMatrixControlInserts, atmMatrixControlDeletes, atmMatrixControlMaxDesiredEntries, atmMatrixControlPriority, atmMatrixControlAddrCollectScope, atmMatrixControlDropEvents, atmMatrixControlOwner, atmMatrixControlStatus, atmMatrixSDCreateTime, atmMatrixSDCells, atmMatrixSDCellsRollovers, atmMatrixSDNumCallAttempts, atmMatrixSDNumCalls, atmMatrixSDConnTime, atmMatrixDSCreateTime, atmMatrixDSCells, atmMatrixDSCellsRollovers, atmMatrixDSNumCallAttempts, atmMatrixDSNumCalls, atmMatrixDSConnTime, atmMatrixTopNControlRateBase, atmMatrixTopNControlSClass, atmMatrixTopNControlTimeRemaining, atmMatrixTopNControlGeneratedReports, atmMatrixTopNControlDuration, atmMatrixTopNControlRequestedSize, atmMatrixTopNControlGrantedSize, atmMatrixTopNControlStartTime, atmMatrixTopNControlOwner, atmMatrixTopNControlStatus, atmMatrixTopNSrcAddress, atmMatrixTopNDstAddress, atmMatrixTopNRate, atmMatrixTopNReverseRate]

class atmMatrixHCGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 7])
	group = [atmMatrixSDHCCells, atmMatrixDSHCCells]

class atmConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 8])
	group = [atmRmonDataCollectMode]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
