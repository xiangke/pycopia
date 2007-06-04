# python
# This file is generated by a program (mib2py). 

import FR_ATM_PVC_SERVICE_IWF_MIB

OIDMAP = {
'1.3.6.1.2.1.86': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfMIB,
'1.3.6.1.2.1.86.1': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfMIBObjects,
'1.3.6.1.2.1.86.2': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfTraps,
'1.3.6.1.2.1.86.2.0': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfTrapsPrefix,
'1.3.6.1.2.1.86.3': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConformance,
'1.3.6.1.2.1.86.3.1': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfGroups,
'1.3.6.1.2.1.86.3.2': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfCompliances,
'1.3.6.1.2.1.86.1.1': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnIndexNext,
'1.3.6.1.2.1.86.1.3': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnectionDescriptorIndexNext,
'1.3.6.1.2.1.86.1.2.1.1': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnIndex,
'1.3.6.1.2.1.86.1.2.1.2': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnAtmPort,
'1.3.6.1.2.1.86.1.2.1.3': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnVpi,
'1.3.6.1.2.1.86.1.2.1.4': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnVci,
'1.3.6.1.2.1.86.1.2.1.5': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnFrPort,
'1.3.6.1.2.1.86.1.2.1.6': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnDlci,
'1.3.6.1.2.1.86.1.2.1.7': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnRowStatus,
'1.3.6.1.2.1.86.1.2.1.8': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnAdminStatus,
'1.3.6.1.2.1.86.1.2.1.9': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnAtm2FrOperStatus,
'1.3.6.1.2.1.86.1.2.1.10': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnAtm2FrLastChange,
'1.3.6.1.2.1.86.1.2.1.11': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnFr2AtmOperStatus,
'1.3.6.1.2.1.86.1.2.1.12': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnFr2AtmLastChange,
'1.3.6.1.2.1.86.1.2.1.13': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnectionDescriptor,
'1.3.6.1.2.1.86.1.2.1.14': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnFailedFrameTranslate,
'1.3.6.1.2.1.86.1.2.1.15': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnOverSizedFrames,
'1.3.6.1.2.1.86.1.2.1.16': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnFailedAal5PduTranslate,
'1.3.6.1.2.1.86.1.2.1.17': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnOverSizedSDUs,
'1.3.6.1.2.1.86.1.2.1.18': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnCrcErrors,
'1.3.6.1.2.1.86.1.2.1.19': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnSarTimeOuts,
'1.3.6.1.2.1.86.1.4.1.1': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnectionDescriptorIndex,
'1.3.6.1.2.1.86.1.4.1.2': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnDescriptorRowStatus,
'1.3.6.1.2.1.86.1.4.1.3': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnDeToClpMappingMode,
'1.3.6.1.2.1.86.1.4.1.4': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnClpToDeMappingMode,
'1.3.6.1.2.1.86.1.4.1.5': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnCongestionMappingMode,
'1.3.6.1.2.1.86.1.4.1.6': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnEncapsulationMappingMode,
'1.3.6.1.2.1.86.1.4.1.7': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnEncapsulationMappings,
'1.3.6.1.2.1.86.1.4.1.8': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnFragAndReassEnabled,
'1.3.6.1.2.1.86.1.4.1.9': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnArpTranslationEnabled,
'1.3.6.1.2.1.86.1.5.1.1': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfVclCrossConnectIdentifier,
'1.3.6.1.2.1.86.2.0.1': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnStatusChange,
'1.3.6.1.2.1.86.3.1.1': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfBasicGroup,
'1.3.6.1.2.1.86.3.1.2': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfConnectionDescriptorGroup,
'1.3.6.1.2.1.86.3.1.3': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfAtmVclTableAugmentGroup,
'1.3.6.1.2.1.86.3.1.4': FR_ATM_PVC_SERVICE_IWF_MIB.frAtmIwfNotificationsGroup,
}
