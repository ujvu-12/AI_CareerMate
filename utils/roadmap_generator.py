def learning_roadmap(missing_skills):
    roadmap = {}
    for s in missing_skills:
        roadmap[s] = [
            f"Step 1: Watch a beginner YouTube tutorial on {s}",
            f"Step 2: Build a small project using {s}",
            f"Step 3: Add this project to your resume."
        ]
    return roadmap
