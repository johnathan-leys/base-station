# This script should grab the data files from the ESP32 web server.

import requests #needed to get the data

# UPDATE THIS IF IP CHANGES
esp32_ip = '10.20.20.20'

# List of filenames. Likely will need to dynamically update when fully ready. 
# Could also use something like BeautifulSoup to scrape for all the files...
files_to_download = ['CONFIG.TXT', '01010000.bin']  # right now only 2 file names

for filename in files_to_download:
    file_url = "http://" + str(esp32_ip) + "/" + str(filename)
    # I think https part might be needed to specify protocol as esp32 is the AP...

    # Send an HTTP GET request to download the file
    file_response = requests.get(file_url)

    if file_response.status_code == 200:    # "indicates that the request has succeeded"
        
        local_filename = f'local_{filename}'

        # Write the content of the response to the local file
        with open(local_filename, 'wb') as file:
            file.write(file_response.content)
        
        print("File " + str(filename) + " downloaded successfully")
    else:
        print("Failed to download file " + str(filename) + ". Status code: " + str(file_response.status_code))
