import requests
import time
import subprocess

# Connect to ESP32 Wi-Fi AP
def connect_to_wifi(ssid, password):
    try:
        # For Windows | This only works when previously connected to network, have pw saved
        subprocess.run(["netsh", "wlan", "connect", f"name={ssid}"], check=True) #normally name is ssid
        # For linux using nmcli:
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

if __name__ == "__main__":
    # Wi-Fi creds
    ssid = "Whale"
    password = "NARWWWWW"
    
    # ESP32 web server IP address
    ip_address = "192.168.4.1"  
    
    # Names of the files to download
    file_names = ['1.bin', '2.bin', '3.bin', '4.bin', '5.bin']  # change names
    
    # Connect to Wi-Fi
    if connect_to_wifi(ssid, password):
        time.sleep(5)  # Waiting for the connection to stabilize
    
        # Download files
        download_files(ip_address, file_names)
