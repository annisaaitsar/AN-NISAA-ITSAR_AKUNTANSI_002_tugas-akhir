import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari file CSV
produk = pd.read_csv('produk.csv')
kota = pd.read_csv('kota.csv')
pelanggan = pd.read_csv('pelanggan.csv')
penjualan = pd.read_csv('penjualan.csv')
pengiriman = pd.read_csv('pengiriman.csv')

# Menampilkan lima baris pertama data
print("Lima baris pertama dari tabel produk:")
print(produk.head())
print("\nLima baris pertama dari tabel kota:")
print(kota.head())
print("\nLima baris pertama dari tabel pelanggan:")
print(pelanggan.head())
print("\nLima baris pertama dari tabel penjualan:")
print(penjualan.head())
print("\nLima baris pertama dari tabel pengiriman:")
print(pengiriman.head())

# Menggabungkan tabel penjualan dengan produk, pelanggan, dan kota
penjualan_full = penjualan.merge(produk, on='ProdukID') \
                          .merge(pelanggan, on='PelangganID') \
                          .merge(kota, on='KotaID')

# Scatter Plot
plt.subplot(2, 2, 1)
plt.scatter(penjualan_full['Umur'], penjualan_full['Jumlah'], color='blue', alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('Umur')
plt.ylabel('Jumlah')

# Histogram
plt.subplot(2, 2, 2)
plt.hist(penjualan_full['Jumlah'].dropna(), bins=20, color='orange', edgecolor='black')
plt.title('Histogram of Jumlah')
plt.xlabel('Jumlah')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(2, 2, 3)
plt.boxplot(penjualan_full['Jumlah'].dropna())
plt.title('Box Plot of Jumlah')
plt.ylabel('Jumlah')

# Membuat data untuk barplot kota
city_data = penjualan_full['NamaKota'].unique()
count_data = [penjualan_full[penjualan_full['NamaKota'] == city]['Jumlah'].sum() for city in city_data]

# Membuat barplot
plt.subplot(2, 2, 4)
plt.bar(city_data, count_data, color=['skyblue', 'green', 'red', 'purple', 'orange', 'brown'])
plt.title('Barplot Kota')
plt.xlabel('Kota')
plt.ylabel('Total Jumlah')

# Menampilkan semua visualisasi dalam satu window
plt.tight_layout()
plt.show()