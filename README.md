I can use ffmpeg to create a video from these.

First step is to create a various length slideshow style video

From here.

https://stackoverflow.com/questions/24961127/how-to-create-a-video-from-images-with-ffmpeg

Different duration for each image

https://video.stackexchange.com/questions/23530/use-ffmpeg-to-create-a-video-from-a-few-images gives a solution.

You create a file in.txt like:

file png/1.png
outpoint 5
file png/2.png
outpoint 2
file png/3.png
outpoint 7
and outpoint sets the duration of the previous image in seconds.

Then we just remove -framerate from the previous conversion commands:

ffmpeg -f concat -i in.txt -framerate 1 -i orig/audio.ogg -c:v libx264 -c:a copy -shortest -r 30 -pix_fmt yuv420p black.mp4

ffmpeg -f concat -i in.txt -framerate 1  -c:v libx264 -c:a copy -shortest -r 30 -pix_fmt yuv420p gary.mp4
