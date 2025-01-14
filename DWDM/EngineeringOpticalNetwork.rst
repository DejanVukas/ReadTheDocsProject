Engineering Optical Network
++++++++++++++++++++++++++++++++

Insertion Loss
=================================

Even the best connectors and splices aren't perfect - they introduce loss.

The typical budgetary figure is 0.5dB per connector.

Insertion loss refers to the fiber optic light loss caused when a fiber optic component insert into one another to form the fiber optic link. 
Absorption, misalignment or air gap between the fiber optic components are the main cause contribution to Insertion Loss.



Insertion loss is also used to describe loss from muxes. It is the "penalty you pay just for inserting the fiber".

Real-life examples:

- 40-channel DWDM 100GHz Mux/Demux: 3.5dB,
- 80-channel DWDM 50GHz Mux/Demux: 9.5dB.

Root cause:

- Mismatched cores,
- Misaligned cores,
- Air gap between fibers.

.. image:: /DWDM/Photos/InsertionLoss.jpg

Optical Link budget
========================

Start with Pout. Deduct fiber loss, splice loss, connector loss, and margin. The result must be bigger than receiver sensitivity.

It's smart to leave some margin in your designs:

- patch cables get bent,
- optic transmitter will cool with age (output power goes down, e.g. from 3dBm to -1dBm),
- fiber cut fix will add more splices, etc.

.. image:: /DWDM/Photos/Power-and-Link-Loss-Budget.jpg

Amplifiers and Power Balance
===============================

Amplifier gain is not consistent across all wavelengths.

The gain must be equalized, or after several amplification stages the power of some channels will be far higher.

Amplifiers also have limits on their **total system power** - both what they can **output** and what they can take as **input**.

But the total input power changes as you add channels.

.. caution::
   A single DWDM channel at 10dBm is 10 mW of input power. (Dejan: in video it is stated that it is 0.1mW and not 10mW! Double check!)
   
   40 DWDM channels at 10dBm is 400mW of power or 26dBm!

   Do not sum up values in dBm, but absolute values in mW (i.e. it is not 40 x 10dBm, but 40 x 10mW)

   10 x log(40 x 10) = 10 x (log40 + log10)

Once you know:

- the amplifier's maximum input power, and
- the number of channels in DWDM,

you can calculate the maximum power of single DWDM channel.

Failing to plan for this can cause problems as you add channels.

Dispersion Compensation Unit
=================================

Essentially, it is just big spool of fiber in a box.

It is designed to cause dispersion in the opposite direction as the transmission fiber used.

But it also adds extra distance to the normal fiber path, causing additional attenuation, requiring more amplification.

There is also electronic dispersion compensation (EDC). Dispersion is compensated for electronically at the receiver.

Re-amplifying, Reshaping, Retiming
========================================

- 1R - Re-amplifying
  
  makes the analog signal stronger (i.e. makes the light brighter). Performed by amplifier.
- 2R - Reshaping
  
  Restores the original pulse shape
- 3R - Retiming
  Restores the original timing between the pulses. Usually involves an O-E-O conversion.


Bit Error Rates
==================

The target maximum BER is generally 10 exp(-12).

Coherent Optical Technologies
===============================

Coherent optics are a group of advancements in optical technology, which combine to deliver significantly increased optical performance.

Coherent technologies generally consist of:

- polarization multiplexing,
- high-order phase modulation techniques,
- using a laser as a local reference oscilator on the receive side,
- advanced Digital Signal Processing (DSPs) which are necessary to tie all of these together, recombine signals, and compensate for impairments.

These technologies combined deliver:

- significantly improved spectrum efficiency (went from 1.6 Tbps to 9.6 Tbps)
- true 100G/200G and beyond optical signals, not just N x 10G signals,
- eliminate the need for physical Dispersion Compensation Units.

Improved Modulation techniques
===================================

Previously optical systems used IM-DD modulation - "bright for 1, dim for 0".

This yields only 1 data bit per "symbol".

Adding bandwidth by increasing clock cycles has limitations.

Improving the modulation technique yields more bits per symbol.

- QPSK delivers 2 bits per symbol,
- 8PSK delivers 3 bits per symbol, et.

Polarization multiplexing
=============================

Light is electromagnetic wave.

In 3-dimensional space (e.g. a cylindrical fiber), you can send two independent orthogonal signals which propagate along a X and Y axis, without interfering each other.

Polarization multiplexing doubles the bandwidth per channel.