# COBEK (Cek Obesitas Kamu) — Web-Based Obesity Classification & Health Risk Analysis

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

**COBEK (Cek Obesitas)** adalah aplikasi berbasis web yang menggabungkan algoritma **Machine Learning (Decision Tree & Random Forest)** dengan panduan medis Body Mass Index (BMI) untuk memprediksi kategori berat badan dan risiko obesitas seseorang secara instan dan akurat.

---
<img width="1280" height="720" alt="cobek" src="https://github.com/user-attachments/assets/0481dc31-60a2-4604-8523-c202de4bd735" />


## 📌 Fitur Utama

- **Machine Learning Classification**: Menggunakan model **Random Forest Classifier** dan **Decision Tree** untuk klasifikasi kategori berat badan.
- **Medical Rule-Based Guardrail**: Dilengkapi validasi berbasis ambang batas BMI medis (Underweight, Normal, Overweight, Obesity Type I, II, & III) untuk menjamin akurasi dan konsistensi medis.
- **RESTful API**: Backend berbasis Flask yang ringan, cepat, dan siap diintegrasikan.
- **Interactive & Responsive UI**: Antarmuka modern berbasis Bootstrap 5 dengan visualisasi kartu status tubuh, kalkulasi BMI otomatis, dan rekomendasi gaya hidup yang dipersonalisasi.

---

## 🛠️ Tech Stack & Arsitektur

### 1. Machine Learning & Backend
- **Language**: Python 3.x
- **Framework**: Flask, Flask-CORS
- **Server/WSGI**: Gunicorn
- **Libraries**:
  - `scikit-learn`: Pelatihan dan inferensi model Decision Tree & Random Forest.
  - `pandas`: Data preprocessing dan penataan fitur input.
  - `joblib`: Serialisasi dan pemuatan model (`.pkl`).

### 2. Frontend
- **Languages**: HTML5, CSS3, Vanilla JavaScript (ES6+ Fetch API)
- **UI Framework**: Bootstrap 5, Bootstrap Icons
- **Typography & Assets**: Google Fonts (Poppins), Custom Vector Illustrations

---

## 🗂️ Struktur Direktori

```text
COBEK v2/
│
├── cobek-backend/
│   ├── app.py                # Server Flask & endpoint /predict
│   ├── decision_tree.pkl     # Model Decision Tree terlatih
│   ├── random_forest.pkl     # Model Random Forest terlatih
│   ├── label_gender.pkl      # Encoder label gender
│   ├── label_output.pkl      # Encoder label output klasifikasi
│   └── requirements.txt      # Dependensi Python
│
├── cobek-frontend/
│   ├── index.html            # Antarmuka web utama
│   ├── asset/                # Aset gambar, ikon, dan font
│   ├── css/                  # Styling kustom & Bootstrap
│   └── js/                   # Skrip JavaScript & Bootstrap bundle
│
├── .gitignore
└── README.md
```

---

## 🚀 Cara Menjalankan Projek Secara Lokal

### 1. Backend (Flask)
```bash
# Masuk ke direktori backend
cd cobek-backend

# Buat virtual environment (opsional namun disarankan)
python -m venv venv
# Windows:
venv\Scripts\activate

# Install dependensi
pip install -r requirements.txt

# Jalankan server
python app.py
```
Backend akan berjalan di `http://127.0.0.1:5000/`.

### 2. Frontend
Cukup buka berkas `cobek-frontend/index.html` langsung di browser atau gunakan ekstensi seperti **Live Server** di VS Code.

> **Catatan Endpoint API**: Pastikan URL endpoint di `cobek-frontend/index.html` (`mulaiPrediksi()`) mengarah ke server lokal (`http://127.0.0.1:5000/predict`) atau URL cloud deployment Anda.

---

## 🧑‍💻 Author
- **Alfananda Devin Yuwono** - [@PinPin27](https://github.com/PinPin27)
