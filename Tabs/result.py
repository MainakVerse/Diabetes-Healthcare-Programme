import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to visualize health metrics
def app():
    st.title("📊 Patient Health Metrics Dashboard")

    # Set global style for neon-like effect
    plt.style.use("dark_background")

    # Simulated glucose level data (With & Without Medication)
    days = np.arange(1, 31)
    glucose_no_med = np.random.normal(loc=180, scale=20, size=len(days))
    glucose_with_med = glucose_no_med - np.random.normal(loc=40, scale=10, size=len(days))
    
    # Line chart: Glucose trend with & without medication
    fig, ax = plt.subplots()
    ax.set_facecolor("black")
    ax.plot(days, glucose_no_med, marker='o', linestyle='-', label='Without Medication', color='#FF00FF')  # Neon pink
    ax.plot(days, glucose_with_med, marker='s', linestyle='--', label='With Medication', color='#00FFFF')  # Neon cyan
    ax.set_title("Glucose Level Trend", color='white')
    ax.set_xlabel("Days", color='white')
    ax.set_ylabel("Glucose Level (mg/dL)", color='white')
    ax.legend()
    st.pyplot(fig)

    # Simulated Insulin level comparison (Patient vs Healthy)
    patient_insulin = np.random.normal(loc=12, scale=2, size=1)[0]
    healthy_insulin = 15
    
    # Bar chart: Insulin level comparison
    fig, ax = plt.subplots()
    ax.set_facecolor("black")
    ax.bar(["Patient"], [patient_insulin], color='#00FF00', label='Patient')  # Neon green
    ax.bar(["Healthy"], [healthy_insulin], color='#FF4500', label='Healthy')  # Neon orange-red
    ax.set_title("Insulin Levels Comparison", color='white')
    ax.set_ylabel("Insulin Level (μU/mL)", color='white')
    ax.legend()
    st.pyplot(fig)
    
    # Simulated Diabetes Class Distribution
    diabetes_classes = ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5"]
    diabetes_distribution = np.random.randint(10, 50, size=len(diabetes_classes))
    
    # Pie chart: Diabetes class distribution
    fig, ax = plt.subplots()
    ax.set_facecolor("black")
    colors = ['#FF00FF', '#00FFFF', '#00FF00', '#FFFF00', '#FF4500']  # Neon colors
    ax.pie(diabetes_distribution, labels=diabetes_classes, autopct='%1.1f%%', startangle=140, colors=colors, textprops={'color': "blue"})
    ax.set_title("Diabetes Classification Distribution", color='white')
    st.pyplot(fig)

# Run the dashboard
if __name__ == "__main__":
    app()