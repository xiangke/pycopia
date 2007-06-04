# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, OBJECT_IDENTITY, Counter32, Integer32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from RFC1213_MIB import transmission
from SNMPv2_TC import MacAddress, TimeStamp

class TOKENRING_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/TOKENRING-MIB'
	conformance = 2
	name = 'TOKENRING-MIB'
	language = 2
	description = 'The MIB module for IEEE Token Ring entities.'

# nodes
class dot5(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9])
	name = 'dot5'

class dot5Tests(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 3])
	name = 'dot5Tests'

class dot5TestInsertFunc(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 3, 1])
	name = 'dot5TestInsertFunc'

class dot5TestFullDuplexLoopBack(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 3, 2])
	name = 'dot5TestFullDuplexLoopBack'

class dot5ChipSets(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 4])
	name = 'dot5ChipSets'

class dot5ChipSetIBM16(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 4, 1])
	name = 'dot5ChipSetIBM16'

class dot5ChipSetTItms380(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 4, 2])
	name = 'dot5ChipSetTItms380'

class dot5ChipSetTItms380c16(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 4, 3])
	name = 'dot5ChipSetTItms380c16'

class dot5Conformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 6])
	name = 'dot5Conformance'

class dot5Groups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 6, 1])
	name = 'dot5Groups'

class dot5Compliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 6, 2])
	name = 'dot5Compliances'


# macros
# types 
# scalars 
# columns
class dot5IfIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5Commands(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noop'), Enum(2, 'open'), Enum(3, 'reset'), Enum(4, 'close')]


class dot5RingStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5RingState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'opened'), Enum(2, 'closed'), Enum(3, 'opening'), Enum(4, 'closing'), Enum(5, 'openFailure'), Enum(6, 'ringFailure')]


class dot5RingOpenStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noOpen'), Enum(2, 'badParam'), Enum(3, 'lobeFailed'), Enum(4, 'signalLoss'), Enum(5, 'insertionTimeout'), Enum(6, 'ringFailed'), Enum(7, 'beaconing'), Enum(8, 'duplicateMAC'), Enum(9, 'requestFailed'), Enum(10, 'removeReceived'), Enum(11, 'open')]


class dot5RingSpeed(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unknown'), Enum(2, 'oneMegabit'), Enum(3, 'fourMegabit'), Enum(4, 'sixteenMegabit')]


class dot5UpStream(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class dot5ActMonParticipate(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'true'), Enum(2, 'false')]


class dot5Functional(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class dot5LastBeaconSent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class dot5StatsIfIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5StatsLineErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsBurstErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsACErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsAbortTransErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsInternalErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsLostFrameErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsReceiveCongestions(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsFrameCopiedErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsTokenErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsSoftErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsHardErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsSignalLoss(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsTransmitBeacons(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsRecoverys(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsLobeWires(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsRemoves(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsSingles(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5StatsFreqErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class dot5TimerIfIndex(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5TimerReturnRepeat(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5TimerHolding(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5TimerQueuePDU(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5TimerValidTransmit(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5TimerNoToken(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5TimerActiveMon(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5TimerStandbyMon(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5TimerErrorReport(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5TimerBeaconTransmit(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class dot5TimerBeaconReceive(ColumnObject):
	access = 4
	status = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class dot5Entry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot5IfIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 1, 1])
	access = 2
	columns = {'dot5IfIndex': dot5IfIndex, 'dot5Commands': dot5Commands, 'dot5RingStatus': dot5RingStatus, 'dot5RingState': dot5RingState, 'dot5RingOpenStatus': dot5RingOpenStatus, 'dot5RingSpeed': dot5RingSpeed, 'dot5UpStream': dot5UpStream, 'dot5ActMonParticipate': dot5ActMonParticipate, 'dot5Functional': dot5Functional, 'dot5LastBeaconSent': dot5LastBeaconSent}


class dot5StatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([dot5StatsIfIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 2, 1])
	access = 2
	columns = {'dot5StatsIfIndex': dot5StatsIfIndex, 'dot5StatsLineErrors': dot5StatsLineErrors, 'dot5StatsBurstErrors': dot5StatsBurstErrors, 'dot5StatsACErrors': dot5StatsACErrors, 'dot5StatsAbortTransErrors': dot5StatsAbortTransErrors, 'dot5StatsInternalErrors': dot5StatsInternalErrors, 'dot5StatsLostFrameErrors': dot5StatsLostFrameErrors, 'dot5StatsReceiveCongestions': dot5StatsReceiveCongestions, 'dot5StatsFrameCopiedErrors': dot5StatsFrameCopiedErrors, 'dot5StatsTokenErrors': dot5StatsTokenErrors, 'dot5StatsSoftErrors': dot5StatsSoftErrors, 'dot5StatsHardErrors': dot5StatsHardErrors, 'dot5StatsSignalLoss': dot5StatsSignalLoss, 'dot5StatsTransmitBeacons': dot5StatsTransmitBeacons, 'dot5StatsRecoverys': dot5StatsRecoverys, 'dot5StatsLobeWires': dot5StatsLobeWires, 'dot5StatsRemoves': dot5StatsRemoves, 'dot5StatsSingles': dot5StatsSingles, 'dot5StatsFreqErrors': dot5StatsFreqErrors}


# notifications (traps) 
# groups 
class dot5StateGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 6, 1, 1])
	group = [dot5Commands, dot5RingStatus, dot5RingState, dot5RingOpenStatus, dot5RingSpeed, dot5UpStream, dot5ActMonParticipate, dot5Functional, dot5LastBeaconSent]

class dot5StatsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 9, 6, 1, 2])
	group = [dot5StatsLineErrors, dot5StatsBurstErrors, dot5StatsACErrors, dot5StatsAbortTransErrors, dot5StatsInternalErrors, dot5StatsLostFrameErrors, dot5StatsReceiveCongestions, dot5StatsFrameCopiedErrors, dot5StatsTokenErrors, dot5StatsSoftErrors, dot5StatsHardErrors, dot5StatsSignalLoss, dot5StatsTransmitBeacons, dot5StatsRecoverys, dot5StatsLobeWires, dot5StatsRemoves, dot5StatsSingles, dot5StatsFreqErrors]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
