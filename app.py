from flask import Flask, render_template, request
import pickle
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load model and encoders
model = pickle.load(open('churn_model.pkl', 'rb'))
label_encoders = pickle.load(open('label_encoders.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form data
        gender = request.form['gender']
        senior_citizen = int(request.form['senior_citizen'])
        partner = request.form['partner']
        dependents = request.form['dependents']
        tenure = float(request.form['tenure'])
        monthly_charges = float(request.form['monthly_charges'])
        total_charges = float(request.form['total_charges'])

        # Create dataframe
        input_data = pd.DataFrame({
            'gender': [gender],
            'SeniorCitizen': [senior_citizen],
            'Partner': [partner],
            'Dependents': [dependents],
            'tenure': [tenure],
            'MonthlyCharges': [monthly_charges],
            'TotalCharges': [total_charges]
        })

        # Apply label encoding only to categorical columns
        for col, le in label_encoders.items():
            if col in input_data.columns and input_data[col].dtype == 'object':
                input_data[col] = le.transform(input_data[col])

        # Make prediction
        prediction = model.predict(input_data)[0]
        result = "Customer is likely to Churn 😞" if prediction == 1 else "Customer is likely to Stay 😊"

        # Return result to HTML
        return render_template('index.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction=f"Error during prediction: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)


