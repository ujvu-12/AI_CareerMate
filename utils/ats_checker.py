def ats_score(resume_text, jd_skills):
    score = 0
    for skill in jd_skills:
        if skill.lower() in resume_text.lower():
            score += 1
    return round((score / len(jd_skills)) * 100, 2)

def ats_feedback(score):
    if score > 80:
        return "Excellent match! Minor keyword tweaks only."
    elif score > 60:
        return "Good match. Add more relevant keywords."
    else:
        return "Low ATS score — strengthen skill coverage."
