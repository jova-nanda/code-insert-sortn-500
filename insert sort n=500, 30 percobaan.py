import random
import time

def percobaan_insertion_sort(jumlah_percobaan=30, n=500, range_nilai=(1, 1000), tampilkan_langkah=True):

    for percobaan in range(1, jumlah_percobaan + 1):
        # Generate data acak
        data = [random.randint(range_nilai[0], range_nilai[1]) for _ in range(n)]
        data_awal = data.copy()
        
        print(f"\n Percobaan {percobaan}")
        
        if n <= 20:
            print(f"   Data Awal : {data_awal}")
        else:
            print(f"   Data Awal : {data_awal[:10]} ... {data_awal[-10:]} (Total {n} data)")
        
        total_waktu_algoritma = 0
        
        # Proses sorting
        for i in range(1, n):
            start_step = time.perf_counter()
            
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
            
            end_step = time.perf_counter()
            durasi_langkah = end_step - start_step
            total_waktu_algoritma += durasi_langkah
            
            # HANYA PRINT JIKA tampilkan_langkah = True
            if tampilkan_langkah:
                # Agar array tidak terlalu panjang di layar, tampilkan sebagian saja
                tampilan_data = data if n <= 20 else f"{data[:10]} ... {data[-10:]}"
                print(f"Langkah {i:<4} | {tampilan_data} | {durasi_langkah:.8f} s")
        
        print("-" * 80)
        
        # Tampilkan hasil akhir sebagian jika n besar
        if n <= 20:
            print(f"   Hasil Akhir : {data}")
        else:
            print(f"   Hasil Akhir : {data[:10]} ... {data[-10:]} (Total {n} data)")
            
        print(f"   Total Waktu Algoritma  : {total_waktu_algoritma:.6f} detik")
        print("=" * 80)

if __name__ == "__main__":
    percobaan_insertion_sort(jumlah_percobaan=1, n=500, range_nilai=(1, 1000), tampilkan_langkah=True)