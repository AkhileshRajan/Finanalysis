# How to Upload Code to GitHub

## Option 1: Command Line (No Code Pasting Needed)

If you use **Option 1 (command line)**, you **DON'T paste code anywhere**. Instead:

1. Open Terminal/Command Prompt
2. Navigate to your project folder
3. Run these commands:

```bash
cd "/Users/akhileshrajan/Documents/Cursor Projects/Web Dev"
git push -u origin main
```

It will ask for your GitHub username and password/token. That's it!

---

## Option 3: GitHub Web Interface (Where to Paste Code)

If you want to **manually upload files via GitHub's website**, here's where to paste code:

### Step-by-Step:

1. **Go to**: https://github.com/AkhileshRajan/Finanalysis
2. **Click**: "Add file" → "Create new file" (or "uploading an existing file")

### For Each File:

**Example: Creating `README.md`**

1. In the filename box, type: `README.md`
2. **Paste the code** from the `README.md` file into the editor below
3. Click "Commit new file"

**Example: Creating `backend/app/main.py`**

1. In the filename box, type: `backend/app/main.py` (include the full path!)
2. **Paste the code** from `backend/app/main.py` file
3. Click "Commit new file"

### File Paths to Create:

Create files in this exact order (with these exact paths):

**Root files:**
- `.gitignore`
- `LICENSE`
- `README.md`
- `docker-compose.yml`

**Backend files:**
- `backend/Dockerfile`
- `backend/requirements.txt`
- `backend/app/__init__.py`
- `backend/app/main.py`
- `backend/app/celery_app.py`
- `backend/app/core/__init__.py`
- `backend/app/core/config.py`
- `backend/app/api/__init__.py`
- `backend/app/api/v1/__init__.py`
- `backend/app/api/v1/router.py`
- `backend/app/api/v1/routes_auth.py`
- `backend/app/api/v1/routes_files.py`
- `backend/app/api/v1/routes_documents.py`
- `backend/app/api/v1/routes_parse.py`
- `backend/app/api/v1/routes_analyze.py`
- `backend/app/api/v1/routes_report.py`
- `backend/app/api/v1/routes_me.py`

**Frontend:**
- `frontend/README.md`

### Important Notes:

- **Include the full path** in the filename box (e.g., `backend/app/main.py`)
- **Create folders first** if needed (GitHub will create them automatically when you create a file inside)
- **Copy-paste the entire file content** from each file in your project folder
- **Don't commit `.env` files** - they're excluded by `.gitignore`

---

## Quick Reference: File Locations

All your code files are now in:
```
/Users/akhileshrajan/Documents/Cursor Projects/Web Dev/
```

Open each file and copy-paste its contents into GitHub's web editor when creating new files.

