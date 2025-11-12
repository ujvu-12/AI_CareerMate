🧠 AI CareerMate — Your Smart Resume & Career Assistant

AI CareerMate helps users improve their resumes and find the right career path using Artificial Intelligence.
It analyzes resumes against job descriptions, checks ATS (Applicant Tracking System) compatibility, identifies missing skills, and generates a personalized roadmap to help users become job-ready.

🚀 Features

✅ Resume & JD Analysis – Upload your resume and a job description to get instant keyword and skill match insights.

✅ ATS Score Evaluation – Estimates the resume’s ATS score and provides suggestions for improvement.

✅ Skill Gap Detection – Highlights the technical and soft skills missing for the target job role.

✅ Smart Roadmap Generator – Builds a personalized learning path to help users bridge skill gaps.

✅ Job Role Recommendations – Suggests the most suitable career roles based on the user’s resume.

✅ Interactive Dashboard (optional frontend feature) – Visualizes skills, match scores, and progress over time.


⚙️ Tech Stack

Languages & Frameworks


Python (Flask / FastAPI)


HTML, CSS, JavaScript


Libraries & Tools


spacy, nltk, transformers – Natural Language Processing

pandas, numpy, scikit-learn – Data and ML operations

joblib, pickle – Model handling and persistence


OpenAI API / Hugging Face models


🧩 Project Structure
AI_CareerMate/
│
├── app.py                     # Main backend application
├── requirements.txt            # Dependencies
│
├── data/
│   ├── job_roles.csv
│   └── skills_list.json
│
├── models/
│   └── (trained models / saved weights)
│
├── utils/
│   ├── resume_parser.py
│   ├── jd_parser.py
│   ├── ats_checker.py
│   ├── skill_extractor.py
│   ├── skill_gap_analyzer.py
│   ├── roadmap_generator.py
│   └── job_recommender.py
│
├── assets/
│   └── (UI images / icons / design files)
│
└── README.md


🧰 Setup Instructions


Clone the repository


git clone https://github.com/ujvu-12/AI_CareerMate.git
cd AI_CareerMate



Create and activate a virtual environment


python -m venv venv
venv\Scripts\activate



Install dependencies


pip install -r requirements.txt



Run the application


python app.py



Open your browser at
👉 http://127.0.0.1:5000/


🎯 Future Enhancements


Integrate AI-powered resume rewriting using OpenAI or Gemini APIs.

Add real-time feedback for resume improvements.

Deploy the system publicly (Render / AWS / Hugging Face Spaces).

Implement user authentication and personalized dashboards.


👥 Contributors

Ujvwala Reddy P	@ujvu-12

Nidhi Tiwari S	@nidhi-ai01


🧾 License


This project is licensed under the MIT License.
See the LICENSE
 file for details.

⭐ Support

If you like this project, please star ⭐ the repository and share it with others interested in AI-powered career tools!
