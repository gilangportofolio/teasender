from web3 import Web3
import os
from dotenv import load_dotenv

# Load .env untuk ambil PRIVATE_KEY dan RPC
load_dotenv()

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

# Inisialisasi koneksi Web3
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# Ambil address dari private key
account = w3.eth.account.from_key(PRIVATE_KEY)
my_address = account.address

# Ambil total outbound transaction (nonce)
tx_count = w3.eth.get_transaction_count(my_address)

# Tampilkan hasil
print(f"🔍 Alamat wallet kamu: {my_address}")
print(f"📦 Total transaksi keluar (outbound): {tx_count}")
print(f"📬 Lihat detail: https://sepolia.tea.xyz/address/{my_address}")
