# 🛡️ Smart Bullying Detection System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Sistem deteksi otomatis cyberbullying & ujaran kebencian pada komentar media sosial berbahasa Indonesia menggunakan Machine Learning.**

[🚀 Demo Live](#) · [📓 Notebook](#) · [📊 Dataset](#)

</div>

---

## 📌 Tentang Proyek

Proyek ini merupakan tugas mata kuliah **Kecerdasan Buatan** Program Studi D3 Teknik Informatika, Universitas Sumatera Utara (USU). Sistem ini mampu mendeteksi apakah sebuah komentar media sosial berbahasa Indonesia mengandung unsur **cyberbullying** atau **ujaran kebencian (hate speech)** secara otomatis menggunakan algoritma Support Vector Machine (SVM).

### 🌍 Keterkaitan dengan SDGs (Sustainable Development Goals)

| SDG | Tujuan | Relevansi |
|-----|--------|-----------|
| 🕊️ **SDG 16** | Peace, Justice & Strong Institutions | Perlindungan warga digital dari kekerasan siber |
| 📚 **SDG 4** | Quality Education | Lingkungan belajar online yang lebih aman |
| 💚 **SDG 3** | Good Health & Well-being | Menjaga kesehatan mental pengguna media sosial |
| ⚖️ **SDG 10** | Reduced Inequalities | Mencegah diskriminasi berbasis SARA di ruang digital |

---

## ✨ Fitur Utama

- 🔍 **Deteksi Real-time** — Analisis komentar secara langsung dengan hasil instan
- 🧠 **Model SVM** — Menggunakan Support Vector Machine dengan kernel linear (akurasi 84.81%)
- 📊 **Statistik Sesi** — Memantau jumlah komentar aman vs berbahaya yang dianalisis
- 📝 **Riwayat Analisis** — Menyimpan 5 analisis terakhir dalam satu sesi
- 🗣️ **Normalisasi Bahasa Alay** — Mampu memahami bahasa gaul/alay Indonesia
- 📱 **Responsive UI** — Tampilan bersih dan modern berbasis Streamlit

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Kegunaan |
|-----------|----------|
| Python 3.10+ | Bahasa pemrograman utama |
| Streamlit | Framework web app |
| Scikit-learn | Algoritma machine learning (SVM) |
| TF-IDF Vectorizer | Ekstraksi fitur teks |
| Pandas | Pengolahan data |
| Joblib | Menyimpan & memuat model |
| Regex | Pembersihan teks |

---

## 📁 Struktur Proyek

```
cyberbullying-detector/
│
├── app.py                        # Aplikasi web utama (Streamlit)
├── projek.ipynb                  # Notebook proses pelatihan model
│
├── model_svm_cyberbullying.joblib  # Model SVM yang sudah dilatih
├── tfidf_vectorizer.joblib         # TF-IDF vectorizer yang sudah dilatih
│
├── data.csv                      # Dataset mentah Twitter
├── data_clean.csv                # Dataset setelah preprocessing
├── new_kamusalay.csv             # Kamus normalisasi kata alay → baku
├── abusive.csv                   # Daftar kata abusif
│
├── requirements.txt              # Daftar library yang dibutuhkan
└── README.md                     # Dokumentasi proyek
```

---

## ⚙️ Cara Menjalankan

### Prasyarat
Pastikan sudah menginstall **Python 3.10+** dan **pip**.

### 1. Clone Repository
```bash
git clone https://github.com/username/cyberbullying-detector.git
cd cyberbullying-detector
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
```bash
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser pada `http://localhost:8501`

---

## 🧪 Cara Kerja Model

```
Input Komentar
      │
      ▼
┌─────────────────────┐
│   Text Preprocessing │
│  • Case folding      │
│  • Hapus URL & RT    │
│  • Hapus tanda baca  │
│  • Normalisasi alay  │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│   TF-IDF Vectorizer  │
│  • ngram (1,2)       │
│  • min_df = 5        │
│  • max_features=10k  │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│    Model SVM         │
│  • Kernel: Linear    │
│  • Akurasi: 84.81%   │
└─────────────────────┘
      │
      ▼
  Hasil Prediksi
 ✅ Aman / 🚨 Bullying
```

---

## 📊 Performa Model

| Model | Akurasi |
|-------|---------|
| Naive Bayes (baseline) | 83.75% |
| Naive Bayes (optimasi) | 84.17% |
| **SVM Linear (final)** | **84.81%** ✅ |

### Classification Report (Model SVM)

```
              precision    recall  f1-score   support

           0       0.82      0.92      0.87      1514
           1       0.87      0.72      0.79      1120

    accuracy                           0.84      2634
   macro avg       0.85      0.82      0.83      2634
weighted avg       0.84      0.84      0.83      2634
```

---

## 📦 requirements.txt

```
streamlit
scikit-learn
pandas
joblib
```

---

## 👤 Pengembang

**Daffa Daulay**
D3 Teknik Informatika — Universitas Sumatera Utara (USU)
Tugas Mata Kuliah Kecerdasan Buatan · 2025

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik. Dataset Twitter yang digunakan adalah milik peneliti asli dan digunakan hanya untuk tujuan pendidikan.
