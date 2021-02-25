import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
    Fs = 200
    Fh = 0.5
    Nf = 1
    bh, ah = signal.butter(Nf, Fh, 'high', fs=Fs)
