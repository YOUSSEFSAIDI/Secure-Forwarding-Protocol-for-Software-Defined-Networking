# Secure Forwarding Protocol for Software-Defined Networking

The Security Protocols and Applied Cryptography Group of the Digital Security
department in EURECOM currently is involved in a project aiming at design
secure protocols for packet forwarding. These protocols ensure that packets
correctly follow dedicated paths over the network. The team has been
investigating a new protocol for packet forwarding based on digital signatures.
Informally, a packet contains a signature that is updated at each visited host of
the network.

The aim of this project is to come up with a prototypical implementation
of this secure forwarding solution within the Software Defined Networking (SDN)
architecture. The solution will be integrated with SDN’s packet forwarding
mechanisms with an extension of OpenFlow protocols using Mininet as the target
environment.

SDN has been widely developed to simplify the management and control over
large networks, thanks to the separation of the control plane and data plane.
OpenFlow, that enables SDN, is a communication protocol that allows network
controllers to determine the path of a packet across network switches.
Mininet is an emulator that can create a realistic virtual network. It runs a set of
end hosts, switches, routers and links on a single machine.
