import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
def load_data():
    file_path = "hour.csv"
    df = pd.read_csv(file_path)
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

df = load_data()

# Streamlit layout
st.title("Dashboard Analisis Penyewaan Sepeda")

# Sidebar Filters
st.sidebar.header("Filter Data")
selected_season = st.sidebar.multiselect("Pilih Musim", df['season'].unique(), df['season'].unique())
selected_hour = st.sidebar.slider("Pilih Jam", min_value=int(df['hr'].min()), max_value=int(df['hr'].max()), value=(0, 23))

df_filtered = df[(df['season'].isin(selected_season)) & (df['hr'].between(selected_hour[0], selected_hour[1]))]

# Show Dataset
if st.checkbox("Tampilkan Data"):
    st.write(df_filtered.head())

# Visualisasi 1: Rata-rata Penyewaan Sepeda per Jam
st.subheader("Rata-rata Penyewaan Sepeda per Jam")
hourly_rentals = df.groupby('hr')['cnt'].mean()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_rentals.index, y=hourly_rentals.values, marker="o", ax=ax)
ax.set_title("Rata-rata Jumlah Penyewaan Sepeda per Jam")
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Visualisasi 2: Distribusi Penyewaan Berdasarkan Cuaca
st.subheader("Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x='weathersit', y='cnt', data=df, palette="coolwarm", ax=ax)
ax.set_xlabel("Cuaca")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Visualisasi 3: Perbedaan Pola Peminjaman Pengguna Kasual & Terdaftar
st.subheader("Pola Peminjaman Pengguna Kasual vs Terdaftar")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=df['hr'], y=df['casual'], label='Casual', marker="o", ax=ax)
sns.lineplot(x=df['hr'], y=df['registered'], label='Registered', marker="s", ax=ax)
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.write("Dashboard ini membantu dalam memahami tren penyewaan sepeda berdasarkan berbagai faktor seperti waktu, cuaca, dan jenis pengguna.")