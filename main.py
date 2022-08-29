from os import listdir
from moviepy.editor import *

duration = int(input('How long would you like the video to be (in seconds): '))
duration = duration - 2
def zoom(t):
    return 2.275 - (t/(duration/len(frames)))*1.075

frames = listdir('./frames')
frames.sort()
print()

clips = []

for i, filename in enumerate(listdir('./frames')):
  if filename.endswith(".png"):
    clips.append(ImageClip('./frames/' + filename).set_duration(duration/len(frames)).resize(zoom))

concat_clip = concatenate_videoclips(clips)
concat_clip = CompositeVideoClip([concat_clip.set_position(('center', 'center'))], size=(1024,1024))
concat_clip = concatenate_videoclips([concat_clip, ImageClip('./frames/' + filename).set_duration(2)], method='compose')
concat_clip.write_videofile("test.mp4", fps=24, )