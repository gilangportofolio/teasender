import json

# Membaca alamat dari file JSON
with open("addresses.json", "r") as f:
    addresses = json.load(f)

# Memeriksa dan menghapus alamat duplikat
seen = set()
unique_addresses = []

for address in addresses:
    # Menggunakan .lower() untuk memastikan perbandingan alamat tidak case-sensitive
    if address.lower() not in seen:
        seen.add(address.lower())
        unique_addresses.append(address)

# Membuat format dengan " dan , (mengubah menjadi format list dengan tanda kutip ganda)
formatted_addresses = [f'"{address}"' for address in unique_addresses]

# Gabungkan alamat dengan koma
formatted_addresses_str = ",\n".join(formatted_addresses)

# Menyimpan alamat yang diformat ke dalam file baru
with open("filtered_addresses_formatted.json", "w") as f:
    f.write(f"[{formatted_addresses_str}]")

# Menampilkan jumlah alamat yang sudah difilter
print(f"✅ Alamat yang sudah difilter dan diformat telah disimpan dalam 'filtered_addresses_formatted.json'.")
print(f"Jumlah alamat unik: {len(unique_addresses)}")
