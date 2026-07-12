import streamlit as st

    
def footer_home():
    
   # logo_url = "https://i.ibb.co/4r5X1FY/apnecollege.png"
    st.markdown(f"""
        <div style="margin-top2rem: display: flex;gap:6px; items-align:center; justify-content:center; text-align:center; margin-bottom:30px;>
            <p style="font-weight:bold: color:white>Created by Mohd Abuzar</p>

        </div> 
       
                """, unsafe_allow_html=True)
    
def footer_dashboard():
    
    #logo_url = "https://i.ibb.co/4r5X1FY/apnecollege.png"
    st.markdown(f"""
        <div style="margin-top2rem: display: flex;gap:6px; items-align:center; justify-content:center; text-align:center; margin-bottom:30px;>
            <p style="font-weight:bold: color:black>Created by Mohd Abuzar</p>

        </div> 
       
                """, unsafe_allow_html=True)