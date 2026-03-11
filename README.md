# BuildSpark

BuildSpark is an AI-powered woodworking and DIY build planner that turns a simple project idea into a structured build plan.

Users enter a build idea, skill level, environment, available materials, tools, budget, and size constraints. BuildSpark then generates a practical plan with:
- a concept breakdown
- a materials list
- step-by-step build logic
- constraints and variations
- missing items and likely leftovers

## Version

**Current version:** V1

BuildSpark V1 is a working local prototype with a simple one-page interface and OpenAI-powered plan generation.

## Features

- Simple form-based input
- AI-generated woodworking and DIY build plans
- Structured 5-section output
- Clean one-page layout
- Preserves form values after submit
- Basic loading-state button behavior
- Local fallback logic if AI response fails

## Tech Stack

- Python
- Flask
- HTML
- CSS
- OpenAI API
- python-dotenv

## Project Structure

```text
BuildSpark/
├── app.py
├── requirements.txt
├── .gitignore
└── templates/
    └── index.html
How It Works

The user enters a build idea and project constraints.

Flask receives the form submission.

The app sends the request to OpenAI.

The model returns a structured JSON response.

The page displays the build plan in five sections.

Setup
1. Clone the repository
git clone https://github.com/GoFinkle/BuildSpark.git
cd BuildSpark
2. Create and activate a virtual environment
Windows
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Create a .env file

Create a file named .env in the project root and add:

OPENAI_API_KEY=your_openai_api_key_here
5. Run the app
python app.py

Then open:

http://127.0.0.1:5000
Example Use Cases

Planning a small wall shelf

Generating a simple sawhorse build

Sketching out a beginner storage box project

Turning rough leftover-material ideas into more structured builds

Current Scope of V1

BuildSpark V1 is intentionally lean. It focuses on:

one-page usability

simple project input

structured AI output

local prototype functionality

It does not yet include:

user accounts

saved history

PDF export

deployment

advanced material optimization

diagrams or build drawings

Future Ideas

Possible future versions may include:

export to PDF

project save/history

improved prompt reliability

cost estimation

material optimization

downloadable cut lists

deployment as a live web app

Notes

This project is an early functional prototype built to validate the concept quickly and keep the scope tight.

Author

Built by GoFinkle.


Then do:

```bash
git add README.md
git commit -m "Add README for BuildSpark V1"
git push

Tiny correction: if you do not already have a README.md, create a new file with that exact name first.

Perfect. Paste this directly into the README box:

# BuildSpark

BuildSpark is an AI-powered woodworking and DIY build planner that turns a simple project idea into a structured build plan.

Users enter a build idea, skill level, environment, available materials, tools, budget, and size constraints. BuildSpark then generates a practical plan with:
- a concept breakdown
- a materials list
- step-by-step build logic
- constraints and variations
- missing items and likely leftovers

## Version

**Current version:** V1

BuildSpark V1 is a working local prototype with a simple one-page interface and OpenAI-powered plan generation.

## Features

- Simple form-based input
- AI-generated woodworking and DIY build plans
- Structured 5-section output
- Clean one-page layout
- Preserves form values after submit
- Basic loading-state button behavior
- Local fallback logic if AI response fails

## Tech Stack

- Python
- Flask
- HTML
- CSS
- OpenAI API
- python-dotenv

## Project Structure

```text
BuildSpark/
├── app.py
├── requirements.txt
├── .gitignore
└── templates/
    └── index.html
How It Works

The user enters a build idea and project constraints.

Flask receives the form submission.

The app sends the request to OpenAI.

The model returns a structured JSON response.

The page displays the build plan in five sections.

Setup
1. Clone the repository
git clone https://github.com/GoFinkle/BuildSpark.git
cd BuildSpark
2. Create and activate a virtual environment
Windows
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Create a .env file

Create a file named .env in the project root and add:

OPENAI_API_KEY=your_openai_api_key_here
5. Run the app
python app.py

Then open:

http://127.0.0.1:5000
Example Use Cases

Planning a small wall shelf

Generating a simple sawhorse build

Sketching out a beginner storage box project

Turning rough leftover-material ideas into more structured builds

Current Scope of V1

BuildSpark V1 is intentionally lean. It focuses on:

one-page usability

simple project input

structured AI output

local prototype functionality

It does not yet include:

user accounts

saved history

PDF export

deployment

advanced material optimization

diagrams or build drawings

Future Ideas

Possible future versions may include:

export to PDF

project save/history

improved prompt reliability

cost estimation

material optimization

downloadable cut lists

deployment as a live web app

Notes

This project is an early functional prototype built to validate the concept quickly and keep the scope tight.

Author

Built by GoFinkle.
