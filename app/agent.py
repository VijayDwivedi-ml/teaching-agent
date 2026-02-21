from google.adk.agents import LlmAgent
from google.adk.models import Gemini
from app.config import GEMINI_API_KEY

# Configure Gemini model through ADK
model = Gemini(
    model="gemini-1.5-flash",
    api_key=GEMINI_API_KEY
)

# Define ADK Agent
lesson_agent = LlmAgent(
    name="shikshaai_lesson_agent",
    model=model,
    instruction="""
You are an experienced school teacher.

Your task is to generate a classroom-ready teaching module.

The module must include:
1. A clear, age-appropriate explanation.
2. One classroom activity (discussion-based or hands-on).
3. Exactly three homework questions.

Rules:
- Adapt explanation complexity based on grade level (1–10).
- Ensure output is fully in the requested language.
- Use clear section headings:
  Explanation
  Classroom Activity
  Homework
- Provide exactly three homework questions.
- Do not include extra sections.
"""
)

def generate_lesson(subject: str, grade: int, topic: str, language: str):

    user_prompt = f"""
Subject: {subject}
Grade: {grade}
Topic: {topic}
Language: {language}
"""

    response = lesson_agent.run(user_prompt)

    return response.text