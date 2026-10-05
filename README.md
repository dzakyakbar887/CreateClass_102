Penjelasan

Program diawali dengan membuat class PersegiPanjang. Class ini berfungsi sebagai cetakan atau blueprint untuk membuat objek persegi panjang.

Di dalam class terdapat constructor init yang digunakan untuk memberikan nilai awal pada objek. Constructor memiliki parameter panjang dan lebar. Nilai tersebut kemudian disimpan ke dalam atribut self.panjang dan self.lebar.

Program memiliki method luas() yang digunakan untuk menghitung luas persegi panjang. Perhitungannya menggunakan rumus panjang dikali lebar. Method ini menggunakan return untuk mengembalikan hasil perhitungan.

Selanjutnya terdapat method keliling() yang digunakan untuk menghitung keliling persegi panjang dengan rumus 2 dikali jumlah panjang dan lebar.

Program juga menggunakan str untuk menentukan tampilan objek ketika ditampilkan menggunakan print(). Pada bagian ini digunakan f-string agar nilai panjang dan lebar dapat dimasukkan ke dalam teks.

Bagian if name == "__main__" digunakan untuk memastikan kode di dalamnya dijalankan ketika file Python dijalankan secara langsung.

Kemudian dibuat sebuah objek bernama pp dari class PersegiPanjang dengan nilai panjang 3 cm dan lebar 2 cm. Objek tersebut digunakan untuk memanggil method luas() dan keliling() serta menampilkan informasi persegi panjang.

Hasil dari program adalah panjang 3 cm, lebar 2 cm, keliling 10 cm, dan luas 6 cm².
