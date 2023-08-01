from moviepy.editor import VideoFileClip, concatenate_videoclips,vfx,ImageClip,CompositeVideoClip
import time
l=[0,1,2,3,4,5,6,7]
for each in l:
    clip1=VideoFileClip("clip_3.mp4")
    clip2=VideoFileClip("clip_4.mp4")
    combined = concatenate_videoclips([clip1,clip2])
    combined.write_videofile("combo"+"l"+".mp4")
