import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Eman Mohammad Faris– Biomedical Engineer & AI Developer Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE ---
st.markdown("""
    <style>
    .stTabs [role="tab"] {
        font-size: 18px;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color:#4CAF50;'>Eman Mohammad Faris– Biomedical Engineer & AI Developer</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color:#555555;'>Developing AI Solutions for Healthcare and Education</h3>", unsafe_allow_html=True)

# Tabs with emojis
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "👩‍💻 About Me",
    "🎯 My Experience",
    "🧩 Problems I Solved",
    "📚 Current Learning & Projects",
    ###"💼 Selected Work",
    "🛠️ Skills & Tools",
    "🚀 Professional Goals 2026",
    ##"🌐 Web Apps"
])

# --- ABOUT ME ---
with tab1:
    st.markdown("### About Me")
    st.write("""
I am a Biomedical Engineer and AI Developer with experience in applied AI, 
medical devices and IoT,I work on building machine learning and neural network solutions, 
deploying models on microcontrollers(ESP32) using TinyML techniques,My focus is on 
practical real-world AI systems with measurable impact.
""")

 # --- Personal Info below About Me ---
    st.markdown("""
    <div style="color: green; font-weight: bold; font-size: 14px;">
    👤 Age: 27<br>
    Nationality: Jordanian<br>
    📧 Email: <a href='mailto:emanmfaris@gmail.com'>emanmfaris@gmail.com</a>
    </div>
    """, unsafe_allow_html=True)

# --- MY EXPERIENCE ---
with tab2:
    st.markdown("### My Experience")
    st.write("""
**Biomedical AI Engineer – Jordan University of Science & Technology (JUST)**  
**Duration:** 1 year and 3+ months

Worked as part of a **specialized team of programmers and under the supervision of the lead professor** to develop a **real, smart medical device**: a **non-invasive glucose monitoring system**.

**Responsibilities & Achievements:**
- End-to-end AI workflow: data collection, cleaning, analysis, and visualization
- Developed ML & Deep Learning models for accurate blood glucose prediction
- Model optimization & quantization for deployment on ESP32 microcontrollers & IoT
- Built CNN models for ECG signal classification and blood cell counting
-Created no-code AI web and mobile apps for non-technical users and students
- Collaborated with a multi-disciplinary team including researchers and developers

**Key Projects:**
1. Non-Invasive Glucose Monitoring Device – AI + embedded deployment  
2. CNN-based ECG Classification – research & personal project  
3. CNN Blood Cell Analysis – research & personal project  
4. No-Code AI Web Applications – data cleaning, visualization, ML experimentation
""")

##############
# --- PROBLEMS I SOLVED ---
with tab3:
    st.markdown("### 🧩 Problems I Solved in Real Projects")

    st.write("""
This section highlights **real problems** I encountered during my previous work  
and how I solved them by building **practical AI-powered web applications**.

Each problem below was addressed by designing a **user-friendly web app**,  
allowing **non-technical users** to interact with data and AI models easily.
""")
    # ---------- Problem 1 ----------
    st.subheader("🔹 Problem 1: Data Handling for Non-Technical Team Members")

    st.write("""
**The Problem:**  
Team members from non-technical backgrounds needed to work with datasets  
but struggled with data cleaning, formatting, and visualization.

**My Solution:**  
I built an **interactive dashboard** that allows users to:
- Upload CSV files
- Automatically clean and organize data
- Visualize datasets based on team-defined requirements

This removed the dependency on technical team members and improved collaboration.
""")
    # ---------- Problem 2 ----------
    st.subheader("🔹 Problem 2: Using ML Models Without ML Knowledge")

    st.write("""
**The Problem:**  
Some team members wanted to experiment with machine learning models  
but had **no background in ML** and could not write code.

**My Solution:**  
I developed a **no-code ML web application** that allows users to:
- Upload their dataset
- Select a predefined ML model
- Adjust model parameters using simple controls
- Understand how each parameter affects results

This enabled experimentation and learning without technical barriers.
""")
    st.markdown("👇👇Try a Demo Version")
    st.markdown("[🌐AI App](https://imanmohammad1998-datadashboard-dash-x8liz7.streamlit.app/)", unsafe_allow_html=True)

######################

# --- CURRENT LEARNING & PROJECTS ---
with tab4:
    st.markdown("### Current Learning & Projects")
    st.write("""
Currently enhancing my professional skills and preparing educational materials:

- **TOT (Training of Trainers) course** – enable me to train non-technical users
- **Training content** focused on TinyML & deploying AI models on microcontrollers
- Teaching AI in a **practical, simplified, and accessible way**
""")
    

# --- SKILLS & TOOLS ---
with tab5:
    st.markdown("### Skills & Tools")
    st.write("Python | Machine Learning | Deep Learning | TensorFlow | Data Analysis | Biomedical Engineering | TinyML | Embedded AI")
    st.subheader("Skill Levels ") 
    skills = {"Python":90, "ML":85, "DL":80, "TensorFlow":75, "Data Analysis":85, "Embedded AI":80, "TinyML":75}
    for skill, value in skills.items():
        st.text(skill)
        st.progress(value/100)

# --- PROFESSIONAL GOALS 2026 ---
with tab6:
    st.markdown("### Professional Goals & Plans for 2026")
    st.write("""
- Find a suitable place to **work on real projects**, with opportunities for **learning, growth, and creativity**.
- Develop **educational courses** in AI for students and engineers that are **practical, simple, and accessible**.
- Enable students and engineers to understand how to **use AI in developing applications and building products**.
- Continue expanding my expertise in **Embedded AI, TinyML, and medical AI solutions**.
""")
