Program to Use @danaszapiro's API
-----------------------------------
Anthony Pasquariello
 - This repo is also on @danaszapiro profile (under app branch).

app.py
 - This python application uses the API 3 times
 - Once to retrieve tweets from BU_Tweets. This works well!
 - Second time to check how it handles error handling. Works well!
 - Third to try and break it. Needs improvement.
 
 
Code Review
------------

Code review completed. All review issues are under the 'Issues' tab in @danaszapiro's repo. Found 7 issues. Some small and some a bit larger. All in all a great API though!
 - Error handling of FFmpeg within python.
 - Manually have to create output folder
 - Running proram multiple times leaves behind old images
 - Saving video try catch block doesn't output ffmpeg errors
 - ffmpeg implementation only works with OSX
 - Performance - Syncronous, must wait until all of the images are computed to output keywords

Website
--------

I built my website using Flask for Python. The home page allows users to enter a Twitter handle and hit the submit button. The submit button runs the program with danaszapiro's API. When it completes it will redirect to the output.html page. This page will play the video that was created and list the descriptor words given by Google's Image recongnition.

Images of Website
------------------

![alt text](https://github.com/danaszapiro/EC500/blob/app/website-images/ec500-1.png)
![alt text](https://github.com/danaszapiro/EC500/blob/app/website-images/ec500-2.png)
