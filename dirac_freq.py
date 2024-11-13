import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

# 1. Générer une impulsion de Dirac discrète
n = np.arange(-50, 51)  # Temps discret de -50 à 50
dirac = np.zeros_like(n)
dirac[n == 0] = 1  # Dirac à n = 0

# 2. Calcul de la réponse fréquentielle avec la transformée de Fourier
N = len(dirac)
freq = fftfreq(N, d=1)  # Fréquences correspondantes
response_freq = fft(dirac)  # Transformée de Fourier de l'impulsion de Dirac

# 3. Affichage de l'impulsion de Dirac et de la réponse fréquentielle
plt.figure(figsize=(12, 6))

# Premier tracé : Impulsion de Dirac dans le domaine temporel
plt.subplot(1, 2, 1)
plt.stem(n, dirac, basefmt="b-")
plt.title("Impulsion de Dirac (discrète)")
plt.xlabel("Temps discret (n)")
plt.ylabel("Amplitude")
plt.grid(True)

# Deuxième tracé : Réponse fréquentielle (module de la transformée de Fourier)
plt.subplot(1, 2, 2)
plt.plot(freq, np.abs(response_freq), 'r')
plt.title("Réponse fréquentielle de l'impulsion de Dirac")
plt.xlabel("Fréquence")
plt.ylabel("Amplitude (module)")
plt.grid(True)

# Affichage
plt.tight_layout()
plt.show()
