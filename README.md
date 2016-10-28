# Project 5: Leaflet Map

### AUTHOR: Brian Leeson, bel@cs.uoregon.edu

## This repo was modified from a cloned and then gutted repo written by:
## Brandon Sov , bhs@cs.uoregon.edu ###

## Description ##
Project runs a server that serves a leaflet map with points of interest as markers.

## Installation and running ##
Deployment should work "out of the box" with this command sequence:
	sudo apt-get install python3-venv
	git clone <gitURL>
	cd to the cloned repository
	make configure
	make run

The default port is 5000. If your are on your own machine connect at localhost:5000. 
If the server is running another machine connect at <OtherMachineIP>:5000.

## Testing the application ## 
Test this server by following the RUNNING instructions and attempt to connect to the server.

To run automated tests:
	make test
