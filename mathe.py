import matplotlib as mpl
import numpy as np
from scipy import misc

mpl.use('pgf')
mpl.rcParams.update({
    'pgf.preamble': r'\usepackage{siunitx}',
})
import matplotlib.pyplot as plt
import matplotlib.image as mplimg

#x = np.linspace(0, 10, 50)
#y = np.cos(x)
#file="1.pdf"

def matheplot(x, y, label="", factor=50, dpi=200, image="mathemann.png"):
    im = mplimg.imread(image)

    plt.figure(dpi=dpi)
    line, = plt.plot(x, y, "None", label=label)
    line._transform_path()
    path, affine = line._transformed_path.get_transformed_points_and_affine()
    path = affine.transform_path(path)

    im = misc.imresize(im, (factor,factor), "bicubic")
    im = np.asarray(im)

    for pixelPoint in path.vertices:
        plt.figimage(im,pixelPoint[0]-factor/2,pixelPoint[1]-factor/2,origin="upper")

    plt.tight_layout()
#   plt.savefig(file, transparent=True)
