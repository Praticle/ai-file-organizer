# AI File Organizer

*"Automatically cleans up messy folders by understanding what files actually contain — AI reads filenames and a snippet of content to sort everything into School, Finance, Images, Code, Personal, or Other folders."*

---

## Features

- Automatically scans folders for files  
- Uses AI (GPT-4) to classify files intelligently  
- Moves files into clean category folders:  
  `School | Finance | Images | Code | Personal | Other`  
- Dry-run mode to preview moves without changing anything  
- File type defaults for instant categorization of common file types  

---

## Tech Stack

- Python 3.9+  
- OpenAI API (GPT-4)  
- Built-in modules: `os`, `shutil`, `pathlib`  
- Optional CLI flags for dry-run and folder selection  

---

## Setup & Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/ai-file-organizer.git
cd ai-file-organizer
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key:

**Option A – Environment variable (recommended):**

```powershell
# Windows PowerShell
setx OPENAI_API_KEY "YOUR_API_KEY_HERE"
```

Then restart VS Code or terminal.

**Option B – Hardcode (for testing only):**

```python
# In ai_classifier.py
openai.api_key = "YOUR_API_KEY_HERE"
```

---

## How to Run

**1️⃣ Dry-run (preview moves):**

```bash
python main.py
```

- Shows what files would be moved and to which folder.  
- Does **not** move files.

**2️⃣ Organize for real:**

Edit `main.py`:

```python
organize_files(dry_run=False)
```

Then run:

```bash
python main.py
```

- Files will actually move into their respective category folders under `organized_files/`.

---

## Demo Flow (Hackathon-Friendly)

1. Open a messy folder in `files_to_organize/`.  
2. Run `python main.py` (dry-run) → explain what will happen.  
3. Run `python main.py` (dry_run=False) → watch files get sorted automatically.  
4. Open `organized_files/` → show clean, categorized folders.

---

## Stretch Goals / Bonus Features

- Undo last organization (keeps a log of moved files)  
- Simple GUI using Tkinter or PySimpleGUI  
- Preview first 500 characters of text/PDF files before classification  
- CLI arguments: `--folder <path>` and `--dry-run`

---

## Tips

- Keep test files in `files_to_organize/` before running.  
- Only files that are recognized (or classified by AI) will move.  
- Non-text files or unrecognized types default to `Other`.
