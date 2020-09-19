# keylogger-spyware<br/>
**PREREQUISITE**<br/>
opencv, zipfile, subprocess (run python script actomatically)<br/>
ToInstall:<br/>
pip install opencv-python<br/>
pip install subprocess.run<br/>
Use python3 to run both program<br/>

***********************************************************************
***image_to_video_program***<br/>
Run as: python3 image_to_video.py<br/> 
Video created and saved as : video_made1.avi<br/>
--------------------------------------------------------------
image_to_video_program<br/>
This program uses all images that are in folder images to make video.
For every time running this program will create new numbered video.<br/>
---------------------------------------------------------------
***keylogger_program***<br/>
Run as: keylogger.py<br/>
 
For keylogger program <br/>
Every time running this program will create a log.txt file in current directory which contain all keystrokes.
and log.txt already created then it will be updated.<br/>

ToExit keylogger program<br/>
press ESC key
But this program also contain signal.alarm(20) tested on ubuntu and time.sleep(20)sys.exit() tested on windows
means program will altomatically terminate after 20 second
Time can be changed just replace 20 with other number in second.
alarm is mentioned to stop it automatically
and this keylogger program will be used in further tasks.<br/>

**********************************************************************

To make the video spyware <br/>
this spyware program require kelogger.py file and video_made1.avi file<br/>
-----------------------------------------------------------
Run as: spyware.py <br/>
Created video spyware as : video_spy.avi<br/>
-----------------------------------------------------------

This spyware program will first create zippedkey.zip file in current directory which contain keylogger program.
Then it will use a video file that is in current directory
and will hide zippedkey.zip within video_spy.avi file
This video_spy.avi will function like normal video.<br/>

After running this program following will be created in current dir:<br/>
video_spy.avi<br/>
zippedkey.zip<br/>

** The created video_spy.avi file will be used by server_send_spyware to client_receive_spyware<br/>

**********************************************************************

Spyware video share from server to client<br/>
There are two folder client and server just to verify
files are shared.
First run server_send_spyware program then client_receive_spyware program
from there respective folder<br/>
------------------------------------------------------------
***server_program***<br/>
Run as: python3 server_send_spyware.py <br/>
Server is Listening on : 5555<br/>
Connected to : 127.0.0.1 : 50490<br/>
Enter filename :video_spy.avi<br/>

Do you want to continue(y/n) :n<br/>
-------------------------------------------------------------
For server program<br/>
contain already video_spy.avi file in current directory as well as in subdirectory text and video_spy.avi is copied from task 5
Enter this if sending subdirectory file ./text/video_spy.avi<br/>
Enter n if don't want to send other files.<br/>

-------------------------------------------------------------

***client_program***<br/>
Run as: python3 client_receive_spyware.py <br/>
Connecting to : 5555<br/>
Successfully Connected.<br/>
File stored : video_spy.avi<br/>

And this video_spy.avi will be used in next task by client_send_log<br/>

**********************************************************************

First run server_receive_log then client_send_log from respective folder.<br/>
--------------------------------------------------------------
***server_program***<br/>
Run as: python3 server_receive_log.py <br/>
Server is Listening on : 5555<br/>
Connected to : 127.0.0.1 : 50958<br/>
File stored : log.txt<br/>
--------------------------------------------------------------
For server program<br/>
As connection with client is already made
so server will wait for log.txt file from client<br/>

--------------------------------------------------------------

***client_program***<br/>
Run as: python3 client_send_log.py <br/>
Connecting to : 5555<br/>
Successfully Connected.<br/>

Do you want to play video again(y/n) :n<br/>
---------------------------------------------------------------
For client program<br/>
Program build in such a way it will look like program to play video
after establishing connction to server.
This program is using video_spy.avi file from previous task 
here it is already there in client folder.<br/>
workflow....
client will run this program 
and video_spy will be played.
If don't want to see video press q.
next automatically keylogger will be extracted from video_spy.avi
after some time (20 sec) a log.txt file will be created in client folder. 
which will be shared to server in the same connection.<br/>

-----------------------------------------------------------------

If want to run keylogger for more time <br/>
just press y on client side to play video again and all the keystroke will be appended to same log.txt file
and shared with server again so server will get updated log.txt file.<br/>
