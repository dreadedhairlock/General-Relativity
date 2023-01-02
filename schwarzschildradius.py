# Kita akan membuat kalkulator untuk menghitung radius Schwarzschild suatu benda
# Radius Schwarzschild adalah ukuran minimum dari sebuah bintang yang terjadi jika benda tersebut menjadi bintang hitam
# Rumus untuk menghitung radius Schwarzschild adalah:
#   R_s = 2 * G * M / c^2
#   G adalah konstanta gravitasi universal
#   M adalah massa benda
#   c adalah kecepatan cahaya

# Kita akan menggunakan konstanta G dan c yang telah ditentukan
G = 6.67430e-11  # m^3 / (kg * s^2)
c = 299792458  # m/s

# Kita akan menggunakan Tkinter untuk membuat GUI
from tkinter import *

# Fungsi ini akan dipanggil saat pengguna menekan tombol "Hitung"
def hitung_radius():
    # Kita dapatkan massa yang dimasukkan oleh pengguna
    massa = float(e1.get())

    # Kita hitung radius Schwarzschild dengan menggunakan rumus di atas
    radius = 2 * G * massa / c**2

    # Kita tampilkan hasil perhitungan kepada pengguna
    l2.config(text=f"Radius Schwarzschild: {radius:.3e} m")

# Kita buat window utama
root = Tk()
root.title("Kalkulator Radius Schwarzschild")

# Kita buat label untuk menampilkan instruksi kepada pengguna
l1 = Label(root, text="Masukkan massa benda (kg):")

# Kita buat entry field untuk meminta massa kepada pengguna
e1 = Entry(root)

# Kita buat tombol untuk menghitung radius Schwarzschild
b1 = Button(root, text="Hitung", command=hitung_radius)

# Kita buat label untuk menampilkan hasil perhitungan
l2 = Label(root, text="")

# Kita letakkan komponen-komponen GUI kita di window utama
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
b1.grid(row=1, column=0, columnspan=2)
l2.grid(row=2, column=0, columnspan=2)

# Kita jalankan event loop
root.mainloop()
