from fastapi import FastAPI, HTTPException
from app.validation import LessonRequest
from app.agent import generate_lesson

app = FastAPI(title="ShikshaAI - Multilingual Lesson Assistant")

@app.post("/generate-lesson")
async def create_lesson(request: LessonRequest):
    try:
        request.validate_fields()

        lesson_content = generate_lesson(
            subject=request.subject,
            grade=request.grade,
            topic=request.topic,
            language=request.language
        )

        return {
            "status": "success",
            "lesson": lesson_content
        }

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")