# ShikshaAI – Multilingual AI Lesson Assistant for School Teachers

## 🚀 Overview

ShikshaAI is a cloud-deployed AI agent built using **Google ADK** and powered by a **Gemini model**.

It generates structured classroom-ready teaching modules for school teachers (Grades 1–10) in English or Hindi.

The agent performs one clearly defined task:

> Generate a teaching module including explanation, classroom activity, and exactly three homework questions based on subject, grade, and topic.

The system is deployed on **Google Cloud Run** and accessible via a public HTTP endpoint.

---

## 🎯 Problem Statement

School teachers spend significant time preparing structured lesson explanations, activities, and homework aligned to grade levels.

In multilingual classrooms, the effort increases as teachers often need content in both English and Hindi.

ShikshaAI reduces preparation time by generating classroom-ready teaching modules instantly while maintaining grade-appropriate complexity.

---

## 💡 Solution

The AI agent:

* Accepts subject, grade (1–10), topic, and language
* Validates input
* Generates:

  * Concept explanation
  * One classroom activity (discussion-based or hands-on)
  * Exactly three homework questions
* Responds entirely in the requested language

---

## 🏗 Architecture

```
Client (HTTP POST)
        ↓
Cloud Run (FastAPI)
        ↓
ADK LlmAgent
        ↓
Gemini Model (gemini-1.5-flash)
        ↓
Generated Lesson Module
```

### Tech Stack

* FastAPI (API layer)
* Google ADK (Agent framework)
* Gemini 1.5 Flash (LLM backend)
* Docker (Containerization)
* Google Cloud Run (Deployment)

---

## 📡 API Endpoint

### POST /generate-lesson

### Request Body

```json
{
  "subject": "Science",
  "grade": 5,
  "topic": "Evaporation",
  "language": "English"
}
```

### Validation Rules

* Grade must be between 1 and 10
* Subject cannot be empty
* Topic cannot be empty
* Language defaults to English if not provided

---

## 📤 Sample Response

```json
{
  "status": "success",
  "lesson": "Explanation: ...\n\nClassroom Activity: ...\n\nHomework:\n1. ...\n2. ...\n3. ..."
}
```

The output includes:

1. Grade-appropriate explanation
2. One classroom activity
3. Exactly three homework questions

---

## ☁ Deployment

The service is deployed on Google Cloud Run.

Public Endpoint:

```
https://YOUR_CLOUD_RUN_URL
```

---

## 🔐 Environment Variables

The following environment variable must be set in Cloud Run:

```
GEMINI_API_KEY=your_api_key_here
```

The API key is never hardcoded and is securely injected via environment configuration.

---

## 🐳 Local Development

Install dependencies:

```
pip install -r requirements.txt
```

Run locally:

```
uvicorn app.main:app --reload
```

Test endpoint:

```
POST http://127.0.0.1:8000/generate-lesson
```

---

## 📈 Business Impact

ShikshaAI:

* Reduces lesson preparation time
* Standardizes instructional quality
* Supports multilingual classrooms
* Scales to public and private schools
* Can integrate with EdTech platforms

---

## 🔮 Future Roadmap

* Additional regional language support
* Curriculum alignment per national standards
* Integration with Learning Management Systems
* SaaS subscription model for schools

---

## 🧠 Built With

* Google ADK
* Gemini Model
* FastAPI
* Google Cloud Platform

---
