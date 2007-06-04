# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from IF_MIB import ifIndex
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Integer32
from CISCO_TC import CountryCode
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import TruthValue, DisplayString

class CISCO_VOICE_IF_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-VOICE-IF-MIB'
	conformance = 3
	name = 'CISCO-VOICE-IF-MIB'
	language = 2
	description = 'Common Voice Interface MIB module.\nThe MIB module manages the common voice related parameters\nfor both voice analog and ISDN interfaces.'

# nodes
class ciscoVoiceInterfaceMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64])
	name = 'ciscoVoiceInterfaceMIB'

class cvIfObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1])
	name = 'cvIfObjects'

class cvIfCfgObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1])
	name = 'cvIfCfgObjects'

class cvIfConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 2])
	name = 'cvIfConformance'

class cvIfCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 2, 1])
	name = 'cvIfCompliances'

class cvIfGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 2, 2])
	name = 'cvIfGroups'


# macros
# types 
# scalars 
# columns
class cvIfCfgNoiseRegEnable(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cvIfCfgNonLinearProcEnable(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cvIfCfgMusicOnHoldThreshold(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'dBm'


class cvIfCfgInGain(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'dB'


class cvIfCfgOutAttn(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'dB'


class cvIfCfgEchoCancelEnable(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cvIfCfgEchoCancelCoverage(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'echoCanceller16ms'), Enum(2, 'echoCanceller24ms'), Enum(3, 'echoCanceller32ms')]


class cvIfCfgConnectionMode(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'normal'), Enum(2, 'trunk'), Enum(3, 'plar')]


class cvIfCfgConnectionNumber(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cvIfCfgInitialDigitTimeOut(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class cvIfCfgInterDigitTimeOut(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class cvIfCfgRegionalTone(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 12])
	syntaxobject = CountryCode


# rows 
class cvIfCfgEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1])
	access = 2
	columns = {'cvIfCfgNoiseRegEnable': cvIfCfgNoiseRegEnable, 'cvIfCfgNonLinearProcEnable': cvIfCfgNonLinearProcEnable, 'cvIfCfgMusicOnHoldThreshold': cvIfCfgMusicOnHoldThreshold, 'cvIfCfgInGain': cvIfCfgInGain, 'cvIfCfgOutAttn': cvIfCfgOutAttn, 'cvIfCfgEchoCancelEnable': cvIfCfgEchoCancelEnable, 'cvIfCfgEchoCancelCoverage': cvIfCfgEchoCancelCoverage, 'cvIfCfgConnectionMode': cvIfCfgConnectionMode, 'cvIfCfgConnectionNumber': cvIfCfgConnectionNumber, 'cvIfCfgInitialDigitTimeOut': cvIfCfgInitialDigitTimeOut, 'cvIfCfgInterDigitTimeOut': cvIfCfgInterDigitTimeOut, 'cvIfCfgRegionalTone': cvIfCfgRegionalTone}


# notifications (traps) 
# groups 
class cvIfGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 2, 2, 1])
	group = [cvIfCfgNoiseRegEnable, cvIfCfgNonLinearProcEnable, cvIfCfgMusicOnHoldThreshold, cvIfCfgInGain, cvIfCfgOutAttn, cvIfCfgEchoCancelEnable, cvIfCfgEchoCancelCoverage, cvIfCfgInitialDigitTimeOut, cvIfCfgInterDigitTimeOut, cvIfCfgRegionalTone]

class cvIfConnectionGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 64, 2, 2, 2])
	group = [cvIfCfgConnectionMode, cvIfCfgConnectionNumber]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
