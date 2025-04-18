import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Recommendation Engine",
    page_icon="✨",
    layout="wide",
)

# Sidebar for briefs
st.sidebar.title("Briefs")
selected_brief = st.sidebar.radio("Select a brief:", ["Brief 1", "Brief 2"])

# Main content
st.title("Recommendation Engine")
st.write("Welcome to the profile/mission recommendation engine for a tech consulting company.")

# Sample data for briefs
briefs = {
    "Brief 1": {
        "description": "We are looking for a senior backend developer with expertise in Python and Django.",
        "profiles": [
            {"name": "Alice Dupont", "seniority": "Senior", "skills": ["Python", "Django"], "availability": "May 2025", "wishes": "Remote"},
            {"name": "Bob Martin", "seniority": "Mid-level", "skills": ["Python", "Flask"], "availability": "June 2025", "wishes": "Full-time"},
        ],
    },
    "Brief 2": {
        "description": "We need a data scientist with skills in machine learning and data visualization.",
        "profiles": [
            {"name": "Charlie Durand", "seniority": "Senior", "skills": ["Machine Learning", "Data Visualization"], "availability": "April 2025", "wishes": "Innovative projects"},
            {"name": "Diane Leroy", "seniority": "Junior", "skills": ["Python", "Pandas"], "availability": "May 2025", "wishes": "Continuous learning"},
        ],
    },
}

# Display the summary of the selected brief
if selected_brief:
    brief = briefs[selected_brief]
    st.subheader(f"Summary of {selected_brief}")
    st.write(brief["description"])

    # Display profile recommendations
    st.subheader("Profile Recommendations")
    for profile in brief["profiles"]:
        st.markdown(f"**Name:** {profile['name']}")
        st.markdown(f"**Seniority:** {profile['seniority']}")
        st.markdown(f"**Skills:** {', '.join(profile['skills'])}")
        st.markdown(f"**Availability:** {profile['availability']}")
        st.markdown(f"**Wishes:** {profile['wishes']}")
        st.markdown("---")