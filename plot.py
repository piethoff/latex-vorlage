import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from mathe import matheplot as mp

mpl.use('pgf')
mpl.rcParams.update({
    'pgf.preamble': r'\usepackage{siunitx}',
})

x = np.linspace(0, 10, 80)
y = x ** np.sin(x)

mp(x,y, dpi=300, factor=60)

plt.savefig("1.pdf", transparent=True)
