# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from IF_MIB import InterfaceIndex
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Integer32
from CISCO_TC import CiscoNetworkProtocol, CiscoNetworkAddress
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import RowStatus, TruthValue

class CISCO_SNAPSHOT_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-SNAPSHOT-MIB'
	conformance = 2
	name = 'CISCO-SNAPSHOT-MIB'
	language = 2
	description = 'Snapshot routing MIB'

# nodes
class ciscoSnapshotMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19])
	name = 'ciscoSnapshotMIB'

class ciscoSnapshotMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1])
	name = 'ciscoSnapshotMIBObjects'

class ciscoSnapshotMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 2])
	name = 'ciscoSnapshotMIBConformance'

class ciscoSnapshotMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 2, 1])
	name = 'ciscoSnapshotMIBCompliances'

class ciscoSnapshotMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 2, 2])
	name = 'ciscoSnapshotMIBGroups'


# macros
# types 
# scalars 
class ciscoSnapshotForceActive(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# columns
class ciscoSnapshotIfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 1])
	syntaxobject = InterfaceIndex


class ciscoSnapshotClient(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class ciscoSnapshotDialer(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class ciscoSnapshotActiveInterval(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'minutes'


class ciscoSnapshotQuietInterval(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'minutes'


class ciscoSnapshotRetryInterval(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'minutes'


class ciscoSnapshotIfUpAction(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'goActive'), Enum(2, 'noAction')]


class ciscoSnapshotRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class ciscoSnapshotActivityIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ciscoSnapshotActivityState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'active'), Enum(2, 'quiet'), Enum(3, 'serverPostActive'), Enum(4, 'transitionToQuiet'), Enum(5, 'transitionToActive'), Enum(6, 'limbo')]


class ciscoSnapshotActivityTimer(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'minutes'


class ciscoSnapshotExchangeTimer(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'minutes'


class ciscoSnapshotDialerMap(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ciscoSnapshotSourceProtocol(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 6])
	syntaxobject = CiscoNetworkProtocol


class ciscoSnapshotSourceAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 7])
	syntaxobject = CiscoNetworkAddress


class ciscoSnapshotProtocolsExchanged(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


# rows 
class ciscoSnapshotInterfaceEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ciscoSnapshotIfIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1])
	access = 2
	rowstatus = ciscoSnapshotRowStatus
	columns = {'ciscoSnapshotIfIndex': ciscoSnapshotIfIndex, 'ciscoSnapshotClient': ciscoSnapshotClient, 'ciscoSnapshotDialer': ciscoSnapshotDialer, 'ciscoSnapshotActiveInterval': ciscoSnapshotActiveInterval, 'ciscoSnapshotQuietInterval': ciscoSnapshotQuietInterval, 'ciscoSnapshotRetryInterval': ciscoSnapshotRetryInterval, 'ciscoSnapshotIfUpAction': ciscoSnapshotIfUpAction, 'ciscoSnapshotRowStatus': ciscoSnapshotRowStatus}


class ciscoSnapshotActivityEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ciscoSnapshotIfIndex, ciscoSnapshotActivityIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1])
	access = 2
	columns = {'ciscoSnapshotActivityIndex': ciscoSnapshotActivityIndex, 'ciscoSnapshotActivityState': ciscoSnapshotActivityState, 'ciscoSnapshotActivityTimer': ciscoSnapshotActivityTimer, 'ciscoSnapshotExchangeTimer': ciscoSnapshotExchangeTimer, 'ciscoSnapshotDialerMap': ciscoSnapshotDialerMap, 'ciscoSnapshotSourceProtocol': ciscoSnapshotSourceProtocol, 'ciscoSnapshotSourceAddress': ciscoSnapshotSourceAddress, 'ciscoSnapshotProtocolsExchanged': ciscoSnapshotProtocolsExchanged}


# notifications (traps) 
# groups 
class ciscoSnapshotMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 19, 2, 2, 1])
	group = [ciscoSnapshotForceActive, ciscoSnapshotClient, ciscoSnapshotDialer, ciscoSnapshotActiveInterval, ciscoSnapshotQuietInterval, ciscoSnapshotRetryInterval, ciscoSnapshotIfUpAction, ciscoSnapshotRowStatus, ciscoSnapshotActivityState, ciscoSnapshotActivityTimer, ciscoSnapshotExchangeTimer, ciscoSnapshotDialerMap, ciscoSnapshotSourceProtocol, ciscoSnapshotSourceAddress, ciscoSnapshotProtocolsExchanged]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
