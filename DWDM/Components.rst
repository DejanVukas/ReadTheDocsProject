Components
+++++++++++++

#. Transponder
#. Muxponder (Multiplexing Transponder)
#. OTN Switching
#. Line System

Transponder
============

Has single client (gray optics) port (10GE client) and single wave port (10G OTU2 wave, wavelength in the 1550nm window).

Functions:
---------------
- wraps the client signal in an OTN frame (electronics). Adds FEC to achieve distance. Does not change Ethernet VLANs and IP packets.
- transmits the OTN-wrapped client on the correct wavelength

Muxponder (Multiplexing Transponder)
========================================

Mux/Demux is a simple device which combines or splits multiple colors or light into a single fiber.
Muxes are entirely passive devices, requiring no power.

A complete system requires a mux+demux for TX and RX.

Muxes are actually optical bandpass filters, typically based on Bragga Grating - some frequencies are reflected, the rest are passed through.

Muxponder has many lower-speed client ports (1GE and/or 10GE) and single higher-speed wave port (100G OTU4 wave).

Functions:
---------------
- terminates client optics
- wraps each client signal in its own OTN container.
- multiplexes many low-order OTN containers (1GE into ODU0 and 10GE into ODU2) into one bigger high-order OTN container. Adds FEC to achieve distance.
- transmits the high-order OTN container on the correct wavelength.

Optical Add/Drop Multiplexer (OADM)
====================================

Selectively adds and drops certain WDM channels, while passing other channels through without disruption.

Mux/Demux is used at the end-point of a WDM network to split all of the component wavelengths, an OADM is used at a mid-point, often in a ring.

It can be:
#. FOADM, or
#. ROADM

ROADM is essentially a "software tuneable OADM".

Some ROADMs are multi-degree - you can choose more than 2 directions (so called East and West) to pass the signal to. This allows you to build complex star topologies at a purely optical level.

OTN Switching
===============

Has many lower-speed client ports (1GE and/or 10GE) and many higher-speed wave ports (100G OTU4 wave).

Functions:
-----------

- terminates client optics
- wraps each client signal in its own OTN container.
- Rearranges OTN containers "any to any"
- ODU cross-connecting - hairpinning, passthrough, add/drop
- transmits the OTN container on the correct wavelength.

Optical Switches
------------------

Optical Switches let you direct light between ports, without doing O-E-O (Optical-Electrical-Optical) conversion.

Built with an array of tiny mirrors, which can be moved electrically.

Allows you to connect two fibers together optically in software.

Becoming popular in optical cross-connect and fiber protection roles.

Line System
=============

Functions:
--------------

- combining many waves together onto a single fiber to achieve capacity (wavelength division multiplexing)
- manipulating wavelengths:
    - added/dropped/passed through/switched
    - optical ADM
    - ROADM (Reconfigurable Optical Add/Drop Multiplexer)
- fixing the effects of analog transmission (amplification and dispersion compensation)

DWDM started in long haul, penetrated metro, now in access.

Circulator
=============

A component typically not seen by the end user. Used in muxes, OADMs, and dispersion compensators.

A circulator has 3 fiber ports:

- Light coming in port 1 goes out port 2,
- Light coming in port 2 goes out port 3.

Optical Splitters and Optical Taps
====================================

They split the signal.

Use cases:
#. Optical protection (50/50 splitter)
#. Optical performance monitoring (99/1 splitter)

Optical protection - split your signal in half and send down two different fiber paths. On the RX side use and optical switch with power monitoring capabilities on the receiver, have it automatically pick from the strongest signal.

Optical performance monitoring - tap 1% of the signal and run it to a spectrum analyzer.

44:55