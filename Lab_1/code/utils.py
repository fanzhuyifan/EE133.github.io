import numpy as np

def snptonumpy(path):
    """ Reads snp touchstone files to numpy array.
    Assuming LinMag + Phase format for the s parameters.
    In the return array, the first column will be the frequency;
    the rest will be the s-parameters
    """
    with open(path) as f:
        lines = f.readlines()
    header = lines[1]
    lines = lines[2:]
    lines = map(lambda s: s.split(), lines)
    lines = list(lines)
    data = np.array(lines, dtype='double')
    n_s = (data.shape[1] - 1) // 2
    result = np.zeros((data.shape[0], 1 + n_s), dtype=np.cdouble)
    result[:, 0] = data[:, 0]
    for i in range(n_s):
        result[:, 1 + i] = data[:, 1 + 2 * i] * np.exp(1j * data[:, 2 + 2 * i])
    return (header.split()[2:], result)

def gamma_to_z(data, z0=50):
    """ Convert gamma to impedance via
    Z = Z0 * (1 + Gamma) / (1 - Gamma)
    """
    return z0 * (1 + data) / (1 - data)