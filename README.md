# Proyek Akhir: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan perusahaan multinasional yang telah beroperasi sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh Indonesia. Meskipun sudah berkembang menjadi perusahaan besar, Jaya Jaya Maju menghadapi tantangan besar dalam hal manajemen sumber daya manusia, khususnya terkait tingginya tingkat attrition atau pengunduran diri karyawan.  

Saat ini, attrition rate perusahaan berada di atas 10%, angka yang cukup tinggi dan berpotensi merugikan perusahaan dalam jangka panjang. Manajer HR ingin memahami lebih dalam faktor-faktor yang berkontribusi terhadap tingginya attrition ini agar dapat menyusun strategi yang lebih tepat untuk mempertahankan karyawan.

---

## Permasalahan Bisnis

Permasalahan utama yang dihadapi perusahaan dan menjadi fokus proyek ini adalah:

- **Mengidentifikasi faktor-faktor utama yang berkontribusi terhadap tingginya attrition rate.**
- **Menyediakan insight visual melalui dashboard agar manajer HR dapat memonitor dan memahami kondisi karyawan dengan lebih baik.**

---

## Cakupan Proyek

Cakupan proyek ini mencakup:

1. Menjalankan seluruh proses data science dari tahap Business Understanding hingga Deployment secara lokal.
2. Melakukan eksplorasi dan analisis data untuk menemukan pola dan hubungan antara berbagai variabel terhadap attrition.
3. (Jika memungkinkan dan dibutuhkan) Membangun model machine learning untuk memprediksi kemungkinan seorang karyawan akan keluar dari perusahaan.
4. Membangun minimal satu **business dashboard** yang menampilkan insight terkait faktor-faktor utama yang berkontribusi terhadap attrition.

---


## Persiapan

**Sumber data**: 
- Input: `dataset/sample_input.csv`  
  File CSV berisi data karyawan yang ingin diprediksi (contoh: 2 baris data).
- Output: `sample_output.csv`  
  File hasil prediksi yang akan dihasilkan setelah menjalankan skrip.

**Setup environment**:
```
# 1. Buat virtual environment
python -m venv venv

# 2. Aktifkan environment
# Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

# 3. Install dependensi
pip install -r requirements.txt
```

**Menjalankan Prediksi**

Setelah lingkungan siap, jalankan perintah berikut untuk memproses prediksi:
```
python predict.py
```

**Hasil prediksi** akan disimpan dalam file `sample_output.csv`.

Setiap baris data akan memiliki kolom tambahan bernama Attrition_Prediction yang berisi hasil prediksi:
- Resign: jika model memprediksi karyawan akan keluar
- Bertahan: jika model memprediksi karyawan akan tetap bekerja

File sample_output.csv dapat ditemukan pada direktori utama proyek setelah menjalankan script predict.py.

---

## Business Dashboard

Untuk menjawab tantangan tingginya *attrition rate* di perusahaan **Jaya Jaya Maju**, telah dibangun sebuah **business dashboard** menggunakan **Metabase**.

### Akses Dashboard

- **Platform:** Metabase
- **URL Lokal:** `http://localhost:3001`
- **Email Login:** `root@mail.com`
- **Password:** `root123`
- **Screenshot:** folder `riakrst-dashboard` (terlampir)
- **Dashboard File:** `metabase.db.mv.db` (disertakan)

---

## Insight dari Visualisasi Dashboard

Dashboard dibangun berdasarkan fitur-fitur terpenting yang memengaruhi keputusan karyawan untuk mengundurkan diri. Berikut insight dari masing-masing visualisasi:
- **Summary:**
  ![image](https://github.com/user-attachments/assets/ff6d8127-e846-4445-8975-7cf1ff2402fa)

- **OverTime:** Karyawan yang lembur lebih sering resign → lembur adalah faktor utama attrition.
  ![image](https://github.com/user-attachments/assets/4396ade5-82a0-40e1-9555-4e925db1c696)

- **Department:** R&D dan Sales menyumbang attrition tertinggi → perlu perhatian khusus.
  ![image](https://github.com/user-attachments/assets/c616c413-aba7-4c1a-9589-01ef848bfb7c)

- **Marital Status:** Karyawan single paling banyak resign → lebih mobile, kurang terikat.
  ![image](https://github.com/user-attachments/assets/f2af2ae0-1172-4d93-be8b-94c3d6ebdb0f)

- **Job Role:** Sales Executive, Lab Technician, dan Research Scientist paling rentan keluar.
  ![image](https://github.com/user-attachments/assets/4aaf3495-dff1-4fb5-89fe-f844f117860f)

- **Age Group:** Usia 25–34 paling banyak resign → targetkan program retensi usia muda.
  ![image](https://github.com/user-attachments/assets/50606d79-7379-4ec3-987a-72cc720c1df6)

- **Satisfaction & Engagement:** Nilai rendah = risiko resign tinggi → tingkatkan kepuasan kerja.
  ![image](https://github.com/user-attachments/assets/714df23c-acdd-487d-817a-da16b1903375)
 
- **Work-Life Balance:** Perlu validasi ulang, karena hasil tidak sesuai ekspektasi.
  ![image](https://github.com/user-attachments/assets/4139d8ff-c337-44c0-9fdd-c12e8473df67)

- **Working Years:** Resign paling tinggi pada 0–10 tahun kerja → butuh program onboarding & pengembangan awal karier.
  ![image](https://github.com/user-attachments/assets/4c868909-59e6-4073-b0a3-3d89f02aa2bd)


---

## Conclusion

Proyek ini berhasil mengidentifikasi dan memvisualisasikan faktor-faktor utama yang menyebabkan tingginya tingkat attrition di perusahaan **Jaya Jaya Maju**, yaitu:

- Beban kerja berlebih (lembur)
- Kepuasan dan keterlibatan kerja yang rendah
- Jabatan dan departemen tertentu (Sales, R&D)
- Kelompok usia muda (25–34 tahun)
- Masa kerja awal (0–10 tahun)

Dengan membangun dashboard, manajer HR kini dapat memantau kondisi karyawan secara real-time dan memahami pola resign berdasarkan data aktual. Ini menjawab kebutuhan utama perusahaan untuk **memahami akar masalah attrition** dan **menyusun strategi retensi yang lebih tepat**.

---

## Rekomendasi Action Items 

Berikut adalah dua rekomendasi tindakan yang dapat diambil perusahaan untuk mengurangi tingkat pengunduran diri:

### Action Item 1: Evaluasi dan Batasi Jam Lembur
Lakukan evaluasi terhadap kebijakan lembur dan pastikan lembur hanya dilakukan jika sangat dibutuhkan. Perkenalkan program kompensasi atau fleksibilitas sebagai pengganti lembur berlebih.

### Action Item 2: Program Retensi untuk Karyawan Baru & Jabatan Kritis
Terapkan program onboarding yang kuat, mentorship, serta jalur karier yang jelas untuk karyawan baru dan mereka yang berada di posisi dengan tingkat resign tinggi seperti Sales Executive dan Research Scientist.

---
