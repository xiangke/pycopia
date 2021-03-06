# python
# This file is generated by a program (mib2py). 

import IANA_IPPM_METRICS_REGISTRY_MIB

OIDMAP = {
'1.3.6.1.2.1.128': IANA_IPPM_METRICS_REGISTRY_MIB.ianaIppmMetricsRegistry,
'1.3.6.1.2.1.128.1': IANA_IPPM_METRICS_REGISTRY_MIB.ianaIppmMetrics,
'1.3.6.1.2.1.128.1.1': IANA_IPPM_METRICS_REGISTRY_MIB.ietfInstantUnidirConnectivity,
'1.3.6.1.2.1.128.1.2': IANA_IPPM_METRICS_REGISTRY_MIB.ietfInstantBidirConnectivity,
'1.3.6.1.2.1.128.1.3': IANA_IPPM_METRICS_REGISTRY_MIB.ietfIntervalUnidirConnectivity,
'1.3.6.1.2.1.128.1.4': IANA_IPPM_METRICS_REGISTRY_MIB.ietfIntervalBidirConnectivity,
'1.3.6.1.2.1.128.1.5': IANA_IPPM_METRICS_REGISTRY_MIB.ietfIntervalTemporalConnectivity,
'1.3.6.1.2.1.128.1.6': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayDelay,
'1.3.6.1.2.1.128.1.7': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayDelayPoissonStream,
'1.3.6.1.2.1.128.1.8': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayDelayPercentile,
'1.3.6.1.2.1.128.1.9': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayDelayMedian,
'1.3.6.1.2.1.128.1.10': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayDelayMinimum,
'1.3.6.1.2.1.128.1.11': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayDelayInversePercentile,
'1.3.6.1.2.1.128.1.12': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayPktLoss,
'1.3.6.1.2.1.128.1.13': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayPktLossPoissonStream,
'1.3.6.1.2.1.128.1.14': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayPktLossAverage,
'1.3.6.1.2.1.128.1.15': IANA_IPPM_METRICS_REGISTRY_MIB.ietfRoundTripDelay,
'1.3.6.1.2.1.128.1.16': IANA_IPPM_METRICS_REGISTRY_MIB.ietfRoundTripDelayPoissonStream,
'1.3.6.1.2.1.128.1.17': IANA_IPPM_METRICS_REGISTRY_MIB.ietfRoundTripDelayPercentile,
'1.3.6.1.2.1.128.1.18': IANA_IPPM_METRICS_REGISTRY_MIB.ietfRoundTripDelayMedian,
'1.3.6.1.2.1.128.1.19': IANA_IPPM_METRICS_REGISTRY_MIB.ietfRoundTripDelayMinimum,
'1.3.6.1.2.1.128.1.20': IANA_IPPM_METRICS_REGISTRY_MIB.ietfRoundTripDelayInvPercentile,
'1.3.6.1.2.1.128.1.21': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayLossDistanceStream,
'1.3.6.1.2.1.128.1.22': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayLossPeriodStream,
'1.3.6.1.2.1.128.1.23': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayLossNoticeableRate,
'1.3.6.1.2.1.128.1.24': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayLossPeriodTotal,
'1.3.6.1.2.1.128.1.25': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayLossPeriodLengths,
'1.3.6.1.2.1.128.1.26': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayInterLossPeriodLengths,
'1.3.6.1.2.1.128.1.27': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayIpdv,
'1.3.6.1.2.1.128.1.28': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayIpdvPoissonStream,
'1.3.6.1.2.1.128.1.29': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayIpdvPercentile,
'1.3.6.1.2.1.128.1.30': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayIpdvInversePercentile,
'1.3.6.1.2.1.128.1.31': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayIpdvJitter,
'1.3.6.1.2.1.128.1.32': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayPeakToPeakIpdv,
'1.3.6.1.2.1.128.1.33': IANA_IPPM_METRICS_REGISTRY_MIB.ietfOneWayDelayPeriodicStream,
'1.3.6.1.2.1.128.1.34': IANA_IPPM_METRICS_REGISTRY_MIB.ietfReorderedSingleton,
'1.3.6.1.2.1.128.1.35': IANA_IPPM_METRICS_REGISTRY_MIB.ietfReorderedPacketRatio,
'1.3.6.1.2.1.128.1.36': IANA_IPPM_METRICS_REGISTRY_MIB.ietfReorderingExtent,
'1.3.6.1.2.1.128.1.37': IANA_IPPM_METRICS_REGISTRY_MIB.ietfReorderingLateTimeOffset,
'1.3.6.1.2.1.128.1.38': IANA_IPPM_METRICS_REGISTRY_MIB.ietfReorderingByteOffset,
'1.3.6.1.2.1.128.1.39': IANA_IPPM_METRICS_REGISTRY_MIB.ietfReorderingGap,
'1.3.6.1.2.1.128.1.40': IANA_IPPM_METRICS_REGISTRY_MIB.ietfReorderingGapTime,
'1.3.6.1.2.1.128.1.41': IANA_IPPM_METRICS_REGISTRY_MIB.ietfReorderingFreeRunx,
'1.3.6.1.2.1.128.1.42': IANA_IPPM_METRICS_REGISTRY_MIB.ietfReorderingFreeRunq,
'1.3.6.1.2.1.128.1.43': IANA_IPPM_METRICS_REGISTRY_MIB.ietfReorderingFreeRunp,
'1.3.6.1.2.1.128.1.44': IANA_IPPM_METRICS_REGISTRY_MIB.ietfReorderingFreeRuna,
'1.3.6.1.2.1.128.1.45': IANA_IPPM_METRICS_REGISTRY_MIB.ietfnReordering,
}
