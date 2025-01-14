Protection Schemes in Optical Networks
++++++++++++++++++++++++++++++++++++++++++

L1 Protection - wavelength protection
======================================

L2 Switching - Service Protection
======================================

MPLS-TP Tunneling

- Establishes Working and Protect route upon creation
- All traffic uses Working route until a fault is declared
- Upon fault, all traffic immediately switches to Protect route
- Reversion can be automatic or manual

Simple and reliable - sub 50ms failover time

Working and Protect path are preconfigured.

We are building tunnels. Tunnels contain services. In case of failure, we switch to Protect tunnel (containing all the services).

L2 Switching - Traffic Engineering
====================================

VLAN Tagging
----------------

-  Allows traffic identification and
-  Management on a per flow basis

We can aggregate traffic - e.g. we aggregate multiple 1Gb/s to 10Gb/s link and keep traffic separate based on the VLAN tags.

Quality of Service
----------------------

- Prioritize traffic in terms of importance,
- High priority traffic can be forwarded first,
- Lower priority traffic is handled 'best effort'.

Bandwidth Profiles
-------------------

- Allows Customer Service a Guaranteed rate plus the ability to burst higher.
- Can be used to strictly define traffic flows.

e.g. Bandwidth profile could consist of three traffic categories:

- Guaranteed,
- Burstable,
- Drop susceptible.

L3 Routing
================

The most expensive solution

IP addressing used for node identification.

We use them on site which are connected to the rest of the world.

EVPN (Ethernet VPN)
-----------------------

Active-Active mode of operation (Active and Protect part are used to transport payload). That's way it is better than MPLS-TP.

Multi-homing

EVPN allows MAC-Mobility - network lets you move within the same L2 network.

