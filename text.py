import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.font_manager as fm


font_path = 'C:/Windows/Fonts/malgun.ttf' 
font_prop = fm.FontProperties(fname=font_path)


fig, ax = plt.subplots()
text = ax.text(1.0, 0.5, '김다연 공부 화이팅!', fontsize=100, ha='center', va='center', color='pink', weight='bold', fontproperties=font_prop)
ax.axis('off')

colors = ['yellow', 'pink']

def update(frame):
    x = 1.0 - 0.01 * (frame % 200)
    text.set_x(x)
    text.set_color(colors[frame % len(colors)])
    return text,

ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=100, blit=True, repeat=True)

plt.show()
