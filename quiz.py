import streamlit as st
import difflib

# Quiz-Fragen und Antworten
quiz_questions = [
    {"question": "Nenne vier Formen des Entrepreneurships.",
     "correct_answers": ["Existenzgründung", "Nebenerwerb", "Franchise", "Startup"]},
    
    {"question": "Welche Motive treiben Menschen zum Unternehmertum an?",
     "correct_answers": ["Opportunity Entrepreneurship", "Necessity Entrepreneurship", 
                         "Ambitious Entrepreneurship", "Social Entrepreneurship"]},
    
    {"question": "Nenne drei unternehmerische Kompetenzen und Fähigkeiten.",
     "correct_answers": ["Innovationsfähigkeit", "Risikobereitschaft", "Führungskompetenz"]},

    {"question": "Market-Pull und Technology-Pull Innovation erklären.",
     "correct_answers": ["Market-Pull: Nachfrage bestimmt Innovation", 
                         "Technology-Push: Technologie treibt Innovation"]},
]

# Funktion zur Überprüfung der Antwort
def is_correct_answer(user_answer, correct_answers):
    user_words = set(user_answer.lower().split(", "))
    
    for correct in correct_answers:
        correct_words = set(correct.lower().split(", "))
        
        if len(user_words) == len(correct_words) and all(
            difflib.get_close_matches(word, correct_words, cutoff=0.8) for word in user_words
        ):
            return True
    return False

# Streamlit App
st.title("🎮 Entrepreneurship Quiz")

# Initialisieren der Session-State Variablen
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# Aktuelle Frage anzeigen
if st.session_state.question_index < len(quiz_questions):
    question_data = quiz_questions[st.session_state.question_index]
    st.subheader(question_data["question"])

    # Antwortfeld (automatisch nach jeder Eingabe zurückgesetzt)
    user_input = st.text_input("Antwort hier eingeben:", key=f"input_{st.session_state.question_index}")

    if st.button("Überprüfen"):
        if is_correct_answer(user_input, question_data["correct_answers"]):
            st.success("✅ Richtig!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Falsch! Richtige Antwort: {', '.join(question_data['correct_answers'])}")

        # Zur nächsten Frage wechseln
        st.session_state.question_index += 1
        st.experimental_rerun()

else:
    # Quiz-Ende anzeigen
    st.subheader(f"🏆 Endergebnis: {st.session_state.score}/{len(quiz_questions)} richtig!")
    if st.button("Nochmal spielen"):
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.experimental_rerun()
