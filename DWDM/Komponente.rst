Komponente
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
============

Has many lower-speed client ports (1GE and/or 10GE) and single higher-speed wave port (100G OTU4 wave).

Functions:
---------------
- terminates client optics
- wraps each client signal in its own OTN container.
- multiplexes many low-order OTN containers (1GE into ODU0 and 10GE into ODU2) into one bigger high-order OTN container. Adds FEC to achieve distance.
- transmits the high-order OTN container on the correct wavelength.

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