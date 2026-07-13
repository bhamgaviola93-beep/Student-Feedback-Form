import streamlit as st
import requests  # Handles sending data to SheetDB
from datetime import datetime

# Set a student-friendly page configuration
st.set_page_config(page_title="Student Feedback Form", page_icon="📝", layout="centered")

# Friendly welcoming header
st.title("✨ Class Feedback Form")
st.markdown("""
Welcome! Your voice matters. Your feedback helps improve the quality of instructions and helps our teachers grow. 
Please take a few moments to answer the questions honestly.
""")

st.write("---")

# --- SECTION 1: CLASS DETAILS ---
st.header("📋 1. Class Details")
st.caption("Tell us which class and teacher you are giving feedback for.")

col1, col2 = st.columns(2)

with col1:
    # 1. Grade Level Selection
    grade_level = st.selectbox(
        "Choose your Grade Level:",
        ["Select Grade Level", "Grade 7", "Grade 8", "Grade 9", "Grade 10"]
    )
    
    # 2. Dynamic Section Selection based on Grade Level
    sections_dict = {
        "Select Grade Level": ["Select a section"],
        "Grade 7": ["Select a section", "Alcala", "Rizal", "Lopez Jaena", "Mabini", "Gomez"],
        "Grade 8": ["Select a section", "Punong Bayan", "Cayabyab", "Tamblot", "Aguinaldo", "De Jesus", "Sikatuna"],
        "Grade 9": ["Select a section", "Dayrit", "Joaquin", "Dagohoy", "Lapu-lapu", "Ponce"],
        "Grade 10": ["Select a section", "Del Mundo", "Orosa", "Aquino", "Magsaysay", "Garcia"]
    }
    section = st.selectbox("Choose your Section:", sections_dict[grade_level])

with col2:
    # 3. Subject locked to English
    subject = st.selectbox("Subject:", ["English"])
    
    # 4. Term Selection
    term = st.selectbox(
        "Choose the Term:",
        ["Select a term", "Term 1", "Term 2", "Term 3"]
    )

# 5. Teacher Selection
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

# --- TOPIC SECTION (Optimized with Radio Buttons for Mobile Text Wrapping) ---
st.write("---")
st.subheader("📖 Choose the Lesson/Topic discussed:")

topics_dict = {
    "Select Grade Level": ["Please select a Grade Level above first."],
    "Grade 7": [
        "Evaluating Literary Texts: Structural Context (Conflict) - Character vs. Character/Society/Nature",
        "Evaluating Literary Texts: Structural Context (Elements & Devices) - Character, Rhyme, Diction, Figures of Speech, POV, Organic Unity",
        "Evaluating Literary Texts: Contextual Analysis - Biographical, Historical, Sociocultural Context",
        "Evaluating Literary Texts: Core Meaning - Maxims, Universal Truths, and Philosophies",
        "Publishing an Original Literary Text: Composition Process (Pre-writing, Drafting, Revision)",
        "Publishing an Original Literary Text: Final Output (Original Poem or Prose)"
    ],
    "Grade 8": [
        "Evaluating Literary Texts: Structural Context (Conflict) - Character vs. Character/Society/Nature/Self",
        "Evaluating Literary Texts: Structural Context (Elements & Devices) - Character, Rhyme, Diction, Figures of Speech, POV, Organic Unity",
        "Evaluating Literary Texts: Contextual Analysis - Biographical, Historical, Sociocultural Contexts",
        "Evaluating Literary Texts: Core Meaning - Maxims, Universal Truths, and Philosophies",
        "Publishing an Original Literary Text: Composition Process (Pre-writing, Drafting, Revision)",
        "Publishing an Original Literary Text: Final Output (Original Poem or Prose)"
    ],
    "Grade 9": [
        "Evaluating Literary Texts: Structural Context (Conflict) - Character vs. Character/Society/Nature/Self",
        "Evaluating Literary Texts: Structural Context (Elements & Devices) - Plot Structures (Linear, Flashback, Parallel Plot)",
        "Evaluating Literary Texts: Structural Context (Elements & Devices) - Dramatic/Film Elements (Spectacle, Dialogue, Music)",
        "Evaluating Literary Texts: Structural Context (Elements & Devices) - Rhyme, Diction, Figures of Speech, POV, Organic Unity, Semiotics",
        "Evaluating Literary Texts: Contextual Analysis - Biographical, Historical, Sociocultural Contexts",
        "Evaluating Literary Texts: Contextual Analysis - Linguistic Context (Deictic, Co-text, Collocation)",
        "Evaluating Literary Texts: Contextual Analysis - Psychological Context",
        "Evaluating Literary Texts: Core Meaning - Maxims, Universal Truths, and Philosophies",
        "Publishing an Original Literary Text: Composition Process (Pre-writing, Drafting, Revision)",
        "Publishing an Original Literary Text: Final Output (Original Script for a One-Act Play)"
    ],
    "Grade 10": [
        "Evaluating Literary Texts: Structural Context (Conflict) - Character vs. Character/Society/Nature/Self",
        "Evaluating Literary Texts: Structural Context (Elements & Devices) - Plot Structures (Linear, Flashback, Parallel, Episodic, In Medias Res)",
        "Evaluating Literary Texts: Structural Context (Elements & Devices) - Spectacle, Dialogue, Music, Rhyme, Diction, Figures of Speech, POV, Organic Unity, Semiotics",
        "Evaluating Literary Texts: Contextual Analysis - Biographical, Historical, Sociocultural Contexts",
        "Evaluating Literary Texts: Contextual Analysis - Linguistic Context (Deictic Time/Place/Situation, Co-text, Collocation)",
        "Evaluating Literary Texts: Contextual Analysis - Psychological Context",
        "Evaluating Literary Texts: Core Meaning - Maxims, Universal Truths, and Philosophies",
        "Publishing an Original Literary Text: Composition Process (Pre-writing, Drafting, Revision)",
        "Publishing an Original Literary Text: Final Output (Original Short Film/Multimodal Text)"
    ]
}

# We use st.radio instead of selectbox so text wraps perfectly into multiple lines on phones
topic = st.radio("Select one:", topics_dict[grade_level], index=0)

st.write("---")

# --- SECTION 2: CLASSROOM EXPERIENCE ---
st.header("💡 2. Your Classroom Experience")
st.caption("What did your teacher do well? Tick as many as you like!")

best_practices = st.multiselect(
    "🌟 Best Teaching Practices observed:",
    [
        "The teacher explained the lesson clearly.",
        "The teacher made learning easy to understand.",
        "The teacher encouraged everyone to participate.",
        "The teacher listened to students' ideas.",
        "The teacher asked interesting questions.",
        "The teacher used fun and engaging activities.",
        "The teacher used examples that were easy to relate to.",
        "The teacher gave helpful feedback.",
        "The teacher treated all students with respect.",
        "The teacher created a friendly and welcoming classroom.",
        "The teacher managed the class well.",
        "The teacher used learning materials effectively.",
        "The teacher kept the class engaged.",
        "The teacher helped students understand difficult concepts.",
        "The teacher reviewed the lesson before ending the class."
    ]
)

positive_feedback = st.multiselect(
    "❤️ Positive Feedback about the teacher's behavior:",
    [
        "The teacher is kind and approachable.",
        "The teacher treats everyone fairly.",
        "The teacher is respectful to all students.",
        "The teacher is patient when teaching.",
        "The teacher is friendly and welcoming.",
        "The teacher listens to students' concerns.",
        "The teacher encourages and motivates students.",
        "The teacher remains calm and professional.",
        "The teacher is well-prepared for class.",
        "The teacher comes to class on time.",
        "The teacher shows enthusiasm while teaching.",
        "The teacher creates a safe and positive learning environment.",
        "The teacher values students' opinions.",
        "The teacher is a good role model.",
        "The teacher shows care and concern for students."
    ]
)

st.write("---")

# --- SECTION 3: IDEAS FOR IMPROVEMENT ---
st.header("🚀 3. Ideas for Growth")
st.caption("How can the class or the teacher become even better? Select your suggestions.")

suggestions = st.multiselect(
    "📖 Suggestions for the lesson:",
    [
        "The teacher may encourage more students to participate.",
        "The teacher may give students more time to answer questions.",
        "The teacher may use more interactive activities.",
        "The teacher may include more group work.",
        "The teacher may use more real-life examples.",
        "The teacher may ask more challenging questions.",
        "The teacher may check students' understanding more often.",
        "The teacher may use more visual aids or technology.",
        "The teacher may give more opportunities for students to share their ideas.",
        "The teacher may provide more time for reflection before ending the lesson."
    ]
)

improvements = st.multiselect(
    "🛠️ Suggestions for teacher interaction:",
    [
        "The teacher may be more approachable to students.",
        "The teacher may encourage quieter students to participate.",
        "The teacher may give equal attention to all students.",
        "The teacher may provide more encouragement and positive reinforcement.",
        "The teacher may listen more to students' ideas and concerns.",
        "The teacher may speak more clearly and confidently.",
        "The teacher may interact more with students during activities.",
        "The teacher may be more patient when answering questions.",
        "The teacher may create more opportunities for students to express themselves.",
        "The teacher may continue fostering a positive and respectful classroom atmosphere."
    ]
)

st.write("---")

# --- SECTION 4: OVERALL RATING ---
st.header("⭐ 4. Overall Rating")
st.write("On a scale of 1 to 10, how would you rate your overall experience with this teacher?")

rating = st.select_slider(
    "Slide to pick your score (10 is the highest!):",
    options=list(range(1, 11)),
    value=10
)

st.write("---")

# --- SUBMIT BUTTON ---
if st.button("🚀 Submit My Feedback", use_container_width=True):
    # Field Validation
    if grade_level == "Select Grade Level" or section == "Select a section" or term == "Select a term" or teacher == "Select a teacher" or grade_level == "Select Grade Level":
        st.error("Oops! Please make sure Grade Level, Section, Term, and Teacher are all selected before submitting.")
    else:
        # Match data mapping to your Google Sheet column headers
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
        
        # Your custom SheetDB endpoint
        sheetdb_url = "https://sheetdb.io/api/v1/0kfovvs2st6yz"
        
        try:
            response = requests.post(sheetdb_url, json=row_data)
            if response.status_code == 201:
                st.balloons()  # Fun celebration animation!
                st.success("🎉 Thank you for honestly giving feedback! Your responses have been saved safely.")
            else:
                st.error("Something went wrong saving your data. Please check your headers.")
        except Exception as e:
            st.error("Could not connect to the sheet right now. Please try again later.")
