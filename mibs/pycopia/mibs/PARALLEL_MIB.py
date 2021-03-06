# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Counter32, Integer32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from RFC1213_MIB import transmission
from IF_MIB import InterfaceIndex

class PARALLEL_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/PARALLEL-MIB'
	conformance = 3
	name = 'PARALLEL-MIB'
	language = 2
	description = 'The MIB module for Parallel-printer-like hardware devices.'

# nodes
class para(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34])
	name = 'para'

class paraConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 5])
	name = 'paraConformance'

class paraGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 5, 1])
	name = 'paraGroups'

class paraCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 5, 2])
	name = 'paraCompliances'


# macros
# types 
# scalars 
class paraNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# columns
class paraPortIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 1])
	syntaxobject = InterfaceIndex


class paraPortType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'centronics'), Enum(3, 'dataproducts')]


class paraPortInSigNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class paraPortOutSigNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class paraInSigPortIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 1])
	syntaxobject = InterfaceIndex


class paraInSigName(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'power'), Enum(2, 'online'), Enum(3, 'busy'), Enum(4, 'paperout'), Enum(5, 'fault')]


class paraInSigState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'on'), Enum(3, 'off')]


class paraInSigChanges(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class paraOutSigPortIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 1])
	syntaxobject = InterfaceIndex


class paraOutSigName(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'power'), Enum(2, 'online'), Enum(3, 'busy'), Enum(4, 'paperout'), Enum(5, 'fault')]


class paraOutSigState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'on'), Enum(3, 'off')]


class paraOutSigChanges(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
class paraPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([paraPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 2, 1])
	access = 2
	columns = {'paraPortIndex': paraPortIndex, 'paraPortType': paraPortType, 'paraPortInSigNumber': paraPortInSigNumber, 'paraPortOutSigNumber': paraPortOutSigNumber}


class paraInSigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([paraInSigPortIndex, paraInSigName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 3, 1])
	access = 2
	columns = {'paraInSigPortIndex': paraInSigPortIndex, 'paraInSigName': paraInSigName, 'paraInSigState': paraInSigState, 'paraInSigChanges': paraInSigChanges}


class paraOutSigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([paraOutSigPortIndex, paraOutSigName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 4, 1])
	access = 2
	columns = {'paraOutSigPortIndex': paraOutSigPortIndex, 'paraOutSigName': paraOutSigName, 'paraOutSigState': paraOutSigState, 'paraOutSigChanges': paraOutSigChanges}


# notifications (traps) 
# groups 
class paraGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 34, 5, 1, 1])
	group = [paraNumber, paraPortIndex, paraPortType, paraPortInSigNumber, paraPortOutSigNumber, paraInSigPortIndex, paraInSigName, paraInSigState, paraInSigChanges, paraOutSigPortIndex, paraOutSigName, paraOutSigState, paraOutSigChanges]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
