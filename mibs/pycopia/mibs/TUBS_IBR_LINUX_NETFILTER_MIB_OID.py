# python
# This file is generated by a program (mib2py). 

import TUBS_IBR_LINUX_NETFILTER_MIB

OIDMAP = {
'1.3.6.1.4.1.1575.1.13': TUBS_IBR_LINUX_NETFILTER_MIB.lnfMIB,
'1.3.6.1.4.1.1575.1.13.1': TUBS_IBR_LINUX_NETFILTER_MIB.lnfObjects,
'1.3.6.1.4.1.1575.1.13.2': TUBS_IBR_LINUX_NETFILTER_MIB.lnfTraps,
'1.3.6.1.4.1.1575.1.13.2.0': TUBS_IBR_LINUX_NETFILTER_MIB.lnfNotifications,
'1.3.6.1.4.1.1575.1.13.3': TUBS_IBR_LINUX_NETFILTER_MIB.lnfConformance,
'1.3.6.1.4.1.1575.1.13.3.1': TUBS_IBR_LINUX_NETFILTER_MIB.lnfCompliances,
'1.3.6.1.4.1.1575.1.13.3.2': TUBS_IBR_LINUX_NETFILTER_MIB.lnfGroups,
'1.3.6.1.4.1.1575.1.13.1.1': TUBS_IBR_LINUX_NETFILTER_MIB.lnfLastChange,
'1.3.6.1.4.1.1575.1.13.1.2.1.1': TUBS_IBR_LINUX_NETFILTER_MIB.lnfTableAddressType,
'1.3.6.1.4.1.1575.1.13.1.2.1.2': TUBS_IBR_LINUX_NETFILTER_MIB.lnfTableName,
'1.3.6.1.4.1.1575.1.13.1.2.1.3': TUBS_IBR_LINUX_NETFILTER_MIB.lnfTableLastChange,
'1.3.6.1.4.1.1575.1.13.1.3.1.1': TUBS_IBR_LINUX_NETFILTER_MIB.lnfChainName,
'1.3.6.1.4.1.1575.1.13.1.3.1.2': TUBS_IBR_LINUX_NETFILTER_MIB.lnfChainPackets,
'1.3.6.1.4.1.1575.1.13.1.3.1.3': TUBS_IBR_LINUX_NETFILTER_MIB.lnfChainOctets,
'1.3.6.1.4.1.1575.1.13.1.3.1.4': TUBS_IBR_LINUX_NETFILTER_MIB.lnfChainTarget,
'1.3.6.1.4.1.1575.1.13.1.3.1.5': TUBS_IBR_LINUX_NETFILTER_MIB.lnfChainLastChange,
'1.3.6.1.4.1.1575.1.13.1.3.1.6': TUBS_IBR_LINUX_NETFILTER_MIB.lnfChainStorage,
'1.3.6.1.4.1.1575.1.13.1.3.1.7': TUBS_IBR_LINUX_NETFILTER_MIB.lnfChainStatus,
'1.3.6.1.4.1.1575.1.13.1.4.1.1': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleIndex,
'1.3.6.1.4.1.1575.1.13.1.4.1.2': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleProtocol,
'1.3.6.1.4.1.1575.1.13.1.4.1.3': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleProtocolInv,
'1.3.6.1.4.1.1575.1.13.1.4.1.4': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleSourceAddress,
'1.3.6.1.4.1.1575.1.13.1.4.1.5': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleSourceAddressPrefixLength,
'1.3.6.1.4.1.1575.1.13.1.4.1.6': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleSourceAddressInv,
'1.3.6.1.4.1.1575.1.13.1.4.1.7': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleDestinationAddress,
'1.3.6.1.4.1.1575.1.13.1.4.1.8': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleDestinationAddressPrefixLength,
'1.3.6.1.4.1.1575.1.13.1.4.1.9': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleDestinationAddressInv,
'1.3.6.1.4.1.1575.1.13.1.4.1.10': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleInInterface,
'1.3.6.1.4.1.1575.1.13.1.4.1.11': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleInInterfaceInv,
'1.3.6.1.4.1.1575.1.13.1.4.1.12': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleOutInterface,
'1.3.6.1.4.1.1575.1.13.1.4.1.13': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleOutInterfaceInv,
'1.3.6.1.4.1.1575.1.13.1.4.1.14': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleFragment,
'1.3.6.1.4.1.1575.1.13.1.4.1.15': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleFragmentInv,
'1.3.6.1.4.1.1575.1.13.1.4.1.16': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRulePackets,
'1.3.6.1.4.1.1575.1.13.1.4.1.17': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleOctets,
'1.3.6.1.4.1.1575.1.13.1.4.1.18': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleTarget,
'1.3.6.1.4.1.1575.1.13.1.4.1.19': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleTargetChain,
'1.3.6.1.4.1.1575.1.13.1.4.1.20': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleTrapEnable,
'1.3.6.1.4.1.1575.1.13.1.4.1.21': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleLastChange,
'1.3.6.1.4.1.1575.1.13.1.4.1.22': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleStorage,
'1.3.6.1.4.1.1575.1.13.1.4.1.23': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleStatus,
'1.3.6.1.4.1.1575.1.13.2.0.1': TUBS_IBR_LINUX_NETFILTER_MIB.lnfRuleMatch,
'1.3.6.1.4.1.1575.1.13.3.2.1': TUBS_IBR_LINUX_NETFILTER_MIB.lnfGeneralGroup,
'1.3.6.1.4.1.1575.1.13.3.2.2': TUBS_IBR_LINUX_NETFILTER_MIB.lnfNotificationGroup,
}
