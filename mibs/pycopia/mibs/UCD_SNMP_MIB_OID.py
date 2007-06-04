# python
# This file is generated by a program (mib2py). 

import UCD_SNMP_MIB

OIDMAP = {
'1.3.6.1.4.1.2021': UCD_SNMP_MIB.ucdavis,
'1.3.6.1.4.1.2021.4': UCD_SNMP_MIB.memory,
'1.3.6.1.4.1.2021.11': UCD_SNMP_MIB.systemStats,
'1.3.6.1.4.1.2021.12': UCD_SNMP_MIB.ucdInternal,
'1.3.6.1.4.1.2021.13': UCD_SNMP_MIB.ucdExperimental,
'1.3.6.1.4.1.2021.16': UCD_SNMP_MIB.logMatch,
'1.3.6.1.4.1.2021.100': UCD_SNMP_MIB.version,
'1.3.6.1.4.1.2021.101': UCD_SNMP_MIB.snmperrs,
'1.3.6.1.4.1.2021.250': UCD_SNMP_MIB.ucdSnmpAgent,
'1.3.6.1.4.1.2021.250.1': UCD_SNMP_MIB.hpux9,
'1.3.6.1.4.1.2021.250.2': UCD_SNMP_MIB.sunos4,
'1.3.6.1.4.1.2021.250.3': UCD_SNMP_MIB.solaris,
'1.3.6.1.4.1.2021.250.4': UCD_SNMP_MIB.osf,
'1.3.6.1.4.1.2021.250.5': UCD_SNMP_MIB.ultrix,
'1.3.6.1.4.1.2021.250.6': UCD_SNMP_MIB.hpux10,
'1.3.6.1.4.1.2021.250.7': UCD_SNMP_MIB.netbsd1,
'1.3.6.1.4.1.2021.250.8': UCD_SNMP_MIB.freebsd,
'1.3.6.1.4.1.2021.250.9': UCD_SNMP_MIB.irix,
'1.3.6.1.4.1.2021.250.10': UCD_SNMP_MIB.linux,
'1.3.6.1.4.1.2021.250.11': UCD_SNMP_MIB.bsdi,
'1.3.6.1.4.1.2021.250.12': UCD_SNMP_MIB.openbsd,
'1.3.6.1.4.1.2021.250.13': UCD_SNMP_MIB.win32,
'1.3.6.1.4.1.2021.250.14': UCD_SNMP_MIB.hpux11,
'1.3.6.1.4.1.2021.250.255': UCD_SNMP_MIB.unknown,
'1.3.6.1.4.1.2021.251': UCD_SNMP_MIB.ucdTraps,
'1.3.6.1.4.1.2021.4.1': UCD_SNMP_MIB.memIndex,
'1.3.6.1.4.1.2021.4.2': UCD_SNMP_MIB.memErrorName,
'1.3.6.1.4.1.2021.4.3': UCD_SNMP_MIB.memTotalSwap,
'1.3.6.1.4.1.2021.4.4': UCD_SNMP_MIB.memAvailSwap,
'1.3.6.1.4.1.2021.4.5': UCD_SNMP_MIB.memTotalReal,
'1.3.6.1.4.1.2021.4.6': UCD_SNMP_MIB.memAvailReal,
'1.3.6.1.4.1.2021.4.7': UCD_SNMP_MIB.memTotalSwapTXT,
'1.3.6.1.4.1.2021.4.8': UCD_SNMP_MIB.memAvailSwapTXT,
'1.3.6.1.4.1.2021.4.9': UCD_SNMP_MIB.memTotalRealTXT,
'1.3.6.1.4.1.2021.4.10': UCD_SNMP_MIB.memAvailRealTXT,
'1.3.6.1.4.1.2021.4.11': UCD_SNMP_MIB.memTotalFree,
'1.3.6.1.4.1.2021.4.12': UCD_SNMP_MIB.memMinimumSwap,
'1.3.6.1.4.1.2021.4.13': UCD_SNMP_MIB.memShared,
'1.3.6.1.4.1.2021.4.14': UCD_SNMP_MIB.memBuffer,
'1.3.6.1.4.1.2021.4.15': UCD_SNMP_MIB.memCached,
'1.3.6.1.4.1.2021.4.100': UCD_SNMP_MIB.memSwapError,
'1.3.6.1.4.1.2021.4.101': UCD_SNMP_MIB.memSwapErrorMsg,
'1.3.6.1.4.1.2021.11.1': UCD_SNMP_MIB.ssIndex,
'1.3.6.1.4.1.2021.11.2': UCD_SNMP_MIB.ssErrorName,
'1.3.6.1.4.1.2021.11.3': UCD_SNMP_MIB.ssSwapIn,
'1.3.6.1.4.1.2021.11.4': UCD_SNMP_MIB.ssSwapOut,
'1.3.6.1.4.1.2021.11.5': UCD_SNMP_MIB.ssIOSent,
'1.3.6.1.4.1.2021.11.6': UCD_SNMP_MIB.ssIOReceive,
'1.3.6.1.4.1.2021.11.7': UCD_SNMP_MIB.ssSysInterrupts,
'1.3.6.1.4.1.2021.11.8': UCD_SNMP_MIB.ssSysContext,
'1.3.6.1.4.1.2021.11.9': UCD_SNMP_MIB.ssCpuUser,
'1.3.6.1.4.1.2021.11.10': UCD_SNMP_MIB.ssCpuSystem,
'1.3.6.1.4.1.2021.11.11': UCD_SNMP_MIB.ssCpuIdle,
'1.3.6.1.4.1.2021.11.50': UCD_SNMP_MIB.ssCpuRawUser,
'1.3.6.1.4.1.2021.11.51': UCD_SNMP_MIB.ssCpuRawNice,
'1.3.6.1.4.1.2021.11.52': UCD_SNMP_MIB.ssCpuRawSystem,
'1.3.6.1.4.1.2021.11.53': UCD_SNMP_MIB.ssCpuRawIdle,
'1.3.6.1.4.1.2021.11.54': UCD_SNMP_MIB.ssCpuRawWait,
'1.3.6.1.4.1.2021.11.55': UCD_SNMP_MIB.ssCpuRawKernel,
'1.3.6.1.4.1.2021.11.56': UCD_SNMP_MIB.ssCpuRawInterrupt,
'1.3.6.1.4.1.2021.11.57': UCD_SNMP_MIB.ssIORawSent,
'1.3.6.1.4.1.2021.11.58': UCD_SNMP_MIB.ssIORawReceived,
'1.3.6.1.4.1.2021.11.59': UCD_SNMP_MIB.ssRawInterrupts,
'1.3.6.1.4.1.2021.11.60': UCD_SNMP_MIB.ssRawContexts,
'1.3.6.1.4.1.2021.16.1': UCD_SNMP_MIB.logMatchMaxEntries,
'1.3.6.1.4.1.2021.100.1': UCD_SNMP_MIB.versionIndex,
'1.3.6.1.4.1.2021.100.2': UCD_SNMP_MIB.versionTag,
'1.3.6.1.4.1.2021.100.3': UCD_SNMP_MIB.versionDate,
'1.3.6.1.4.1.2021.100.4': UCD_SNMP_MIB.versionCDate,
'1.3.6.1.4.1.2021.100.5': UCD_SNMP_MIB.versionIdent,
'1.3.6.1.4.1.2021.100.6': UCD_SNMP_MIB.versionConfigureOptions,
'1.3.6.1.4.1.2021.100.10': UCD_SNMP_MIB.versionClearCache,
'1.3.6.1.4.1.2021.100.11': UCD_SNMP_MIB.versionUpdateConfig,
'1.3.6.1.4.1.2021.100.12': UCD_SNMP_MIB.versionRestartAgent,
'1.3.6.1.4.1.2021.100.13': UCD_SNMP_MIB.versionSavePersistentData,
'1.3.6.1.4.1.2021.100.20': UCD_SNMP_MIB.versionDoDebugging,
'1.3.6.1.4.1.2021.101.1': UCD_SNMP_MIB.snmperrIndex,
'1.3.6.1.4.1.2021.101.2': UCD_SNMP_MIB.snmperrNames,
'1.3.6.1.4.1.2021.101.100': UCD_SNMP_MIB.snmperrErrorFlag,
'1.3.6.1.4.1.2021.101.101': UCD_SNMP_MIB.snmperrErrMessage,
'1.3.6.1.4.1.2021.2.1.1': UCD_SNMP_MIB.prIndex,
'1.3.6.1.4.1.2021.2.1.2': UCD_SNMP_MIB.prNames,
'1.3.6.1.4.1.2021.2.1.3': UCD_SNMP_MIB.prMin,
'1.3.6.1.4.1.2021.2.1.4': UCD_SNMP_MIB.prMax,
'1.3.6.1.4.1.2021.2.1.5': UCD_SNMP_MIB.prCount,
'1.3.6.1.4.1.2021.2.1.100': UCD_SNMP_MIB.prErrorFlag,
'1.3.6.1.4.1.2021.2.1.101': UCD_SNMP_MIB.prErrMessage,
'1.3.6.1.4.1.2021.2.1.102': UCD_SNMP_MIB.prErrFix,
'1.3.6.1.4.1.2021.2.1.103': UCD_SNMP_MIB.prErrFixCmd,
'1.3.6.1.4.1.2021.8.1.1': UCD_SNMP_MIB.extIndex,
'1.3.6.1.4.1.2021.8.1.2': UCD_SNMP_MIB.extNames,
'1.3.6.1.4.1.2021.8.1.3': UCD_SNMP_MIB.extCommand,
'1.3.6.1.4.1.2021.8.1.100': UCD_SNMP_MIB.extResult,
'1.3.6.1.4.1.2021.8.1.101': UCD_SNMP_MIB.extOutput,
'1.3.6.1.4.1.2021.8.1.102': UCD_SNMP_MIB.extErrFix,
'1.3.6.1.4.1.2021.8.1.103': UCD_SNMP_MIB.extErrFixCmd,
'1.3.6.1.4.1.2021.9.1.1': UCD_SNMP_MIB.dskIndex,
'1.3.6.1.4.1.2021.9.1.2': UCD_SNMP_MIB.dskPath,
'1.3.6.1.4.1.2021.9.1.3': UCD_SNMP_MIB.dskDevice,
'1.3.6.1.4.1.2021.9.1.4': UCD_SNMP_MIB.dskMinimum,
'1.3.6.1.4.1.2021.9.1.5': UCD_SNMP_MIB.dskMinPercent,
'1.3.6.1.4.1.2021.9.1.6': UCD_SNMP_MIB.dskTotal,
'1.3.6.1.4.1.2021.9.1.7': UCD_SNMP_MIB.dskAvail,
'1.3.6.1.4.1.2021.9.1.8': UCD_SNMP_MIB.dskUsed,
'1.3.6.1.4.1.2021.9.1.9': UCD_SNMP_MIB.dskPercent,
'1.3.6.1.4.1.2021.9.1.10': UCD_SNMP_MIB.dskPercentNode,
'1.3.6.1.4.1.2021.9.1.100': UCD_SNMP_MIB.dskErrorFlag,
'1.3.6.1.4.1.2021.9.1.101': UCD_SNMP_MIB.dskErrorMsg,
'1.3.6.1.4.1.2021.10.1.1': UCD_SNMP_MIB.laIndex,
'1.3.6.1.4.1.2021.10.1.2': UCD_SNMP_MIB.laNames,
'1.3.6.1.4.1.2021.10.1.3': UCD_SNMP_MIB.laLoad,
'1.3.6.1.4.1.2021.10.1.4': UCD_SNMP_MIB.laConfig,
'1.3.6.1.4.1.2021.10.1.5': UCD_SNMP_MIB.laLoadInt,
'1.3.6.1.4.1.2021.10.1.6': UCD_SNMP_MIB.laLoadFloat,
'1.3.6.1.4.1.2021.10.1.100': UCD_SNMP_MIB.laErrorFlag,
'1.3.6.1.4.1.2021.10.1.101': UCD_SNMP_MIB.laErrMessage,
'1.3.6.1.4.1.2021.15.1.1': UCD_SNMP_MIB.fileIndex,
'1.3.6.1.4.1.2021.15.1.2': UCD_SNMP_MIB.fileName,
'1.3.6.1.4.1.2021.15.1.3': UCD_SNMP_MIB.fileSize,
'1.3.6.1.4.1.2021.15.1.4': UCD_SNMP_MIB.fileMax,
'1.3.6.1.4.1.2021.15.1.100': UCD_SNMP_MIB.fileErrorFlag,
'1.3.6.1.4.1.2021.15.1.101': UCD_SNMP_MIB.fileErrorMsg,
'1.3.6.1.4.1.2021.16.2.1.1': UCD_SNMP_MIB.logMatchIndex,
'1.3.6.1.4.1.2021.16.2.1.2': UCD_SNMP_MIB.logMatchName,
'1.3.6.1.4.1.2021.16.2.1.3': UCD_SNMP_MIB.logMatchFilename,
'1.3.6.1.4.1.2021.16.2.1.4': UCD_SNMP_MIB.logMatchRegEx,
'1.3.6.1.4.1.2021.16.2.1.5': UCD_SNMP_MIB.logMatchGlobalCounter,
'1.3.6.1.4.1.2021.16.2.1.6': UCD_SNMP_MIB.logMatchGlobalCount,
'1.3.6.1.4.1.2021.16.2.1.7': UCD_SNMP_MIB.logMatchCurrentCounter,
'1.3.6.1.4.1.2021.16.2.1.8': UCD_SNMP_MIB.logMatchCurrentCount,
'1.3.6.1.4.1.2021.16.2.1.9': UCD_SNMP_MIB.logMatchCounter,
'1.3.6.1.4.1.2021.16.2.1.10': UCD_SNMP_MIB.logMatchCount,
'1.3.6.1.4.1.2021.16.2.1.11': UCD_SNMP_MIB.logMatchCycle,
'1.3.6.1.4.1.2021.16.2.1.100': UCD_SNMP_MIB.logMatchErrorFlag,
'1.3.6.1.4.1.2021.16.2.1.101': UCD_SNMP_MIB.logMatchRegExCompilation,
'1.3.6.1.4.1.2021.102.1.1': UCD_SNMP_MIB.mrIndex,
'1.3.6.1.4.1.2021.102.1.2': UCD_SNMP_MIB.mrModuleName,
'1.3.6.1.4.1.2021.251.1': UCD_SNMP_MIB.ucdStart,
'1.3.6.1.4.1.2021.251.2': UCD_SNMP_MIB.ucdShutdown,
}
