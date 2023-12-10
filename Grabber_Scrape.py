import requests
import time
import subprocess
from bs4 import BeautifulSoup
import sys

# Connect to ESP32 Wi-Fi AP
def connect_to_wifi(ssid, password):
    try:
        # For Windows | This only works when previously connected to network, have pw saved
        subprocess.run(["netsh", "wlan", "connect", f"name={ssid}"], check=True) #normally name is ssid
        # For linux using nmcli: Might need sudo
        # subprocess.run(["nmcli", "device", "wifi", "connect", ssid, "password", password], check=True)
        # sudo apt-get install network-manager 

        print(f"Attempting conn to {ssid}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to {ssid}: {str(e)}")
        return False
    return True

def download_files(ip_address, file_names):
    base_url = f"http://{ip_address}"
    for file_name in file_names:
        try:
            time.sleep(1)
            # Creating data for POST request
            data = {'download': f'download_{file_name}'}
            
            # Sending POST request to initiate download
            response = requests.post(base_url, data=data) 
            
            # Checking response status and writing file if successful
            if response.status_code == 200:
                with open("Binary/" + file_name, 'wb') as f: 
                    f.write(response.content)
                print(f"File {file_name} downloaded successfully")
            else:
                print(f"Failed to download {file_name}: {response.status_code}")
        except requests.RequestException as e:
            print(f"HTTP request failed: {str(e)}")

#   Use bsoup to parse html and grab the files to download
def extract_file_names(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    download_buttons = soup.find_all('button', attrs={'name': 'download'})
    file_names = [btn['value'].replace('download_', '') for btn in download_buttons]
    return file_names

if __name__ == "__main__":
    ssid = "Whale"
    password = "NARWWWWW"
    ip_address = "192.168.4.1"

     # Connect to Wi-Fi
    if connect_to_wifi(ssid, password):
            # Fetch the Server.html content using an HTTP request
        try:
            response = requests.get(f"http://{ip_address}")
            server_html_content = response.text
        except requests.RequestException as e:
            print(f"Failed to fetch Server.html content: {str(e)}")
            sys.exit(1) # should count as failture for bash script
        
        # Extract file names from the Server.html content
        file_names = extract_file_names(server_html_content)
        time.sleep(5)
        download_files(ip_address, file_names)
    
   
    
   