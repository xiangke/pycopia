# python
# This file is generated by a program (mib2py). 

import TE_MIB

OIDMAP = {
'1.3.6.1.2.1.122': TE_MIB.teMIB,
'1.3.6.1.2.1.122.0': TE_MIB.teMIBNotifications,
'1.3.6.1.2.1.122.1': TE_MIB.teMIBObjects,
'1.3.6.1.2.1.122.1.1': TE_MIB.teInfo,
'1.3.6.1.2.1.122.2': TE_MIB.teMIBConformance,
'1.3.6.1.2.1.122.2.1': TE_MIB.teGroups,
'1.3.6.1.2.1.122.2.2': TE_MIB.teModuleCompliance,
'1.3.6.1.2.1.122.1.1.1': TE_MIB.teDistProtocol,
'1.3.6.1.2.1.122.1.1.2': TE_MIB.teSignalingProto,
'1.3.6.1.2.1.122.1.1.3': TE_MIB.teNotificationEnable,
'1.3.6.1.2.1.122.1.1.4': TE_MIB.teNextTunnelIndex,
'1.3.6.1.2.1.122.1.1.5': TE_MIB.teNextPathHopIndex,
'1.3.6.1.2.1.122.1.1.6': TE_MIB.teConfiguredTunnels,
'1.3.6.1.2.1.122.1.1.7': TE_MIB.teActiveTunnels,
'1.3.6.1.2.1.122.1.1.8': TE_MIB.tePrimaryTunnels,
'1.3.6.1.2.1.122.1.1.9.1.1': TE_MIB.teAdminGroupNumber,
'1.3.6.1.2.1.122.1.1.9.1.2': TE_MIB.teAdminGroupName,
'1.3.6.1.2.1.122.1.1.9.1.3': TE_MIB.teAdminGroupRowStatus,
'1.3.6.1.2.1.122.1.2.1.1': TE_MIB.teTunnelIndex,
'1.3.6.1.2.1.122.1.2.1.2': TE_MIB.teTunnelName,
'1.3.6.1.2.1.122.1.2.1.3': TE_MIB.teTunnelNextPathIndex,
'1.3.6.1.2.1.122.1.2.1.4': TE_MIB.teTunnelRowStatus,
'1.3.6.1.2.1.122.1.2.1.5': TE_MIB.teTunnelStorageType,
'1.3.6.1.2.1.122.1.2.1.6': TE_MIB.teTunnelSourceAddressType,
'1.3.6.1.2.1.122.1.2.1.7': TE_MIB.teTunnelSourceAddress,
'1.3.6.1.2.1.122.1.2.1.8': TE_MIB.teTunnelDestinationAddressType,
'1.3.6.1.2.1.122.1.2.1.9': TE_MIB.teTunnelDestinationAddress,
'1.3.6.1.2.1.122.1.2.1.10': TE_MIB.teTunnelState,
'1.3.6.1.2.1.122.1.2.1.11': TE_MIB.teTunnelDiscontinuityTimer,
'1.3.6.1.2.1.122.1.2.1.12': TE_MIB.teTunnelOctets,
'1.3.6.1.2.1.122.1.2.1.13': TE_MIB.teTunnelPackets,
'1.3.6.1.2.1.122.1.2.1.14': TE_MIB.teTunnelLPOctets,
'1.3.6.1.2.1.122.1.2.1.15': TE_MIB.teTunnelLPPackets,
'1.3.6.1.2.1.122.1.2.1.16': TE_MIB.teTunnelAge,
'1.3.6.1.2.1.122.1.2.1.17': TE_MIB.teTunnelTimeUp,
'1.3.6.1.2.1.122.1.2.1.18': TE_MIB.teTunnelPrimaryTimeUp,
'1.3.6.1.2.1.122.1.2.1.19': TE_MIB.teTunnelTransitions,
'1.3.6.1.2.1.122.1.2.1.20': TE_MIB.teTunnelLastTransition,
'1.3.6.1.2.1.122.1.2.1.21': TE_MIB.teTunnelPathChanges,
'1.3.6.1.2.1.122.1.2.1.22': TE_MIB.teTunnelLastPathChange,
'1.3.6.1.2.1.122.1.2.1.23': TE_MIB.teTunnelConfiguredPaths,
'1.3.6.1.2.1.122.1.2.1.24': TE_MIB.teTunnelStandbyPaths,
'1.3.6.1.2.1.122.1.2.1.25': TE_MIB.teTunnelOperationalPaths,
'1.3.6.1.2.1.122.1.3.1.1': TE_MIB.tePathIndex,
'1.3.6.1.2.1.122.1.3.1.2': TE_MIB.tePathName,
'1.3.6.1.2.1.122.1.3.1.3': TE_MIB.tePathRowStatus,
'1.3.6.1.2.1.122.1.3.1.4': TE_MIB.tePathStorageType,
'1.3.6.1.2.1.122.1.3.1.5': TE_MIB.tePathType,
'1.3.6.1.2.1.122.1.3.1.6': TE_MIB.tePathConfiguredRoute,
'1.3.6.1.2.1.122.1.3.1.7': TE_MIB.tePathBandwidth,
'1.3.6.1.2.1.122.1.3.1.8': TE_MIB.tePathIncludeAny,
'1.3.6.1.2.1.122.1.3.1.9': TE_MIB.tePathIncludeAll,
'1.3.6.1.2.1.122.1.3.1.10': TE_MIB.tePathExclude,
'1.3.6.1.2.1.122.1.3.1.11': TE_MIB.tePathSetupPriority,
'1.3.6.1.2.1.122.1.3.1.12': TE_MIB.tePathHoldPriority,
'1.3.6.1.2.1.122.1.3.1.13': TE_MIB.tePathProperties,
'1.3.6.1.2.1.122.1.3.1.14': TE_MIB.tePathOperStatus,
'1.3.6.1.2.1.122.1.3.1.15': TE_MIB.tePathAdminStatus,
'1.3.6.1.2.1.122.1.3.1.16': TE_MIB.tePathComputedRoute,
'1.3.6.1.2.1.122.1.3.1.17': TE_MIB.tePathRecordedRoute,
'1.3.6.1.2.1.122.1.4.1.1': TE_MIB.teHopListIndex,
'1.3.6.1.2.1.122.1.4.1.2': TE_MIB.tePathHopIndex,
'1.3.6.1.2.1.122.1.4.1.3': TE_MIB.tePathHopRowStatus,
'1.3.6.1.2.1.122.1.4.1.4': TE_MIB.tePathHopStorageType,
'1.3.6.1.2.1.122.1.4.1.5': TE_MIB.tePathHopAddrType,
'1.3.6.1.2.1.122.1.4.1.6': TE_MIB.tePathHopAddress,
'1.3.6.1.2.1.122.1.4.1.7': TE_MIB.tePathHopType,
'1.3.6.1.2.1.122.0.1': TE_MIB.teTunnelUp,
'1.3.6.1.2.1.122.0.2': TE_MIB.teTunnelDown,
'1.3.6.1.2.1.122.0.3': TE_MIB.teTunnelChanged,
'1.3.6.1.2.1.122.0.4': TE_MIB.teTunnelRerouted,
'1.3.6.1.2.1.122.2.1.1': TE_MIB.teTrafficEngineeringGroup,
'1.3.6.1.2.1.122.2.1.2': TE_MIB.teNotificationGroup,
}
