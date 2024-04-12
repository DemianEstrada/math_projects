import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw

def wf(a, s=2, i=-2):
    
    x = np.linspace(i, s, 200)
    y = x * np.exp(x) - a

    plt.plot(x, y, label = r'$f(x) = xe^x - {a}$',color='b', linestyle='--')
    
    return

def bis_wlamb(a, iteraciones=10, xs0=2, xi0=-2):
    colormap = plt.cm.cool
    colores = [colormap(i) for i in np.linspace(0, 1, iteraciones+1)]
    
    plt.figure()
    wf(a, xs0, xi0)
    for iteracion in range(iteraciones+1):
        x_mid = (xs0 + xi0) / 2
        f_xs0 = xs0 * np.exp(xs0) - a
        f_xi0 = xi0 * np.exp(xi0) - a
        f_mid = x_mid * np.exp(x_mid) - a
        
        plt.scatter( xs0,10-iteracion, color=colores[iteracion])
        plt.scatter( xi0,10-iteracion, color=colores[iteracion])
        plt.scatter( x_mid,10-iteracion, color=colores[iteracion])

        if np.sign(f_mid) == np.sign(f_xs0):
            xs0 = x_mid
        elif np.sign(f_mid) == np.sign(f_xi0):
            xi0 = x_mid
        else:
            print('Error')
            return None

    plt.axvline(lambertw(a), color='r', linestyle='-', label='Raíz (W de Lambert)')
    
    plt.title(f'Buscando: {a}')
    plt.ylim(None, 11)
    plt.grid()
    plt.legend()
    plt.show()

    return x_mid

valores_a = np.array([3/2, 1/2, -1/5])

for e, a in enumerate(valores_a):
    
    raiz = bis_wlamb(a)    
    
    print(f"Raíz para a={a}: {raiz}")
