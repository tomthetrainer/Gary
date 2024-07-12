# Using modified time to generate movie

In this one there is a shell script to change modified time to exif data created time

So applying this should work. And probably be easier actually. 

Last video gets 5 seconds, so if you are verifying time match, that is what the discrpency is. 

The ffmpeg command now looks like this.

```ffmpeg  -ts_from_file 1 -i gary-%1d.jpeg -framerate 1 -c:v libx264 -c:a copy -shortest -r 30 -pix_fmt yuv420p gary2.mp4```

