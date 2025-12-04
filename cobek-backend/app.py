from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# LOAD MODEL
dt = joblib.load("decision_tree.pkl")
rf = joblib.load("random_forest.pkl")
label_gender = joblib.load("label_gender.pkl")
label_output = joblib.load("label_output.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    age = int(data["age"])
    gender = data["gender"]
    height = float(data["height"])
    weight = float(data["weight"])

    # 1. Encode Gender & Hitung BMI
    gender_code = label_gender.transform([gender])[0]
    bmi = weight / ((height/100)**2)

    # 2. Siapkan Dataframe
    df = pd.DataFrame([[age, gender_code, height, weight, bmi]],
                      columns=["Age", "Gender", "Height", "Weight", "BMI"])

    # 3. Prediksi Murni dari AI
    pred_dt_raw = label_output.inverse_transform(dt.predict(df))[0]
    pred_rf_raw = label_output.inverse_transform(rf.predict(df))[0]

    # 4. === LOGIKA SATPAM DETAIL (Type I, II, III Balik Lagi) ===
    
    final_result = pred_rf_raw # Default pakai hasil AI

    # KOREKSI PAKSA BERDASARKAN BMI (Biar Akurat Secara Medis)
    # Kita kembalikan label detailnya di sini
    if bmi >= 40:
        final_result = "Obesity Type III" 
    elif bmi >= 35 and "Obesity" not in final_result:
        final_result = "Obesity Type II"
    elif bmi >= 30 and "Obesity" not in final_result:
        final_result = "Obesity Type I"
    elif bmi < 18.5:
        final_result = "Under Weight"

    return jsonify({
        "BMI": round(bmi, 2),
        "DecisionTree": pred_dt_raw,
        "RandomForest": final_result  # Output: "Obesity Type III", "Overweight", dll
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)