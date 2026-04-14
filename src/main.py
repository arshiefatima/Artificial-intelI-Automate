# 🤖 AI Resume Analyzer (Advanced Version)

def analyze_resume(resume_text, job_role):
    resume_text = resume_text.lower()
    job_role = job_role.lower()

    # Skill database (simulating RAG knowledge base)
    job_skills = {
        "data scientist": ["python", "machine learning", "statistics", "sql"],
        "software engineer": ["python", "java", "algorithms", "git"],
        "qa engineer": ["testing", "automation", "selenium", "api"]
    }

    detected_skills = []
    missing_skills = []

    if job_role in job_skills:
        for skill in job_skills[job_role]:
            if skill in resume_text:
                detected_skills.append(skill)
            else:
                missing_skills.append(skill)

    # Smart feedback (LLM-style simulation)
    feedback = []

    if detected_skills:
        feedback.append(f"Good: You have relevant skills: {detected_skills}")

    if missing_skills:
        feedback.append(f"Improve: Add missing skills: {missing_skills}")

    if "project" not in resume_text:
        feedback.append("Add project experience to strengthen your profile")

    return detected_skills, missing_skills, feedback


if __name__ == "__main__":
    print("📄 AI Resume Analyzer (Advanced)")

    resume = input("Paste your resume: ")
    role = input("Enter job role (Data Scientist / Software Engineer / QA Engineer): ")

    detected, missing, feedback = analyze_resume(resume, role)

    print("\n✅ Detected Skills:", detected)
    print("❌ Missing Skills:", missing)

    print("\n💡 AI Feedback:")
    for f in feedback:
        print("-", f)
