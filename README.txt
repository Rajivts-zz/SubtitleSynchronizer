The application is used to solve the problems of out of sync subtitles.

Input:
The Synchronizer function takes two Inputs:

File Path:
The full UNIX style file path, of the subtitles file which needs to be rectified.

Offset:
The offset in seconds, that is the difference in timing between the video and the time when the subtitle is displayed. If the subtitle appears before the dialogue, the offset is positive, else if it appears after the dialogue the offset is negative.

Output:
The modified subtitle file which is in perfect sync with the video.

The application is developed in Python 2.7.