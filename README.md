# Streaming AI (Twitch or Youtube)

## Install FFmpeg
https://www.wikihow.com/Install-FFmpeg-on-Windows
### Install ffmpeg-python  [ffmpeg-python API Docs](https://kkroening.github.io/ffmpeg-python/)
```
pip install ffmpeg-python
```

## Play sounds
```
pip3 install gTTS playsound

import gtts
from playsound import playsound
# play the audio file
playsound("hello.mp3")
```

## Language transalation
### [https://www.geeksforgeeks.org/create-a-real-time-voice-translator-using-python/](https://www.geeksforgeeks.org/create-a-real-time-voice-translator-using-python/)
```
import speech_recognition as sr
r = sr.Recognizer()

with sr.AudioFile("hello_world.wav") as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))
```


## Remove orginal audio channel from MP4
```
import subprocess
command = 'for file in *.mp4; do ffmpeg -i "$file" -c copy -an "noaudio_$file"; done'
subprocess.call(command, shell=True)
```

## Combine MP4 and MP3
```
pip install ffmpeg-python

import ffmpeg
infile1 = ffmpeg.input(combine + "/" + name + ".mp4")
infile2 = ffmpeg.input(combine + "/" + name + ".mp3")
ffmpeg.concat(infile1, infile2, v=1, a=1).output(final_save_path + "/" + name + ".mp4").run()
```

## Text-to-Speech generation
### [Convert text to speech in Python code](https://www.thepythoncode.com/article/convert-text-to-speech-in-python)
### [TTS library](https://github.com/coqui-ai/TTS)

## API to retrieve videos and meta data from Youtube 
#### [Pytube](https://pytube.io/)


## Twitch API to retrieve videos and meta data from Twitch 
#### twitch-python (Current and release recently)
* [https://pypi.org/project/twitch-python/](https://pypi.org/project/twitch-python/)
#### python-twitch-client (rich functionalities, but no update for two years) 
* [https://python-twitch-client.readthedocs.io/en/latest/](https://python-twitch-client.readthedocs.io/en/latest/)
* [https://github.com/tsifrer/python-twitch-client](https://github.com/tsifrer/python-twitch-client)


## 5 Manual Ways to Subtitle and Caption Videos Automatically Using Speech Recognition
It's always good ideas to start manually to work out the concept and workflow manully before you developed software and tool to automate them. 
* [https://photography.tutsplus.com/tutorials/3-ways-to-subtitle-and-caption-your-videos-automatically-using-artificial-intelligence--cms-26834](https://photography.tutsplus.com/tutorials/3-ways-to-subtitle-and-caption-your-videos-automatically-using-artificial-intelligence--cms-26834)

## Video Captioning API and Code 
####  Sequence to Sequence -- Video to Text
* [https://vsubhashini.github.io/s2vt.html](https://vsubhashini.github.io/s2vt.html)
####  Automated Video Captioning using S2VT
* [https://github.com/vijayvee/video-captioning'(https://github.com/vijayvee/video-captioning)

### References
#### Twitch Stream Highlights Detection with Machine Learning
* [https://towardsdatascience.com/how-i-created-an-app-for-live-stream-highlight-detection-for-twitch-532f4027987e](https://towardsdatascience.com/how-i-created-an-app-for-live-stream-highlight-detection-for-twitch-532f4027987e)
* [https://github.com/artkulak/twitch-stream-highlights-detection](https://github.com/artkulak/twitch-stream-highlights-detection)
