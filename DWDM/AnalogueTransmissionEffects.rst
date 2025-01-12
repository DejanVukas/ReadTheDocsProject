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

In case of optical attenuation, -OSNR becomes too low - receiver cannot detect the signal from the noise.
To mitigate this effect we use amplifiers (e.g. EDFA amplifier), which amplifies all wavelengths at once, without terminating them.
We can use:

- booster or post-amplifier (on TX side),
- pre-amplifier (on RX side),
- in-line amplifier (in case of very long links).

We can use limited number of amplifiers on the line, because each amplifier degrades OSNR.

Colour dispersion - pulses of light spread out as they travel causing ISI (Inter Symbol Interference). Receiver cannot distinguish one pulse from another.
This is an issue only in 10Gb/s systems (and below), since they are intensity modulated.
Dispersion is compensated with DCM (Dispersion Compensation Module) which is special type of fiber, located at receiver end, which "undoes" pulse spreading.
In higher capacity systems we have coherent detection where colour dispersion is not an issue.

.. caution::
   Do not mix 10Gb/s (or lower) capacity waves in composite signal with 100Gb/s (or higher) capacity waves, since DCM module degrades performance of coherent detection.

Non-linear effects (e.g. Rayleigh scattering) - wavelengths can trample on other wavelengths.

Composite signal - that is the term used for all waves on the fiber.

Amplifier gain depends on:

#. input power, and
#. frequency of each wavelength.

i.e. it is not the same for all wavelengths in composite signal.

The same is applicable to amplifier noise as well!



