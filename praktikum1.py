# Mendefinisikan class bernama PersegiPanjang sebagai blueprint/template objek
class PersegiPanjang:

    # Method __init__ (Konstruktor): Otomatis dipanggil saat objek baru dibuat
    # 'self' mewakili objek itu sendiri, 'panjang' dan 'lebar' adalah parameter masukan
    def __init__(self, panjang, lebar):
        # Menyimpan nilai parameter 'panjang' ke dalam atribut/properti objek
        self.panjang = panjang
        # Menyimpan nilai parameter 'lebar' ke dalam atribut/properti objek
        self.lebar = lebar

    # Method untuk menghitung luas persegi panjang
    def luas(self):
        # Mengembalikan hasil perkalian antara atribut panjang dan lebar
        return self.panjang * self.lebar

    # Method untuk menghitung keliling persegi panjang
    def keliling(self):
        # Mengembalikan hasil rumus keliling: 2 * (panjang + lebar)
        return 2 * (self.panjang + self.lebar)

    # Dunder Method __str__: Menentukan tampilan teks saat objek di-print
    def __str__(self):
        # Menambahkan huruf 'f' (f-string) agar variabel {self.panjang} dan {self.lebar} terisi otomatis
        return (
            f"Persegi Panjang dengan panjang {self.panjang} cm, "
            f"dan lebar {self.lebar} cm"
        )


# Memastikan kode pengujian di bawah ini hanya berjalan jika file ini dieksekusi langsung
if __name__ == "__main__":

    # Instansiasi Objek: Membuat objek 'pp' dari class PersegiPanjang dengan panjang=3 dan lebar=2
    pp = PersegiPanjang(3, 2)

    # Mencetak deskripsi objek (menjalankan method __str__ secara otomatis)
    print(pp)

    # Memanggil method keliling() dari objek 'pp' dan mencetak hasilnya
    print("keliling:", pp.keliling(), "cm")

    # Memanggil method luas() dari objek 'pp' dan mencetak hasilnya
    print("luas:", pp.luas(), "cm^2")