# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, OBJECT_IDENTITY, mib_2, Integer32, Counter64
from SNMPv2_TC import DisplayString, DateAndTime
from ATM_TC_MIB import AtmAddr

class ATM_ACCOUNTING_INFORMATION_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/ATM-ACCOUNTING-INFORMATION-MIB'
	conformance = 3
	name = 'ATM-ACCOUNTING-INFORMATION-MIB'
	language = 2
	description = 'The MIB module for identifying items of accounting\ninformation which are applicable to ATM connections.'

# nodes
class atmAccountingInformationMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59])
	name = 'atmAccountingInformationMIB'

class atmAcctngMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1])
	name = 'atmAcctngMIBObjects'

class atmAcctngDataObjects(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1])
	name = 'atmAcctngDataObjects'


# macros
# types 
# scalars 
class atmAcctngConnectionType(ScalarObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'pvc'), Enum(2, 'pvp'), Enum(3, 'svcIncoming'), Enum(4, 'svcOutgoing'), Enum(5, 'svpIncoming'), Enum(6, 'svpOutgoing'), Enum(7, 'spvcInitiator'), Enum(8, 'spvcTarget'), Enum(9, 'spvpInitiator'), Enum(10, 'spvpTarget')]


class atmAcctngCastType(ScalarObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'p2p'), Enum(2, 'p2mp')]


class atmAcctngIfName(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class atmAcctngIfAlias(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class atmAcctngVpi(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngVci(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngCallingParty(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 7])
	syntaxobject = AtmAddr


class atmAcctngCalledParty(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 8])
	syntaxobject = AtmAddr


class atmAcctngCallReference(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class atmAcctngStartTime(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class atmAcctngCollectionTime(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class atmAcctngCollectMode(ScalarObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'onRelease'), Enum(2, 'periodically'), Enum(3, 'onCommand')]


class atmAcctngReleaseCause(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngServiceCategory(ScalarObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'other'), Enum(2, 'cbr'), Enum(3, 'vbrRt'), Enum(4, 'vbrNrt'), Enum(5, 'abr'), Enum(6, 'ubr'), Enum(7, 'unknown')]


class atmAcctngTransmittedCells(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class atmAcctngTransmittedClp0Cells(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class atmAcctngReceivedCells(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class atmAcctngReceivedClp0Cells(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class atmAcctngTransmitTrafficDescriptorType(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class atmAcctngTransmitTrafficDescriptorParam1(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngTransmitTrafficDescriptorParam2(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngTransmitTrafficDescriptorParam3(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngTransmitTrafficDescriptorParam4(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 23])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngTransmitTrafficDescriptorParam5(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 24])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngReceiveTrafficDescriptorType(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 25])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class atmAcctngReceiveTrafficDescriptorParam1(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 26])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngReceiveTrafficDescriptorParam2(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 27])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngReceiveTrafficDescriptorParam3(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 28])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngReceiveTrafficDescriptorParam4(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 29])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngReceiveTrafficDescriptorParam5(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 30])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class atmAcctngCallingPartySubAddress(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 31])
	syntaxobject = AtmAddr


class atmAcctngCalledPartySubAddress(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 32])
	syntaxobject = AtmAddr


class atmAcctngRecordCrc16(ScalarObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 59, 1, 1, 33])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


# columns
# rows 
# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
