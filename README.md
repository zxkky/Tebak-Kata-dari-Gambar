# 🖼️ Tebak Kata dari Gambar

Game edukasi desktop **tebak kata berbasis gambar** yang dibangun dengan Python dan Tkinter. Pemain menebak kata dari gambar yang ditampilkan menggunakan tombol huruf acak — cocok untuk pembelajaran kosakata maupun hiburan ringan.

---

## 🎮 Cara Bermain

1. Sebuah gambar akan ditampilkan di layar
2. Di bawah gambar, muncul tombol-tombol **huruf acak** dari jawaban
3. Klik tombol huruf untuk menyusun jawaban, atau ketik langsung di kolom input
4. Tekan **Periksa** atau `Enter` untuk mengecek jawaban
5. Tekan **Next** untuk lanjut ke gambar berikutnya

---

## ✨ Fitur

- Tampilan gambar otomatis dengan resize proporsional (maks. 400×300 px)
- Huruf jawaban **diacak** secara otomatis setiap soal
- Input bisa lewat **klik tombol huruf** atau **ketik keyboard**
- Tombol `Backspace` dan `Clear` untuk koreksi jawaban
- Navigasi soal dengan tombol **Next** (bisa skip)
- Dukungan soal **tidak terbatas** — tinggal tambah gambar dan jawaban di konfigurasi
- Bisa dikompilasi menjadi file `.exe` dengan PyInstaller

---

## 📁 Struktur Proyek

```
tebak-kata-gambar/
├── tebak_kata_gambar.py    # File utama aplikasi
├── tebak_kata_gambar.spec  # Konfigurasi build PyInstaller
├── images/                 # Folder gambar soal (buat manual)
│   ├── apple.jpg
│   ├── banana.jpg
│   └── ...
└── README.md
```

> **Penting:** Folder `images/` tidak disertakan di repo. Buat sendiri dan isi dengan gambar sesuai konfigurasi `ITEMS` di kode.

---

## 🚀 Cara Menjalankan

### Prasyarat

- Python 3.8+
- Pillow

```bash
pip install Pillow
```

### Jalankan langsung

```bash
python tebak_kata_gambar.py
```

---

## ➕ Menambah Soal

Buka `tebak_kata_gambar.py`, cari bagian `ITEMS`, lalu tambahkan pasangan nama file gambar dan jawabannya:

```python
ITEMS = {
    'apple.jpg':    'APPLE',
    'banana.jpg':   'BANANA',
    'orange.jpg':   'ORANGE',
    'computer.jpg': 'COMPUTER',
    'mobil.png':    'MOBIL',      # ← tambahkan di sini
    'kucing.jpg':   'KUCING',     # ← dan seterusnya
}
```

Kemudian letakkan file gambarnya di folder `images/`. Format yang didukung: `.jpg`, `.jpeg`, `.png`, `.bmp`, dll (semua yang didukung Pillow).

---

## 📦 Build ke Executable (.exe)

Pastikan PyInstaller sudah terinstal:

```bash
pip install pyinstaller
```

Build menggunakan file spec yang sudah tersedia:

```bash
pyinstaller tebak_kata_gambar.spec
```

File `.exe` akan tersimpan di folder `dist/`. Folder `images/` akan otomatis ikut dikemas di dalam executable.

---

## 🛠️ Teknologi

| Komponen | Keterangan |
|---|---|
| Python 3 | Bahasa pemrograman utama |
| Tkinter | GUI bawaan Python |
| Pillow (PIL) | Load & resize gambar |
| PyInstaller | Build ke `.exe` |

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan lomba / pembelajaran. Bebas digunakan dan dimodifikasi.
