# =====================================================
# STEP 1 OF 4
# =====================================================

st.write("")
st.progress(25, text="Step 1 of 4 • Class Information")
st.write("")

with st.container(border=True):

    st.subheader("📋 Class Details")
    st.caption("Please tell us which class you belong to.")

    section = st.selectbox(
        "🏫 Section",
        [
            "Select your section",
            "Grade 9 - Dayrit",
            "Grade 9 - Joaquin",
            "Grade 9 - Dagohoy"
        ]
    )

    term = st.selectbox(
        "📅 School Term",
        [
            "Term 1",
            "Term 2",
            "Term 3"
        ]
    )

    st.info(
        """
        **Teacher:** Mr. Abraham C. Gaviola  
        **Subject:** English 9
        """
    )
    # =====================================================
# STEP 2 OF 4
# =====================================================

st.write("")
st.progress(50, text="Step 2 of 4 • Lesson & Classroom Experience")
st.write("")

# =====================================================
# LESSON / TOPIC
# =====================================================

with st.container(border=True):

    st.subheader("📖 Lesson Discussed")
    st.caption("Select the lesson discussed during today's class.")

    topic = st.radio(

        "Which lesson did your teacher discuss today?",

        [

            "Conflict (Character vs. Character, Society, Nature, Self)",

            "Character and Characterization",

            "Plot and Structural Elements",

            "Spectacle, Dialogue, and Music",

            "Rhyme and Meter",

            "Diction",

            "Tone and Mood",

            "Style",

            "Patterns and Motifs",

            "Figures of Speech and Sound Devices",

            "Point of View and Narrative Techniques",

            "Organic Unity",

            "Binary Opposition",

            "Contextual Analysis",

            "Core Meaning",

            "Composition Process",

            "Performance Task"

        ]

    )

# =====================================================
# CLASSROOM EXPERIENCE
# =====================================================

st.write("")

with st.container(border=True):

    st.subheader("💡 Classroom Experience")
    st.caption("Select all statements that describe your learning experience today.")

    best_practices = st.multiselect(

        "🌟 Best Teaching Practices",

        [

            "Explained the lesson clearly",

            "Made difficult ideas easy to understand",

            "Used examples that were easy to relate to",

            "Asked questions that made us think",

            "Encouraged everyone to participate",

            "Used engaging classroom activities",

            "Connected the lesson to real-life situations",

            "Checked if students understood the lesson",

            "Answered students' questions clearly",

            "Provided helpful feedback",

            "Reviewed important points before ending the class",

            "Used learning materials effectively",

            "Managed the class well",

            "Kept students interested throughout the lesson",

            "Created an enjoyable learning experience"

        ]

    )

    st.divider()

    positive_feedback = st.multiselect(

        "❤️ Positive Teacher Behaviors",

        [

            "Kind and approachable",

            "Respectful to students",

            "Patient",

            "Friendly",

            "Treats everyone fairly",

            "Listens to students",

            "Encourages participation",

            "Supports students who need help",

            "Prepared for the lesson",

            "Starts class on time",

            "Speaks clearly",

            "Shows enthusiasm while teaching",

            "Creates a safe classroom environment",

            "Makes students feel comfortable",

            "Shows genuine care for students"

        ]

    )

    st.divider()

    st.subheader("😊 Overall Classroom Experience")

    quick_rating = st.radio(

        "How would you describe today's class?",

        [

            "🤩 Excellent",

            "😊 Very Good",

            "🙂 Good",

            "😐 Fair",

            "😔 Needs Improvement"

        ],

        horizontal=True

    )

    st.info(
        "💙 Thank you for sharing your honest feedback. Your responses help improve teaching and learning."
    )
    # =====================================================
# STEP 3 OF 4
# =====================================================

st.write("")
st.progress(75, text="Step 3 of 4 • Suggestions & Overall Rating")
st.write("")

with st.container(border=True):

    st.subheader("🚀 Suggestions for Improvement")
    st.caption("Your suggestions will help improve future English classes.")

    col1, col2 = st.columns(2)

    with col1:

        suggestions = st.multiselect(

            "📚 Lesson Improvement",

            [

                "Give more examples",

                "Use more group activities",

                "Give more time for activities",

                "Use more educational games",

                "Use more videos or multimedia",

                "Review difficult lessons",

                "Provide more practice exercises",

                "Ask more higher-order thinking questions",

                "Everything was excellent"

            ]

        )

    with col2:

        teacher_improvement = st.multiselect(

            "👨‍🏫 Teacher Improvement",

            [

                "Speak more slowly",

                "Speak louder and clearer",

                "Give everyone a chance to participate",

                "Provide more feedback",

                "Walk around the classroom more often",

                "Encourage shy students",

                "Continue the excellent teaching"

            ]

        )

    st.divider()

    comments = st.text_area(

        "💬 Additional Comments",

        placeholder="Write your comments or suggestions here (optional)...",

        height=120

    )

    st.divider()

    overall_rating = st.slider(

        "⭐ Overall Rating for Today's Lesson",

        min_value=1,

        max_value=5,

        value=5,

        help="1 = Poor   |   5 = Excellent"

    )
    # =====================================================
# STEP 4 OF 4
# =====================================================

st.write("")
st.progress(100, text="Step 4 of 4 • Submit Feedback")
st.write("")

st.info("📩 Please review your answers before submitting.")

submit = st.button(
    "📨 Submit Feedback",
    use_container_width=True,
    type="primary"
)

if submit:

    # -------------------------
    # VALIDATION
    # -------------------------

    if section == "Select your section":
        st.error("Please select your section.")
        st.stop()

    if term == "Select a term":
        st.error("Please select the school term.")
        st.stop()

    if topic is None:
        st.error("Please select the lesson discussed.")
        st.stop()

    # -------------------------
    # DATA TO SEND
    # -------------------------

    data = {

        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "teacher": "Mr. Abraham C. Gaviola",

        "subject": "English 9",

        "section": section,

        "term": term,

        "topic": topic,

        "best_practices": ", ".join(best_practices),

        "positive_behaviors": ", ".join(positive_feedback),

        "class_experience": quick_rating,

        "lesson_suggestions": ", ".join(suggestions),

        "teacher_suggestions": ", ".join(teacher_improvement),

        "comments": comments,

        "overall_rating": overall_rating

    }

    # -------------------------
    # SEND TO GOOGLE SHEETS
    # -------------------------

    WEB_APP_URL = "YOUR_WEB_APP_URL_HERE"

    try:

        response = requests.post(
            WEB_APP_URL,
            json=data,
            timeout=15
        )

        if response.status_code == 200:

            st.success("✅ Thank you! Your feedback has been submitted successfully.")

            st.balloons()

        else:

            st.error("❌ Unable to submit your feedback. Please try again later.")

    except Exception as e:

        st.error(f"⚠️ Connection Error: {e}")
