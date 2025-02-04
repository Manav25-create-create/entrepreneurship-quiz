import streamlit as st
import difflib

# Liste der Fragen und Antworten
quiz_questions = [
    {"question": "Nenne vier Formen des Entrepreneurships.",
     "correct_answers": ["Existenzgründung", "Nebenerwerb", "Franchise", "Startup"]},

    {"question": "Welche Motive treiben Menschen zum Unternehmertum an?",
     "correct_answers": ["Opportunity Entrepreneurship", "Necessity Entrepreneurship", 
                         "Ambitious Entrepreneurship", "Social Entrepreneurship"]},

    {"question": "Nenne drei unternehmerische Kompetenzen und Fähigkeiten.",
     "correct_answers": ["Innovationsfähigkeit", "Risikobereitschaft", "Führungskompetenz"]},

    {"question": "Erkläre Market-Pull und Technology-Pull Innovation.",
     "correct_answers": ["Market-Pull: Nachfrage bestimmt Innovation", 
                         "Technology-Push: Technologie treibt Innovation"]},

    {"question": "Nenne 2-3 Innovationsarten mit Beispielen.",
     "correct_answers": ["Produktinnovation", "Prozessinnovation", "Soziale Innovation"]},

    {"question": "Nenne drei Arten von Geschäftsideen.",
     "correct_answers": ["Disruptiv", "Kreativ-imitativ", "Rein Imitativ"]},

    {"question": "Nenne drei Bestandteile einer Geschäftsidee.",
     "correct_answers": ["Bedürfnisidee", "Problemlösungsidee", "Kaufmännische Umsetzungsidee"]},

    {"question": "Wie kann eine Idee entstehen oder gewonnen werden?",
     "correct_answers": ["Beobachtung von Märkten", "Blue Oceans", "Verbesserungen"]},

    {"question": "Nenne die fünf Phasen des Design Thinking Prozesses.",
     "correct_answers": ["Einfühlen", "Definieren", "Ideenbildung", "Prototypen erstellen", "Testen"]},

    {"question": "Was ist der Unterschied zwischen Open und Closed Innovation?",
     "correct_answers": ["Open Innovation: Wissen teilen", "Closed Innovation: Internes Wissen behalten"]},

    {"question": "Nenne fünf Faktoren zur Bewertung einer Geschäftsidee.",
     "correct_answers": ["Marktpotenzial", "technisch-organisatorisch", "finanziell", "kommerziell", "nachhaltig"]},

    {"question": "Erkläre TAM, SAM, SOM.",
     "correct_answers": ["TAM: Gesamtmarkt", "SAM: Zielmarkt", "SOM: Erreichbarer Markt"]},

    {"question": "Was bedeutet USP und nenne ein Beispiel.",
     "correct_answers": ["Unique Selling Proposition", "Beispiel: Erstes Smartphone"]},

    {"question": "Was sind die Prinzipien des Lean Startup?",
     "correct_answers": ["Build-Measure-Learn", "Schnelle Iteration", "Datengetriebene Entscheidungen"]},

    {"question": "Erkläre das MVP-Konzept mit Vor- und Nachteilen.",
     "correct_answers": ["MVP: Einfachste Version eines Produkts", 
                         "Vorteile: Schnelle Markteinführung", "Nachteile: Kunden können enttäuscht sein"]},

    {"question": "Nenne drei Gründe für Business Planning.",
     "correct_answers": ["Unternehmensgründung", "Kapitalbeschaffung", "Strategische Planung"]},

    {"question": "Nenne zwei Aspekte zur Qualitätsbewertung im Business Planning.",
     "correct_answers": ["Marktanalyse", "Geschäftsmodellanalyse"]},

    {"question": "Was sind Vorteile einer Teamgründung?",
     "correct_answers": ["Mehr Wissen", "Geteiltes Risiko", "Bessere Netzwerke"]},

    {"question": "Nenne drei Elemente eines Gründerökosystems.",
     "correct_answers": ["Standortfaktoren", "Kapitalzugang", "Netzwerkressourcen"]},

    {"question": "Welche Marketinginstrumente sind für Startups wichtig?",
     "correct_answers": ["Social Media", "Influencer-Marketing", "Guerilla-Marketing"]},

    {"question": "Nenne vier Methoden zur Preisbestimmung.",
     "correct_answers": ["Kostenbasiert", "Wettbewerbsbasiert", "Nachfragebasiert", "Wertorientiert"]},

    {"question": "Nenne vier Finanzierungsziele mit Beispielen.",
     "correct_answers": ["Liquiditätssicherung", "Rentabilitätsmaximierung", "Sicherheitsstreben", "Unabhängigkeit"]},

    {"question": "Nenne vier Finanzierungsmethoden.",
     "correct_answers": ["Venture Capital", "Bootstrapping", "Business Angels", "Crowdfunding"]},

    {"question": "Welche Arten von Pitching gibt es?",
     "correct_answers": ["Elevator Pitch", "Investoren-Pitch", "Value Proposition Statement"]},

    {"question": "Nenne eine interne und eine externe Wachstumsstrategie.",
     "correct_answers": ["Produktinnovation", "Übernahmen"]},

    {"question": "Erkläre den EXIT-Prozess.",
     "correct_answers": ["Verkauf", "Börsengang", "Übernahme"]},

    {"question": "Nenne die vier Phasen eines Startups.",
     "correct_answers": ["Seed", "Startup", "Growth", "Expansion"]}
]

# Funktion zur Überprüfung der Antwort (Akzeptiert ähnliche und unsortierte Eingaben)
def is_correct_answer(user_answer, correct_answers):
    user_words = {word.strip().lower() for word in user_answer.split(",")}
    correct_set = {word.lower() for word in correct_answers}

    if user_words == correct_set:
        return True

    match_count = sum(any(difflib.get_close_matches(word, correct_set, cutoff=0.8)) for word in user_words)
    return match_count == len(correct_set)

# Streamlit App
st.title("🎮 Entrepreneurship Quiz")

if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "message" not in st.session_state:
    st.session_state.message = ""

if st.session_state.question_index < len(quiz_questions):
    question_data = quiz_questions[st.session_state.question_index]
    st.subheader(question_data["question"])

    user_input = st.text_input("Antwort hier eingeben:", key="input", value="")

    if st.button("Überprüfen"):
        if user_input.strip():
            if is_correct_answer(user_input, question_data["correct_answers"]):
                st.session_state.message = "✅ Richtig!"
                st.session_state.score += 1
            else:
                st.session_state.message = f"❌ Falsch! Richtige Antwort: {', '.join(question_data['correct_answers'])}"

            st.session_state.question_index += 1
            st.rerun()
        else:
            st.session_state.message = ""

    if st.session_state.message:
        if "❌" in st.session_state.message:
            st.error(st.session_state.message)
        else:
            st.success(st.session_state.message)

else:
    st.subheader(f"🏆 Endergebnis: {st.session_state.score}/{len(quiz_questions)} richtig!")
    if st.button("Nochmal spielen"):
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.message = ""
        st.rerun()
