# python
# This file is generated by a program (mib2py). 

import RFC1158_MIB

OIDMAP = {
'0.0': RFC1158_MIB.nullSpecific,
'1.3.6.1.2.1': RFC1158_MIB.mib_2,
'1.3.6.1.2.1.1': RFC1158_MIB.system,
'1.3.6.1.2.1.2': RFC1158_MIB.interfaces,
'1.3.6.1.2.1.3': RFC1158_MIB.at,
'1.3.6.1.2.1.4': RFC1158_MIB.ip,
'1.3.6.1.2.1.5': RFC1158_MIB.icmp,
'1.3.6.1.2.1.6': RFC1158_MIB.tcp,
'1.3.6.1.2.1.7': RFC1158_MIB.udp,
'1.3.6.1.2.1.8': RFC1158_MIB.egp,
'1.3.6.1.2.1.10': RFC1158_MIB.transmission,
'1.3.6.1.2.1.11': RFC1158_MIB.snmp,
'1.3.6.1.2.1.1.1': RFC1158_MIB.sysDescr,
'1.3.6.1.2.1.1.2': RFC1158_MIB.sysObjectID,
'1.3.6.1.2.1.1.3': RFC1158_MIB.sysUpTime,
'1.3.6.1.2.1.1.4': RFC1158_MIB.sysContact,
'1.3.6.1.2.1.1.5': RFC1158_MIB.sysName,
'1.3.6.1.2.1.1.6': RFC1158_MIB.sysLocation,
'1.3.6.1.2.1.1.7': RFC1158_MIB.sysServices,
'1.3.6.1.2.1.2.1': RFC1158_MIB.ifNumber,
'1.3.6.1.2.1.2.2.1.1': RFC1158_MIB.ifIndex,
'1.3.6.1.2.1.2.2.1.2': RFC1158_MIB.ifDescr,
'1.3.6.1.2.1.2.2.1.3': RFC1158_MIB.ifType,
'1.3.6.1.2.1.2.2.1.4': RFC1158_MIB.ifMtu,
'1.3.6.1.2.1.2.2.1.5': RFC1158_MIB.ifSpeed,
'1.3.6.1.2.1.2.2.1.6': RFC1158_MIB.ifPhysAddress,
'1.3.6.1.2.1.2.2.1.7': RFC1158_MIB.ifAdminStatus,
'1.3.6.1.2.1.2.2.1.8': RFC1158_MIB.ifOperStatus,
'1.3.6.1.2.1.2.2.1.9': RFC1158_MIB.ifLastChange,
'1.3.6.1.2.1.2.2.1.10': RFC1158_MIB.ifInOctets,
'1.3.6.1.2.1.2.2.1.11': RFC1158_MIB.ifInUcastPkts,
'1.3.6.1.2.1.2.2.1.12': RFC1158_MIB.ifInNUcastPkts,
'1.3.6.1.2.1.2.2.1.13': RFC1158_MIB.ifInDiscards,
'1.3.6.1.2.1.2.2.1.14': RFC1158_MIB.ifInErrors,
'1.3.6.1.2.1.2.2.1.15': RFC1158_MIB.ifInUnknownProtos,
'1.3.6.1.2.1.2.2.1.16': RFC1158_MIB.ifOutOctets,
'1.3.6.1.2.1.2.2.1.17': RFC1158_MIB.ifOutUcastPkts,
'1.3.6.1.2.1.2.2.1.18': RFC1158_MIB.ifOutNUcastPkts,
'1.3.6.1.2.1.2.2.1.19': RFC1158_MIB.ifOutDiscards,
'1.3.6.1.2.1.2.2.1.20': RFC1158_MIB.ifOutErrors,
'1.3.6.1.2.1.2.2.1.21': RFC1158_MIB.ifOutQLen,
'1.3.6.1.2.1.2.2.1.22': RFC1158_MIB.ifSpecific,
'1.3.6.1.2.1.4.1': RFC1158_MIB.ipForwarding,
'1.3.6.1.2.1.4.2': RFC1158_MIB.ipDefaultTTL,
'1.3.6.1.2.1.4.3': RFC1158_MIB.ipInReceives,
'1.3.6.1.2.1.4.4': RFC1158_MIB.ipInHdrErrors,
'1.3.6.1.2.1.4.5': RFC1158_MIB.ipInAddrErrors,
'1.3.6.1.2.1.4.6': RFC1158_MIB.ipForwDatagrams,
'1.3.6.1.2.1.4.7': RFC1158_MIB.ipInUnknownProtos,
'1.3.6.1.2.1.4.8': RFC1158_MIB.ipInDiscards,
'1.3.6.1.2.1.4.9': RFC1158_MIB.ipInDelivers,
'1.3.6.1.2.1.4.10': RFC1158_MIB.ipOutRequests,
'1.3.6.1.2.1.4.11': RFC1158_MIB.ipOutDiscards,
'1.3.6.1.2.1.4.12': RFC1158_MIB.ipOutNoRoutes,
'1.3.6.1.2.1.4.13': RFC1158_MIB.ipReasmTimeout,
'1.3.6.1.2.1.4.14': RFC1158_MIB.ipReasmReqds,
'1.3.6.1.2.1.4.15': RFC1158_MIB.ipReasmOKs,
'1.3.6.1.2.1.4.16': RFC1158_MIB.ipReasmFails,
'1.3.6.1.2.1.4.17': RFC1158_MIB.ipFragOKs,
'1.3.6.1.2.1.4.18': RFC1158_MIB.ipFragFails,
'1.3.6.1.2.1.4.19': RFC1158_MIB.ipFragCreates,
'1.3.6.1.2.1.4.20.1.1': RFC1158_MIB.ipAdEntAddr,
'1.3.6.1.2.1.4.20.1.2': RFC1158_MIB.ipAdEntIfIndex,
'1.3.6.1.2.1.4.20.1.3': RFC1158_MIB.ipAdEntNetMask,
'1.3.6.1.2.1.4.20.1.4': RFC1158_MIB.ipAdEntBcastAddr,
'1.3.6.1.2.1.4.20.1.5': RFC1158_MIB.ipAdEntReasmMaxSize,
'1.3.6.1.2.1.4.21.1.1': RFC1158_MIB.ipRouteDest,
'1.3.6.1.2.1.4.21.1.2': RFC1158_MIB.ipRouteIfIndex,
'1.3.6.1.2.1.4.21.1.3': RFC1158_MIB.ipRouteMetric1,
'1.3.6.1.2.1.4.21.1.4': RFC1158_MIB.ipRouteMetric2,
'1.3.6.1.2.1.4.21.1.5': RFC1158_MIB.ipRouteMetric3,
'1.3.6.1.2.1.4.21.1.6': RFC1158_MIB.ipRouteMetric4,
'1.3.6.1.2.1.4.21.1.7': RFC1158_MIB.ipRouteNextHop,
'1.3.6.1.2.1.4.21.1.8': RFC1158_MIB.ipRouteType,
'1.3.6.1.2.1.4.21.1.9': RFC1158_MIB.ipRouteProto,
'1.3.6.1.2.1.4.21.1.10': RFC1158_MIB.ipRouteAge,
'1.3.6.1.2.1.4.21.1.11': RFC1158_MIB.ipRouteMask,
'1.3.6.1.2.1.4.22.1.1': RFC1158_MIB.ipNetToMediaIfIndex,
'1.3.6.1.2.1.4.22.1.2': RFC1158_MIB.ipNetToMediaPhysAddress,
'1.3.6.1.2.1.4.22.1.3': RFC1158_MIB.ipNetToMediaNetAddress,
'1.3.6.1.2.1.4.22.1.4': RFC1158_MIB.ipNetToMediaType,
'1.3.6.1.2.1.5.1': RFC1158_MIB.icmpInMsgs,
'1.3.6.1.2.1.5.2': RFC1158_MIB.icmpInErrors,
'1.3.6.1.2.1.5.3': RFC1158_MIB.icmpInDestUnreachs,
'1.3.6.1.2.1.5.4': RFC1158_MIB.icmpInTimeExcds,
'1.3.6.1.2.1.5.5': RFC1158_MIB.icmpInParmProbs,
'1.3.6.1.2.1.5.6': RFC1158_MIB.icmpInSrcQuenchs,
'1.3.6.1.2.1.5.7': RFC1158_MIB.icmpInRedirects,
'1.3.6.1.2.1.5.8': RFC1158_MIB.icmpInEchos,
'1.3.6.1.2.1.5.9': RFC1158_MIB.icmpInEchoReps,
'1.3.6.1.2.1.5.10': RFC1158_MIB.icmpInTimestamps,
'1.3.6.1.2.1.5.11': RFC1158_MIB.icmpInTimestampReps,
'1.3.6.1.2.1.5.12': RFC1158_MIB.icmpInAddrMasks,
'1.3.6.1.2.1.5.13': RFC1158_MIB.icmpInAddrMaskReps,
'1.3.6.1.2.1.5.14': RFC1158_MIB.icmpOutMsgs,
'1.3.6.1.2.1.5.15': RFC1158_MIB.icmpOutErrors,
'1.3.6.1.2.1.5.16': RFC1158_MIB.icmpOutDestUnreachs,
'1.3.6.1.2.1.5.17': RFC1158_MIB.icmpOutTimeExcds,
'1.3.6.1.2.1.5.18': RFC1158_MIB.icmpOutParmProbs,
'1.3.6.1.2.1.5.19': RFC1158_MIB.icmpOutSrcQuenchs,
'1.3.6.1.2.1.5.20': RFC1158_MIB.icmpOutRedirects,
'1.3.6.1.2.1.5.21': RFC1158_MIB.icmpOutEchos,
'1.3.6.1.2.1.5.22': RFC1158_MIB.icmpOutEchoReps,
'1.3.6.1.2.1.5.23': RFC1158_MIB.icmpOutTimestamps,
'1.3.6.1.2.1.5.24': RFC1158_MIB.icmpOutTimestampReps,
'1.3.6.1.2.1.5.25': RFC1158_MIB.icmpOutAddrMasks,
'1.3.6.1.2.1.5.26': RFC1158_MIB.icmpOutAddrMaskReps,
'1.3.6.1.2.1.6.1': RFC1158_MIB.tcpRtoAlgorithm,
'1.3.6.1.2.1.6.2': RFC1158_MIB.tcpRtoMin,
'1.3.6.1.2.1.6.3': RFC1158_MIB.tcpRtoMax,
'1.3.6.1.2.1.6.4': RFC1158_MIB.tcpMaxConn,
'1.3.6.1.2.1.6.5': RFC1158_MIB.tcpActiveOpens,
'1.3.6.1.2.1.6.6': RFC1158_MIB.tcpPassiveOpens,
'1.3.6.1.2.1.6.7': RFC1158_MIB.tcpAttemptFails,
'1.3.6.1.2.1.6.8': RFC1158_MIB.tcpEstabResets,
'1.3.6.1.2.1.6.9': RFC1158_MIB.tcpCurrEstab,
'1.3.6.1.2.1.6.10': RFC1158_MIB.tcpInSegs,
'1.3.6.1.2.1.6.11': RFC1158_MIB.tcpOutSegs,
'1.3.6.1.2.1.6.12': RFC1158_MIB.tcpRetransSegs,
'1.3.6.1.2.1.6.13.1.1': RFC1158_MIB.tcpConnState,
'1.3.6.1.2.1.6.13.1.2': RFC1158_MIB.tcpConnLocalAddress,
'1.3.6.1.2.1.6.13.1.3': RFC1158_MIB.tcpConnLocalPort,
'1.3.6.1.2.1.6.13.1.4': RFC1158_MIB.tcpConnRemAddress,
'1.3.6.1.2.1.6.13.1.5': RFC1158_MIB.tcpConnRemPort,
'1.3.6.1.2.1.6.14': RFC1158_MIB.tcpInErrs,
'1.3.6.1.2.1.6.15': RFC1158_MIB.tcpOutRsts,
'1.3.6.1.2.1.7.1': RFC1158_MIB.udpInDatagrams,
'1.3.6.1.2.1.7.2': RFC1158_MIB.udpNoPorts,
'1.3.6.1.2.1.7.3': RFC1158_MIB.udpInErrors,
'1.3.6.1.2.1.7.4': RFC1158_MIB.udpOutDatagrams,
'1.3.6.1.2.1.7.5.1.1': RFC1158_MIB.udpLocalAddress,
'1.3.6.1.2.1.7.5.1.2': RFC1158_MIB.udpLocalPort,
'1.3.6.1.2.1.8.1': RFC1158_MIB.egpInMsgs,
'1.3.6.1.2.1.8.2': RFC1158_MIB.egpInErrors,
'1.3.6.1.2.1.8.3': RFC1158_MIB.egpOutMsgs,
'1.3.6.1.2.1.8.4': RFC1158_MIB.egpOutErrors,
'1.3.6.1.2.1.8.5.1.1': RFC1158_MIB.egpNeighState,
'1.3.6.1.2.1.8.5.1.2': RFC1158_MIB.egpNeighAddr,
'1.3.6.1.2.1.8.5.1.3': RFC1158_MIB.egpNeighAs,
'1.3.6.1.2.1.8.5.1.4': RFC1158_MIB.egpNeighInMsgs,
'1.3.6.1.2.1.8.5.1.5': RFC1158_MIB.egpNeighInErrs,
'1.3.6.1.2.1.8.5.1.6': RFC1158_MIB.egpNeighOutMsgs,
'1.3.6.1.2.1.8.5.1.7': RFC1158_MIB.egpNeighOutErrs,
'1.3.6.1.2.1.8.5.1.8': RFC1158_MIB.egpNeighInErrMsgs,
'1.3.6.1.2.1.8.5.1.9': RFC1158_MIB.egpNeighOutErrMsgs,
'1.3.6.1.2.1.8.5.1.10': RFC1158_MIB.egpNeighStateUps,
'1.3.6.1.2.1.8.5.1.11': RFC1158_MIB.egpNeighStateDowns,
'1.3.6.1.2.1.8.5.1.12': RFC1158_MIB.egpNeighIntervalHello,
'1.3.6.1.2.1.8.5.1.13': RFC1158_MIB.egpNeighIntervalPoll,
'1.3.6.1.2.1.8.5.1.14': RFC1158_MIB.egpNeighMode,
'1.3.6.1.2.1.8.5.1.15': RFC1158_MIB.egpNeighEventTrigger,
'1.3.6.1.2.1.8.6': RFC1158_MIB.egpAs,
'1.3.6.1.2.1.11.1': RFC1158_MIB.snmpInPkts,
'1.3.6.1.2.1.11.2': RFC1158_MIB.snmpOutPkts,
'1.3.6.1.2.1.11.3': RFC1158_MIB.snmpInBadVersions,
'1.3.6.1.2.1.11.4': RFC1158_MIB.snmpInBadCommunityNames,
'1.3.6.1.2.1.11.5': RFC1158_MIB.snmpInBadCommunityUses,
'1.3.6.1.2.1.11.6': RFC1158_MIB.snmpInASNParseErrs,
'1.3.6.1.2.1.11.7': RFC1158_MIB.snmpInBadTypes,
'1.3.6.1.2.1.11.8': RFC1158_MIB.snmpInTooBigs,
'1.3.6.1.2.1.11.9': RFC1158_MIB.snmpInNoSuchNames,
'1.3.6.1.2.1.11.10': RFC1158_MIB.snmpInBadValues,
'1.3.6.1.2.1.11.11': RFC1158_MIB.snmpInReadOnlys,
'1.3.6.1.2.1.11.12': RFC1158_MIB.snmpInGenErrs,
'1.3.6.1.2.1.11.13': RFC1158_MIB.snmpInTotalReqVars,
'1.3.6.1.2.1.11.14': RFC1158_MIB.snmpInTotalSetVars,
'1.3.6.1.2.1.11.15': RFC1158_MIB.snmpInGetRequests,
'1.3.6.1.2.1.11.16': RFC1158_MIB.snmpInGetNexts,
'1.3.6.1.2.1.11.17': RFC1158_MIB.snmpInSetRequests,
'1.3.6.1.2.1.11.18': RFC1158_MIB.snmpInGetResponses,
'1.3.6.1.2.1.11.19': RFC1158_MIB.snmpInTraps,
'1.3.6.1.2.1.11.20': RFC1158_MIB.snmpOutTooBigs,
'1.3.6.1.2.1.11.21': RFC1158_MIB.snmpOutNoSuchNames,
'1.3.6.1.2.1.11.22': RFC1158_MIB.snmpOutBadValues,
'1.3.6.1.2.1.11.23': RFC1158_MIB.snmpOutReadOnlys,
'1.3.6.1.2.1.11.24': RFC1158_MIB.snmpOutGenErrs,
'1.3.6.1.2.1.11.25': RFC1158_MIB.snmpOutGetRequests,
'1.3.6.1.2.1.11.26': RFC1158_MIB.snmpOutGetNexts,
'1.3.6.1.2.1.11.27': RFC1158_MIB.snmpOutSetRequests,
'1.3.6.1.2.1.11.28': RFC1158_MIB.snmpOutGetResponses,
'1.3.6.1.2.1.11.29': RFC1158_MIB.snmpOutTraps,
'1.3.6.1.2.1.11.30': RFC1158_MIB.snmpEnableAuthTraps,
}
