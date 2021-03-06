# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Integer32, IpAddress, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import DisplayString, RowStatus, TruthValue
from IF_MIB import InterfaceIndex, ifIndex
from ATM_TC_MIB import AtmAddr, AtmConnKind, AtmConnCastType, AtmServiceCategory, AtmTrafficDescrParamIndex, AtmVpIdentifier, AtmVcIdentifier, AtmVorXAdminStatus, AtmVorXLastChange, AtmVorXOperStatus, atmNoClpNoScr

class ATM_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/ATM-MIB'
	conformance = 4
	name = 'ATM-MIB'
	language = 2
	description = 'This is the MIB Module for ATM and AAL5-related\nobjects for managing ATM interfaces, ATM virtual\nlinks, ATM cross-connects, AAL5 entities, and\nand AAL5 connections.'

# nodes
class atmMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37])
	name = 'atmMIB'

class atmMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1])
	name = 'atmMIBObjects'

class atmMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2])
	name = 'atmMIBConformance'

class atmMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1])
	name = 'atmMIBGroups'

class atmMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 2])
	name = 'atmMIBCompliances'


# macros
# types 
# scalars 
class atmVpCrossConnectIndexNext(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmVcCrossConnectIndexNext(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmTrafficDescrParamIndexNext(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# columns
class atmInterfaceMaxVpcs(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmInterfaceMaxVccs(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmInterfaceConfVpcs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmInterfaceConfVccs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmInterfaceMaxActiveVpiBits(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmInterfaceMaxActiveVciBits(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmInterfaceIlmiVpi(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 7])
	syntaxobject = AtmVpIdentifier


class atmInterfaceIlmiVci(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 8])
	syntaxobject = AtmVcIdentifier


class atmInterfaceAddressType(ColumnObject):
	status = 2
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'private'), Enum(2, 'nsapE164'), Enum(3, 'nativeE164'), Enum(4, 'other')]


class atmInterfaceAdminAddress(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 10])
	syntaxobject = AtmAddr


class atmInterfaceMyNeighborIpAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class atmInterfaceMyNeighborIfName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class atmInterfaceCurrentMaxVpiBits(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmInterfaceCurrentMaxVciBits(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmInterfaceSubscrAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 15])
	syntaxobject = AtmAddr


class atmInterfaceDs3PlcpSEFSs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmInterfaceDs3PlcpAlarmState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noAlarm'), Enum(2, 'receivedFarEndAlarm'), Enum(3, 'incomingLOF')]


class atmInterfaceDs3PlcpUASs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmInterfaceOCDEvents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class atmInterfaceTCAlarmState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noAlarm'), Enum(2, 'lcdFailure')]


class atmTrafficDescrParamIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 1])
	syntaxobject = AtmTrafficDescrParamIndex


class atmTrafficDescrType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class atmTrafficDescrParam1(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmTrafficDescrParam2(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmTrafficDescrParam3(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmTrafficDescrParam4(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmTrafficDescrParam5(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmTrafficQoSClass(ColumnObject):
	access = 5
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmTrafficDescrRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class atmServiceCategory(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 10])
	syntaxobject = AtmServiceCategory


class atmTrafficFrameDiscard(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class atmVplVpi(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 1])
	syntaxobject = AtmVpIdentifier


class atmVplAdminStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 2])
	syntaxobject = AtmVorXAdminStatus


class atmVplOperStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 3])
	syntaxobject = AtmVorXOperStatus


class atmVplLastChange(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 4])
	syntaxobject = AtmVorXLastChange


class atmVplReceiveTrafficDescrIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 5])
	syntaxobject = AtmTrafficDescrParamIndex


class atmVplTransmitTrafficDescrIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 6])
	syntaxobject = AtmTrafficDescrParamIndex


class atmVplCrossConnectIdentifier(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmVplRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class atmVplCastType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 9])
	syntaxobject = AtmConnCastType


class atmVplConnKind(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 10])
	syntaxobject = AtmConnKind


class atmVclVpi(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 1])
	syntaxobject = AtmVpIdentifier


class atmVclVci(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 2])
	syntaxobject = AtmVcIdentifier


class atmVclAdminStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 3])
	syntaxobject = AtmVorXAdminStatus


class atmVclOperStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 4])
	syntaxobject = AtmVorXOperStatus


class atmVclLastChange(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 5])
	syntaxobject = AtmVorXLastChange


class atmVclReceiveTrafficDescrIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 6])
	syntaxobject = AtmTrafficDescrParamIndex


class atmVclTransmitTrafficDescrIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 7])
	syntaxobject = AtmTrafficDescrParamIndex


class atmVccAalType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'aal1'), Enum(2, 'aal34'), Enum(3, 'aal5'), Enum(4, 'other'), Enum(5, 'unknown'), Enum(6, 'aal2')]


class atmVccAal5CpcsTransmitSduSize(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmVccAal5CpcsReceiveSduSize(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmVccAal5EncapsType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'vcMultiplexRoutedProtocol'), Enum(2, 'vcMultiplexBridgedProtocol8023'), Enum(3, 'vcMultiplexBridgedProtocol8025'), Enum(4, 'vcMultiplexBridgedProtocol8026'), Enum(5, 'vcMultiplexLANemulation8023'), Enum(6, 'vcMultiplexLANemulation8025'), Enum(7, 'llcEncapsulation'), Enum(8, 'multiprotocolFrameRelaySscs'), Enum(9, 'other'), Enum(10, 'unknown')]


class atmVclCrossConnectIdentifier(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmVclRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class atmVclCastType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 14])
	syntaxobject = AtmConnCastType


class atmVclConnKind(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 15])
	syntaxobject = AtmConnKind


class atmVpCrossConnectIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmVpCrossConnectLowIfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 2])
	syntaxobject = InterfaceIndex


class atmVpCrossConnectLowVpi(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 3])
	syntaxobject = AtmVpIdentifier


class atmVpCrossConnectHighIfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 4])
	syntaxobject = InterfaceIndex


class atmVpCrossConnectHighVpi(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 5])
	syntaxobject = AtmVpIdentifier


class atmVpCrossConnectAdminStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 6])
	syntaxobject = AtmVorXAdminStatus


class atmVpCrossConnectL2HOperStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 7])
	syntaxobject = AtmVorXOperStatus


class atmVpCrossConnectH2LOperStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 8])
	syntaxobject = AtmVorXOperStatus


class atmVpCrossConnectL2HLastChange(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 9])
	syntaxobject = AtmVorXLastChange


class atmVpCrossConnectH2LLastChange(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 10])
	syntaxobject = AtmVorXLastChange


class atmVpCrossConnectRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class atmVcCrossConnectIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmVcCrossConnectLowIfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 2])
	syntaxobject = InterfaceIndex


class atmVcCrossConnectLowVpi(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 3])
	syntaxobject = AtmVpIdentifier


class atmVcCrossConnectLowVci(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 4])
	syntaxobject = AtmVcIdentifier


class atmVcCrossConnectHighIfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 5])
	syntaxobject = InterfaceIndex


class atmVcCrossConnectHighVpi(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 6])
	syntaxobject = AtmVpIdentifier


class atmVcCrossConnectHighVci(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 7])
	syntaxobject = AtmVcIdentifier


class atmVcCrossConnectAdminStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 8])
	syntaxobject = AtmVorXAdminStatus


class atmVcCrossConnectL2HOperStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 9])
	syntaxobject = AtmVorXOperStatus


class atmVcCrossConnectH2LOperStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 10])
	syntaxobject = AtmVorXOperStatus


class atmVcCrossConnectL2HLastChange(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 11])
	syntaxobject = AtmVorXLastChange


class atmVcCrossConnectH2LLastChange(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 12])
	syntaxobject = AtmVorXLastChange


class atmVcCrossConnectRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class aal5VccVpi(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 1])
	syntaxobject = AtmVpIdentifier


class aal5VccVci(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 2])
	syntaxobject = AtmVcIdentifier


class aal5VccCrcErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class aal5VccSarTimeOuts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class aal5VccOverSizedSDUs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
class atmInterfaceConfEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 2, 1])
	access = 2
	columns = {'atmInterfaceMaxVpcs': atmInterfaceMaxVpcs, 'atmInterfaceMaxVccs': atmInterfaceMaxVccs, 'atmInterfaceConfVpcs': atmInterfaceConfVpcs, 'atmInterfaceConfVccs': atmInterfaceConfVccs, 'atmInterfaceMaxActiveVpiBits': atmInterfaceMaxActiveVpiBits, 'atmInterfaceMaxActiveVciBits': atmInterfaceMaxActiveVciBits, 'atmInterfaceIlmiVpi': atmInterfaceIlmiVpi, 'atmInterfaceIlmiVci': atmInterfaceIlmiVci, 'atmInterfaceAddressType': atmInterfaceAddressType, 'atmInterfaceAdminAddress': atmInterfaceAdminAddress, 'atmInterfaceMyNeighborIpAddress': atmInterfaceMyNeighborIpAddress, 'atmInterfaceMyNeighborIfName': atmInterfaceMyNeighborIfName, 'atmInterfaceCurrentMaxVpiBits': atmInterfaceCurrentMaxVpiBits, 'atmInterfaceCurrentMaxVciBits': atmInterfaceCurrentMaxVciBits, 'atmInterfaceSubscrAddress': atmInterfaceSubscrAddress}


class atmInterfaceDs3PlcpEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 3, 1])
	access = 2
	columns = {'atmInterfaceDs3PlcpSEFSs': atmInterfaceDs3PlcpSEFSs, 'atmInterfaceDs3PlcpAlarmState': atmInterfaceDs3PlcpAlarmState, 'atmInterfaceDs3PlcpUASs': atmInterfaceDs3PlcpUASs}


class atmInterfaceTCEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 4, 1])
	access = 2
	columns = {'atmInterfaceOCDEvents': atmInterfaceOCDEvents, 'atmInterfaceTCAlarmState': atmInterfaceTCAlarmState}


class atmTrafficDescrParamEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([atmTrafficDescrParamIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 5, 1])
	access = 2
	rowstatus = atmTrafficDescrRowStatus
	columns = {'atmTrafficDescrParamIndex': atmTrafficDescrParamIndex, 'atmTrafficDescrType': atmTrafficDescrType, 'atmTrafficDescrParam1': atmTrafficDescrParam1, 'atmTrafficDescrParam2': atmTrafficDescrParam2, 'atmTrafficDescrParam3': atmTrafficDescrParam3, 'atmTrafficDescrParam4': atmTrafficDescrParam4, 'atmTrafficDescrParam5': atmTrafficDescrParam5, 'atmTrafficQoSClass': atmTrafficQoSClass, 'atmTrafficDescrRowStatus': atmTrafficDescrRowStatus, 'atmServiceCategory': atmServiceCategory, 'atmTrafficFrameDiscard': atmTrafficFrameDiscard}


class atmVplEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, atmVplVpi], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 6, 1])
	access = 2
	rowstatus = atmVplRowStatus
	columns = {'atmVplVpi': atmVplVpi, 'atmVplAdminStatus': atmVplAdminStatus, 'atmVplOperStatus': atmVplOperStatus, 'atmVplLastChange': atmVplLastChange, 'atmVplReceiveTrafficDescrIndex': atmVplReceiveTrafficDescrIndex, 'atmVplTransmitTrafficDescrIndex': atmVplTransmitTrafficDescrIndex, 'atmVplCrossConnectIdentifier': atmVplCrossConnectIdentifier, 'atmVplRowStatus': atmVplRowStatus, 'atmVplCastType': atmVplCastType, 'atmVplConnKind': atmVplConnKind}


class atmVclEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, atmVclVpi, atmVclVci], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 7, 1])
	access = 2
	rowstatus = atmVclRowStatus
	columns = {'atmVclVpi': atmVclVpi, 'atmVclVci': atmVclVci, 'atmVclAdminStatus': atmVclAdminStatus, 'atmVclOperStatus': atmVclOperStatus, 'atmVclLastChange': atmVclLastChange, 'atmVclReceiveTrafficDescrIndex': atmVclReceiveTrafficDescrIndex, 'atmVclTransmitTrafficDescrIndex': atmVclTransmitTrafficDescrIndex, 'atmVccAalType': atmVccAalType, 'atmVccAal5CpcsTransmitSduSize': atmVccAal5CpcsTransmitSduSize, 'atmVccAal5CpcsReceiveSduSize': atmVccAal5CpcsReceiveSduSize, 'atmVccAal5EncapsType': atmVccAal5EncapsType, 'atmVclCrossConnectIdentifier': atmVclCrossConnectIdentifier, 'atmVclRowStatus': atmVclRowStatus, 'atmVclCastType': atmVclCastType, 'atmVclConnKind': atmVclConnKind}


class atmVpCrossConnectEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([atmVpCrossConnectIndex, atmVpCrossConnectLowIfIndex, atmVpCrossConnectLowVpi, atmVpCrossConnectHighIfIndex, atmVpCrossConnectHighVpi], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 9, 1])
	access = 2
	rowstatus = atmVpCrossConnectRowStatus
	columns = {'atmVpCrossConnectIndex': atmVpCrossConnectIndex, 'atmVpCrossConnectLowIfIndex': atmVpCrossConnectLowIfIndex, 'atmVpCrossConnectLowVpi': atmVpCrossConnectLowVpi, 'atmVpCrossConnectHighIfIndex': atmVpCrossConnectHighIfIndex, 'atmVpCrossConnectHighVpi': atmVpCrossConnectHighVpi, 'atmVpCrossConnectAdminStatus': atmVpCrossConnectAdminStatus, 'atmVpCrossConnectL2HOperStatus': atmVpCrossConnectL2HOperStatus, 'atmVpCrossConnectH2LOperStatus': atmVpCrossConnectH2LOperStatus, 'atmVpCrossConnectL2HLastChange': atmVpCrossConnectL2HLastChange, 'atmVpCrossConnectH2LLastChange': atmVpCrossConnectH2LLastChange, 'atmVpCrossConnectRowStatus': atmVpCrossConnectRowStatus}


class atmVcCrossConnectEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([atmVcCrossConnectIndex, atmVcCrossConnectLowIfIndex, atmVcCrossConnectLowVpi, atmVcCrossConnectLowVci, atmVcCrossConnectHighIfIndex, atmVcCrossConnectHighVpi, atmVcCrossConnectHighVci], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 11, 1])
	access = 2
	rowstatus = atmVcCrossConnectRowStatus
	columns = {'atmVcCrossConnectIndex': atmVcCrossConnectIndex, 'atmVcCrossConnectLowIfIndex': atmVcCrossConnectLowIfIndex, 'atmVcCrossConnectLowVpi': atmVcCrossConnectLowVpi, 'atmVcCrossConnectLowVci': atmVcCrossConnectLowVci, 'atmVcCrossConnectHighIfIndex': atmVcCrossConnectHighIfIndex, 'atmVcCrossConnectHighVpi': atmVcCrossConnectHighVpi, 'atmVcCrossConnectHighVci': atmVcCrossConnectHighVci, 'atmVcCrossConnectAdminStatus': atmVcCrossConnectAdminStatus, 'atmVcCrossConnectL2HOperStatus': atmVcCrossConnectL2HOperStatus, 'atmVcCrossConnectH2LOperStatus': atmVcCrossConnectH2LOperStatus, 'atmVcCrossConnectL2HLastChange': atmVcCrossConnectL2HLastChange, 'atmVcCrossConnectH2LLastChange': atmVcCrossConnectH2LLastChange, 'atmVcCrossConnectRowStatus': atmVcCrossConnectRowStatus}


class aal5VccEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, aal5VccVpi, aal5VccVci], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 1, 12, 1])
	access = 2
	columns = {'aal5VccVpi': aal5VccVpi, 'aal5VccVci': aal5VccVci, 'aal5VccCrcErrors': aal5VccCrcErrors, 'aal5VccSarTimeOuts': aal5VccSarTimeOuts, 'aal5VccOverSizedSDUs': aal5VccOverSizedSDUs}


# notifications (traps) 
# groups 
class atmInterfaceConfGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 1])
	group = [atmInterfaceMaxVpcs, atmInterfaceMaxVccs, atmInterfaceConfVpcs, atmInterfaceConfVccs, atmInterfaceMaxActiveVpiBits, atmInterfaceMaxActiveVciBits, atmInterfaceIlmiVpi, atmInterfaceIlmiVci, atmInterfaceAddressType, atmInterfaceAdminAddress, atmInterfaceMyNeighborIpAddress, atmInterfaceMyNeighborIfName]

class atmTrafficDescrGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 2])
	group = [atmTrafficDescrType, atmTrafficDescrParam1, atmTrafficDescrParam2, atmTrafficDescrParam3, atmTrafficDescrParam4, atmTrafficDescrParam5, atmTrafficQoSClass, atmTrafficDescrRowStatus]

class atmInterfaceDs3PlcpGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 3])
	group = [atmInterfaceDs3PlcpSEFSs, atmInterfaceDs3PlcpAlarmState, atmInterfaceDs3PlcpUASs]

class atmInterfaceTCGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 4])
	group = [atmInterfaceOCDEvents, atmInterfaceTCAlarmState]

class atmVpcTerminationGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 5])
	group = [atmVplOperStatus, atmVplAdminStatus, atmVplLastChange, atmVplReceiveTrafficDescrIndex, atmVplTransmitTrafficDescrIndex, atmVplRowStatus]

class atmVccTerminationGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 6])
	group = [atmVclOperStatus, atmVclAdminStatus, atmVclLastChange, atmVclReceiveTrafficDescrIndex, atmVclTransmitTrafficDescrIndex, atmVccAalType, atmVclRowStatus]

class atmVpCrossConnectGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 7])
	group = [atmVplReceiveTrafficDescrIndex, atmVplTransmitTrafficDescrIndex, atmVplOperStatus, atmVplRowStatus, atmVpCrossConnectAdminStatus, atmVpCrossConnectL2HOperStatus, atmVpCrossConnectH2LOperStatus, atmVpCrossConnectL2HLastChange, atmVpCrossConnectH2LLastChange, atmVpCrossConnectRowStatus, atmVplCrossConnectIdentifier, atmVpCrossConnectIndexNext]

class atmVcCrossConnectGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 8])
	group = [atmVclReceiveTrafficDescrIndex, atmVclTransmitTrafficDescrIndex, atmVclOperStatus, atmVclRowStatus, atmVcCrossConnectAdminStatus, atmVcCrossConnectL2HOperStatus, atmVcCrossConnectH2LOperStatus, atmVcCrossConnectL2HLastChange, atmVcCrossConnectH2LLastChange, atmVcCrossConnectRowStatus, atmVclCrossConnectIdentifier, atmVcCrossConnectIndexNext]

class aal5VccGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 9])
	group = [atmVccAal5CpcsTransmitSduSize, atmVccAal5CpcsReceiveSduSize, atmVccAal5EncapsType, aal5VccCrcErrors, aal5VccSarTimeOuts, aal5VccOverSizedSDUs]

class atmInterfaceConfGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 10])
	group = [atmInterfaceMaxVpcs, atmInterfaceMaxVccs, atmInterfaceConfVpcs, atmInterfaceConfVccs, atmInterfaceMaxActiveVpiBits, atmInterfaceMaxActiveVciBits, atmInterfaceIlmiVpi, atmInterfaceIlmiVci, atmInterfaceMyNeighborIpAddress, atmInterfaceMyNeighborIfName, atmInterfaceCurrentMaxVpiBits, atmInterfaceCurrentMaxVciBits, atmInterfaceSubscrAddress]

class atmTrafficDescrGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 11])
	group = [atmTrafficDescrType, atmTrafficDescrParam1, atmTrafficDescrParam2, atmTrafficDescrParam3, atmTrafficDescrParam4, atmTrafficDescrParam5, atmTrafficDescrRowStatus, atmServiceCategory, atmTrafficFrameDiscard, atmTrafficDescrParamIndexNext]

class atmVpcTerminationGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 12])
	group = [atmVplOperStatus, atmVplAdminStatus, atmVplLastChange, atmVplReceiveTrafficDescrIndex, atmVplTransmitTrafficDescrIndex, atmVplRowStatus, atmVplCastType, atmVplConnKind]

class atmVccTerminationGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 13])
	group = [atmVclOperStatus, atmVclAdminStatus, atmVclLastChange, atmVclReceiveTrafficDescrIndex, atmVclTransmitTrafficDescrIndex, atmVccAalType, atmVclRowStatus, atmVclCastType, atmVclConnKind]

class atmVplCrossConnectGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 14])
	group = [atmVplReceiveTrafficDescrIndex, atmVplTransmitTrafficDescrIndex, atmVplOperStatus, atmVplLastChange, atmVplRowStatus, atmVplCastType, atmVplConnKind]

class atmVpPvcCrossConnectGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 15])
	group = [atmVpCrossConnectAdminStatus, atmVpCrossConnectL2HOperStatus, atmVpCrossConnectH2LOperStatus, atmVpCrossConnectL2HLastChange, atmVpCrossConnectH2LLastChange, atmVpCrossConnectRowStatus, atmVplCrossConnectIdentifier, atmVpCrossConnectIndexNext]

class atmVclCrossConnectGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 16])
	group = [atmVclReceiveTrafficDescrIndex, atmVclTransmitTrafficDescrIndex, atmVclOperStatus, atmVclLastChange, atmVclRowStatus, atmVclCastType, atmVclConnKind]

class atmVcPvcCrossConnectGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 37, 2, 1, 17])
	group = [atmVcCrossConnectAdminStatus, atmVcCrossConnectL2HOperStatus, atmVcCrossConnectH2LOperStatus, atmVcCrossConnectL2HLastChange, atmVcCrossConnectH2LLastChange, atmVcCrossConnectRowStatus, atmVclCrossConnectIdentifier, atmVcCrossConnectIndexNext]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
