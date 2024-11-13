import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Paramètres du signal
frequence_signal = 10  # Fréquence du signal (en Hz)
duree_signal = 0.2      # Durée du signal (en secondes)
frequence_echantillonnage = 20  # Fréquence d'échantillonnage (en Hz)

# Génération de l'axe temporel à haute résolution pour le signal original
temps = np.linspace(0, duree_signal, 1000)

# Génération du signal sinusoïdal
signal_sin = np.sin(2 * np.pi * frequence_signal * temps)

# Génération du signal triangulaire
#signal_triangle = signal.sawtooth(2 * np.pi * frequence_signal * temps, 0.5)

# Échantillonnage du signal
intervalle_echantillonnage = int(1000 / frequence_echantillonnage)
temps_echantillonne = temps[::intervalle_echantillonnage]
signal_sin_echantillonne = signal_sin[::intervalle_echantillonnage]
#signal_triangle_echantillonne = signal_triangle[::intervalle_echantillonnage]

# Tracé du signal original et du signal échantillonné (sinusoïde)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(temps, signal_sin, label='Signal sinusoïdal original')
plt.plot(temps_echantillonne, signal_sin_echantillonne, 'o-', label='Signal sinusoïdal échantillonné')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.title(f'Échantillonnage du signal sinusoïdal à {frequence_echantillonnage} Hz')
plt.legend()
plt.grid(True)


# Tracé du signal original et du signal échantillonné (triangulaire)
# plt.subplot(2, 1, 2)
# plt.plot(temps, signal_triangle, label='Signal triangulaire original')
# plt.plot(temps_echantillonne, signal_triangle_echantillonne, 'o-', label='Signal triangulaire échantillonné')
# plt.xlabel('Temps (s)')
# plt.ylabel('Amplitude')
# plt.title(f'Échantillonnage du signal triangulaire à {frequence_echantillonnage} Hz')
# plt.legend()
# plt.grid(True)

plt.tight_layout()
plt.show()
