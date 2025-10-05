# Customer_Churn_Flask_App
A Machine Learning web application built using Flask that predicts customer churn based on telecom user data. The project includes data preprocessing, model training using XGBoost, and deployment of an interactive Flask web interface for live predictions.
# 🧮 Customer Churn Prediction Flask App 
# 📊 Customer Churn Prediction Web App (Flask + Machine Learning)

An interactive **Flask web application** that predicts whether a telecom customer is likely to **churn (leave the service)** based on customer demographics, account information, and service usage data.

This project demonstrates a **complete end-to-end machine learning workflow** — from **data preprocessing and model training** in Jupyter Notebook to **model deployment** using Flask.

---

## 🧠 Key Features

- 🧩 **End-to-End ML Workflow** — Covers preprocessing, model training, evaluation, and deployment.
- ⚙️ **Flask Web App** — Simple web interface for real-time predictions.
- 📦 **Pre-Trained Model** — XGBoost model trained on the Telco Customer Churn dataset.
- 💾 **Persistent Encoders** — Label encoders stored as `.pkl` for consistent data handling.
- 🌐 **User-Friendly Interface** — HTML form for inputs and clear prediction output.

---

## 📁 Project Structure
Customer_Churn_Flask_App/
│
├── app.py # Main Flask app
├── churn_model.pkl # Trained XGBoost model
├── label_encoders.pkl # Saved label encoders
├── requirements.txt # Project dependencies
├── templates/
│ └── index.html # Frontend HTML page
├── static/ # (Optional) CSS / JS files
├── Churn_model_training.ipynb # Jupyter notebook for training
└── WA_Fn-UseC_-Telco-Customer-Churn.csv # Dataset 

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS (Flask Templates) |
| **Backend** | Flask (Python) |
| **Modeling** | XGBoost, Scikit-learn, Pandas, NumPy |
| **Deployment** | Flask (local) / Render / Heroku |

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/warrior678/Customer_Churn_Flask_App.git
   cd Customer_Churn_Flask_App
   pip install -r requirements.txt
  python app.py
http://127.0.0.1:5000/
📈 Model Training (Overview)

Dataset: Telco Customer Churn (IBM)

Process:

Data cleaning and missing value handling

Label encoding of categorical variables

Feature engineering and splitting (Train/Test)

Model training with XGBoost Classifier

Model and encoder serialization using pickle 
🧪 Example Prediction
Input	Prediction
Gender: Female, Contract: Month-to-month, Tenure: 3 months, InternetService: Fiber optic	❌ Customer will churn
Gender: Male, Contract: Two year, Tenure: 50 months, InternetService: DSL	✅ Customer will not churn 

churn
🧰 Future Enhancements

Add SHAP/LIME explainability for model transparency

Expose REST API endpoint for programmatic access

Deploy using Render / AWS / GCP / Azure

Add Dockerfile for containerized deployment

Integrate input validation, logging, and error handling





---

## 🚀 Features
- Interactive Flask-based web app for real-time predictions  
- Machine Learning model trained using **XGBoost**  
- Label encoding for categorical variables  
- Pickle-based model loading for deployment  
- Responsive front-end built with HTML + CSS
-  <img width="1111" height="560" alt="image" src="https://github.com/user-attachments/assets/7efc8722-099e-42a7-b88e-a98cd09924e1" />


---

## 🧠 Tech Stack
- **Python 3.x**  
- **Flask**  
- **Pandas, NumPy, XGBoost, Scikit-learn**  
- **HTML, CSS, Bootstrap**
- ## 📓 Model Training
The model used in this app was trained in the Jupyter Notebook:

  

---

## 🧩 How It Works
1. Data is preprocessed and categorical variables are encoded.  
2. The trained XGBoost model predicts customer churn.  
3. Flask renders the web page and returns prediction results instantly.

---

## 🖥️ Run Locally
```bash
# Step 1: Clone this repository
git clone https://github.com/yourusername/Customer_Churn_Flask_App.git

# Step 2: Go to project directory
cd Customer_Churn_Flask_App
<img width="1112" height="568" alt="image" src="https://github.com/user-attachments/assets/1ec11f88-e24f-45e1-9e63-a40eef29606a" />


# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the app
python app.py

