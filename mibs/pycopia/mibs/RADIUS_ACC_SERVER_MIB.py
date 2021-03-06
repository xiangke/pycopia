# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, OBJECT_IDENTITY, Counter32, Integer32, IpAddress, TimeTicks, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from INET_ADDRESS_MIB import InetAddressType, InetAddress
from SNMP_FRAMEWORK_MIB import SnmpAdminString

class RADIUS_ACC_SERVER_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/RADIUS-ACC-SERVER-MIB'
	conformance = 4
	name = 'RADIUS-ACC-SERVER-MIB'
	language = 2
	description = 'The MIB module for entities implementing the server\nside of the Remote Authentication Dial-In User\nService (RADIUS) accounting protocol.  Copyright (C)\nThe Internet Society (2006).  This version of this\nMIB module is part of RFC 4671; see the RFC itself\nfor full legal notices.'

# nodes
class radiusMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67])
	name = 'radiusMIB'

class radiusAccounting(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2])
	name = 'radiusAccounting'

class radiusAccServMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1])
	name = 'radiusAccServMIB'

class radiusAccServMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1])
	name = 'radiusAccServMIBObjects'

class radiusAccServ(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1])
	name = 'radiusAccServ'

class radiusAccServMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 2])
	name = 'radiusAccServMIBConformance'

class radiusAccServMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1])
	name = 'radiusAccServMIBCompliances'

class radiusAccServMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2])
	name = 'radiusAccServMIBGroups'


# macros
# types 
# scalars 
class radiusAccServIdent(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 1])
	syntaxobject = SnmpAdminString


class radiusAccServUpTime(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class radiusAccServResetTime(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class radiusAccServConfigReset(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'reset'), Enum(3, 'initializing'), Enum(4, 'running')]


class radiusAccServTotalRequests(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServTotalInvalidRequests(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServTotalDupRequests(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServTotalResponses(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServTotalMalformedRequests(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServTotalBadAuthenticators(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServTotalPacketsDropped(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServTotalNoRecords(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServTotalUnknownTypes(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


# columns
class radiusAccClientIndex(ColumnObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class radiusAccClientAddress(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class radiusAccClientID(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 3])
	syntaxobject = SnmpAdminString


class radiusAccServPacketsDropped(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServRequests(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServDupRequests(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServResponses(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServBadAuthenticators(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServMalformedRequests(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServNoRecords(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServUnknownTypes(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientExtIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class radiusAccClientInetAddressType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 2])
	syntaxobject = InetAddressType


class radiusAccClientInetAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 3])
	syntaxobject = InetAddress


class radiusAccClientExtID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 4])
	syntaxobject = SnmpAdminString


class radiusAccServExtPacketsDropped(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServExtRequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServExtDupRequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServExtResponses(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServExtBadAuthenticators(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServExtMalformedRequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServExtNoRecords(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServExtUnknownTypes(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServerCounterDiscontinuity(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks
	access = 4
	units = 'centiseconds'


# rows 
class radiusAccClientEntry(RowObject):
	status = 2
	index = pycopia.SMI.Objects.IndexObjects([radiusAccClientIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1])
	access = 2
	columns = {'radiusAccClientIndex': radiusAccClientIndex, 'radiusAccClientAddress': radiusAccClientAddress, 'radiusAccClientID': radiusAccClientID, 'radiusAccServPacketsDropped': radiusAccServPacketsDropped, 'radiusAccServRequests': radiusAccServRequests, 'radiusAccServDupRequests': radiusAccServDupRequests, 'radiusAccServResponses': radiusAccServResponses, 'radiusAccServBadAuthenticators': radiusAccServBadAuthenticators, 'radiusAccServMalformedRequests': radiusAccServMalformedRequests, 'radiusAccServNoRecords': radiusAccServNoRecords, 'radiusAccServUnknownTypes': radiusAccServUnknownTypes}


class radiusAccClientExtEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([radiusAccClientExtIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 15, 1])
	access = 2
	columns = {'radiusAccClientExtIndex': radiusAccClientExtIndex, 'radiusAccClientInetAddressType': radiusAccClientInetAddressType, 'radiusAccClientInetAddress': radiusAccClientInetAddress, 'radiusAccClientExtID': radiusAccClientExtID, 'radiusAccServExtPacketsDropped': radiusAccServExtPacketsDropped, 'radiusAccServExtRequests': radiusAccServExtRequests, 'radiusAccServExtDupRequests': radiusAccServExtDupRequests, 'radiusAccServExtResponses': radiusAccServExtResponses, 'radiusAccServExtBadAuthenticators': radiusAccServExtBadAuthenticators, 'radiusAccServExtMalformedRequests': radiusAccServExtMalformedRequests, 'radiusAccServExtNoRecords': radiusAccServExtNoRecords, 'radiusAccServExtUnknownTypes': radiusAccServExtUnknownTypes, 'radiusAccServerCounterDiscontinuity': radiusAccServerCounterDiscontinuity}


# notifications (traps) 
# groups 
class radiusAccServMIBGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2, 1])
	group = [radiusAccServIdent, radiusAccServUpTime, radiusAccServResetTime, radiusAccServConfigReset, radiusAccServTotalRequests, radiusAccServTotalInvalidRequests, radiusAccServTotalDupRequests, radiusAccServTotalResponses, radiusAccServTotalMalformedRequests, radiusAccServTotalBadAuthenticators, radiusAccServTotalPacketsDropped, radiusAccServTotalNoRecords, radiusAccServTotalUnknownTypes, radiusAccClientAddress, radiusAccClientID, radiusAccServPacketsDropped, radiusAccServRequests, radiusAccServDupRequests, radiusAccServResponses, radiusAccServBadAuthenticators, radiusAccServMalformedRequests, radiusAccServNoRecords, radiusAccServUnknownTypes]

class radiusAccServExtMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2, 2])
	group = [radiusAccServIdent, radiusAccServUpTime, radiusAccServResetTime, radiusAccServConfigReset, radiusAccServTotalRequests, radiusAccServTotalInvalidRequests, radiusAccServTotalDupRequests, radiusAccServTotalResponses, radiusAccServTotalMalformedRequests, radiusAccServTotalBadAuthenticators, radiusAccServTotalPacketsDropped, radiusAccServTotalNoRecords, radiusAccServTotalUnknownTypes, radiusAccClientInetAddressType, radiusAccClientInetAddress, radiusAccClientExtID, radiusAccServExtPacketsDropped, radiusAccServExtRequests, radiusAccServExtDupRequests, radiusAccServExtResponses, radiusAccServExtBadAuthenticators, radiusAccServExtMalformedRequests, radiusAccServExtNoRecords, radiusAccServExtUnknownTypes, radiusAccServerCounterDiscontinuity]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
