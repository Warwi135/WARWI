# # import google.generativeai as genai

# # genai.configure(api_key="AIzaSyDtIORgv9uGsJ72NkTUk6UsUss5l2u4LXo")  # Ganti dengan API key kamu

# # # Gunakan model terbaru
# # model = genai.GenerativeModel("gemini-2.0-flash")

# # try:
# #     response = model.generate_content("Halo! Apa kabar?")
# #     print("✅ Jawaban:", response.text)
# # except Exception as e:
# #     print("❌ Error:", e)
# import logging
# import google.generativeai as genai

# # Konfigurasi logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Mengonfigurasi API key
# genai.configure(api_key="AIzaSyDtIORgv9uGsJ72NkTUk6UsUss5l2u4LXo")  # Ganti dengan API key Anda

# # Menggunakan model terbaru
# model = genai.GenerativeModel("gemini-2.0-flash")

# try:
#     user_input = "Halo! Apa kabar?"
#     logging.info(f"Sending request to API with input: {user_input}")
    
#     response = model.generate_content(user_input)
    
#     logging.info("Received response from API")
#     print("✅ Jawaban:", response.text)
# except Exception as e:
#     logging.error(f"❌ Error: {e}")


import requests
import os
from dotenv import load_dotenv

# Load API key dari .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def cek_gemini_api():
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [
            {
                "parts": [{"text": "Cek status API"}]
            }
        ]
    }

    try:
        response = requests.post(
            GEMINI_API_URL,
            headers=headers,
            json=payload,
            params={'key': GEMINI_API_KEY}
        )

        if response.status_code == 200:
            print("✅ API Gemini aktif dan merespons dengan benar.")
            print("Contoh respons:", response.json()["candidates"][0]["content"]["parts"][0]["text"])

        elif response.status_code == 429:
            print("❗ Kuota API Gemini sudah habis (HTTP 429). Coba lagi besok.")

        elif response.status_code == 401:
            print("❌ API key tidak valid atau sudah kadaluwarsa (HTTP 401).")

        elif response.status_code == 403:
            print("⛔ Akses ditolak (HTTP 403). Periksa apakah API sudah diaktifkan di Google Cloud Console.")

        else:
            print(f"⚠️ Error lain: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print("🔌 Gagal menghubungi API Gemini:", e)

if __name__ == "__main__":
    cek_gemini_api()
