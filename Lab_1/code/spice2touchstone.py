import numpy as np
import matplotlib.pyplot as plt
from skrf import Network
import skrf
import ltspice


def main(input, output, expr):
    l = ltspice.Ltspice(input)
    l.parse()
    print(l.variables)
    net = Network()
    print(l.frequency)
    f = l.frequency / 1e6
    z = eval(expr)
    z = z.reshape((-1, 1, 1))
    net = net.from_z(z)
    net.frequency.unit = 'mhz'
    net.f = f
    net.write_touchstone(output, form='ma')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        print(f"Usage: python raw2touchstone input output expr")
        print("""where expr is an expression to calculate the Z values, like l.getData(V(001))/l.getData(I(C)) """)
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])