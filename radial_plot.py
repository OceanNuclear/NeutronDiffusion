import matplotlib.pyplot as plt
from numpy import pi
from numpy import array as ary
import numpy as np
π = pi
LEN = 300
circle = np.linspace(0, 2*pi, LEN)
np.random.seed(0)
rand_range = np.random.uniform

if __name__=="__main__":
    ax = plt.subplot(polar=True)
    plt.grid(False)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_axis_off()

    ax.fill_between(circle, np.repeat(1, LEN), color="C3", alpha=0.5, edgecolor=None)
    ax.fill_between(circle, np.repeat(1.1, LEN), np.repeat(1.2, LEN), color="C0")
    ax.fill_between(circle, np.repeat(1.2, LEN), np.repeat(1.5, LEN), color="C1")
    plt.tight_layout( )
    ax.text(0, 0, "Plasma\n(Neutron source)", ha="center")
    ax.text(π/2, 1.12, "First wall", ha="center", va="center")
    ax.text(π/2, 1.4, "Blanket", ha="center", va="center")
    ax.text(π/4, 1.6, "Vacuum", va="center")

    for i in range(5):
        start = (rand_range(0.3, 1), rand_range(0, 2*π))
        end = (rand_range(1.1, 1.7), rand_range(0, 2*π))
        ax.annotate("n.", xy=end[::-1], xytext=start[::-1], arrowprops=dict(facecolor='k', arrowstyle="->")) # arrowhead style needs fix?

    plt.savefig("radial_plot.pdf")