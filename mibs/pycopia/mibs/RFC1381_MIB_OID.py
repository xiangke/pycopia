# python
# This file is generated by a program (mib2py). 

import RFC1381_MIB

OIDMAP = {
'1.3.6.1.2.1.10.16': RFC1381_MIB.lapb,
'1.3.6.1.2.1.10.16.5': RFC1381_MIB.lapbProtocolVersion,
'1.3.6.1.2.1.10.16.5.1': RFC1381_MIB.lapbProtocolIso7776v1986,
'1.3.6.1.2.1.10.16.5.2': RFC1381_MIB.lapbProtocolCcittV1980,
'1.3.6.1.2.1.10.16.5.3': RFC1381_MIB.lapbProtocolCcittV1984,
'1.3.6.1.2.1.10.16.1.1.1': RFC1381_MIB.lapbAdmnIndex,
'1.3.6.1.2.1.10.16.1.1.2': RFC1381_MIB.lapbAdmnStationType,
'1.3.6.1.2.1.10.16.1.1.3': RFC1381_MIB.lapbAdmnControlField,
'1.3.6.1.2.1.10.16.1.1.4': RFC1381_MIB.lapbAdmnTransmitN1FrameSize,
'1.3.6.1.2.1.10.16.1.1.5': RFC1381_MIB.lapbAdmnReceiveN1FrameSize,
'1.3.6.1.2.1.10.16.1.1.6': RFC1381_MIB.lapbAdmnTransmitKWindowSize,
'1.3.6.1.2.1.10.16.1.1.7': RFC1381_MIB.lapbAdmnReceiveKWindowSize,
'1.3.6.1.2.1.10.16.1.1.8': RFC1381_MIB.lapbAdmnN2RxmitCount,
'1.3.6.1.2.1.10.16.1.1.9': RFC1381_MIB.lapbAdmnT1AckTimer,
'1.3.6.1.2.1.10.16.1.1.10': RFC1381_MIB.lapbAdmnT2AckDelayTimer,
'1.3.6.1.2.1.10.16.1.1.11': RFC1381_MIB.lapbAdmnT3DisconnectTimer,
'1.3.6.1.2.1.10.16.1.1.12': RFC1381_MIB.lapbAdmnT4IdleTimer,
'1.3.6.1.2.1.10.16.1.1.13': RFC1381_MIB.lapbAdmnActionInitiate,
'1.3.6.1.2.1.10.16.1.1.14': RFC1381_MIB.lapbAdmnActionRecvDM,
'1.3.6.1.2.1.10.16.2.1.1': RFC1381_MIB.lapbOperIndex,
'1.3.6.1.2.1.10.16.2.1.2': RFC1381_MIB.lapbOperStationType,
'1.3.6.1.2.1.10.16.2.1.3': RFC1381_MIB.lapbOperControlField,
'1.3.6.1.2.1.10.16.2.1.4': RFC1381_MIB.lapbOperTransmitN1FrameSize,
'1.3.6.1.2.1.10.16.2.1.5': RFC1381_MIB.lapbOperReceiveN1FrameSize,
'1.3.6.1.2.1.10.16.2.1.6': RFC1381_MIB.lapbOperTransmitKWindowSize,
'1.3.6.1.2.1.10.16.2.1.7': RFC1381_MIB.lapbOperReceiveKWindowSize,
'1.3.6.1.2.1.10.16.2.1.8': RFC1381_MIB.lapbOperN2RxmitCount,
'1.3.6.1.2.1.10.16.2.1.9': RFC1381_MIB.lapbOperT1AckTimer,
'1.3.6.1.2.1.10.16.2.1.10': RFC1381_MIB.lapbOperT2AckDelayTimer,
'1.3.6.1.2.1.10.16.2.1.11': RFC1381_MIB.lapbOperT3DisconnectTimer,
'1.3.6.1.2.1.10.16.2.1.12': RFC1381_MIB.lapbOperT4IdleTimer,
'1.3.6.1.2.1.10.16.2.1.13': RFC1381_MIB.lapbOperPortId,
'1.3.6.1.2.1.10.16.2.1.14': RFC1381_MIB.lapbOperProtocolVersionId,
'1.3.6.1.2.1.10.16.3.1.1': RFC1381_MIB.lapbFlowIfIndex,
'1.3.6.1.2.1.10.16.3.1.2': RFC1381_MIB.lapbFlowStateChanges,
'1.3.6.1.2.1.10.16.3.1.3': RFC1381_MIB.lapbFlowChangeReason,
'1.3.6.1.2.1.10.16.3.1.4': RFC1381_MIB.lapbFlowCurrentMode,
'1.3.6.1.2.1.10.16.3.1.5': RFC1381_MIB.lapbFlowBusyDefers,
'1.3.6.1.2.1.10.16.3.1.6': RFC1381_MIB.lapbFlowRejOutPkts,
'1.3.6.1.2.1.10.16.3.1.7': RFC1381_MIB.lapbFlowRejInPkts,
'1.3.6.1.2.1.10.16.3.1.8': RFC1381_MIB.lapbFlowT1Timeouts,
'1.3.6.1.2.1.10.16.3.1.9': RFC1381_MIB.lapbFlowFrmrSent,
'1.3.6.1.2.1.10.16.3.1.10': RFC1381_MIB.lapbFlowFrmrReceived,
'1.3.6.1.2.1.10.16.3.1.11': RFC1381_MIB.lapbFlowXidReceived,
'1.3.6.1.2.1.10.16.4.1.1': RFC1381_MIB.lapbXidIndex,
'1.3.6.1.2.1.10.16.4.1.2': RFC1381_MIB.lapbXidAdRIdentifier,
'1.3.6.1.2.1.10.16.4.1.3': RFC1381_MIB.lapbXidAdRAddress,
'1.3.6.1.2.1.10.16.4.1.4': RFC1381_MIB.lapbXidParameterUniqueIdentifier,
'1.3.6.1.2.1.10.16.4.1.5': RFC1381_MIB.lapbXidGroupAddress,
'1.3.6.1.2.1.10.16.4.1.6': RFC1381_MIB.lapbXidPortNumber,
'1.3.6.1.2.1.10.16.4.1.7': RFC1381_MIB.lapbXidUserDataSubfield,
}
