# Bike Sharing Dashboard

## Project Overview
Bike Sharing Dashboard ini dibuat untuk menganalisis dan memvisualisasikan pola peminjaman sepeda berdasarkan berbagai faktor seperti waktu, musim, hari kerja, dan kondisi cuaca. Dashboard ini dikembangkan menggunakan **Streamlit, Pandas, Seaborn, dan Matplotlib**, sehingga memberikan tampilan interaktif untuk mengeksplorasi tren penggunaan sepeda.

Proyek ini merupakan bagian dari latihan dalam **analisis data** untuk meningkatkan keterampilan dalam **data wrangling, exploratory data analysis (EDA), dan data visualization**. Melalui proyek ini, saya mempelajari bagaimana menangani dataset dunia nyata, mengidentifikasi tren, serta menyajikan hasil analisis secara efektif menggunakan Python.

---

## Features
✅ **Total Rentals Analysis** – Menampilkan jumlah total peminjaman sepeda dalam rentang waktu yang dipilih.

✅ **Daily Rentals Pattern** – Menunjukkan pola peminjaman sepeda per hari dalam sebulan.

✅ **Casual vs Registered Users Analysis** – Membandingkan pola peminjaman antara pengguna casual dan pengguna terdaftar berdasarkan jam.

✅ **Weather Impact Analysis** – Menganalisis bagaimana suhu, kelembaban, dan kecepatan angin mempengaruhi jumlah peminjaman sepeda.

✅ **Seasonal Trends** – Menampilkan tren peminjaman sepeda berdasarkan musim (Spring, Summer, Fall, Winter).

---

## Dataset
Proyek ini menggunakan **Bike Sharing Dataset**, yang terdiri dari dua file:

- **hour.csv** – Data peminjaman sepeda per jam.
- **day.csv** – Data peminjaman sepeda per hari.

Sumber dataset: **UCI Machine Learning Repository**

---

## Installation & Setup

1️⃣ **Clone Repository**
```bash
git clone https://github.com/codedreamerD/bike-sharing-dashboard.git
cd bike-sharing-dashboard
```

2️⃣ **Install Dependencies**
```bash
pip install pandas matplotlib seaborn streamlit
```

3️⃣ **Run the Dashboard**
```bash
streamlit run dashboard/dashboard.py
```

---

## Dashboard Deployment
Akses dashboard langsung di sini: **🔗 [Bike Sharing Dashboard](#)**

---

## Results & Insights
📌 **Peak Hours** – Peminjaman sepeda tertinggi terjadi pada jam sibuk pagi dan sore hari.

📌 **Seasonal Trends** – **Fall** memiliki jumlah peminjaman tertinggi, diikuti oleh **Summer**, sedangkan **Spring** memiliki peminjaman terendah.

📌 **Weather Impact** – Peminjaman sepeda menurun saat kelembaban dan kecepatan angin meningkat.

📌 **Working Days vs. Holidays** – Peminjaman sepeda lebih tinggi pada hari kerja dibandingkan hari libur.

---  
🚀 **Proyek ini bertujuan untuk membantu penyedia layanan dalam memahami tren peminjaman sepeda, sehingga strategi operasional dan promosi dapat dioptimalkan sesuai dengan faktor musiman dan lingkungan.** 