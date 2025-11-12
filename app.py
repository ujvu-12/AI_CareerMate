<<<<<<< HEAD
import streamlit as st
from utils.resume_parser import extract_text
from utils.jd_parser import get_jd_text
from utils.skill_extractor import extract_skills
from utils.skill_gap_analyzer import skill_gap
from utils.ats_checker import ats_score, ats_feedback
from utils.roadmap_generator import learning_roadmap
from utils.job_recommender import recommend_roles
import plotly.express as px

st.set_page_config(page_title="AI CareerMate", page_icon="🤖", layout="wide")

st.title("🤖 AI CareerMate – Smart Resume & Career Advisor")

resume = st.file_uploader("📄 Upload your Resume", type=['pdf', 'docx'])
jd_text = st.text_area("🧾 Paste Job Description")

if resume and jd_text:
    with st.spinner("Analyzing your resume..."):
        resume_text = extract_text(resume)
        jd_clean = get_jd_text(jd_text)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_clean)
        matched, missing = skill_gap(resume_skills, jd_skills)
        score = ats_score(resume_text, jd_skills)
        feedback = ats_feedback(score)
        roadmap = learning_roadmap(missing)
        roles = recommend_roles(resume_skills)

    st.success("✅ Analysis Complete!")

    st.subheader("🎯 ATS Score")
    st.progress(score / 100)
    st.write(f"**Score:** {score}% — {feedback}")

    st.subheader("✅ Matched Skills")
    st.write(", ".join(matched) if matched else "None")

    st.subheader("❌ Missing Skills")
    st.write(", ".join(missing) if missing else "Perfect match!")

    st.subheader("📘 Learning Roadmap")
    st.json(roadmap)

    st.subheader("💼 Suggested Job Roles")
    st.dataframe(roles)

    # Visualization
    fig = px.bar(roles, x='job_role', y='score', color='job_role', title="Job Role Fit Score")
    st.plotly_chart(fig, use_container_width=True)
=======
import streamlit as st
from utils.resume_parser import extract_text
from utils.jd_parser import get_jd_text
from utils.skill_extractor import extract_skills
from utils.skill_gap_analyzer import skill_gap
from utils.ats_checker import ats_score, ats_feedback
from utils.roadmap_generator import learning_roadmap
from utils.job_recommender import recommend_roles
import plotly.express as px

st.set_page_config(page_title="AI CareerMate", page_icon="🤖", layout="wide")

st.title("🤖 AI CareerMate – Smart Resume & Career Advisor")

resume = st.file_uploader("📄 Upload your Resume", type=['pdf', 'docx'])
jd_text = st.text_area("🧾 Paste Job Description")

if resume and jd_text:
    with st.spinner("Analyzing your resume..."):
        resume_text = extract_text(resume)
        jd_clean = get_jd_text(jd_text)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_clean)
        matched, missing = skill_gap(resume_skills, jd_skills)
        score = ats_score(resume_text, jd_skills)
        feedback = ats_feedback(score)
        roadmap = learning_roadmap(missing)
        roles = recommend_roles(resume_skills)

    st.success("✅ Analysis Complete!")

    st.subheader("🎯 ATS Score")
    st.progress(score / 100)
    st.write(f"**Score:** {score}% — {feedback}")

    st.subheader("✅ Matched Skills")
    st.write(", ".join(matched) if matched else "None")

    st.subheader("❌ Missing Skills")
    st.write(", ".join(missing) if missing else "Perfect match!")

    st.subheader("📘 Learning Roadmap")
    st.json(roadmap)

    st.subheader("💼 Suggested Job Roles")
    st.dataframe(roles)

    # Visualization
    fig = px.bar(roles, x='job_role', y='score', color='job_role', title="Job Role Fit Score")
    st.plotly_chart(fig, use_container_width=True)
>>>>>>> 7c061ee44d80838da119ee5ebd8bef2d30655ef0
