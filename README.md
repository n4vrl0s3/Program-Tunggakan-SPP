# Program Tunggakan SPP

This repository aims to provide a comprehensive starting point for understanding and implementing an SPP (Education Development Contribution) arrears tracking system. This program is implemented in Python and is suitable as an introduction to managing and tracking SPP payments for students, suitable for beginner and intermediate programmers.

<hr><br>

## Purpose of This Repository

This repository aims to provide a complete guide to understanding and implementing an SPP (Education Development Contribution) arrears tracking system. This program uses Python and is designed to help school administrators monitor and manage student SPP payments. By using this program, users can easily record, check, and update the status of student SPP payments, making it suitable for beginner and intermediate programmers who want to learn data management and practical applications in education.

<hr><br>

## Demonstration

Here is a simple demonstration of how to use the main functions in the program:

```python
# main.py

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
```

<hr><br>

## Features

- Record student SPP payments
- Check payment status
- Update payment status
- SPP arrears report

<hr><br>

## Technologies Used

- Python

<hr><br>

## Project Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/n4vrl0s3/Program-Tunggakan-SPP.git
   ```
2. **Navigate to the project directory**
   ```bash
   cd Program-Tunggakan-SPP
   ```
3. **Install the required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

<hr><br>

## Steps to Run

1. Ensure you have Python installed on your machine.
2. Run the program
   ```bash
   python main.py
   ```

<hr><br>

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<hr><br>

<div align="center">
  <a href="https://www.x.com/n4vrl0s3/">
    <img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=100:49108B,20:F3F8FF&section=footer&reversal=false&textBg=false&fontAlignY=50&descAlign=48&descAlignY=59"/>
  </a>
</div>
