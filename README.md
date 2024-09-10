# Loan Prediction App

This is a **Loan Prediction Web App** built using **Streamlit** and **scikit-learn** to predict the approval of a loan based on several input parameters. The model is trained on historical loan data and can predict whether a loan will be approved based on inputs such as number of dependents, education, employment status, income, loan amount, loan duration, CIBIL score, and assets.

## Features

- Input parameters include:
  - Number of dependents
  - Education status (Graduated/Not Graduated)
  - Employment status (Self-employed or not)
  - Annual income
  - Loan amount
  - Loan duration (in years)
  - CIBIL score
  - Total assets

- Outputs:
  - **Loan Approved**: The loan application is likely to be approved based on the provided information.
  - **Loan Not Approved**: The loan application is unlikely to be approved.

## Requirements

To run this project, you will need:

- Python 3.7 or higher
- Required libraries listed in the `requirements.txt` file:
  - `streamlit`
  - `pandas`
  - `scikit-learn`
  - `pickle`

## How to Run the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/loan-prediction-app.git
    cd loan-prediction-app
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Place the model file (`model.pkl`) and the scaler file (`scaler.pkl`) in the root directory of the project.

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

5. Open the app in your browser at the URL provided by Streamlit, typically: `http://localhost:8501`.

## Files

- `app.py`: The main file that contains the Streamlit app code.
- `model.pkl`: Pre-trained machine learning model for loan prediction.
- `scaler.pkl`: Scaler object for standardizing input data before making predictions.
- `requirements.txt`: A list of required libraries to run the app.

## Model

- The machine learning model is trained using a classification algorithm to predict loan approval.
- The data is scaled using a standard scaler to ensure all inputs are on a similar scale.

## How It Works

1. **Input Fields**: The user inputs information such as the number of dependents, education level, employment status, annual income, loan amount, loan term, CIBIL score, and assets.
   
2. **Model Prediction**: The input data is first standardized using the saved scaler and then fed into the pre-trained loan prediction model.

3. **Output**: The model predicts whether the loan will be approved (Loan Approved) or not (Loan Not Approved).





## Acknowledgments

- This project was built using **Streamlit**, an open-source Python framework for creating web apps for machine learning and data science.
  
Feel free to raise issues or contribute to the project by submitting a pull request!
