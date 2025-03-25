import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    file_path = "../data/hour.csv"  # Sesuaikan dengan lokasi file
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

# Visualisasi 1: Tren Peminjaman Sepeda Sepanjang Hari
st.subheader("📈 Tren Peminjaman Sepeda Sepanjang Hari")
hourly_rentals = df_filtered.groupby('hr')['cnt'].mean()
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x=hourly_rentals.index, y=hourly_rentals.values, marker="o", linewidth=2, ax=ax)
ax.set_title("Rata-rata Jumlah Penyewaan Sepeda per Jam")
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_xticks(range(0, 24))
ax.grid(True)
st.pyplot(fig)

# Visualisasi 2: Pengaruh Cuaca terhadap Peminjaman Sepeda
st.subheader("🌦️ Pengaruh Cuaca terhadap Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=df_filtered, palette="coolwarm", ax=ax)
ax.set_title("Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda")
ax.set_xlabel("Cuaca (1=Clear, 2=Cloudy, 3=Rain/Snow, 4=Extreme)")
ax.set_ylabel("Jumlah Peminjaman")
ax.grid(axis="y", linestyle="--", alpha=0.7)
st.pyplot(fig)

# Visualisasi 3: Perbedaan Pola Peminjaman Pengguna Kasual vs Terdaftar
st.subheader("👥 Pola Peminjaman Pengguna Kasual vs Terdaftar")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x=df_filtered['hr'], y=df_filtered['casual'], label='Casual', marker="o", ax=ax)
sns.lineplot(x=df_filtered['hr'], y=df_filtered['registered'], label='Registered', marker="s", ax=ax)
ax.set_title("Perbedaan Pola Peminjaman antara Pengguna Kasual dan Terdaftar")
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_xticks(range(0, 24))
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.write("💡 **Dashboard ini membantu memahami pola peminjaman sepeda berdasarkan waktu, cuaca, dan jenis pengguna.** 🚴‍♂️📊")