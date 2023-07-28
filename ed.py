from moviepy.editor import VideoFileClip, concatenate_videoclips,vfx,ImageClip,CompositeVideoClip

clip1=VideoFileClip("clip_3.mp4").subclip(5,10)
clip2=VideoFileClip("clip_4.mp4").subclip(5,10)
combined = concatenate_videoclips([clip1,clip2])
combined.write_videofile("combo.mp4")
