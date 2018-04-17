#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False)

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h5 = net.addHost('h5', cls=Host, ip='192.168.6.3', defaultRoute='via 192.168.6.1')
    h3 = net.addHost('h3', cls=Host, ip='192.168.5.3', defaultRoute='via 192.168.5.1')
    h4 = net.addHost('h4', cls=Host, ip='192.168.6.2', defaultRoute='via 192.168.6.1')
    h1 = net.addHost('h1', cls=Host, ip='192.168.4.2', defaultRoute='via 192.168.4.1')
    h2 = net.addHost('h2', cls=Host, ip='192.168.5.2', defaultRoute='via 192.168.5.1')

    info( '*** Add links\n')
    net.addLink(s1, h1)
    net.addLink(s2, h2)
    net.addLink(s2, h3)
    net.addLink(s3, h5)
    net.addLink(s3, h4)
    net.addLink(s1, s2)
    net.addLink(s2, s3)

    info( '**** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s3').start([c0])
    net.get('s2').start([c0])
    net.get('s1').start([c0])

    info( '*** Post configure switches and hosts\n')
    s3.cmd('ifconfig s3 192.168.6.5')
    s2.cmd('ifconfig s2 192.168.5.5')
    s1.cmd('ifconfig s1 192.168.4.5')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

