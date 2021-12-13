import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)

def gauss(sigma, mu):
    return 1/(sigma * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sigma**2))

dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))

plt.plot(x, gauss(0.5, 1.0), 'ro-')
plt.plot(x, gauss(1.0, 0.5), 'go-')
plt.plot(x, gauss(1.5, 0.0), 'bo-')

plt.legend(['sigma = 0.5, mu = 1.0',
            'sigma = 1.0, mu = 0.5',
            'sigma = 1.5, mu = 0.0'], loc='upper left')

fig.savefig('gauss.png')
plt.show()
