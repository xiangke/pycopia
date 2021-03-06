# python
# This file is generated by a program (mib2py). 

import TE_LINK_STD_MIB

OIDMAP = {
'1.3.6.1.2.1.10.200': TE_LINK_STD_MIB.teLinkStdMIB,
'1.3.6.1.2.1.10.200.0': TE_LINK_STD_MIB.teLinkNotifications,
'1.3.6.1.2.1.10.200.1': TE_LINK_STD_MIB.teLinkObjects,
'1.3.6.1.2.1.10.200.2': TE_LINK_STD_MIB.teLinkConformance,
'1.3.6.1.2.1.10.200.2.1': TE_LINK_STD_MIB.teLinkCompliances,
'1.3.6.1.2.1.10.200.2.2': TE_LINK_STD_MIB.teLinkGroups,
'1.3.6.1.2.1.10.200.1.1.1.1': TE_LINK_STD_MIB.teLinkAddressType,
'1.3.6.1.2.1.10.200.1.1.1.2': TE_LINK_STD_MIB.teLinkLocalIpAddr,
'1.3.6.1.2.1.10.200.1.1.1.3': TE_LINK_STD_MIB.teLinkRemoteIpAddr,
'1.3.6.1.2.1.10.200.1.1.1.4': TE_LINK_STD_MIB.teLinkMetric,
'1.3.6.1.2.1.10.200.1.1.1.5': TE_LINK_STD_MIB.teLinkMaximumReservableBandwidth,
'1.3.6.1.2.1.10.200.1.1.1.6': TE_LINK_STD_MIB.teLinkProtectionType,
'1.3.6.1.2.1.10.200.1.1.1.7': TE_LINK_STD_MIB.teLinkWorkingPriority,
'1.3.6.1.2.1.10.200.1.1.1.8': TE_LINK_STD_MIB.teLinkResourceClass,
'1.3.6.1.2.1.10.200.1.1.1.9': TE_LINK_STD_MIB.teLinkIncomingIfId,
'1.3.6.1.2.1.10.200.1.1.1.10': TE_LINK_STD_MIB.teLinkOutgoingIfId,
'1.3.6.1.2.1.10.200.1.1.1.11': TE_LINK_STD_MIB.teLinkRowStatus,
'1.3.6.1.2.1.10.200.1.1.1.12': TE_LINK_STD_MIB.teLinkStorageType,
'1.3.6.1.2.1.10.200.1.2.1.1': TE_LINK_STD_MIB.teLinkDescriptorId,
'1.3.6.1.2.1.10.200.1.2.1.2': TE_LINK_STD_MIB.teLinkDescrSwitchingCapability,
'1.3.6.1.2.1.10.200.1.2.1.3': TE_LINK_STD_MIB.teLinkDescrEncodingType,
'1.3.6.1.2.1.10.200.1.2.1.4': TE_LINK_STD_MIB.teLinkDescrMinLspBandwidth,
'1.3.6.1.2.1.10.200.1.2.1.5': TE_LINK_STD_MIB.teLinkDescrMaxLspBandwidthPrio0,
'1.3.6.1.2.1.10.200.1.2.1.6': TE_LINK_STD_MIB.teLinkDescrMaxLspBandwidthPrio1,
'1.3.6.1.2.1.10.200.1.2.1.7': TE_LINK_STD_MIB.teLinkDescrMaxLspBandwidthPrio2,
'1.3.6.1.2.1.10.200.1.2.1.8': TE_LINK_STD_MIB.teLinkDescrMaxLspBandwidthPrio3,
'1.3.6.1.2.1.10.200.1.2.1.9': TE_LINK_STD_MIB.teLinkDescrMaxLspBandwidthPrio4,
'1.3.6.1.2.1.10.200.1.2.1.10': TE_LINK_STD_MIB.teLinkDescrMaxLspBandwidthPrio5,
'1.3.6.1.2.1.10.200.1.2.1.11': TE_LINK_STD_MIB.teLinkDescrMaxLspBandwidthPrio6,
'1.3.6.1.2.1.10.200.1.2.1.12': TE_LINK_STD_MIB.teLinkDescrMaxLspBandwidthPrio7,
'1.3.6.1.2.1.10.200.1.2.1.13': TE_LINK_STD_MIB.teLinkDescrInterfaceMtu,
'1.3.6.1.2.1.10.200.1.2.1.14': TE_LINK_STD_MIB.teLinkDescrIndication,
'1.3.6.1.2.1.10.200.1.2.1.15': TE_LINK_STD_MIB.teLinkDescrRowStatus,
'1.3.6.1.2.1.10.200.1.2.1.16': TE_LINK_STD_MIB.teLinkDescrStorageType,
'1.3.6.1.2.1.10.200.1.3.1.1': TE_LINK_STD_MIB.teLinkSrlg,
'1.3.6.1.2.1.10.200.1.3.1.2': TE_LINK_STD_MIB.teLinkSrlgRowStatus,
'1.3.6.1.2.1.10.200.1.3.1.3': TE_LINK_STD_MIB.teLinkSrlgStorageType,
'1.3.6.1.2.1.10.200.1.4.1.1': TE_LINK_STD_MIB.teLinkBandwidthPriority,
'1.3.6.1.2.1.10.200.1.4.1.2': TE_LINK_STD_MIB.teLinkBandwidthUnreserved,
'1.3.6.1.2.1.10.200.1.4.1.3': TE_LINK_STD_MIB.teLinkBandwidthRowStatus,
'1.3.6.1.2.1.10.200.1.4.1.4': TE_LINK_STD_MIB.teLinkBandwidthStorageType,
'1.3.6.1.2.1.10.200.1.5.1.1': TE_LINK_STD_MIB.componentLinkMaxResBandwidth,
'1.3.6.1.2.1.10.200.1.5.1.2': TE_LINK_STD_MIB.componentLinkPreferredProtection,
'1.3.6.1.2.1.10.200.1.5.1.3': TE_LINK_STD_MIB.componentLinkCurrentProtection,
'1.3.6.1.2.1.10.200.1.5.1.4': TE_LINK_STD_MIB.componentLinkRowStatus,
'1.3.6.1.2.1.10.200.1.5.1.5': TE_LINK_STD_MIB.componentLinkStorageType,
'1.3.6.1.2.1.10.200.1.6.1.1': TE_LINK_STD_MIB.componentLinkDescrId,
'1.3.6.1.2.1.10.200.1.6.1.2': TE_LINK_STD_MIB.componentLinkDescrSwitchingCapability,
'1.3.6.1.2.1.10.200.1.6.1.3': TE_LINK_STD_MIB.componentLinkDescrEncodingType,
'1.3.6.1.2.1.10.200.1.6.1.4': TE_LINK_STD_MIB.componentLinkDescrMinLspBandwidth,
'1.3.6.1.2.1.10.200.1.6.1.5': TE_LINK_STD_MIB.componentLinkDescrMaxLspBandwidthPrio0,
'1.3.6.1.2.1.10.200.1.6.1.6': TE_LINK_STD_MIB.componentLinkDescrMaxLspBandwidthPrio1,
'1.3.6.1.2.1.10.200.1.6.1.7': TE_LINK_STD_MIB.componentLinkDescrMaxLspBandwidthPrio2,
'1.3.6.1.2.1.10.200.1.6.1.8': TE_LINK_STD_MIB.componentLinkDescrMaxLspBandwidthPrio3,
'1.3.6.1.2.1.10.200.1.6.1.9': TE_LINK_STD_MIB.componentLinkDescrMaxLspBandwidthPrio4,
'1.3.6.1.2.1.10.200.1.6.1.10': TE_LINK_STD_MIB.componentLinkDescrMaxLspBandwidthPrio5,
'1.3.6.1.2.1.10.200.1.6.1.11': TE_LINK_STD_MIB.componentLinkDescrMaxLspBandwidthPrio6,
'1.3.6.1.2.1.10.200.1.6.1.12': TE_LINK_STD_MIB.componentLinkDescrMaxLspBandwidthPrio7,
'1.3.6.1.2.1.10.200.1.6.1.13': TE_LINK_STD_MIB.componentLinkDescrInterfaceMtu,
'1.3.6.1.2.1.10.200.1.6.1.14': TE_LINK_STD_MIB.componentLinkDescrIndication,
'1.3.6.1.2.1.10.200.1.6.1.15': TE_LINK_STD_MIB.componentLinkDescrRowStatus,
'1.3.6.1.2.1.10.200.1.6.1.16': TE_LINK_STD_MIB.componentLinkDescrStorageType,
'1.3.6.1.2.1.10.200.1.7.1.1': TE_LINK_STD_MIB.componentLinkBandwidthPriority,
'1.3.6.1.2.1.10.200.1.7.1.2': TE_LINK_STD_MIB.componentLinkBandwidthUnreserved,
'1.3.6.1.2.1.10.200.1.7.1.3': TE_LINK_STD_MIB.componentLinkBandwidthRowStatus,
'1.3.6.1.2.1.10.200.1.7.1.4': TE_LINK_STD_MIB.componentLinkBandwidthStorageType,
'1.3.6.1.2.1.10.200.2.2.1': TE_LINK_STD_MIB.teLinkGroup,
'1.3.6.1.2.1.10.200.2.2.2': TE_LINK_STD_MIB.teLinkSrlgGroup,
'1.3.6.1.2.1.10.200.2.2.3': TE_LINK_STD_MIB.teLinkBandwidthGroup,
'1.3.6.1.2.1.10.200.2.2.4': TE_LINK_STD_MIB.componentLinkBandwidthGroup,
'1.3.6.1.2.1.10.200.2.2.5': TE_LINK_STD_MIB.teLinkPscGroup,
'1.3.6.1.2.1.10.200.2.2.6': TE_LINK_STD_MIB.teLinkTdmGroup,
}
