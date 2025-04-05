# 🧠 TEA Token Toolbox by [@gilangportofolio](https://github.com/gilangportofolio)

> Otomatisasi pengiriman token di jaringan TEA Sepolia — dilengkapi fitur validasi, filtering, dan keamanan.  
> Dibuat dengan ❤️ oleh **Pram**.

---

## 📦 Fitur Utama

- ✅ Perbaiki dan validasi format file `addresses.json`
- 🔎 Filter alamat unik & hapus duplikat
- 🚀 Kirim token TEA ke banyak alamat dengan delay acak
- 🧾 Cek histori transaksi wallet
- 🔐 Banner proteksi anti modifikasi

---

## 🧰 Instalasi

Pastikan Python sudah terinstall (versi 3.8 ke atas), lalu jalankan:

```bash
pip install web3 python-dotenv requests
```

---

## 📂 Struktur Folder

```
.
├── main.py                             # Menu utama (interface CLI)
├── .env                                # Simpan PRIVATE_KEY dan TOKEN_ADDRESS
├── addresses.json                      # Daftar alamat tujuan
├── sent_addresses.json                 # Log alamat yang sudah dikirimi token
├── filtered_addresses_formatted.json  # Hasil filtering duplikat
├── addresses_fixed.json                # Alamat yang sudah diformat
├── mainbot/
│   ├── __init__.py
│   ├── address_tool.py                 # Perbaiki & filter alamat
│   ├── banner.py                       # Proteksi banner
│   ├── check_tx_history.py             # Cek histori transaksi
│   └── send_tokens.py                  # Fungsi utama pengiriman token
```

---

## ⚙️ Konfigurasi `.env`

Buat file `.env` di root folder dengan isi seperti berikut:

```
PRIVATE_KEY=your_private_key_here
TOKEN_ADDRESS=your_token_contract_address_here
RPC_URL=https://tea-sepolia.g.alchemy.com/public
```

---

## 🚀 Cara Penggunaan

Jalankan menu utama:

```bash
python main.py
```

### Menu CLI:

- 1️⃣ Perbaiki format file `addresses.json`
- 2️⃣ Filter alamat (hapus duplikat, validasi)
- 3️⃣ Kirim token ke daftar alamat
- 4️⃣ Cek histori transaksi wallet (.env)
- 0️⃣ Keluar dari program

---

## 🔧 Catatan Teknis

### 💰 Jumlah Token & Delay Acak

Jumlah token, delay & jumlah transaksi bisa diatur saat menjalankan menu **kirim token**:

- Contoh input token: `1000,10000` → acak antara 1k–10k token
- Contoh delay: `3,7` → delay 3–7 detik antar transaksi
- Contoh transaksi: `101` (standar misi)

---

## 🧾 Mengulang Transaksi

Jika ingin mengirim ulang ke alamat yang sama, hapus file:

```bash
sent_addresses.json
```

---

## ❗ Penting

- Jangan pernah membagikan `PRIVATE_KEY` kamu!
- Pastikan wallet memiliki cukup saldo & token untuk dikirim
- Hindari mengubah struktur file jika tidak memahami alur program

---

## 💬 Kontak

📧 GitHub: [github.com/gilangportofolio](https://github.com/gilangportofolio)  
💬 Discord: `gpram`

---

## 🎉 Penutup

Selamat menggunakan **TEA Token Toolbox**!  
Semoga memudahkan distribusi token Anda. 🚀
