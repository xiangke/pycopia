#! python
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
# License: LGPL
# Author unknown. Found on snippets site
# $Id$

import array, fcntl, struct, socket, sys

class IfConfig(object):
    """Access to socket interfaces"""

    SIOCGIFNAME = 0x8910
    SIOCGIFCONF = 0x8912
    SIOCGIFFLAGS = 0x8913
    SIOCGIFADDR = 0x8915
    SIOCGIFBRDADDR = 0x8919
    SIOCGIFNETMASK = 0x891b
    SIOCGIFCOUNT = 0x8938

    IFF_UP = 0x1                # Interface is up.
    IFF_BROADCAST = 0x2         # Broadcast address valid.
    IFF_DEBUG = 0x4             # Turn on debugging.
    IFF_LOOPBACK = 0x8          # Is a loopback net.
    IFF_POINTOPOINT = 0x10      # Interface is point-to-point link.
    IFF_NOTRAILERS = 0x20       # Avoid use of trailers.
    IFF_RUNNING = 0x40          # Resources allocated.
    IFF_NOARP = 0x80            # No address resolution protocol.
    IFF_PROMISC = 0x100         # Receive all packets.
    IFF_ALLMULTI = 0x200        # Receive all multicast packets.
    IFF_MASTER = 0x400          # Master of a load balancer.
    IFF_SLAVE = 0x800           # Slave of a load balancer.
    IFF_MULTICAST = 0x1000      # Supports multicast.
    IFF_PORTSEL = 0x2000        # Can set media type.
    IFF_AUTOMEDIA = 0x4000      # Auto media select active.

    def __init__(self):
        # create a socket so we have a handle to query
        self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def _fcntl(self, func, args):
        return fcntl.ioctl(self.sockfd.fileno(), func, args)

    def _getaddr(self, ifname, func):
        ifreq = (ifname + '\0'*32)[:32]
        try:
            result = self._fcntl(func, ifreq)
        except IOError:
            return None

        return socket.inet_ntoa(result[20:24])

    def getInterfaceList(self):
        """ Get all interface names in a list
        """
        # get interface list
        buffer = array.array('c', '\0' * 1024)
        ifconf = struct.pack("iP", buffer.buffer_info()[1], buffer.buffer_info()[0])
        result = self._fcntl(self.SIOCGIFCONF, ifconf)
        
        # loop over interface names
        iflist = []
        size, ptr = struct.unpack("iP", result)
        for idx in range(0, size, 32):
            ifconf = buffer.tostring()[idx:idx+32]
            name, dummy = struct.unpack("16s16s", ifconf)
            name, dummy = name.split('\0', 1)
            iflist.append(name)

        return iflist

    def getFlags(self, ifname):
        """ Get the flags for an interface
        """
        ifreq = (ifname + '\0'*32)[:32]
        try:
            result = self._fcntl(self.SIOCGIFFLAGS, ifreq)
        except IOError:
            return 0

        # extract the interface's flags from the return value
        flags, = struct.unpack('H', result[16:18])

        # return "UP" bit
        return flags

    def getAddr(self, ifname):
        """ Get the inet addr for an interface
        """
        return self._getaddr(ifname, self.SIOCGIFADDR)

    def getMask(self, ifname):
        """ Get the netmask for an interface
        """
        return self._getaddr(ifname, self.SIOCGIFNETMASK)

    def getBroadcast(self, ifname):
        """ Get the broadcast addr for an interface
        """
        return self._getaddr(ifname, self.SIOCGIFBRDADDR)

    def isUp(self, ifname):
        """ Check whether interface 'ifname' is UP
        """
        return (self.getFlags(ifname) & self.IFF_UP) != 0


if __name__ == "__main__":
    ifc = IfConfig()
    ifaces = ifc.getInterfaceList()
    for name in ifaces:
        print "%s is %s, addr %s, mask %s, bcast %s" % (name, ('DOWN', 'UP')[ifc.isUp(name)], 
            ifc.getAddr(name), ifc.getMask(name), ifc.getBroadcast(name))
