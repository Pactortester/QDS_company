import random

import numpy as np

from config.globalparam import data_path


def xz(filename):

    data = np.loadtxt(data_path + "\\" + filename)

    return int(random.choice(data))
