import numpy as np
import matplotlib.pyplot as plt

# Paramètres globaux
fs = 48000  # Fréquence d'échantillonnage en Hz (nombre de points par seconde)
duration = 0.05  # Durée des sinusoïdes en secondes (ici, 50 ms)
t_specific = 21e-6  # Un instant spécifique pour lequel on calcule une valeur (21 microsecondes)

# Paramètres des sinusoïdes
frequences = [120, 260, 1080, 4102, 440, 2080]  # Fréquences des sinusoïdes en Hz
dephasages = [0, 45, 10, 0, 90, 30]  # Déphasages correspondants en degrés
amplitudes = [1, 1, 1, 1, 1, 1]  # Amplitudes maximales fixées à 1 (normalisées)

# Initialisation de l'axe temporel
t = np.linspace(0, duration, int(fs * duration), endpoint=False)  
# Création d'un tableau `t` représentant le temps, échantillonné entre 0 et `duration`
# Le nombre de points est donné par `fs * duration` (ici, 2400 points pour 50 ms)

# Initialisation de la somme des sinusoïdes (toutes les valeurs sont initialisées à 0)
signal_sum = np.zeros_like(t)

# Initialisation des sous-graphiques (un pour chaque sinusoïde, plus un pour la somme et la FFT)
n = len(frequences) + 2  # Nombre total de sous-graphiques : une par sinusoïde, un pour la somme, un pour la FFT
fig, axes = plt.subplots(n, 1, figsize=(10, 14), sharex=False)
# Création d'une figure avec `n` sous-graphiques empilés verticalement

# Génération et tracé des sinusoïdes individuelles
for i, (freq, phase, amp) in enumerate(zip(frequences, dephasages, amplitudes)):  
    # Boucle sur chaque fréquence, déphasage et amplitude
    
    dephasage_rad = np.deg2rad(phase)  
    # Conversion du déphasage de degrés en radians (car np.sin() attend des radians)
    
    omega = 2 * np.pi * freq  # Calcul de la pulsation ω = 2πf
    y = amp * np.sin(omega * t + dephasage_rad)  
    # Calcul de la sinusoïde avec la formule Umax * sin(ωt + déphasage)
    
    signal_sum += y  
    # Ajout de la sinusoïde actuelle à la somme des sinusoïdes
    
    f_t_specific = amp * np.sin(omega * t_specific + dephasage_rad)  
    # Calcul de la valeur instantanée de la sinusoïde à t_specific
    
    print(f"Sinusoïde {freq} Hz, déphasage {phase}° : f({t_specific:.2e}s) = {f_t_specific:.5f}")
    # Affichage de la valeur instantanée calculée
    
    axes[i].plot(t, y, label=f'{freq} Hz, {phase}°, Umax={amp}')  
    # Tracé de la sinusoïde dans son propre sous-graphe
    
    axes[i].set_title(f"Sinusoïde {freq} Hz, déphasage {phase}°")  
    # Ajout d'un titre indiquant les paramètres de la sinusoïde
    
    axes[i].set_ylabel("Amplitude")  # Étiquette de l'axe Y
    axes[i].set_xlim(0, 0.01)  # Zoom sur les premières périodes de la sinusoïde pour une meilleure lisibilité
    axes[i].grid(True)  # Affichage de la grille
    axes[i].legend()  # Affichage de la légende avec les paramètres

# Tracé de la somme des sinusoïdes
axes[-2].plot(t, signal_sum, label="Somme des sinusoïdes", color="black")  
# La somme des sinusoïdes est tracée sur l'avant-dernier sous-graphe

axes[-2].set_title("Somme des sinusoïdes")  # Titre de ce graphique
axes[-2].set_ylabel("Amplitude")  # Étiquette de l'axe Y
axes[-2].set_xlim(0, 0.01)  # Zoom sur les premières périodes
axes[-2].grid(True)  # Affichage de la grille
axes[-2].legend()  # Affichage de la légende

# Calcul de la FFT de la somme des sinusoïdes
fft_result = np.fft.fft(signal_sum)  
# Calcul de la transformée de Fourier rapide (FFT) de la somme des sinusoïdes

frequencies = np.fft.fftfreq(len(t), d=1/fs)  
# Calcul des fréquences associées à la FFT, en fonction de l'échantillonnage
print(frequencies) #Affichage dans la console des "frequencies"

half_n = len(t) // 2  # On garde seulement la moitié positive (le spectre est symétrique)
frequencies_positive = frequencies[:half_n]  # Extraction des fréquences positives
fft_magnitude = np.abs(fft_result[:half_n]) / len(t)  
# Extraction des amplitudes FFT positives et normalisation (division par la taille du signal)

# Tracé du spectre FFT
axes[-1].plot(frequencies_positive, fft_magnitude, label="Spectre FFT", color="red")  
# Tracé du spectre de fréquence (FFT) dans le dernier sous-graphe

axes[-1].set_title("Spectre de fréquence (FFT)")  # Titre
axes[-1].set_xlabel("Fréquence (Hz)")  # Étiquette de l'axe X
axes[-1].set_ylabel("Amplitude normalisée")  # Étiquette de l'axe Y
axes[-1].grid(True)  # Affichage de la grille
axes[-1].legend()  # Affichage de la légende

# Ajustement de l'affichage
plt.tight_layout()  # Réglage automatique des espaces entre les graphiques
plt.show()  # Affichage de tous les graphiques
