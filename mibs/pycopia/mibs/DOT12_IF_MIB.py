# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import transmission, Counter32, Counter64, OBJECT_TYPE, MODULE_IDENTITY
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from IF_MIB import ifIndex

class DOT12_IF_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/DOT12-IF-MIB'
	conformance = 3
	name = 'DOT12-IF-MIB'
	language = 2
	description = 'This MIB module describes objects for\nmanaging IEEE 802.12 interfaces.'

# nodes
class dot12MIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45])
	name = 'dot12MIB'

class dot12MIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1])
	name = 'dot12MIBObjects'

class dot12Conformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 2])
	name = 'dot12Conformance'

class dot12Compliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 2, 1])
	name = 'dot12Compliances'

class dot12Groups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 2, 2])
	name = 'dot12Groups'


# macros
# types 
# scalars 
# columns
class dot12CurrentFramingType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'frameType88023'), Enum(2, 'frameType88025'), Enum(3, 'frameTypeUnknown')]


class dot12DesiredFramingType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'frameType88023'), Enum(2, 'frameType88025'), Enum(3, 'frameTypeEither')]


class dot12FramingCapability(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'frameType88023'), Enum(2, 'frameType88025'), Enum(3, 'frameTypeEither')]


class dot12DesiredPromiscStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'singleAddressMode'), Enum(2, 'promiscuousMode')]


class dot12TrainingVersion(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot12LastTrainingConfig(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class dot12Commands(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noOp'), Enum(2, 'open'), Enum(3, 'reset'), Enum(4, 'close')]


class dot12Status(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'opened'), Enum(2, 'closed'), Enum(3, 'opening'), Enum(5, 'openFailure'), Enum(6, 'linkFailure')]


class dot12ControlMode(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'masterMode'), Enum(2, 'slaveMode'), Enum(3, 'learn')]


class dot12InHighPriorityFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot12InHighPriorityOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot12InNormPriorityFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot12InNormPriorityOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot12InIPMErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot12InOversizeFrameErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot12InDataErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot12InNullAddressedFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot12OutHighPriorityFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot12OutHighPriorityOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot12TransitionIntoTrainings(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot12HCInHighPriorityOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class dot12HCInNormPriorityOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class dot12HCOutHighPriorityOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


# rows 
class dot12ConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 1, 1])
	access = 2
	columns = {'dot12CurrentFramingType': dot12CurrentFramingType, 'dot12DesiredFramingType': dot12DesiredFramingType, 'dot12FramingCapability': dot12FramingCapability, 'dot12DesiredPromiscStatus': dot12DesiredPromiscStatus, 'dot12TrainingVersion': dot12TrainingVersion, 'dot12LastTrainingConfig': dot12LastTrainingConfig, 'dot12Commands': dot12Commands, 'dot12Status': dot12Status, 'dot12ControlMode': dot12ControlMode}


class dot12StatEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 1, 2, 1])
	access = 2
	columns = {'dot12InHighPriorityFrames': dot12InHighPriorityFrames, 'dot12InHighPriorityOctets': dot12InHighPriorityOctets, 'dot12InNormPriorityFrames': dot12InNormPriorityFrames, 'dot12InNormPriorityOctets': dot12InNormPriorityOctets, 'dot12InIPMErrors': dot12InIPMErrors, 'dot12InOversizeFrameErrors': dot12InOversizeFrameErrors, 'dot12InDataErrors': dot12InDataErrors, 'dot12InNullAddressedFrames': dot12InNullAddressedFrames, 'dot12OutHighPriorityFrames': dot12OutHighPriorityFrames, 'dot12OutHighPriorityOctets': dot12OutHighPriorityOctets, 'dot12TransitionIntoTrainings': dot12TransitionIntoTrainings, 'dot12HCInHighPriorityOctets': dot12HCInHighPriorityOctets, 'dot12HCInNormPriorityOctets': dot12HCInNormPriorityOctets, 'dot12HCOutHighPriorityOctets': dot12HCOutHighPriorityOctets}


# notifications (traps) 
# groups 
class dot12ConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 2, 2, 1])
	group = [dot12DesiredFramingType, dot12FramingCapability, dot12DesiredPromiscStatus, dot12TrainingVersion, dot12LastTrainingConfig, dot12Commands, dot12Status, dot12CurrentFramingType, dot12ControlMode]

class dot12StatsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 45, 2, 2, 2])
	group = [dot12InHighPriorityFrames, dot12InHighPriorityOctets, dot12InNormPriorityFrames, dot12InNormPriorityOctets, dot12InIPMErrors, dot12InOversizeFrameErrors, dot12InDataErrors, dot12InNullAddressedFrames, dot12OutHighPriorityFrames, dot12OutHighPriorityOctets, dot12TransitionIntoTrainings, dot12HCInHighPriorityOctets, dot12HCInNormPriorityOctets, dot12HCOutHighPriorityOctets]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
