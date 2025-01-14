Transponder
+++++++++++++++++

Baud rate: [symbols/second]

.. list-table:: Modulations
   :widths: 25 25
   :header-rows: 1

   * - Modulation [bits/symbol]
     - Bits per symbol
   * - QPSK
     - 2
   * - 8PSK
     - 3
   * - 16PSK
     - 4
   * - 32PSK
     - 5
   * - 64PSK
     - 6

Line rate [bits/second] = Baud rate x Modulation x 2 polarizations

Example: "100"Gb/s line = 34GBaud x 2 bits/symbol x 2 polarizations

Trade-off:

#. Increasing baud rate:
	#. increases spectrum required
	#. improves transceiver efficiency (bits/device)
#. Increasing modulation:
	#. improves spectral efficiency (bits/Hz)
	#. decreases distance (higher modulation scheme means there are more points in signal constellation and it becomes more difficult to correctly detect them on receiving end)

Damage by Overpowered Transmitters?
=========================================

Actually, most optics transmit at roughly the same power. The typical output of 10km vs 80km optics are within 3db.

Long reach optics achieve their distances by having extremely sensitive receivers, not stronger transmitters. 80km optics may have a 10dB+ more sensitive receiver than 10km. These sensitive receivers are what are in danger of burning out.

There are two thresholds you need to be concerned with:

#. Saturation point (where the receiver is "blinded", and takes errors),
#. Damage point (where the receiver is actually damaged).

Generally speaking, only 80km optics are at risk.

.. image:: /DWDM/Photos/TransceiverPowerRanges.png