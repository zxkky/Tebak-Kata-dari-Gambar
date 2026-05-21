
import os
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ======== KONFIGURASI ========
# Tambahkan gambar dan jawaban di sini (nama file di folder images -> jawaban tanpa spasi besar kecil sensitif)
ITEMS = {
    'apple.jpg': 'APPLE',
    'banana.jpg': 'BANANA',
    'orange.jpg': 'ORANGE',
    'computer.jpg': 'COMPUTER',
    # contoh: 'mobil.png': 'MOBIL'
}

IMAGES_DIR = os.path.join(os.path.dirname(__file__), 'images')
MAX_IMG_W, MAX_IMG_H = 400, 300

# ======== UTIL ========

def load_image(path, max_w=MAX_IMG_W, max_h=MAX_IMG_H):
    img = Image.open(path)
    img.thumbnail((max_w, max_h), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


def shuffle_letters(word):
    letters = list(word)
    # Jika panjang 1 atau semua huruf sama, kembalikan apa adanya
    if len(set(letters)) == 1 or len(letters) <= 1:
        return letters
    while True:
        shuffled = random.sample(letters, len(letters))
        if shuffled != letters:
            return shuffled


# ======== APLIKASI ========
class TebakKataApp:
    def __init__(self, master):
        self.master = master
        master.title('Tebak Kata - Tebak Gambar')
        master.resizable(False, False)

        # ambil daftar item valid yang ada di folder images
        self.entries = []
        for fname, ans in ITEMS.items():
            p = os.path.join(IMAGES_DIR, fname)
            if os.path.isfile(p):
                self.entries.append((p, ans.upper()))
        if not self.entries:
            messagebox.showerror('Error', f'Tidak menemukan gambar di {IMAGES_DIR}. Tambahkan file gambar dan jalankan lagi.')
            master.destroy()
            return

        self.index = 0
        random.shuffle(self.entries)

        # Frame gambar
        self.frame_img = tk.Frame(master)
        self.frame_img.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.img_label = tk.Label(self.frame_img)
        self.img_label.pack()

        # Frame jawaban dan kontrol
        self.frame_ctrl = tk.Frame(master)
        self.frame_ctrl.grid(row=1, column=0, sticky='w', padx=10)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.frame_ctrl, textvariable=self.entry_var, font=('Arial', 18), width=20)
        self.entry.grid(row=0, column=0, columnspan=4, pady=(0,8))
        self.entry.bind('<Return>', lambda e: self.check_answer())

        self.btn_check = tk.Button(self.frame_ctrl, text='Periksa', command=self.check_answer, width=10)
        self.btn_check.grid(row=1, column=0, pady=4)
        self.btn_back = tk.Button(self.frame_ctrl, text='Kembali', command=self.backspace, width=10)
        self.btn_back.grid(row=1, column=1, pady=4)
        self.btn_clear = tk.Button(self.frame_ctrl, text='Clear', command=self.clear_entry, width=10)
        self.btn_clear.grid(row=1, column=2, pady=4)
        self.btn_next = tk.Button(self.frame_ctrl, text='Next', command=self.next_item, width=10)
        self.btn_next.grid(row=1, column=3, pady=4)

        # Frame huruf
        self.frame_letters = tk.Frame(master)
        self.frame_letters.grid(row=2, column=0, columnspan=2, padx=10, pady=(0,10))

        # status label
        self.status_var = tk.StringVar()
        self.status_label = tk.Label(master, textvariable=self.status_var, anchor='w')
        self.status_label.grid(row=3, column=0, columnspan=2, sticky='w', padx=10)

        self.load_current_item()

    def load_current_item(self):
        p, ans = self.entries[self.index]
        self.current_path = p
        self.current_answer = ans
        self.entry_var.set('')
        self.status_var.set(f'Gambar {self.index+1} dari {len(self.entries)}. Panjang kata: {len(ans)}')

        # load gambar
        try:
            self.photo = load_image(p)
            self.img_label.config(image=self.photo)
        except Exception as e:
            self.img_label.config(text=f'Gagal memuat gambar:\n{p}')

        # set huruf acak
        letters = shuffle_letters(ans)
        # jika jawaban mengandung spasi, tampilkan spasi sebagai pemisah (digunakan sedikit berbeda)
        # buat tombol huruf
        for widget in self.frame_letters.winfo_children():
            widget.destroy()

        # Menampilkan tombol huruf (dalam grid dua baris jika terlalu banyak)
        max_cols = 10
        for i, L in enumerate(letters):
            b = tk.Button(self.frame_letters, text=L, width=4, height=2,
                          command=lambda ch=L: self.add_letter(ch))
            r = i // max_cols
            c = i % max_cols
            b.grid(row=r, column=c, padx=2, pady=2)

    def add_letter(self, ch):
        cur = self.entry_var.get()
        self.entry_var.set(cur + ch)

    def backspace(self):
        cur = self.entry_var.get()
        self.entry_var.set(cur[:-1])

    def clear_entry(self):
        self.entry_var.set('')

    def check_answer(self):
        guess = self.entry_var.get().strip().upper()
        if not guess:
            messagebox.showinfo('Info', 'Masukkan tebakan terlebih dahulu.')
            return
        if guess == self.current_answer:
            messagebox.showinfo('Benar!', 'Jawaban benar!')
            self.next_item()
        else:
            messagebox.showwarning('Salah', f'Jawaban salah: "{guess}"')

    def next_item(self):
        self.index = (self.index + 1) % len(self.entries)
        self.load_current_item()


if __name__ == '__main__':
    root = tk.Tk()
    app = TebakKataApp(root)
    root.mainloop()
