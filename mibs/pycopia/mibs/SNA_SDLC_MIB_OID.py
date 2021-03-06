# python
# This file is generated by a program (mib2py). 

import SNA_SDLC_MIB

OIDMAP = {
'1.3.6.1.2.1.41': SNA_SDLC_MIB.snaDLC,
'1.3.6.1.2.1.41.1': SNA_SDLC_MIB.sdlc,
'1.3.6.1.2.1.41.1.1': SNA_SDLC_MIB.sdlcPortGroup,
'1.3.6.1.2.1.41.1.2': SNA_SDLC_MIB.sdlcLSGroup,
'1.3.6.1.2.1.41.1.3': SNA_SDLC_MIB.sdlcTraps,
'1.3.6.1.2.1.41.1.4': SNA_SDLC_MIB.sdlcConformance,
'1.3.6.1.2.1.41.1.4.1': SNA_SDLC_MIB.sdlcCompliances,
'1.3.6.1.2.1.41.1.4.2': SNA_SDLC_MIB.sdlcGroups,
'1.3.6.1.2.1.41.1.4.2.1': SNA_SDLC_MIB.sdlcCoreGroups,
'1.3.6.1.2.1.41.1.4.2.2': SNA_SDLC_MIB.sdlcPrimaryGroups,
'1.3.6.1.2.1.41.1.1.1.1.1': SNA_SDLC_MIB.sdlcPortAdminName,
'1.3.6.1.2.1.41.1.1.1.1.2': SNA_SDLC_MIB.sdlcPortAdminRole,
'1.3.6.1.2.1.41.1.1.1.1.3': SNA_SDLC_MIB.sdlcPortAdminType,
'1.3.6.1.2.1.41.1.1.1.1.4': SNA_SDLC_MIB.sdlcPortAdminTopology,
'1.3.6.1.2.1.41.1.1.1.1.5': SNA_SDLC_MIB.sdlcPortAdminISTATUS,
'1.3.6.1.2.1.41.1.1.1.1.6': SNA_SDLC_MIB.sdlcPortAdminACTIVTO,
'1.3.6.1.2.1.41.1.1.1.1.7': SNA_SDLC_MIB.sdlcPortAdminPAUSE,
'1.3.6.1.2.1.41.1.1.1.1.8': SNA_SDLC_MIB.sdlcPortAdminSERVLIM,
'1.3.6.1.2.1.41.1.1.1.1.9': SNA_SDLC_MIB.sdlcPortAdminSlowPollTimer,
'1.3.6.1.2.1.41.1.1.2.1.1': SNA_SDLC_MIB.sdlcPortOperName,
'1.3.6.1.2.1.41.1.1.2.1.2': SNA_SDLC_MIB.sdlcPortOperRole,
'1.3.6.1.2.1.41.1.1.2.1.3': SNA_SDLC_MIB.sdlcPortOperType,
'1.3.6.1.2.1.41.1.1.2.1.4': SNA_SDLC_MIB.sdlcPortOperTopology,
'1.3.6.1.2.1.41.1.1.2.1.5': SNA_SDLC_MIB.sdlcPortOperISTATUS,
'1.3.6.1.2.1.41.1.1.2.1.6': SNA_SDLC_MIB.sdlcPortOperACTIVTO,
'1.3.6.1.2.1.41.1.1.2.1.7': SNA_SDLC_MIB.sdlcPortOperPAUSE,
'1.3.6.1.2.1.41.1.1.2.1.8': SNA_SDLC_MIB.sdlcPortOperSlowPollMethod,
'1.3.6.1.2.1.41.1.1.2.1.9': SNA_SDLC_MIB.sdlcPortOperSERVLIM,
'1.3.6.1.2.1.41.1.1.2.1.10': SNA_SDLC_MIB.sdlcPortOperSlowPollTimer,
'1.3.6.1.2.1.41.1.1.2.1.11': SNA_SDLC_MIB.sdlcPortOperLastModifyTime,
'1.3.6.1.2.1.41.1.1.2.1.12': SNA_SDLC_MIB.sdlcPortOperLastFailTime,
'1.3.6.1.2.1.41.1.1.2.1.13': SNA_SDLC_MIB.sdlcPortOperLastFailCause,
'1.3.6.1.2.1.41.1.1.3.1.1': SNA_SDLC_MIB.sdlcPortStatsPhysicalFailures,
'1.3.6.1.2.1.41.1.1.3.1.2': SNA_SDLC_MIB.sdlcPortStatsInvalidAddresses,
'1.3.6.1.2.1.41.1.1.3.1.3': SNA_SDLC_MIB.sdlcPortStatsDwarfFrames,
'1.3.6.1.2.1.41.1.1.3.1.4': SNA_SDLC_MIB.sdlcPortStatsPollsIn,
'1.3.6.1.2.1.41.1.1.3.1.5': SNA_SDLC_MIB.sdlcPortStatsPollsOut,
'1.3.6.1.2.1.41.1.1.3.1.6': SNA_SDLC_MIB.sdlcPortStatsPollRspsIn,
'1.3.6.1.2.1.41.1.1.3.1.7': SNA_SDLC_MIB.sdlcPortStatsPollRspsOut,
'1.3.6.1.2.1.41.1.1.3.1.8': SNA_SDLC_MIB.sdlcPortStatsLocalBusies,
'1.3.6.1.2.1.41.1.1.3.1.9': SNA_SDLC_MIB.sdlcPortStatsRemoteBusies,
'1.3.6.1.2.1.41.1.1.3.1.10': SNA_SDLC_MIB.sdlcPortStatsIFramesIn,
'1.3.6.1.2.1.41.1.1.3.1.11': SNA_SDLC_MIB.sdlcPortStatsIFramesOut,
'1.3.6.1.2.1.41.1.1.3.1.12': SNA_SDLC_MIB.sdlcPortStatsOctetsIn,
'1.3.6.1.2.1.41.1.1.3.1.13': SNA_SDLC_MIB.sdlcPortStatsOctetsOut,
'1.3.6.1.2.1.41.1.1.3.1.14': SNA_SDLC_MIB.sdlcPortStatsProtocolErrs,
'1.3.6.1.2.1.41.1.1.3.1.15': SNA_SDLC_MIB.sdlcPortStatsActivityTOs,
'1.3.6.1.2.1.41.1.1.3.1.16': SNA_SDLC_MIB.sdlcPortStatsRNRLIMITs,
'1.3.6.1.2.1.41.1.1.3.1.17': SNA_SDLC_MIB.sdlcPortStatsRetriesExps,
'1.3.6.1.2.1.41.1.1.3.1.18': SNA_SDLC_MIB.sdlcPortStatsRetransmitsIn,
'1.3.6.1.2.1.41.1.1.3.1.19': SNA_SDLC_MIB.sdlcPortStatsRetransmitsOut,
'1.3.6.1.2.1.41.1.2.1.1.1': SNA_SDLC_MIB.sdlcLSAddress,
'1.3.6.1.2.1.41.1.2.1.1.2': SNA_SDLC_MIB.sdlcLSAdminName,
'1.3.6.1.2.1.41.1.2.1.1.3': SNA_SDLC_MIB.sdlcLSAdminState,
'1.3.6.1.2.1.41.1.2.1.1.4': SNA_SDLC_MIB.sdlcLSAdminISTATUS,
'1.3.6.1.2.1.41.1.2.1.1.5': SNA_SDLC_MIB.sdlcLSAdminMAXDATASend,
'1.3.6.1.2.1.41.1.2.1.1.6': SNA_SDLC_MIB.sdlcLSAdminMAXDATARcv,
'1.3.6.1.2.1.41.1.2.1.1.7': SNA_SDLC_MIB.sdlcLSAdminREPLYTO,
'1.3.6.1.2.1.41.1.2.1.1.8': SNA_SDLC_MIB.sdlcLSAdminMAXIN,
'1.3.6.1.2.1.41.1.2.1.1.9': SNA_SDLC_MIB.sdlcLSAdminMAXOUT,
'1.3.6.1.2.1.41.1.2.1.1.10': SNA_SDLC_MIB.sdlcLSAdminMODULO,
'1.3.6.1.2.1.41.1.2.1.1.11': SNA_SDLC_MIB.sdlcLSAdminRETRIESm,
'1.3.6.1.2.1.41.1.2.1.1.12': SNA_SDLC_MIB.sdlcLSAdminRETRIESt,
'1.3.6.1.2.1.41.1.2.1.1.13': SNA_SDLC_MIB.sdlcLSAdminRETRIESn,
'1.3.6.1.2.1.41.1.2.1.1.14': SNA_SDLC_MIB.sdlcLSAdminRNRLIMIT,
'1.3.6.1.2.1.41.1.2.1.1.15': SNA_SDLC_MIB.sdlcLSAdminDATMODE,
'1.3.6.1.2.1.41.1.2.1.1.16': SNA_SDLC_MIB.sdlcLSAdminGPoll,
'1.3.6.1.2.1.41.1.2.1.1.17': SNA_SDLC_MIB.sdlcLSAdminSimRim,
'1.3.6.1.2.1.41.1.2.1.1.18': SNA_SDLC_MIB.sdlcLSAdminXmitRcvCap,
'1.3.6.1.2.1.41.1.2.1.1.19': SNA_SDLC_MIB.sdlcLSAdminRowStatus,
'1.3.6.1.2.1.41.1.2.2.1.1': SNA_SDLC_MIB.sdlcLSOperName,
'1.3.6.1.2.1.41.1.2.2.1.2': SNA_SDLC_MIB.sdlcLSOperRole,
'1.3.6.1.2.1.41.1.2.2.1.3': SNA_SDLC_MIB.sdlcLSOperState,
'1.3.6.1.2.1.41.1.2.2.1.4': SNA_SDLC_MIB.sdlcLSOperMAXDATASend,
'1.3.6.1.2.1.41.1.2.2.1.5': SNA_SDLC_MIB.sdlcLSOperREPLYTO,
'1.3.6.1.2.1.41.1.2.2.1.6': SNA_SDLC_MIB.sdlcLSOperMAXIN,
'1.3.6.1.2.1.41.1.2.2.1.7': SNA_SDLC_MIB.sdlcLSOperMAXOUT,
'1.3.6.1.2.1.41.1.2.2.1.8': SNA_SDLC_MIB.sdlcLSOperMODULO,
'1.3.6.1.2.1.41.1.2.2.1.9': SNA_SDLC_MIB.sdlcLSOperRETRIESm,
'1.3.6.1.2.1.41.1.2.2.1.10': SNA_SDLC_MIB.sdlcLSOperRETRIESt,
'1.3.6.1.2.1.41.1.2.2.1.11': SNA_SDLC_MIB.sdlcLSOperRETRIESn,
'1.3.6.1.2.1.41.1.2.2.1.12': SNA_SDLC_MIB.sdlcLSOperRNRLIMIT,
'1.3.6.1.2.1.41.1.2.2.1.13': SNA_SDLC_MIB.sdlcLSOperDATMODE,
'1.3.6.1.2.1.41.1.2.2.1.14': SNA_SDLC_MIB.sdlcLSOperLastModifyTime,
'1.3.6.1.2.1.41.1.2.2.1.15': SNA_SDLC_MIB.sdlcLSOperLastFailTime,
'1.3.6.1.2.1.41.1.2.2.1.16': SNA_SDLC_MIB.sdlcLSOperLastFailCause,
'1.3.6.1.2.1.41.1.2.2.1.17': SNA_SDLC_MIB.sdlcLSOperLastFailCtrlIn,
'1.3.6.1.2.1.41.1.2.2.1.18': SNA_SDLC_MIB.sdlcLSOperLastFailCtrlOut,
'1.3.6.1.2.1.41.1.2.2.1.19': SNA_SDLC_MIB.sdlcLSOperLastFailFRMRInfo,
'1.3.6.1.2.1.41.1.2.2.1.20': SNA_SDLC_MIB.sdlcLSOperLastFailREPLYTOs,
'1.3.6.1.2.1.41.1.2.2.1.21': SNA_SDLC_MIB.sdlcLSOperEcho,
'1.3.6.1.2.1.41.1.2.2.1.22': SNA_SDLC_MIB.sdlcLSOperGPoll,
'1.3.6.1.2.1.41.1.2.2.1.23': SNA_SDLC_MIB.sdlcLSOperSimRim,
'1.3.6.1.2.1.41.1.2.2.1.24': SNA_SDLC_MIB.sdlcLSOperXmitRcvCap,
'1.3.6.1.2.1.41.1.2.3.1.1': SNA_SDLC_MIB.sdlcLSStatsBLUsIn,
'1.3.6.1.2.1.41.1.2.3.1.2': SNA_SDLC_MIB.sdlcLSStatsBLUsOut,
'1.3.6.1.2.1.41.1.2.3.1.3': SNA_SDLC_MIB.sdlcLSStatsOctetsIn,
'1.3.6.1.2.1.41.1.2.3.1.4': SNA_SDLC_MIB.sdlcLSStatsOctetsOut,
'1.3.6.1.2.1.41.1.2.3.1.5': SNA_SDLC_MIB.sdlcLSStatsPollsIn,
'1.3.6.1.2.1.41.1.2.3.1.6': SNA_SDLC_MIB.sdlcLSStatsPollsOut,
'1.3.6.1.2.1.41.1.2.3.1.7': SNA_SDLC_MIB.sdlcLSStatsPollRspsOut,
'1.3.6.1.2.1.41.1.2.3.1.8': SNA_SDLC_MIB.sdlcLSStatsPollRspsIn,
'1.3.6.1.2.1.41.1.2.3.1.9': SNA_SDLC_MIB.sdlcLSStatsLocalBusies,
'1.3.6.1.2.1.41.1.2.3.1.10': SNA_SDLC_MIB.sdlcLSStatsRemoteBusies,
'1.3.6.1.2.1.41.1.2.3.1.11': SNA_SDLC_MIB.sdlcLSStatsIFramesIn,
'1.3.6.1.2.1.41.1.2.3.1.12': SNA_SDLC_MIB.sdlcLSStatsIFramesOut,
'1.3.6.1.2.1.41.1.2.3.1.13': SNA_SDLC_MIB.sdlcLSStatsUIFramesIn,
'1.3.6.1.2.1.41.1.2.3.1.14': SNA_SDLC_MIB.sdlcLSStatsUIFramesOut,
'1.3.6.1.2.1.41.1.2.3.1.15': SNA_SDLC_MIB.sdlcLSStatsXIDsIn,
'1.3.6.1.2.1.41.1.2.3.1.16': SNA_SDLC_MIB.sdlcLSStatsXIDsOut,
'1.3.6.1.2.1.41.1.2.3.1.17': SNA_SDLC_MIB.sdlcLSStatsTESTsIn,
'1.3.6.1.2.1.41.1.2.3.1.18': SNA_SDLC_MIB.sdlcLSStatsTESTsOut,
'1.3.6.1.2.1.41.1.2.3.1.19': SNA_SDLC_MIB.sdlcLSStatsREJsIn,
'1.3.6.1.2.1.41.1.2.3.1.20': SNA_SDLC_MIB.sdlcLSStatsREJsOut,
'1.3.6.1.2.1.41.1.2.3.1.21': SNA_SDLC_MIB.sdlcLSStatsFRMRsIn,
'1.3.6.1.2.1.41.1.2.3.1.22': SNA_SDLC_MIB.sdlcLSStatsFRMRsOut,
'1.3.6.1.2.1.41.1.2.3.1.23': SNA_SDLC_MIB.sdlcLSStatsSIMsIn,
'1.3.6.1.2.1.41.1.2.3.1.24': SNA_SDLC_MIB.sdlcLSStatsSIMsOut,
'1.3.6.1.2.1.41.1.2.3.1.25': SNA_SDLC_MIB.sdlcLSStatsRIMsIn,
'1.3.6.1.2.1.41.1.2.3.1.26': SNA_SDLC_MIB.sdlcLSStatsRIMsOut,
'1.3.6.1.2.1.41.1.2.3.1.27': SNA_SDLC_MIB.sdlcLSStatsDISCIn,
'1.3.6.1.2.1.41.1.2.3.1.28': SNA_SDLC_MIB.sdlcLSStatsDISCOut,
'1.3.6.1.2.1.41.1.2.3.1.29': SNA_SDLC_MIB.sdlcLSStatsUAIn,
'1.3.6.1.2.1.41.1.2.3.1.30': SNA_SDLC_MIB.sdlcLSStatsUAOut,
'1.3.6.1.2.1.41.1.2.3.1.31': SNA_SDLC_MIB.sdlcLSStatsDMIn,
'1.3.6.1.2.1.41.1.2.3.1.32': SNA_SDLC_MIB.sdlcLSStatsDMOut,
'1.3.6.1.2.1.41.1.2.3.1.33': SNA_SDLC_MIB.sdlcLSStatsSNRMIn,
'1.3.6.1.2.1.41.1.2.3.1.34': SNA_SDLC_MIB.sdlcLSStatsSNRMOut,
'1.3.6.1.2.1.41.1.2.3.1.35': SNA_SDLC_MIB.sdlcLSStatsProtocolErrs,
'1.3.6.1.2.1.41.1.2.3.1.36': SNA_SDLC_MIB.sdlcLSStatsActivityTOs,
'1.3.6.1.2.1.41.1.2.3.1.37': SNA_SDLC_MIB.sdlcLSStatsRNRLIMITs,
'1.3.6.1.2.1.41.1.2.3.1.38': SNA_SDLC_MIB.sdlcLSStatsRetriesExps,
'1.3.6.1.2.1.41.1.2.3.1.39': SNA_SDLC_MIB.sdlcLSStatsRetransmitsIn,
'1.3.6.1.2.1.41.1.2.3.1.40': SNA_SDLC_MIB.sdlcLSStatsRetransmitsOut,
'1.3.6.1.2.1.41.1.3.1': SNA_SDLC_MIB.sdlcPortStatusChange,
'1.3.6.1.2.1.41.1.3.2': SNA_SDLC_MIB.sdlcLSStatusChange,
'1.3.6.1.2.1.41.1.4.2.1.1': SNA_SDLC_MIB.sdlcCorePortAdminGroup,
'1.3.6.1.2.1.41.1.4.2.1.2': SNA_SDLC_MIB.sdlcCorePortOperGroup,
'1.3.6.1.2.1.41.1.4.2.1.3': SNA_SDLC_MIB.sdlcCorePortStatsGroup,
'1.3.6.1.2.1.41.1.4.2.1.4': SNA_SDLC_MIB.sdlcCoreLSAdminGroup,
'1.3.6.1.2.1.41.1.4.2.1.5': SNA_SDLC_MIB.sdlcCoreLSOperGroup,
'1.3.6.1.2.1.41.1.4.2.1.6': SNA_SDLC_MIB.sdlcCoreLSStatsGroup,
'1.3.6.1.2.1.41.1.4.2.2.1': SNA_SDLC_MIB.sdlcPrimaryGroup,
'1.3.6.1.2.1.41.1.4.2.2.2': SNA_SDLC_MIB.sdlcPrimaryMultipointGroup,
}
