import streamlit as st
import requests  # Handles sending data to SheetDB
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Student Feedback Form", page_icon="📝", layout="centered")

# --- CUSTOM CSS FOR LARGE, READABLE TEXT ---
st.markdown("""
    <style>
        /* Make radio button text larger */
        .stRadio div [data-testid="stMarkdownContainer"] p {
            font-size: 18px !important;
            font-weight: 500;
        }
        /* Make multi-select option text larger */
        .stMultiSelect div div [data-testid="stMarkdownContainer"] p {
            font-size: 16px !important;
        }
        /* Make dropdown menu items larger */
        .stSelectbox div div div div {
            font-size: 16px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Friendly welcoming header
st.title("✨ Class Feedback Form")
st.markdown("Your feedback helps improve the quality of instructions and helps our teachers grow.")

st.write("---")

# --- SECTION 1: CLASS DETAILS ---
st.header("📋 1. Class Details")

col1, col2 = st.columns(2)

with col1:
    grade_level = st.selectbox(
        "Choose your Grade Level:",
        ["Select Grade Level", "Grade 7", "Grade 8", "Grade 9", "Grade 10"]
    )
    
    sections_dict = {
        "Select Grade Level": ["Select a section"],
        "Grade 7": ["Select a section", "Alcala", "Rizal", "Lopez Jaena", "Mabini", "Gomez"],
        "Grade 8": ["Select a section", "Punong Bayan", "Cayabyab", "Tamblot", "Aguinaldo", "De Jesus", "Sikatuna"],
        "Grade 9": ["Select a section", "Dayrit", "Joaquin", "Dagohoy", "Lapu-lapu", "Ponce"],
        "Grade 10": ["Select a section", "Del Mundo", "Orosa", "Aquino", "Magsaysay", "Garcia"]
    }
    section = st.selectbox("Choose your Section:", sections_dict[grade_level])

with col2:
    subject = st.selectbox("Subject:", ["English"])
    term = st.selectbox("Choose the Term:", ["Select a term", "Term 1", "Term 2", "Term 3"])

teacher = st.selectbox(
    "Choose your Teacher:",
    [
        "Select a teacher", 
        "Mr. Abraham C. Gaviola", 
        "Mr. Apolinario Queroy", 
        "Ms. Carmel G. Macua", 
        "Mrs. Josefina A. Singson", 
        "Mrs. Vionarissa R. Galo", 
        "Mrs. Ma. Terisa P. Salinas", 
        "Mrs. Ken Jared B. Advincula"
    ]
)

# --- SHORTENED TOPIC SECTIONS ---
st.write("---")
st.subheader("📖 Choose the Lesson/Topic discussed:")

topics_dict = {
    "Select Grade Level": ["Please select a Grade Level above first."],
    "Grade 7": [
        "Evaluating Literary Texts: Conflict (Character vs. Character/Society/Nature)",
        "Evaluating Literary Texts: Structural Elements & Devices (Character, Diction, POV)",
        "Evaluating Literary Texts: Contextual Analysis (Biographical, Historical, Sociocultural)",
        "Evaluating Literary Texts: Core Meaning (Universal Truths & Philosophies)",
        "Publishing Text: Composition Process (Pre-writing, Drafting, Revision)",
        "Publishing Text: Final Output (Original Poem or Prose)"
    ],
    "Grade 8": [
        "Evaluating Literary Texts: Conflict (Character vs. Self/Character/Society/Nature)",
        "Evaluating Literary Texts: Structural Elements & Devices (Character, Diction, POV)",
        "Evaluating Literary Texts: Contextual Analysis (Biographical, Historical, Sociocultural)",
        "Evaluating Literary Texts: Core Meaning (Universal Truths & Philosophies)",
        "Publishing Text: Composition Process (Pre-writing, Drafting, Revision)",
        "Publishing Text: Final Output (Original Poem or Prose)"
    ],
    "Grade 9": [
        "Evaluating Literary Texts: Conflict (Character vs. Self/Character/Society/Nature)",
        "Evaluating Literary Texts: Structural Elements (Linear, Flashback, Parallel Plots)",
        "Evaluating Literary Texts: Dramatic & Film Elements (Spectacle, Dialogue, Music)",
        "Evaluating Literary Texts: Devices & Semiotics (Rhyme, Diction, POV, Sign/Referent)",
        "Evaluating Literary Texts: Contextual Analysis (Biographical, Historical, Sociocultural)",
        "Evaluating Literary Texts: Linguistic Context (Deictic, Co-text, Collocation)",
        "Evaluating Literary Texts: Psychological Context",
        "Evaluating Literary Texts: Core Meaning (Universal Truths & Philosophies)",
        "Publishing Text: Composition Process (Pre-writing, Drafting, Revision)",
        "Publishing Text: Final Output (Original One-Act Play Script)"
    ],
    "Grade 10": [
        "Evaluating Literary Texts: Conflict (Character vs. Self/Character/Society/Nature)",
        "Evaluating Literary Texts: Structural Elements (Linear, Flashback, Parallel, Episodic, In Medias Res)",
        "Evaluating Literary Texts: Devices & Semiotics (Spectacle, Dialogue, Rhyme, Diction, POV)",
        "Evaluating Literary Texts: Contextual Analysis (Biographical, Historical, Sociocultural)",
        "Evaluating Literary Texts: Linguistic Context (Deictic Time/Place/Situation, Co-text)",
        "Evaluating Literary Texts: Psychological Context",
        "Evaluating Literary Texts: Core Meaning (Universal Truths & Philosophies)",
        "Publishing Text: Composition Process (Pre-writing, Drafting, Revision)",
        "Publishing Text: Final Output (Original Short Film/Multimodal Text)"
    ]
}

topic = st.radio("Select one:", topics_dict[grade_level], index=0)

st.write("---")

# --- SECTION 2: CLASSROOM EXPERIENCE (SHORTENED PHRASES) ---
st.header("💡 2. Your Classroom Experience")
st.caption("Select all that apply.")

best_practices = st.multiselect(
    "🌟 Best Teaching Practices observed:",
    [
        "Explained lessons clearly",
        "Made learning easy to understand",
        "Encouraged everyone to participate",
        "Listened closely to student ideas",
        "Asked interesting questions",
        "Used fun and engaging activities",
        "Used easy-to-relate examples",
        "Gave helpful feedback",
        "Treated students with respect",
        "Created a welcoming classroom",
        "Managed the classroom well",
        "Used learning materials effectively",
        "Kept the class well engaged",
        "Helped with difficult concepts",
        "Reviewed the lesson at the end"
    ]
)

positive_feedback = st.multiselect(
    "❤️ Positive Teacher Behavior:",
    [
        "Kind and approachable",
        "Treats everyone fairly",
        "Respectful to all students",
        "Patient when teaching",
        "Friendly and welcoming",
        "Listens to student concerns",
        "Encourages and motivates",
        "Calm and professional",
        "Well-prepared for class",
        "Comes to class on time",
        "Enthusiastic while teaching",
        "Creates a safe environment",
        "Values student opinions",
        "Good classroom role model",
        "Shows care and concern"
    ]
)

st.write("---")

# --- SECTION 3: IDEAS FOR IMPROVEMENT (SHORTENED PHRASES) ---
st.header("🚀 3. Ideas for Growth")

suggestions = st.multiselect(
    "📖 Suggestions for the lesson:",
    [
        "Encourage more student participation",
        "Give more time to answer questions",
        "Use more interactive activities",
        "Include more group work activities",
        "Use more real-life examples",
        "Ask more challenging questions",
        "Check understanding more often",
        "Use more visual aids or technology",
        "Give more opportunities to share ideas",
        "Provide reflection time before ending"
    ]
)

improvements = st.multiselect(
    "🛠️ Suggestions for teacher interaction:",
    [
        "Be more approachable to students",
        "Encourage quieter students to join",
        "Give equal attention to everyone",
        "Provide more positive encouragement",
        "Listen more to ideas and concerns",
        "Speak more clearly and confidently",
        "Interact more during activities",
        "Be more patient with questions",
        "Create more expression opportunities",
        "Maintain a respectful atmosphere"
    ]
)

st.write("---")

# --- SECTION 4: OVERALL RATING ---
st.header("⭐ 4. Overall Rating")
rating = st.select_slider(
    "Slide to pick your score (10 is the highest!):",
    options=list(range(1, 11)),
    value=10
)

st.write("---")

# --- SUBMIT BUTTON ---
if st.button("🚀 Submit My Feedback", use_container_width=True):
    if grade_level == "Select Grade Level" or section == "Select a section" or term == "Select a term" or teacher == "Select a teacher":
        st.error("Oops! Please make sure Grade Level, Section, Term, and Teacher are all selected before submitting.")
    else:
        row_data = {
            "data": [{
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Grade Level": grade_level,
                "Section": section,
                "Subject": subject,
                "Term": term,
                "Teacher": teacher,
                "Topic": topic,
                "Best Practices": ", ".join(best_practices),
                "Positive Feedback": ", ".join(positive_feedback),
                "Suggestions": ", ".join(suggestions),
                "Improvements": ", ".join(improvements),
                "Rating": str(rating)
            }]
        }
        
        sheetdb_url = "https://sheetdb.io/api/v1/0kfovvs2st6yz"
        
        try:
            response = requests.post(sheetdb_url, json=row_data)
            if response.status_code == 201:
                st.balloons()
                st.success("🎉 Thank you for honestly giving feedback! Your responses have been saved safely.")
            else:
                st.error("Something went wrong saving your data. Please check your headers.")
        except Exception as e:
            st.error("Could not connect to the sheet right now. Please try again later.")
