import cv2
import os

#load the video capture
vidcap = cv2.VideoCapture('video.mp4')

success,image = vidcap.read()
property_id = int(cv2.CAP_PROP_FRAME_COUNT) 
total_frames = int(cv2.VideoCapture.get(vidcap, property_id))

#make image output folder
os.mkdir('image_output')
os.chdir('image_output')

#define frame skip amounts
frame_skip = 5

#loop over all frames in the video
for ii in range(total_frames):
    if ii % frame_skip == 0:
        
        count = ii
        vidcap.set(1,count)

        #output images
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print(f'Succesfully read frame {count}: {success}')
        

        
  