import matplotlib.pyplot as plt
import numpy as np

# Set besarnya
plt.figure(figsize=(8,8))

# Banyak titik di grid
N = 50

# Radius lubang hitam
R = 1

# Set jauhnya bintang dari Lubang hitam
D = 5

# Buat grid
theta, phi = np.mgrid[0:2*np.pi:N*1j, 0:np.pi:N*1j]

# Hitung koordinat Lubang Hitam
x_bh = R * np.sin(phi) * np.cos(theta)
y_bh = R * np.sin(phi) * np.sin(theta)
z_bh = R * np.cos(phi)

# Hitung koordinat bintang
x_s = D * np.sin(phi) * np.cos(theta)
y_s = D * np.sin(phi) * np.sin(theta)
z_s = D * np.cos(phi)

# Hitung pembengkokan cahaya
x_l = x_s + (R**2 / D) * np.sin(phi) * np.cos(theta)
y_l = y_s + (R**2 / D) * np.sin(phi) * np.sin(theta)
z_l = z_s + (R**2 / D) * np.cos(phi)

# Buat grafik 3D
ax = plt.axes(projection='3d')

# Tambah lubang hitam
ax.plot_surface(x_bh, y_bh, z_bh, color='#000000')

# Tambah Bintang
ax.plot_surface(x_s, y_s, z_s, color='#FFFFFF')

# Tambah pembengkokan cahaya
ax.plot(x_l.flatten(), y_l.flatten(), z_l.flatten(), color='#FFFF00')

# label poros
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Tunukkan
plt.show()
