import ffmpeg
import subprocess

input = ffmpeg.input('source2.mp4')
#audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
video = input.video
other_audio = ffmpeg.input('voice.mp3')
ffmpeg.output(other_audio, video, 'video_with_other_audio.mp4').run()