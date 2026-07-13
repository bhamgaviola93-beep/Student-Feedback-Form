import streamlit as st

# Custom title and introduction
st.title("📝 Student Feedback Form")
st.write("Your feedback helps us improve. Please answer the short questions below.")

# 1. Course Selection
course = st.selectbox(
    "Select your course:",
    ["Select an option", "Introduction to Python", "Web Development 101", "Data Science Basics"]
)

# 2. Rating Scale
rating = st.slider("How would you rate this course overall?", 1, 5, 3)

# 3. Text Feedback
feedback = st.text_area("What did you like or dislike? How can we improve?")

# 4. Submit Button
if st.button("Submit Feedback"):
    if course == "Select an option":
        st.error("Please select a course before submitting.")
    else:
        st.success("Thank you! Your text feedback has been received.")
        # Tip: You can connect this to a Google Sheet later to save responses!
