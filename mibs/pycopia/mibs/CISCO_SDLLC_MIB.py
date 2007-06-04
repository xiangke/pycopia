# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Integer32, NOTIFICATION_TYPE
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import TruthValue, MacAddress
from IF_MIB import ifIndex

class CISCO_SDLLC_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-SDLLC-MIB'
	conformance = 3
	name = 'CISCO-SDLLC-MIB'
	language = 2
	description = "This is the MIB module for objects used to manage SDLLC.\n\nOverview of SDLLC conversion MIB\n\n\nMIB description                        \nThe SDLLC MIB includes read-only configuration and operational\ninformation on Cisco's implementation of SDLC to LLC2 media\ntranslation.  The following example shows the entities managed\nby the SDLLC MIB.\n\n\n FEP/ ==  Token == CISCO A == WAN/RSRB == CISCO B == Serial == SDLC  \n Host     Ring                                       line      station\n\n  |=============== LLC2 session ============|=== SDLC session ====|\n  \n  In this example configuration, CISCO B is performing the SDLLC \n  conversion, and so we query CISCO B for this MIB.\n  The SDLC device believes it is talking to the host via a direct\n  SDLC session.  The host believes it is talking to the SDLC station on \n  the same token ring.  CISCO A is also unaware of the SDLLC conversion\n  going on at CISCO B; it just believes it has an RSRB session with \n  its peer CISCO B to bridge two token ring separated by a WAN.\n  So CISCO B is the only agent that can provide the SDLLC conversion\n  details.  We can combine this MIB with the CISCO-RSRB-MIB from\n  either CISCO A or CISCO B to get a better picture of the network.\n  \n  This MIB has two tables:  \n  \n  convSdllcPortTable has an entry for each serial interface for \n  general SDLLC information on an interface, such as administered \n  virtual MAC addresses and virtual ring and bridge numbers.\n  This table is indexed by ifIndex.\n  \n  convSdllcAddrTable has an entry for each serial interface and\n  SDLC address pair.  It contains information specific to an SDLC\n  address on an interface, such as the partner MAC address, \n  XID value, and address state.  This table is indexed by ifIndex\n  and convSdllcAddrSdlcAddr (the address of the SDLC station).\n\n  The above configuration would have a single entry in each table.\n  If CISCO B had two serial lines configured for sdllc conversion, \n  there would be two entries per table.  If there\n  were only one serial line, but it was multipoint and\n  supported two sdlc addresses on the other end of the \n  line, there would be a single entry in convSdllcPortTable, and\n  two entries in convSdllcAddrTable.\n  \n  The MIB provides the following information for convSdllcPortTable:\n  \n  convSdllcPortVirtMacAddr - The locally administered MAC addressed\n    assigned to the serial interface.  Note that this address must\n    always end in '00'.  CISCO B replaces the 00 with the sdlc\n    address of the serial device.  For a multipoint configuration\n    with two SDLC stations the llc2 side will 'see' two token ring \n    stations with unique MAC addresses on the sdlc side.\n  convSdllcPortVirtRing - The locally administered token ring number\n    assigned to the serial interface.  This gives the serial interface\n    a token ring appearance to the llc2 side of the conversion, so\n    that it appears that it is a token ring on the other side of\n    a bridge.\n  convSdllcPortBridge - The bridge number assigned to CISCO B \n  convSdllcPortLlc2Ring - The token ring number on the LLC2 session\n    side.  In this case it is the RSRB virtual ring group number\n    between CISCO A and CISCO B.  \n  convSdllcPortLocalAck - indicates whether local acknowledgement\n    of SDLLC sessions is active.        \n  convSdllcPortLocalAckState - indicates the state of\n   the local acknowledgement session.   \n  convSdllcPortMaxLlc2FrameSize - the largest I-frame size that\n    can be sent or received on the LLC2 session.\n\n  The MIB provides the following information for convSdllcAddrTable:\n  convSdllcAddrSdlcAddr - The address of the SDLC station.\n  convSdllcAddrPartnerMacAddr - The MAC address of the FEP, as\n    specified with the sdllc partner command.\n  convSdllcAddrXID - The IDBLK and IDNUM of the SDLC station;\n    these must match the VTAM configured values\n  convSdllcAddrState - indicates the state of the SDLLC conversion\n  convSdllcAddrMaxSdlcFrameSize - the largest I-frame size that\n    can be sent or received on the SDLC session.\n                         "

# nodes
class ciscoSnaSdllcMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28])
	name = 'ciscoSnaSdllcMIB'

class convSdllcObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1])
	name = 'convSdllcObjects'

class convSdllcPorts(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1])
	name = 'convSdllcPorts'

class convSdllcAddrs(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2])
	name = 'convSdllcAddrs'

class convSdllcNotificationPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 2])
	name = 'convSdllcNotificationPrefix'

class convSdllcNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 2, 0])
	name = 'convSdllcNotifications'

class sdllcMibConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 3])
	name = 'sdllcMibConformance'

class sdllcMibCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 1])
	name = 'sdllcMibCompliances'

class sdllcMibGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 2])
	name = 'sdllcMibGroups'


# macros
# types 
# scalars 
# columns
class convSdllcPortVirtMacAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class convSdllcPortVirtRing(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class convSdllcPortBridge(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class convSdllcPortLlc2Ring(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class convSdllcPortLocalAck(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class convSdllcPortLocalAckState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'disconnected'), Enum(2, 'localDiscWait'), Enum(3, 'remDiscWait'), Enum(4, 'remWait'), Enum(5, 'localWait'), Enum(6, 'connectPending'), Enum(7, 'connected'), Enum(8, 'remQOnWait'), Enum(9, 'remQOffWait'), Enum(10, 'quenched'), Enum(255, 'unknown')]


class convSdllcPortMaxLlc2FrameSize(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class convSdllcAddrSdlcAddr(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class convSdllcAddrPartnerMacAddr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class convSdllcAddrXID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class convSdllcAddrState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'disconnected'), Enum(2, 'sdlcDisconnecting'), Enum(3, 'sdlcPriConnecting'), Enum(4, 'netDisconnecting'), Enum(5, 'netConnecting'), Enum(6, 'sdlcSecConnecting'), Enum(7, 'connected')]


class convSdllcAddrMaxSdlcFrameSize(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class convSdllcPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1])
	access = 2
	columns = {'convSdllcPortVirtMacAddr': convSdllcPortVirtMacAddr, 'convSdllcPortVirtRing': convSdllcPortVirtRing, 'convSdllcPortBridge': convSdllcPortBridge, 'convSdllcPortLlc2Ring': convSdllcPortLlc2Ring, 'convSdllcPortLocalAck': convSdllcPortLocalAck, 'convSdllcPortLocalAckState': convSdllcPortLocalAckState, 'convSdllcPortMaxLlc2FrameSize': convSdllcPortMaxLlc2FrameSize}


class convSdllcAddrEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, convSdllcAddrSdlcAddr], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1])
	access = 2
	columns = {'convSdllcAddrSdlcAddr': convSdllcAddrSdlcAddr, 'convSdllcAddrPartnerMacAddr': convSdllcAddrPartnerMacAddr, 'convSdllcAddrXID': convSdllcAddrXID, 'convSdllcAddrState': convSdllcAddrState, 'convSdllcAddrMaxSdlcFrameSize': convSdllcAddrMaxSdlcFrameSize}


# notifications (traps) 
class convSdllcPeerStateChangeNotification(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 2, 0, 1])

# groups 
class convSdllcPortGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 2, 1])
	group = [convSdllcPortVirtMacAddr, convSdllcPortVirtRing, convSdllcPortBridge, convSdllcPortLlc2Ring, convSdllcPortLocalAck, convSdllcPortLocalAckState, convSdllcPortMaxLlc2FrameSize]

class convSdllcAddrGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 2, 2])
	group = [convSdllcAddrPartnerMacAddr, convSdllcAddrXID, convSdllcAddrState, convSdllcAddrMaxSdlcFrameSize]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
