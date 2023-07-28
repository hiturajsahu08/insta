from moviepy.editor import VideoFileClip, concatenate_videoclips,vfx,ImageClip,CompositeVideoClip

clip1=VideoFileClip("clip_1.mp4").subclip(5,10)


clip2=VideoFileClip("clip_2.mp4").subclip(5,10)
combined = concatenate_videoclips([clip1,clip2])
#combined.write_videofile("combo.mp4")


#video =VideoFileClip("clip_1.mp4").subclip(5,10)

title = ImageClip("title.png").set_start(0).set_duration(5).set_pos(("center", "top"))
# .resize(height=50) # if you need to resize...


final = CompositeVideoClip([video, title])
final.write_videofile("test1.mp4")
