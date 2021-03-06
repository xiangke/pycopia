# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from OSPF_MIB import BigMetric
from SNMPv2_SMI import OBJECT_TYPE, MODULE_IDENTITY, IpAddress
from IANA_RTPROTO_MIB import IANAipRouteProtocol
from HP_ICF_OID import hpSwitch
from SNMPv2_TC import TruthValue, RowStatus

class HP_ICF_OSPF(ModuleObject):
	path = '/usr/share/snmp/mibs/site/HP-ICF-OSPF'
	conformance = 2
	name = 'HP-ICF-OSPF'
	language = 2
	description = 'This MIB module contains HP proprietary\nextensions to the OSPF-MIB module.'

# nodes
class hpicfOspf(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14])
	name = 'hpicfOspf'

class hpicfOspfObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1])
	name = 'hpicfOspfObjects'

class hpicfOspfGeneral(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1])
	name = 'hpicfOspfGeneral'

class hpicfOspfConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2])
	name = 'hpicfOspfConformance'

class hpicfOspfGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1])
	name = 'hpicfOspfGroups'

class hpicfOspfCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 2])
	name = 'hpicfOspfCompliances'


# macros
# types 
# scalars 
class hpicfOspf1583CompatibilityMode(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class hpicfOspfDefaultImportMetric(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 2])
	syntaxobject = BigMetric


class hpicfOspfDefaultImportMetricType(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'externalType1'), Enum(2, 'externalType2')]


class hpicfOspfIntraAreaDistance(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpicfOspfInterAreaDistance(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class hpicfOspfExternalDistance(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# columns
class hpicfOspfRedistSrcProto(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 2, 1, 1])
	syntaxobject = IANAipRouteProtocol


class hpicfOspfRedistEnabled(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class hpicfOspfRedistRestrictAddr(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class hpicfOspfRedistRestrictMask(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class hpicfOspfRedistRestrictStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class hpicfOspfRedistEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([hpicfOspfRedistSrcProto], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 2, 1])
	access = 2
	columns = {'hpicfOspfRedistSrcProto': hpicfOspfRedistSrcProto, 'hpicfOspfRedistEnabled': hpicfOspfRedistEnabled}


class hpicfOspfRedistRestrictEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([hpicfOspfRedistRestrictAddr, hpicfOspfRedistRestrictMask], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 3, 1])
	access = 2
	rowstatus = hpicfOspfRedistRestrictStatus
	columns = {'hpicfOspfRedistRestrictAddr': hpicfOspfRedistRestrictAddr, 'hpicfOspfRedistRestrictMask': hpicfOspfRedistRestrictMask, 'hpicfOspfRedistRestrictStatus': hpicfOspfRedistRestrictStatus}


# notifications (traps) 
# groups 
class hpicfOspfBaseGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 1])
	group = [hpicfOspf1583CompatibilityMode, hpicfOspfDefaultImportMetric, hpicfOspfDefaultImportMetricType]

class hpicfOspfRedistGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 2])
	group = [hpicfOspfRedistEnabled, hpicfOspfRedistRestrictStatus]

class hpicfOspfDistanceGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 3])
	group = [hpicfOspfIntraAreaDistance, hpicfOspfInterAreaDistance, hpicfOspfExternalDistance]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
