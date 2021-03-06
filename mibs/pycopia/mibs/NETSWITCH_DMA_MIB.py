# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from RFC_1212 import OBJECT_TYPE
from RFC1155_SMI import enterprises, Counter

class NETSWITCH_DMA_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/NETSWITCH-DMA-MIB'
	name = 'NETSWITCH-DMA-MIB'
	language = 1

# nodes
class hp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11])
	name = 'hp'

class nm(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2])
	name = 'nm'

class icf(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14])
	name = 'icf'

class hpicfObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11])
	name = 'hpicfObjects'

class hpicfSwitch(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5])
	name = 'hpicfSwitch'

class hpSwitch(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1])
	name = 'hpSwitch'

class hpOpSystem(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1])
	name = 'hpOpSystem'

class hpHwSystem(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2])
	name = 'hpHwSystem'

class hpDMAStats(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2])
	name = 'hpDMAStats'


# macros
# types 
# scalars 
class hpDMAReset(ScalarObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'reset')]


class hpDMAFrameRcvcnt(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAOctetsRcvcnt(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAPrevRcvFrames(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAFrameRcvPerSec(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAPeakRcvFrames(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAPrevRcvOctets(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAOctetsRcvPerSec(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAPeakRcvOctets(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAFrameXmtcnt(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAOctetsXmtcnt(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAPrevXmtFrames(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAFrameXmtPerSec(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAPeakXmtFrames(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAPrevXmtOctets(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAOctetsXmtPerSec(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAPeakXmtOctets(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAFrameClippedcnt(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAFrameClippedOccurance(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class hpDMAMissBufCnt(ScalarObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# columns
# rows 
# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
