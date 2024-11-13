#np.linspace(start, stop, num)
import numpy as np
import matplotlib.pyplot as plt

# Fonction pour générer et tracer une sinusoïde
def tracer_sinusoide(frequence, nombre_de_points, nombre_de_periodes):
    # Définition de la période de la sinusoïde
    periode = 1 / frequence
    
    # Génération de l'axe temporel en fonction du nombre de périodes souhaité
    temps = np.linspace(0, nombre_de_periodes * periode, nombre_de_points)
    
    # Calcul des valeurs de la sinusoïde
    signal_sin = np.sin(2 * np.pi * frequence * temps)
    
    # Affichage des points (temps, signal_sin)
    print("Points de la sinusoïde :")
    for i in range(nombre_de_points):
        print(f"Point {i+1}: x = {temps[i]:.2f}, y = {signal_sin[i]:.2f}")
    
    # Tracé de la sinusoïde
    plt.plot(temps, signal_sin, 'o-', label=f'Sinusoïde {frequence} Hz')
    plt.xlabel('Temps (s)')
    plt.ylabel('Amplitude')
    plt.title(f'Tracé de la sinusoïde à {frequence} Hz\navec {nombre_de_periodes} période(s) et {nombre_de_points} points')
    plt.legend()
    plt.grid(True)
    plt.show()

# Paramètres de la sinusoïde
frequence = 2  # Fréquence en Hertz (Hz)
nombre_de_points = 50  # Nombre de points à tracer
nombre_de_periodes = 3  # Nombre de périodes de la sinusoïde

# Appel de la fonction pour tracer la sinusoïde
tracer_sinusoide(frequence, nombre_de_points, nombre_de_periodes)


