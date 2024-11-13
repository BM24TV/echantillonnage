import numpy as np
import matplotlib.pyplot as plt

# Définition du nombre de points
nombre_de_points = 20

# Génération des points sur l'axe x entre 0 et 2π
x = np.linspace(0, 2 * np.pi, nombre_de_points)

# Calcul des valeurs de la sinusoïde pour chaque point x
y = np.sin(x)

# Affichage des points (x, y)
print("Points de la sinusoïde :")
for i in range(nombre_de_points):
    print(f"Point {i+1}: x = {x[i]:.2f}, y = {y[i]:.2f}")

# Tracé de la sinusoïde
plt.plot(x, y, 'o-', label='Sinusoïde')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Tracé de la sinusoïde avec environ 20 points')
plt.legend()
plt.grid(True)
plt.show()
