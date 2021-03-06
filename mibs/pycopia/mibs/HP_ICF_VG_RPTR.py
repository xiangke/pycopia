# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import Integer32, Counter32, Counter64, OBJECT_TYPE, MODULE_IDENTITY, NOTIFICATION_TYPE
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from SNMPv2_TC import DisplayString, TruthValue
from HP_ICF_OID import hpicfObjectModules, hpicfVg, hpicfVgRptrTrapsPrefix
from ICF_VG_RPTR import icfVgPortStatus

class HP_ICF_VG_RPTR(ModuleObject):
	path = '/usr/share/snmp/mibs/site/HP-ICF-VG-RPTR'
	conformance = 5
	name = 'HP-ICF-VG-RPTR'
	language = 2
	description = 'This MIB module contains objects that provide\nHP-specific extensions to the 802.12 Repeater MIB.'

# nodes
class hpicfVgRptrMib(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11])
	name = 'hpicfVgRptrMib'

class hpicfVgRptrConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1])
	name = 'hpicfVgRptrConformance'

class hpicfVgRptrCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 1])
	name = 'hpicfVgRptrCompliances'

class hpicfVgRptrGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2])
	name = 'hpicfVgRptrGroups'

class hpVgBasic(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1])
	name = 'hpVgBasic'

class hpVgBasicGlobal(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1])
	name = 'hpVgBasicGlobal'

class hpVgBasicGroup(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2])
	name = 'hpVgBasicGroup'

class hpVgBasicPort(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3])
	name = 'hpVgBasicPort'

class hpVgMonitor(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2])
	name = 'hpVgMonitor'

class hpVgMonitorGlobal(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1])
	name = 'hpVgMonitorGlobal'

class hpVgMonCounters(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1])
	name = 'hpVgMonCounters'

class hpVgMonitorGroup(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 2])
	name = 'hpVgMonitorGroup'

class hpVgMonitorPort(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 3])
	name = 'hpVgMonitorPort'


# macros
# types 
# scalars 
class hpVgEntityName(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class hpVgRedundantUpLinksFlag(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class hpVgNullAddrTraining(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'preventNullAddr'), Enum(2, 'allowNullAddr')]


class hpVgMonGlbReadableFrames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbReadableOctets(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbUnreadableOctets(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbHighPriorityFrames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbHighPriorityOctets(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbBroadcastFrames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbMulticastFrames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbIPMFrames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbDataErrorFrames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbPriorityPromotions(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbHCReadableOctets(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class hpVgMonGlbHCUnreadableOctets(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class hpVgMonGlbHCHighPriorityOctets(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class hpVgMonGlbHCNormPriorityOctets(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class hpVgMonGlbNormPriorityFrames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbNormPriorityOctets(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbNullAddressedFrames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbOversizeFrames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgMonGlbTransitionToTrainings(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# columns
class hpVgXcvrGroupIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpVgXcvrIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpVgXcvrType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'unknown'), Enum(3, 'pmdMissing'), Enum(4, 'utp4'), Enum(5, 'stp2'), Enum(6, 'fibre')]


class hpVgXcvrAssociatedPort(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpVgXcvrState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unknown'), Enum(2, 'inUse'), Enum(3, 'standby'), Enum(4, 'silent'), Enum(5, 'linkFailure')]


class hpVgXcvrAbandonments(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpVgXcvrIsMovable(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class hpVgGrpGroupIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpVgGrpPortsAdminStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class hpVgGrpPortsTrained(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class hpVgGrpPortsInTraining(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class hpVgGrpPortsCascaded(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class hpVgGrpPortsPromiscuous(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class hpVgPortGroupIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpVgPortIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpVgPortPolarityReversed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class hpVgPortWireSkewError(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class hpVgPortAssociatedXcvrIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpVgPortNumAssociatedXcvrs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class hpVgXcvrEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([hpVgXcvrGroupIndex, hpVgXcvrIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1])
	access = 2
	columns = {'hpVgXcvrGroupIndex': hpVgXcvrGroupIndex, 'hpVgXcvrIndex': hpVgXcvrIndex, 'hpVgXcvrType': hpVgXcvrType, 'hpVgXcvrAssociatedPort': hpVgXcvrAssociatedPort, 'hpVgXcvrState': hpVgXcvrState, 'hpVgXcvrAbandonments': hpVgXcvrAbandonments, 'hpVgXcvrIsMovable': hpVgXcvrIsMovable}


class hpVgBasicGroupEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([hpVgGrpGroupIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1])
	access = 2
	columns = {'hpVgGrpGroupIndex': hpVgGrpGroupIndex, 'hpVgGrpPortsAdminStatus': hpVgGrpPortsAdminStatus, 'hpVgGrpPortsTrained': hpVgGrpPortsTrained, 'hpVgGrpPortsInTraining': hpVgGrpPortsInTraining, 'hpVgGrpPortsCascaded': hpVgGrpPortsCascaded, 'hpVgGrpPortsPromiscuous': hpVgGrpPortsPromiscuous}


class hpVgBasicPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([hpVgPortGroupIndex, hpVgPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1])
	access = 2
	columns = {'hpVgPortGroupIndex': hpVgPortGroupIndex, 'hpVgPortIndex': hpVgPortIndex, 'hpVgPortPolarityReversed': hpVgPortPolarityReversed, 'hpVgPortWireSkewError': hpVgPortWireSkewError, 'hpVgPortAssociatedXcvrIndex': hpVgPortAssociatedXcvrIndex, 'hpVgPortNumAssociatedXcvrs': hpVgPortNumAssociatedXcvrs}


# notifications (traps) 
class hpVgRedundantUplinkTrap(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 3, 0, 1])

class hpVgLossOfActiveTrap(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 3, 0, 2])

# groups 
class hpicfVgRptrBasicGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 2])
	group = [hpVgEntityName, hpVgNullAddrTraining, hpVgGrpPortsAdminStatus, hpVgGrpPortsTrained, hpVgGrpPortsInTraining, hpVgGrpPortsCascaded, hpVgGrpPortsPromiscuous, hpVgPortPolarityReversed, hpVgPortWireSkewError]

class hpicfVgRptrMonitorGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 4])
	group = [hpVgMonGlbReadableFrames, hpVgMonGlbReadableOctets, hpVgMonGlbUnreadableOctets, hpVgMonGlbHighPriorityFrames, hpVgMonGlbHighPriorityOctets, hpVgMonGlbBroadcastFrames, hpVgMonGlbMulticastFrames, hpVgMonGlbIPMFrames, hpVgMonGlbDataErrorFrames, hpVgMonGlbPriorityPromotions, hpVgMonGlbHCReadableOctets, hpVgMonGlbHCUnreadableOctets, hpVgMonGlbHCHighPriorityOctets, hpVgMonGlbHCNormPriorityOctets, hpVgMonGlbNormPriorityFrames, hpVgMonGlbNormPriorityOctets, hpVgMonGlbNullAddressedFrames, hpVgMonGlbOversizeFrames, hpVgMonGlbTransitionToTrainings]

class hpicfVgRptrXcvrGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 5])
	group = [hpVgXcvrType, hpVgXcvrAssociatedPort, hpVgXcvrState, hpVgXcvrAbandonments, hpVgXcvrIsMovable, hpVgPortAssociatedXcvrIndex, hpVgPortNumAssociatedXcvrs]

class hpicfVgRptrRedundantUplinkGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 6])
	group = [hpVgRedundantUpLinksFlag]

class hpicfVgRptrBasicTraps(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 7])
	group = [hpVgLossOfActiveTrap]

class hpicfVgRptrRedundantUplinkTraps(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 8])
	group = [hpVgRedundantUplinkTrap]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
