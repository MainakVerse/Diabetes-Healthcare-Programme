import streamlit as st

def app():
    st.markdown('''<h1><center>Knowledge Centre</center></h1>''',unsafe_allow_html=True)
    # Paragraph 1: Diabetes Detection
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("./images/1.png", caption="Diabetes Detection", width=200)
    with col2:
        st.markdown('''
            The diabetes care system is an advanced, data-driven platform designed to detect diabetes type and its stage using numerical data from medical test datasets. By leveraging machine learning algorithms, the system analyzes key health metrics such as blood glucose levels, HbA1c, insulin levels, and BMI to classify the type of diabetes (Type 1, Type 2, or prediabetes) and determine its progression stage. This automated detection process ensures accurate and timely diagnosis, enabling healthcare providers to intervene early. The system is user-friendly, allowing patients to upload their medical test results directly, and it generates a comprehensive analysis within seconds.
        ''')

    # Paragraph 2: Medical Recommendations
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('''
            In addition to detection, the system provides personalized medical recommendations based on the patient's specific condition. These recommendations include dietary plans, exercise routines, medication guidelines, and lifestyle modifications tailored to the individual's needs. The system also generates a detailed medical report, which can be downloaded in PDF format for easy sharing with healthcare professionals. This feature ensures that patients have a portable and accessible record of their health status, empowering them to take control of their diabetes management.
        ''')
    with col2:
        st.image("./images/2.png", caption="Medical Recommendations", width=200)

    # Paragraph 3: Capsule Chatbot
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("./images/3.png", caption="Capsule Chatbot", width=200)
    with col2:
        st.markdown('''
            A standout feature of the system is Capsule, an intelligent medical chatbot designed to answer any diabetes-related queries. Capsule is equipped with a vast knowledge base, enabling it to provide information on symptoms, medication dosages, potential health implications, and side effects of treatments. The chatbot uses natural language processing (NLP) to understand user queries and deliver accurate, easy-to-understand responses. Whether a patient is unsure about their medication schedule or curious about the long-term effects of diabetes, Capsule is available 24/7 to provide reliable support and guidance.
        ''')

    # Paragraph 4: Trend Visualization
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('''
            The system also includes a visualization module named Trend, which provides insights into global diabetes trends. Trend uses interactive charts, maps, and graphs to display data such as the prevalence of diabetes across different regions, demographic patterns, and historical trends. This module is particularly useful for researchers, policymakers, and healthcare providers who need to understand the broader impact of diabetes. By visualizing data in an engaging and accessible way, Trend helps stakeholders make informed decisions and develop effective strategies for diabetes prevention and management.
        ''')
    with col2:
        st.image("./images/4.png", caption="Trend Visualization", width=200)

    # Paragraph 5: Streamlit Integration
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("./images/5.png", caption="Streamlit Integration", width=200)
    with col2:
        st.markdown('''
            Built using Streamlit, the diabetes care system offers a seamless and interactive user experience. Streamlit's framework allows for easy integration of machine learning models, data visualizations, and interactive components, making the system both powerful and user-friendly. The platform is accessible via web browsers, ensuring compatibility across devices. With its combination of advanced analytics, personalized recommendations, and interactive features like Capsule and Trend, this diabetes care system represents a significant step forward in diabetes management, providing patients and healthcare providers with the tools they need to combat this global health challenge.
        ''')

# Run the app
if __name__ == "__main__":
    app()
