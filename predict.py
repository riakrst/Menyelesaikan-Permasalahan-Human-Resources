import pandas as pd
import joblib
import os

def load_model():
    model = joblib.load('model/random_forest_model.pkl')
    scaler = joblib.load('model/scaler.pkl')
    feature_columns = joblib.load('model/feature_columns.pkl')
    return model, scaler, feature_columns

def prepare_data(df, feature_columns, scaler):
    # One-hot encoding
    df_encoded = pd.get_dummies(df)

    # Pastikan semua fitur sesuai dengan saat training
    for col in feature_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[feature_columns]

    # Scaling
    df_scaled = scaler.transform(df_encoded)
    return df_scaled

def predict_and_save(df, df_scaled, model):
    y_pred = model.predict(df_scaled)
    df['Attrition_Prediction'] = y_pred
    df['Attrition_Prediction'] = df['Attrition_Prediction'].map({0: 'Bertahan', 1: 'Resign'})

    # Simpan hasil ke CSV
    df.to_csv('sample_output.csv', index=False)

    # Cetak hasil prediksi ke terminal
    print("\n Prediksi selesai. Hasil disimpan ke sample_output.csv")
    print("\n Hasil Prediksi:")
    print(df[['Attrition_Prediction']])

def manual_input():
    print(" Input data manual:")
    data = {}

    # Numerik dan kategorikal
    data['Age'] = int(input("Age: "))
    data['BusinessTravel'] = input("Business Travel (Travel_Rarely, Travel_Frequently, Non-Travel): ")
    data['DailyRate'] = int(input("Daily Rate: "))
    data['Department'] = input("Department (Sales, Research & Development, Human Resources): ")
    data['DistanceFromHome'] = int(input("Distance From Home (in km): "))
    data['Education'] = int(input("Education (1-Below College, 2-College, 3-Bachelor, 4-Master,5-Doctor): "))
    data['EducationField'] = input("Education Field (Life Sciences, Medical, Marketing, Technical Degree, Human Resources, Other.): ")
    data['EnvironmentSatisfaction'] = int(input("Environment Satisfaction (1-Low to 4-Very High): "))
    # kolom jumlah karyawan, setiap baris mewakili satu karyawan. Karena dalam model kolom ini diikutsertakan, maka pada input manual diberi nilai default 1 
    data['EmployeeCount'] = 1
    data['Gender'] = input("Gender (Male/Female): ")
    data['HourlyRate'] = int(input("Hourly Rate: "))
    data['JobInvolvement'] = int(input("Job Involvement (1-Low to 4-Very High): "))
    data['JobLevel'] = int(input("Job Level (1 to 5): "))
    data['JobRole'] = input("Job Role (e.g. Human Resources, Healthcare Representative, Research Scientist, Sales Executive, Manager Laboratory Technician, Research Director, Manufacturing Director, Sales Representative): ")
    data['JobSatisfaction'] = int(input("Job Satisfaction (1-Low to 4-Very High): "))
    data['MaritalStatus'] = input("Marital Status (Single, Married, Divorced): ")
    data['MonthlyIncome'] = int(input("Monthly Income: "))
    data['MonthlyRate'] = int(input("Monthly Rate: "))
    data['NumCompaniesWorked'] = int(input("Number of Companies Worked: "))
    data['Over18'] = input("Over 18 (Y/N): ")
    data['OverTime'] = input("OverTime (Yes/No): ")
    data['PercentSalaryHike'] = int(input("Percent Salary Hike: "))
    data['PerformanceRating'] = int(input("Performance Rating (1 to 4): "))
    data['RelationshipSatisfaction'] = int(input("Relationship Satisfaction (1 to 4): "))
    data['StandardHours'] = int(input("Standard Hours: "))
    data['StockOptionLevel'] = int(input("Stock Option Level: "))
    data['TotalWorkingYears'] = int(input("Total Working Years: "))
    data['TrainingTimesLastYear'] = int(input("Training Times Last Year: "))
    data['WorkLifeBalance'] = int(input("WorkLife Balance (1 to 4): "))
    data['YearsAtCompany'] = int(input("Years At Company: "))
    data['YearsInCurrentRole'] = int(input("Years In Current Role: "))
    data['YearsSinceLastPromotion'] = int(input("Years Since Last Promotion: "))
    data['YearsWithCurrManager'] = int(input("Years With Current Manager: "))

    return pd.DataFrame([data])

def main():
    print("=== ATTRITION PREDICTOR ===")
    print("1. Gunakan file dataset/sample_input.csv")
    print("2. Input data manual")
    choice = input("Pilih opsi (1/2): ")

    model, scaler, feature_columns = load_model()

    if choice == '1':
        if not os.path.exists('dataset/sample_input.csv'):
            print("File sample_input.csv tidak ditemukan di folder dataset/")
            return
        df = pd.read_csv('dataset/sample_input.csv')
    elif choice == '2':
        df = manual_input()
    else:
        print("Pilihan tidak valid.")
        return

    df_scaled = prepare_data(df, feature_columns, scaler)
    predict_and_save(df, df_scaled, model)

if __name__ == '__main__':
    main()
