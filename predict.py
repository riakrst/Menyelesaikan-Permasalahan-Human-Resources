import pandas as pd
import joblib

# Load model, scaler, dan fitur yang digunakan saat training
model = joblib.load('model/random_forest_model.pkl')
scaler = joblib.load('model/scaler.pkl')
feature_columns = joblib.load('model/feature_columns.pkl')

# Load data dummy
df = pd.read_csv('dataset/sample_input.csv')

# Encode data (One-Hot)
df_encoded = pd.get_dummies(df)

# Pastikan semua fitur sesuai
for col in feature_columns:
    if col not in df_encoded.columns:
        df_encoded[col] = 0
df_encoded = df_encoded[feature_columns]

# Standardisasi
df_scaled = scaler.transform(df_encoded)

# Prediksi
y_pred = model.predict(df_scaled)

# Tambahkan ke hasil
df['Attrition_Prediction'] = y_pred
df['Attrition_Prediction'] = df['Attrition_Prediction'].map({0: 'Bertahan', 1: 'Resign'})

# Simpan hasil
df.to_csv('sample_output.csv', index=False)
print("Prediksi selesai. Hasil disimpan ke sample_output.csv")
