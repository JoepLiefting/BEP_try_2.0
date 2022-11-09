# importing required libraries
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.animation as animation
from IPython import display
import moviepy.editor as mp

gif_name = 'animation_4.gif'
mp4_name = 'animation_4.mp4'

# initializing a figure
fig = plt.figure()

# labeling the x-axis and y-axis
axis = plt.axes(xlim=(0, 1000), ylim=(0, 1000))

# lists storing x and y values
x, y = [], []

line, = axis.plot(0, 0)


def animate(frame_number):
    x.append(frame_number)
    y.append(frame_number)
    line.set_xdata(x)
    line.set_ydata(y)
    return line,


anim = animation.FuncAnimation(fig, animate, frames=1000,
                               interval=20, blit=True)
fig.suptitle('Straight Line plot', fontsize=14)

# saving to m4 using ffmpeg writer
f = r"C://Users/joepl/PycharmProjects/BEP_try_2.0/Animations/"+gif_name
writervideo = animation.PillowWriter(fps=30)
anim.save(f, writer=writervideo)
plt.close()

clip = mp.VideoFileClip(f)
clip.write_videofile(r"C://Users/joepl/PycharmProjects/BEP_try_2.0/Animations/"+mp4_name)

