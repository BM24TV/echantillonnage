import numpy as np
import matplotlib.pyplot as plt

# 1. Paramètres
f_sampling = 10  # Fréquence d'échantillonnage (10 Hz)
f_max = f_sampling / 2  # Fréquence maximale selon Nyquist (5 Hz)
t_continu = np.arange(0, 2, 0.001)  # Temps continu de 0 à 2 secondes, échantillonné finement
t_discret = np.arange(0, 2, 1 / f_sampling)  # Temps discret avec période d'échantillonnage 1 / f_sampling

# 2. Générer un signal aléatoire composé de plusieurs sinusoïdes
np.random.seed(42)  # Pour la reproductibilité
n_sinusoides = 5  # Nombre de sinusoïdes aléatoires
frequences = np.random.uniform(0, f_max, n_sinusoides)  # Fréquences aléatoires (inférieures à f_max)
phases = np.random.uniform(0, 2 * np.pi, n_sinusoides)  # Phases aléatoires
amplitudes = np.random.uniform(0.5, 1.5, n_sinusoides)  # Amplitudes aléatoires

signal_continu = np.zeros_like(t_continu)
for i in range(n_sinusoides):
    signal_continu += amplitudes[i] * np.sin(2 * np.pi * frequences[i] * t_continu + phases[i])

# 3. Appliquer le peigne de Dirac (échantillonnage)
signal_discret = np.zeros_like(t_discret)
for i in range(n_sinusoides):
    signal_discret += amplitudes[i] * np.sin(2 * np.pi * frequences[i] * t_discret + phases[i])

# 4. Affichage
plt.figure(figsize=(10, 8))

# Premier tracé : Signal continu
plt.subplot(2, 1, 1)
plt.plot(t_continu, signal_continu, label="Signal continu (aléatoire)", color='b')
plt.title("Signal analogique continu (composé de sinusoïdes aléatoires)")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Deuxième tracé : Signal discrétisé avec peigne de Dirac
plt.subplot(2, 1, 2)
plt.stem(t_discret, signal_discret, linefmt='r-', markerfmt='ro', basefmt='r-', label="Signal échantillonné (peigne de Dirac)")
plt.title("Signal échantillonné avec un peigne de Dirac")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Ajustement de l'affichage pour éviter que les sous-graphes se chevauchent
plt.tight_layout()

# Afficher les deux tracés
plt.show()
