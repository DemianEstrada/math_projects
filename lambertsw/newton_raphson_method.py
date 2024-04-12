import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw

valores_a = np.array([3/2, 1/2, -1/5])

def wf(a):
    
    x = np.linspace(-2, 2, 200)
    y = x * np.exp(x) - a

    plt.plot(x, y, label = r'$f(x) = xe^x - {a}$',color='b', linestyle='--')
    
    return

def new_wlamb(a, iteraciones=10, x0=0):
    
    iteraciones+=1

    colormap = plt.cm.cool
    colores = [colormap(i) for i in np.linspace(0, 1, iteraciones)]
    
    x_aux = x0
    
    for iteracion in range(iteraciones):


        plt.scatter( x_aux,10-iteracion, color=colores[iteracion])
        
        x_aux = x_aux - ((x_aux*np.exp(x_aux)-a) / ((x_aux + 1)*np.exp(x_aux)))
        
    plt.axvline(lambertw(a), color='r', linestyle='-', label='Raiz (W de Lambert)')
    wf(a)
    plt.title(f'Buscando: {a}')
    plt.grid()
    plt.legend()
    plt.show()
    
    return x_aux

for e, a in enumerate(valores_a):
  
    plt.figure()
  
    raiz = new_wlamb(a)
            
    print(f"Raíz para a={a}: {raiz}")
