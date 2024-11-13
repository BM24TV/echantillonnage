import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

# 1. Générer une impulsion de Dirac imparfaite (gaussienne)
n = np.arange(-50, 51)  # Temps discret de -50 à 50
sigma = 3  # Largeur de l'impulsion gaussienne (écart-type)
dirac_imparfait = np.exp(-n**2 / (2 * sigma**2))  # Forme gaussienne centrée à n=0

# 2. Calcul de la réponse fréquentielle avec la transformée de Fourier
N = len(dirac_imparfait)
freq = fftfreq(N, d=1)  # Fréquences correspondantes
response_freq = fft(dirac_imparfait)  # Transformée de Fourier de l'impulsion imparfaite

# 3. Affichage de l'impulsion de Dirac imparfaite et de sa réponse fréquentielle
plt.figure(figsize=(12, 6))

# Premier tracé : Impulsion de Dirac imparfaite dans le domaine temporel
plt.subplot(1, 2, 1)
plt.plot(n, dirac_imparfait, label="Impulsion gaussienne", color='b')
plt.title("Impulsion de Dirac imparfaite (gaussienne)")
plt.xlabel("Temps discret (n)")
plt.ylabel("Amplitude")
plt.grid(True)

# Deuxième tracé : Réponse fréquentielle (module de la transformée de Fourier)
plt.subplot(1, 2, 2)
plt.plot(freq, np.abs(response_freq), 'r')
plt.title("Réponse fréquentielle de l'impulsion imparfaite")
plt.xlabel("Fréquence")
plt.ylabel("Amplitude (module)")
plt.grid(True)

# Affichage
plt.tight_layout()
plt.show()
