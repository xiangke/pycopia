# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, OBJECT_IDENTITY
from ATM_MIB import atmTrafficDescrParamEntry
from CISCO_SMI import ciscoExperiment
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP

class CISCO_ATM_TRAFFIC_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-ATM-TRAFFIC-MIB'
	name = 'CISCO-ATM-TRAFFIC-MIB'
	language = 2
	description = 'This MIB module is an extension to traffic OIDs\nand variables defined in rfc1695.'

# nodes
class ciscoAtmTrafficExtMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11])
	name = 'ciscoAtmTrafficExtMIB'

class ciscoAtmTrafficExtMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 1])
	name = 'ciscoAtmTrafficExtMIBObjects'

class ciscoAtmTrafficTypeExt(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1])
	name = 'ciscoAtmTrafficTypeExt'

class atmNoClpNoScrCdvt(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 1])
	name = 'atmNoClpNoScrCdvt'

class atmClpScrMbsCdvt(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 2])
	name = 'atmClpScrMbsCdvt'

class atmNoClpScrMbsCdvt(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 3])
	name = 'atmNoClpScrMbsCdvt'

class atmNoClpMcr(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 4])
	name = 'atmNoClpMcr'

class atmNoClpMcrCdvt(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 5])
	name = 'atmNoClpMcrCdvt'

class ciscoAtmTrafficTableExt(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2])
	name = 'ciscoAtmTrafficTableExt'

class ciscoAtmTrafficExtMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 3])
	name = 'ciscoAtmTrafficExtMIBConformance'

class ciscoAtmTrafficExtMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1])
	name = 'ciscoAtmTrafficExtMIBCompliances'

class ciscoAtmTrafficExtMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2])
	name = 'ciscoAtmTrafficExtMIBGroups'


# macros
# types 
# scalars 
# columns
class atmTrafficExplicitServCategory(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'cbr'), Enum(2, 'vbrRt'), Enum(3, 'vbrNrt'), Enum(4, 'abr'), Enum(5, 'ubr'), Enum(6, 'notDef')]


class atmTrafficDerivedServCategory(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'cbr'), Enum(2, 'vbrRt'), Enum(3, 'vbrNrt'), Enum(4, 'abr'), Enum(5, 'ubr')]


# rows 
from ATM_MIB import atmTrafficDescrParamIndex
class atmTrafficDescrParamExtEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([atmTrafficDescrParamIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1])
	access = 2
	columns = {'atmTrafficExplicitServCategory': atmTrafficExplicitServCategory, 'atmTrafficDerivedServCategory': atmTrafficDerivedServCategory}


# notifications (traps) 
# groups 
class ciscoAtmTrafficTableExtMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2, 1])
	group = [atmTrafficExplicitServCategory, atmTrafficDerivedServCategory]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
