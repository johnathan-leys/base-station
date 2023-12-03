#!/bin/bash

# Navigate to the directory where scripts are
cd /home/capstone # I think this is right? dont have pi rn

# Run grabber until it succeeds
until python Grabber_Scrape.py; do
    echo "Grabber failed, retrying..."
    sleep 15  
done

# Run the rest of the scripts in order
python Combine_Binary2.py
python Server.py
python FlaskRun.py
