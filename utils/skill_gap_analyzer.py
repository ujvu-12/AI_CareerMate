def skill_gap(resume_skills, jd_skills):
    matched = [s for s in jd_skills if s in resume_skills]
    missing = [s for s in jd_skills if s not in resume_skills]
    return matched, missing
