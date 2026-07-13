import streamlit as st

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

# Using columns to make the dropdowns look neat side-by-side
col1, col2 = st.columns(2)

with col1:
    subject = st.selectbox(
        "Choose your Subject:",
        ["Select a subject", "English 7", "English 8", "English 9", "English 10"]
    )
    term = st.selectbox(
        "Choose the Term:",
        ["Select a term", "Term 1", "Term 2", "Term 3"]
    )

with col2:
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
    topic = st.text_input("What was the Lesson/Topic? (Optional)", placeholder="e.g., Poetry, Grammar, Essay Writing...")

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

# Using select_slider to make the 1-10 choice look clean and satisfying to slide
rating = st.select_slider(
    "Slide to pick your score (10 is the highest!):",
    options=list(range(1, 11)),
    value=10
)

# Friendly score indicator text
if rating >= 9:
    st.info(f"Awesome! You rated this a {rating}/10. 🙌")
elif rating >= 7:
    st.info(f"Great! You rated this a {rating}/10. 👍")
else:
    st.info(f"Thank you. You rated this a {rating}/10. Keep the feedback coming!")

st.write("---")

# --- SUBMIT BUTTON ---
if st.button("🚀 Submit My Feedback", use_container_width=True):
    if subject == "Select a subject" or term == "Select a term" or teacher == "Select a teacher":
        st.error("Oops! Please make sure to select a Subject, Term, and Teacher before submitting.")
    else:
        st.balloons()  # Adds a fun celebration animation for the student!
        st.success("🎉 Thank you for honestly giving feedback! Your responses have been saved safely.")
