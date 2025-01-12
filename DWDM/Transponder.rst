Transponder
+++++++++++++++++

Baud rate: [symbols/second]
Modulation [bits/symbol] - QPSK (2 bits per symbol), 8PSK (3 bits per symbol), 16PSK (4 bits per symbol), 32PSK (5 bits per symbol), 64PSK (6 bits per symbol)

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
