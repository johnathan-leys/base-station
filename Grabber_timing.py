import requests
import time
import os

def download_files(ip_address, file_names):
    base_url = f"http://{ip_address}"
    total_speed = 0
    successful_downloads = 0

    for file_name in file_names:
        try:
            time.sleep(1)  # Waiting for 1 second as per your original design

            # Creating data for POST request
            data = {'download': f'download_{file_name}'}
            
            # Record start time
            start_time = time.time()

            # Sending POST request to initiate download
            response = requests.post(base_url, data=data) 
            
            # Record end time
            end_time = time.time()

            # Checking response status and writing file if successful
            if response.status_code == 200:
                file_path = "Binary/" + file_name
                with open(file_path, 'wb') as f: 
                    f.write(response.content)

                download_time = end_time - start_time  # Calculate download time
                file_size = os.path.getsize(file_path)  # Get file size in bytes
                speed = file_size / download_time  # Speed in bytes per second

                total_speed += speed  # Add to total speed
                successful_downloads += 1

                print(f"File {file_name} downloaded successfully at {speed} bytes/sec")
            else:
                print(f"Failed to download {file_name}: {response.status_code}")
        except requests.RequestException as e:
            print(f"HTTP request failed: {str(e)}")

    if successful_downloads > 0:
        average_speed = total_speed / successful_downloads
        print(f"Average download speed: {average_speed} bytes/sec")
    else:
        print("No files were successfully downloaded.")


