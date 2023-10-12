# This script will probably need permissions... sudo on pi or run as admin windows
import requests
import subprocess
import time

# Connect to ESP32 Wi-Fi AP
def connect_to_wifi(ssid, password):
    try:
        # For Windows
        subprocess.run(["netsh", "wlan", "connect", f"name={ssid}", f"key={password}"], check=True)
        # For linux using nmcli:
        # subprocess.run(["nmcli", "device", "wifi", "connect", ssid, "password", password], check=True)
        # sudo apt-get install network-manager 

        print(f"Connected to {ssid}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to {ssid}: {str(e)}")
        return False
    return True

# Send HTTP request and download files
def download_files(ip_address, file_paths):
    base_url = f"http://{ip_address}"
    for file_path in file_paths:
        try:
            response = requests.get(f"{base_url}/{file_path}")
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f"File {file_path} downloaded successfully")
            else:
                print(f"Failed to download {file_path}: {response.status_code}")
        except requests.RequestException as e:
            print(f"HTTP request failed: {str(e)}")


if __name__ == "__main__":
    # Wi-Fi creds
    ssid = "Whale"
    with open('.password', 'r') as file:
        password = file.read().strip()

    ip_address = "192.168.4.1" #I think this is right
    
    # Paths of the files to download
    file_paths = ["file1.bin", "file2.bin"]  # Not sure what the filepaths would be
    
    # Connect to Wi-Fi
    if connect_to_wifi(ssid, password):
        # Give it a moment to establish a connection
        time.sleep(8)
        # Download files
        download_files(ip_address, file_paths)
