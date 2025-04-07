Introduction
++++++++++++++++++

.. note::
   These notes are taken from these sites/videos: 
   
   #. `Fundamentals of PON: The Optical LAN Solution <https://www.youtube.com/watch?v=KMI-s5m53fY>`_
   #. `Understand GPON Technology <https://www.cisco.com/c/en/us/support/docs/switches/catalyst-pon-series/216230-understand-gpon-technology.html>`_ 
   
GPON (Gigabit Passive Optical Network) is an alternative to Ethernet switching in campus networking. GPON replaces the traditional three-tier Ethernet design with a two-tier optic network which eliminates access and distribution Ethernet switches with passive optical devices.

.. image:: /GPON/Photos/NetworkingGPON.avif

GPON adopts WDM to transmit data of different upstream/downstream wavelengths over the same ODN (Optical Distribution Network).

Data is broadcast in the downstream direction, and in the upstream direction data is burst in TDMA mode (based on timeslots).

Downstream packets are forwarded as broadcasts, with the same data sent to all the same ONU/ONT with different data identified by the GEM port ID (GEM - GPON encapsulation method).

Maximum differential fiber distance: 20km

PON topology (point-to-multipoint (P2MP) scheme) and point-to-point (P2P) architecture

.. image:: /GPON/Photos/P2MP_P2P.png

Benefits
=============

#. Fiber delivers better investment protection with superior extended life
#. Fiber technology offers graceful migration from gigabit to 100 gigabits
#. Fiber cabling is more secure, reliable and has greater reach than copper
#. Fiber in buildings and outside plant is technology independent
#. Fiber, such as Single Mode Fiber, has no known bandwidth capacity limits.