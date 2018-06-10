import matplotlib as mpl

mpl.use('pgf')
mpl.rcParams.update({
    'pgf.preamble': r'\usepackage{siunitx}',
})

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import unumpy as unp
from uncertainties import ufloat

#params, covar = curve_fit(f1, l, unp.nominal_values(n**2), absolute_sigma=True, sigma = unp.std_devs(n**2), p0=(1.728, 13420))
#uparams = unp.uarray(params, np.sqrt(np.diag(covar)))
#print(uparams)
