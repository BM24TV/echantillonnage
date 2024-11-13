import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, fftshift

# 1. Paramètres du signal sinusoïdal et de l'échantillonnage
f_signal = 5  # Fréquence du sinus (5 Hz)
f_sampling = 50  # Fréquence d'échantillonnage (50 Hz)
T_sampling = 1 / f_sampling  # Période d'échantillonnage
t_continu = np.arange(0, 1, 0.001)  # Temps continu (de 0 à 1 seconde, pas fin de 0.001s)
t_discret = np.arange(0, 1, T_sampling)  # Temps discret (échantillonné avec T_sampling)

# 2. Générer le signal sinusoïdal (continu et échantillonné)
signal_continu = np.sin(2 * np.pi * f_signal * t_continu)
signal_discret = np.sin(2 * np.pi * f_signal * t_discret)

# 3. Maintien de la valeur entre les échantillons
signal_montant = np.repeat(signal_discret, 2)[:-1]  # Conserver chaque échantillon jusqu'au suivant
t_montant = np.linspace(0, 1, len(signal_montant))  # Temps correspondant au signal échantillonné

# 4. Calcul de la réponse fréquentielle (FFT) du signal échantillonné avec maintien
N_montant = len(signal_montant)
response_freq_montant = fftshift(fft(signal_montant))  # Transformée de Fourier centrée
freqs_montant = fftshift(fftfreq(N_montant, d=T_sampling / 2))  # Fréquences correspondantes

# 5. Affichage du signal et de la réponse fréquentielle
plt.figure(figsize=(12, 10))

# Premier tracé : Signal sinusoïdal (continu et échantillonné avec maintien)
plt.subplot(4, 1, 1)
plt.plot(t_continu, signal_continu, label="Signal continu (sinus)", color='b')
plt.step(t_montant, signal_montant, where='post', color='r', label="Signal échantillonné (maintien)")
plt.title("Signal sinusoïdal continu et échantillonné avec maintien")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Deuxième tracé : Signal échantillonné uniquement avec maintien
plt.subplot(4, 1, 2)
plt.step(t_montant, signal_montant, where='post', color='r', label="Signal échantillonné (maintien)")
plt.title("Signal échantillonné avec maintien")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Troisième tracé : Réponse fréquentielle du signal échantillonné
plt.subplot(4, 1, 3)
plt.plot(freqs_montant, np.abs(response_freq_montant), 'g')
plt.title("Réponse fréquentielle du signal échantillonné (FFT)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude (module)")
plt.grid(True)

# Quatrième tracé : Spectre du signal échantillonné avec maintien
plt.subplot(4, 1, 4)
#plt.plot(freqs_montant, 20 * np.log10(np.abs(response_freq_montant)), 'm')
plt.plot(freqs_montant, (np.abs(response_freq_montant)), 'm')
plt.title("Spectre du signal échantillonné avec maintien (dB)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)

# Ajustement et affichage
plt.tight_layout()
plt.show()
