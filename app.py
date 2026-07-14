import streamlit as st
import requests
from datetime import datetime

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="English 9 Student Feedback",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

.stApp{
    background:linear-gradient(135deg,#1E3A8A,#3B82F6);
}

/* Hide Streamlit Menu */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#153E90;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Containers */
div[data-testid="stVerticalBlockBorderWrapper"]{
    background:rgba(255,255,255,.08);
    border-radius:18px;
    border:1px solid rgba(255,255,255,.20);
    padding:18px;
}

/* Labels */
h1,h2,h3,h4,h5,h6,label,label p,.stWidgetLabel p{
    color:white !important;
}

/* Caption */
.stCaption{
    color:#E5E7EB !important;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"]{
    background:#1E3A8A !important;
    border:1px solid #60A5FA;
    border-radius:10px;
}

.stSelectbox *{
    color:white !important;
}

/* Multiselect */
.stMultiSelect div[data-baseweb="select"]{
    background:#1E3A8A !important;
    color:white !important;
}

/* Radio */
.stRadio *{
    color:white !important;
}

/* Slider */
.stSlider *{
    color:white !important;
}

/* Text Area */
textarea{
    background:#1E3A8A !important;
    color:white !important;
}

/* Buttons */
.stButton button{
    width:100%;
    background:#2563EB;
    color:white;
    font-size:18px;
    font-weight:bold;
    border-radius:12px;
    border:none;
    padding:14px;
}

.stButton button:hover{
    background:#1D4ED8;
}

/* Hero */
.hero{
    background:linear-gradient(135deg,#2563EB,#1E40AF);
    border-radius:20px;
    padding:40px;
    text-align:center;
    color:white;
    box-shadow:0px 12px 30px rgba(0,0,0,.25);
}

.hero h1{
    color:white;
    font-size:50px;
}

.hero h3{
    color:#FCD34D;
}

.hero p{
    color:white;
    font-size:19px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:
    st.title("🎓 Student Feedback")
    st.markdown("---")
    st.info("""
### ⏱ Estimated Time
**3 Minutes**
""")

    st.success("""
### 🔒 Confidential
Your responses are anonymous and will only be used to improve classroom instruction.
""")
    st.markdown("---")
    st.markdown("### 👨‍🏫 Teacher")
    st.write("**Mr. Abraham C. Gaviola**")

    st.markdown("### 📚 Subject")
    st.write("**English 9**")

    st.markdown("### 🏫 Sections")
    st.write("""
• Grade 9 – Dayrit
• Grade 9 – Joaquin
• Grade 9 – Dagohoy
""")
    st.markdown("---")
    st.caption("President Carlos P. Garcia TVSFA")
    st.caption("Student Feedback System v1.0")

# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="hero">
<h1>🎓 Student Feedback System</h1>
<h3>English 9 Classroom Observation</h3>
<p>
Your honest feedback helps improve classroom instruction.
All responses are kept confidential.
</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# STEP 1 OF 4
# =====================================================

st.write("")
st.progress(25, text="Step 1 of 4 • Class Information")
st.write("")

with st.container(border=True):
    st.subheader("📋 Class Information")
    st.caption("Tell us which class you belong to.")
    col1, col2 = st.columns(2)

    with col1:
        section = st.selectbox(
            "🏫 Section",
            [
                "Select your section",
                "Grade 9 - Dayrit",
                "Grade 9 - Joaquin",
                "Grade 9 - Dagohoy"
            ]
        )

    with col2:
        term = st.selectbox(
            "📅 School Term",
            [
                "Select a term",
                "Term 1",
                "Term 2",
                "Term 3"
            ]
        )

    st.info("""
**Teacher:** Mr. Abraham C. Gaviola
**Subject:** English 9
""")

# =====================================================
# STEP 2 OF 4
# =====================================================

st.write("")
st.progress(50, text="Step 2 of 4 • Lesson & Classroom Experience")
st.write("")

with st.container(border=True):
    st.subheader("📖 Lesson Discussed")
    st.caption("Select the lesson discussed during today's English class.")

    topic = st.selectbox(
        "Lesson / Topic",
        [
            "Select today's lesson",
            "Conflict (Character vs. Self, Character, Society, Nature)",
            "Structural Elements (Episodic & Parallel Plot)",
            "Dramatic Elements (Spectacle, Dialogue, Music)",
            "Film Elements",
            "Figures of Speech",
            "Sound Devices",
            "Rhyme",
            "Meter",
            "Contextual Analysis",
            "Linguistic Context",
            "Psychological Context",
            "Core Meaning",
            "Composition Process",
            "Performance Task"
        ]
    )

st.write("")

with st.container(border=True):
    st.subheader("🌟 Classroom Experience")
    st.caption("Select all statements that describe your experience during today's lesson.")

    best_practices = st.multiselect(
        "Best Teaching Practices",
        [
            "Explained the lesson clearly",
            "Made the lesson easy to understand",
            "Used real-life examples",
            "Asked thought-provoking questions",
            "Encouraged everyone to participate",
            "Used engaging classroom activities",
            "Checked students' understanding",
            "Answered students' questions",
            "Provided helpful feedback",
            "Used learning materials effectively",
            "Managed the classroom well",
            "Reviewed important ideas before ending the lesson"
        ]
    )

    st.divider()

    positive_feedback = st.multiselect(
        "Teacher's Positive Behaviors",
        [
            "Kind and approachable",
            "Respectful",
            "Patient",
            "Friendly",
            "Treats everyone fairly",
            "Listens to students",
            "Encourages participation",
            "Prepared for class",
            "Starts class on time",
            "Speaks clearly",
            "Shows enthusiasm",
            "Creates a positive learning environment"
        ]
    )

    st.divider()

    quick_rating = st.radio(
        "😊 Overall Classroom Experience",
        [
            "🤩 Excellent",
            "😊 Very Good",
            "🙂 Good",
            "😐 Fair",
            "😔 Needs Improvement"
        ],
        horizontal=True
    )

    st.info("💙 Thank you for giving honest feedback. Your responses help improve classroom instruction.")

# =====================================================
# STEP 3 OF 4
# =====================================================

st.write("")
st.progress(75, text="Step 3 of 4 • Suggestions & Overall Rating")
st.write("")

with st.container(border=True):
    st.subheader("📝 Suggestions and Feedback")
    st.caption("Help us make future English classes even better.")

    helped_learning = st.multiselect(
        "✅ What helped you learn today?",
        [
            "Clear explanation",
            "Examples",
            "Group activities",
            "Class discussion",
            "Teacher's feedback",
            "Learning materials",
            "Games or interactive activities",
            "Question and answer session",
            "Everything helped"
        ]
    )

    st.divider()

    improvement = st.multiselect(
        "💡 What would improve future lessons?",
        [
            "More examples",
            "More group activities",
            "More educational games",
            "More videos",
            "More practice exercises",
            "More time for activities",
            "More class discussions",
            "More review before quizzes",
            "Nothing. The lesson was excellent."
        ]
    )

    st.divider()

    comments = st.text_area(
        "💬 Additional Comments",
        placeholder="Share any comments, suggestions, or appreciation for today's lesson (optional).",
        height=150
    )

    st.divider()

    overall_rating = st.slider(
        "⭐ Overall Rating",
        min_value=1,
        max_value=5,
        value=5,
        help="1 = Poor | 5 = Excellent"
    )

    st.success("👏 Thank you! Your feedback helps improve the quality of teaching and learning.")

# =====================================================
# STEP 4 OF 4
# =====================================================

st.write("")
st.progress(100, text="Step 4 of 4 • Submit Feedback")
st.write("")

st.info("📩 Please review your responses before clicking **Submit Feedback**.")

submit = st.button(
    "📨 Submit Feedback",
    use_container_width=True,
    type="primary"
)

if submit:
    # =====================================================
    # VALIDATION
    # =====================================================
    if section == "Select your section":
        st.error("Please select your section.")
        st.stop()

    if term == "Select a term":
        st.error("Please select the school term.")
        st.stop()

    if topic == "Select today's lesson":
        st.error("Please select the lesson discussed today.")
        st.stop()

    # =====================================================
    # DATA STRUCTURE FOR SHEETDB
    # =====================================================
    data = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Teacher": "Mr. Abraham C. Gaviola",
        "Subject": "English 9",
        "Section": section,
        "Term": term,
        "Lesson": topic,
        "Best Teaching Practices": ", ".join(best_practices),
        "Positive Teacher Behaviors": ", ".join(positive_feedback),
        "Class Experience": quick_rating,
        "Helped Learning": ", ".join(helped_learning),
        "Suggested Improvements": ", ".join(improvement),
        "Comments": comments,
        "Overall Rating": overall_rating
    }

    # Wrap the row inside a 'data' array as required by SheetDB
    payload = {"data": [data]}

    # =====================================================
    # API ENDPOINT (READ SECURELY FROM STREAMLIT SECRETS)
    # =====================================================
    try:
        API_URL = st.secrets["SHEETDB_URL"]
    except KeyError:
        st.error("Missing secret: please add SHEETDB_URL to your Streamlit App settings.")
        st.stop()

    # =====================================================
    # SEND DATA
    # =====================================================
    with st.spinner("Submitting your feedback..."):
        try:
            response = requests.post(
                API_URL,
                json=payload,
                timeout=20
            )

            # SheetDB responds with 201 when rows are successfully added
            if response.status_code == 201:
                st.balloons()
                st.success("""
### ✅ Feedback Submitted!

Thank you for taking the time to complete the evaluation.
Your responses have been recorded successfully.
""")
            else:
                st.error(f"Submission failed (Status Code: {response.status_code}). Response text: {response.text}")

        except requests.exceptions.Timeout:
            st.error("The request timed out. Please check your internet connection and try again.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
