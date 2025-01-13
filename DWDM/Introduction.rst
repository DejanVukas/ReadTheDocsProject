Introduction
+++++++++++++

.. note::
   These notes are taken from these videos: 

   #. `Optical Networking / DWDM Basics (Dense Wave Division Multiplexing) <https://www.youtube.com/watch?v=T31CQ3KdDN0&t=1268s>`_
   #. `Tutorial: Everything You Always Wanted to Know About Optical Networking <https://nanog.org/news-stories/nanog-tv/top-talks/tutorial-everything-you-always-wanted-know-about-optical-networking/>`_ 

Fiber cable is a waveguide for light.

The speed of light in any particular material is expressed as a ratio of speed of light in vacuum and that material refractive index, n.

When light is passing from one medium to another with a different index of refraction, a total reflection can occur instead.

Fiber cable consists of two layers:

#. core
#. cladding

Cladding always has a higher index of refraction than the core.

If the source of light into the fiber has incident angle within the "acceptance cone", total reflection occurs at the edge between core and cladding.

The vast majority of deployed fiber optic systems operate as "duplex" or as a fiber pair.

But, fiber is perfectly capable of carrying many signals, in both directions, over a single strand. It just requires more expensive optical components to do so. It is typically reserved for systems where the fiber in question is relatively expensive (e.g. fiber going across the ocean).

Modulation
============

The simplest and cheapest method is IMDD (Intensity Modulation with Direct Detection). It is typically encoded as "NRZ" (Non-Return to Zero), which means: "bright for a 1, dim for a 0". This technique was used for all optical signals up to 10Gbps.

Coherent modulations (QPSK, 8PSK, 16PSK, 32PSK, and 64PSK) are used for 100Gbps and higher bit rates.

Fiber Types
============

#. Multi-Mode Fiber (MMF)
#. Single-Mode Fiber (SMF)

Multi-Mode Fiber (MMF)
--------------------------

Multi-Mode Fiber has been designed for use with "cheaper" light sources.

MMF has extremely wide core (~50 micro meters), allowing the use of less prcisely focused, aimed and calibrated light sources.

This comes at the expence of shorter link distance.

Fiber is so named because it allows multiple "modes" of light to propagate.

Modal distortions typically limit distances to "tens to hundreds" of meters.

Types of Multi-Mode Fiber:

#. OM1/OM2 (orange fiber jacket)
#. OM3/OM4 (light blue fiber jacket)

OM1/OM2 has been originally designed for 100M/1310nm signals. Starts to fail at 10Gbps speeds.

OM3/OM4 has been designed for 850nm short reach laser sources. Supports 10Gbps signals at much longer distances (300-550m).
Required for 40G/100G signals (100-150m).

Single-Mode Fiber (SMF)
--------------------------

SM fiber is used for high bandwidths and long distances.

Has a much smaller core size, 8-10 micro meters. It prevents other modes from propagating along the fiber cable.

Can easily transmit a signal several thousends kilometers (with appropriate amplification), without requiring regeneration.

Typlically supports distances of ~80km even without amplification.

Types of Single-Mode Fiber:

#. OS1 (for indoor use),
#. OS2 (for buried use),
#. "Classic" SMF (a.k.a. SMF-28, NDSF - Non-Dispersion Shifted Fiber), ITU-T G.652,
#. Low Water Peak Fiber, ITU-T G.652.C/D,
#. Dispersion Shifted Fiber (DSF), ITU-T G.653,
#. Low-Loss Fiber, ITU-T G.654, (for submarine cables, low attenuation at the expense of dispersion)
#. Non-Zero Dispersion Shifted Fiber, ITU-T G.655,
#. Bend Insensitive Fiber, ITU-T G.657 (in data centers).

OS1 is also called "tight buffered".

OS2 is also called "loose", because it is blown into the duct.

Fiber Optic Transmission Bands
==================================

.. list-table:: Fiber Optic Transmission Bands
   :widths: 25 25 25
   :header-rows: 1

   * - Wavelength [nm]
     - Code
     - Usage
   * - 850
     - /
     - Highest attenuation, used only for short reach (up to 100m)
   * - 1310
     - O-band
     - The point of zero dispersion on classic SMF, but high attenuation.
       
       Primarily used for medium reach applications (up to 10km)
   * - 1550
     - C-band
     - Stands for Conventional band. Covers 1525nm-1565nm. 
       
       Has the lowest attenuation over SMF.
       
       Used for long-reach and DWDM applications.
   * - 1570-1610
     - L-band
     - Stands for Long band. Used for submarine systems.


DWDM
------

.. list-table:: DWDM Wavelength Ranges
   :widths: 25 25 25
   :header-rows: 1

   * - Wavelength
     - Min. Wavelength [nm]
     - Max. Wavelength [nm]
   * - C-band
     - 1528
     - 1568
   * - L-band
     - 1568
     - 1610

Gray optics: 1310nm

DWDM is the only system that delivers:

#. increased capacity and
#. increased distance

DWDM grid is defined by ITU-T G.694.1 standard.

CWDM (Coarse Wavelength Division Multiplexing)
---------------------------------------------------

The actual signal in a CWDM system isn't really any wider - the wide channel allows for large temperature variations. Cheaper, uncooled lasers can more easily stay within the window.

Wavelength of the laser is not stable as it heats-up and cools-down.

WDM
------

It is possible to buy cheap equipment which will combine 1310 and 1550nm wavelengths (used in gray optics).

OTN
=====

Optical Transport Network (OTN) is a set of standards allowing interoperability and the generic transport of any protocol across an optical network.

