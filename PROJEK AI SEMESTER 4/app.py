import streamlit as st
import joblib
import re
import pandas as pd

# Konfigurasi Halaman Web
st.set_page_config(page_title="Cyberbullying Detection", page_icon="🛡️")

# 1. Memuat kamus alay agar fungsi pembersihan berjalan lancar di web
@st.cache_data
def load_kamus():
    df_alay = pd.read_csv('new_kamusalay.csv', encoding='latin-1', header=None, names=['alay', 'formal'])
    return dict(zip(df_alay['alay'], df_alay['formal']))

kamus_alay_dict = load_kamus()

# 2. Fungsi pembersihan teks (Sama persis seperti di Jupyter Notebook)
def bersihkan_teks(text):
    text = str(text).lower()
    text = re.sub(r'rt\s+|user\s+', '', text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    kata_kata = text.split()
    kata_baku = [kamus_alay_dict.get(kata, kata) for kata in kata_kata]
    return ' '.join(kata_baku)

# 3. Memuat Model SVM dan Pembobot TF-IDF yang sudah kamu awetkan
@st.cache_resource
def load_models():
    model = joblib.load('model_svm_cyberbullying.joblib')
    vectorizer = joblib.load('tfidf_vectorizer.joblib')
    return model, vectorizer

model_svm, tfidf_optimized = load_models()

# --- TAMPILAN ANTARMUKA WEB ---

st.title("🛡️ Smart Cyberbullying Detection System")
st.write("Sistem cerdas berbasis Machine Learning untuk mendeteksi perundungan siber pada komentar media sosial.")
st.markdown("---")

# Kotak input untuk mengetik kalimat
teks_input = st.text_area("Masukkan komentar yang ingin diuji:", height=150, placeholder="Ketik komentar di sini...")

# Tombol untuk menjalankan prediksi
if st.button("Deteksi Komentar", type="primary"):
    if teks_input.strip() != "":
        with st.spinner('Model sedang menganalisis kalimat...'):
            # Bersihkan teks dan ubah ke angka
            teks_bersih = bersihkan_teks(teks_input)
            vektor_teks = tfidf_optimized.transform([teks_bersih])
            
            # Lakukan prediksi
            prediksi = model_svm.predict(vektor_teks)[0]
            
            # Tampilkan hasil
            st.markdown("### Hasil Analisis:")
            if prediksi == 1:
                st.error("🔴 **Peringatan:** Komentar ini terdeteksi mengandung unsur **CYBERBULLYING / Ujaran Kebencian!**")
            else:
                st.success("🟢 **Aman:** Komentar ini tidak mengandung unsur Cyberbullying.")
    else:
        st.warning("⚠️ Silakan masukkan teks terlebih dahulu!")

# Footer bagian bawah halaman
st.markdown("---")
st.caption("Dikembangkan oleh Daffa Daulay - D3 Teknik Informatika USU | Tugas Kecerdasan Buatan")