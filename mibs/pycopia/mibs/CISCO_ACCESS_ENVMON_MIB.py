# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from CISCO_ENVMON_MIB import ciscoEnvMonSupplyStatusEntry, ciscoEnvMonTemperatureStatusDescr, ciscoEnvMonTemperatureState, ciscoEnvMonVoltageStatusDescr, ciscoEnvMonVoltageState

class CISCO_ACCESS_ENVMON_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-ACCESS-ENVMON-MIB'
	conformance = 4
	name = 'CISCO-ACCESS-ENVMON-MIB'
	language = 2
	description = 'The MIB module to describe the additional status of\nthe Environmental Monitor on those Cisco Access devices\nwhich support one.'

# nodes
class ciscoAccessEnvMonMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 61])
	name = 'ciscoAccessEnvMonMIB'

class caemObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 61, 1])
	name = 'caemObjects'

class caemMIBNotificationPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 61, 2])
	name = 'caemMIBNotificationPrefix'

class caemMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0])
	name = 'caemMIBNotifications'

class caemConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 61, 3])
	name = 'caemConformance'

class caemCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 1])
	name = 'caemCompliances'

class caemGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 2])
	name = 'caemGroups'


# macros
# types 
# scalars 
# columns
class caemSupplyFailedComponent(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'none'), Enum(2, 'inputVoltage'), Enum(3, 'dcOutputVoltage'), Enum(4, 'thermal'), Enum(5, 'multiple'), Enum(6, 'fan'), Enum(7, 'overvoltage')]


# rows 
from CISCO_ENVMON_MIB import ciscoEnvMonSupplyStatusIndex
class caemSupplyStatusEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ciscoEnvMonSupplyStatusIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1, 1])
	access = 2
	columns = {'caemSupplyFailedComponent': caemSupplyFailedComponent}


# notifications (traps) 
class caemTemperatureNotification(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0, 1])

class caemVoltageNotification(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0, 2])

# groups 
class caemGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 2, 1])
	group = [caemSupplyFailedComponent]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
