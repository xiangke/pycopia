# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from RFC1213_MIB import ifIndex
from SNMPv2_TC import DisplayString, RowStatus, MacAddress
from CISCO_SMI import ciscoMgmt

class CISCO_CIPLAN_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-CIPLAN-MIB'
	conformance = 2
	name = 'CISCO-CIPLAN-MIB'
	language = 2
	description = "This is the Management Information Base (MIB) \nmodule for objects used to manage the cisco internal \nLAN support in Cisco Mainframe Channel Connection \n(CMCC) environments.\n\n1) LAN\n2) Adapter \n\nThe following example configuration of a router that\nshows the entities managed by the CIPLAN MIB.\n\n                  Router A\n-----------------------------------------\n| ------------------------------------- |\n| |                                   | |\n| | -------------------               | |\n| | | Adapter         |      --       | |\n| | | 400000000401    |    /    \\     | |\n| | | ADAPNO 0        |---| Ring |    | |\n| | -------------------   |      |----| |\n| | | Adapter         |---| 1000 |    | |\n| | | 400000000402    |    \\    /     | |\n| | | ADAPNO 1        |      --       | |\n| | -------------------               | |\n| |                       Token Ring  | |\n| |                       LAN 0       | |\n| |                                   | |\n| |                          --       | |\n| | -------------------    /    \\     | |\n| | | Adapter         |---| Ring |    | |\n| | | 400000000401    |   |      |----| |\n| | | ADAPNO 3        |---| 1001 |    | |\n| | -------------------    \\    /     | |\n| |                          --       | |\n| |                                   | |\n| |                       Token Ring  | |\n| |                       LAN 1       | |\n| |                                   | |\n| |                                   | |\n| | -------------------               | |\n| | | Adapter         |           |   | |\n| | | 0200000000C1    |---------------| |\n| | | ADAPNO 4        |     |         | |\n| | -------------------               | |\n| |                       Ethernet    | |\n| |                       LAN 0       | |\n| |                                   | |\n| |                                   | |\n| | -------------------      =        | |\n| | | Adapter         |    /   \\      | |\n| | | 400000000001    |===|     |=====| |\n| | | ADAPNO 5        |    \\   /      | |\n| | -------------------      =        | |\n| |                                   | |\n| |                       FDDI        | |\n| |                       LAN 0       | |\n| |                                   | |\n| |     CMCC CARD 6                   | |\n| ------------------------------------- |\n|                                       |\n-----------------------------------------\n\nNOTE:  A special ifIndex has been created to address\ninternal LAN objects that are on the CMCC card.\n\nPhysically the CMCC card would have two ifIndex's\nof type `other` for each CMCC Slot/Daughter Board.\nThe additional ifIndex is made looks like the\nphysical with the Daughter Board being replaced\nwith a simple integer.  For example:\n\nIf the CMCC is in slot/bay 6; The first daughter\nboard would have the ifIndex of 6/0.  The\nsecond daughter board would have the ifIndex\nof 6/1.  The internal objects on this CMCC card\nwould have the ifIndex of 6/2.\n\nThe ifIndex is an INTEGER to which the values will\nbe translated to agent specific number by the \nagent itself.\n\n\nThe first table is the LAN Admin table.\nEach entry created in this table will represent a\ninternal CIP LAN that will be used by MAC adapters\nto bridge data to and from the host.\nThe indices of the table are:\n* The special ifIndex that addresses the virtual\nobjects on a CMCC card\n* The LAN type (token-ring, ethernet, fddi)\n* The unique LAN identifier\nNOTE:  This value is used to uniquely identify\neach and every LAN based on LAN type\nand on a single CMCC card.\nThe fields included in this table represent:\n* The LAN type used as on index\n* The unique LAN identifier used as an index\n* The bridging type\n* For Source Route Bridging, the local ring number\n* For Source Route Bridging, the next bridge number\n* For Source Route Bridging, the target ring number\n* For Transparent Bridging, the bridge group\n* The row control variable\nIn the example above, four entries would exist.\nThe first entry would be:\n- ifIndex is created by the agent\n- LAN type of token ring\n- LAN identifier of 0\n- bridging type of Source Route\n- local ring number 1000\n- next bridge number is unknown\n- target ring number is unknown\n- transparent bridge group has no meaning\nThe second entry would be:\n- ifIndex is created by the agent\n- LAN type of token ring\n- LAN identifier of 1\n- bridging type of Source Route\n- local ring number 1001\n- next bridge number is unknown\n- target ring number is unknown\n- transparent bridge group has no meaning\nThe third entry would be:\n- ifIndex is created by the agent\n- LAN type of ethernet\n- LAN identifier of 0\n- bridging type of transparent\n- local ring number has no meaning\n- next bridge number has no meaning\n- target ring number has no meaning\n- transparent bridge group is unknown\nThe fourth entry would be:\n- ifIndex is created by the agent\n- LAN type of fddi\n- LAN identifier of 0\n- bridging type of transparent\n- local ring number has no meaning\n- next bridge number has no meaning\n- target ring number has no meaning\n- transparent bridge group is unknown\n\nThe last table is the CIP LAN Adapter Admin table.\nEach entry created in this table will represent a\nLAN adapter on one of the CMCC internal LAN's\ndefined in the first table.\nThe indices of the table are:\n* The special ifIndex that addresses the virtual\nobjects on a CMCC card\n* The LAN type (token-ring, ethernet, fddi)\n* The unique LAN identifier from the first table\n* The unique Adapter Number for this LAN type\nNOTE:  When multiple LANs of the same type\nexist, this number must be kept unique\nby the agent.  (The LAN type is defined\nby the Virtual LAN Admin table.)\nThe fields included in this table represent:\n* The unique Adapter Number for this LAN type\nas defined by the LAN Admin Entry\ncorresponding the the first two indices in\nthis table\n* The MAC Address for this Adapter;  this\nMAC Address is unique for all Adapters\ndefine on this LAN, but does not need to be\nunique across LANs for redundancy\n* The Adapter name\n* The row control variable\nIn the example above, five entries would exist.\nThe first entry would be:\n- ifIndex is created by the agent\n- the LAN type from the first table\n- the LAN identifier from the first table = 0\n- adapter number of 0\n- Mac Address of 400000000401\n- Configured Name\nThe second entry would be:\n- ifIndex is created by the agent\n- the LAN type from the first table\n- the LAN identifier from the first table = 0\n- adapter number of 1\n- Mac Address of 400000000402\n- Configured Name\nThe first entry would be:\n- ifIndex is created by the agent\n- the LAN type from the first table\n- the LAN identifier from the first table = 1\n- adapter number of 2\n- Mac Address of 400000000401\n- Configured Name\nThe first entry would be:\n- ifIndex is created by the agent\n- the LAN type from the first table\n- the LAN identifier from the first table = 0\n- adapter number of 3\n- Mac Address of 0200000000C1\n- Configured Name\nThe first entry would be:\n- ifIndex is created by the agent\n- the LAN type from the first table\n- the LAN identifier from the first table = 0\n- adapter number of 4\n- Mac Address of 400000000001\n- Configured Name"

# nodes
class ciscoCipLanMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34])
	name = 'ciscoCipLanMIB'

class cipLanObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1])
	name = 'cipLanObjects'

class cipLan(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1])
	name = 'cipLan'

class ciscoCipLanMibConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 2])
	name = 'ciscoCipLanMibConformance'

class ciscoCipLanMibCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 1])
	name = 'ciscoCipLanMibCompliances'

class ciscoCipLanMibGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 2])
	name = 'ciscoCipLanMibGroups'


# macros
# types 
# scalars 
# columns
class cipCardLanAdminLanType(ColumnObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'iso88023csmacd'), Enum(2, 'iso88025tokenRing'), Enum(3, 'fddi')]


class cipCardLanAdminLanId(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipCardLanAdminBridgeType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'transparentOnly'), Enum(2, 'sourcerouteOnly'), Enum(3, 'transpAndSourceRoute')]


class cipCardLanAdminSrbLocalRing(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipCardLanAdminSrbBridgeNum(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipCardLanAdminSrbTargetRing(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipCardLanAdminTbBridgeGrp(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipCardLanAdminRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class cipCardLanAdaptAdminAdaptNo(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipCardLanAdaptAdminMacAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class cipCardLanAdaptAdminAdaptName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cipCardLanAdaptAdminRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class cipCardLanAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, cipCardLanAdminLanType, cipCardLanAdminLanId], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1])
	access = 2
	rowstatus = cipCardLanAdminRowStatus
	columns = {'cipCardLanAdminLanType': cipCardLanAdminLanType, 'cipCardLanAdminLanId': cipCardLanAdminLanId, 'cipCardLanAdminBridgeType': cipCardLanAdminBridgeType, 'cipCardLanAdminSrbLocalRing': cipCardLanAdminSrbLocalRing, 'cipCardLanAdminSrbBridgeNum': cipCardLanAdminSrbBridgeNum, 'cipCardLanAdminSrbTargetRing': cipCardLanAdminSrbTargetRing, 'cipCardLanAdminTbBridgeGrp': cipCardLanAdminTbBridgeGrp, 'cipCardLanAdminRowStatus': cipCardLanAdminRowStatus}


class cipCardLanAdaptAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, cipCardLanAdminLanType, cipCardLanAdminLanId, cipCardLanAdaptAdminAdaptNo], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1])
	access = 2
	rowstatus = cipCardLanAdaptAdminRowStatus
	columns = {'cipCardLanAdaptAdminAdaptNo': cipCardLanAdaptAdminAdaptNo, 'cipCardLanAdaptAdminMacAddress': cipCardLanAdaptAdminMacAddress, 'cipCardLanAdaptAdminAdaptName': cipCardLanAdaptAdminAdaptName, 'cipCardLanAdaptAdminRowStatus': cipCardLanAdaptAdminRowStatus}


# notifications (traps) 
# groups 
class ciscoLanGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 2, 1])
	group = [cipCardLanAdminBridgeType, cipCardLanAdminSrbLocalRing, cipCardLanAdminSrbBridgeNum, cipCardLanAdminSrbTargetRing, cipCardLanAdminTbBridgeGrp, cipCardLanAdminRowStatus]

class ciscoLanAdaptGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 2, 2])
	group = [cipCardLanAdaptAdminMacAddress, cipCardLanAdaptAdminAdaptName, cipCardLanAdaptAdminRowStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
