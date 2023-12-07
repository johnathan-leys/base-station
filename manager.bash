#!/bin/bash

# Navigate to the directory where scripts are
cd /home/capstone # I think this is right? dont have pi rn

raspi-gpio set 5 op dh  # turn on charging

raspi-gpio set 23 op dh # turn on "running" LED

# Run grabber until it succeeds
until python Grabber_Scrape.py; do
    echo "Grabber failed, retrying..."
    sleep 15  
done

# Run the rest of the scripts in order
python Combine_Binary2.py

export BOKEH_BROWSER=/usr/bin/chromium-browser    # When using pi with display, opens in browser

python Server.py
python FlaskRun.py

raspi-gpio set 24 op dh  # turn on "ready" LED
raspi-gpio set 23 op dl 
