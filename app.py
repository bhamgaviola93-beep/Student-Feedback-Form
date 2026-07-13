import streamlit as st
import requests
from datetime import datetime

# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------

st.set_page_config(
    page_title="Student Feedback System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------

st.markdown("""

<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* -----------------------------
GLOBAL
------------------------------ */

html, body, [class*="css"]{

    font-family:'Inter',sans-serif;

}

.stApp{

    background:linear-gradient(135deg,#eef5ff,#dfeaff);

}

/* Hide Streamlit default menu */

#MainMenu{
visibility:hidden;
}

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

/* -----------------------------
HEADINGS
------------------------------ */

h1,h2,h3,h4,h5,h6{

    color:#1E3A8A;

}

/* -----------------------------
LABELS
------------------------------ */

label{

    color:#1E293B !important;

    font-size:17px !important;

    font-weight:600 !important;

}

label p{

    color:#1E293B !important;

}

/* -----------------------------
SELECT BOXES
------------------------------ */

.stSelectbox div[data-baseweb="select"]{

    background:white !important;

    border-radius:12px;

    border:1px solid #CBD5E1;

}

.stSelectbox *{

    color:#1E293B !important;

}

/* -----------------------------
RADIOS
------------------------------ */

.stRadio *{

    color:#1E293B !important;

}

/* -----------------------------
MULTISELECT
------------------------------ */

.stMultiSelect *{

    color:#1E293B !important;

}

/* -----------------------------
TEXT AREA
------------------------------ */

textarea{

    background:white !important;

    color:#1E293B !important;

}

/* -----------------------------
BUTTON
------------------------------ */

.stButton button{

    background:#2563EB;

    color:white;

    border:none;

    border-radius:12px;

    padding:15px;

    font-size:18px;

    font-weight:700;

}

.stButton button:hover{

    background:#1D4ED8;

}

/* -----------------------------
PROGRESS TEXT
------------------------------ */

[data-testid="stProgress"] p{

    color:#1E293B !important;

    font-weight:600;

}

/* -----------------------------
SIDEBAR
------------------------------ */

section[data-testid="stSidebar"]{

    background:#1E3A8A;

}

section[data-testid="stSidebar"] *{

    color:white;

}

/* -----------------------------
SUCCESS BOX
------------------------------ */

.stAlert{

    border-radius:12px;

}

.hero{

    background:linear-gradient(135deg,#2563EB,#1E40AF);

    padding:35px;

    border-radius:22px;

    color:white;

    box-shadow:0 12px 30px rgba(0,0,0,.15);

}

.hero h1{

    color:white;

    text-align:center;

    font-size:48px;

    margin-bottom:10px;

}

.hero h3{

    color:#FDE68A;

    text-align:center;

}

.hero p{

    text-align:center;

    font-size:19px;

    color:white;

}

</style>

""", unsafe_allow_html=True)
with st.sidebar:

    st.title("🎓 Student Feedback")

    st.markdown("---")

    st.info("""

**Estimated Time**

🕒 3 minutes

""")

    st.success("""

🔒 Your responses are confidential.

""")

    st.markdown("---")

    st.caption("Developed by")

    st.write("**Mr. Abraham C. Gaviola**")
    st.markdown("""

<div class="hero">

<h1>🎓 Student Feedback System</h1>

<h3>President Carlos P. Garcia TVSFA</h3>

<p>

Help us improve classroom instruction by sharing your honest feedback.

Your responses are confidential.

</p>

</div>

""", unsafe_allow_html=True)
    st.write("")

st.progress(25, text="Step 1 of 4 • Class Information")

st.write("")
with st.container(border=True):

    st.subheader("📋 Class Details")

    st.caption("Please provide your class information.")

    col1,col2 = st.columns(2)

    with col1:

        grade_level = st.selectbox(

            "🎓 Grade Level",

            [

                "Select Grade Level",

                "Grade 7",

                "Grade 8",

                "Grade 9",

                "Grade 10"

            ]

        )

        sections_dict = {

            "Select Grade Level":["Select a section"],

            "Grade 7":["Select a section","Alcala","Rizal","Lopez Jaena","Mabini","Gomez"],

            "Grade 8":["Select a section","Punong Bayan","Cayabyab","Tamblot","Aguinaldo","De Jesus","Sikatuna"],

            "Grade 9":["Select a section","Dayrit","Joaquin","Dagohoy","Lapu-lapu","Ponce"],

            "Grade 10":["Select a section","Del Mundo","Orosa","Aquino","Magsaysay","Garcia"]

        }

        section = st.selectbox(

            "🏫 Section",

            sections_dict[grade_level]

        )

    with col2:

        subject = st.selectbox(

            "📚 Subject",

            ["English"]

        )

        term = st.selectbox(

            "📅 School Term",

            [

                "Select a term",

                "Term 1",

                "Term 2",

                "Term 3"

            ]

        )

    teacher = st.selectbox(

        "👨‍🏫 Teacher",

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

    st.subheader("📖 Lesson / Topic")
    st.caption("Select the lesson discussed during today's class.")

    topics_dict = {

        "Select Grade Level": [
            "Please select a Grade Level first."
        ],

        "Grade 7": [
            "Conflict (Character vs. Character/Society/Nature)",
            "Structural Elements & Devices",
            "Contextual Analysis",
            "Core Meaning",
            "Composition Process",
            "Final Output (Original Poem or Prose)"
        ],

        "Grade 8": [
            "Conflict (Character vs. Self/Character/Society/Nature)",
            "Structural Elements & Devices",
            "Contextual Analysis",
            "Core Meaning",
            "Composition Process",
            "Final Output (Original Poem or Prose)"
        ],

        "Grade 9": [
            "Conflict (Character vs. Self/Character/Society/Nature)",
            "Structural Elements (Linear, Flashback, Parallel Plots)",
            "Dramatic & Film Elements",
            "Devices & Semiotics",
            "Contextual Analysis",
            "Linguistic Context",
            "Psychological Context",
            "Core Meaning",
            "Composition Process",
            "Final Output (Original One-Act Play Script)"
        ],

        "Grade 10": [
            "Conflict (Character vs. Self/Character/Society/Nature)",
            "Structural Elements",
            "Devices & Semiotics",
            "Contextual Analysis",
            "Linguistic Context",
            "Psychological Context",
            "Core Meaning",
            "Composition Process",
            "Final Output (Original Short Film)"
        ]

    }

    topic = st.radio(
        "Which lesson was discussed today?",
        topics_dict[grade_level]
    )

# =====================================================
# CLASSROOM EXPERIENCE
# =====================================================

st.write("")

with st.container(border=True):

    st.subheader("💡 Classroom Experience")
    st.caption("Select all statements that describe your experience.")

    best_practices = st.multiselect(

        "🌟 Best Teaching Practices",

        [

            "Explained lessons clearly",

            "Made learning easy to understand",

            "Encouraged everyone to participate",

            "Listened carefully to students",

            "Asked interesting questions",

            "Used engaging activities",

            "Used real-life examples",

            "Gave helpful feedback",

            "Treated students with respect",

            "Created a welcoming classroom",

            "Managed the class well",

            "Used learning materials effectively",

            "Kept students engaged",

            "Helped with difficult concepts",

            "Reviewed the lesson before dismissal"

        ]

    )

    st.divider()

    positive_feedback = st.multiselect(

        "❤️ Positive Teacher Behaviour",

        [

            "Kind and approachable",

            "Treats everyone fairly",

            "Respectful",

            "Patient",

            "Friendly",

            "Listens to student concerns",

            "Encourages participation",

            "Calm and professional",

            "Prepared for class",

            "Comes to class on time",

            "Shows enthusiasm",

            "Creates a safe classroom",

            "Values student opinions",

            "Good role model",

            "Shows care and concern"

        ]

    )

    st.divider()

    st.markdown("### 😊 How did you feel during today's class?")

    quick_rating = st.radio(

        "",

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
        "💙 Your honest feedback helps teachers improve their classroom instruction."
    )
    # =====================================================
# STEP 3 OF 4
# =====================================================

st.write("")
st.progress(75, text="Step 3 of 4 • Suggestions & Overall Rating")
st.write("")

# =====================================================
# SUGGESTIONS
# =====================================================

with st.container(border=True):

    st.subheader("🚀 Suggestions for Improvement")
    st.caption("Help us improve future lessons and classroom experiences.")

    col1, col2 = st.columns(2)

    with col1:

        suggestions = st.multiselect(

            "📚 Suggestions for the Lesson",

            [

                "Encourage more student participation",

                "Give more time to answer questions",

                "Use more interactive activities",

                "Include more group work",

                "Use more real-life examples",

                "Ask more higher-order thinking questions",

                "
                # =====================================================
# STEP 4 OF 4
# SUBMIT FEEDBACK
# =====================================================

st.write("")
st.progress(100, text="Step 4 of 4 • Submit Feedback")
st.write("")

with st.container(border=True):

    st.subheader("✅ Submit Your Feedback")

    st.caption(
        "Please review your responses. Once submitted, your feedback will be saved."
    )

    submit = st.button(
        "🚀 Submit My Feedback",
        use_container_width=True
    )

# =====================================================
# SAVE TO SHEETDB
# =====================================================

if submit:

    # Validation
    if (
        grade_level == "Select Grade Level"
        or section == "Select a section"
        or term == "Select a term"
        or teacher == "Select a teacher"
    ):

        st.error(
            "⚠ Please complete the Grade Level, Section, Term, and Teacher fields."
        )

    else:

        row_data = {

            "data":[{

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

                "Additional Comment": comment,

                "Quick Rating": quick_rating,

                "Overall Rating": rating

            }]
        }

        SHEETDB_URL = "https://sheetdb.io/api/v1/0kfovvs2st6yz"

        with st.spinner("Saving your feedback..."):

            try:

                response = requests.post(
                    SHEETDB_URL,
                    json=row_data,
                    timeout=15
                )

                if response.status_code == 201:

                    st.balloons()

                    st.success(
                        "🎉 Thank you! Your feedback has been submitted successfully."
                    )

                    st.markdown(
                        """
                        ### 💙 Your opinion matters!

                        Every response helps our teachers improve instruction and
                        create a better learning experience for everyone.

                        Thank you for taking the time to complete this survey.
                        """
                    )

                    st.info(
                        "You may now close this page."
                    )

                else:

                    st.error(
                        "❌ Unable to save your feedback. Please try again."
                    )

            except requests.exceptions.Timeout:

                st.error(
                    "⏱ The server took too long to respond."
                )

            except requests.exceptions.ConnectionError:

                st.error(
                    "📡 Unable to connect to the internet."
                )

            except Exception as e:

                st.error(f"Unexpected error: {e}")

# =====================================================
# FOOTER
# =====================================================

st.write("")
st.write("")
st.divider()

col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.markdown(
        """
        <div style="text-align:center; color:#64748B;">

        <h4>🎓 Student Feedback System</h4>

        President Carlos P. Garcia Technical Vocational School
        of Fisheries and Arts

        <br><br>

        Developed by

        <br>

        <b>Mr. Abraham C. Gaviola</b>

        <br>

        English Teacher III

        <br><br>

        © 2026 All Rights Reserved

        </div>
        """,
        unsafe_allow_html=True
    )
                
