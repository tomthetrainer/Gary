import exiftool
from exiftool import ExifToolHelper
import glob
import os
from datetime import datetime


listing = glob.glob('*.jpeg')
listing.sort() # put them in order
# for filename in listing:
#     print(f"file {filename}") # first one we just emit

#print(listing[0])

# print("########")
# print(len(listing))
### Looking for this
# file gary-1.jpeg
# outpoint 5
# file gary-2.jpeg
# outpoint 2
# file gary-3.jpeg
# outpoint 7 
# file gary-4.jpeg
# outpoint 2


FMT = '%H:%M:%S%z ' # string time format for date diff

# Create function to extract time from string
# exiftool wrapper is calling what would look like this on a command line
# exiftool -TimeCreated gary-4.jpeg

for i in range(len(listing)):
    print(f'file {listing[i]}') # First one we just print
    # Next we need diff in seconds from i to i+1
    # Get the time
    this_data = ExifToolHelper().execute("-TimeCreated", listing[i])
    this_time = this_data.split(": ")[-1]
    this_time.strip()
    this_time.rstrip()
    # uncomment to show time for debugging
    #print(f'--Time stamp for image = {this_time}')
   

    next_record = i+1
    next_data = ExifToolHelper().execute("-TimeCreated", listing[next_record])
    next_time = next_data.split(": ")[-1]
    next_time.strip()
    next_time.rstrip()
    # uncomment to show time for debugging
    #print(f'--Time stamp for NEXT image = {next_time}')
    
    # Get the time delta, how long to hold the current image
    # This goes into the file as outpoint numsec

    tdelta = datetime.strptime(next_time, FMT) - datetime.strptime(this_time, FMT)
    print(f'outpoint {tdelta}')
    
    
   





