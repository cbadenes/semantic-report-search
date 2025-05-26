# Semantic Report Search

A prototype system for exploring business intelligence reports using NLP techniques.  
Initially, it supports tag-based search (by Area, Department, Team) and will evolve into a semantic search engine.

## Features
- Simple web interface for filtering reports
- FastAPI backend with data integration
- Ready for semantic enhancements in future sessions

## Initial Set Up

### 0. Prepare an AI-assisted Code Environment 

##### Sign Up for GitHub

If you don’t have a GitHub account yet:

- Go to: [https://github.com/join](https://github.com/join)
- Create your account with a valid email.

##### Apply for the GitHub Student Developer Pack (optional)

- Visit: [https://education.github.com/pack](https://education.github.com/pack)
- Click “**Get Student Benefits**”
- Use your school email or upload a document to verify your student status.
- Once approved, you'll get **GitHub Copilot for free** (for 1 year).

##### Enable GitHub Copilot

- Go to: [https://github.com/settings/copilot](https://github.com/settings/copilot)
- Activate your Copilot subscription.
- Make sure **Copilot Chat** is enabled too.

##### Install Visual Studio Code

- Download and install VS Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)

##### Install Required Extensions

In VS Code:
- Open the Extensions panel (left sidebar or press `Ctrl+Shift+X`)
- Search and install:
  - **GitHub Copilot**
  - **GitHub Copilot Chat**
  - **Jupyter**
  - **Live Server**

Then:
- Sign in to GitHub inside VS Code when prompted (using your github account).
- Authorize the extensions to use Copilot.


### 1. Clone or unzip this project

```bash
git clone https://github.com/cbadenes/semantic-report-search.git
cd semantic-report-search/
```

### 2. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python3.9 -m venv .venv

# Activate it
# On Linux/Mac:
source .venv/bin/activate

# On Windows:
.venv\\Scripts\\activate
```


### 3. Install Required Dependencies
```bash
# Install all Python dependencies
pip install --upgrade pip
pip install --upgrade setuptools wheel
pip install -r requirements.txt

# Download models
python setup_environment.py
```

### 4. Open and Use Jupyter Notebooks from VSCode

- Open any `.ipynb` notebook in VS Code.
- Use **Markdown cells** to describe your ideas and reasoning.
- Use **Copilot Chat** to ask for code suggestions or explanations.
  - Open the chat panel (click the Copilot icon or press `Ctrl+I`)
  - Ask things like:
    - “Write a Python function that returns all even numbers from a list.”
    - “Explain what this code does.”

### 5. Start the backend server (API)

```bash
# Start the backend
python run_api.py
```
The API will be available at: http://localhost:8000/v0/search

```bash
GET http://localhost:8000/v0/search?q=Digital
```

---

This setup allows you to write ideas in natural language and use AI to turn them into code — great for learning and understanding the logic behind programming.
