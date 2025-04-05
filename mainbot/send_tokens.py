import os
import json
import random
import time
import hashlib
from dotenv import load_dotenv
from web3 import Web3
from eth_account import Account

# ================================ PROTECTED BANNER ================================

BANNER_TEXT = """
===============================================
|   🚀 TEA TOKEN SENDER - CREATED BY PRAMM   |
|   GitHub: github.com/gilangportofolio       |
|   Discord: gpram                            |
===============================================
"""

def print_banner():
    print(BANNER_TEXT)

def get_banner_hash():
    return hashlib.sha256(BANNER_TEXT.encode()).hexdigest()

ORIGINAL_BANNER_HASH = "20e3cdc94d0a864a12208a1abb1b38ab3ab3a9b83fdaad8a12576902bf00b56b"

# ================================================================================

def send_all_tokens():
    if get_banner_hash() != ORIGINAL_BANNER_HASH:
        print("\n🚨 ERROR: Unauthorized modification detected in 'print_banner()'. Exiting... 🚨")
        return

    print_banner()
    load_dotenv()

    PRIVATE_KEY = os.getenv("PRIVATE_KEY")
    TOKEN_ADDRESS = os.getenv("TOKEN_ADDRESS")
    RPC_URL = "https://tea-sepolia.g.alchemy.com/public"
    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    SENDER_ADDRESS = Account.from_key(PRIVATE_KEY).address

    # Load sent addresses
    try:
        if os.path.exists("sent_addresses.json") and os.path.getsize("sent_addresses.json") > 0:
            with open("sent_addresses.json", "r") as f:
                sent_addresses = set(json.load(f))
        else:
            sent_addresses = set()
    except json.JSONDecodeError:
        print("⚠️ Error: 'sent_addresses.json' is corrupted. Reinitializing...")
        sent_addresses = set()
        with open("sent_addresses.json", "w") as f:
            json.dump([], f)

    try:
        min_amount, max_amount = map(int, input("💰 Token amount range (e.g., 1000,10000): ").split(","))
        min_delay, max_delay = map(int, input("⏱️ Delay range in seconds (e.g., 5,10): ").split(","))
        max_addresses = int(input("📦 Max addresses to process (default 101): ") or 101)
    except Exception as e:
        print(f"❌ Input error: {e}")
        return

    def send_token(to_address, amount, nonce):
        token_abi = '[{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}], "name":"transfer","outputs":[{"name":"","type":"bool"}], "type":"function"}]'
        token_contract = web3.eth.contract(address=TOKEN_ADDRESS, abi=token_abi)
        amount_in_wei = amount * (10 ** 18)
        tx = token_contract.functions.transfer(to_address, amount_in_wei).build_transaction({
            'chainId': 10218,
            'gas': 100000,
            'gasPrice': web3.to_wei('10', 'gwei'),
            'nonce': nonce
        })

        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        tx_link = f"https://sepolia.tea.xyz/tx/{web3.to_hex(tx_hash)}"
        print(f"✅ Sent {amount} ADP to {to_address} | TX: {tx_link}")
        return nonce + 1

    with open("addresses.json", "r") as f:
        wallet_addresses = json.load(f)

    nonce = web3.eth.get_transaction_count(SENDER_ADDRESS)
    processed = 0

    for address in wallet_addresses:
        if processed >= max_addresses:
            break
        address = web3.to_checksum_address(address)

        if address in sent_addresses:
            print(f"⚠️ Already sent to {address}, skipping.")
            continue

        amount = random.randint(min_amount, max_amount)
        nonce = send_token(address, amount, nonce)
        sent_addresses.add(address)

        with open("sent_addresses.json", "w") as f:
            json.dump(list(sent_addresses), f, indent=4)

        sleep_time = random.uniform(min_delay, max_delay)
        print(f"⏳ Waiting {sleep_time:.2f} seconds...")
        time.sleep(sleep_time)

        processed += 1

    print("🎉 All transactions completed!")

# Hanya untuk testing langsung
if __name__ == "__main__":
    send_all_tokens()
