import numpy as np
import moviepy.editor as mpy
from moviepy.video.tools.cuts import FramesMatches

clip = mpy.VideoFileClip("../hamac.mp4").resize(width=200)
matches = FramesMatches.from_clip(clip, 40, 3)

print(os.getcwd())

t1 = 3.1364666666666667
t2 = 5.2052000000000005
clip = mpy.VideoFileClip("../hamac.mp4")

N_pixels = clip.w * clip.h * 3
dot_product = lambda F1, F2: (F1*F2).sum()/N_pixels

def distance(f1, f2):
    uv = dot_product(f1, f2)
    flat_f1 = 1.0*f1.flatten()
    flat_f2 = 1.0*f2.flatten()
    u = dot_product(flat_f1, flat_f1)
    v = dot_product(flat_f2, flat_f2)
    return np.sqrt(u+v - 2*uv)

frame1 = clip.get_frame(t1)
frame2 = clip.get_frame(t2)

final = clip.subclip(t1, t2)

start = time.time()
for i in range(10000):
    distance(frame1, frame2)
end = time.time()

print("Time: %f" % (end-start)/10000)

class Main(object):


    @staticmethod
    def dot_product(f1, f2):
        return (f1*f2).sum()/N_pixels

    @staticmethod
    def distance(f1, f2):
        uv = dot_product(f1, f2)
        flat_f1 = 1.0*f1.flatten()
        flat_f2 = 1.0*f2.flatten()
        u = dot_product(flat_f1, flat_f1)
        v = dot_product(flat_f2, flat_f2)
        return np.sqrt(u+v - 2*uv)