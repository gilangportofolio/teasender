from web3 import Web3
import os
from dotenv import load_dotenv

def check_transaction_history():
    load_dotenv()

    RPC_URL = os.getenv("RPC_URL")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")

    if not RPC_URL or not PRIVATE_KEY:
        print("❌ RPC_URL atau PRIVATE_KEY belum diset di .env")
        return

    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    account = w3.eth.account.from_key(PRIVATE_KEY)
    my_address = account.address

    try:
        tx_count = w3.eth.get_transaction_count(my_address)
        print(f"🔍 Alamat wallet kamu: {my_address}")
        print(f"📦 Total transaksi keluar (outbound): {tx_count}")
        print(f"📬 Lihat detail: https://sepolia.tea.xyz/address/{my_address}")
    except Exception as e:
        print(f"❌ Gagal mengambil data transaksi: {e}")

# Untuk debug langsung tanpa main.py
if __name__ == "__main__":
    check_transaction_history()
