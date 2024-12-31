import os

def read_pembayaran(filename):
    pembayaran = []
    with open(filename, 'r') as file:
        for line in file:
            tanggal, semester, jumlah = line.strip().split(', ')
            pembayaran.append({
                'tanggal': tanggal,
                'semester': semester,
                'jumlah': int(jumlah),
            })
    return pembayaran

def hitung_total_pembayaran(pembayaran):
    total = 0
    for bayar in pembayaran:
        total += bayar['jumlah']
    return total

def cek_tertunggak(pembayaran):
    semester_terbayar = [bayar['semester'] for bayar in pembayaran]
    for i in range(1, 13): # Semester 1 hingga 13
        if f"Semester {i}" not in semester_terbayar:
            return i
    return None

def ringkasan_pembayaran(filename):
    pembayaran = read_pembayaran(filename)
    total = hitung_total_pembayaran(pembayaran)
    tertunggak = cek_tertunggak(pembayaran)

    print(f"Total Pembayaran untuk {filename}: Rp{total}")
    if tertunggak:
        print(f"Tertunggak: Semester {tertunggak}")
    else:
        print("Tertunggak: Tidak ada")

def main():
    NIM = input("Masukkan NIM Anda: ")
    filename = f"{NIM}_pembayaran.txt"
    if os.path.exists(filename):
        ringkasan_pembayaran(filename)
    else:
        print(f"File '{filename}' tidak ditemukan")

if __name__ == "__main__":
    main()