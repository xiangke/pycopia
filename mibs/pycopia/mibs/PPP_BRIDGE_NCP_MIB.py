# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from RFC_1212 import OBJECT_TYPE
from RFC1213_MIB import ifIndex
from PPP_LCP_MIB import ppp
from RFC1155_SMI import Counter

class PPP_BRIDGE_NCP_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/PPP-BRIDGE-NCP-MIB'
	conformance = 2
	name = 'PPP-BRIDGE-NCP-MIB'
	language = 1

# nodes
class pppBridge(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4])
	name = 'pppBridge'


# macros
# types 
# scalars 
# columns
class pppBridgeOperStatus(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'opened'), Enum(2, 'not-opened')]


class pppBridgeLocalToRemoteTinygramCompression(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'false'), Enum(2, 'true')]


class pppBridgeRemoteToLocalTinygramCompression(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'false'), Enum(2, 'true')]


class pppBridgeLocalToRemoteLanId(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'false'), Enum(2, 'true')]


class pppBridgeRemoteToLocalLanId(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'false'), Enum(2, 'true')]


class pppBridgeConfigAdminStatus(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'open'), Enum(2, 'close')]


class pppBridgeConfigTinygram(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'false'), Enum(2, 'true')]


class pppBridgeConfigRingId(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'false'), Enum(2, 'true')]


class pppBridgeConfigLineId(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'false'), Enum(2, 'true')]


class pppBridgeConfigLanId(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'false'), Enum(2, 'true')]


class pppBridgeMediaMacType(ColumnObject):
	access = 4
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class pppBridgeMediaLocalStatus(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'accept'), Enum(2, 'dont-accept')]


class pppBridgeMediaRemoteStatus(ColumnObject):
	status = 3
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'accept'), Enum(2, 'dont-accept')]


class pppBridgeMediaConfigMacType(ColumnObject):
	access = 5
	status = 3
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class pppBridgeMediaConfigLocalStatus(ColumnObject):
	status = 3
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'accept'), Enum(2, 'dont-accept')]


# rows 
class pppBridgeEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1])
	access = 2
	columns = {'pppBridgeOperStatus': pppBridgeOperStatus, 'pppBridgeLocalToRemoteTinygramCompression': pppBridgeLocalToRemoteTinygramCompression, 'pppBridgeRemoteToLocalTinygramCompression': pppBridgeRemoteToLocalTinygramCompression, 'pppBridgeLocalToRemoteLanId': pppBridgeLocalToRemoteLanId, 'pppBridgeRemoteToLocalLanId': pppBridgeRemoteToLocalLanId}


class pppBridgeConfigEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1])
	access = 2
	columns = {'pppBridgeConfigAdminStatus': pppBridgeConfigAdminStatus, 'pppBridgeConfigTinygram': pppBridgeConfigTinygram, 'pppBridgeConfigRingId': pppBridgeConfigRingId, 'pppBridgeConfigLineId': pppBridgeConfigLineId, 'pppBridgeConfigLanId': pppBridgeConfigLanId}


class pppBridgeMediaEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, pppBridgeMediaMacType], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1])
	access = 2
	columns = {'pppBridgeMediaMacType': pppBridgeMediaMacType, 'pppBridgeMediaLocalStatus': pppBridgeMediaLocalStatus, 'pppBridgeMediaRemoteStatus': pppBridgeMediaRemoteStatus}


class pppBridgeMediaConfigEntry(RowObject):
	status = 3
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, pppBridgeMediaConfigMacType], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 23, 4, 4, 1])
	access = 2
	columns = {'pppBridgeMediaConfigMacType': pppBridgeMediaConfigMacType, 'pppBridgeMediaConfigLocalStatus': pppBridgeMediaConfigLocalStatus}


# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
