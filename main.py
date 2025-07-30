import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="🎓 School Admission Form", page_icon="📋")
st.title("🎓 School Admission Form")

# Path to Excel file
EXCEL_FILE = "admissions.xlsx"

# Define form
with st.form("admission_form"):
    student_name = st.text_input("Student Name")
    father_name = st.text_input("Father's Name")
    student_class = st.selectbox("Class", ["ECE", "I", "II", "III", "IV", "V"])
    age = st.number_input("Age", min_value=3, max_value=15, step=1)
    gender = st.radio("Gender", ["Male", "Female"])
    submitted = st.form_submit_button("Submit")

# When form is submitted
if submitted:
    new_entry = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Student Name": student_name,
        "Father's Name": father_name,
        "Class": student_class,
        "Age": age,
        "Gender": gender
    }

    # Load or create DataFrame
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    else:
        df = pd.DataFrame([new_entry])

    # Save to Excel
    df.to_excel(EXCEL_FILE, index=False)

    st.success("✅ Admission saved to Excel!")
    st.dataframe(df.tail(1))  # Show last entry
