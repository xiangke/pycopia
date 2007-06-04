# python
# This file is generated by a program (mib2py). 

import Q_BRIDGE_MIB

OIDMAP = {
'1.3.6.1.2.1.17.7': Q_BRIDGE_MIB.qBridgeMIB,
'1.3.6.1.2.1.17.7.1': Q_BRIDGE_MIB.qBridgeMIBObjects,
'1.3.6.1.2.1.17.7.1.1': Q_BRIDGE_MIB.dot1qBase,
'1.3.6.1.2.1.17.7.1.2': Q_BRIDGE_MIB.dot1qTp,
'1.3.6.1.2.1.17.7.1.3': Q_BRIDGE_MIB.dot1qStatic,
'1.3.6.1.2.1.17.7.1.4': Q_BRIDGE_MIB.dot1qVlan,
'1.3.6.1.2.1.17.7.1.5': Q_BRIDGE_MIB.dot1vProtocol,
'1.3.6.1.2.1.17.7.2': Q_BRIDGE_MIB.qBridgeConformance,
'1.3.6.1.2.1.17.7.2.1': Q_BRIDGE_MIB.qBridgeGroups,
'1.3.6.1.2.1.17.7.2.2': Q_BRIDGE_MIB.qBridgeCompliances,
'1.3.6.1.2.1.17.7.1.1.1': Q_BRIDGE_MIB.dot1qVlanVersionNumber,
'1.3.6.1.2.1.17.7.1.1.2': Q_BRIDGE_MIB.dot1qMaxVlanId,
'1.3.6.1.2.1.17.7.1.1.3': Q_BRIDGE_MIB.dot1qMaxSupportedVlans,
'1.3.6.1.2.1.17.7.1.1.4': Q_BRIDGE_MIB.dot1qNumVlans,
'1.3.6.1.2.1.17.7.1.1.5': Q_BRIDGE_MIB.dot1qGvrpStatus,
'1.3.6.1.2.1.17.7.1.4.1': Q_BRIDGE_MIB.dot1qVlanNumDeletes,
'1.3.6.1.2.1.17.7.1.4.4': Q_BRIDGE_MIB.dot1qNextFreeLocalVlanIndex,
'1.3.6.1.2.1.17.7.1.4.9': Q_BRIDGE_MIB.dot1qConstraintSetDefault,
'1.3.6.1.2.1.17.7.1.4.10': Q_BRIDGE_MIB.dot1qConstraintTypeDefault,
'1.3.6.1.2.1.17.7.1.2.1.1.1': Q_BRIDGE_MIB.dot1qFdbId,
'1.3.6.1.2.1.17.7.1.2.1.1.2': Q_BRIDGE_MIB.dot1qFdbDynamicCount,
'1.3.6.1.2.1.17.7.1.2.2.1.1': Q_BRIDGE_MIB.dot1qTpFdbAddress,
'1.3.6.1.2.1.17.7.1.2.2.1.2': Q_BRIDGE_MIB.dot1qTpFdbPort,
'1.3.6.1.2.1.17.7.1.2.2.1.3': Q_BRIDGE_MIB.dot1qTpFdbStatus,
'1.3.6.1.2.1.17.7.1.2.3.1.1': Q_BRIDGE_MIB.dot1qTpGroupAddress,
'1.3.6.1.2.1.17.7.1.2.3.1.2': Q_BRIDGE_MIB.dot1qTpGroupEgressPorts,
'1.3.6.1.2.1.17.7.1.2.3.1.3': Q_BRIDGE_MIB.dot1qTpGroupLearnt,
'1.3.6.1.2.1.17.7.1.2.4.1.1': Q_BRIDGE_MIB.dot1qForwardAllPorts,
'1.3.6.1.2.1.17.7.1.2.4.1.2': Q_BRIDGE_MIB.dot1qForwardAllStaticPorts,
'1.3.6.1.2.1.17.7.1.2.4.1.3': Q_BRIDGE_MIB.dot1qForwardAllForbiddenPorts,
'1.3.6.1.2.1.17.7.1.2.5.1.1': Q_BRIDGE_MIB.dot1qForwardUnregisteredPorts,
'1.3.6.1.2.1.17.7.1.2.5.1.2': Q_BRIDGE_MIB.dot1qForwardUnregisteredStaticPorts,
'1.3.6.1.2.1.17.7.1.2.5.1.3': Q_BRIDGE_MIB.dot1qForwardUnregisteredForbiddenPorts,
'1.3.6.1.2.1.17.7.1.3.1.1.1': Q_BRIDGE_MIB.dot1qStaticUnicastAddress,
'1.3.6.1.2.1.17.7.1.3.1.1.2': Q_BRIDGE_MIB.dot1qStaticUnicastReceivePort,
'1.3.6.1.2.1.17.7.1.3.1.1.3': Q_BRIDGE_MIB.dot1qStaticUnicastAllowedToGoTo,
'1.3.6.1.2.1.17.7.1.3.1.1.4': Q_BRIDGE_MIB.dot1qStaticUnicastStatus,
'1.3.6.1.2.1.17.7.1.3.2.1.1': Q_BRIDGE_MIB.dot1qStaticMulticastAddress,
'1.3.6.1.2.1.17.7.1.3.2.1.2': Q_BRIDGE_MIB.dot1qStaticMulticastReceivePort,
'1.3.6.1.2.1.17.7.1.3.2.1.3': Q_BRIDGE_MIB.dot1qStaticMulticastStaticEgressPorts,
'1.3.6.1.2.1.17.7.1.3.2.1.4': Q_BRIDGE_MIB.dot1qStaticMulticastForbiddenEgressPorts,
'1.3.6.1.2.1.17.7.1.3.2.1.5': Q_BRIDGE_MIB.dot1qStaticMulticastStatus,
'1.3.6.1.2.1.17.7.1.4.2.1.1': Q_BRIDGE_MIB.dot1qVlanTimeMark,
'1.3.6.1.2.1.17.7.1.4.2.1.2': Q_BRIDGE_MIB.dot1qVlanIndex,
'1.3.6.1.2.1.17.7.1.4.2.1.3': Q_BRIDGE_MIB.dot1qVlanFdbId,
'1.3.6.1.2.1.17.7.1.4.2.1.4': Q_BRIDGE_MIB.dot1qVlanCurrentEgressPorts,
'1.3.6.1.2.1.17.7.1.4.2.1.5': Q_BRIDGE_MIB.dot1qVlanCurrentUntaggedPorts,
'1.3.6.1.2.1.17.7.1.4.2.1.6': Q_BRIDGE_MIB.dot1qVlanStatus,
'1.3.6.1.2.1.17.7.1.4.2.1.7': Q_BRIDGE_MIB.dot1qVlanCreationTime,
'1.3.6.1.2.1.17.7.1.4.3.1.1': Q_BRIDGE_MIB.dot1qVlanStaticName,
'1.3.6.1.2.1.17.7.1.4.3.1.2': Q_BRIDGE_MIB.dot1qVlanStaticEgressPorts,
'1.3.6.1.2.1.17.7.1.4.3.1.3': Q_BRIDGE_MIB.dot1qVlanForbiddenEgressPorts,
'1.3.6.1.2.1.17.7.1.4.3.1.4': Q_BRIDGE_MIB.dot1qVlanStaticUntaggedPorts,
'1.3.6.1.2.1.17.7.1.4.3.1.5': Q_BRIDGE_MIB.dot1qVlanStaticRowStatus,
'1.3.6.1.2.1.17.7.1.4.5.1.1': Q_BRIDGE_MIB.dot1qPvid,
'1.3.6.1.2.1.17.7.1.4.5.1.2': Q_BRIDGE_MIB.dot1qPortAcceptableFrameTypes,
'1.3.6.1.2.1.17.7.1.4.5.1.3': Q_BRIDGE_MIB.dot1qPortIngressFiltering,
'1.3.6.1.2.1.17.7.1.4.5.1.4': Q_BRIDGE_MIB.dot1qPortGvrpStatus,
'1.3.6.1.2.1.17.7.1.4.5.1.5': Q_BRIDGE_MIB.dot1qPortGvrpFailedRegistrations,
'1.3.6.1.2.1.17.7.1.4.5.1.6': Q_BRIDGE_MIB.dot1qPortGvrpLastPduOrigin,
'1.3.6.1.2.1.17.7.1.4.5.1.7': Q_BRIDGE_MIB.dot1qPortRestrictedVlanRegistration,
'1.3.6.1.2.1.17.7.1.4.6.1.1': Q_BRIDGE_MIB.dot1qTpVlanPortInFrames,
'1.3.6.1.2.1.17.7.1.4.6.1.2': Q_BRIDGE_MIB.dot1qTpVlanPortOutFrames,
'1.3.6.1.2.1.17.7.1.4.6.1.3': Q_BRIDGE_MIB.dot1qTpVlanPortInDiscards,
'1.3.6.1.2.1.17.7.1.4.6.1.4': Q_BRIDGE_MIB.dot1qTpVlanPortInOverflowFrames,
'1.3.6.1.2.1.17.7.1.4.6.1.5': Q_BRIDGE_MIB.dot1qTpVlanPortOutOverflowFrames,
'1.3.6.1.2.1.17.7.1.4.6.1.6': Q_BRIDGE_MIB.dot1qTpVlanPortInOverflowDiscards,
'1.3.6.1.2.1.17.7.1.4.7.1.1': Q_BRIDGE_MIB.dot1qTpVlanPortHCInFrames,
'1.3.6.1.2.1.17.7.1.4.7.1.2': Q_BRIDGE_MIB.dot1qTpVlanPortHCOutFrames,
'1.3.6.1.2.1.17.7.1.4.7.1.3': Q_BRIDGE_MIB.dot1qTpVlanPortHCInDiscards,
'1.3.6.1.2.1.17.7.1.4.8.1.1': Q_BRIDGE_MIB.dot1qConstraintVlan,
'1.3.6.1.2.1.17.7.1.4.8.1.2': Q_BRIDGE_MIB.dot1qConstraintSet,
'1.3.6.1.2.1.17.7.1.4.8.1.3': Q_BRIDGE_MIB.dot1qConstraintType,
'1.3.6.1.2.1.17.7.1.4.8.1.4': Q_BRIDGE_MIB.dot1qConstraintStatus,
'1.3.6.1.2.1.17.7.1.5.1.1.1': Q_BRIDGE_MIB.dot1vProtocolTemplateFrameType,
'1.3.6.1.2.1.17.7.1.5.1.1.2': Q_BRIDGE_MIB.dot1vProtocolTemplateProtocolValue,
'1.3.6.1.2.1.17.7.1.5.1.1.3': Q_BRIDGE_MIB.dot1vProtocolGroupId,
'1.3.6.1.2.1.17.7.1.5.1.1.4': Q_BRIDGE_MIB.dot1vProtocolGroupRowStatus,
'1.3.6.1.2.1.17.7.1.5.2.1.1': Q_BRIDGE_MIB.dot1vProtocolPortGroupId,
'1.3.6.1.2.1.17.7.1.5.2.1.2': Q_BRIDGE_MIB.dot1vProtocolPortGroupVid,
'1.3.6.1.2.1.17.7.1.5.2.1.3': Q_BRIDGE_MIB.dot1vProtocolPortRowStatus,
'1.3.6.1.2.1.17.7.2.1.1': Q_BRIDGE_MIB.qBridgeBaseGroup,
'1.3.6.1.2.1.17.7.2.1.2': Q_BRIDGE_MIB.qBridgeFdbUnicastGroup,
'1.3.6.1.2.1.17.7.2.1.3': Q_BRIDGE_MIB.qBridgeFdbMulticastGroup,
'1.3.6.1.2.1.17.7.2.1.4': Q_BRIDGE_MIB.qBridgeServiceRequirementsGroup,
'1.3.6.1.2.1.17.7.2.1.5': Q_BRIDGE_MIB.qBridgeFdbStaticGroup,
'1.3.6.1.2.1.17.7.2.1.6': Q_BRIDGE_MIB.qBridgeVlanGroup,
'1.3.6.1.2.1.17.7.2.1.7': Q_BRIDGE_MIB.qBridgeVlanStaticGroup,
'1.3.6.1.2.1.17.7.2.1.8': Q_BRIDGE_MIB.qBridgePortGroup,
'1.3.6.1.2.1.17.7.2.1.9': Q_BRIDGE_MIB.qBridgeVlanStatisticsGroup,
'1.3.6.1.2.1.17.7.2.1.10': Q_BRIDGE_MIB.qBridgeVlanStatisticsOverflowGroup,
'1.3.6.1.2.1.17.7.2.1.11': Q_BRIDGE_MIB.qBridgeVlanHCStatisticsGroup,
'1.3.6.1.2.1.17.7.2.1.12': Q_BRIDGE_MIB.qBridgeLearningConstraintsGroup,
'1.3.6.1.2.1.17.7.2.1.13': Q_BRIDGE_MIB.qBridgeLearningConstraintDefaultGroup,
'1.3.6.1.2.1.17.7.2.1.14': Q_BRIDGE_MIB.qBridgeClassificationDeviceGroup,
'1.3.6.1.2.1.17.7.2.1.15': Q_BRIDGE_MIB.qBridgeClassificationPortGroup,
'1.3.6.1.2.1.17.7.2.1.16': Q_BRIDGE_MIB.qBridgePortGroup2,
}
