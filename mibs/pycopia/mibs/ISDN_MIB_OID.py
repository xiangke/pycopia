# python
# This file is generated by a program (mib2py). 

import ISDN_MIB

OIDMAP = {
'1.3.6.1.2.1.10.20': ISDN_MIB.isdnMib,
'1.3.6.1.2.1.10.20.1': ISDN_MIB.isdnMibObjects,
'1.3.6.1.2.1.10.20.1.1': ISDN_MIB.isdnBasicRateGroup,
'1.3.6.1.2.1.10.20.1.2': ISDN_MIB.isdnBearerGroup,
'1.3.6.1.2.1.10.20.1.3': ISDN_MIB.isdnSignalingGroup,
'1.3.6.1.2.1.10.20.1.4': ISDN_MIB.isdnEndpointGroup,
'1.3.6.1.2.1.10.20.1.5': ISDN_MIB.isdnDirectoryGroup,
'1.3.6.1.2.1.10.20.2': ISDN_MIB.isdnMibTrapPrefix,
'1.3.6.1.2.1.10.20.2.0': ISDN_MIB.isdnMibTraps,
'1.3.6.1.2.1.10.20.2.1': ISDN_MIB.isdnMibCompliances,
'1.3.6.1.2.1.10.20.2.2': ISDN_MIB.isdnMibGroups,
'1.3.6.1.2.1.10.20.1.3.1': ISDN_MIB.isdnSignalingGetIndex,
'1.3.6.1.2.1.10.20.1.4.1': ISDN_MIB.isdnEndpointGetIndex,
'1.3.6.1.2.1.10.20.1.1.1.1.1': ISDN_MIB.isdnBasicRateIfType,
'1.3.6.1.2.1.10.20.1.1.1.1.2': ISDN_MIB.isdnBasicRateLineTopology,
'1.3.6.1.2.1.10.20.1.1.1.1.3': ISDN_MIB.isdnBasicRateIfMode,
'1.3.6.1.2.1.10.20.1.1.1.1.4': ISDN_MIB.isdnBasicRateSignalMode,
'1.3.6.1.2.1.10.20.1.2.1.1.1': ISDN_MIB.isdnBearerChannelType,
'1.3.6.1.2.1.10.20.1.2.1.1.2': ISDN_MIB.isdnBearerOperStatus,
'1.3.6.1.2.1.10.20.1.2.1.1.3': ISDN_MIB.isdnBearerChannelNumber,
'1.3.6.1.2.1.10.20.1.2.1.1.4': ISDN_MIB.isdnBearerPeerAddress,
'1.3.6.1.2.1.10.20.1.2.1.1.5': ISDN_MIB.isdnBearerPeerSubAddress,
'1.3.6.1.2.1.10.20.1.2.1.1.6': ISDN_MIB.isdnBearerCallOrigin,
'1.3.6.1.2.1.10.20.1.2.1.1.7': ISDN_MIB.isdnBearerInfoType,
'1.3.6.1.2.1.10.20.1.2.1.1.8': ISDN_MIB.isdnBearerMultirate,
'1.3.6.1.2.1.10.20.1.2.1.1.9': ISDN_MIB.isdnBearerCallSetupTime,
'1.3.6.1.2.1.10.20.1.2.1.1.10': ISDN_MIB.isdnBearerCallConnectTime,
'1.3.6.1.2.1.10.20.1.2.1.1.11': ISDN_MIB.isdnBearerChargedUnits,
'1.3.6.1.2.1.10.20.1.3.2.1.1': ISDN_MIB.isdnSignalingIndex,
'1.3.6.1.2.1.10.20.1.3.2.1.2': ISDN_MIB.isdnSignalingIfIndex,
'1.3.6.1.2.1.10.20.1.3.2.1.3': ISDN_MIB.isdnSignalingProtocol,
'1.3.6.1.2.1.10.20.1.3.2.1.4': ISDN_MIB.isdnSignalingCallingAddress,
'1.3.6.1.2.1.10.20.1.3.2.1.5': ISDN_MIB.isdnSignalingSubAddress,
'1.3.6.1.2.1.10.20.1.3.2.1.6': ISDN_MIB.isdnSignalingBchannelCount,
'1.3.6.1.2.1.10.20.1.3.2.1.7': ISDN_MIB.isdnSignalingInfoTrapEnable,
'1.3.6.1.2.1.10.20.1.3.2.1.8': ISDN_MIB.isdnSignalingStatus,
'1.3.6.1.2.1.10.20.1.3.3.1.1': ISDN_MIB.isdnSigStatsInCalls,
'1.3.6.1.2.1.10.20.1.3.3.1.2': ISDN_MIB.isdnSigStatsInConnected,
'1.3.6.1.2.1.10.20.1.3.3.1.3': ISDN_MIB.isdnSigStatsOutCalls,
'1.3.6.1.2.1.10.20.1.3.3.1.4': ISDN_MIB.isdnSigStatsOutConnected,
'1.3.6.1.2.1.10.20.1.3.3.1.5': ISDN_MIB.isdnSigStatsChargedUnits,
'1.3.6.1.2.1.10.20.1.3.4.1.1': ISDN_MIB.isdnLapdPrimaryChannel,
'1.3.6.1.2.1.10.20.1.3.4.1.2': ISDN_MIB.isdnLapdOperStatus,
'1.3.6.1.2.1.10.20.1.3.4.1.3': ISDN_MIB.isdnLapdPeerSabme,
'1.3.6.1.2.1.10.20.1.3.4.1.4': ISDN_MIB.isdnLapdRecvdFrmr,
'1.3.6.1.2.1.10.20.1.4.2.1.1': ISDN_MIB.isdnEndpointIndex,
'1.3.6.1.2.1.10.20.1.4.2.1.2': ISDN_MIB.isdnEndpointIfIndex,
'1.3.6.1.2.1.10.20.1.4.2.1.3': ISDN_MIB.isdnEndpointIfType,
'1.3.6.1.2.1.10.20.1.4.2.1.4': ISDN_MIB.isdnEndpointTeiType,
'1.3.6.1.2.1.10.20.1.4.2.1.5': ISDN_MIB.isdnEndpointTeiValue,
'1.3.6.1.2.1.10.20.1.4.2.1.6': ISDN_MIB.isdnEndpointSpid,
'1.3.6.1.2.1.10.20.1.4.2.1.7': ISDN_MIB.isdnEndpointStatus,
'1.3.6.1.2.1.10.20.1.5.1.1.1': ISDN_MIB.isdnDirectoryIndex,
'1.3.6.1.2.1.10.20.1.5.1.1.2': ISDN_MIB.isdnDirectoryNumber,
'1.3.6.1.2.1.10.20.1.5.1.1.3': ISDN_MIB.isdnDirectorySigIndex,
'1.3.6.1.2.1.10.20.1.5.1.1.4': ISDN_MIB.isdnDirectoryStatus,
'1.3.6.1.2.1.10.20.2.0.1': ISDN_MIB.isdnMibCallInformation,
'1.3.6.1.2.1.10.20.2.2.1': ISDN_MIB.isdnMibBasicRateGroup,
'1.3.6.1.2.1.10.20.2.2.2': ISDN_MIB.isdnMibBearerGroup,
'1.3.6.1.2.1.10.20.2.2.3': ISDN_MIB.isdnMibSignalingGroup,
'1.3.6.1.2.1.10.20.2.2.4': ISDN_MIB.isdnMibEndpointGroup,
'1.3.6.1.2.1.10.20.2.2.5': ISDN_MIB.isdnMibDirectoryGroup,
'1.3.6.1.2.1.10.20.2.2.6': ISDN_MIB.isdnMibNotificationsGroup,
}
