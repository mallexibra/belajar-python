import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    file_path = "hour.csv"  # Sesuaikan dengan lokasi file
    df = pd.read_csv(file_path)
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

df = load_data()

# Streamlit layout
st.title("📊 Dashboard Analisis Penyewaan Sepeda")

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")
selected_hour = st.sidebar.slider("Pilih Rentang Jam", 0, 23, (0, 23))
selected_weathersit = st.sidebar.multiselect("Pilih Kondisi Cuaca", df['weathersit'].unique(), df['weathersit'].unique())

# Terapkan filter ke dataset
df_filtered = df[(df['hr'].between(selected_hour[0], selected_hour[1])) & (df['weathersit'].isin(selected_weathersit))]

# Show Dataset
if st.checkbox("Tampilkan Data 🚲"):
    st.write(df_filtered.head())

# Visualisasi 1: Tren Peminjaman Sepeda Sepanjang Hari (berdasarkan filter)
st.subheader("📈 Tren Peminjaman Sepeda Sepanjang Hari (Sesuai Filter)")
hourly_rentals = df_filtered.groupby('hr')['cnt'].mean()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_rentals.index, y=hourly_rentals.values, marker="o", ax=ax)
ax.set_title("Rata-rata Jumlah Penyewaan Sepeda per Jam")
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Visualisasi 2: Dampak Cuaca terhadap Peminjaman Sepeda (berdasarkan filter)
st.subheader("🌦️ Pengaruh Cuaca terhadap Peminjaman Sepeda")
weather_rentals = df_filtered.groupby('weathersit')['cnt'].mean()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=weather_rentals.index, y=weather_rentals.values, palette="coolwarm", ax=ax)
ax.set_xlabel("Cuaca (1=Clear, 2=Cloudy, 3=Rain/Snow, 4=Extreme)")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Rata-rata Jumlah Penyewaan Berdasarkan Cuaca")
st.pyplot(fig)

# Visualisasi 3: Pola Peminjaman Pengguna Kasual vs Terdaftar (berdasarkan filter)
st.subheader("👥 Pola Peminjaman Pengguna Kasual vs Terdaftar")
casual_rentals = df_filtered.groupby('weekday')['casual'].mean()
registered_rentals = df_filtered.groupby('weekday')['registered'].mean()

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=casual_rentals.index, y=casual_rentals.values, label='Casual', marker="o", ax=ax)
sns.lineplot(x=registered_rentals.index, y=registered_rentals.values, label='Registered', marker="s", ax=ax)
ax.set_xticks(range(7))
ax.set_xticklabels(["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"])
ax.set_xlabel("Hari dalam Seminggu")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Perbedaan Pola Peminjaman: Pengguna Kasual vs Terdaftar")
st.pyplot(fig)

st.write("💡 **Dashboard ini membantu memahami pola peminjaman sepeda berdasarkan waktu, cuaca, dan jenis pengguna.** 🚴‍♂️📊")