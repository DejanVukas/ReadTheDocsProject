Protection Schemes in Optical Networks
++++++++++++++++++++++++++++++++++++++++++

L1 Protection - wavelength protection
======================================

Optical splitters (50:50)

Optical protection - split your signal in half and send down two different fiber paths. On the RX side use an optical switch with power monitoring capabilities on the receiver, have it automatically pick from the strongest signal.

SNCP (SubNetwork Connection Protection)
-------------------------------------------

SNCP can protect from equipment failures and fiber cut.
Simply put, SNCP means: dual sending and selective receiving

SNCP operates at the subnetwork connection level, which refers to a specific path or connection between two nodes in the network.

SNCP has two types:

#. O-SNCP (Optical), and
#. E-SNCP (Electrical).

O-SNCP can be implemented by assigning 2 different devices and routes for the same optical signal.
For traffic protection we send the same signal twice and selectively receive the main.
It’s called dual sending & selective receiving in Huawei or as Nokia called it head end bridging and tail end switching.

We have 2 options available to implement O-SNCP:

#. Through Y cable, and
#. Through OPS card (Optical Protection Switching).

In OPS we have the chance to Improve the survivability by placing the main and standby transponder in 2 different shelves.

.. image:: /DWDM/Photos/O_SNCPwithY_Cable.jpeg

L2 Switching - Service Protection
======================================

MPLS-TP Tunneling

- Establishes **Working** and **Protect** route upon creation
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

