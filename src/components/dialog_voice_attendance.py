import streamlit as st 
from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase

st.dialog("Voice Attendance")
def voice_attendance_dialog(selected_subject_id):
    st.write("Record audio of students saying 'I am Present'. The AI will recognize the students.")
    
    audio_data = None
    
    audio_data = st.audio_input("Record classroom audio")
    
    if st.botton('Analye Audio', width='stretch', type='primary'):
        with st.spinner('Processing Audio data...'):
            enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id', selected_subject_id).execute()
            enrolled_students = enrolled_res.data
            
            if not enrolled_students:
                st.warning("No students enrolled in this course.")
                return
            
                