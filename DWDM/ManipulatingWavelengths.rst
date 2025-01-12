Manipulating Wavelengths
+++++++++++++++++++++++++++


#. Point-to-point only:
	- all waves going in Site A come out at Site B
#. FOADM - Fixed Optical Add/Drop Multiplexer
	- cheap hardware, but requires manual configuration on Site B
	- add/drop pre-determined channels at intermediate sites and pass remaining channels through without demultiplexing
#. ROADM - Reconfigurable Optical Add/Drop Multiplexer
	- automates wave manipulation to create larger networks
	- it contains WSS (Wavelength Selective Switch)
	- it can add/drop/pass-through wavelengths via remote provisioning
	- you can reconfigure the paths to avoid cable cuts or create maintenance window

Types of ROADMs:

#. Static,
#. Colorless (C),
#. Colorless-Directionless (CD),
#. Colorless-Directionless-Contentionless (CDC).

In Static ROADM port is tied to Direction (East or West), and Colour (wavelength).

In Colorless ROADM port is tied to direction only (we can pick any colour).

In Colorless/Directionless ROADM port is not tied to any direction and any colour. Only one drop port can occupy a colour (drop side contention).

In Colorless/Directionless/Contentionless ROADM port is not tied to any direction, any colour and many ports can occupy a colour (eliminates drop side contention).

Trade-off flexibility for cost!