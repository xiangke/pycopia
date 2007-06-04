# python
# This file is generated by a program (mib2py). 

import MAU_MIB

OIDMAP = {
'1.3.6.1.2.1.26': MAU_MIB.snmpDot3MauMgt,
'1.3.6.1.2.1.26.0': MAU_MIB.snmpDot3MauTraps,
'1.3.6.1.2.1.26.1': MAU_MIB.dot3RpMauBasicGroup,
'1.3.6.1.2.1.26.2': MAU_MIB.dot3IfMauBasicGroup,
'1.3.6.1.2.1.26.3': MAU_MIB.dot3BroadMauBasicGroup,
'1.3.6.1.2.1.26.4': MAU_MIB.dot3MauType,
'1.3.6.1.2.1.26.4.1': MAU_MIB.dot3MauTypeAUI,
'1.3.6.1.2.1.26.4.2': MAU_MIB.dot3MauType10Base5,
'1.3.6.1.2.1.26.4.3': MAU_MIB.dot3MauTypeFoirl,
'1.3.6.1.2.1.26.4.4': MAU_MIB.dot3MauType10Base2,
'1.3.6.1.2.1.26.4.5': MAU_MIB.dot3MauType10BaseT,
'1.3.6.1.2.1.26.4.6': MAU_MIB.dot3MauType10BaseFP,
'1.3.6.1.2.1.26.4.7': MAU_MIB.dot3MauType10BaseFB,
'1.3.6.1.2.1.26.4.8': MAU_MIB.dot3MauType10BaseFL,
'1.3.6.1.2.1.26.4.9': MAU_MIB.dot3MauType10Broad36,
'1.3.6.1.2.1.26.4.10': MAU_MIB.dot3MauType10BaseTHD,
'1.3.6.1.2.1.26.4.11': MAU_MIB.dot3MauType10BaseTFD,
'1.3.6.1.2.1.26.4.12': MAU_MIB.dot3MauType10BaseFLHD,
'1.3.6.1.2.1.26.4.13': MAU_MIB.dot3MauType10BaseFLFD,
'1.3.6.1.2.1.26.4.14': MAU_MIB.dot3MauType100BaseT4,
'1.3.6.1.2.1.26.4.15': MAU_MIB.dot3MauType100BaseTXHD,
'1.3.6.1.2.1.26.4.16': MAU_MIB.dot3MauType100BaseTXFD,
'1.3.6.1.2.1.26.4.17': MAU_MIB.dot3MauType100BaseFXHD,
'1.3.6.1.2.1.26.4.18': MAU_MIB.dot3MauType100BaseFXFD,
'1.3.6.1.2.1.26.4.19': MAU_MIB.dot3MauType100BaseT2HD,
'1.3.6.1.2.1.26.4.20': MAU_MIB.dot3MauType100BaseT2FD,
'1.3.6.1.2.1.26.4.21': MAU_MIB.dot3MauType1000BaseXHD,
'1.3.6.1.2.1.26.4.22': MAU_MIB.dot3MauType1000BaseXFD,
'1.3.6.1.2.1.26.4.23': MAU_MIB.dot3MauType1000BaseLXHD,
'1.3.6.1.2.1.26.4.24': MAU_MIB.dot3MauType1000BaseLXFD,
'1.3.6.1.2.1.26.4.25': MAU_MIB.dot3MauType1000BaseSXHD,
'1.3.6.1.2.1.26.4.26': MAU_MIB.dot3MauType1000BaseSXFD,
'1.3.6.1.2.1.26.4.27': MAU_MIB.dot3MauType1000BaseCXHD,
'1.3.6.1.2.1.26.4.28': MAU_MIB.dot3MauType1000BaseCXFD,
'1.3.6.1.2.1.26.4.29': MAU_MIB.dot3MauType1000BaseTHD,
'1.3.6.1.2.1.26.4.30': MAU_MIB.dot3MauType1000BaseTFD,
'1.3.6.1.2.1.26.4.31': MAU_MIB.dot3MauType10GigBaseX,
'1.3.6.1.2.1.26.4.32': MAU_MIB.dot3MauType10GigBaseLX4,
'1.3.6.1.2.1.26.4.33': MAU_MIB.dot3MauType10GigBaseR,
'1.3.6.1.2.1.26.4.34': MAU_MIB.dot3MauType10GigBaseER,
'1.3.6.1.2.1.26.4.35': MAU_MIB.dot3MauType10GigBaseLR,
'1.3.6.1.2.1.26.4.36': MAU_MIB.dot3MauType10GigBaseSR,
'1.3.6.1.2.1.26.4.37': MAU_MIB.dot3MauType10GigBaseW,
'1.3.6.1.2.1.26.4.38': MAU_MIB.dot3MauType10GigBaseEW,
'1.3.6.1.2.1.26.4.39': MAU_MIB.dot3MauType10GigBaseLW,
'1.3.6.1.2.1.26.4.40': MAU_MIB.dot3MauType10GigBaseSW,
'1.3.6.1.2.1.26.5': MAU_MIB.dot3IfMauAutoNegGroup,
'1.3.6.1.2.1.26.6': MAU_MIB.mauMod,
'1.3.6.1.2.1.26.6.1': MAU_MIB.mauModConf,
'1.3.6.1.2.1.26.6.1.1': MAU_MIB.mauModCompls,
'1.3.6.1.2.1.26.6.1.2': MAU_MIB.mauModObjGrps,
'1.3.6.1.2.1.26.6.1.3': MAU_MIB.mauModNotGrps,
'1.3.6.1.2.1.26.1.1.1.1': MAU_MIB.rpMauGroupIndex,
'1.3.6.1.2.1.26.1.1.1.2': MAU_MIB.rpMauPortIndex,
'1.3.6.1.2.1.26.1.1.1.3': MAU_MIB.rpMauIndex,
'1.3.6.1.2.1.26.1.1.1.4': MAU_MIB.rpMauType,
'1.3.6.1.2.1.26.1.1.1.5': MAU_MIB.rpMauStatus,
'1.3.6.1.2.1.26.1.1.1.6': MAU_MIB.rpMauMediaAvailable,
'1.3.6.1.2.1.26.1.1.1.7': MAU_MIB.rpMauMediaAvailableStateExits,
'1.3.6.1.2.1.26.1.1.1.8': MAU_MIB.rpMauJabberState,
'1.3.6.1.2.1.26.1.1.1.9': MAU_MIB.rpMauJabberingStateEnters,
'1.3.6.1.2.1.26.1.1.1.10': MAU_MIB.rpMauFalseCarriers,
'1.3.6.1.2.1.26.1.2.1.1': MAU_MIB.rpJackIndex,
'1.3.6.1.2.1.26.1.2.1.2': MAU_MIB.rpJackType,
'1.3.6.1.2.1.26.2.1.1.1': MAU_MIB.ifMauIfIndex,
'1.3.6.1.2.1.26.2.1.1.2': MAU_MIB.ifMauIndex,
'1.3.6.1.2.1.26.2.1.1.3': MAU_MIB.ifMauType,
'1.3.6.1.2.1.26.2.1.1.4': MAU_MIB.ifMauStatus,
'1.3.6.1.2.1.26.2.1.1.5': MAU_MIB.ifMauMediaAvailable,
'1.3.6.1.2.1.26.2.1.1.6': MAU_MIB.ifMauMediaAvailableStateExits,
'1.3.6.1.2.1.26.2.1.1.7': MAU_MIB.ifMauJabberState,
'1.3.6.1.2.1.26.2.1.1.8': MAU_MIB.ifMauJabberingStateEnters,
'1.3.6.1.2.1.26.2.1.1.9': MAU_MIB.ifMauFalseCarriers,
'1.3.6.1.2.1.26.2.1.1.10': MAU_MIB.ifMauTypeList,
'1.3.6.1.2.1.26.2.1.1.11': MAU_MIB.ifMauDefaultType,
'1.3.6.1.2.1.26.2.1.1.12': MAU_MIB.ifMauAutoNegSupported,
'1.3.6.1.2.1.26.2.1.1.13': MAU_MIB.ifMauTypeListBits,
'1.3.6.1.2.1.26.2.1.1.14': MAU_MIB.ifMauHCFalseCarriers,
'1.3.6.1.2.1.26.2.2.1.1': MAU_MIB.ifJackIndex,
'1.3.6.1.2.1.26.2.2.1.2': MAU_MIB.ifJackType,
'1.3.6.1.2.1.26.3.1.1.1': MAU_MIB.broadMauIfIndex,
'1.3.6.1.2.1.26.3.1.1.2': MAU_MIB.broadMauIndex,
'1.3.6.1.2.1.26.3.1.1.3': MAU_MIB.broadMauXmtRcvSplitType,
'1.3.6.1.2.1.26.3.1.1.4': MAU_MIB.broadMauXmtCarrierFreq,
'1.3.6.1.2.1.26.3.1.1.5': MAU_MIB.broadMauTranslationFreq,
'1.3.6.1.2.1.26.5.1.1.1': MAU_MIB.ifMauAutoNegAdminStatus,
'1.3.6.1.2.1.26.5.1.1.2': MAU_MIB.ifMauAutoNegRemoteSignaling,
'1.3.6.1.2.1.26.5.1.1.4': MAU_MIB.ifMauAutoNegConfig,
'1.3.6.1.2.1.26.5.1.1.5': MAU_MIB.ifMauAutoNegCapability,
'1.3.6.1.2.1.26.5.1.1.6': MAU_MIB.ifMauAutoNegCapAdvertised,
'1.3.6.1.2.1.26.5.1.1.7': MAU_MIB.ifMauAutoNegCapReceived,
'1.3.6.1.2.1.26.5.1.1.8': MAU_MIB.ifMauAutoNegRestart,
'1.3.6.1.2.1.26.5.1.1.9': MAU_MIB.ifMauAutoNegCapabilityBits,
'1.3.6.1.2.1.26.5.1.1.10': MAU_MIB.ifMauAutoNegCapAdvertisedBits,
'1.3.6.1.2.1.26.5.1.1.11': MAU_MIB.ifMauAutoNegCapReceivedBits,
'1.3.6.1.2.1.26.5.1.1.12': MAU_MIB.ifMauAutoNegRemoteFaultAdvertised,
'1.3.6.1.2.1.26.5.1.1.13': MAU_MIB.ifMauAutoNegRemoteFaultReceived,
'1.3.6.1.2.1.26.0.1': MAU_MIB.rpMauJabberTrap,
'1.3.6.1.2.1.26.0.2': MAU_MIB.ifMauJabberTrap,
'1.3.6.1.2.1.26.6.1.2.1': MAU_MIB.mauRpGrpBasic,
'1.3.6.1.2.1.26.6.1.2.2': MAU_MIB.mauRpGrp100Mbs,
'1.3.6.1.2.1.26.6.1.2.3': MAU_MIB.mauRpGrpJack,
'1.3.6.1.2.1.26.6.1.2.4': MAU_MIB.mauIfGrpBasic,
'1.3.6.1.2.1.26.6.1.2.5': MAU_MIB.mauIfGrp100Mbs,
'1.3.6.1.2.1.26.6.1.2.6': MAU_MIB.mauIfGrpJack,
'1.3.6.1.2.1.26.6.1.2.7': MAU_MIB.mauIfGrpAutoNeg,
'1.3.6.1.2.1.26.6.1.2.8': MAU_MIB.mauBroadBasic,
'1.3.6.1.2.1.26.6.1.2.9': MAU_MIB.mauIfGrpHighCapacity,
'1.3.6.1.2.1.26.6.1.2.10': MAU_MIB.mauIfGrpAutoNeg2,
'1.3.6.1.2.1.26.6.1.2.11': MAU_MIB.mauIfGrpAutoNeg1000Mbps,
'1.3.6.1.2.1.26.6.1.2.12': MAU_MIB.mauIfGrpHCStats,
'1.3.6.1.2.1.26.6.1.3.1': MAU_MIB.rpMauNotifications,
'1.3.6.1.2.1.26.6.1.3.2': MAU_MIB.ifMauNotifications,
}
