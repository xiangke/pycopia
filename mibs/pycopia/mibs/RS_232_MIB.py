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

class RS_232_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/RS-232-MIB'
	conformance = 3
	name = 'RS-232-MIB'
	language = 2
	description = 'The MIB module for RS-232-like hardware devices.'

# nodes
class rs232(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33])
	name = 'rs232'

class rs232Conformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 7])
	name = 'rs232Conformance'

class rs232Groups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 7, 1])
	name = 'rs232Groups'

class rs232Compliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 7, 2])
	name = 'rs232Compliances'


# macros
# types 
# scalars 
class rs232Number(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# columns
class rs232PortIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 1])
	syntaxobject = InterfaceIndex


class rs232PortType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'rs232'), Enum(3, 'rs422'), Enum(4, 'rs423'), Enum(5, 'v35'), Enum(6, 'x21')]


class rs232PortInSigNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rs232PortOutSigNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rs232PortInSpeed(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rs232PortOutSpeed(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rs232PortInFlowType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'ctsRts'), Enum(3, 'dsrDtr')]


class rs232PortOutFlowType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'ctsRts'), Enum(3, 'dsrDtr')]


class rs232AsyncPortIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 1])
	syntaxobject = InterfaceIndex


class rs232AsyncPortBits(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rs232AsyncPortStopBits(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'one'), Enum(2, 'two'), Enum(3, 'oneAndHalf'), Enum(4, 'dynamic')]


class rs232AsyncPortParity(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'odd'), Enum(3, 'even'), Enum(4, 'mark'), Enum(5, 'space')]


class rs232AsyncPortAutobaud(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class rs232AsyncPortParityErrs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rs232AsyncPortFramingErrs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rs232AsyncPortOverrunErrs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rs232SyncPortIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 1])
	syntaxobject = InterfaceIndex


class rs232SyncPortClockSource(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'internal'), Enum(2, 'external'), Enum(3, 'split')]


class rs232SyncPortFrameCheckErrs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rs232SyncPortTransmitUnderrunErrs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rs232SyncPortReceiveOverrunErrs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rs232SyncPortInterruptedFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rs232SyncPortAbortedFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rs232SyncPortRole(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'dte'), Enum(2, 'dce')]


class rs232SyncPortEncoding(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'nrz'), Enum(2, 'nrzi')]


class rs232SyncPortRTSControl(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'controlled'), Enum(2, 'constant')]


class rs232SyncPortRTSCTSDelay(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rs232SyncPortMode(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'fdx'), Enum(2, 'hdx'), Enum(3, 'simplex-receive'), Enum(4, 'simplex-send')]


class rs232SyncPortIdlePattern(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'mark'), Enum(2, 'space')]


class rs232SyncPortMinFlags(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rs232InSigPortIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 5, 1, 1])
	syntaxobject = InterfaceIndex


class rs232InSigName(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'rts'), Enum(2, 'cts'), Enum(3, 'dsr'), Enum(4, 'dtr'), Enum(5, 'ri'), Enum(6, 'dcd'), Enum(7, 'sq'), Enum(8, 'srs'), Enum(9, 'srts'), Enum(10, 'scts'), Enum(11, 'sdcd')]


class rs232InSigState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'on'), Enum(3, 'off')]


class rs232InSigChanges(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 5, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rs232OutSigPortIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 6, 1, 1])
	syntaxobject = InterfaceIndex


class rs232OutSigName(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'rts'), Enum(2, 'cts'), Enum(3, 'dsr'), Enum(4, 'dtr'), Enum(5, 'ri'), Enum(6, 'dcd'), Enum(7, 'sq'), Enum(8, 'srs'), Enum(9, 'srts'), Enum(10, 'scts'), Enum(11, 'sdcd')]


class rs232OutSigState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 6, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'on'), Enum(3, 'off')]


class rs232OutSigChanges(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 6, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
class rs232PortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([rs232PortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 2, 1])
	access = 2
	columns = {'rs232PortIndex': rs232PortIndex, 'rs232PortType': rs232PortType, 'rs232PortInSigNumber': rs232PortInSigNumber, 'rs232PortOutSigNumber': rs232PortOutSigNumber, 'rs232PortInSpeed': rs232PortInSpeed, 'rs232PortOutSpeed': rs232PortOutSpeed, 'rs232PortInFlowType': rs232PortInFlowType, 'rs232PortOutFlowType': rs232PortOutFlowType}


class rs232AsyncPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([rs232AsyncPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 3, 1])
	access = 2
	columns = {'rs232AsyncPortIndex': rs232AsyncPortIndex, 'rs232AsyncPortBits': rs232AsyncPortBits, 'rs232AsyncPortStopBits': rs232AsyncPortStopBits, 'rs232AsyncPortParity': rs232AsyncPortParity, 'rs232AsyncPortAutobaud': rs232AsyncPortAutobaud, 'rs232AsyncPortParityErrs': rs232AsyncPortParityErrs, 'rs232AsyncPortFramingErrs': rs232AsyncPortFramingErrs, 'rs232AsyncPortOverrunErrs': rs232AsyncPortOverrunErrs}


class rs232SyncPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([rs232SyncPortIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 4, 1])
	access = 2
	columns = {'rs232SyncPortIndex': rs232SyncPortIndex, 'rs232SyncPortClockSource': rs232SyncPortClockSource, 'rs232SyncPortFrameCheckErrs': rs232SyncPortFrameCheckErrs, 'rs232SyncPortTransmitUnderrunErrs': rs232SyncPortTransmitUnderrunErrs, 'rs232SyncPortReceiveOverrunErrs': rs232SyncPortReceiveOverrunErrs, 'rs232SyncPortInterruptedFrames': rs232SyncPortInterruptedFrames, 'rs232SyncPortAbortedFrames': rs232SyncPortAbortedFrames, 'rs232SyncPortRole': rs232SyncPortRole, 'rs232SyncPortEncoding': rs232SyncPortEncoding, 'rs232SyncPortRTSControl': rs232SyncPortRTSControl, 'rs232SyncPortRTSCTSDelay': rs232SyncPortRTSCTSDelay, 'rs232SyncPortMode': rs232SyncPortMode, 'rs232SyncPortIdlePattern': rs232SyncPortIdlePattern, 'rs232SyncPortMinFlags': rs232SyncPortMinFlags}


class rs232InSigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([rs232InSigPortIndex, rs232InSigName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 5, 1])
	access = 2
	columns = {'rs232InSigPortIndex': rs232InSigPortIndex, 'rs232InSigName': rs232InSigName, 'rs232InSigState': rs232InSigState, 'rs232InSigChanges': rs232InSigChanges}


class rs232OutSigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([rs232OutSigPortIndex, rs232OutSigName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 6, 1])
	access = 2
	columns = {'rs232OutSigPortIndex': rs232OutSigPortIndex, 'rs232OutSigName': rs232OutSigName, 'rs232OutSigState': rs232OutSigState, 'rs232OutSigChanges': rs232OutSigChanges}


# notifications (traps) 
# groups 
class rs232Group(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 7, 1, 1])
	group = [rs232Number, rs232PortIndex, rs232PortType, rs232PortInSigNumber, rs232PortOutSigNumber, rs232PortInSpeed, rs232PortOutSpeed, rs232PortInFlowType, rs232PortOutFlowType, rs232InSigPortIndex, rs232InSigName, rs232InSigState, rs232InSigChanges, rs232OutSigPortIndex, rs232OutSigName, rs232OutSigState, rs232OutSigChanges]

class rs232AsyncGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 7, 1, 2])
	group = [rs232AsyncPortIndex, rs232AsyncPortBits, rs232AsyncPortStopBits, rs232AsyncPortParity, rs232AsyncPortAutobaud, rs232AsyncPortParityErrs, rs232AsyncPortFramingErrs, rs232AsyncPortOverrunErrs]

class rs232SyncGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 7, 1, 3])
	group = [rs232SyncPortIndex, rs232SyncPortClockSource, rs232SyncPortFrameCheckErrs, rs232SyncPortTransmitUnderrunErrs, rs232SyncPortReceiveOverrunErrs, rs232SyncPortInterruptedFrames, rs232SyncPortAbortedFrames]

class rs232SyncSDLCGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 33, 7, 1, 4])
	group = [rs232SyncPortRole, rs232SyncPortEncoding, rs232SyncPortRTSControl, rs232SyncPortRTSCTSDelay, rs232SyncPortMode, rs232SyncPortIdlePattern, rs232SyncPortMinFlags]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
