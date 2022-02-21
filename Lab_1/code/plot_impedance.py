import numpy as np
import matplotlib.pyplot as plt
from skrf import Network
import skrf

plot_methods = {
    "smith": Network.plot_s_smith,
    "db": Network.plot_z_db,
}

plot_args_dict = {
    "smith": {
        "draw_labels": True,
        "label_axes": True,
    },
    "db": {

    }
}

def plot_file(file, plot_method, plot_args, label=None):
    net = Network(file)
    l = net.nports
    n_port = int(np.sqrt(l))
    for i in range(l):
        m = i % n_port
        n = i // n_port
        d = net.s[:, m, n]
        g_max = np.max(np.abs(d))
        g_min = np.min(np.abs(d))
        print(f"S{m+1}{n+1}: max: {g_max:.2f}, {20 * np.log10(g_max):.2f}dB, min: {g_min:.2f} {20 * np.log10(g_min):.2f}dB")
        impedances = net.z[:, m, n]
        for j in range(0, len(d), len(d) // 10):
            print(f"{net.frequency.f[j] / 1e6:.3f} & {d[j]:.2f} & {impedances[j]:.2f}")
        if label is not None:
            plot_method(
                net,
                m= m,
                n= n,
                label=f"{label}, S{m+1}{n+1}",
                **plot_args,
            )
        else:
            plot_method(
                net,
                m= m,
                n= n,
                **plot_args,
            )

def main():
    skrf.plotting.stylely()
    plt.figure()
    plot_method = plot_methods[sys.argv[1]]
    plot_args = plot_args_dict[sys.argv[1]]
    for i in range(len(sys.argv) - 2):
        args = sys.argv[i + 2].split(':')
        plot_file(args[0], plot_method, plot_args, args[1] if len(args) > 1 else None)
    plt.show()

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: python plot_impedance plot_method filename1[:label1] ...")
        print(f"plot_method is one of {list(plot_methods.keys())}")
    else:
        main()