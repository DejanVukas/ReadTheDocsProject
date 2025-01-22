Analogue Transmission Effects
+++++++++++++++++++++++++++++++

.. list-table:: Analogue Transmission Effects
   :widths: 25 25
   :header-rows: 1

   * - Effect
     - Mitigation
   * - Optical Attenuation (Loss)
     - Amplifiers
   * - Dispersion
     - Dispersion compensation
   * - Non-linear effects
     - Overcome it with proper optical network design
   * - The fiber is physically damaged
     - Automated network, OTDR measurements.

Optical Attenuation
=====================

Quite simply, optical power is the brightness (or "intensity") of light.

As light travels through fiber, some energy is lost:

- it can be absorbed by glass particles (and converted into heat), or
- scattered by microscopic imperfections in the fiber.

This loss of intensity is called attenuation.

Decibel
------------

Optical power is measured in decibels (dB). A decibel is a logarithmic-scale unit expressing the relationship between two values.

The decibel is a dimensionless-unit, meaning it does not express an actual physical measurement on its own.

Gain in dB = 10 log Pout/Pin

- -10dB gain means Pout is 1/10th of the Pin
- -20dB gain means Pout is 1/100th of the Pin
- 3dB gain means Pout is double of the Pin,
- -3dB gain means Pout is half of the Pin.

To express an absolute value, we need a reference value. In optical networking it is 1mW. 

dBm - decibel relative to 1mW

- 0dBm is 1mW
- 3dBm is 2mW,
- -3dBm is 0,5mW

Why do we measure light with the Decibel?

Light, like sound, follows the inverse square law: the signal is inversely proportional to the distance squared.

A signal travels distance X and loses half of its intensity. The signal travels another distance X and loses another half. After 2X only 25% remains.

Using logarithmic scale simplifies the calculations: a -3dB change is approximately half the original signal. In the example above, there is a 3dB loss per distance X. At distance 2X there is 6dB of loss.

This allows us to use elementary school addition/subtraction when measuring **gain/losses**, which is easier.

Note
-----------

.. note::
   In absolute values, we multiply gains/losses along the way. In logarithmic values (like dB) we add/subtract them, because log(a x b) = loga +logb and log(a/b)=loga - logb!

Amplifiers
============

In case of optical attenuation, OSNR becomes too low - receiver cannot detect the signal from the noise.
To mitigate this effect we use amplifiers (e.g. EDFA amplifier), which amplifies all wavelengths at once, without terminating them.

EDFA amplifiers operate in C-band.

We can use:

- booster or post-amplifier (on TX side),
- pre-amplifier (on RX side),
- in-line amplifier (in case of very long links).

We can use limited number of amplifiers on the line, because each amplifier degrades OSNR.

Dispersion
=====================

Dispersion means "to spread out".

There are two main types of dispersion to deal with:

#. Chromatic Dispersion
#. Polarization Mode Dispersion

Chromatic Dispersion
----------------------

Different frequencies of light propagate through a non-vacum at slightly different speeds. This is why optical prisms work (i.e. on the other side of the prism we get different colors).

c = lambda x frequency

So, lower frequency light travels slower

Colour dispersion - pulses of light spread out as they travel causing ISI (Inter Symbol Interference). Receiver cannot distinguish one pulse from another.
This is an issue only in 10Gb/s systems (and below), since they are intensity modulated.
Dispersion is compensated with DCM (Dispersion Compensation Module) which is special type of fiber, located at receiver end, which "undoes" pulse spreading.
In higher capacity systems we have coherent detection where colour dispersion is not an issue.

.. caution::
   Do not mix 10Gb/s (or lower) capacity waves with 100Gb/s (or higher) capacity waves in composite signal, since DCM module degrades performance of coherent detection.

Polarization Mode Dispersion
-------------------------------

Polarization Mode Dispersion is caused by imperfection in shape of the fiber (not perfectly round). One polarization of light propagates faster than the other. Older fiber is particlularly affected. It may get worse with age.

Non-linear Effects
=====================

Non-linear effects (e.g. Rayleigh scattering) - wavelengths can trample on other wavelengths.

Composite signal - that is the term used for all waves on the fiber.

Amplifier gain depends on:

#. input power, and
#. frequency of each wavelength.

i.e. it is not the same for all wavelengths in composite signal.

The same is applicable to amplifier noise as well!



