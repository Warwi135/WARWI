from flask import Flask, request, redirect, session, jsonify, send_from_directory
from flask_cors import CORS
import mysql.connector
import hashlib
import requests
import os
import json
import difflib
import re
from dotenv import load_dotenv

# Load .env file untuk API key
load_dotenv()

app = Flask(__name__)
app.secret_key = 'secretkey'
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host='warungdwi.mysql.pythonanywhere-services.com',
        user='WarungDwi',
        password='famzok152',
        database='WarungDwi$warung_dwi'
    )

# Muat dataset dari file JSON
with open('dataset.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

# API Key Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

@app.route('/')
def utama():
    return send_from_directory('.', 'utama.html')

@app.route('/utama')
def utamaa():
    return send_from_directory('.', 'utama.html')

@app.route('/get_nama')
def get_nama():
    nama = session.get('nama', None)
    if nama:
        return jsonify({'nama': nama})
    return jsonify({'nama': None}), 401

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM warwi WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            session['email'] = email
            session['nama'] = user['nama']
            return redirect('/index')
        else:
            return redirect('/login')
    else:
        return send_from_directory('.', 'login.html')

@app.route('/index')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = hashlib.sha256(request.form['password'].encode()).hexdigest()
    password_con = hashlib.sha256(request.form['passwordCon'].encode()).hexdigest()
    phone = request.form['phone']

    if not name or not email or not password or not password_con:
        return "Semua field harus diisi!", 400

    if password != password_con:
        return "Password dan konfirmasi tidak cocok!", 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM warwi WHERE email=%s", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        cursor.close()
        conn.close()
        return "Email sudah terdaftar!", 400

    cursor.execute("INSERT INTO warwi (nama, email, password, notelp) VALUES (%s, %s, %s, %s)", (name, email, password, phone))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/utama')

def jawab_dari_dataset(user_message):
    msg = user_message.lower()
    no_wa = dataset['restoran']['informasi_kontak']['telepon']
    lokasi = dataset['restoran']['informasi_kontak']['lokasi']
    jam = dataset["restoran"]["jam_operasional"]["jam"]
    hari = dataset["restoran"]["jam_operasional"]["hari"]
    deskripsi_warwi = dataset["restoran"]["deskripsi"]

    frasa_diet = [
        "kalori rendah", "rendah kalori", "diet", "menu diet",
        "makanan diet", "lagi diet", "untuk diet", "diet sehat"
    ]

    # 0. Intent umum: "bisa pesan?"
    if "bisa pesan" in msg or "pesan di sini" in msg or "order di sini" in msg:
        return f"Ya, tentu! Kamu bisa pesan menu Warwi lewat WhatsApp kami di {no_wa} 😊"

    # 1. Intent: pesan menu spesifik
    if any(x in msg for x in ["pesan", "order", "beli"]):
        jumlah = "beberapa"
        angka = re.findall(r'\b\d+\b', msg)
        if angka:
            jumlah = angka[0]

        for kategori in dataset["menu"]["kategori"].values():
            for item in kategori:
                nama_menu = item["nama"].lower()
                if nama_menu in msg or difflib.get_close_matches(nama_menu, [msg], n=1, cutoff=0.85):
                    return (
                        f"Kamu ingin pesan {jumlah} {item['nama']}? "
                        f"Silakan hubungi WhatsApp Warwi di {no_wa} untuk melakukan pemesanan ya 😊"
                    )

        return f"Tentu, kamu bisa memesan! Hubungi WhatsApp kami di {no_wa} dan sebutkan menu yang kamu mau ya 😊"

    # 2. Informasi Umum 
    if "menu favorit" in msg:
        favorit = dataset.get("menu", {}).get("favorit", [])
        if favorit:
            daftar = ", ".join(item["nama"] for item in favorit)
            return f"Menu favorit di Warwi antara lain: {daftar}."
        return "Maaf, tidak ada menu favorit yang tersedia."

    # Gabungan kontak (jam buka, lokasi, nomor WA)
    if ("jam buka" in msg or "buka jam berapa" in msg 
        or "lokasi" in msg or "alamat" in msg 
        or "nomor" in msg or "telepon" in msg or "whatsapp" in msg 
        or "kontak" in msg):
        return (
            f"Kontak Warwi:\n"
            f"- Lokasi: {lokasi}\n"
            f"- Jam buka: {hari}, pukul {jam}\n"
            f"- WhatsApp: {no_wa}"
        )

    if "tentang" in msg or "warwi itu" in msg or "apa itu warwi" in msg:
        return deskripsi_warwi

    # 3. Harga menu
    if "harga" in msg:
        for kategori in dataset["menu"]["kategori"].values():
            for item in kategori:
                nama = item["nama"].lower()
                if nama in msg or difflib.get_close_matches(nama, [msg], n=1, cutoff=0.85):
                    return f"Harga {item['nama']} adalah {item['harga']}"

    # 4. Menu rendah kalori
    if any(phrase in msg for phrase in frasa_diet):
        hasil = []
        for kategori in dataset["menu"]["kategori"].values():
            for item in kategori:
                gizi = item.get("perkiraan_kandungan_gizi", {})
                kalori_text = gizi.get("kalori", "").lower()
                angka = list(map(int, re.findall(r'\d+', kalori_text)))
                if angka and max(angka) <= 150:
                    hasil.append(
                        f"{item['nama']} → Kalori: {gizi.get('kalori', 'N/A')}, "
                        f"Protein: {gizi.get('protein', 'N/A')}"
                    )
        if hasil:
            return "Berikut menu rendah kalori yang cocok:\n- " + "\n- ".join(hasil)
        return "Maaf, saya tidak menemukan menu dengan kalori rendah."

    # 5. Menu tinggi protein
    if "protein tinggi" in msg or "tinggi protein" in msg or "butuh protein" in msg:
        hasil = []
        for kategori in dataset["menu"]["kategori"].values():
            for item in kategori:
                gizi = item.get("perkiraan_kandungan_gizi", {})
                protein_text = gizi.get("protein", "").lower()
                angka = list(map(int, re.findall(r'\d+', protein_text)))
                if angka and max(angka) >= 20:
                    hasil.append(
                        f"{item['nama']} → Protein: {gizi.get('protein', 'N/A')}, "
                        f"Kalori: {gizi.get('kalori', 'N/A')}"
                    )
        if hasil:
            return "Menu tinggi protein yang tersedia:\n- " + "\n- ".join(hasil)
        return "Maaf, tidak ada menu dengan protein tinggi yang tersedia."

    # 6. Cek kategori menu
    for kategori_nama, daftar in dataset["menu"]["kategori"].items():
        if kategori_nama.lower() in msg:
            nama_item = ", ".join(item["nama"] for item in daftar)
            return f"Berikut daftar menu {kategori_nama}: {nama_item}"

    # 7. Deskripsi menu
    for kategori in dataset["menu"]["kategori"].values():
        for item in kategori:
            nama_menu = item["nama"].lower()
            if nama_menu in msg or difflib.get_close_matches(nama_menu, [msg], n=1, cutoff=0.85):
                return f"{item['nama']}: {item['deskripsi']} Harga: {item['harga']}"

    # 8. Fallback jika tidak cocok
    return None



def gemini_fallback(user_message):
    headers = {'Content-Type': 'application/json'}
    prompt = (
        f"Pertanyaan pengguna: {user_message}\n\n"
        "Jawablah pertanyaan ini dengan pengetahuan umum terbaikmu. "
        "Gunakan gaya bahasa yang ramah dan mudah dimengerti."
    )

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(
            GEMINI_API_URL,
            headers=headers,
            json=payload,
            params={'key': GEMINI_API_KEY},
            timeout=10
        )

        if response.status_code == 200:
            try:
                return response.json()["candidates"][0]["content"]["parts"][0]["text"]
            except (KeyError, IndexError):
                return "Maaf, saya tidak bisa menjawab pertanyaan tersebut."

        elif response.status_code == 429:
            print("❗ Kuota habis:", response.text)
            return "Maaf, kuota penggunaan AI sedang habis. Coba lagi besok ya 😊"

        elif response.status_code == 401:
            print("❌ API Key tidak valid:", response.text)
            return "Maaf, layanan AI sedang tidak aktif. Silakan hubungi admin."

        elif response.status_code == 403:
            print("⛔ Akses ditolak:", response.text)
            return "Maaf, akses ke layanan AI saat ini dibatasi."

        else:
            print("⚠️ Error tidak dikenal:", response.status_code, response.text)
            return "Maaf, layanan AI sedang bermasalah. Coba lagi nanti ya."

    except requests.exceptions.RequestException as e:
        print("🔌 Error saat menghubungi Gemini API:", e)
        return "Maaf, terjadi masalah jaringan saat menghubungi AI. Coba lagi nanti ya."



@app.route('/chat', methods=['POST'])   
def chat(): 
    user_message = request.json.get('message', '')
    jawaban_dataset = jawab_dari_dataset(user_message)

    if jawaban_dataset:
        return jsonify({'reply': jawaban_dataset})
    else:
        bot_reply = gemini_fallback(user_message)
        return jsonify({'reply': bot_reply})

@app.route('/static', methods=['POST'])
def list_images():
    image_folder = 'static'
    images = os.listdir(image_folder)
    images = [img for img in images if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return jsonify(images)

@app.route('/list/css', methods=['GET'])
def list_css():
    css_folder = os.path.join(app.root_path, 'static/css')
    if not os.path.exists(css_folder):
        return jsonify([]), 404
    css_files = [f for f in os.listdir(css_folder) if f.lower().endswith('.css')]
    return jsonify(css_files)

@app.route('/list/js', methods=['GET'])
def list_js():
    js_folder = os.path.join(app.root_path, 'static/js')
    if not os.path.exists(js_folder):
        return jsonify([]), 404
    js_files = [f for f in os.listdir(js_folder) if f.lower().endswith('.js')]
    return jsonify(js_files)

if __name__ == '__main__':
    app.run(debug=True)
