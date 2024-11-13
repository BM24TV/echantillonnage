import numpy as np
import matplotlib.pyplot as plt

# Paramètres
nombre_de_points = 20
frequence = 2  # Fréquence de la sinusoïde

# Génération des points sur l'axe x entre 0 et 2π
x = np.linspace(0, 2 * np.pi, nombre_de_points)

# Calcul des valeurs de la sinusoïde pour chaque point x avec la fréquence
y = np.sin(frequence * x)

# Affichage des points (x, y)
print("Points de la sinusoïde :")
for i in range(nombre_de_points):
    print(f"Point {i+1}: x = {x[i]:.2f}, y = {y[i]:.2f}")

# Tracé de la sinusoïde
plt.plot(x, y, 'o-', label=f'Sinusoïde avec fréquence f = {frequence}')
plt.xlabel('x')
plt.ylabel('sin(f * x)')
plt.title(f'Tracé de la sinusoïde avec fréquence f = {frequence}')
plt.legend()
plt.grid(True)
plt.show()
