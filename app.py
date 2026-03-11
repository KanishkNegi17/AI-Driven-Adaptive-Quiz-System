import streamlit as st
import random
from quiz_logic import get_adaptive_question

# --- Configuration & State Initialization ---
st.set_page_config(page_title="EASA Flight Dispatcher Quiz", layout="centered")

topics = ["Aviation Navigation", "Aviation Meteorology", "EASA Flight Dispatcher Concepts"]

if 'level' not in st.session_state:
    st.session_state.level = 1
if 'question_num' not in st.session_state:
    st.session_state.question_num = 1
if 'q_data' not in st.session_state:
    st.session_state.q_data = None
if 'quiz_complete' not in st.session_state:
    st.session_state.quiz_complete = False
if 'feedback' not in st.session_state:
    st.session_state.feedback = None

# --- Main UI ---
st.title("✈️ AI-Adaptive Quiz")

if st.session_state.quiz_complete:
    st.success(f"Quiz Complete! Your final EASA Proficiency Level is: {st.session_state.level} / 10")
    if st.button("Restart Quiz"):
        st.session_state.clear()
        st.rerun()

else:
    st.progress(st.session_state.question_num / 10)
    st.subheader(f"Question {st.session_state.question_num} of 10 | Current Level: {st.session_state.level}")
    
    # Fetch question if we don't have one loaded
    if st.session_state.q_data is None:
        with st.spinner("AI is generating your next question..."):
            topic = random.choice(topics)
            st.session_state.q_data = get_adaptive_question(topic, st.session_state.level)
            st.rerun()

    if st.session_state.q_data:
        q = st.session_state.q_data
        st.write(f"**Topic:** {q.get('topic', 'General EASA')}") 
        st.markdown(f"### {q['question']}")
        
        # User Form
        with st.form(key='answer_form'):
            user_choice = st.radio("Select your answer:", q['options'])
            submit_button = st.form_submit_button(label='Submit Answer')
            
        if submit_button:
            is_correct = (user_choice == q['correct_answer'])
            
            if is_correct:
                st.session_state.feedback = {"type": "success", "msg": "Correct! 🎉\n\n" + q['explanation']}
                st.session_state.level = min(10, st.session_state.level + 1)
            else:
                st.session_state.feedback = {"type": "error", "msg": f"Incorrect. The correct answer was: **{q['correct_answer']}**\n\n{q['explanation']}"}
                st.session_state.level = max(1, st.session_state.level - 1)
            
            # Move to next stage
            st.session_state.question_num += 1
            if st.session_state.question_num > 10:
                st.session_state.quiz_complete = True
            
            st.session_state.q_data = None
            st.rerun()

if st.session_state.feedback:
    if st.session_state.feedback["type"] == "success":
        st.success(st.session_state.feedback["msg"])
    else:
        st.error(st.session_state.feedback["msg"])
    st.session_state.feedback = None