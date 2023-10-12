# This script should grab the data files from the ESP32 web server.

import requests #needed to get the data
import time

# IP address on the Whale network
esp32_ip = '192.168.4.1'

wifi_ssid = 'Whale'     # Going off of memory...
with open('.password', 'r') as file:
    password = file.read().strip()

# List of filenames. Likely will need to dynamically update when fully ready. 
# Could also use something like BeautifulSoup to scrape for all the files...
files_to_download = ['10061425.bin', '01010000.bin']  # right now only 2 file names

session = requests.Session()
session.auth = (wifi_ssid, password)    # should connect to AP

for filename in files_to_download:
    file_url = "http://" + str(esp32_ip) + "/" + str(filename)
    # I think https part might be needed to specify protocol as esp32 is the AP...

    # Record the start time for speed calc
    start_time = time.time()


    # Send an HTTP GET request to download the file
    file_response = requests.get(file_url)

    end_time = time.time() 

    if file_response.status_code == 200:    # "indicates that the request has succeeded"

        # Calculate the file size/download speed
        file_size = len(file_response.content)
        download_time = end_time - start_time
        download_speed = file_size / download_time
        
        local_filename = f'local_{filename}' #append local_ to front

        # Write the content of the response to the local file
        with open(local_filename, 'wb') as file:
            file.write(file_response.content)
        
        print("File " + str(filename) + " downloaded successfully")
        print("Download Speed " + str(download_speed) + " bytes/sec")
    else:
        print("Failed to download file " + str(filename) + ". Status code: " + str(file_response.status_code))
