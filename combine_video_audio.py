import ffmpeg
import sys

input_video = ffmpeg.input('source1.mp4')
input_audio = ffmpeg.input('voice.mp3')
ffmpeg.concat(input_video, input_audio, v=1, a=1).output('combined2.mp4').run()
