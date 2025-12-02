import numpy as np
import matplotlib.pyplot as plt

def mapa_logistico(x, r):
    """Função do mapa logístico G(x) = rx(1-x)"""
    x = r * x * (1 - x)
    return x

def diagrama_bifurcacao(rinit, rend, num_pontos_r=500, num_transiente=500, num_plotados=100):
    """
    Gera o diagrama de bifurcação do mapa logístico.
    
    Parâmetros:
    -----------
    rinit : float
        Valor inicial de r
    rend : float
        Valor final de r
    num_pontos_r : int
        Número de valores de r a serem testados
    num_transiente : int
        Número de iterações para descartar (transiente)
    num_plotados : int
        Número de pontos a serem plotados após o transiente
    
    Retorna:
    --------
    buffer_r, buffer_diagrama : arrays
        Arrays com os valores de r e x para plotagem
    """
    buffer_r = np.zeros(num_pontos_r * num_plotados)
    buffer_diagrama = np.zeros(num_pontos_r * num_plotados)
    k = 0
    
    for i in range(num_pontos_r):
        r = rinit + i * (rend - rinit) / num_pontos_r
        x = 0.1  # Condição inicial
        
        # Descarta valores transientes
        for j in range(num_transiente):
            x = mapa_logistico(x, r)
        
        # Armazena os valores após o transiente
        for j in range(num_plotados):
            x = mapa_logistico(x, r)
            buffer_r[k] = r
            buffer_diagrama[k] = x
            k = k + 1
    
    return buffer_r, buffer_diagrama

# Gera o diagrama para r ∈ [2.5, 4.0]
rinit_a = 2.5
rend_a = 4.0

buffer_r_a, buffer_diagrama_a = diagrama_bifurcacao(rinit_a, rend_a)

# Plotagem
plt.figure(figsize=(12, 8))
plt.scatter(buffer_r_a, buffer_diagrama_a, s=0.01, color='black')
plt.xlabel('r', fontsize=14)
plt.ylabel('x', fontsize=14)
plt.title('Diagrama de Bifurcação do Mapa Logístico: $r \in [2.5, 4.0]$', fontsize=16)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Gera o diagrama para r ∈ [3.62, 3.64] - Zoom em região específica
rinit_b = 3.62
rend_b = 3.64

buffer_r_b, buffer_diagrama_b = diagrama_bifurcacao(rinit_b, rend_b)

# Plotagem
plt.figure(figsize=(12, 8))
plt.scatter(buffer_r_b, buffer_diagrama_b, s=0.05, color='darkblue')
plt.xlabel('r', fontsize=14)
plt.ylabel('x', fontsize=14)
plt.title('Diagrama de Bifurcação do Mapa Logístico: $r \in [3.62, 3.64]$ (Zoom)', fontsize=16)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()