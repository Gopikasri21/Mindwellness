import streamlit as st

st.set_page_config(page_title="Mind Wellness", layout="wide")

# Background image
page_bg = """
<style>

[data-testid="stAppViewContainer"]{
background-image:url("https://images.unsplash.com/photo-1501785888041-af3ef285b470");
background-size:cover;
background-position:center;
background-attachment:fixed;
}

.block-container{
background:rgba(0,0,0,0.55);
padding:40px;
border-radius:15px;
color:white;
}

</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ☰ Sidebar menu
page = st.sidebar.radio(
"Navigation",
["Home","Activities","Tips","Contact"]
)

# ---------------- HOME ----------------

if page == "Home":

    st.title("Mind Wellness 🌿")

    st.write("""
Mind wellness means having a calm, balanced and healthy mind.  
When our mind is healthy we can think clearly, manage emotions and 
handle daily life challenges better.

In today's busy world people face stress because of studies, work 
and responsibilities. Practicing mind wellness helps us stay calm, 
focused and positive.

Simple habits like meditation, good sleep, exercise and spending 
time with family help improve our mental health.
""")

    st.subheader("Benefits of Mind Wellness")

    st.write("""
• Reduces stress and anxiety  
• Improves focus and concentration  
• Builds emotional strength  
• Improves relationships  
• Creates a happier life
""")

# ---------------- ACTIVITIES ----------------

elif page == "Activities":

    st.title("Mental Health Activities")

    st.write("""
• Deep Breathing – Calms the mind and reduces stress  

• Listening to Music – Improves mood  

• Nature Walk – Refreshes the brain  

• Writing a Journal – Helps express feelings  

• Reading Books – Improves focus
""")
    
    st.subheader("Ask a Question")

    question = st.text_input("Ask about activities")

    if question:
        st.success("Mental health activities like meditation, music, journaling and nature walks help maintain a peaceful mind.")

# ---------------- TIPS ----------------

elif page == "Tips":

    st.title("Tips for Mind Wellness")

    st.write("""
• Meditation and Yoga – Calm the mind and reduce anxiety  

• Proper Sleep – Helps the brain rest and improves focus  

• Positive Thinking – Builds confidence and mental strength  

• Exercise Daily – Improves mood  

• Spend Time with Family – Improves emotional health
""")

    st.subheader("Ask a Question")

    question = st.text_input("Ask about mind wellness")

    if question:
        st.success("Following healthy habits like meditation, exercise and positive thinking improves mental health.")

# ---------------- CONTACT ----------------

elif page == "Contact":

    st.title("Contact / Feedback")

    name = st.text_input("Name")
    email = st.text_input("Email")
    feedback = st.text_area("Your Feedback")

    if st.button("Submit"):
        st.success("Your feedback has been submitted successfully!")