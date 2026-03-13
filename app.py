from flask import Flask, render_template, request, url_for, redirect
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import uuid

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PLANS_FILE = "saved_plans.json"


def load_saved_plans():
    if not os.path.exists(PLANS_FILE):
        return []

    try:
        with open(PLANS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_plan_entry(entry):
    plans = load_saved_plans()
    plans.insert(0, entry)

    with open(PLANS_FILE, "w", encoding="utf-8") as f:
        json.dump(plans, f, indent=2, ensure_ascii=False)



def parse_list(text):
    if not text.strip():
        return []
    return [item.strip() for item in text.split(",") if item.strip()]


def local_fallback_plan(idea, skill, environment, materials, tools, budget, size):
    materials_on_hand = parse_list(materials)
    tools_on_hand = parse_list(tools)

    materials_lines = [
        "Suggested materials:",
        "- wood stock",
        "- screws",
        "- wood glue",
        "- sandpaper",
        "",
        "Materials on hand:"
    ]

    if materials_on_hand:
        for item in materials_on_hand:
            materials_lines.append(f"- {item}")
    else:
        materials_lines.append("- None provided")

    materials_lines.append("")
    materials_lines.append(f"Budget target: {budget}" if budget else "Budget target: Not provided")

    return {
        "concept_breakdown": (
            f"This project is a {idea} intended for {environment.lower()} use. "
            f"It is being planned around a {skill.lower()} skill level, with the goal of keeping the build practical, realistic, and achievable."
        ),
        "materials_list": "\n".join(materials_lines),
        "step_by_step": "\n".join([
            f"1. Review the {idea} idea and sketch a simple layout.",
            "2. Measure the space and confirm dimensions.",
            "3. Sort available materials and tools.",
            "4. Mark and cut the main pieces.",
            "5. Dry-fit before final assembly.",
            "6. Assemble with the simplest strong method.",
            "7. Check for strength, fit, and finish."
        ]),
        "constraints_variations": "\n".join([
            f"- Skill level: {skill}",
            f"- Environment: {environment}",
            f"- Size constraints: {size if size else 'None provided'}",
            f"- Tools on hand: {', '.join(tools_on_hand) if tools_on_hand else 'None provided'}",
            "- Variation idea: simplify the design if tools or materials are limited."
        ]),
        "missing_leftovers": "\n".join([
            "Missing items:",
            "- Final missing items depend on exact dimensions and joinery.",
            "",
            "Possible leftovers:",
            "- Scrap wood offcuts",
            "- Extra screws",
            "- Small trim pieces"
        ])
    }

def generate_buildspark_plan(idea, skill, environment, materials, tools, budget, size, refine):
    prompt = f"""
You are BuildSpark, an AI woodworking and DIY build planner.

Your job is to create a build plan that MATCHES the user's build idea exactly.
Do not change the project into a different object.
If the user asks for a shelf, do not turn it into a box.
If the user asks for a sawhorse, do not turn it into a bench.

Return ONLY valid JSON with exactly these keys:
concept_breakdown
materials_list
step_by_step
constraints_variations
missing_leftovers

User inputs:
Build idea: {idea}
Skill level: {skill}
Environment: {environment}
Materials on hand: {materials if materials else "None provided"}
Tools on hand: {tools if tools else "None provided"}
Budget: {budget if budget else "Not provided"}
Size constraints: {size if size else "Not provided"}
Refine request: {refine if refine else "None"}

Rules:
- The plan must directly match the build idea.
- Keep the build practical and realistic.
- Respect the user's stated materials, tools, budget, and size constraints.
- Do not invent a different project.
- concept_breakdown: 2-4 sentences.
- materials_list: plain text bullet-style lines.
- step_by_step: numbered steps in plain text.
- constraints_variations: plain text bullet-style lines.
- missing_leftovers: plain text bullet-style lines.
- Output JSON only, no markdown, no extra commentary.
- If a refine request is provided, adjust the same project accordingly without changing it into a different object.
"""

    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        raw_text = response.output_text.strip()
        result = json.loads(raw_text)

        required_keys = [
            "concept_breakdown",
            "materials_list",
            "step_by_step",
            "constraints_variations",
            "missing_leftovers"
        ]

        if not all(key in result for key in required_keys):
            raise ValueError("Missing required keys in AI response.")

        return result

    except Exception as e:
        print("OpenAI error:", e)
        return local_fallback_plan(idea, skill, environment, materials, tools, budget, size)
       
@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    form_data = {
        "idea": "",
        "skill": "Beginner",
        "environment": "Indoor",
        "materials": "",
        "tools": "",
        "budget": "",
        "size": "",
        "refine": ""
    }

    if request.method == "POST":
        form_data["idea"] = request.form.get("idea", "").strip()
        form_data["skill"] = request.form.get("skill", "").strip()
        form_data["environment"] = request.form.get("environment", "").strip()
        form_data["materials"] = request.form.get("materials", "").strip()
        form_data["tools"] = request.form.get("tools", "").strip()
        form_data["budget"] = request.form.get("budget", "").strip()
        form_data["size"] = request.form.get("size", "").strip()
        form_data["refine"] = request.form.get("refine", "").strip()

        result = generate_buildspark_plan(
            idea=form_data["idea"],
            skill=form_data["skill"],
            environment=form_data["environment"],
            materials=form_data["materials"],
            tools=form_data["tools"],
            budget=form_data["budget"],
            size=form_data["size"],
            refine=form_data["refine"]
        )


        plan_entry = {
            "id": str(uuid.uuid4()),
            "idea": form_data["idea"],
            "skill": form_data["skill"],
            "environment": form_data["environment"],
            "materials": form_data["materials"],
            "tools": form_data["tools"],
            "budget": form_data["budget"],
            "size": form_data["size"],
            "refine": form_data["refine"],
            "result": result
        }

        save_plan_entry(plan_entry)


    return render_template("index.html", result=result, form_data=form_data)

@app.route("/plans")
def plans():
    saved_plans = load_saved_plans()
    return render_template("plans.html", saved_plans=saved_plans)


def overwrite_saved_plans(plans):
    with open(PLANS_FILE, "w", encoding="utf-8") as f:
        json.dump(plans, f, indent=2, ensure_ascii=False)


@app.route("/delete-plan/<plan_id>", methods=["POST"])
def delete_plan(plan_id):
    plans = load_saved_plans()
    updated_plans = [plan for plan in plans if plan.get("id") != plan_id]
    overwrite_saved_plans(updated_plans)
    return redirect("/plans")


if __name__ == "__main__":
    app.run(debug=True)