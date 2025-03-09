import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Load Dataset
data = pd.read_csv("dashboard/all_data.csv")  # Pastikan path benar

# Konversi kolom tanggal ke format datetime
data["dteday"] = pd.to_datetime(data["dteday"])

# Menentukan rentang waktu minimal & maksimal
min_date = data["dteday"].min()
max_date = data["dteday"].max()

# Sidebar untuk filter
with st.sidebar:
    st.title("Dashboard Analisis Peminjaman Sepeda")
    st.write("Analisis data peminjaman sepeda berdasarkan berbagai faktor.")

    # Pilihan rentang waktu
    start_date, end_date = st.date_input(
        label='Pilih Rentang Waktu', 
        min_value=min_date,
        max_value=max_date, 
        value=[min_date, max_date]
    )

    # Validasi input rentang waktu
    if start_date > end_date:
        st.error("Tanggal mulai tidak boleh lebih besar dari tanggal akhir.")
        st.stop()

# Filter data berdasarkan rentang waktu
filtered_data = data[(data["dteday"] >= pd.Timestamp(start_date)) & (data["dteday"] <= pd.Timestamp(end_date))]

# **Statistik Peminjaman**
total_pinjaman = filtered_data["cnt_day"].sum()
rata_rata_pinjaman = round(filtered_data["cnt_day"].mean(), 2)
hari_terbanyak = filtered_data.loc[filtered_data["cnt_day"].idxmax(), "dteday"]
jumlah_hari_terbanyak = filtered_data["cnt_day"].max()

st.markdown(f"## **Total Peminjaman Sepeda: {total_pinjaman:,} Unit**")

# Layout dua kolom untuk statistik tambahan
col1, col2 = st.columns(2)

with col1:
    st.metric("Rata-rata Peminjaman per Hari", f"{rata_rata_pinjaman:,} Unit")
with col2:
    st.metric("Hari dengan Peminjaman Terbanyak", f"{hari_terbanyak.date()} ({jumlah_hari_terbanyak:,} Unit)")

st.divider()

# **Visualisasi Data**

# 1️⃣ Tren Peminjaman Sepeda dari Waktu ke Waktu

# Distribusi Peminjaman Sepeda per Jam
st.subheader("Distribusi Jumlah Peminjaman Sepeda per Jam")

fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(filtered_data["cnt_hour"], bins=30, kde=True, color="coral", ax=ax)

plt.xlabel("Jumlah Peminjaman")
plt.ylabel("Frekuensi")
plt.title("Distribusi Peminjaman Sepeda per Jam")
st.pyplot(fig)

st.divider()

# Distribusi Peminjaman Sepeda per Hari
st.subheader("Distribusi Peminjaman Sepeda per Hari")

fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(filtered_data["cnt_day"], bins=30, kde=True, color="coral", ax=ax)

plt.xlabel("Jumlah Peminjaman")
plt.ylabel("Frekuensi")
plt.title("Distribusi Peminjaman Sepeda per Hari")
st.pyplot(fig)

st.divider()

# Distribusi Peminjaman Sepeda Berdasarkan Hari Kerja
st.subheader("Distribusi Peminjaman Sepeda Berdasarkan Hari Kerja")

fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=filtered_data, x="workingday_day", y="cnt_day", palette="coolwarm")

ax.set_title("Distribusi Peminjaman Sepeda Berdasarkan Hari Kerja")
ax.set_xlabel("Hari Kerja (0: Libur, 1: Kerja)")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

st.divider()

# Tren Peminjaman Sepeda Sepanjang Hari
st.subheader("Tren Peminjaman Sepeda Sepanjang Hari")

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=filtered_data["dteday"], y=filtered_data["cnt_hour"], marker="o", color="coral", ax=ax)

plt.xlabel("Jam")
plt.ylabel("Rata-rata Peminjaman")
plt.title("Tren Peminjaman Sepeda sepanjang Hari")
st.pyplot(fig)

st.divider()

# Tren Peminjaman Sepeda Harian
st.subheader("Tren Peminjaman Sepeda Harian")

fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x=filtered_data["dteday"], y=filtered_data["cnt_day"], marker="o", ax=ax, color="coral")

plt.title("Tren Peminjaman Sepeda Harian")
plt.xlabel("Tanggal")
plt.ylabel("Jumlah Peminjaman")
plt.xticks(rotation=45)
st.pyplot(fig)

st.divider()

# Tren Peminjaman Berdasarkan Musim
st.subheader("Tren Peminjaman Berdasarkan Musim")

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=filtered_data, x="season_day", y="cnt_day", palette="pastel")

ax.set_title("Tren Peminjaman Berdasarkan Musim")
ax.set_xlabel("Musim (1: Semi, 2: Panas, 3: Gugur, 4: Dingin)")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

st.divider()

# Trend Peminjaman Sepeda dari Waktu ke Waktu
st.subheader("Tren Peminjaman Sepeda dari Waktu ke Waktu")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(filtered_data["dteday"], filtered_data["cnt_day"], marker="o", linestyle="-", color="coral", label="Total Peminjaman")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman")
ax.legend()
st.pyplot(fig)

st.divider()

# 2️⃣ Jam dengan Peminjaman Tertinggi
st.subheader("Jam dengan Peminjaman Tertinggi")
hour_avg = filtered_data.groupby("hr")["cnt_hour"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(hour_avg.index, hour_avg.values, color="coral")
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Peminjaman")
st.pyplot(fig)

# 3️⃣ Pengaruh Cuaca terhadap Peminjaman
st.subheader("Pengaruh Cuaca terhadap Jumlah Peminjaman")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="weathersit_day", y="cnt_day", data=filtered_data, ax=ax, color="coral")
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# 4️⃣ Pola Peminjaman Casual vs Registered
st.subheader("Pola Peminjaman Casual vs Registered")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(filtered_data["dteday"], filtered_data["casual_day"], label="Casual", color="red")
ax.plot(filtered_data["dteday"], filtered_data["registered_day"], label="Registered", color="green")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman")
ax.legend()
st.pyplot(fig)

# 5️⃣ Hubungan Suhu dengan Peminjaman
st.subheader("Hubungan Suhu dengan Jumlah Peminjaman")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x="temp_day", y="cnt_day", data=filtered_data, ax=ax, color="coral")
ax.set_xlabel("Suhu")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)
