# Simple script to combine the binary files. Need to decide on a naming format or somehow know the order.
files_to_combine = ['Binary/exFile.bin', 'Binary/noisy.bin']

with open('Binary/combined.bin', 'wb') as outfile:
    # Should just go in order of array
    for filename in files_to_combine:
        with open(filename, 'rb') as infile:
            outfile.write(infile.read())
