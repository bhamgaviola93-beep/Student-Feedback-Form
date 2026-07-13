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
    initial_sidebar_state="collapsed"
)

# ----------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

/* Background */
.stApp{
    background:linear-gradient(135deg,#eef4ff 0%,#dce9ff 50%,#f7fbff 100%);
}

/* Hide Streamlit menu */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Hero Banner */
.hero{
    background:linear-gradient(135deg,#2563eb,#1e3a8a);
    padding:35px;
    border-radius:20px;
    color:white;
    box-shadow:0 12px 35px rgba(0,0,0,.18);
}

.hero h1{
    font-size:48px;
    margin-bottom:5px;
    text-align:center;
}

.hero h3{
    text-align:center;
    font-weight:400;
}

.hero p{
    text-align:center;
    font-size:18px;
}

/* Cards */

.card{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0 10px 25px rgba(0,0,0,.08);
    margin-top:20px;
}

/* Section Titles */

.section-title{
    color:#1e3a8a;
    font-size:30px;
    font-weight:700;
    margin-bottom:20px;
}

/* Labels */

label p{
    font-size:18px !important;
    font-weight:600 !important;
}

/* Buttons */

.stButton>button{

    width:100%;

    background:#2563eb;

    color:white;

    border:none;

    border-radius:12px;

    font-size:20px;

    font-weight:700;

    padding:15px;

    transition:.3s;

}

.stButton>button:hover{

    background:#1d4ed8;

    transform:translateY(-2px);

}

/* Radio */

.stRadio p{
    font-size:17px;
}

/* Multiselect */

.stMultiSelect p{
    font-size:17px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HERO
# ----------------------------------------------------

st.markdown("""
<div class='hero'>

<h1>🎓 Student Feedback System</h1>

<h3>President Carlos P. Garcia TVSFA</h3>

<p>
Your voice matters.
Help us improve classroom instruction by sharing your honest feedback.
All responses are kept confidential.
</p>

</div>

""", unsafe_allow_html=True)

st.write("")

# Progress

st.progress(0.25, text="Step 1 of 4 • Class Information")

st.write("")

# ----------------------------------------------------
# SECTION 1
# ----------------------------------------------------

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>📋 Class Details</div>", unsafe_allow_html=True)

col1,col2=st.columns(2)

with col1:

    grade_level=st.selectbox(
        "🎓 Grade Level",
        [
            "Select Grade Level",
            "Grade 7",
            "Grade 8",
            "Grade 9",
            "Grade 10"
        ]
    )

    sections_dict={
        "Select Grade Level":["Select a section"],
        "Grade 7":["Select a section","Alcala","Rizal","Lopez Jaena","Mabini","Gomez"],
        "Grade 8":["Select a section","Punong Bayan","Cayabyab","Tamblot","Aguinaldo","De Jesus","Sikatuna"],
        "Grade 9":["Select a section","Dayrit","Joaquin","Dagohoy","Lapu-lapu","Ponce"],
        "Grade 10":["Select a section","Del Mundo","Orosa","Aquino","Magsaysay","Garcia"]
    }

    section=st.selectbox(
        "🏫 Section",
        sections_dict[grade_level]
    )

with col2:

    subject=st.selectbox(
        "📚 Subject",
        ["English"]
    )

    term=st.selectbox(
        "📅 School Term",
        [
            "Select a term",
            "Term 1",
            "Term 2",
            "Term 3"
        ]
    )

teacher=st.selectbox(
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

st.markdown("</div>",unsafe_allow_html=True)

st.write("")
# ==========================================================
# STEP 2
# ==========================================================

st.progress(0.50, text="Step 2 of 4 • Lesson & Classroom Experience")

st.write("")

# ==========================================================
# TOPIC
# ==========================================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='section-title'>📖 Lesson / Topic Discussed</div>",
    unsafe_allow_html=True
)

topics_dict = {

    "Select Grade Level":[
        "Please select a Grade Level first."
    ],

    "Grade 7":[
        "Conflict (Character vs. Character/Society/Nature)",
        "Structural Elements & Devices",
        "Contextual Analysis",
        "Core Meaning",
        "Composition Process",
        "Final Output (Original Poem or Prose)"
    ],

    "Grade 8":[
        "Conflict (Character vs. Self/Character/Society/Nature)",
        "Structural Elements & Devices",
        "Contextual Analysis",
        "Core Meaning",
        "Composition Process",
        "Final Output (Original Poem or Prose)"
    ],

    "Grade 9":[
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

    "Grade 10":[
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

    topics_dict[grade_level],

    horizontal=False

)

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ==========================================================
# CLASSROOM EXPERIENCE
# ==========================================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='section-title'>💡 Classroom Experience</div>",
    unsafe_allow_html=True
)

st.info(
    "✅ Select all statements that describe your classroom experience."
)

# --------------------------
# Best Teaching Practices
# --------------------------

best_practices = st.multiselect(

    "🌟 Best Teaching Practices",

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

        "Kept students engaged",

        "Helped with difficult concepts",

        "Reviewed the lesson before dismissal"

    ]

)

st.write("")

# --------------------------
# Positive Behaviour
# --------------------------

positive_feedback = st.multiselect(

    "❤️ Positive Teacher Behaviour",

    [

        "Kind and approachable",

        "Treats everyone fairly",

        "Respectful to all students",

        "Patient while teaching",

        "Friendly and welcoming",

        "Listens to student concerns",

        "Encourages students",

        "Calm and professional",

        "Well prepared",

        "Comes to class on time",

        "Shows enthusiasm",

        "Creates a safe classroom",

        "Values student opinions",

        "Good role model",

        "Shows care and concern"

    ]

)

# ----------------------------------------------------
# QUICK RATING
# ----------------------------------------------------

st.write("")

st.markdown("### 😊 How enjoyable was today's class?")

quick_rating = st.radio(

    "",

    [

        "😞 Poor",

        "😐 Fair",

        "🙂 Good",

        "😄 Very Good",

        "🤩 Excellent"

    ],

    horizontal=True

)

st.markdown("</div>", unsafe_allow_html=True)

st.write("")
# ==========================================================
# STEP 3
# ==========================================================

st.progress(0.75, text="Step 3 of 4 • Suggestions & Overall Rating")

st.write("")

# ==========================================================
# SUGGESTIONS
# ==========================================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='section-title'>🚀 Help Us Improve</div>",
    unsafe_allow_html=True
)

st.info(
    "Your suggestions will help teachers improve future lessons."
)

col1, col2 = st.columns(2)

# -------------------------------------------------
# Lesson Suggestions
# -------------------------------------------------

with col1:

    suggestions = st.multiselect(

        "📚 Suggestions for the Lesson",

        [

            "Encourage more student participation",

            "Give more time to answer questions",

            "Use more interactive activities",

            "Include more group activities",

            "Use more real-life examples",

            "Ask more higher-order questions",

            "Check understanding more often",

            "Use more technology",

            "Give more opportunities to share ideas",

            "Provide reflection before dismissal"

        ]

    )

# -------------------------------------------------
# Teacher Interaction
# -------------------------------------------------

with col2:

    improvements = st.multiselect(

        "👨‍🏫 Suggestions for Teacher Interaction",

        [

            "Be more approachable",

            "Encourage quieter students",

            "Give equal attention to everyone",

            "Provide more encouragement",

            "Listen more to student concerns",

            "Speak more clearly",

            "Interact more during activities",

            "Be more patient",

            "Create more opportunities for expression",

            "Maintain a respectful classroom"

        ]

    )

st.write("")

# -------------------------------------------------
# Additional Comment
# -------------------------------------------------

comment = st.text_area(

    "💬 Additional Comment (Optional)",

    placeholder="Write any additional feedback or suggestions here..."

)

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ==========================================================
# OVERALL RATING
# ==========================================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='section-title'>⭐ Overall Evaluation</div>",
    unsafe_allow_html=True
)

st.write("### Overall Rating")

rating = st.slider(

    "Move the slider",

    min_value=1,

    max_value=10,

    value=10,

    help="10 = Excellent"

)

# Rating message

if rating >= 9:

    st.success("🌟 Excellent! Thank you for recognizing quality teaching.")

elif rating >= 7:

    st.info("😊 Thank you! We're glad you had a positive learning experience.")

elif rating >= 5:

    st.warning("🙂 Thank you. We'll continue improving.")

else:

    st.error("💙 Thank you for your honesty. Your feedback will help us improve.")

st.write("")

# ==========================================================
# REVIEW BEFORE SUBMITTING
# ==========================================================

with st.expander("📋 Review Your Responses Before Submitting"):

    st.markdown(f"**Grade Level:** {grade_level}")

    st.markdown(f"**Section:** {section}")

    st.markdown(f"**Teacher:** {teacher}")

    st.markdown(f"**Subject:** {subject}")

    st.markdown(f"**Term:** {term}")

    st.markdown(f"**Lesson:** {topic}")

    st.markdown(f"**Overall Rating:** ⭐ {rating}/10")

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ==========================================================
# SUBMIT SECTION
# ==========================================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='section-title'>✅ Submit Feedback</div>",
    unsafe_allow_html=True
)

st.caption(
    "Please review your responses carefully before clicking Submit."
)

submit = st.button(

    "🚀 Submit My Feedback",

    use_container_width=True

)

st.markdown("</div>", unsafe_allow_html=True)

st.write("")
# ==========================================================
# STEP 4
# ==========================================================

st.progress(1.0, text="Step 4 of 4 • Ready to Submit")

if submit:

    # ---------------------------------------
    # VALIDATION
    # ---------------------------------------

    if (
        grade_level == "Select Grade Level"
        or section == "Select a section"
        or term == "Select a term"
        or teacher == "Select a teacher"
    ):

        st.error("⚠ Please complete all required fields before submitting.")

    else:

        row_data = {

            "data":[{

                "Timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

                "Grade Level":grade_level,

                "Section":section,

                "Subject":subject,

                "Term":term,

                "Teacher":teacher,

                "Topic":topic,

                "Best Practices":", ".join(best_practices),

                "Positive Feedback":", ".join(positive_feedback),

                "Suggestions":", ".join(suggestions),

                "Improvements":", ".join(improvements),

                "Additional Comment":comment,

                "Quick Rating":quick_rating,

                "Rating":rating

            }]

        }

        sheetdb_url = "https://sheetdb.io/api/v1/0kfovvs2st6yz"

        with st.spinner("Submitting your feedback..."):

            try:

                response = requests.post(
                    sheetdb_url,
                    json=row_data,
                    timeout=15
                )

                if response.status_code == 201:

                    st.balloons()

                    st.success("🎉 Feedback submitted successfully!")

                    st.markdown("---")

                    st.markdown(
                        """
                        # 💙 Thank You!

                        Your feedback has been recorded successfully.

                        Your responses help our teachers improve their classroom instruction.

                        We appreciate your honesty and participation.
                        """
                    )

                    st.info(
                        "You may now safely close this page."
                    )

                else:

                    st.error(
                        "Unable to save your feedback.\n\nPlease try again."
                    )

            except requests.exceptions.Timeout:

                st.error(
                    "⏰ The server took too long to respond."
                )

            except requests.exceptions.ConnectionError:

                st.error(
                    "📡 Unable to connect to the internet."
                )

            except Exception as e:

                st.error(f"Unexpected error:\n{e}")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
"""
<hr>

<div style='text-align:center;color:#64748b;font-size:15px;'>

<b>Student Feedback System</b><br>

President Carlos P. Garcia Technical Vocational School of Fisheries and Arts

<br><br>

Developed by

<b>Mr. Abraham C. Gaviola</b>

<br>

English Teacher III

<br><br>

© 2026 All Rights Reserved

</div>
""",
unsafe_allow_html=True
)
