import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in = open("RCF1.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"
	

def predict_claim_authentication(Age,Gender,Days_spend_hsptl,Admission_type,Home_or_self care,ccs_diagnosis_code,ccs_procedure_code,Code_illness,Mortality_risk,Surg_Description,Emergency_dept_yes/No,Tot_charg,Tot_cost,ratio_of_total_costs_to_total_charges,Payment_Typology):
    
    """Let's Authenticate the Claims 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Age
        in: query
        type: number
        required: true
      - name: Gender
        in: query
        type: number
        required: true
      - name: Days_spend_hsptl
        in: query
        type: number
        required: true
      - name: Admission_type
        in: query
        type: number
        required: true
	  - name: Home_or_self care
        in: query
        type: number
        required: true
	  - name: ccs_diagnosis_code
        in: query
        type: number
        required: true
	  - name: ccs_procedure_code
        in: query
        type: number
        required: true	
	  - name: Code_illness
        in: query
        type: number
        required: true
	  - name: Mortality_risk
        in: query
        type: number
        required: true
	  - name: Surg_Description
        in: query
        type: number
        required: true
	  - name: Emergency_dept_yes/No
        in: query
        type: number
        required: true
	  - name: Tot_cost
        in: query
        type: number
        required: true
	  - name: Tot_charg
        in: query
        type: number
        required: true
	  - name: ratio_of_total_costs_to_total_charges
        in: query
        type: number
        required: true	
	  - name: Payment_Typology
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=RCF1.predict([[Age,Gender,Days_spend_hsptl,Admission_type,Home_or_self care,ccs_diagnosis_code,ccs_procedure_code,Code_illness,Mortality_risk,Surg_Description,Emergency dept_yes/No,Tot_charg,Tot_cost,ratio_of_total_costs_to_total_charges,Payment_Typology]])
    print(prediction)
    return prediction


def main():
    st.title("Claim Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Health Insurance Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
	
	
	Age = st.text_input("Age","Type Here")
	Gender = st.text_input("Gender","Type Here")
	Days_spend_hsptl = st.text_input("Days_spend_hsptl","Type Here")
	Admission_type = st.text_input("Admission_type","Type Here")
	Home_or_self care = st.text_input("Home or self care","Type Here")
	ccs_diagnosis_code = st.text_input("ccs_diagnosis_code","Type Here")
	ccs_procedure_code = st.text_input("ccs_procedure_code","Type Here")
	Code_illness = st.text_input("Code_illness","Type Here")
	Mortality risk = st.text_input("Mortality_risk","Type Here")
	Surg_Description = st.text_input("Surg_Description","Type Here")
	Emergency_dept_yes/No = st.text_input("Emergency_dept_yes/No","Type Here")
	Tot_charg = st.text_input("Tot_charg","Type Here")
	Tot_cost = st.text_input("Tot_cost","Type Here")
	Payment_Typology = st.text_input("Payment_Typology","Type Here")
	
	
    result=""
    if st.button("Predict"):
        result=predict_claim_authentication(Age,Gender,Days_spend_hsptl,Admission_type,Home_or_self care,ccs_diagnosis_code,ccs_procedure_code,Code_illness,Mortality_risk,Surg_Description,Emergency dept_yes/No,Tot_charg,Tot_cost,(Tot_cost/Tot_charg),Payment_Typology)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    