import matplotlib.pyplot as plt
from numpy import array as ary
import numpy as np

np.random.seed(7)
rand_range = np.random.uniform
rand_sign = lambda: np.random.choice([-1, 1])
HEIGHT = 2
MID = HEIGHT/2
y_range = [HEIGHT, HEIGHT]

if __name__=="__main__":
    ax = plt.subplot()
    ax.set_axis_off()
    for x_sign in (-1, 1):
        ax.fill_between(x_sign * ary([0,1]), y_range, color="C3", alpha=0.5, edgecolor=None)
        ax.fill_between(x_sign * ary([1.1,1.2]), y_range, color="C0")
        ax.fill_between(x_sign * ary([1.2,1.5]), y_range, color="C1")

    ax.text(0, MID, "Plasma\n(Neutron source)", ha="center")
    ax.text(1.12, MID, "First wall (right)", va="center", ha="center", rotation=270)
    ax.text(-1.12, MID, "First wall (left)", va="center", ha="center", rotation=90)
    ax.text(1.4, MID, "Blanket (right)", va="center", ha="center", rotation=270)
    ax.text(-1.4, MID, "Blanket (left)", va="center", ha="center", rotation=90)
    # ax.set_ylim()
    # ax.set_xlim(-1.5, 1.5)
    # plt.tight_layout()
    for i in range(6):
        start = (rand_range(0, 1)*rand_sign(), rand_range(0, HEIGHT))
        end = (rand_range(1.1, 1.6)*rand_sign(), rand_range(0, HEIGHT))
        ax.annotate("n.", xy=end, xytext=start, arrowprops=dict(facecolor='k', arrowstyle="->")) # arrowhead style needs fix?
    plt.savefig("semiinfinite_plot.pdf")