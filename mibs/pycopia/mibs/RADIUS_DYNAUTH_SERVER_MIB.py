# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Integer32, mib_2, TimeTicks
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from INET_ADDRESS_MIB import InetAddressType, InetAddress
from SNMP_FRAMEWORK_MIB import SnmpAdminString

class RADIUS_DYNAUTH_SERVER_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/RADIUS-DYNAUTH-SERVER-MIB'
	conformance = 132
	name = 'RADIUS-DYNAUTH-SERVER-MIB'
	language = 2
	description = 'The MIB module for entities implementing the server\nside of the Dynamic Authorization Extensions to the\nRemote Authentication Dial-In User Service (RADIUS)\nprotocol.  Copyright (C) The Internet Society (2006).\n\n\n\nInitial version as published in RFC 4673; for full\nlegal notices see the RFC itself.'

# nodes
class radiusDynAuthServerMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146])
	name = 'radiusDynAuthServerMIB'

class radiusDynAuthServerMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1])
	name = 'radiusDynAuthServerMIBObjects'

class radiusDynAuthServerScalars(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 1])
	name = 'radiusDynAuthServerScalars'

class radiusDynAuthServerMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 2])
	name = 'radiusDynAuthServerMIBConformance'

class radiusDynAuthServerMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 2, 1])
	name = 'radiusDynAuthServerMIBCompliances'

class radiusDynAuthServerMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 2, 2])
	name = 'radiusDynAuthServerMIBGroups'


# macros
# types 
# scalars 
class radiusDynAuthServerDisconInvalidClientAddresses(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class radiusDynAuthServerCoAInvalidClientAddresses(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class radiusDynAuthServerIdentifier(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 1, 3])
	syntaxobject = SnmpAdminString


# columns
class radiusDynAuthClientIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class radiusDynAuthClientAddressType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 2])
	syntaxobject = InetAddressType


class radiusDynAuthClientAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 3])
	syntaxobject = InetAddress


class radiusDynAuthServDisconRequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServDisconAuthOnlyRequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServDupDisconRequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServDisconAcks(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'replies'


class radiusDynAuthServDisconNaks(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'replies'


class radiusDynAuthServDisconNakAuthOnlyRequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'replies'


class radiusDynAuthServDisconNakSessNoContext(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'replies'


class radiusDynAuthServDisconUserSessRemoved(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'sessions'


class radiusDynAuthServMalformedDisconRequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServDisconBadAuthenticators(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServDisconPacketsDropped(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServCoARequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServCoAAuthOnlyRequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServDupCoARequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServCoAAcks(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'replies'


class radiusDynAuthServCoANaks(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'replies'


class radiusDynAuthServCoANakAuthOnlyRequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'replies'


class radiusDynAuthServCoANakSessNoContext(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'replies'


class radiusDynAuthServCoAUserSessChanged(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'sessions'


class radiusDynAuthServMalformedCoARequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 23])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServCoABadAuthenticators(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 24])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServCoAPacketsDropped(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 25])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServUnknownTypes(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 26])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'requests'


class radiusDynAuthServerCounterDiscontinuity(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 27])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks
	access = 4
	units = 'hundredths of a second'


# rows 
class radiusDynAuthClientEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([radiusDynAuthClientIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 1, 2, 1])
	access = 2
	columns = {'radiusDynAuthClientIndex': radiusDynAuthClientIndex, 'radiusDynAuthClientAddressType': radiusDynAuthClientAddressType, 'radiusDynAuthClientAddress': radiusDynAuthClientAddress, 'radiusDynAuthServDisconRequests': radiusDynAuthServDisconRequests, 'radiusDynAuthServDisconAuthOnlyRequests': radiusDynAuthServDisconAuthOnlyRequests, 'radiusDynAuthServDupDisconRequests': radiusDynAuthServDupDisconRequests, 'radiusDynAuthServDisconAcks': radiusDynAuthServDisconAcks, 'radiusDynAuthServDisconNaks': radiusDynAuthServDisconNaks, 'radiusDynAuthServDisconNakAuthOnlyRequests': radiusDynAuthServDisconNakAuthOnlyRequests, 'radiusDynAuthServDisconNakSessNoContext': radiusDynAuthServDisconNakSessNoContext, 'radiusDynAuthServDisconUserSessRemoved': radiusDynAuthServDisconUserSessRemoved, 'radiusDynAuthServMalformedDisconRequests': radiusDynAuthServMalformedDisconRequests, 'radiusDynAuthServDisconBadAuthenticators': radiusDynAuthServDisconBadAuthenticators, 'radiusDynAuthServDisconPacketsDropped': radiusDynAuthServDisconPacketsDropped, 'radiusDynAuthServCoARequests': radiusDynAuthServCoARequests, 'radiusDynAuthServCoAAuthOnlyRequests': radiusDynAuthServCoAAuthOnlyRequests, 'radiusDynAuthServDupCoARequests': radiusDynAuthServDupCoARequests, 'radiusDynAuthServCoAAcks': radiusDynAuthServCoAAcks, 'radiusDynAuthServCoANaks': radiusDynAuthServCoANaks, 'radiusDynAuthServCoANakAuthOnlyRequests': radiusDynAuthServCoANakAuthOnlyRequests, 'radiusDynAuthServCoANakSessNoContext': radiusDynAuthServCoANakSessNoContext, 'radiusDynAuthServCoAUserSessChanged': radiusDynAuthServCoAUserSessChanged, 'radiusDynAuthServMalformedCoARequests': radiusDynAuthServMalformedCoARequests, 'radiusDynAuthServCoABadAuthenticators': radiusDynAuthServCoABadAuthenticators, 'radiusDynAuthServCoAPacketsDropped': radiusDynAuthServCoAPacketsDropped, 'radiusDynAuthServUnknownTypes': radiusDynAuthServUnknownTypes, 'radiusDynAuthServerCounterDiscontinuity': radiusDynAuthServerCounterDiscontinuity}


# notifications (traps) 
# groups 
class radiusDynAuthServerMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 2, 2, 1])
	group = [radiusDynAuthServerDisconInvalidClientAddresses, radiusDynAuthServerCoAInvalidClientAddresses, radiusDynAuthServerIdentifier, radiusDynAuthClientAddressType, radiusDynAuthClientAddress, radiusDynAuthServDisconRequests, radiusDynAuthServDupDisconRequests, radiusDynAuthServDisconAcks, radiusDynAuthServDisconNaks, radiusDynAuthServDisconUserSessRemoved, radiusDynAuthServMalformedDisconRequests, radiusDynAuthServDisconBadAuthenticators, radiusDynAuthServDisconPacketsDropped, radiusDynAuthServCoARequests, radiusDynAuthServDupCoARequests, radiusDynAuthServCoAAcks, radiusDynAuthServCoANaks, radiusDynAuthServCoAUserSessChanged, radiusDynAuthServMalformedCoARequests, radiusDynAuthServCoABadAuthenticators, radiusDynAuthServCoAPacketsDropped, radiusDynAuthServUnknownTypes, radiusDynAuthServerCounterDiscontinuity]

class radiusDynAuthServerAuthOnlyGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 2, 2, 2])
	group = [radiusDynAuthServDisconAuthOnlyRequests, radiusDynAuthServDisconNakAuthOnlyRequests, radiusDynAuthServCoAAuthOnlyRequests, radiusDynAuthServCoANakAuthOnlyRequests]

class radiusDynAuthServerNoSessGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 146, 2, 2, 3])
	group = [radiusDynAuthServDisconNakSessNoContext, radiusDynAuthServCoANakSessNoContext]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
