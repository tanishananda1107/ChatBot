# ChatBot
# AI Robotics QA Uploader

This project uploads structured question-answer (QA) pairs from an Excel spreadsheet to a Firebase Realtime Database. It's designed for use in AI and Robotics education, chatbot backends, or quiz systems.

## Features

- Upload Q&A pairs from Excel (.xlsx)
- Cleans and validates missing data
- Authenticates securely with Firebase using a service account
- Stores QA pairs under a single database node
- Sanitizes Firebase keys to be safe (e.g., replaces slashes, dots)

## Project Structure

ai-robotics-qa/
├── main.py # Main Python script to execute
├── ai_robotics_qa.xlsx # Excel file with question/answer pairs
├── .env # Environment variables (do not commit)## ⚙️ Requirements

## Requirements
- Python 3.8 or later
- Firebase Realtime Database
- Firebase service account JSON
- Excel file with 'question' and 'answer' columns

## Firebase Setup
1. Go to Firebase Console:
   - Navigate to Project Settings → Service Accounts
   - Click "Generate new private key"
   - Download and save the `.json` credentials file

2. Place the JSON file in your project folder.

3. Create a .env file with the following content:
FIREBASE_URL=https://your-project-id.firebaseio.com/
SERVICE_ACCOUNT=qa-service-account.json

## Excel File Format

Ensure your Excel file contains the following columns:

| question                       | answer                          |
|--------------------------------|----------------------------------|
| What is AI?                    | Artificial Intelligence...       |
| What does a sensor do?         | It detects physical input...     |

Use .xlsx format and column names: question and answer (lowercase or mixed-case is OK).

## Setup Instructions (Windows/Mac/Linux)

1. Clone the repo

```bash
git clone https://github.com/your-username/ai-robotics-qa.git
cd ai-robotics-qa
