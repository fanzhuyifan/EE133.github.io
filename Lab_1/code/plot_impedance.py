import numpy as np
import utils
import matplotlib.pyplot as plt
from skrf import Network

def main():
    header, data = utils.snptonumpy(sys.argv[1])
    net = Network(sys.argv[1])
    l = len(header)
    n_port = int(np.sqrt(l))
    for i in range(l):
        d = data[:, 1+i]
        g_max = np.max(np.abs(d))
        g_min = np.min(np.abs(d))
        print(f"{header[i]}: max: {g_max:.2f}, {20 * np.log10(g_max):.2f}dB, min: {g_min:.2f} {20 * np.log10(g_min):.2f}dB")
        net.plot_s_smith(
            m= i % n_port,
            n= i // n_port,
            draw_labels=True,
            label_axes=True,
        )
        plt.show()

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: ./plot_impedance filename")
    else:
        main()