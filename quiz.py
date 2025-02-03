import streamlit as st
import difflib

# Quiz-Fragen & Antworten
quiz_questions = {
    "Nenne vier Formen des Entrepreneurships.": ["Existenzgründung", "Nebenerwerb", "Franchise", "Startup"],
    "Welche Motive treiben Menschen zum Unternehmertum an?": ["Eigenverantwortung", "Unabhängigkeit", "finanzielle Chancen"],
}

def check_answer(user_input, correct_answers):
    for correct_answer in correct_answers:
        if difflib.SequenceMatcher(None, user_input.lower(), correct_answer.lower()).ratio() > 0.7:
            return True
    return False

st.title("🎮 Entrepreneurship Quiz")
score = 0

for question, answers in quiz_questions.items():
    user_input = st.text_input(question, key=question)
    if user_input:
        if check_answer(user_input, answers):
            st.success("✅ Richtig!")
            score += 1
        else:
            st.error(f"❌ Falsch! Richtige Antwort: {', '.join(answers)}")

st.write(f"🏆 Endergebnis: {score}/{len(quiz_questions)} richtig!")
