import json

# Dataset yang telah dibuat
dataset = {
  "restoran": {
    "nama": "WARWI (Warung Dwi)",
    "deskripsi": "Sebuah warung makan tradisional yang berkomitmen menyajikan makanan sehat, bergizi, dan terjangkau bagi masyarakat luas, terutama di kawasan Sunter Jaya. Mengusung konsep warteg kekinian, Warwi hadir sebagai solusi bagi mereka yang ingin menikmati hidangan rumahan yang lezat namun tetap memperhatikan asupan nutrisi. Dengan menu yang bervariasi dan dikembangkan oleh ahli gizi, Warwi tidak hanya memperhatikan rasa, tetapi juga kandungan kalori, protein, dan keseimbangan gizi dalam setiap porsi. Inovasi terbaru dari Warwi adalah integrasi teknologi chatbot berbasis AI dan NLP untuk membantu pelanggan memilih menu sehat sesuai kebutuhan gizi harian mereka, menjadikan pengalaman makan lebih informatif, praktis, dan personal.",
    "informasi_kontak": {
      "lokasi": "Sunter Jaya, Jakarta Utara",
      "telepon": "085960143403",
      "email": "warwi@gmail.com"
    },
    "jam_operasional": {
      "hari": "Setiap hari",
      "jam": "10.00 AM - 19.00 PM"
    },
    "media_sosial": {
      "whatsapp": "085960143403"
    },
    "chatbot": {
      "pesan_sambutan": "Halo! Saya chatbot Warung Dwi. Ada yang bisa saya bantu?"
    },
    "peta": "Google Maps lokasi Warung Dwi di Sunter Jaya, Jakarta Utara"
  },
  "menu": {
    "favorit": [
      {
        "nama": "Ayam Goreng",
        "harga": "Rp 15.000 / pcs",
        "gambar": "images/ayam.png",
        "jumlah_terjual": "8000 pcs"
      },
      {
        "nama": "Ikan Tongkol",
        "harga": "Rp 3.000 / pcs",
        "gambar": "images/t.png",
        "jumlah_terjual": "3000 pcs"
      }
    ],
    "kategori": {
      "makanan": [
        {
          "nama": "Ayam Goreng",
          "harga": "Rp 15.000",
          "deskripsi": "Ayam goreng adalah hidangan populer yang terbuat dari potongan ayam dilapisi adonan tepung berbumbu, digoreng hingga matang sempurna dengan kulit renyah dan daging juicy di dalamnya.",
          "perkiraan_kandungan_gizi": {
            "kalori": "250-350 kalori per 100 gram",
            "protein": "20-30 gram",
            "lemak": "15-25 gram",
            "karbohidrat": "5-10 gram",
            "kolesterol": "70-100 mg",
            "sodium": "Beragam tergantung bumbu"
          },
          "catatan": "Kulit ayam mengandung sebagian besar lemak jenuh dan kolesterol. Penggunaan minyak sehat dan porsi wajar disarankan.",
          "kategori_menu": "Makanan"
        },
        {
          "nama": "Ikan Tongkol",
          "harga": "Rp 15.000",
          "deskripsi": "Hidangan ikan tongkol pedas yang dimasak dengan bumbu rempah pedas seperti cabai, bawang, kunyit, dan serai, memberikan rasa gurih pedas dengan tekstur lembut.",
          "perkiraan_kandungan_gizi": {
            "kalori": "150-250 kalori per 100 gram",
            "protein": "20-25 gram",
            "lemak": "5-15 gram",
            "karbohidrat": "5-10 gram",
            "sodium": "Tergantung garam bumbu"
          },
          "catatan": "Mengandung omega-3 dan berbagai vitamin B serta mineral. Rasa pedas mengandung capsaicin dan antioksidan bumbu alami.",
          "kategori_menu": "Makanan"
        },
        {
          "nama": "Cumi Goreng",
          "harga": "Rp 18.000",
          "deskripsi": "Cumi-cumi yang dilapisi tepung dan digoreng hingga renyah dengan bagian dalam yang lembut, disajikan bersama saus pelengkap.",
          "perkiraan_kandungan_gizi": {
            "kalori": "250-350 kalori per 100 gram",
            "protein": "15-20 gram",
            "lemak": "15-25 gram",
            "karbohidrat": "10-20 gram",
            "kolesterol": "150-200 mg",
            "sodium": "Tergantung bumbu dan saus"
          },
          "catatan": "Penggunaan minyak sehat dan porsi moderat disarankan. Alternatif memasak lebih sehat tersedia.",
          "kategori_menu": "Makanan"
        },
        {
          "nama": "Tahu Goreng",
          "harga": "Rp 3.000",
          "deskripsi": "Tahu yang digoreng hingga berwarna keemasan dengan tekstur renyah luar dan lembut dalam, sering disajikan dengan pelengkap seperti sambal dan kecap.",
          "perkiraan_kandungan_gizi": {
            "kalori": "150-200 kalori per 100 gram",
            "protein": "10-15 gram",
            "lemak": "10-15 gram",
            "karbohidrat": "2-5 gram",
            "serat": "1-2 gram"
          },
          "catatan": "Penggunaan minyak sehat dan porsi sedang disarankan. Tahu mengandung isoflavon yang bermanfaat.",
          "kategori_menu": "Appetizer"
        },
        {
          "nama": "Salad Sayuran Segar",
          "harga": "Rp 13.000",
          "deskripsi": "Campuran sayuran mentah segar dengan tekstur renyah dan rasa segar, sering disajikan dengan dressing ringan.",
          "perkiraan_kandungan_gizi": {
            "kalori": "Rendah hingga sedang, tergantung dressing",
            "protein": "Rendah",
            "lemak": "Rendah hingga sedang, tergantung dressing",
            "karbohidrat": "Rendah hingga sedang",
            "serat": "Tinggi"
          },
          "catatan": "Pilih dressing rendah kalori untuk kesehatan optimal. Variasi sayuran memperkaya nutrisi.",
          "kategori_menu": "Appetizer"
        },
        {
          "nama": "Sup Sayur Bening",
          "harga": "Rp 13.000",
          "deskripsi": "Sup dengan kuah bening dan sayuran segar yang direbus dengan bumbu sederhana, menghasilkan hidangan yang segar dan bergizi.",
          "perkiraan_kandungan_gizi": {
            "kalori": "50-150 kalori per porsi",
            "protein": "2-5 gram",
            "lemak": "Sangat rendah",
            "karbohidrat": "5-15 gram",
            "serat": "3-7 gram"
          },
          "catatan": "Kandungan gizi bergantung bahan sayur dan tambahan. Cocok untuk menu rendah kalori.",
          "kategori_menu": "Soup"
        }
      ],
      "minuman": [
        {
          "nama": "Teh Manis (Dingin atau Panas)",
          "harga": "Rp 5.000",
          "deskripsi": "Teh hitam dengan gula sebagai pemanis, disajikan panas atau dingin dengan es batu. Rasa manis dan aroma khas teh yang menyegarkan.",
          "perkiraan_kandungan_gizi": {
            "kalori": "50-150 kalori per gelas",
            "karbohidrat": "12-38 gram",
            "gula": "Bergantung jumlah gula",
            "lemak": "< 0.1 gram",
            "protein": "< 0.1 gram"
          },
          "catatan": "Kandungan gula tinggi. Konsumsi seimbang disarankan untuk kesehatan.",
          "kategori_menu": "Minuman"
        },
        {
          "nama": "Teh Tawar / Tanpa Gula (Dingin atau Panas)",
          "harga": "Rp 5.000",
          "deskripsi": "Teh hitam, hijau, putih, atau oolong yang hanya diseduh tanpa pemanis, menawarkan rasa asli dan manfaat antioksidan.",
          "perkiraan_kandungan_gizi": {
            "kalori": "0-2 kalori per gelas",
            "karbohidrat": "< 0.5 gram",
            "gula": "0 gram",
            "lemak": "< 0.1 gram",
            "protein": "< 0.1 gram"
          },
          "catatan": "Pilihan minuman sehat dengan manfaat antioksidan dan rendah kalori.",
          "kategori_menu": "Minuman"
        },
        {
          "nama": "Kopi Good Day Cappuccino",
          "harga": "Rp 5.000",
          "deskripsi": "Minuman kopi instan dalam sachet dengan rasa cappuccino, creamy dan manis, mudah disajikan dengan air panas.",
          "perkiraan_kandungan_gizi": {
            "kalori": "100-130 kalori per sachet",
            "karbohidrat": "15-20 gram",
            "gula": "10-15 gram",
            "lemak": "3-5 gram",
            "protein": "< 1 gram",
            "sodium": "10-40 mg"
          },
          "catatan": "Mengandung gula dan lemak jenuh, konsumsi disarankan dengan bijak.",
          "kategori_menu": "Minuman"
        },
        {
          "nama": "Kopi ABC Susu",
          "harga": "Rp 5.000",
          "deskripsi": "Kopi instan dengan campuran bubuk kopi, gula, dan krimer susu, praktis disajikan dan memiliki rasa creamy manis.",
          "perkiraan_kandungan_gizi": {
            "kalori": "130-160 kalori per sachet",
            "karbohidrat": "20-25 gram",
            "gula": "15-20 gram",
            "lemak": "4-7 gram",
            "protein": "< 1 gram",
            "sodium": "20-50 mg"
          },
          "catatan": "Mengandung gula dan lemak jenuh, konsumsi secukupnya untuk kesehatan.",
          "kategori_menu": "Minuman"
        }
      ]
    }
  }
}



# Simpan dataset ke file JSON
with open('dataset.json', 'w', encoding='utf-8') as json_file:
    json.dump(dataset, json_file, ensure_ascii=False, indent=4)

print("Dataset telah disimpan ke 'dataset.json'")
