# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import Integer32, MODULE_IDENTITY, mib_2
from SNMPv2_TC import TEXTUAL_CONVENTION

class DIFFSERV_DSCP_TC(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/DIFFSERV-DSCP-TC'
	conformance = 5
	name = 'DIFFSERV-DSCP-TC'
	language = 2
	description = 'The Textual Conventions defined in this module should be used\nwhenever a Differentiated Services Code Point is used in a MIB.'

# nodes
class diffServDSCPTC(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 96])
	name = 'diffServDSCPTC'


# macros
# types 

class Dscp(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 63))
	format = 'd'


class DscpOrAny(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(-1, 63))
	format = 'd'

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
