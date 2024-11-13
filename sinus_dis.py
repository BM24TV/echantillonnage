import numpy as np
import matplotlib.pyplot as plt

# 1. Paramètres pour le signal
f = 1  # Fréquence du signal sinusoïdal en Hz
sampling_period = 0.1  # Période d'échantillonnage (temps entre deux Dirac)
t_continu = np.arange(0, 2, 0.001)  # Temps continu de 0 à 2 secondes, échantillonné finement
t_discret = np.arange(0, 2, sampling_period)  # Temps discret (peigne de Dirac, espacés de sampling_period)

# 2. Générer le signal sinusoïdal continu
signal_continu = np.sin(2 * np.pi * f * t_continu)

# 3. Appliquer le peigne de Dirac (échantillonnage)
signal_discret = np.sin(2 * np.pi * f * t_discret)

# 4. Création des sous-graphes
plt.figure(figsize=(10, 8))

# Premier tracé : Signal continu
plt.subplot(2, 1, 1)
plt.plot(t_continu, signal_continu, label="Signal continu (sinusoïde)", color='b')
plt.title("Signal sinusoïdal continu")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Deuxième tracé : Signal discrétisé avec peigne de Dirac
plt.subplot(2, 1, 2)
plt.stem(t_discret, signal_discret, linefmt='r-', markerfmt='ro', basefmt='r-', label="Signal échantillonné (peigne de Dirac)")
plt.title("Signal discrétisé avec un peigne de Dirac")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Ajustement de l'affichage pour éviter que les sous-graphes se chevauchent
plt.tight_layout()

# Afficher les deux tracés
plt.show()

