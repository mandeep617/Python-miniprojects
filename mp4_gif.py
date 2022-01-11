# pip install moviepy in the terminal
# Import everything needed to edit video clips
from moviepy.editor import *
Mandeep = VideoFileClip("old.mp4")
Mandeep.write_gif("new.gif")