import streamlit as st
import difflib

# Quiz-Fragen und Antworten
quiz_questions = [
    {"question": "Nenne vier Formen des Entrepreneurships.", 
     "correct_answers": ["Existenzgründung", "Nebenerwerb", "Franchise", "Startup"]},
    
    {"question": "Welche Motive treiben Menschen zum Unternehmertum an?", 
     "correct_answers": ["Opportunity Entrepreneurship", "Necessity Entrepreneurship", "Ambitous Entrepreneurship", "Social Entrepreneurship"]},
    
    {"question": "Nenne drei unternehmerische Kompetenzen & Fähigkeiten.", 
     "correct_answers": ["Innovationsfähigkeit", "Risikobereitschaft", "Führungskompetenz"]},

    {"question": "Was versteht man unter Market-Pull und Technology-Pull Innovation?", 
     "correct_answers": ["Market-Pull: Nachfrage bestimmt Innovation", "Technology-Push: Technologie treibt Innovation"]},

    {"question": "Nenne drei Innovationsarten mit Beispielen.", 
     "correct_answers": ["Produktinnovation: iPhone", "Prozessinnovation: Automatisierung", "Soziale Innovation: Qualifikationserhöhungen"]},

    {"question": "Welche drei Arten von Geschäftsideen gibt es?", 
     "correct_answers": ["Disruptiv", "Kreativ-imitativ", "Rein Imitativ"]},

    {"question": "Nenne drei Bestandteile einer Geschäftsidee.", 
     "correct_answers": ["Bedürfnisidee", "Problemlösungsidee", "Kaufmännische Umsetzungsidee"]},

    {"question": "Welche Methoden zur Ideenherkunft und -gewinnung gibt es?", 
     "correct_answers": ["Beobachtung von Märkten", "Blue Oceans", "Verbesserungen"]},

    {"question": "Nenne die fünf Schritte im Design Thinking Prozess.", 
     "correct_answers": ["Einfühlen", "Definieren", "Ideenbildung", "Prototypen erstellen", "Testen"]},

    {"question": "Was ist der Unterschied zwischen Open und Closed Innovation?", 
     "correct_answers": ["Open Innovation: Wissen teilen", "Closed Innovation: Internes Wissen behalten"]},

    {"question": "Nenne fünf Faktoren zur Bewertung einer Geschäftsidee.", 
     "correct_answers": ["Marktpotenzial", "technisch-organisatorisch", "finanziell", "kommerziell", "nachhaltig"]},

    {"question": "Was bedeutet TAM, SAM und SOM?", 
     "correct_answers": ["TAM: Gesamtmarkt", "SAM: Zielmarkt", "SOM: erreichbarer Markt"]},

    {"question": "Was ist ein USP?", 
     "correct_answers": ["Unique Selling Proposition", "Einzigartiges Verkaufsargument"]},

    {"question": "Was sind die Lean Startup Prinzipien?", 
     "correct_answers": ["Build-Measure-Learn", "Schnelle Iteration", "Kundenfeedback nutzen"]},

    {"question": "Was ist ein MVP? Nenne Vor- und Nachteile.", 
     "correct_answers": ["MVP: Einfachste Produktversion", "Vorteil: Schnelles Kundenfeedback", "Nachteil: Unfertiges Produkt"]},

    {"question": "Nenne drei Gründe für Business Planning.", 
     "correct_answers": ["Unternehmensgründung", "Kapitalbeschaffung", "Strategische Planung"]},

    {"question": "Was sind die Vorteile einer Teamgründung?", 
     "correct_answers": ["Mehr Wissen", "Geteiltes Risiko", "Bessere Netzwerke", "Motivation"]},

    {"question": "Nenne drei Elemente des Gründerökosystems.", 
     "correct_answers": ["Standortfaktoren", "Kapitalzugang", "Netzwerkressourcen"]},

    {"question": "Nenne drei Marketinginstrumente für Startups.", 
     "correct_answers": ["Social Media", "Influencer-Marketing", "Guerilla-Marketing"]},

    {"question": "Nenne vier Methoden zur Preisbestimmung.", 
     "correct_answers": ["Kostenbasiert", "Wettbewerbsbasiert", "Nachfragebasiert", "Wertorientiert"]},

    {"question": "Nenne vier Finanzierungsziele.", 
     "correct_answers": ["Liquiditätssicherung", "Rentabilitätsmaximierung", "Sicherheitsstreben", "Unabhängigkeitsstreben"]},

    {"question": "Nenne vier Finanzierungsmethoden.", 
     "correct_answers": ["Venture Capital", "Bootstrapping", "Business Angels", "Crowdfunding"]},

    {"question": "Nenne drei Pitching-Arten.", 
     "correct_answers": ["Elevator Pitch", "Investoren-Pitch", "Value Proposition Statement"]},

    {"question": "Welche Wachstumsstrategien gibt es?", 
     "correct_answers": ["Interne Wachstumsstrategien: Produktinnovation", "Externe Wachstumsstrategien: Übernahmen"]},

    {"question": "Welche Exit-Strategien gibt es?", 
     "correct_answers": ["Verkauf", "Börsengang", "Übernahme"]},

    {"question": "Nenne die vier Phasen eines Startups.", 
     "correct_answers": ["Seed", "Startup", "Growth", "Expansion"]}
]

# Initialisierung des Quiz-Zustands
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answers" not in st.session_state:
    st.session_state.answers = [""] * len(quiz_questions)

# Anzeige der aktuellen Frage
st.title("🎮 Entrepreneurship Quiz")

question_data = quiz_questions[st.session_state.current_question]
st.write(question_data["question"])

# Eingabefeld für die Antwort
user_answer = st.text_input("Deine Antwort:", value=st.session_state.answers[st.session_state.current_question])

# Funktion zur Überprüfung der Ähnlichkeit
def is_answer_correct(user_input, correct_answers):
    for correct in correct_answers:
        if difflib.SequenceMatcher(None, user_input.lower(), correct.lower()).ratio() > 0.7:
            return True
    return False

# Weiter-Button
if st.button("Weiter"):
    # Antwort speichern
    st.session_state.answers[st.session_state.current_question] = user_answer.strip()

    # Überprüfen, ob die Antwort richtig ist
    if is_answer_correct(user_answer, question_data["correct_answers"]):
        st.session_state.score += 1
        st.success("✅ Richtig!")
    else:
        st.error(f"❌ Falsch! Richtige Antwort: {', '.join(question_data['correct_answers'])}")

    # Zur nächsten Frage wechseln
    if st.session_state.current_question < len(quiz_questions) - 1:
        st.session_state.current_question += 1
    else:
        st.session_state.current_question = 0  # Zurück zum Anfang des Quiz

# Endergebnis anzeigen
st.write(f"🏆 Endergebnis: {st.session_state.score}/{len(quiz_questions)} richtig!")
