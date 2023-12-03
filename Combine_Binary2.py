import os

# Modified to combine all files in Binary
directory = 'Binary'

# Get all file paths in the directory
file_paths = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Sort files by creation date (oldest first)
sorted_files = sorted(file_paths, key=os.path.getmtime)

# Combine the files
with open('Combined/combined.bin', 'wb') as outfile:
    for filename in sorted_files:
        with open(filename, 'rb') as infile:
            outfile.write(infile.read())
