# Vedaz AI Engineer Assignment

## Overview

This project was developed as part of the Vedaz AI Engineer technical assignment.

It includes:

- Chat Checker
- Chat Generator
- Quality Tester

---

## Project Structure

```
.
├── checker.py
├── generator.py
├── tester.py
├── generated_chats.jsonl
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Task 1 - Chat Checker

Features:

- Validates JSON chat structure
- Counts words in each chat
- Detects duplicate and near-duplicate chats
- Splits chats into training and test sets
- Detects unsafe astrology responses

---

## Task 2 - Chat Generator

Features:

- Uses Google Gemini API
- Generates astrology conversations
- Produces valid JSONL output
- Automatically validates chats using checker.py
- Saves only valid chats

---

## Task 3 - Quality Tester

Features:

- Accepts user questions
- Sends questions to Gemini
- Displays assistant responses
- Performs simple quality checks for safety, helpfulness, and astrology relevance

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variable

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key
```

---

## Run

Checker

```bash
python checker.py
```

Generator

```bash
python generator.py
```

Tester

```bash
python tester.py
```

---

## Libraries Used

- google-genai
- python-dotenv
- rapidfuzz
- scikit-learn

---

## Notes

The project uses the Gemini API. If the free API quota is exceeded, the scripts may temporarily return a 429 RESOURCE_EXHAUSTED error until the quota resets.