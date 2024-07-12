#!/bin/bash
#
#
#Read the exif create time, and make it the create time of the file
#exiftool -T -DateTimeCreated gary-1bak.jpeg
# We want to change the value returned my
# GetFileInfo -m Gary-1bak.jpeg
# The modified time, we can change this with touch

for f in *.jpeg; do
  #echo "File -> $f"


  myvar=`exiftool -d "%Y-%m-%dT%H:%M:%S" -T -DateTimeCreated $f`
#echo $myvar

#touch -d "2 hours ago" filename
# I think I want touch -m
# Actually it has to be -d, modified can't be older than create ??

  touch -d $myvar $f
done
