# python
# This file is generated by a program (mib2py). 

import DSMON_MIB

OIDMAP = {
'1.3.6.1.2.1.16.26': DSMON_MIB.dsmonMIB,
'1.3.6.1.2.1.16.26.1': DSMON_MIB.dsmonObjects,
'1.3.6.1.2.1.16.26.1.1': DSMON_MIB.dsmonAggObjects,
'1.3.6.1.2.1.16.26.1.2': DSMON_MIB.dsmonStatsObjects,
'1.3.6.1.2.1.16.26.1.3': DSMON_MIB.dsmonPdistObjects,
'1.3.6.1.2.1.16.26.1.4': DSMON_MIB.dsmonHostObjects,
'1.3.6.1.2.1.16.26.1.5': DSMON_MIB.dsmonCapsObjects,
'1.3.6.1.2.1.16.26.1.6': DSMON_MIB.dsmonMatrixObjects,
'1.3.6.1.2.1.16.26.2': DSMON_MIB.dsmonNotifications,
'1.3.6.1.2.1.16.26.3': DSMON_MIB.dsmonConformance,
'1.3.6.1.2.1.16.26.3.1': DSMON_MIB.dsmonCompliances,
'1.3.6.1.2.1.16.26.3.2': DSMON_MIB.dsmonGroups,
'1.3.6.1.2.1.16.26.1.1.1': DSMON_MIB.dsmonMaxAggGroups,
'1.3.6.1.2.1.16.26.1.1.2': DSMON_MIB.dsmonAggControlLocked,
'1.3.6.1.2.1.16.26.1.1.3': DSMON_MIB.dsmonAggControlChanges,
'1.3.6.1.2.1.16.26.1.1.4': DSMON_MIB.dsmonAggControlLastChangeTime,
'1.3.6.1.2.1.16.26.1.5.1': DSMON_MIB.dsmonCapabilities,
'1.3.6.1.2.1.16.26.1.1.5.1.1': DSMON_MIB.dsmonAggControlIndex,
'1.3.6.1.2.1.16.26.1.1.5.1.2': DSMON_MIB.dsmonAggControlDescr,
'1.3.6.1.2.1.16.26.1.1.5.1.3': DSMON_MIB.dsmonAggControlOwner,
'1.3.6.1.2.1.16.26.1.1.5.1.4': DSMON_MIB.dsmonAggControlStatus,
'1.3.6.1.2.1.16.26.1.1.6.1.1': DSMON_MIB.dsmonAggProfileDSCP,
'1.3.6.1.2.1.16.26.1.1.6.1.2': DSMON_MIB.dsmonAggGroupIndex,
'1.3.6.1.2.1.16.26.1.1.7.1.1': DSMON_MIB.dsmonAggGroupDescr,
'1.3.6.1.2.1.16.26.1.1.7.1.2': DSMON_MIB.dsmonAggGroupStatus,
'1.3.6.1.2.1.16.26.1.2.1.1.1': DSMON_MIB.dsmonStatsControlIndex,
'1.3.6.1.2.1.16.26.1.2.1.1.2': DSMON_MIB.dsmonStatsControlDataSource,
'1.3.6.1.2.1.16.26.1.2.1.1.3': DSMON_MIB.dsmonStatsControlAggProfile,
'1.3.6.1.2.1.16.26.1.2.1.1.4': DSMON_MIB.dsmonStatsControlDroppedFrames,
'1.3.6.1.2.1.16.26.1.2.1.1.5': DSMON_MIB.dsmonStatsControlCreateTime,
'1.3.6.1.2.1.16.26.1.2.1.1.6': DSMON_MIB.dsmonStatsControlOwner,
'1.3.6.1.2.1.16.26.1.2.1.1.7': DSMON_MIB.dsmonStatsControlStatus,
'1.3.6.1.2.1.16.26.1.2.2.1.1': DSMON_MIB.dsmonStatsInPkts,
'1.3.6.1.2.1.16.26.1.2.2.1.2': DSMON_MIB.dsmonStatsInOctets,
'1.3.6.1.2.1.16.26.1.2.2.1.3': DSMON_MIB.dsmonStatsInOvflPkts,
'1.3.6.1.2.1.16.26.1.2.2.1.4': DSMON_MIB.dsmonStatsInOvflOctets,
'1.3.6.1.2.1.16.26.1.2.2.1.5': DSMON_MIB.dsmonStatsInHCPkts,
'1.3.6.1.2.1.16.26.1.2.2.1.6': DSMON_MIB.dsmonStatsInHCOctets,
'1.3.6.1.2.1.16.26.1.2.2.1.7': DSMON_MIB.dsmonStatsOutPkts,
'1.3.6.1.2.1.16.26.1.2.2.1.8': DSMON_MIB.dsmonStatsOutOctets,
'1.3.6.1.2.1.16.26.1.2.2.1.9': DSMON_MIB.dsmonStatsOutOvflPkts,
'1.3.6.1.2.1.16.26.1.2.2.1.10': DSMON_MIB.dsmonStatsOutOvflOctets,
'1.3.6.1.2.1.16.26.1.2.2.1.11': DSMON_MIB.dsmonStatsOutHCPkts,
'1.3.6.1.2.1.16.26.1.2.2.1.12': DSMON_MIB.dsmonStatsOutHCOctets,
'1.3.6.1.2.1.16.26.1.3.1.1.1': DSMON_MIB.dsmonPdistCtlIndex,
'1.3.6.1.2.1.16.26.1.3.1.1.2': DSMON_MIB.dsmonPdistCtlDataSource,
'1.3.6.1.2.1.16.26.1.3.1.1.3': DSMON_MIB.dsmonPdistCtlAggProfile,
'1.3.6.1.2.1.16.26.1.3.1.1.4': DSMON_MIB.dsmonPdistCtlMaxDesiredEntries,
'1.3.6.1.2.1.16.26.1.3.1.1.5': DSMON_MIB.dsmonPdistCtlDroppedFrames,
'1.3.6.1.2.1.16.26.1.3.1.1.6': DSMON_MIB.dsmonPdistCtlInserts,
'1.3.6.1.2.1.16.26.1.3.1.1.7': DSMON_MIB.dsmonPdistCtlDeletes,
'1.3.6.1.2.1.16.26.1.3.1.1.8': DSMON_MIB.dsmonPdistCtlCreateTime,
'1.3.6.1.2.1.16.26.1.3.1.1.9': DSMON_MIB.dsmonPdistCtlOwner,
'1.3.6.1.2.1.16.26.1.3.1.1.10': DSMON_MIB.dsmonPdistCtlStatus,
'1.3.6.1.2.1.16.26.1.3.2.1.1': DSMON_MIB.dsmonPdistTimeMark,
'1.3.6.1.2.1.16.26.1.3.2.1.2': DSMON_MIB.dsmonPdistStatsPkts,
'1.3.6.1.2.1.16.26.1.3.2.1.3': DSMON_MIB.dsmonPdistStatsOctets,
'1.3.6.1.2.1.16.26.1.3.2.1.4': DSMON_MIB.dsmonPdistStatsOvflPkts,
'1.3.6.1.2.1.16.26.1.3.2.1.5': DSMON_MIB.dsmonPdistStatsOvflOctets,
'1.3.6.1.2.1.16.26.1.3.2.1.6': DSMON_MIB.dsmonPdistStatsHCPkts,
'1.3.6.1.2.1.16.26.1.3.2.1.7': DSMON_MIB.dsmonPdistStatsHCOctets,
'1.3.6.1.2.1.16.26.1.3.2.1.8': DSMON_MIB.dsmonPdistStatsCreateTime,
'1.3.6.1.2.1.16.26.1.3.3.1.1': DSMON_MIB.dsmonPdistTopNCtlIndex,
'1.3.6.1.2.1.16.26.1.3.3.1.2': DSMON_MIB.dsmonPdistTopNCtlPdistIndex,
'1.3.6.1.2.1.16.26.1.3.3.1.3': DSMON_MIB.dsmonPdistTopNCtlRateBase,
'1.3.6.1.2.1.16.26.1.3.3.1.4': DSMON_MIB.dsmonPdistTopNCtlTimeRemaining,
'1.3.6.1.2.1.16.26.1.3.3.1.5': DSMON_MIB.dsmonPdistTopNCtlGeneratedReprts,
'1.3.6.1.2.1.16.26.1.3.3.1.6': DSMON_MIB.dsmonPdistTopNCtlDuration,
'1.3.6.1.2.1.16.26.1.3.3.1.7': DSMON_MIB.dsmonPdistTopNCtlRequestedSize,
'1.3.6.1.2.1.16.26.1.3.3.1.8': DSMON_MIB.dsmonPdistTopNCtlGrantedSize,
'1.3.6.1.2.1.16.26.1.3.3.1.9': DSMON_MIB.dsmonPdistTopNCtlStartTime,
'1.3.6.1.2.1.16.26.1.3.3.1.10': DSMON_MIB.dsmonPdistTopNCtlOwner,
'1.3.6.1.2.1.16.26.1.3.3.1.11': DSMON_MIB.dsmonPdistTopNCtlStatus,
'1.3.6.1.2.1.16.26.1.3.4.1.1': DSMON_MIB.dsmonPdistTopNIndex,
'1.3.6.1.2.1.16.26.1.3.4.1.2': DSMON_MIB.dsmonPdistTopNPDLocalIndex,
'1.3.6.1.2.1.16.26.1.3.4.1.3': DSMON_MIB.dsmonPdistTopNAggGroup,
'1.3.6.1.2.1.16.26.1.3.4.1.4': DSMON_MIB.dsmonPdistTopNRate,
'1.3.6.1.2.1.16.26.1.3.4.1.5': DSMON_MIB.dsmonPdistTopNRateOvfl,
'1.3.6.1.2.1.16.26.1.3.4.1.6': DSMON_MIB.dsmonPdistTopNHCRate,
'1.3.6.1.2.1.16.26.1.4.1.1.1': DSMON_MIB.dsmonHostCtlIndex,
'1.3.6.1.2.1.16.26.1.4.1.1.2': DSMON_MIB.dsmonHostCtlDataSource,
'1.3.6.1.2.1.16.26.1.4.1.1.3': DSMON_MIB.dsmonHostCtlAggProfile,
'1.3.6.1.2.1.16.26.1.4.1.1.4': DSMON_MIB.dsmonHostCtlMaxDesiredEntries,
'1.3.6.1.2.1.16.26.1.4.1.1.5': DSMON_MIB.dsmonHostCtlIPv4PrefixLen,
'1.3.6.1.2.1.16.26.1.4.1.1.6': DSMON_MIB.dsmonHostCtlIPv6PrefixLen,
'1.3.6.1.2.1.16.26.1.4.1.1.7': DSMON_MIB.dsmonHostCtlDroppedFrames,
'1.3.6.1.2.1.16.26.1.4.1.1.8': DSMON_MIB.dsmonHostCtlInserts,
'1.3.6.1.2.1.16.26.1.4.1.1.9': DSMON_MIB.dsmonHostCtlDeletes,
'1.3.6.1.2.1.16.26.1.4.1.1.10': DSMON_MIB.dsmonHostCtlCreateTime,
'1.3.6.1.2.1.16.26.1.4.1.1.11': DSMON_MIB.dsmonHostCtlOwner,
'1.3.6.1.2.1.16.26.1.4.1.1.12': DSMON_MIB.dsmonHostCtlStatus,
'1.3.6.1.2.1.16.26.1.4.2.1.1': DSMON_MIB.dsmonHostTimeMark,
'1.3.6.1.2.1.16.26.1.4.2.1.2': DSMON_MIB.dsmonHostAddress,
'1.3.6.1.2.1.16.26.1.4.2.1.3': DSMON_MIB.dsmonHostInPkts,
'1.3.6.1.2.1.16.26.1.4.2.1.4': DSMON_MIB.dsmonHostInOctets,
'1.3.6.1.2.1.16.26.1.4.2.1.5': DSMON_MIB.dsmonHostInOvflPkts,
'1.3.6.1.2.1.16.26.1.4.2.1.6': DSMON_MIB.dsmonHostInOvflOctets,
'1.3.6.1.2.1.16.26.1.4.2.1.7': DSMON_MIB.dsmonHostInHCPkts,
'1.3.6.1.2.1.16.26.1.4.2.1.8': DSMON_MIB.dsmonHostInHCOctets,
'1.3.6.1.2.1.16.26.1.4.2.1.9': DSMON_MIB.dsmonHostOutPkts,
'1.3.6.1.2.1.16.26.1.4.2.1.10': DSMON_MIB.dsmonHostOutOctets,
'1.3.6.1.2.1.16.26.1.4.2.1.11': DSMON_MIB.dsmonHostOutOvflPkts,
'1.3.6.1.2.1.16.26.1.4.2.1.12': DSMON_MIB.dsmonHostOutOvflOctets,
'1.3.6.1.2.1.16.26.1.4.2.1.13': DSMON_MIB.dsmonHostOutHCPkts,
'1.3.6.1.2.1.16.26.1.4.2.1.14': DSMON_MIB.dsmonHostOutHCOctets,
'1.3.6.1.2.1.16.26.1.4.2.1.15': DSMON_MIB.dsmonHostCreateTime,
'1.3.6.1.2.1.16.26.1.4.3.1.1': DSMON_MIB.dsmonHostTopNCtlIndex,
'1.3.6.1.2.1.16.26.1.4.3.1.2': DSMON_MIB.dsmonHostTopNCtlHostIndex,
'1.3.6.1.2.1.16.26.1.4.3.1.3': DSMON_MIB.dsmonHostTopNCtlRateBase,
'1.3.6.1.2.1.16.26.1.4.3.1.4': DSMON_MIB.dsmonHostTopNCtlTimeRemaining,
'1.3.6.1.2.1.16.26.1.4.3.1.5': DSMON_MIB.dsmonHostTopNCtlGeneratedReports,
'1.3.6.1.2.1.16.26.1.4.3.1.6': DSMON_MIB.dsmonHostTopNCtlDuration,
'1.3.6.1.2.1.16.26.1.4.3.1.7': DSMON_MIB.dsmonHostTopNCtlRequestedSize,
'1.3.6.1.2.1.16.26.1.4.3.1.8': DSMON_MIB.dsmonHostTopNCtlGrantedSize,
'1.3.6.1.2.1.16.26.1.4.3.1.9': DSMON_MIB.dsmonHostTopNCtlStartTime,
'1.3.6.1.2.1.16.26.1.4.3.1.10': DSMON_MIB.dsmonHostTopNCtlOwner,
'1.3.6.1.2.1.16.26.1.4.3.1.11': DSMON_MIB.dsmonHostTopNCtlStatus,
'1.3.6.1.2.1.16.26.1.4.4.1.1': DSMON_MIB.dsmonHostTopNIndex,
'1.3.6.1.2.1.16.26.1.4.4.1.2': DSMON_MIB.dsmonHostTopNPDLocalIndex,
'1.3.6.1.2.1.16.26.1.4.4.1.3': DSMON_MIB.dsmonHostTopNAddress,
'1.3.6.1.2.1.16.26.1.4.4.1.4': DSMON_MIB.dsmonHostTopNAggGroup,
'1.3.6.1.2.1.16.26.1.4.4.1.5': DSMON_MIB.dsmonHostTopNRate,
'1.3.6.1.2.1.16.26.1.4.4.1.6': DSMON_MIB.dsmonHostTopNRateOvfl,
'1.3.6.1.2.1.16.26.1.4.4.1.7': DSMON_MIB.dsmonHostTopNHCRate,
'1.3.6.1.2.1.16.26.1.6.1.1.1': DSMON_MIB.dsmonMatrixCtlIndex,
'1.3.6.1.2.1.16.26.1.6.1.1.2': DSMON_MIB.dsmonMatrixCtlDataSource,
'1.3.6.1.2.1.16.26.1.6.1.1.3': DSMON_MIB.dsmonMatrixCtlAggProfile,
'1.3.6.1.2.1.16.26.1.6.1.1.4': DSMON_MIB.dsmonMatrixCtlMaxDesiredEntries,
'1.3.6.1.2.1.16.26.1.6.1.1.5': DSMON_MIB.dsmonMatrixCtlDroppedFrames,
'1.3.6.1.2.1.16.26.1.6.1.1.6': DSMON_MIB.dsmonMatrixCtlInserts,
'1.3.6.1.2.1.16.26.1.6.1.1.7': DSMON_MIB.dsmonMatrixCtlDeletes,
'1.3.6.1.2.1.16.26.1.6.1.1.8': DSMON_MIB.dsmonMatrixCtlCreateTime,
'1.3.6.1.2.1.16.26.1.6.1.1.9': DSMON_MIB.dsmonMatrixCtlOwner,
'1.3.6.1.2.1.16.26.1.6.1.1.10': DSMON_MIB.dsmonMatrixCtlStatus,
'1.3.6.1.2.1.16.26.1.6.2.1.1': DSMON_MIB.dsmonMatrixTimeMark,
'1.3.6.1.2.1.16.26.1.6.2.1.2': DSMON_MIB.dsmonMatrixNLIndex,
'1.3.6.1.2.1.16.26.1.6.2.1.3': DSMON_MIB.dsmonMatrixSourceAddress,
'1.3.6.1.2.1.16.26.1.6.2.1.4': DSMON_MIB.dsmonMatrixDestAddress,
'1.3.6.1.2.1.16.26.1.6.2.1.5': DSMON_MIB.dsmonMatrixALIndex,
'1.3.6.1.2.1.16.26.1.6.2.1.6': DSMON_MIB.dsmonMatrixSDPkts,
'1.3.6.1.2.1.16.26.1.6.2.1.7': DSMON_MIB.dsmonMatrixSDOvflPkts,
'1.3.6.1.2.1.16.26.1.6.2.1.8': DSMON_MIB.dsmonMatrixSDHCPkts,
'1.3.6.1.2.1.16.26.1.6.2.1.9': DSMON_MIB.dsmonMatrixSDOctets,
'1.3.6.1.2.1.16.26.1.6.2.1.10': DSMON_MIB.dsmonMatrixSDOvflOctets,
'1.3.6.1.2.1.16.26.1.6.2.1.11': DSMON_MIB.dsmonMatrixSDHCOctets,
'1.3.6.1.2.1.16.26.1.6.2.1.12': DSMON_MIB.dsmonMatrixSDCreateTime,
'1.3.6.1.2.1.16.26.1.6.3.1.1': DSMON_MIB.dsmonMatrixDSPkts,
'1.3.6.1.2.1.16.26.1.6.3.1.2': DSMON_MIB.dsmonMatrixDSOvflPkts,
'1.3.6.1.2.1.16.26.1.6.3.1.3': DSMON_MIB.dsmonMatrixDSHCPkts,
'1.3.6.1.2.1.16.26.1.6.3.1.4': DSMON_MIB.dsmonMatrixDSOctets,
'1.3.6.1.2.1.16.26.1.6.3.1.5': DSMON_MIB.dsmonMatrixDSOvflOctets,
'1.3.6.1.2.1.16.26.1.6.3.1.6': DSMON_MIB.dsmonMatrixDSHCOctets,
'1.3.6.1.2.1.16.26.1.6.3.1.7': DSMON_MIB.dsmonMatrixDSCreateTime,
'1.3.6.1.2.1.16.26.1.6.4.1.1': DSMON_MIB.dsmonMatrixTopNCtlIndex,
'1.3.6.1.2.1.16.26.1.6.4.1.2': DSMON_MIB.dsmonMatrixTopNCtlMatrixIndex,
'1.3.6.1.2.1.16.26.1.6.4.1.3': DSMON_MIB.dsmonMatrixTopNCtlRateBase,
'1.3.6.1.2.1.16.26.1.6.4.1.4': DSMON_MIB.dsmonMatrixTopNCtlTimeRemaining,
'1.3.6.1.2.1.16.26.1.6.4.1.5': DSMON_MIB.dsmonMatrixTopNCtlGeneratedRpts,
'1.3.6.1.2.1.16.26.1.6.4.1.6': DSMON_MIB.dsmonMatrixTopNCtlDuration,
'1.3.6.1.2.1.16.26.1.6.4.1.7': DSMON_MIB.dsmonMatrixTopNCtlRequestedSize,
'1.3.6.1.2.1.16.26.1.6.4.1.8': DSMON_MIB.dsmonMatrixTopNCtlGrantedSize,
'1.3.6.1.2.1.16.26.1.6.4.1.9': DSMON_MIB.dsmonMatrixTopNCtlStartTime,
'1.3.6.1.2.1.16.26.1.6.4.1.10': DSMON_MIB.dsmonMatrixTopNCtlOwner,
'1.3.6.1.2.1.16.26.1.6.4.1.11': DSMON_MIB.dsmonMatrixTopNCtlStatus,
'1.3.6.1.2.1.16.26.1.6.5.1.1': DSMON_MIB.dsmonMatrixTopNIndex,
'1.3.6.1.2.1.16.26.1.6.5.1.2': DSMON_MIB.dsmonMatrixTopNAggGroup,
'1.3.6.1.2.1.16.26.1.6.5.1.3': DSMON_MIB.dsmonMatrixTopNNLIndex,
'1.3.6.1.2.1.16.26.1.6.5.1.4': DSMON_MIB.dsmonMatrixTopNSourceAddress,
'1.3.6.1.2.1.16.26.1.6.5.1.5': DSMON_MIB.dsmonMatrixTopNDestAddress,
'1.3.6.1.2.1.16.26.1.6.5.1.6': DSMON_MIB.dsmonMatrixTopNALIndex,
'1.3.6.1.2.1.16.26.1.6.5.1.7': DSMON_MIB.dsmonMatrixTopNPktRate,
'1.3.6.1.2.1.16.26.1.6.5.1.8': DSMON_MIB.dsmonMatrixTopNPktRateOvfl,
'1.3.6.1.2.1.16.26.1.6.5.1.9': DSMON_MIB.dsmonMatrixTopNHCPktRate,
'1.3.6.1.2.1.16.26.1.6.5.1.10': DSMON_MIB.dsmonMatrixTopNRevPktRate,
'1.3.6.1.2.1.16.26.1.6.5.1.11': DSMON_MIB.dsmonMatrixTopNRevPktRateOvfl,
'1.3.6.1.2.1.16.26.1.6.5.1.12': DSMON_MIB.dsmonMatrixTopNHCRevPktRate,
'1.3.6.1.2.1.16.26.1.6.5.1.13': DSMON_MIB.dsmonMatrixTopNOctetRate,
'1.3.6.1.2.1.16.26.1.6.5.1.14': DSMON_MIB.dsmonMatrixTopNOctetRateOvfl,
'1.3.6.1.2.1.16.26.1.6.5.1.15': DSMON_MIB.dsmonMatrixTopNHCOctetRate,
'1.3.6.1.2.1.16.26.1.6.5.1.16': DSMON_MIB.dsmonMatrixTopNRevOctetRate,
'1.3.6.1.2.1.16.26.1.6.5.1.17': DSMON_MIB.dsmonMatrixTopNRevOctetRateOvfl,
'1.3.6.1.2.1.16.26.1.6.5.1.18': DSMON_MIB.dsmonMatrixTopNHCRevOctetRate,
'1.3.6.1.2.1.16.26.3.2.1': DSMON_MIB.dsmonCounterAggControlGroup,
'1.3.6.1.2.1.16.26.3.2.2': DSMON_MIB.dsmonStatsGroup,
'1.3.6.1.2.1.16.26.3.2.3': DSMON_MIB.dsmonStatsOvflGroup,
'1.3.6.1.2.1.16.26.3.2.4': DSMON_MIB.dsmonStatsHCGroup,
'1.3.6.1.2.1.16.26.3.2.5': DSMON_MIB.dsmonPdistGroup,
'1.3.6.1.2.1.16.26.3.2.6': DSMON_MIB.dsmonPdistOvflGroup,
'1.3.6.1.2.1.16.26.3.2.7': DSMON_MIB.dsmonPdistHCGroup,
'1.3.6.1.2.1.16.26.3.2.8': DSMON_MIB.dsmonHostGroup,
'1.3.6.1.2.1.16.26.3.2.9': DSMON_MIB.dsmonHostOvflGroup,
'1.3.6.1.2.1.16.26.3.2.10': DSMON_MIB.dsmonHostHCGroup,
'1.3.6.1.2.1.16.26.3.2.11': DSMON_MIB.dsmonCapsGroup,
'1.3.6.1.2.1.16.26.3.2.12': DSMON_MIB.dsmonMatrixGroup,
'1.3.6.1.2.1.16.26.3.2.13': DSMON_MIB.dsmonMatrixOvflGroup,
'1.3.6.1.2.1.16.26.3.2.14': DSMON_MIB.dsmonMatrixHCGroup,
}
