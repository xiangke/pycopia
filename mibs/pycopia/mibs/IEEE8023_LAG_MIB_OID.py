# python
# This file is generated by a program (mib2py). 

import IEEE8023_LAG_MIB

OIDMAP = {
'1.2.840.10006.300.43': IEEE8023_LAG_MIB.lagMIB,
'1.2.840.10006.300.43.1': IEEE8023_LAG_MIB.lagMIBObjects,
'1.2.840.10006.300.43.1.1': IEEE8023_LAG_MIB.dot3adAgg,
'1.2.840.10006.300.43.1.2': IEEE8023_LAG_MIB.dot3adAggPort,
'1.2.840.10006.300.43.2': IEEE8023_LAG_MIB.dot3adAggConformance,
'1.2.840.10006.300.43.2.1': IEEE8023_LAG_MIB.dot3adAggGroups,
'1.2.840.10006.300.43.2.2': IEEE8023_LAG_MIB.dot3adAggCompliances,
'1.2.840.10006.300.43.1.3': IEEE8023_LAG_MIB.dot3adTablesLastChanged,
'1.2.840.10006.300.43.1.1.1.1.1': IEEE8023_LAG_MIB.dot3adAggIndex,
'1.2.840.10006.300.43.1.1.1.1.2': IEEE8023_LAG_MIB.dot3adAggMACAddress,
'1.2.840.10006.300.43.1.1.1.1.3': IEEE8023_LAG_MIB.dot3adAggActorSystemPriority,
'1.2.840.10006.300.43.1.1.1.1.4': IEEE8023_LAG_MIB.dot3adAggActorSystemID,
'1.2.840.10006.300.43.1.1.1.1.5': IEEE8023_LAG_MIB.dot3adAggAggregateOrIndividual,
'1.2.840.10006.300.43.1.1.1.1.6': IEEE8023_LAG_MIB.dot3adAggActorAdminKey,
'1.2.840.10006.300.43.1.1.1.1.7': IEEE8023_LAG_MIB.dot3adAggActorOperKey,
'1.2.840.10006.300.43.1.1.1.1.8': IEEE8023_LAG_MIB.dot3adAggPartnerSystemID,
'1.2.840.10006.300.43.1.1.1.1.9': IEEE8023_LAG_MIB.dot3adAggPartnerSystemPriority,
'1.2.840.10006.300.43.1.1.1.1.10': IEEE8023_LAG_MIB.dot3adAggPartnerOperKey,
'1.2.840.10006.300.43.1.1.1.1.11': IEEE8023_LAG_MIB.dot3adAggCollectorMaxDelay,
'1.2.840.10006.300.43.1.1.2.1.1': IEEE8023_LAG_MIB.dot3adAggPortListPorts,
'1.2.840.10006.300.43.1.2.1.1.1': IEEE8023_LAG_MIB.dot3adAggPortIndex,
'1.2.840.10006.300.43.1.2.1.1.2': IEEE8023_LAG_MIB.dot3adAggPortActorSystemPriority,
'1.2.840.10006.300.43.1.2.1.1.3': IEEE8023_LAG_MIB.dot3adAggPortActorSystemID,
'1.2.840.10006.300.43.1.2.1.1.4': IEEE8023_LAG_MIB.dot3adAggPortActorAdminKey,
'1.2.840.10006.300.43.1.2.1.1.5': IEEE8023_LAG_MIB.dot3adAggPortActorOperKey,
'1.2.840.10006.300.43.1.2.1.1.6': IEEE8023_LAG_MIB.dot3adAggPortPartnerAdminSystemPriority,
'1.2.840.10006.300.43.1.2.1.1.7': IEEE8023_LAG_MIB.dot3adAggPortPartnerOperSystemPriority,
'1.2.840.10006.300.43.1.2.1.1.8': IEEE8023_LAG_MIB.dot3adAggPortPartnerAdminSystemID,
'1.2.840.10006.300.43.1.2.1.1.9': IEEE8023_LAG_MIB.dot3adAggPortPartnerOperSystemID,
'1.2.840.10006.300.43.1.2.1.1.10': IEEE8023_LAG_MIB.dot3adAggPortPartnerAdminKey,
'1.2.840.10006.300.43.1.2.1.1.11': IEEE8023_LAG_MIB.dot3adAggPortPartnerOperKey,
'1.2.840.10006.300.43.1.2.1.1.12': IEEE8023_LAG_MIB.dot3adAggPortSelectedAggID,
'1.2.840.10006.300.43.1.2.1.1.13': IEEE8023_LAG_MIB.dot3adAggPortAttachedAggID,
'1.2.840.10006.300.43.1.2.1.1.14': IEEE8023_LAG_MIB.dot3adAggPortActorPort,
'1.2.840.10006.300.43.1.2.1.1.15': IEEE8023_LAG_MIB.dot3adAggPortActorPortPriority,
'1.2.840.10006.300.43.1.2.1.1.16': IEEE8023_LAG_MIB.dot3adAggPortPartnerAdminPort,
'1.2.840.10006.300.43.1.2.1.1.17': IEEE8023_LAG_MIB.dot3adAggPortPartnerOperPort,
'1.2.840.10006.300.43.1.2.1.1.18': IEEE8023_LAG_MIB.dot3adAggPortPartnerAdminPortPriority,
'1.2.840.10006.300.43.1.2.1.1.19': IEEE8023_LAG_MIB.dot3adAggPortPartnerOperPortPriority,
'1.2.840.10006.300.43.1.2.1.1.20': IEEE8023_LAG_MIB.dot3adAggPortActorAdminState,
'1.2.840.10006.300.43.1.2.1.1.21': IEEE8023_LAG_MIB.dot3adAggPortActorOperState,
'1.2.840.10006.300.43.1.2.1.1.22': IEEE8023_LAG_MIB.dot3adAggPortPartnerAdminState,
'1.2.840.10006.300.43.1.2.1.1.23': IEEE8023_LAG_MIB.dot3adAggPortPartnerOperState,
'1.2.840.10006.300.43.1.2.1.1.24': IEEE8023_LAG_MIB.dot3adAggPortAggregateOrIndividual,
'1.2.840.10006.300.43.1.2.2.1.1': IEEE8023_LAG_MIB.dot3adAggPortStatsLACPDUsRx,
'1.2.840.10006.300.43.1.2.2.1.2': IEEE8023_LAG_MIB.dot3adAggPortStatsMarkerPDUsRx,
'1.2.840.10006.300.43.1.2.2.1.3': IEEE8023_LAG_MIB.dot3adAggPortStatsMarkerResponsePDUsRx,
'1.2.840.10006.300.43.1.2.2.1.4': IEEE8023_LAG_MIB.dot3adAggPortStatsUnknownRx,
'1.2.840.10006.300.43.1.2.2.1.5': IEEE8023_LAG_MIB.dot3adAggPortStatsIllegalRx,
'1.2.840.10006.300.43.1.2.2.1.6': IEEE8023_LAG_MIB.dot3adAggPortStatsLACPDUsTx,
'1.2.840.10006.300.43.1.2.2.1.7': IEEE8023_LAG_MIB.dot3adAggPortStatsMarkerPDUsTx,
'1.2.840.10006.300.43.1.2.2.1.8': IEEE8023_LAG_MIB.dot3adAggPortStatsMarkerResponsePDUsTx,
'1.2.840.10006.300.43.1.2.3.1.1': IEEE8023_LAG_MIB.dot3adAggPortDebugRxState,
'1.2.840.10006.300.43.1.2.3.1.2': IEEE8023_LAG_MIB.dot3adAggPortDebugLastRxTime,
'1.2.840.10006.300.43.1.2.3.1.3': IEEE8023_LAG_MIB.dot3adAggPortDebugMuxState,
'1.2.840.10006.300.43.1.2.3.1.4': IEEE8023_LAG_MIB.dot3adAggPortDebugMuxReason,
'1.2.840.10006.300.43.1.2.3.1.5': IEEE8023_LAG_MIB.dot3adAggPortDebugActorChurnState,
'1.2.840.10006.300.43.1.2.3.1.6': IEEE8023_LAG_MIB.dot3adAggPortDebugPartnerChurnState,
'1.2.840.10006.300.43.1.2.3.1.7': IEEE8023_LAG_MIB.dot3adAggPortDebugActorChurnCount,
'1.2.840.10006.300.43.1.2.3.1.8': IEEE8023_LAG_MIB.dot3adAggPortDebugPartnerChurnCount,
'1.2.840.10006.300.43.1.2.3.1.9': IEEE8023_LAG_MIB.dot3adAggPortDebugActorSyncTransitionCount,
'1.2.840.10006.300.43.1.2.3.1.10': IEEE8023_LAG_MIB.dot3adAggPortDebugPartnerSyncTransitionCount,
'1.2.840.10006.300.43.1.2.3.1.11': IEEE8023_LAG_MIB.dot3adAggPortDebugActorChangeCount,
'1.2.840.10006.300.43.1.2.3.1.12': IEEE8023_LAG_MIB.dot3adAggPortDebugPartnerChangeCount,
'1.2.840.10006.300.43.2.1.1': IEEE8023_LAG_MIB.dot3adAggGroup,
'1.2.840.10006.300.43.2.1.1.6': IEEE8023_LAG_MIB.dot3adTablesLastChangedGroup,
'1.2.840.10006.300.43.2.1.2': IEEE8023_LAG_MIB.dot3adAggPortListGroup,
'1.2.840.10006.300.43.2.1.3': IEEE8023_LAG_MIB.dot3adAggPortGroup,
'1.2.840.10006.300.43.2.1.4': IEEE8023_LAG_MIB.dot3adAggPortStatsGroup,
'1.2.840.10006.300.43.2.1.5': IEEE8023_LAG_MIB.dot3adAggPortDebugGroup,
}
