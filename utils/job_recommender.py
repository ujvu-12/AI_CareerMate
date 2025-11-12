import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

roles = pd.read_csv("data/job_roles.csv")

def recommend_roles(resume_skills):
    vectorizer = CountVectorizer().fit_transform(
        [', '.join(resume_skills)] + list(roles['skills'])
    )
    similarities = cosine_similarity(vectorizer[0:1], vectorizer[1:]).flatten()
    roles['score'] = similarities
    return roles.sort_values('score', ascending=False).head(3)[['job_role', 'score']]
