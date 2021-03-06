# python
# This file is generated by a program (mib2py). 

import DISMAN_TRACEROUTE_MIB

OIDMAP = {
'1.3.6.1.2.1.81': DISMAN_TRACEROUTE_MIB.traceRouteMIB,
'1.3.6.1.2.1.81.0': DISMAN_TRACEROUTE_MIB.traceRouteNotifications,
'1.3.6.1.2.1.81.1': DISMAN_TRACEROUTE_MIB.traceRouteObjects,
'1.3.6.1.2.1.81.2': DISMAN_TRACEROUTE_MIB.traceRouteConformance,
'1.3.6.1.2.1.81.2.1': DISMAN_TRACEROUTE_MIB.traceRouteCompliances,
'1.3.6.1.2.1.81.2.2': DISMAN_TRACEROUTE_MIB.traceRouteGroups,
'1.3.6.1.2.1.81.3': DISMAN_TRACEROUTE_MIB.traceRouteImplementationTypeDomains,
'1.3.6.1.2.1.81.3.1': DISMAN_TRACEROUTE_MIB.traceRouteUsingUdpProbes,
'1.3.6.1.2.1.81.1.1': DISMAN_TRACEROUTE_MIB.traceRouteMaxConcurrentRequests,
'1.3.6.1.2.1.81.1.2.1.1': DISMAN_TRACEROUTE_MIB.traceRouteCtlOwnerIndex,
'1.3.6.1.2.1.81.1.2.1.2': DISMAN_TRACEROUTE_MIB.traceRouteCtlTestName,
'1.3.6.1.2.1.81.1.2.1.3': DISMAN_TRACEROUTE_MIB.traceRouteCtlTargetAddressType,
'1.3.6.1.2.1.81.1.2.1.4': DISMAN_TRACEROUTE_MIB.traceRouteCtlTargetAddress,
'1.3.6.1.2.1.81.1.2.1.5': DISMAN_TRACEROUTE_MIB.traceRouteCtlByPassRouteTable,
'1.3.6.1.2.1.81.1.2.1.6': DISMAN_TRACEROUTE_MIB.traceRouteCtlDataSize,
'1.3.6.1.2.1.81.1.2.1.7': DISMAN_TRACEROUTE_MIB.traceRouteCtlTimeOut,
'1.3.6.1.2.1.81.1.2.1.8': DISMAN_TRACEROUTE_MIB.traceRouteCtlProbesPerHop,
'1.3.6.1.2.1.81.1.2.1.9': DISMAN_TRACEROUTE_MIB.traceRouteCtlPort,
'1.3.6.1.2.1.81.1.2.1.10': DISMAN_TRACEROUTE_MIB.traceRouteCtlMaxTtl,
'1.3.6.1.2.1.81.1.2.1.11': DISMAN_TRACEROUTE_MIB.traceRouteCtlDSField,
'1.3.6.1.2.1.81.1.2.1.12': DISMAN_TRACEROUTE_MIB.traceRouteCtlSourceAddressType,
'1.3.6.1.2.1.81.1.2.1.13': DISMAN_TRACEROUTE_MIB.traceRouteCtlSourceAddress,
'1.3.6.1.2.1.81.1.2.1.14': DISMAN_TRACEROUTE_MIB.traceRouteCtlIfIndex,
'1.3.6.1.2.1.81.1.2.1.15': DISMAN_TRACEROUTE_MIB.traceRouteCtlMiscOptions,
'1.3.6.1.2.1.81.1.2.1.16': DISMAN_TRACEROUTE_MIB.traceRouteCtlMaxFailures,
'1.3.6.1.2.1.81.1.2.1.17': DISMAN_TRACEROUTE_MIB.traceRouteCtlDontFragment,
'1.3.6.1.2.1.81.1.2.1.18': DISMAN_TRACEROUTE_MIB.traceRouteCtlInitialTtl,
'1.3.6.1.2.1.81.1.2.1.19': DISMAN_TRACEROUTE_MIB.traceRouteCtlFrequency,
'1.3.6.1.2.1.81.1.2.1.20': DISMAN_TRACEROUTE_MIB.traceRouteCtlStorageType,
'1.3.6.1.2.1.81.1.2.1.21': DISMAN_TRACEROUTE_MIB.traceRouteCtlAdminStatus,
'1.3.6.1.2.1.81.1.2.1.22': DISMAN_TRACEROUTE_MIB.traceRouteCtlDescr,
'1.3.6.1.2.1.81.1.2.1.23': DISMAN_TRACEROUTE_MIB.traceRouteCtlMaxRows,
'1.3.6.1.2.1.81.1.2.1.24': DISMAN_TRACEROUTE_MIB.traceRouteCtlTrapGeneration,
'1.3.6.1.2.1.81.1.2.1.25': DISMAN_TRACEROUTE_MIB.traceRouteCtlCreateHopsEntries,
'1.3.6.1.2.1.81.1.2.1.26': DISMAN_TRACEROUTE_MIB.traceRouteCtlType,
'1.3.6.1.2.1.81.1.2.1.27': DISMAN_TRACEROUTE_MIB.traceRouteCtlRowStatus,
'1.3.6.1.2.1.81.1.3.1.1': DISMAN_TRACEROUTE_MIB.traceRouteResultsOperStatus,
'1.3.6.1.2.1.81.1.3.1.2': DISMAN_TRACEROUTE_MIB.traceRouteResultsCurHopCount,
'1.3.6.1.2.1.81.1.3.1.3': DISMAN_TRACEROUTE_MIB.traceRouteResultsCurProbeCount,
'1.3.6.1.2.1.81.1.3.1.4': DISMAN_TRACEROUTE_MIB.traceRouteResultsIpTgtAddrType,
'1.3.6.1.2.1.81.1.3.1.5': DISMAN_TRACEROUTE_MIB.traceRouteResultsIpTgtAddr,
'1.3.6.1.2.1.81.1.3.1.6': DISMAN_TRACEROUTE_MIB.traceRouteResultsTestAttempts,
'1.3.6.1.2.1.81.1.3.1.7': DISMAN_TRACEROUTE_MIB.traceRouteResultsTestSuccesses,
'1.3.6.1.2.1.81.1.3.1.8': DISMAN_TRACEROUTE_MIB.traceRouteResultsLastGoodPath,
'1.3.6.1.2.1.81.1.4.1.1': DISMAN_TRACEROUTE_MIB.traceRouteProbeHistoryIndex,
'1.3.6.1.2.1.81.1.4.1.2': DISMAN_TRACEROUTE_MIB.traceRouteProbeHistoryHopIndex,
'1.3.6.1.2.1.81.1.4.1.3': DISMAN_TRACEROUTE_MIB.traceRouteProbeHistoryProbeIndex,
'1.3.6.1.2.1.81.1.4.1.4': DISMAN_TRACEROUTE_MIB.traceRouteProbeHistoryHAddrType,
'1.3.6.1.2.1.81.1.4.1.5': DISMAN_TRACEROUTE_MIB.traceRouteProbeHistoryHAddr,
'1.3.6.1.2.1.81.1.4.1.6': DISMAN_TRACEROUTE_MIB.traceRouteProbeHistoryResponse,
'1.3.6.1.2.1.81.1.4.1.7': DISMAN_TRACEROUTE_MIB.traceRouteProbeHistoryStatus,
'1.3.6.1.2.1.81.1.4.1.8': DISMAN_TRACEROUTE_MIB.traceRouteProbeHistoryLastRC,
'1.3.6.1.2.1.81.1.4.1.9': DISMAN_TRACEROUTE_MIB.traceRouteProbeHistoryTime,
'1.3.6.1.2.1.81.1.5.1.1': DISMAN_TRACEROUTE_MIB.traceRouteHopsHopIndex,
'1.3.6.1.2.1.81.1.5.1.2': DISMAN_TRACEROUTE_MIB.traceRouteHopsIpTgtAddressType,
'1.3.6.1.2.1.81.1.5.1.3': DISMAN_TRACEROUTE_MIB.traceRouteHopsIpTgtAddress,
'1.3.6.1.2.1.81.1.5.1.4': DISMAN_TRACEROUTE_MIB.traceRouteHopsMinRtt,
'1.3.6.1.2.1.81.1.5.1.5': DISMAN_TRACEROUTE_MIB.traceRouteHopsMaxRtt,
'1.3.6.1.2.1.81.1.5.1.6': DISMAN_TRACEROUTE_MIB.traceRouteHopsAverageRtt,
'1.3.6.1.2.1.81.1.5.1.7': DISMAN_TRACEROUTE_MIB.traceRouteHopsRttSumOfSquares,
'1.3.6.1.2.1.81.1.5.1.8': DISMAN_TRACEROUTE_MIB.traceRouteHopsSentProbes,
'1.3.6.1.2.1.81.1.5.1.9': DISMAN_TRACEROUTE_MIB.traceRouteHopsProbeResponses,
'1.3.6.1.2.1.81.1.5.1.10': DISMAN_TRACEROUTE_MIB.traceRouteHopsLastGoodProbe,
'1.3.6.1.2.1.81.0.1': DISMAN_TRACEROUTE_MIB.traceRoutePathChange,
'1.3.6.1.2.1.81.0.2': DISMAN_TRACEROUTE_MIB.traceRouteTestFailed,
'1.3.6.1.2.1.81.0.3': DISMAN_TRACEROUTE_MIB.traceRouteTestCompleted,
'1.3.6.1.2.1.81.2.2.1': DISMAN_TRACEROUTE_MIB.traceRouteGroup,
'1.3.6.1.2.1.81.2.2.2': DISMAN_TRACEROUTE_MIB.traceRouteTimeStampGroup,
'1.3.6.1.2.1.81.2.2.3': DISMAN_TRACEROUTE_MIB.traceRouteNotificationsGroup,
'1.3.6.1.2.1.81.2.2.4': DISMAN_TRACEROUTE_MIB.traceRouteHopsTableGroup,
'1.3.6.1.2.1.81.2.2.5': DISMAN_TRACEROUTE_MIB.traceRouteMinimumGroup,
'1.3.6.1.2.1.81.2.2.6': DISMAN_TRACEROUTE_MIB.traceRouteCtlRowStatusGroup,
'1.3.6.1.2.1.81.2.2.7': DISMAN_TRACEROUTE_MIB.traceRouteHistoryGroup,
}
