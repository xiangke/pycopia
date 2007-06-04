# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_IDENTITY, enterprises

class CISCO_SMI(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-SMI'
	conformance = 5
	name = 'CISCO-SMI'
	language = 2
	description = 'The Structure of Management Information for the\nCisco enterprise.'

# nodes
class cisco(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9])
	name = 'cisco'

class ciscoProducts(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 1])
	name = 'ciscoProducts'

class local(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 2])
	name = 'local'

class temporary(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 3])
	name = 'temporary'

class pakmon(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 4])
	name = 'pakmon'

class workgroup(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 5])
	name = 'workgroup'

class otherEnterprises(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 6])
	name = 'otherEnterprises'

class ciscoAgentCapability(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 7])
	name = 'ciscoAgentCapability'

class ciscoConfig(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 8])
	name = 'ciscoConfig'

class ciscoMgmt(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9])
	name = 'ciscoMgmt'

class ciscoExperiment(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10])
	name = 'ciscoExperiment'

class ciscoAdmin(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11])
	name = 'ciscoAdmin'

class ciscoProxy(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 1])
	name = 'ciscoProxy'

class ciscoPartyProxy(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 1, 1])
	name = 'ciscoPartyProxy'

class ciscoContextProxy(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 1, 2])
	name = 'ciscoContextProxy'

class ciscoRptrGroupObjectID(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 2])
	name = 'ciscoRptrGroupObjectID'

class ciscoUnknownRptrGroup(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 2, 1])
	name = 'ciscoUnknownRptrGroup'

class cisco2505RptrGroup(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 2, 2])
	name = 'cisco2505RptrGroup'

class cisco2507RptrGroup(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 2, 3])
	name = 'cisco2507RptrGroup'

class cisco2516RptrGroup(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 2, 4])
	name = 'cisco2516RptrGroup'

class ciscoWsx5020RptrGroup(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 2, 5])
	name = 'ciscoWsx5020RptrGroup'

class ciscoChipSets(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 3])
	name = 'ciscoChipSets'

class ciscoChipSetSaint1(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 3, 1])
	name = 'ciscoChipSetSaint1'

class ciscoChipSetSaint2(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 3, 2])
	name = 'ciscoChipSetSaint2'

class ciscoChipSetSaint3(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 3, 3])
	name = 'ciscoChipSetSaint3'

class ciscoChipSetSaint4(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 11, 3, 4])
	name = 'ciscoChipSetSaint4'

class ciscoModules(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 12])
	name = 'ciscoModules'

class lightstream(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 13])
	name = 'lightstream'

class ciscoworks(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 14])
	name = 'ciscoworks'

class newport(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 15])
	name = 'newport'

class ciscoPartnerProducts(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 16])
	name = 'ciscoPartnerProducts'

class ciscoPolicy(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 17])
	name = 'ciscoPolicy'

class ciscoPIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 17, 2])
	name = 'ciscoPIB'

class ciscoPolicyAuto(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 18])
	name = 'ciscoPolicyAuto'

class ciscoPibToMib(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 18, 2])
	name = 'ciscoPibToMib'


# macros
# types 
# scalars 
# columns
# rows 
# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
