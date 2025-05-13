import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Initialize session state for student data if not already initialized
if 'students' not in st.session_state:
    st.session_state.students = []

# Sidebar Navigation
st.sidebar.title("Student Portal")
st.text("A Project by Kshama R - 1DA21EC074")
page = st.sidebar.radio("Go to", ["Add Student", "Student List", "Project Info"])

# Page 1: Add Student
if page == "Add Student":
    st.title("Student Registration")
    
    with st.form("student_form"):
        name = st.text_input("Name")
        student_id = st.text_input("Student ID")
        attendance = st.slider("Attendance (%)", 0, 100, 75)
        marks = st.number_input("Marks (out of 100)", 0, 100, 50)
        submit = st.form_submit_button("Add Student")

        if submit:
            st.session_state.students.append({
                'name': name,
                'student_id': student_id,
                'attendance': attendance,
                'marks': marks,
                'performance': np.random.choice(['Excellent', 'Good', 'Average', 'Poor'])
            })
            st.success("Student added successfully!")

# Page 2: Student List & Details
elif page == "Student List":
    st.title("Student List")

    # Pseudo Data (if no entries, load demo)
    if not st.session_state.students:
        st.session_state.students = [
            {'name': 'Alice', 'student_id': 'S001', 'attendance': 90, 'marks': 85, 'performance': 'Excellent'},
            {'name': 'Bob', 'student_id': 'S002', 'attendance': 70, 'marks': 65, 'performance': 'Average'},
            {'name': 'Charlie', 'student_id': 'S003', 'attendance': 80, 'marks': 75, 'performance': 'Good'},
        ]

    df = pd.DataFrame(st.session_state.students)
    selected_student = st.selectbox("Select a student", df['name'])

    student_data = df[df['name'] == selected_student].iloc[0]
    st.subheader(f"Details for {student_data['name']}")
    st.write(f"**Student ID**: {student_data['student_id']}")
    st.write(f"**Attendance**: {student_data['attendance']}%")
    st.write(f"**Marks**: {student_data['marks']}")
    st.write(f"**Performance**: {student_data['performance']}")

    # Performance Graphs
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    # Attendance Pie Chart
    ax[0].pie([student_data['attendance'], 100 - student_data['attendance']], labels=['Present', 'Absent'], autopct='%1.1f%%')
    ax[0].set_title("Attendance")

    # Marks Bar Chart
    ax[1].bar(['Marks'], [student_data['marks']], color='skyblue')
    ax[1].set_ylim(0, 100)
    ax[1].set_title("Marks")

    st.pyplot(fig)

# Page 3: Project Info
elif page == "Project Info":
    st.title("Project Implementation Details")
    
    st.markdown("""
    ### Streamlit Student Portal

    This project demonstrates a multi-page Streamlit application that functions as a student portal.

    **Page 1: Add Student**
    - Collects student details like name, student ID, attendance, and marks.
    - Data is stored in session state.

    **Page 2: Student List**
    - Displays a list of all registered students (with fallback demo data).
    - Selecting a student shows their details and visualizations (attendance pie chart and marks bar graph).

    **Page 3: Project Info**
    - Describes how the project was built and technologies used.

    **Technologies**
    - [Streamlit](https://streamlit.io): Python library for web apps.
    - [Matplotlib](https://matplotlib.org/): For visualizations.
    - [Pandas](https://pandas.pydata.org/): For data management.

    **Future Enhancements**
    - Integration with a database.
    - Authentication and user roles.
    - Exporting reports.
    """)
