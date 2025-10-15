import streamlit as st

# PHQ-9 Questions and Symptom Mappings
PHQ9_QUESTIONS = [
    ("Little interest or pleasure in doing things that you normally enjoy", "anhedonia"),
    ("Feeling down, depressed, or hopeless", "depressed mood"),
    ("Trouble falling or staying asleep, sleeping too much", "difficulty with sleep"),
    ("Feeling tired or having little energy", "fatigue"),
    ("Poor appetite or overeating", "poor/increased appetite related to mood"),
    ("Feeling bad about yourself or that you are a failure", "low self esteem"),
    ("Trouble concentrating on things", "difficulty concentrating"),
    ("Moving or speaking slowly", "psychomotor slowing"),
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

# Y-BOCS Questions and Response Options
YBOCS_QUESTIONS = [
    {
        "question": "How much of your time is occupied by obsessive thoughts?",
        "symptom": "time occupied by obsessive thoughts",
        "options": [
            "0 - None",
            "1 - Less than 1 hr/day or occasional occurrence",
            "2 - 1 to 3 hrs/day or frequent",
            "3 - Greater than 3 and up to 8 hrs/day or very frequent occurrence",
            "4 - Greater than 8 hrs/day or nearly constant occurrence"
        ]
    },
    {
        "question": "How much do your obsessive thoughts interfere with your work, school, social, or other important role functioning?",
        "symptom": "interference from obsessive thoughts",
        "options": [
            "0 - None",
            "1 - Slight interference with social or other activities, but overall performance not impaired",
            "2 - Definite interference with social or occupational performance, but still manageable",
            "3 - Causes substantial impairment in social or occupational performance",
            "4 - Incapacitating"
        ]
    },
    {
        "question": "How much distress do your obsessive thoughts cause you?",
        "symptom": "distress from obsessive thoughts",
        "options": [
            "0 - None",
            "1 - Not too disturbing",
            "2 - Disturbing, but still manageable",
            "3 - Very disturbing",
            "4 - Near constant and disabling distress"
        ]
    },
    {
        "question": "How much of an effort do you make to resist the obsessive thoughts?",
        "symptom": "difficulty resisting obsessive thoughts",
        "options": [
            "0 - Try to resist all the time",
            "1 - Try to resist most of the time",
            "2 - Make some effort to resist",
            "3 - Yield to all obsessions without attempting to control them, but with some reluctance",
            "4 - Completely and willingly yield to all obsessions"
        ]
    },
    {
        "question": "How much control do you have over your obsessive thoughts?",
        "symptom": "lack of control over obsessive thoughts",
        "options": [
            "0 - Complete control",
            "1 - Usually able to stop or divert obsessions with some effort and concentration",
            "2 - Sometimes able to stop or divert obsessions",
            "3 - Rarely successful in stopping or dismissing obsessions, can only divert attention with difficulty",
            "4 - Obsessions are completely involuntary, rarely able to even momentarily alter obsessive thinking"
        ]
    },
    {
        "question": "How much time do you spend performing compulsive behaviors?",
        "symptom": "time spent on compulsive behaviors",
        "options": [
            "0 - None",
            "1 - Less than 1 hr/day or occasional performance of compulsive behaviors",
            "2 - From 1 to 3 hrs/day, or frequent performance of compulsive behaviors",
            "3 - More than 3 and up to 8 hrs/day, or very frequent performance of compulsive behaviors",
            "4 - More than 8 hrs/day, or near constant performance of compulsive behaviors"
        ]
    },
    {
        "question": "How much do your compulsive behaviors interfere with your work, school, social, or other important role functioning?",
        "symptom": "interference from compulsive behaviors",
        "options": [
            "0 - None",
            "1 - Slight interference with social or other activities, but overall performance not impaired",
            "2 - Definite interference with social or occupational performance, but still manageable",
            "3 - Causes substantial impairment in social or occupational performance",
            "4 - Incapacitating"
        ]
    },
    {
        "question": "How would you feel if prevented from performing your compulsion(s)? How anxious would you become?",
        "symptom": "distress when prevented from compulsions",
        "options": [
            "0 - None",
            "1 - Only slightly anxious if compulsions prevented",
            "2 - Anxiety would mount but remain manageable if compulsions prevented",
            "3 - Prominent and very disturbing increase in anxiety if compulsions interrupted",
            "4 - Incapacitating anxiety from any intervention aimed at modifying activity"
        ]
    },
    {
        "question": "How much of an effort do you make to resist the compulsions?",
        "symptom": "difficulty resisting compulsions",
        "options": [
            "0 - Always try to resist",
            "1 - Try to resist most of the time",
            "2 - Make some effort to resist",
            "3 - Yield to almost all compulsions without attempting to control them, but with some reluctance",
            "4 - Completely and willingly yield to all compulsions"
        ]
    },
    {
        "question": "How strong is the drive to perform the compulsive behavior? How much control do you have over the compulsions?",
        "symptom": "lack of control over compulsive behaviors",
        "options": [
            "0 - Complete control",
            "1 - Pressure to perform the behavior but usually able to exercise voluntary control over it",
            "2 - Strong pressure to perform behavior, can control it only with difficulty",
            "3 - Very strong drive to perform behavior, must be carried to completion, can only delay with difficulty",
            "4 - Drive to perform behavior experienced as completely involuntary and overpowering, rarely able to even momentarily delay activity"
        ]
    }
]

# Define PHQ-9 and GAD-7 options
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
    elif scale == "YBOCS":
        if score <= 7:
            return "subclinical"
        elif score <= 15:
            return "mild"
        elif score <= 23:
            return "moderate"
        elif score <= 31:
            return "severe"
        else:
            return "extreme"

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

def generate_ybocs_summary(ybocs_score, obsessions_score, compulsions_score, ybocs_symptoms):
    ybocs_severity = get_severity(ybocs_score, "YBOCS")
    ybocs_text = format_symptoms(ybocs_symptoms)
    
    summary = f"Y-BOCS Total: {ybocs_score}\n"
    summary += f"Obsessions: {obsessions_score}, Compulsions: {compulsions_score}\n"
    summary += f"Patient endorses {ybocs_severity} obsessive-compulsive symptoms of {ybocs_text}."
    
    return summary

def main():
    st.title("Mental Health Screening Summary Generator")
    
    # GAD-7 Section
    st.header("GAD-7 Assessment")
    gad7_scores = []
    for i, (question, symptom) in enumerate(GAD7_QUESTIONS):
        score = st.radio(
            f"{question}",
            options=RESPONSE_OPTIONS,
            key=f"gad7_{i}",
            horizontal=True
        )
        
        # Get numeric score (0-3) from the selected option
        score_value = RESPONSE_OPTIONS.index(score)
        gad7_scores.append(score_value)
    
    # Calculate GAD-7 symptoms
    gad7_symptoms = [
        symptom for (_, symptom), score in zip(GAD7_QUESTIONS, gad7_scores)
        if score >= 1
    ]
    
    total_gad7 = sum(gad7_scores)
    st.write(f"Total GAD-7 Score: {total_gad7}")

    # PHQ-9 Section
    st.header("PHQ-9 Assessment")
    phq9_scores = []
    for i, (question, symptom) in enumerate(PHQ9_QUESTIONS):
        score = st.radio(
            f"{question}",
            options=RESPONSE_OPTIONS,
            key=f"phq9_{i}",
            horizontal=True
        )
        
        # Get numeric score (0-3) from the selected option
        score_value = RESPONSE_OPTIONS.index(score)
        phq9_scores.append(score_value)
    
    # Calculate PHQ-9 symptoms
    phq9_symptoms = [
        symptom for (_, symptom), score in zip(PHQ9_QUESTIONS, phq9_scores)
        if score >= 1
    ]
    
    total_phq9 = sum(phq9_scores)
    st.write(f"Total PHQ-9 Score: {total_phq9}")
    
    # Y-BOCS Section
    st.header("Y-BOCS Assessment")
    st.write("**Obsessions** are unwanted ideas, images or impulses. **Compulsions** are urges to do repetitive behaviors to lessen anxiety.")
    
    # Obsessions subsection
    st.subheader("Obsessions (Questions 1-5)")
    ybocs_scores = []
    for i in range(5):
        question_data = YBOCS_QUESTIONS[i]
        score = st.radio(
            f"{i+1}. {question_data['question']}",
            options=question_data['options'],
            key=f"ybocs_{i}"
        )
        
        # Get numeric score (0-4) from the selected option
        score_value = question_data['options'].index(score)
        ybocs_scores.append(score_value)
    
    obsessions_score = sum(ybocs_scores[:5])
    st.write(f"Obsessions Subtotal: {obsessions_score}")
    
    # Compulsions subsection
    st.subheader("Compulsions (Questions 6-10)")
    for i in range(5, 10):
        question_data = YBOCS_QUESTIONS[i]
        score = st.radio(
            f"{i+1}. {question_data['question']}",
            options=question_data['options'],
            key=f"ybocs_{i}"
        )
        
        # Get numeric score (0-4) from the selected option
        score_value = question_data['options'].index(score)
        ybocs_scores.append(score_value)
    
    compulsions_score = sum(ybocs_scores[5:])
    st.write(f"Compulsions Subtotal: {compulsions_score}")
    
    # Calculate Y-BOCS symptoms
    ybocs_symptoms = [
        YBOCS_QUESTIONS[i]['symptom'] for i, score in enumerate(ybocs_scores)
        if score >= 1
    ]
    
    total_ybocs = sum(ybocs_scores)
    st.write(f"**Total Y-BOCS Score: {total_ybocs}**")
    
    # NOW display all results at the end after everything is collected
    st.header("Depression & Anxiety Assessment Results")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("PHQ-9 Score", total_phq9)
    with col2:
        st.metric("GAD-7 Score", total_gad7)
        
    st.subheader("Clinical Summary")
    summary = generate_combined_summary(
        total_phq9,
        phq9_symptoms,
        total_gad7,
        gad7_symptoms
    )
    st.text_area("", summary, height=100, key="phq_gad_summary")
    
    # Display Y-BOCS results
    st.header("OCD Assessment Results")
    
    st.metric("Y-BOCS Total Score", total_ybocs)
        
    st.subheader("Y-BOCS Clinical Summary")
    ybocs_summary = generate_ybocs_summary(total_ybocs, obsessions_score, compulsions_score, ybocs_symptoms)
    st.text_area("", ybocs_summary, height=100, key="ybocs_summary")

if __name__ == "__main__":
    main()
