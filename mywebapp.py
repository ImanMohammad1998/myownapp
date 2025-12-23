import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Eman – Biomedical AI Engineer Portfolio",
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
st.markdown("<h1 style='text-align: center; color:#4CAF50;'>Eman – Biomedical AI Engineer</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color:#555555;'>Developing AI Solutions for Healthcare and Education</h3>", unsafe_allow_html=True)

# Tabs with emojis
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "👩‍💻 About Me",
    "🎯 My Experience",
    "📚 Current Learning & Projects",
    "💼 Selected Work",
    "🛠️ Skills & Tools",
    "🚀 Professional Goals 2026",
    "🌐 Web Apps"
])

# --- ABOUT ME ---
with tab1:
    st.markdown("### About Me")
    st.write("""
Biomedical Engineer and AI Enthusiast with experience in **medical AI**, **embedded systems**, and **no-code AI solutions**.
I combine biomedical knowledge with AI techniques to solve real-world healthcare challenges and empower non-technical users.
""")
    st.image(
        "https://images.unsplash.com/photo-1581092580494-8e567af7b9be?auto=format&fit=crop&w=800&q=80",
        caption="AI + Healthcare",
        use_column_width=True
    )

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
- Created no-code AI web and mobile apps for non-technical users and students
- Collaborated with a multi-disciplinary team including researchers and developers

**Key Projects:**
1. Non-Invasive Glucose Monitoring Device – AI + embedded deployment  
2. CNN-based ECG Classification – research & personal project  
3. CNN Blood Cell Analysis – research & personal project  
4. No-Code AI Web Applications – data cleaning, visualization, ML experimentation
""")
    st.image(
        "https://images.unsplash.com/photo-1581092580494-8e567af7b9be?auto=format&fit=crop&w=800&q=80",
        caption="Team Collaboration & AI Project",
        use_column_width=True
    )

# --- CURRENT LEARNING & PROJECTS ---
with tab3:
    st.markdown("### Current Learning & Projects")
    st.write("""
Currently enhancing my professional skills and preparing educational materials:

- **TOT (Training of Trainers) course** – enable me to train non-technical users
- **Training content** focused on TinyML & deploying AI models on microcontrollers
- Teaching AI in a **practical, simplified, and accessible way**
""")
    st.image(
        "https://images.unsplash.com/photo-1555685812-4b943f1b5ebf?auto=format&fit=crop&w=800&q=80",
        caption="Learning & Training Preparation",
        use_column_width=True
    )

# --- SELECTED WORK ---
with tab4:
    st.markdown("### Selected Work")
    st.write("""
**AI-Based Biomedical Data Analysis**  
- Developed ML pipelines for biomedical applications  
- Data preprocessing, feature engineering, and model evaluation  

**Machine Learning Model Development**  
- Built models to assist healthcare workflows  
- Collaborated with cross-functional teams
""")
    if st.checkbox("Show Performance Chart"):
        df = pd.DataFrame({
            "Step": ["Data Prep", "Feature Eng.", "Model Training", "Evaluation"],
            "Progress": [80, 70, 90, 85]
        })
        st.bar_chart(df.set_index("Step"))
    st.image(
        "https://images.unsplash.com/photo-1581092580494-8e567af7b9be?auto=format&fit=crop&w=800&q=80",
        caption="Selected Work / Projects",
        use_column_width=True
    )

# --- SKILLS & TOOLS ---
with tab5:
    st.markdown("### Skills & Tools")
    st.write("Python | Machine Learning | Deep Learning | TensorFlow | Data Analysis | Biomedical Engineering | TinyML | Embedded AI")
    st.subheader("Skill Levels (Dummy Data)")
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
    st.image(
        "https://images.unsplash.com/photo-1555685812-4b943f1b5ebf?auto=format&fit=crop&w=800&q=80",
        caption="Future Goals & Career Development",
        use_column_width=True
    )

# --- WEB APPS ---
with tab7:
    st.markdown("### Interactive No-Code AI Web Applications")
    st.write("These are interactive applications I developed for students and non-technical users:")

    st.subheader("1️⃣ Data Cleaning Dashboard")
    st.write("Upload, clean, and visualize datasets easily. Perfect for non-technical users.")
    st.markdown("[🌐 Live Demo Link](https://link-to-your-dash-app)")
    st.image("https://images.unsplash.com/photo-1581092580494-8e567af7b9be?auto=format&fit=crop&w=800&q=80", caption="Data Cleaning Dashboard", use_column_width=True)

    st.subheader("2️⃣ ML Model Playground")
    st.write("Experiment with ML models, tune hyperparameters, and evaluate performance. Ideal for students and non-technical users.")
    st.markdown("[🌐 Live Demo Link](https://link-to-your-ml-app)")
    st.image("https://images.unsplash.com/photo-1555685812-4b943f1b5ebf?auto=format&fit=crop&w=800&q=80", caption="ML Model Playground", use_column_width=True)
