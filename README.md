# base-station
Base station for University of Maine ECE senior project.

Working alongside UMaine Marine Science department to develop a base station that will wirelessly charge, transfer/display data from whale-monitoring hydrophone.

Uses various Python libraries to pull data from ESP32 (hydrophone's web server) and combine and display the data.

A Raspberry Pi HAT PCB is providing power to the Pi and wirelessly charging the hydrophone capsule. The pi can determine when to start/stop charging the capsule based on battery level.
