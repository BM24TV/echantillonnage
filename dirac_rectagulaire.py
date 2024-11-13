import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, fftshift

# 1. Générer une impulsion rectangulaire
n = np.arange(-50, 51)  # Temps discret de -50 à 50
rect_width = 10  # Largeur de l'impulsion rectangulaire
dirac_rect = np.zeros_like(n)
dirac_rect[(n >= -rect_width // 2) & (n <= rect_width // 2)] = 1  # Impulsion rectangulaire de largeur donnée

# 2. Calcul de la réponse fréquentielle avec la transformée de Fourier
N = len(dirac_rect)
response_freq = fftshift(fft(dirac_rect))  # Transformée de Fourier de l'impulsion rectangulaire
freq = fftshift(fftfreq(N, d=1))  # Fréquences correspondantes

# 3. Affichage de l'impulsion rectangulaire et de la réponse fréquentielle (sinc)
plt.figure(figsize=(12, 6))

# Premier tracé : Impulsion rectangulaire dans le domaine temporel
plt.subplot(1, 2, 1)
plt.plot(n, dirac_rect, label="Impulsion rectangulaire", color='b')
plt.title("Impulsion de Dirac imparfaite (rectangulaire)")
plt.xlabel("Temps discret (n)")
plt.ylabel("Amplitude")
plt.grid(True)

# Deuxième tracé : Réponse fréquentielle (sinc)
plt.subplot(1, 2, 2)
plt.plot(freq, np.abs(response_freq), 'r')
plt.title("Réponse fréquentielle de l'impulsion rectangulaire (sinc)")
plt.xlabel("Fréquence")
plt.ylabel("Amplitude (module)")
plt.grid(True)

# Affichage
plt.tight_layout()
plt.show()
