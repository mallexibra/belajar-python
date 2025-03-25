# 📊 Bike Sharing Dashboard

Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis dataset penyewaan sepeda per jam. Data diambil dari dataset `hour.csv`, yang berisi informasi jumlah penyewaan sepeda berdasarkan berbagai faktor seperti cuaca, musim, hari kerja, dan lain-lain.

## 🚀 Fitur
- **Visualisasi Data**: Menampilkan berbagai grafik untuk memahami pola peminjaman sepeda.
- **Analisis Tren**: Melihat tren penggunaan sepeda berdasarkan waktu.
- **Filter Interaktif**: Memungkinkan pengguna menyaring data berdasarkan parameter tertentu.

## 🛠 Instalasi & Menjalankan
1. **Clone repository**:
   ```bash
   git clone https://github.com/mallexibra/belajar-python.git
   cd belajar-python
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Streamlit**:
   ```bash
   cd dashboard
   streamlit run dashboard.py
   ```

## 📊 Dataset
Dataset yang digunakan (`hour.csv`) memiliki kolom utama berikut:
- `dteday` : Tanggal
- `season` : Musim (1: Spring, 2: Summer, 3: Fall, 4: Winter)
- `hr` : Jam dalam sehari (0-23)
- `holiday` : Hari libur atau bukan (0: Bukan, 1: Libur)
- `weekday` : Hari dalam seminggu (0: Minggu, 6: Sabtu)
- `weathersit` : Kondisi cuaca (1-4)
- `temp` : Suhu normalisasi
- `cnt` : Jumlah total penyewaan sepeda

## 📌 Catatan
- Jika mengalami error saat menjalankan, pastikan dataset tersedia di path yang benar.
- Gunakan Python versi 3.8 atau lebih baru untuk kompatibilitas terbaik.
