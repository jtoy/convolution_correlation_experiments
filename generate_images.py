import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

time = np.arange(0, 10, 0.1);
amplitude  = np.sin(time)

plt.plot(time, amplitude)
plt.xticks([])
plt.yticks([])
f = "sin.png"
plt.savefig(f)
i = Image.open(f)
i = i.resize((256,256))
i.save(f)

#https://stackoverflow.com/questions/2169478/how-to-make-a-checkerboard-in-numpy
checkers = np.indices((256,256,3)).sum(axis=0) % 2
im = Image.fromarray((checkers * 255).astype(np.uint8))
im.save("checkers.png")

big_checkers = np.kron([[1, 0] * 4, [0, 1] * 4] * 4, np.ones((10, 10)))

r = np.arange(256)==256//2
r = r*1 | r[:,None]
r = np.dstack((r,r,r))
im = Image.fromarray((r * 255).astype(np.uint8))
im.save("cross.png")


n_points = 10000
n_classes = 2

x = np.random.uniform(-10,10, size=(n_points, n_classes))
mask = np.logical_or(np.logical_and(np.sin(x[:,0]) > 0.0, np.sin(x[:,1]) > 0.0), \
np.logical_and(np.sin(x[:,0]) < 0.0, np.sin(x[:,1]) < 0.0))
y = np.eye(n_classes)[1*mask]

plt.scatter(x[:,0], x[:,1], c=y[:,0], cmap="bwr", alpha=0.5)
f = "checker_dist.png"
plt.xticks([])
plt.yticks([])
plt.savefig(f)
i = Image.open(f)
i = i.resize((256,256))
i.save(f)
