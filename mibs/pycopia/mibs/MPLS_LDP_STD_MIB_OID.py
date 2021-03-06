# python
# This file is generated by a program (mib2py). 

import MPLS_LDP_STD_MIB

OIDMAP = {
'1.3.6.1.2.1.10.166.4': MPLS_LDP_STD_MIB.mplsLdpStdMIB,
'1.3.6.1.2.1.10.166.4.0': MPLS_LDP_STD_MIB.mplsLdpNotifications,
'1.3.6.1.2.1.10.166.4.1': MPLS_LDP_STD_MIB.mplsLdpObjects,
'1.3.6.1.2.1.10.166.4.1.1': MPLS_LDP_STD_MIB.mplsLdpLsrObjects,
'1.3.6.1.2.1.10.166.4.1.2': MPLS_LDP_STD_MIB.mplsLdpEntityObjects,
'1.3.6.1.2.1.10.166.4.1.3': MPLS_LDP_STD_MIB.mplsLdpSessionObjects,
'1.3.6.1.2.1.10.166.4.1.3.5': MPLS_LDP_STD_MIB.mplsLdpHelloAdjacencyObjects,
'1.3.6.1.2.1.10.166.4.1.3.8': MPLS_LDP_STD_MIB.mplsFecObjects,
'1.3.6.1.2.1.10.166.4.2': MPLS_LDP_STD_MIB.mplsLdpConformance,
'1.3.6.1.2.1.10.166.4.2.1': MPLS_LDP_STD_MIB.mplsLdpGroups,
'1.3.6.1.2.1.10.166.4.2.2': MPLS_LDP_STD_MIB.mplsLdpCompliances,
'1.3.6.1.2.1.10.166.4.1.1.1': MPLS_LDP_STD_MIB.mplsLdpLsrId,
'1.3.6.1.2.1.10.166.4.1.1.2': MPLS_LDP_STD_MIB.mplsLdpLsrLoopDetectionCapable,
'1.3.6.1.2.1.10.166.4.1.2.1': MPLS_LDP_STD_MIB.mplsLdpEntityLastChange,
'1.3.6.1.2.1.10.166.4.1.2.2': MPLS_LDP_STD_MIB.mplsLdpEntityIndexNext,
'1.3.6.1.2.1.10.166.4.1.3.1': MPLS_LDP_STD_MIB.mplsLdpPeerLastChange,
'1.3.6.1.2.1.10.166.4.1.3.8.1': MPLS_LDP_STD_MIB.mplsFecLastChange,
'1.3.6.1.2.1.10.166.4.1.3.8.2': MPLS_LDP_STD_MIB.mplsFecIndexNext,
'1.3.6.1.2.1.10.166.4.1.3.9': MPLS_LDP_STD_MIB.mplsLdpLspFecLastChange,
'1.3.6.1.2.1.10.166.4.1.2.3.1.1': MPLS_LDP_STD_MIB.mplsLdpEntityLdpId,
'1.3.6.1.2.1.10.166.4.1.2.3.1.2': MPLS_LDP_STD_MIB.mplsLdpEntityIndex,
'1.3.6.1.2.1.10.166.4.1.2.3.1.3': MPLS_LDP_STD_MIB.mplsLdpEntityProtocolVersion,
'1.3.6.1.2.1.10.166.4.1.2.3.1.4': MPLS_LDP_STD_MIB.mplsLdpEntityAdminStatus,
'1.3.6.1.2.1.10.166.4.1.2.3.1.5': MPLS_LDP_STD_MIB.mplsLdpEntityOperStatus,
'1.3.6.1.2.1.10.166.4.1.2.3.1.6': MPLS_LDP_STD_MIB.mplsLdpEntityTcpPort,
'1.3.6.1.2.1.10.166.4.1.2.3.1.7': MPLS_LDP_STD_MIB.mplsLdpEntityUdpDscPort,
'1.3.6.1.2.1.10.166.4.1.2.3.1.8': MPLS_LDP_STD_MIB.mplsLdpEntityMaxPduLength,
'1.3.6.1.2.1.10.166.4.1.2.3.1.9': MPLS_LDP_STD_MIB.mplsLdpEntityKeepAliveHoldTimer,
'1.3.6.1.2.1.10.166.4.1.2.3.1.10': MPLS_LDP_STD_MIB.mplsLdpEntityHelloHoldTimer,
'1.3.6.1.2.1.10.166.4.1.2.3.1.11': MPLS_LDP_STD_MIB.mplsLdpEntityInitSessionThreshold,
'1.3.6.1.2.1.10.166.4.1.2.3.1.12': MPLS_LDP_STD_MIB.mplsLdpEntityLabelDistMethod,
'1.3.6.1.2.1.10.166.4.1.2.3.1.13': MPLS_LDP_STD_MIB.mplsLdpEntityLabelRetentionMode,
'1.3.6.1.2.1.10.166.4.1.2.3.1.14': MPLS_LDP_STD_MIB.mplsLdpEntityPathVectorLimit,
'1.3.6.1.2.1.10.166.4.1.2.3.1.15': MPLS_LDP_STD_MIB.mplsLdpEntityHopCountLimit,
'1.3.6.1.2.1.10.166.4.1.2.3.1.16': MPLS_LDP_STD_MIB.mplsLdpEntityTransportAddrKind,
'1.3.6.1.2.1.10.166.4.1.2.3.1.17': MPLS_LDP_STD_MIB.mplsLdpEntityTargetPeer,
'1.3.6.1.2.1.10.166.4.1.2.3.1.18': MPLS_LDP_STD_MIB.mplsLdpEntityTargetPeerAddrType,
'1.3.6.1.2.1.10.166.4.1.2.3.1.19': MPLS_LDP_STD_MIB.mplsLdpEntityTargetPeerAddr,
'1.3.6.1.2.1.10.166.4.1.2.3.1.20': MPLS_LDP_STD_MIB.mplsLdpEntityLabelType,
'1.3.6.1.2.1.10.166.4.1.2.3.1.21': MPLS_LDP_STD_MIB.mplsLdpEntityDiscontinuityTime,
'1.3.6.1.2.1.10.166.4.1.2.3.1.22': MPLS_LDP_STD_MIB.mplsLdpEntityStorageType,
'1.3.6.1.2.1.10.166.4.1.2.3.1.23': MPLS_LDP_STD_MIB.mplsLdpEntityRowStatus,
'1.3.6.1.2.1.10.166.4.1.2.4.1.1': MPLS_LDP_STD_MIB.mplsLdpEntityStatsSessionAttempts,
'1.3.6.1.2.1.10.166.4.1.2.4.1.2': MPLS_LDP_STD_MIB.mplsLdpEntityStatsSessionRejectedNoHelloErrors,
'1.3.6.1.2.1.10.166.4.1.2.4.1.3': MPLS_LDP_STD_MIB.mplsLdpEntityStatsSessionRejectedAdErrors,
'1.3.6.1.2.1.10.166.4.1.2.4.1.4': MPLS_LDP_STD_MIB.mplsLdpEntityStatsSessionRejectedMaxPduErrors,
'1.3.6.1.2.1.10.166.4.1.2.4.1.5': MPLS_LDP_STD_MIB.mplsLdpEntityStatsSessionRejectedLRErrors,
'1.3.6.1.2.1.10.166.4.1.2.4.1.6': MPLS_LDP_STD_MIB.mplsLdpEntityStatsBadLdpIdentifierErrors,
'1.3.6.1.2.1.10.166.4.1.2.4.1.7': MPLS_LDP_STD_MIB.mplsLdpEntityStatsBadPduLengthErrors,
'1.3.6.1.2.1.10.166.4.1.2.4.1.8': MPLS_LDP_STD_MIB.mplsLdpEntityStatsBadMessageLengthErrors,
'1.3.6.1.2.1.10.166.4.1.2.4.1.9': MPLS_LDP_STD_MIB.mplsLdpEntityStatsBadTlvLengthErrors,
'1.3.6.1.2.1.10.166.4.1.2.4.1.10': MPLS_LDP_STD_MIB.mplsLdpEntityStatsMalformedTlvValueErrors,
'1.3.6.1.2.1.10.166.4.1.2.4.1.11': MPLS_LDP_STD_MIB.mplsLdpEntityStatsKeepAliveTimerExpErrors,
'1.3.6.1.2.1.10.166.4.1.2.4.1.12': MPLS_LDP_STD_MIB.mplsLdpEntityStatsShutdownReceivedNotifications,
'1.3.6.1.2.1.10.166.4.1.2.4.1.13': MPLS_LDP_STD_MIB.mplsLdpEntityStatsShutdownSentNotifications,
'1.3.6.1.2.1.10.166.4.1.3.2.1.1': MPLS_LDP_STD_MIB.mplsLdpPeerLdpId,
'1.3.6.1.2.1.10.166.4.1.3.2.1.2': MPLS_LDP_STD_MIB.mplsLdpPeerLabelDistMethod,
'1.3.6.1.2.1.10.166.4.1.3.2.1.3': MPLS_LDP_STD_MIB.mplsLdpPeerPathVectorLimit,
'1.3.6.1.2.1.10.166.4.1.3.2.1.4': MPLS_LDP_STD_MIB.mplsLdpPeerTransportAddrType,
'1.3.6.1.2.1.10.166.4.1.3.2.1.5': MPLS_LDP_STD_MIB.mplsLdpPeerTransportAddr,
'1.3.6.1.2.1.10.166.4.1.3.3.1.1': MPLS_LDP_STD_MIB.mplsLdpSessionStateLastChange,
'1.3.6.1.2.1.10.166.4.1.3.3.1.2': MPLS_LDP_STD_MIB.mplsLdpSessionState,
'1.3.6.1.2.1.10.166.4.1.3.3.1.3': MPLS_LDP_STD_MIB.mplsLdpSessionRole,
'1.3.6.1.2.1.10.166.4.1.3.3.1.4': MPLS_LDP_STD_MIB.mplsLdpSessionProtocolVersion,
'1.3.6.1.2.1.10.166.4.1.3.3.1.5': MPLS_LDP_STD_MIB.mplsLdpSessionKeepAliveHoldTimeRem,
'1.3.6.1.2.1.10.166.4.1.3.3.1.6': MPLS_LDP_STD_MIB.mplsLdpSessionKeepAliveTime,
'1.3.6.1.2.1.10.166.4.1.3.3.1.7': MPLS_LDP_STD_MIB.mplsLdpSessionMaxPduLength,
'1.3.6.1.2.1.10.166.4.1.3.3.1.8': MPLS_LDP_STD_MIB.mplsLdpSessionDiscontinuityTime,
'1.3.6.1.2.1.10.166.4.1.3.4.1.1': MPLS_LDP_STD_MIB.mplsLdpSessionStatsUnknownMesTypeErrors,
'1.3.6.1.2.1.10.166.4.1.3.4.1.2': MPLS_LDP_STD_MIB.mplsLdpSessionStatsUnknownTlvErrors,
'1.3.6.1.2.1.10.166.4.1.3.5.1.1.1': MPLS_LDP_STD_MIB.mplsLdpHelloAdjacencyIndex,
'1.3.6.1.2.1.10.166.4.1.3.5.1.1.2': MPLS_LDP_STD_MIB.mplsLdpHelloAdjacencyHoldTimeRem,
'1.3.6.1.2.1.10.166.4.1.3.5.1.1.3': MPLS_LDP_STD_MIB.mplsLdpHelloAdjacencyHoldTime,
'1.3.6.1.2.1.10.166.4.1.3.5.1.1.4': MPLS_LDP_STD_MIB.mplsLdpHelloAdjacencyType,
'1.3.6.1.2.1.10.166.4.1.3.6.1.1': MPLS_LDP_STD_MIB.mplsInSegmentLdpLspIndex,
'1.3.6.1.2.1.10.166.4.1.3.6.1.2': MPLS_LDP_STD_MIB.mplsInSegmentLdpLspLabelType,
'1.3.6.1.2.1.10.166.4.1.3.6.1.3': MPLS_LDP_STD_MIB.mplsInSegmentLdpLspType,
'1.3.6.1.2.1.10.166.4.1.3.7.1.1': MPLS_LDP_STD_MIB.mplsOutSegmentLdpLspIndex,
'1.3.6.1.2.1.10.166.4.1.3.7.1.2': MPLS_LDP_STD_MIB.mplsOutSegmentLdpLspLabelType,
'1.3.6.1.2.1.10.166.4.1.3.7.1.3': MPLS_LDP_STD_MIB.mplsOutSegmentLdpLspType,
'1.3.6.1.2.1.10.166.4.1.3.8.3.1.1': MPLS_LDP_STD_MIB.mplsFecIndex,
'1.3.6.1.2.1.10.166.4.1.3.8.3.1.2': MPLS_LDP_STD_MIB.mplsFecType,
'1.3.6.1.2.1.10.166.4.1.3.8.3.1.3': MPLS_LDP_STD_MIB.mplsFecAddrPrefixLength,
'1.3.6.1.2.1.10.166.4.1.3.8.3.1.4': MPLS_LDP_STD_MIB.mplsFecAddrType,
'1.3.6.1.2.1.10.166.4.1.3.8.3.1.5': MPLS_LDP_STD_MIB.mplsFecAddr,
'1.3.6.1.2.1.10.166.4.1.3.8.3.1.6': MPLS_LDP_STD_MIB.mplsFecStorageType,
'1.3.6.1.2.1.10.166.4.1.3.8.3.1.7': MPLS_LDP_STD_MIB.mplsFecRowStatus,
'1.3.6.1.2.1.10.166.4.1.3.10.1.1': MPLS_LDP_STD_MIB.mplsLdpLspFecSegment,
'1.3.6.1.2.1.10.166.4.1.3.10.1.2': MPLS_LDP_STD_MIB.mplsLdpLspFecSegmentIndex,
'1.3.6.1.2.1.10.166.4.1.3.10.1.3': MPLS_LDP_STD_MIB.mplsLdpLspFecIndex,
'1.3.6.1.2.1.10.166.4.1.3.10.1.4': MPLS_LDP_STD_MIB.mplsLdpLspFecStorageType,
'1.3.6.1.2.1.10.166.4.1.3.10.1.5': MPLS_LDP_STD_MIB.mplsLdpLspFecRowStatus,
'1.3.6.1.2.1.10.166.4.1.3.11.1.1': MPLS_LDP_STD_MIB.mplsLdpSessionPeerAddrIndex,
'1.3.6.1.2.1.10.166.4.1.3.11.1.2': MPLS_LDP_STD_MIB.mplsLdpSessionPeerNextHopAddrType,
'1.3.6.1.2.1.10.166.4.1.3.11.1.3': MPLS_LDP_STD_MIB.mplsLdpSessionPeerNextHopAddr,
'1.3.6.1.2.1.10.166.4.0.1': MPLS_LDP_STD_MIB.mplsLdpInitSessionThresholdExceeded,
'1.3.6.1.2.1.10.166.4.0.2': MPLS_LDP_STD_MIB.mplsLdpPathVectorLimitMismatch,
'1.3.6.1.2.1.10.166.4.0.3': MPLS_LDP_STD_MIB.mplsLdpSessionUp,
'1.3.6.1.2.1.10.166.4.0.4': MPLS_LDP_STD_MIB.mplsLdpSessionDown,
'1.3.6.1.2.1.10.166.4.2.1.1': MPLS_LDP_STD_MIB.mplsLdpGeneralGroup,
'1.3.6.1.2.1.10.166.4.2.1.2': MPLS_LDP_STD_MIB.mplsLdpLspGroup,
'1.3.6.1.2.1.10.166.4.2.1.3': MPLS_LDP_STD_MIB.mplsLdpNotificationsGroup,
}
