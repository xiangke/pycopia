# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY
from HP_ICF_OID import hpicfAdmin
from SNMPv2_TC import TEXTUAL_CONVENTION

class HP_ICF_TC(ModuleObject):
	path = '/usr/share/snmp/mibs/site/HP-ICF-TC'
	conformance = 5
	name = 'HP-ICF-TC'
	language = 2
	description = 'This module contains common textual convention\ndefinitons used by various HP ICF MIB modules.'

# nodes
class hpicfTextualConventions(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 4])
	name = 'hpicfTextualConventions'


# macros
# types 

class ConfigStatus(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'active'), Enum(2, 'notInService'), Enum(3, 'notReady')]


class HpSwitchPortType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'none'), Enum(3, 'unknown'), Enum(6, 'ethernetCsmacd'), Enum(7, 'iso88023Csmacd'), Enum(15, 'fddi'), Enum(37, 'atm'), Enum(54, 'propMultiplexor'), Enum(55, 'ieee80212'), Enum(62, 'fastEther'), Enum(69, 'fastEtherFX'), Enum(117, 'gigabitEthernetSX'), Enum(118, 'gigabitEthernetLX'), Enum(119, 'gigabitEthernetT'), Enum(120, 'gigabitEthernetStk'), Enum(121, 'gigabitEthernetLH')]

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
