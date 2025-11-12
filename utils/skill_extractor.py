import json, spacy
from keybert import KeyBERT

nlp = spacy.load('en_core_web_sm')
kw_model = KeyBERT()

with open('data/skills_list.json') as f:
    SKILLS = json.load(f)

def extract_skills(text):
    text_lower = text.lower()
    found = [s for s in SKILLS if s.lower() in text_lower]
    return list(set(found))
