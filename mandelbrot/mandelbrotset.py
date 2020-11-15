import matplotlib.pyplot as plt
import numpy as np
 
npts = 300
max_iter = 100
 
X = np.linspace(-2, 1, 2 * npts)
Y = np.linspace(-1.25, 1.25, 2 * npts)
 
C = X[:, None] + 1j * Y
Z = np.zeros_like(C)
 
exit_times = max_iter * np.ones(C.shape, np.int32)
mask = exit_times > 0
 
for k in range(max_iter):
    Z[mask] = Z[mask] * Z[mask] + C[mask]
    mask, old_mask = abs(Z) < 2, mask
    exit_times[mask ^ old_mask] = k
 
plt.imshow(exit_times.T, cmap=plt.cm.twilight_shifted, extent=(X.min(), X.max(), Y.min(), Y.max()))
plt.savefig("mandelbrot.png", dpi=200)
