import hashlib

BANNER_TEXT = """
===============================================
|   🚀 TEA TOKEN TOOLBOX - CREATED BY PRAMM   |
|   GitHub: github.com/gilangportofolio       |
|   Discord: gpram                            |
===============================================
"""

def print_banner():
    print(BANNER_TEXT)

def get_banner_hash():
    return hashlib.sha256(BANNER_TEXT.encode()).hexdigest()

# Hash asli yang valid dari BANNER_TEXT
ORIGINAL_BANNER_HASH = "1b2372134b7dc0e487aad4389c230c57d11e2f368c46c447010075030b9a6bb4"

def verify_banner():
    if get_banner_hash() != ORIGINAL_BANNER_HASH:
        print("\n🚨 ERROR: Banner telah dimodifikasi tanpa izin. Program dihentikan. 🚨")
        exit(1)
