import json
import os

def fix_json_format():
    try:
        with open("addresses.json", "r") as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]
        addresses = [line for line in lines if line]
        with open("addresses_fixed.json", "w") as file:
            json.dump(addresses, file, indent=4)
        print("✅ File berhasil diperbaiki dan disimpan sebagai 'addresses_fixed.json'")
    except Exception as e:
        print(f"❌ Gagal memperbaiki file: {e}")

def filter_addresses():
    try:
        with open("addresses.json", "r") as f:
            addresses = json.load(f)
        seen = set()
        unique_addresses = []
        for address in addresses:
            if address.lower() not in seen:
                seen.add(address.lower())
                unique_addresses.append(address)
        formatted_addresses = [f'"{address}"' for address in unique_addresses]
        formatted_addresses_str = ",\n".join(formatted_addresses)
        with open("filtered_addresses_formatted.json", "w") as f:
            f.write(f"[{formatted_addresses_str}]")
        print("✅ Alamat yang sudah difilter dan diformat telah disimpan dalam 'filtered_addresses_formatted.json'.")
        print(f"Jumlah alamat unik: {len(unique_addresses)}")
    except Exception as e:
        print(f"❌ Gagal memfilter alamat: {e}")

def main_menu():
    while True:
        print("\n📜 MENU TEA Address Tool")
        print("\n📜 Pastikan Addres disimpan dlu di addresses.json")
        print("1. Perbaiki format addresses.json → addresses_fixed.json")
        print("2. Filter dan format addresses.json → filtered_addresses_formatted.json")
        print("0. Keluar")

        choice = input("Pilih menu (0-2): ")

        if choice == "1":
            fix_json_format()
        elif choice == "2":
            filter_addresses()
        elif choice == "0":
            print("👋 Keluar dari program.")
            break
        else:
            print("❌ Pilihan tidak valid.")

if __name__ == "__main__":
    main_menu()
