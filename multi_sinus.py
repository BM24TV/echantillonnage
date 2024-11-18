import numpy as np
import matplotlib.pyplot as plt

# Fonction pour générer et tracer une sinusoïde
def tracer_sinusoide(frequence, amplitude, dephasage_deg, sampling_rate, duration):
    # Conversion du déphasage en radians
    dephasage_rad = np.deg2rad(dephasage_deg)
    
    # Calcul des points temporels
    t = np.linspace(0, duration, int(sampling_rate * duration))
    
    # Calcul de la sinusoïde
    omega = 2 * np.pi * frequence
    signal = amplitude * np.sin(omega * t + dephasage_rad)
    
    # Affichage des points (temps, signal)
    print(f"Points pour la sinusoïde à {frequence} Hz, amplitude {amplitude}, déphasage {dephasage_deg}° :")
    for i in range(len(t)):
        print(f"t = {t[i]:.5f}, f(t) = {signal[i]:.5f}")
    
    # Tracé
    plt.plot(t, signal, label=f'{frequence} Hz, {dephasage_deg}°, Umax={amplitude}')
    return t, signal

# Paramètres des sinusoïdes
frequences = [120, 260, 1080, 4102, 440, 2080]  # Fréquences en Hz
dephasages = [0, 45, 10, 0, 90, 30]  # Déphasages en degrés
amplitudes = [1, 0.8, 0.5, 1, 0.7, 0.6]  # Amplitudes maximales
sampling_rate = 10000  # Taux d'échantillonnage en Hz
duration = 0.01  # Durée en secondes

# Tracé des sinusoïdes
plt.figure(figsize=(12, 8))
for freq, amp, phase in zip(frequences, amplitudes, dephasages):
    tracer_sinusoide(freq, amp, phase, sampling_rate, duration)

# Configuration du graphique
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.title('Tracé de plusieurs sinusoïdes')
plt.legend()
plt.grid(True)
plt.show()
