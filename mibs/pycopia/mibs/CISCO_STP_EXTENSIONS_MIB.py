# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Integer32, NOTIFICATION_TYPE
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_VTP_MIB import vlanTrunkPortEntry, VlanIndex
from SNMPv2_TC import TruthValue
from CISCO_SMI import ciscoMgmt

class CISCO_STP_EXTENSIONS_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-STP-EXTENSIONS-MIB'
	conformance = 1
	name = 'CISCO-STP-EXTENSIONS-MIB'
	language = 2
	description = 'The MIB module for managing Cisco extensions to\nthe 802.1D Spanning Tree Protocol (STP).'

# nodes
class ciscoStpExtensionsMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82])
	name = 'ciscoStpExtensionsMIB'

class stpxObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1])
	name = 'stpxObjects'

class stpxUplinkFastObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 1])
	name = 'stpxUplinkFastObjects'

class stpxVlanObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2])
	name = 'stpxVlanObjects'

class stpxInconsistencyObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 3])
	name = 'stpxInconsistencyObjects'

class stpxBackboneFastObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4])
	name = 'stpxBackboneFastObjects'

class stpxNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 2])
	name = 'stpxNotifications'

class stpxNotificationsPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 2, 0])
	name = 'stpxNotificationsPrefix'

class stpxMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 3])
	name = 'stpxMIBConformance'

class stpxMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1])
	name = 'stpxMIBCompliances'

class stpxMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2])
	name = 'stpxMIBGroups'


# macros
# types 
# scalars 
class stpxUplinkFastEnabled(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class stpxUplinkFastTransitions(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'transitions'


class stpxUplinkStationLearningGenRate(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'frames'


class stpxUplinkStationLearningFrames(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'frames'


class stpxBackboneFastEnabled(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 1])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class stpxBackboneFastInInferiorBPDUs(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class stpxBackboneFastInRLQRequestPDUs(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class stpxBackboneFastInRLQResponsePDUs(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class stpxBackboneFastOutRLQRequestPDUs(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class stpxBackboneFastOutRLQResponsePDUs(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# columns
class stpxPreferredVlansMap(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class stpxVlanIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 3, 1, 1, 1])
	syntaxobject = VlanIndex


class stpxPortIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
from CISCO_VTP_MIB import vlanTrunkPortIfIndex
class stpxPreferredVlansEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([vlanTrunkPortIfIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2, 1, 1])
	access = 2
	columns = {'stpxPreferredVlansMap': stpxPreferredVlansMap}


class stpxInconsistencyEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([stpxVlanIndex, stpxPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 3, 1, 1])
	access = 2
	columns = {'stpxVlanIndex': stpxVlanIndex, 'stpxPortIndex': stpxPortIndex}


# notifications (traps) 
class stpxInconsistencyUpdate(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 2, 0, 1])

# groups 
class stpxUplinkGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 1])
	group = [stpxUplinkFastEnabled, stpxUplinkFastTransitions, stpxUplinkStationLearningGenRate, stpxUplinkStationLearningFrames]

class stpxPreferredVlansGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 2])
	group = [stpxPreferredVlansMap]

class stpxSstpGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 3])
	group = [stpxInconsistentState]

class stpxBackboneGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 5])
	group = [stpxBackboneFastEnabled, stpxBackboneFastInInferiorBPDUs, stpxBackboneFastInRLQRequestPDUs, stpxBackboneFastInRLQResponsePDUs, stpxBackboneFastOutRLQRequestPDUs, stpxBackboneFastOutRLQResponsePDUs]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
