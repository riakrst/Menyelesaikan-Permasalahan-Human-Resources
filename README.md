# Proyek Akhir: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan perusahaan multinasional yang telah beroperasi sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh Indonesia. Meskipun sudah berkembang menjadi perusahaan besar, Jaya Jaya Maju menghadapi tantangan besar dalam hal manajemen sumber daya manusia, khususnya terkait tingginya tingkat attrition atau pengunduran diri karyawan.  

Saat ini, attrition rate perusahaan berada di atas 10%, angka yang cukup tinggi dan berpotensi merugikan perusahaan dalam jangka panjang. Manajer HR ingin memahami lebih dalam faktor-faktor yang berkontribusi terhadap tingginya attrition ini agar dapat menyusun strategi yang lebih tepat untuk mempertahankan karyawan.


## Permasalahan Bisnis

Perusahaan saat ini menghadapi permasalahan berikut:

- **Tingginya angka attrition (lebih dari 10%)** yang mengancam stabilitas dan efektivitas operasional perusahaan.
- **Kurangnya pemahaman berbasis data** mengenai faktor-faktor yang menyebabkan karyawan mengundurkan diri.
- **Belum adanya sistem dashboard** yang dapat membantu HR dalam memantau kondisi karyawan secara visual dan menyeluruh.
- **Tidak tersedia strategi retensi yang terukur dan berbasis bukti** untuk mengurangi tingkat pengunduran diri.

Jika permasalahan ini tidak segera diatasi, perusahaan berisiko:
- Mengalami lonjakan biaya rekrutmen dan pelatihan.
- Kehilangan karyawan potensial dan berpengalaman.
- Menurunnya motivasi kerja serta meningkatnya beban kerja pada karyawan yang tersisa.

## Cakupan Proyek

Proyek ini mencakup serangkaian proses analisis data dan pengembangan solusi yang terdiri dari:

-  **Eksplorasi dan pembersihan data karyawan** untuk memastikan kualitas data yang digunakan.
- **Analisis eksploratif (EDA)** untuk menemukan pola-pola penting yang memengaruhi attrition.
- **Preprocessing data**, termasuk encoding, normalisasi, dan penyeimbangan data (SMOTE).
- **Pembangunan model prediktif** membandingkan algoritma XGBoost dan Random Forest untuk memperkirakan kemungkinan karyawan resign.
- **Pembuatan dashboard** menggunakan Metabase yang menampilkan insight utama dari data attrition.
- **Simulasi prediksi** menggunakan sample data dalam format CSV atau input manual.

---


## Persiapan

## Sumber Data

- **Dataset utama** berasal dari repositori resmi Dicoding:  
  [employee_data.csv (Dicoding GitHub)](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

  > Pada tahap **preprocessing**, baris data dengan nilai `Attrition = null` telah dihapus dari data pelatihan karena tidak memiliki label dan tidak bisa digunakan dalam proses modelling.
  > Namun, data tersebut **tidak dibuang**, melainkan dipindahkan ke file terpisah sebagai **data simulasi untuk prediksi**.

- **Data input manual**:  
  Proses prediksi juga mendukung input data karyawan satu per satu secara manual melalui terminal — cocok untuk memprediksi risiko resign dari karyawan tertentu.

## Sample Input dan Output

 **Input File**

`dataset/sample_input.csv`  
Berisi data karyawan **tanpa kolom `Attrition`** yang sebelumnya didrop dari dataset pelatihan.

 **Output File**

 `sample_output.csv`  
Setelah script `predict.py` dijalankan, hasil prediksi akan disimpan ke file ini.  
Setiap baris akan memiliki kolom tambahan `Attrition_Prediction` yang berisi hasil prediksi:

- `Resign` → jika model memprediksi karyawan akan keluar
- `Bertahan` → jika model memprediksi karyawan akan tetap bekerja

### Setup Environment

Lakukan langkah-langkah berikut untuk menyiapkan environment proyek:

```bash
# 1. Buat virtual environment
python -m venv venv

# 2. Aktifkan environment
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# 3. Install semua dependensi
pip install -r requirements.txt
```
### Menjalankan Prediksi
Setelah semua dependensi terinstal, jalankan script berikut:
```
python predict.py

```

Program akan menampilkan dua opsi:
1. Menggunakan file dataset/sample_input.csv
2. Input data karyawan secara manual melalui terminal

Setelah proses selesai, hasil prediksi akan otomatis disimpan di file sample_output.csv pada direktori utama proyek.
Fitur prediksi pada proyek ini menggunakan model Random Forest yang telah dibandingkan dengan XGBoost, kemudian dibangun dan dievaluasi di file notebook.py sebelum diterapkan dalam script prediksi.

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

Berdasarkan hasil analisis data dan visualisasi yang telah dibuat, terdapat beberapa **faktor kunci yang memengaruhi attrition (pengunduran diri karyawan)** di perusahaan *Jaya Jaya Maju*, antara lain:

- **Lembur (OverTime):** Karyawan yang sering lembur menunjukkan tingkat pengunduran diri yang signifikan lebih tinggi dibandingkan yang tidak lembur.
- **Kepuasan dan keterlibatan kerja:** Attrition lebih banyak terjadi pada karyawan dengan skor rendah pada **Job Satisfaction**, **Environment Satisfaction**, dan **Job Involvement** (khususnya skor ≤ 2).
- **Posisi pekerjaan dan departemen:** Posisi seperti **Sales Executive** dan **Research Scientist**, serta divisi seperti **Sales** dan **Research & Development**, menunjukkan angka resign yang lebih tinggi.
- **Kelompok usia muda dan masa kerja singkat:** Karyawan berusia antara **25–34 tahun** dan dengan **Total Working Years < 10** menjadi kelompok yang paling rentan mengundurkan diri.

### Karakteristik Umum Karyawan yang Resign:
- Usia 25–34 tahun  
- Belum menikah  
- Sering melakukan lembur  
- Bekerja di divisi Sales atau R&D  
- Memiliki skor kepuasan dan keterlibatan kerja rendah  
- Masa kerja relatif singkat (di bawah 10 tahun)
 
Dashboard yang dibangun menggunakan Metabase telah memberikan insight penting seperti:
- **Pemetaan visual kelompok karyawan** dengan risiko resign tinggi.
- **Pemantauan kondisi attrition berdasarkan berbagai dimensi**, seperti jam kerja, kepuasan, jabatan, usia, dan masa kerja.
- **Dukungan pengambilan keputusan berbasis data** bagi manajer HR dalam merancang strategi retensi yang lebih akurat dan terukur.

Temuan ini diharapkan dapat menjadi landasan awal bagi perusahaan untuk **menyusun kebijakan HR yang lebih proaktif** dan berfokus pada kelompok rentan agar dapat **mengurangi angka pengunduran diri di masa mendatang**.

---

## Rekomendasi Action Items

Berdasarkan analisis data dan dashboard, berikut tindakan yang disarankan untuk mengurangi attrition di perusahaan:

### 1. Batasi Lembur
- Maksimal lembur: **6 jam/minggu**.
- Berikan kompensasi atau fleksibilitas waktu kerja.
- Pantau lembur secara berkala melalui dashboard.

### 2. Retensi Karyawan Baru & Usia Muda
- Onboarding intensif selama **3 bulan** pertama.
- Coaching rutin untuk karyawan dengan masa kerja <2 tahun.
- Program mentor bagi karyawan usia <35 tahun.

### 3. Fokus pada Jabatan & Departemen Kritis
- Tinjau beban kerja dan jalur karier di posisi **Sales Executive**, **Research Scientist**, **Sales**, dan **R&D**.
- Tambahkan insentif atau pelatihan khusus untuk posisi tersebut.

### 4. Tingkatkan Kepuasan & Keterlibatan
- Lakukan survei rutin untuk mengukur kepuasan kerja.
- Tindak lanjuti karyawan dengan skor keterlibatan ≤ 2.
- Latih atasan agar lebih responsif terhadap kebutuhan tim.

