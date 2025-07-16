import streamlit as st

# PHQ-9 Questions and Symptom Mappings
PHQ9_QUESTIONS = [
    ("Little interest or pleasure in doing things", "anhedonia"),
    ("Feeling down, depressed, or hopeless", "depressed mood"),
    ("Trouble falling/staying asleep, sleeping too much", "difficulty with sleep"),
    ("Feeling tired or having little energy", "fatigue"),
    ("Poor appetite or overeating", "poor/increased appetite related to mood"),
    ("Feeling bad about yourself or that you are a failure", "low self esteem"),
    ("Trouble concentrating on things", "difficulty concentrating"),
    ("Moving or speaking slowly/being fidgety or restless", "psychomotor slowing"),
    ("Thoughts that you would be better off dead or of hurting yourself", "SI")
]

# GAD-7 Questions and Symptom Mappings
GAD7_QUESTIONS = [
    ("Feeling nervous, anxious, or on edge", "anxiety"),
    ("Not being able to stop or control worrying", "uncontrollable worry"),
    ("Worrying too much about different things", "excessive worry"),
    ("Trouble relaxing", "difficulty relaxing"),
    ("Being so restless that it's hard to sit still", "restlessness"),
    ("Becoming easily annoyed or irritable", "irritability"),
    ("Feeling afraid as if something awful might happen", "sense of doom")
]

# Define the options once to ensure consistency
RESPONSE_OPTIONS = [
    "Not at all (0)",
    "Several days (1)",
    "More than half the days (2)",
    "Nearly every day (3)"
]

def get_severity(score, scale):
    if scale == "PHQ9":
        if score <= 4:
            return "minimal"
        elif score <= 9:
            return "mild"
        elif score <= 14:
            return "moderate"
        elif score <= 19:
            return "moderately severe"
        else:
            return "severe"
    elif scale == "GAD7":
        if score <= 4:
            return "minimal"
        elif score <= 9:
            return "mild"
        elif score <= 14:
            return "moderate"
        else:
            return "severe"

def format_symptoms(symptoms):
    if len(symptoms) == 0:
        return "no specific symptoms"
    elif len(symptoms) == 1:
        return symptoms[0]
    elif len(symptoms) == 2:
        return f"{symptoms[0]} and {symptoms[1]}"
    else:
        return ", ".join(symptoms[:-1]) + f", and {symptoms[-1]}"

def generate_combined_summary(phq9_score, phq9_symptoms, gad7_score, gad7_symptoms):
    phq9_severity = get_severity(phq9_score, "PHQ9")
    gad7_severity = get_severity(gad7_score, "GAD7")
    
    phq9_text = format_symptoms(phq9_symptoms)
    gad7_text = format_symptoms(gad7_symptoms)
    
    summary = f"PHQ9: {phq9_score}\n"
    summary += f"GAD7: {gad7_score}\n"
    summary += f"Patient endorses {phq9_severity} depressive symptoms of {phq9_text} and {gad7_severity} anxious symptoms of {gad7_text}."
    
    return summary

def main():
    st.title("Mental Health Screening Summary Generator")
    # Initialize session state for storing scores and symptoms
    if 'phq9_scores' not in st.session_state:
        st.session_state.phq9_scores = [0] * len(PHQ9_QUESTIONS)
        st.session_state.gad7_scores = [0] * len(GAD7_QUESTIONS)
        st.session_state.phq9_symptoms = []
        st.session_state.gad7_symptoms = []
    # GAD-7 Section
    st.header("GAD-7 Assessment")
    for i, (question, symptom) in enumerate(GAD7_QUESTIONS):
        score = st.radio(
            f"{question}",
            options=RESPONSE_OPTIONS,
            key=f"gad7_{i}",
            horizontal=True
        )
        
        # Get numeric score (0-3) from the selected option
        score_value = RESPONSE_OPTIONS.index(score)
        st.session_state.gad7_scores[i] = score_value
        
    # Calculate GAD-7 symptoms
    st.session_state.gad7_symptoms = [
        symptom for (_, symptom), score in zip(GAD7_QUESTIONS, st.session_state.gad7_scores)
        if score >= 1
    ]
    
    total_gad7 = sum(st.session_state.gad7_scores)
    st.write(f"Total GAD-7 Score: {total_gad7}")

    # PHQ-9 Section
    st.header("PHQ-9 Assessment")
    for i, (question, symptom) in enumerate(PHQ9_QUESTIONS):
        score = st.radio(
            f"{question}",
            options=RESPONSE_OPTIONS,
            key=f"phq9_{i}",
            horizontal=True
        )
        
        # Get numeric score (0-3) from the selected option
        score_value = RESPONSE_OPTIONS.index(score)
        st.session_state.phq9_scores[i] = score_value
        
    # Calculate PHQ-9 symptoms
    st.session_state.phq9_symptoms = [
        symptom for (_, symptom), score in zip(PHQ9_QUESTIONS, st.session_state.phq9_scores)
        if score >= 1
    ]
    
    total_phq9 = sum(st.session_state.phq9_scores)
    st.write(f"Total PHQ-9 Score: {total_phq9}")
    
    # Display scores and summary
    st.header("Assessment Results")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("PHQ-9 Score", total_phq9)
    with col2:
        st.metric("GAD-7 Score", total_gad7)
        
    st.subheader("Clinical Summary")
    summary = generate_combined_summary(
        total_phq9,
        st.session_state.phq9_symptoms,
        total_gad7,
        st.session_state.gad7_symptoms
    )
    st.text_area("", summary, height=100)

if __name__ == "__main__":
    main()