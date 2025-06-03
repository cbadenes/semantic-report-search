# Semantic Report Search

A prototype system for exploring business intelligence reports using NLP techniques.  
Initially, it supports tag-based search (by Area, Department, Team) and will evolve into a semantic search engine.

## Features
- Simple web interface for filtering reports
- FastAPI backend with data integration
- Ready for semantic enhancements in future sessions

## Initial Set Up

### 0. Prepare an AI-assisted Code Environment 

#### Install Python 3.9 (on Windows 10)
Before continuing, you need Python 3.9 installed:
    1. Download it from: https://www.python.org/downloads/release/python-390/
    2. Run the installer and check the option `Add Python 3.9 to PATH`
    3. Click Install Now
    4. After it finishes, verify installation in a terminal:
```bash
    python --version
```
You should see something like: `Python 3.9.x`

Now you can proceed with the rest of the environment setup.

##### Sign Up for GitHub

If you don’t have a GitHub account yet:

- Go to: [https://github.com/join](https://github.com/join)
- Create your account with a valid email.

##### Apply for the GitHub Student Developer Pack (optional)

- Visit: [https://education.github.com/pack](https://education.github.com/pack)
- Click “**Get Student Benefits**”
- Use your school email or upload a document to verify your student status.
- Once approved, you'll get **GitHub Copilot for free** (for 1 year).

#### Or Use GitHub Copilot without a Student Account (Optional)

If you don’t have access to the GitHub Student Developer Pack, you can still use GitHub Copilot for free for 30 days with any personal account.

###### Start a Free Trial of GitHub Copilot
1. Go to: https://github.com/features/copilot
2. Click on “Start my free trial”
3. Enter your payment method (credit or debit card)
4. Enjoy 30 days of full access to Copilot and Copilot Chat

You won’t be charged if you cancel before the end of the trial.

###### Cancel the Subscription to Avoid Charges
To cancel before the trial ends:
1. Visit: https://github.com/settings/billing
2. Click on “Copilot”
3. Select “Cancel subscription” and confirm

This lets you use Copilot’s AI features inside VS Code for a full month — ideal for completing exercises or trying out Copilot's capabilities.

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
git clone https://github.com/cbadenes/semantic-report-search.git  --config core.autocrlf=false
cd semantic-report-search/
```

### 2. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

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

### 6.Test the Search API from the Frontend Interface

To explore the search results via a web interface:

1. Open the file *frontend/index.html* in your browser (right-click → *"Open with Live Server"* in VS Code, or double-click to open it locally).
2. Type a search query in the *Search term* input box.
3. Choose the desired *API version* from the dropdown:
    - v0: Exact match
    - v1.4: Autocomplete support
    - v2.1: Word Embeddings
    - etc.
4. Click the Search button to query the backend.
5. Results will be displayed dynamically, including matched report names, views, and highlighted keywords.


Make sure the API backend (python run_api.py) is running on http://localhost:8000 before you open the page.
Otherwise, the frontend won't be able to fetch data.

---

This setup allows you to write ideas in natural language and use AI to turn them into code — great for learning and understanding the logic behind programming.
