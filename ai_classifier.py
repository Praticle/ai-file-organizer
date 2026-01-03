import openai
import os
from pathlib import Path

# ----------------------------
# Configuration
# ----------------------------
CATEGORIES = ["School", "Finance", "Images", "Code", "Personal", "Other"]
openai.api_key = os.getenv("OPENAI_API_KEY")

# Quick file type defaults to avoid calling OpenAI unnecessarily
FILE_TYPE_DEFAULTS = {
    ".txt": "School",
    ".pdf": "Finance",
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".md": "Personal"
}

# ----------------------------
# Classification function
# ----------------------------
def classify_file(file_path: Path) -> str:
    # 1️⃣ Check file type defaults first
    ext = file_path.suffix.lower()
    if ext in FILE_TYPE_DEFAULTS:
        return FILE_TYPE_DEFAULTS[ext]

    # 2️⃣ For other files, use OpenAI GPT
    try:
        with open(file_path, "r", errors="ignore") as f:
            content = f.read(500)  # read first 500 chars
    except:
        content = ""  # non-text files

    prompt = f"""
You are a file organizer. Categorize this file into one of the following categories:
{', '.join(CATEGORIES)}.
Filename: {file_path.name}
Content: {content}

Only respond with the category name.
"""

    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        category = response.choices[0].message.content.strip()

        if category not in CATEGORIES:
            category = "Other"

        return category

    except Exception as e:
        print(f"[WARNING] OpenAI API failed for {file_path.name}: {e}")
        return "Other"
