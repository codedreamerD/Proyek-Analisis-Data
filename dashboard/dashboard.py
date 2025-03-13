import pandas as pd
import calendar
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Konfigurasi tema dan layout
sns.set_theme(style="darkgrid")
st.set_page_config(layout="wide")

# Load dataset
day_df = pd.read_csv("D:/Bike-Sharing-Dashboard/data/day.csv")
hour_df = pd.read_csv("D:/Bike-Sharing-Dashboard/data/hour.csv")

# Konversi tanggal ke format datetime
day_df["dteday"] = pd.to_datetime(day_df["dteday"])

# Menambahkan kategori suhu, kelembaban, dan kecepatan angin
hour_df["temp_category"] = pd.cut(hour_df["temp"], bins=[0, 0.3, 0.6, 1], labels=['Cold', 'Mild', 'Hot'])
hour_df["humidity_category"] = pd.cut(hour_df["hum"], bins=[0, 0.3, 0.6, 1], labels=['Low', 'Medium', 'High'])
hour_df["windspeed_category"] = pd.cut(hour_df["windspeed"], bins=[0, 0.3, 0.6, 1], labels=['Low', 'Medium', 'High'])

with st.sidebar:
    st.title("Gowes on the Road!")
    st.write("Making every ride an adventure!")  # Motto

    # Rentang tanggal
    min_date = day_df["dteday"].min()
    max_date = day_df["dteday"].max()
    start_date, end_date = st.date_input("Rentang Waktu", [min_date, max_date], min_value=min_date, max_value=max_date)

# Pastikan format tanggal kompatibel
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data berdasarkan rentang tanggal
filtered_day_df = day_df[(day_df["dteday"] >= start_date) & (day_df["dteday"] <= end_date)]
filtered_hour_df = hour_df[hour_df["instant"].isin(filtered_day_df["instant"])]

def total_rentals(df):
    return df["cnt"].sum()

def by_season(df):
    season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    season_avg_rentals = df.groupby("season")["cnt"].mean().reset_index()
    season_avg_rentals["season_desc"] = season_avg_rentals["season"].map(season_map)
    return season_avg_rentals

st.header("Bike Rentals Dashboard")

# Menampilkan Total Rentals
st.metric("Total Bike Rentals", value=total_rentals(filtered_day_df))

st.subheader("Highest Bike Rentals per Month")

# Tambahkan Kolom Tahun dan Bulan
day_df['year'] = day_df['dteday'].dt.year
day_df['month'] = day_df['dteday'].dt.month

# Total peminjaman per bulan
month_rent = day_df.groupby(['year', 'month'])['cnt'].sum().reset_index()
month_rent['month'] = month_rent['month'].apply(lambda x: calendar.month_name[x])

# Menampilkan bulan dengan peminjaman tertinggi
for year in [2011, 2012]:
    highest_month = month_rent[month_rent['year'] == year].nlargest(1, 'cnt')
    st.write(f"{year}: Highest rentals in {highest_month['month'].values[0]} ({highest_month['cnt'].values[0]} rentals).")

st.subheader("Daily Rentals Pattern")

daily_rentals = filtered_day_df.groupby(filtered_day_df["dteday"].dt.day)["cnt"].agg(["max", "min", "mean"]).reset_index()

fig, ax = plt.subplots(1, 3, figsize=(18, 5))
metrics = ['max', 'min', 'mean']
titles = ['Maximum Rentals per Day', 'Minimum Rentals per Day', 'Average Rentals per Day']

for i, metric in enumerate(metrics):
    sns.barplot(data=daily_rentals, x='dteday', y=metric, ax=ax[i], palette="Oranges")
    ax[i].set_title(titles[i])
    ax[i].set_ylabel('Number of Rentals')
    ax[i].set_xlabel('Day')

plt.tight_layout()
st.pyplot(fig)

st.subheader("Casual vs Registered Users Rental Patterns")

hourly_rentals = filtered_hour_df.groupby("hr").agg(
    Casual_Mean=('casual', 'mean'),
    Registered_Mean=('registered', 'mean')
).reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_rentals["hr"], y=hourly_rentals["Casual_Mean"], label="Casual Users", marker="o", color="coral")
sns.lineplot(x=hourly_rentals["hr"], y=hourly_rentals["Registered_Mean"], label="Registered Users", marker="o", color="gray")
ax.set_title("Casual vs Registered Users Rental Patterns")
ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Average Rentals")
ax.legend()
st.pyplot(fig)

st.subheader("Impact of Weather on Bike Rentals")

# Suhu
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=hour_df['temp_category'], y=hour_df['cnt'], palette="Oranges", ax=ax)
ax.set_title("Peminjaman Sepeda Berdasarkan Kategori Suhu")
ax.set_xlabel("Suhu")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# Kelembaban
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x=hour_df['humidity_category'], y=hour_df['cnt'], palette="Oranges", ax=ax)
ax.set_title("Distribusi Peminjaman Sepeda Berdasarkan Kelembaban")
ax.set_xlabel("Kelembapan")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# Kecepatan Angin
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=hour_df['windspeed_category'], y=hour_df['cnt'], palette="Oranges", ax=ax)
ax.set_title("Peminjaman Sepeda Berdasarkan Kecepatan Angin")
ax.set_xlabel("Kategori Kecepatan Angin")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# Season
st.subheader("Average Rentals by Season")

season_avg_rentals = by_season(filtered_day_df)

plt.figure(figsize=(12, 7))

colors = sns.color_palette("Oranges", len(season_avg_rentals))

plt.bar(season_avg_rentals['season_desc'], season_avg_rentals['cnt'], color=colors)
plt.xlabel('Season')
plt.ylabel('Average Rentals (Unit)')
plt.title('Average Bike Rentals by Season')

st.pyplot(plt)