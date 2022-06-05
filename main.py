import os

from pytube import YouTube
import ffmpeg
from Tools.scripts.combinerefs import combine
from youtube_api import YouTubeDataAPI
import youtube_dl
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

import subprocess


def get_mp3(url):
    video_info = youtube_dl.YoutubeDL().extract_info(url)

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': f"{video_info['title']}.mp3",
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])


def get_mp4(url):
    print(url)
    yts = YouTube(url)
    print(yts)

    caption = yts.captions.get_by_language_code('en')
    print(caption)

    print(yts.streams.count())

    mp4 = yts.streams.filter(file_extension="mp4")
    stream = yts.streams.get_highest_resolution()
    stream.download()

    # mp4 = yts.streams.filter(file_extension="mp4")
    # mp4_1080p = mp4.get_by_resolution("1080p")
    # mp4_1080p.download()


api_key = 'AIzaSyB2d1meTlIzGFTlFv47euoWMy6X7HFLCcU'
yt = YouTubeDataAPI(api_key)

video = yt.search('The Most Beautiful Equation in Math')[0]
# print(video)
url = 'https://www.youtube.com/watch?v=' + video['video_id'] + '&ab_channel=' + video['channel_title']

get_mp3(url)
get_mp4(url)

# CONVERT mp3 to WAV to use Google trans
src = video['video_title'] + '.mp3'
dst = 'test.wav'
subprocess.call(['ffmpeg', '-i', src, dst])

r = sr.Recognizer()
with sr.AudioFile(dst) as source:
    audio = r.record(source)
os.remove('test.wav')
query = r.recognize_google(audio, language='en')

translator = Translator()
text_to_translate = translator.translate(query, dest='zh-CN')
text = text_to_translate.text
print(text)

speak = gTTS(text=text, lang='zh-CN', slow=False)
speak.save(video['video_title'] + ' - chinese-translated.mp3')

other_audio = ffmpeg.input(video['video_title'] + ' - chinese-translated.mp3')
mp4 = ffmpeg.input(video['video_title'] + '.mp4')
video = mp4.video

ffmpeg.concat(video, other_audio, v=1, a=1).output('combined2.mp4').run()