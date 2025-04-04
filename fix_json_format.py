import json

# Membaca file yang salah format
with open("addresses.json", "r") as file:
    # Membaca seluruh baris dalam file
    lines = file.readlines()

# Menghapus spasi atau baris kosong
lines = [line.strip() for line in lines if line.strip()]

# Membuat list dari alamat yang ada di dalam file
addresses = [line.strip() for line in lines if line]

# Menyimpan hasil dalam format JSON yang valid
with open("addresses_fixed.json", "w") as file:
    json.dump(addresses, file, indent=4)

print("✅ File berhasil diperbaiki dan disimpan sebagai addresses_fixed.json")
