import os
from mainbot.address_tool import fix_json_format, filter_addresses
from mainbot.check_tx_history import check_transaction_history
from mainbot.send_tokens import send_all_tokens
from mainbot.banner import print_banner, verify_banner

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear()
    verify_banner()
    print_banner()
    input("\nTekan ENTER untuk mulai...")

    while True:
        clear()
        print_banner()
        print("🧠 TEA TOKEN TOOLBOX by @gilangportofolio\n")
        print("1️⃣  Perbaiki format JSON (→ addresses_fixed.json)")
        print("2️⃣  Filter duplikat dan format JSON (→ filtered_addresses_formatted.json)")
        print("3️⃣  Kirim token (send_tokens.py)")
        print("4️⃣  Cek histori transaksi wallet (.env)")
        print("0️⃣  Keluar\n")

        choice = input("Pilih menu (0-4): ")

        if choice == "1":
            fix_json_format()
        elif choice == "2":
            filter_addresses()
        elif choice == "3":
            send_all_tokens()
        elif choice == "4":
            check_transaction_history()
        elif choice == "0":
            print("👋 Keluar dari program.")
            break
        else:
            print("❌ Pilihan tidak valid.")

        input("\nTekan ENTER untuk kembali ke menu...")

if __name__ == "__main__":
    main_menu()
