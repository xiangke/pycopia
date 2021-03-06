# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Unsigned32, Counter32, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import TruthValue
from ROHC_MIB import rohcChannelID, rohcContextCID

class ROHC_RTP_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/ROHC-RTP-MIB'
	name = 'ROHC-RTP-MIB'
	language = 2
	description = 'This MIB module defines a set of objects for monitoring\nand configuring RObust Header Compression (ROHC).\nThe objects are specific to ROHC RTP (profile 0x0001),\nROHC UDP (profile 0x0002), and ROHC ESP (profile 0x0003)\ndefined in RFC 3095 and for the ROHC LLA profile (profile\n0x0005) defined in RFC 3242.\n\nCopyright (C) The Internet Society (2004). The\ninitial version of this MIB module was published\nin RFC 3816. For full legal notices see the RFC\nitself or see:\nhttp://www.ietf.org/copyrights/ianamib.html'

# nodes
class rohcRtpMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114])
	name = 'rohcRtpMIB'

class rohcRtpObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1])
	name = 'rohcRtpObjects'

class rohcRtpConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 2])
	name = 'rohcRtpConformance'

class rohcRtpCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 2, 1])
	name = 'rohcRtpCompliances'

class rohcRtpGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 2, 2])
	name = 'rohcRtpGroups'


# macros
# types 
# scalars 
# columns
class rohcRtpContextState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'initAndRefresh'), Enum(2, 'firstOrder'), Enum(3, 'secondOrder'), Enum(4, 'noContext'), Enum(5, 'staticContext'), Enum(6, 'fullContext')]


class rohcRtpContextMode(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unidirectional'), Enum(2, 'optimistic'), Enum(3, 'reliable')]


class rohcRtpContextAlwaysPad(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class rohcRtpContextLargePktsAllowed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class rohcRtpContextVerifyPeriod(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class rohcRtpContextSizesAllowed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class rohcRtpContextSizesUsed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class rohcRtpContextACKs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rohcRtpContextNACKs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rohcRtpContextSNACKs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rohcRtpContextNHPs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rohcRtpContextCSPs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rohcRtpContextCCPs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rohcRtpContextPktsLostPhysical(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rohcRtpContextPktsLostPreLink(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rohcRtpPacketSize(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class rohcRtpPacketSizePreferred(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class rohcRtpPacketSizeUsed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class rohcRtpPacketSizeRestrictedType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'nhpOnly'), Enum(2, 'rhpOnly'), Enum(3, 'noRestrictions')]


# rows 
class rohcRtpContextEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([rohcChannelID, rohcContextCID], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 1, 1])
	access = 2
	columns = {'rohcRtpContextState': rohcRtpContextState, 'rohcRtpContextMode': rohcRtpContextMode, 'rohcRtpContextAlwaysPad': rohcRtpContextAlwaysPad, 'rohcRtpContextLargePktsAllowed': rohcRtpContextLargePktsAllowed, 'rohcRtpContextVerifyPeriod': rohcRtpContextVerifyPeriod, 'rohcRtpContextSizesAllowed': rohcRtpContextSizesAllowed, 'rohcRtpContextSizesUsed': rohcRtpContextSizesUsed, 'rohcRtpContextACKs': rohcRtpContextACKs, 'rohcRtpContextNACKs': rohcRtpContextNACKs, 'rohcRtpContextSNACKs': rohcRtpContextSNACKs, 'rohcRtpContextNHPs': rohcRtpContextNHPs, 'rohcRtpContextCSPs': rohcRtpContextCSPs, 'rohcRtpContextCCPs': rohcRtpContextCCPs, 'rohcRtpContextPktsLostPhysical': rohcRtpContextPktsLostPhysical, 'rohcRtpContextPktsLostPreLink': rohcRtpContextPktsLostPreLink}


class rohcRtpPacketSizeEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([rohcChannelID, rohcContextCID, rohcRtpPacketSize], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 1, 2, 1])
	access = 2
	columns = {'rohcRtpPacketSize': rohcRtpPacketSize, 'rohcRtpPacketSizePreferred': rohcRtpPacketSizePreferred, 'rohcRtpPacketSizeUsed': rohcRtpPacketSizeUsed, 'rohcRtpPacketSizeRestrictedType': rohcRtpPacketSizeRestrictedType}


# notifications (traps) 
# groups 
class rohcRtpContextGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 2, 2, 1])
	group = [rohcRtpContextState, rohcRtpContextMode, rohcRtpContextAlwaysPad, rohcRtpContextLargePktsAllowed, rohcRtpContextVerifyPeriod]

class rohcRtpPacketSizesGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 2, 2, 2])
	group = [rohcRtpContextSizesAllowed, rohcRtpContextSizesUsed, rohcRtpPacketSizePreferred, rohcRtpPacketSizeUsed, rohcRtpPacketSizeRestrictedType]

class rohcRtpStatisticsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 114, 2, 2, 3])
	group = [rohcRtpContextACKs, rohcRtpContextNACKs, rohcRtpContextSNACKs, rohcRtpContextNHPs, rohcRtpContextCSPs, rohcRtpContextCCPs, rohcRtpContextPktsLostPhysical, rohcRtpContextPktsLostPreLink]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
