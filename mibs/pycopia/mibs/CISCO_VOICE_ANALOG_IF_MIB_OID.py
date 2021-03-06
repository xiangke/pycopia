# python
# This file is generated by a program (mib2py). 

import CISCO_VOICE_ANALOG_IF_MIB

OIDMAP = {
'1.3.6.1.4.1.9.9.62': CISCO_VOICE_ANALOG_IF_MIB.ciscoVoiceAnalogIfMIB,
'1.3.6.1.4.1.9.9.62.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfObjects,
'1.3.6.1.4.1.9.9.62.1.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfGeneralObjects,
'1.3.6.1.4.1.9.9.62.1.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMObjects,
'1.3.6.1.4.1.9.9.62.1.3': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXOObjects,
'1.3.6.1.4.1.9.9.62.1.4': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXSObjects,
'1.3.6.1.4.1.9.9.62.3': CISCO_VOICE_ANALOG_IF_MIB.cvaIfMIBConformance,
'1.3.6.1.4.1.9.9.62.3.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfMIBCompliances,
'1.3.6.1.4.1.9.9.62.3.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfMIBGroups,
'1.3.6.1.4.1.9.9.62.1.1.1.1.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfCfgImpedance,
'1.3.6.1.4.1.9.9.62.1.1.1.1.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfCfgIntegratedDSP,
'1.3.6.1.4.1.9.9.62.1.1.2.1.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfStatusInfoType,
'1.3.6.1.4.1.9.9.62.1.1.2.1.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfMaintenanceMode,
'1.3.6.1.4.1.9.9.62.1.1.2.1.3': CISCO_VOICE_ANALOG_IF_MIB.cvaIfStatusSignalErrors,
'1.3.6.1.4.1.9.9.62.1.2.1.1.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMCfgSignalType,
'1.3.6.1.4.1.9.9.62.1.2.1.1.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMCfgOperation,
'1.3.6.1.4.1.9.9.62.1.2.1.1.3': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMCfgType,
'1.3.6.1.4.1.9.9.62.1.2.1.1.4': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMCfgDialType,
'1.3.6.1.4.1.9.9.62.1.2.2.1.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMInSeizureActive,
'1.3.6.1.4.1.9.9.62.1.2.2.1.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMOutSeizureActive,
'1.3.6.1.4.1.9.9.62.1.2.3.1.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMTimingDigitDuration,
'1.3.6.1.4.1.9.9.62.1.2.3.1.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMTimingInterDigitDuration,
'1.3.6.1.4.1.9.9.62.1.2.3.1.3': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMTimingPulseRate,
'1.3.6.1.4.1.9.9.62.1.2.3.1.4': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMTimingPulseInterDigitDuration,
'1.3.6.1.4.1.9.9.62.1.2.3.1.5': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMTimingClearWaitDuration,
'1.3.6.1.4.1.9.9.62.1.2.3.1.6': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMTimingMaxWinkWaitDuration,
'1.3.6.1.4.1.9.9.62.1.2.3.1.7': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMTimingMaxWinkDuration,
'1.3.6.1.4.1.9.9.62.1.2.3.1.8': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMTimingDelayStart,
'1.3.6.1.4.1.9.9.62.1.2.3.1.9': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMTimingMaxDelayDuration,
'1.3.6.1.4.1.9.9.62.1.2.3.1.10': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMTimingMinDelayPulseWidth,
'1.3.6.1.4.1.9.9.62.1.3.1.1.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXOCfgSignalType,
'1.3.6.1.4.1.9.9.62.1.3.1.1.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXOCfgNumberRings,
'1.3.6.1.4.1.9.9.62.1.3.1.1.3': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXOCfgSupDisconnect,
'1.3.6.1.4.1.9.9.62.1.3.1.1.4': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXOCfgDialType,
'1.3.6.1.4.1.9.9.62.1.3.2.1.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXOHookStatus,
'1.3.6.1.4.1.9.9.62.1.3.2.1.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXORingDetect,
'1.3.6.1.4.1.9.9.62.1.3.2.1.3': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXORingGround,
'1.3.6.1.4.1.9.9.62.1.3.2.1.4': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXOTipGround,
'1.3.6.1.4.1.9.9.62.1.3.3.1.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXOTimingDigitDuration,
'1.3.6.1.4.1.9.9.62.1.3.3.1.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXOTimingInterDigitDuration,
'1.3.6.1.4.1.9.9.62.1.3.3.1.3': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXOTimingPulseRate,
'1.3.6.1.4.1.9.9.62.1.3.3.1.4': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXOTimingPulseInterDigitDuration,
'1.3.6.1.4.1.9.9.62.1.4.1.1.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXSCfgSignalType,
'1.3.6.1.4.1.9.9.62.1.4.1.1.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXSRingFrequency,
'1.3.6.1.4.1.9.9.62.1.4.2.1.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXSHookStatus,
'1.3.6.1.4.1.9.9.62.1.4.2.1.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXSRingActive,
'1.3.6.1.4.1.9.9.62.1.4.2.1.3': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXSRingGround,
'1.3.6.1.4.1.9.9.62.1.4.2.1.4': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXSTipGround,
'1.3.6.1.4.1.9.9.62.1.4.3.1.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXSTimingDigitDuration,
'1.3.6.1.4.1.9.9.62.1.4.3.1.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXSTimingInterDigitDuration,
'1.3.6.1.4.1.9.9.62.3.2.1': CISCO_VOICE_ANALOG_IF_MIB.cvaIfGeneralGroup,
'1.3.6.1.4.1.9.9.62.3.2.2': CISCO_VOICE_ANALOG_IF_MIB.cvaIfEMGroup,
'1.3.6.1.4.1.9.9.62.3.2.3': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXOGroup,
'1.3.6.1.4.1.9.9.62.3.2.4': CISCO_VOICE_ANALOG_IF_MIB.cvaIfFXSGroup,
}
