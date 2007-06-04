# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from FRAME_RELAY_DTE_MIB import DLCI
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE
from MPLS_TC_STD_MIB import mplsStdMIB
from MPLS_LSR_STD_MIB import mplsInterfaceIndex
from SNMPv2_TC import RowStatus, StorageType

class MPLS_LC_FR_STD_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/MPLS-LC-FR-STD-MIB'
	conformance = 4
	name = 'MPLS-LC-FR-STD-MIB'
	language = 2
	description = 'This MIB module contains managed object definitions for\nMPLS Label-Controlled Frame-Relay interfaces as defined\nin (RFC3034).\n\nCopyright (C) The Internet Society (2006).  This\nversion of this MIB module is part of RFC 4368; see\nthe RFC itself for full legal notices.'

# nodes
class mplsLcFrStdMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10])
	name = 'mplsLcFrStdMIB'

class mplsLcFrStdNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 0])
	name = 'mplsLcFrStdNotifications'

class mplsLcFrStdObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 1])
	name = 'mplsLcFrStdObjects'

class mplsLcFrStdConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 2])
	name = 'mplsLcFrStdConformance'

class mplsLcFrStdCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1])
	name = 'mplsLcFrStdCompliances'

class mplsLcFrStdGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 2])
	name = 'mplsLcFrStdGroups'


# macros
# types 
# scalars 
# columns
class mplsLcFrStdTrafficMinDlci(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 1])
	syntaxobject = DLCI


class mplsLcFrStdTrafficMaxDlci(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 2])
	syntaxobject = DLCI


class mplsLcFrStdCtrlMinDlci(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 3])
	syntaxobject = DLCI


class mplsLcFrStdCtrlMaxDlci(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 4])
	syntaxobject = DLCI


class mplsLcFrStdInterfaceConfRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class mplsLcFrStdInterfaceConfStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


# rows 
class mplsLcFrStdInterfaceConfEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsInterfaceIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1])
	access = 2
	rowstatus = mplsLcFrStdInterfaceConfRowStatus
	columns = {'mplsLcFrStdTrafficMinDlci': mplsLcFrStdTrafficMinDlci, 'mplsLcFrStdTrafficMaxDlci': mplsLcFrStdTrafficMaxDlci, 'mplsLcFrStdCtrlMinDlci': mplsLcFrStdCtrlMinDlci, 'mplsLcFrStdCtrlMaxDlci': mplsLcFrStdCtrlMaxDlci, 'mplsLcFrStdInterfaceConfRowStatus': mplsLcFrStdInterfaceConfRowStatus, 'mplsLcFrStdInterfaceConfStorageType': mplsLcFrStdInterfaceConfStorageType}


# notifications (traps) 
# groups 
class mplsLcFrStdIfGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 2, 1])
	group = [mplsLcFrStdTrafficMinDlci, mplsLcFrStdTrafficMaxDlci, mplsLcFrStdCtrlMinDlci, mplsLcFrStdCtrlMaxDlci, mplsLcFrStdInterfaceConfRowStatus, mplsLcFrStdInterfaceConfStorageType]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
