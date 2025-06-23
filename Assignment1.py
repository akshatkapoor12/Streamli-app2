import pandas as pd
import streamlit as st
data = { 
"Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"], 
"Age": [24, 27, 22, 32, 29, 41, 35], 
"Gender": ["F", "M", "M", "M", "F", "M", "F"], 
"Department": ["HR", "IT", "Finance", "IT", "HR", "Finance", "IT"], 
"Salary": [45000, 54000, 50000, 62000, 48000, 70000, 60000], 
"Experience": [2, 4, 3, 6, 5, 10, 7] 
} 
df = pd.DataFrame(data) 
df.to_csv("employee_data.csv", index=False)


data=pd.read_csv("employee_data.csv")
#print(data)


#to print first 5 rows of the data
#print(data.head())

#to print last 5 rows of the data

#print(data.tail())

#to print column names
#print(data.columns)

#to print data types of each columns

#print(data.dtypes)

#group data by departement to find average salary and experience

g_data= data.groupby("Department").agg({"Salary": "mean", "Experience": "mean"}).reset_index()

print(g_data)

#to filter data for employees with salary greater than 50000

high_salary = data[data["Salary"] > 50000]

#print(high_salary)

#to filter data for employees with experience less than 5 years

l_experience = data[data["Experience"] < 5]

#print(l_experience)

#to create a streamlit app with title and description 

st.title("Employee Data Analysis")
st.write("This application analyzes employee data ")

#to add description and title 

st.subheader("Employee Data Overview")
st.write("This section provides an overview of the employee data including basic statistics.")
#to display the dataframe in app
st.dataframe(data)

#to display filtered data as a table
st.subheader("Employees with Salary Greater than 50000")
st.dataframe(high_salary)

st.subheader("Employees with Experience Less than 5 Years")
st.dataframe(l_experience)


#to display bar charts of filtered data by departement
st.subheader("Average Salary and Experience by Department")
st.bar_chart(g_data.set_index("Department"))

# to add a button for downloading the filetred  data
st.subheader("Download Filtered Data")
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Filtered Data",
    data=convert_df(high_salary),
    file_name='high_salary_employees.csv',
    mime='text/csv',
)

