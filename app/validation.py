from pydantic import BaseModel, Field

class LessonRequest(BaseModel):
    subject: str
    grade: int = Field(..., ge=1, le=10)
    topic: str
    language: str = "English"

    def validate_fields(self):
        if not self.subject.strip():
            raise ValueError("Subject cannot be empty.")
        if not self.topic.strip():
            raise ValueError("Topic cannot be empty.")