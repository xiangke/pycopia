# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, Gauge32, mib_2
from SNMPv2_TC import TEXTUAL_CONVENTION

class PerfHist_TC_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/PerfHist-TC-MIB'
	conformance = 5
	name = 'PerfHist-TC-MIB'
	language = 2
	description = 'This MIB Module provides Textual Conventions\nto be used by systems supporting 15 minute\nbased performance history counts.\n\nCopyright (C) The Internet Society (2003).\nThis version of this MIB module is part of\nRFC 3593;  see the RFC itself for full\nlegal notices.'

# nodes
class perfHistTCMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 58])
	name = 'perfHistTCMIB'


# macros
# types 

class PerfCurrentCount(pycopia.SMI.Basetypes.Gauge32):
	status = 1


class PerfIntervalCount(pycopia.SMI.Basetypes.Gauge32):
	status = 1


class PerfTotalCount(pycopia.SMI.Basetypes.Gauge32):
	status = 1

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
