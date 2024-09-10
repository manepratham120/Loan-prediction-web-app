import streamlit as st
import pandas as pd 
import pickle as pk

model=pk.load(open('model.pkl','rb'))
scaler=pk.load(open('scaler.pkl','rb'))

st.header("Loan Prediction App")

no_of_dep=st.slider('No.of dependents',0,5)

edu=st.selectbox('choose Education',['Graduated','Not Graduated'])
emp=st.selectbox('self Employed',['Yes','No'])
income=st.slider('choose Annual Income',0,10000000)
amount=st.slider('choose loan amount',0,10000000)
time=st.slider('choose Loan duration',0,20)
cibil=st.slider('choose cibil score',0,1000)
ass=st.slider('choose assests',0,10000000)

if edu=='Graduated':
    edu_s=0
else:
    edu_s=1
    
if emp=='No':
    emp_s=0
else:
    emp_s=1
    
if st.button('Predict'):
    # Creating the input DataFrame with matching feature names
    pred_data = pd.DataFrame([[no_of_dep, edu_s, emp_s, income, amount, time, cibil, ass]], 
                             columns=['no_of_dependents', 'education', 'self_employed', 'income_annum', 'loan_amount', 'loan_term', 'cibil_score', 'Assests'])  # Note: using 'Assests'
    
    # Apply the scaler to standardize the input data
    pred_data_scaled = scaler.transform(pred_data)
    
    # Make prediction
    pred = model.predict(pred_data_scaled)
    
    # Output the result
    if pred[0] == 1:
        st.markdown("Loan approved")
    else:
        st.markdown("Loan Not approved")


        
        