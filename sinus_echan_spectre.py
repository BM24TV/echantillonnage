import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, fftshift

# 1. Paramètres du signal sinusoïdal et de l'échantillonnage
f_signal = 5  # Fréquence du sinus (5 Hz)
f_sampling = 50  # Fréquence d'échantillonnage augmentée (50 Hz)
T_sampling = 1 / f_sampling  # Période d'échantillonnage
t_continu = np.arange(0, 1, 0.001)  # Temps continu (de 0 à 1 seconde, pas fin de 0.001s)
t_discret = np.arange(0, 1, T_sampling)  # Temps discret (échantillonné avec T_sampling)

# 2. Générer le signal sinusoïdal (continu et échantillonné)
signal_continu = np.sin(2 * np.pi * f_signal * t_continu)
signal_discret = np.sin(2 * np.pi * f_signal * t_discret)

# 3. Calcul de la réponse fréquentielle (FFT) du signal échantillonné
N_discret = len(signal_discret)
response_freq = fftshift(fft(signal_discret))  # Transformée de Fourier centrée
freqs = fftshift(fftfreq(N_discret, d=T_sampling))  # Fréquences correspondantes

# 4. Affichage du signal et de la réponse fréquentielle
plt.figure(figsize=(12, 8))

# Premier tracé : Signal sinusoïdal (continu et échantillonné)
plt.subplot(3, 1, 1)
plt.plot(t_continu, signal_continu, label="Signal continu (sinus)", color='b')
plt.stem(t_discret, signal_discret, linefmt='r-', markerfmt='ro', basefmt='r-', label="Signal échantillonné")
plt.title("Signal sinusoïdal continu et échantillonné")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Deuxième tracé : Signal échantillonné uniquement
plt.subplot(3, 1, 2)
plt.stem(t_discret, signal_discret, linefmt='r-', markerfmt='ro', basefmt='r-', label="Signal échantillonné")
plt.title("Signal échantillonné (peigne de Dirac)")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Troisième tracé : Réponse fréquentielle du signal échantillonné
plt.subplot(3, 1, 3)
plt.plot(freqs, np.abs(response_freq), 'g')
plt.title("Réponse fréquentielle du signal échantillonné")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude (module)")
plt.grid(True)

# Ajustement et affichage
plt.tight_layout()
plt.show()
