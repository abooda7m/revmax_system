import streamlit as st

# إعداد الصفحة
st.set_page_config(
    page_title="RevMax | Smart Retail Dashboard",
    page_icon="📊",
    layout="centered"
)

# العنوان والوصف
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color:#4B9CD3;'>Welcome to RevMax</h1>
        <h3>Your Smart Retail Analytics Platform</h3>
        <p style='max-width: 600px; margin: auto; font-size: 18px; color: gray;'>
            RevMax helps you make data-driven decisions by analyzing sales, customers, and product trends – all in one beautiful dashboard.
        </p>
    </div>
""", unsafe_allow_html=True)

# مسافة بسيطة
st.markdown("<br><br>", unsafe_allow_html=True)

# زر في الوسط
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("👉 Start Dashboard"):
        st.switch_page("pages/home.py")
