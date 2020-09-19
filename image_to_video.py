import cv2
import numpy as np
import os
from os.path import isfile, join
# directory which contain images
image_path= './images/'
# set frames per second
fps = 0.5
image_array = []
files_list = [f for f in os.listdir(image_path) if isfile(join(image_path, f))]
# make file name in sorted order
files_list.sort(key = lambda x: x[5:-4])

for i in range(len(files_list)):
    file_name=image_path + files_list[i]
    #reading each files
    image = cv2.imread(file_name)
    height, width, layers = image.shape
    size = (width,height)
    
    # insert each frame into an image_array
    image_array.append(image)
i = 1
while os.path.exists("video_made%s.avi" % i):
    i += 1
video_name = "video_made%s.avi" % i
out = cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(image_array)):
    out.write(image_array[i])
out.release()
print("Video created and saved as :",video_name)