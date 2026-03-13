# BuildSpark

BuildSpark is an AI-powered woodworking and DIY build planner.

It helps turn a rough project idea into a clearer build plan based on skill level, environment, materials, tools, budget, and size constraints.

## Current Version

**V3 – Polished Public Release**

This version focuses on presentation, usability, and portfolio readiness.

## Features

- AI-generated woodworking and DIY build plans
- Structured output with five clear sections
- Starter project templates
- Cleaner public-facing interface
- Saved plans page
- Print / save as PDF support
- Local fallback plan generation if AI output fails

## Output Sections

BuildSpark generates:

- Concept Breakdown
- Materials List
- Step-by-Step Build Logic
- Constraints & Variations
- Missing Items + Leftovers

## Tech Stack

- Python
- Flask
- HTML
- CSS
- OpenAI API
- python-dotenv

## Run Locally

```bash
git clone https://github.com/GoFinkle/BuildSpark.git
cd BuildSpark
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
