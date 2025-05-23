import matplotlib.pyplot as plt
from numpy import array as ary
import numpy as np
import matplotlib.pyplot as mpl
plt.rcParams['pgf.preamble'] = r'\usepackage{amsmath}'  # for \text command as well
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'  # for \text command
plt.rcParams['text.usetex'] = True  # use TeX to render everything
plt.rcParams['font.family'] = 'STIXGeneral'  # correct font!

np.random.seed(7)
rand_range = np.random.uniform
rand_sign = lambda: np.random.choice([-1, 1])
HEIGHT = 2
MID = HEIGHT/2
y_range = [HEIGHT, HEIGHT]

if __name__=="__main__":
    ax = plt.subplot()
    # ax.set_axis_off()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_yaxis().set_visible(False)
    # x_axis = ax.get_xaxis()
    ax.set_xticks([-0.4, -0.1, 0, 0.1, 0.4], [r"-$x_{BZ}$", r"-$x_{FW}$", 0, r"$x_{FW}$", r"$x_{BZ}$"])

    ax.plot([0,0], [0, HEIGHT], color="red")
    for x_sign in (-1, 1):
        ax.fill_between(x_sign * ary([0.0,0.1]), y_range, color="C0")
        ax.fill_between(x_sign * ary([0.1,0.4]), y_range, color="C1")

    ax.text(0.04, MID, "First wall (right)", va="center", ha="center", rotation=270)
    ax.text(-0.04, MID, "First wall (left)", va="center", ha="center", rotation=90)
    ax.text(0.3, MID, "Blanket (right)", va="center", ha="center", rotation=270)
    ax.text(-0.3, MID, "Blanket (left)", va="center", ha="center", rotation=90)
    ax.text(0, HEIGHT, "Planar source\nof neutrons", color="red", va="bottom", ha="center")
    # ax.set_ylim()
    # ax.set_xlim(-0.5, 0.5)
    # plt.tight_layout()
    for i in range(6):
        start = (rand_range(0, 0)*rand_sign(), rand_range(0, HEIGHT))
        end = (rand_range(0.02, 0.45)*rand_sign(), rand_range(0, HEIGHT))
        ax.annotate("n.", xy=end, xytext=start, arrowprops=dict(facecolor='k', arrowstyle="->"), ha="center") # arrowhead style needs fix?
    plt.savefig("collapsed_geometry.pdf")