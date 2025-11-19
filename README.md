📌 Zero of Functions (ZOF) Solver
Numerical Methods Project — Root Finding Algorithms

This project implements six numerical methods for finding the zeros of nonlinear equations.
It contains:

✔ Python CLI Application (ZOF_CLI.py)

✔ Flask Web GUI Application (app.py + HTML/CSS)

✔ Deployment-ready project structure

✔ All six root-finding methods implemented in a separate core file (zof_core.py)

📁 Project Structure
/ZOF_Project/
│
├── zof_core.py                # All algorithms + safe function parser
├── ZOF_CLI.py                 # Command-line interface
├── app.py                     # Flask web GUI
├── requirements.txt
├── README.md
├── ZOF_hosted_webGUI_link.txt
│
├── /templates/
│     └── index.html
│
└── /static/
      └── style.css

✨ Features Implemented
✔ Six Numerical Methods

Bisection Method

Regula–Falsi (False Position) Method

Secant Method

Newton–Raphson Method

Fixed Point Iteration Method

Modified Secant Method

✔ CLI Features

Accepts equations as text input

Accepts initial guesses, interval bounds

Supports tolerance + maximum iterations

Displays iteration table

Displays final approximate root

✔ Web GUI Features (Flask)

User selects method from dropdown

Inputs automatically show/hide based on method

Table of iterations is displayed

Clear error messages

Mobile-friendly UI

▶️ How to Run the CLI Application

Ensure Python 3.8+ is installed.

1. Install dependencies
pip install -r requirements.txt

2. Run the CLI
python ZOF_CLI.py

Sample CLI Input
Enter f(x): x**3 - 5*x + 1
Choose method: 1
Tolerance: 1e-6
Max iterations: 50
a: 0
b: 2

🌐 How to Run the Web GUI (Flask)
1. Install dependencies
pip install -r requirements.txt

2. Start Flask app
python app.py

3. Open Browser

Visit:

http://127.0.0.1:5000

🚀 Deployment Instructions

You may deploy with:
✔ Render.com (recommended)
✔ PythonAnywhere.com
✔ Streamlit Cloud
✔ Vercel (via Flask adapter)

🟦 Deploy on Render.com (Fastest Option)

Push the project to GitHub

Go to: https://render.com

Click New → Web Service

Connect your GitHub repo

Choose:

Runtime: Python

Build command:

pip install -r requirements.txt


Start command:

gunicorn app:app


Click Deploy

Render will automatically generate your public URL.

📄 ZOF_hosted_webGUI_link.txt (What to Write)

Create this file and include:

Name: <Your Full Name>
Matric Number: <Your Matric No>

Hosted Web App URL:
https://<your-render-link>.onrender.com

GitHub Repository:
https://github.com/<your-username>/ZOF_Project

✔️ Marking Checklist (Examiner Requirements)
Requirement	Included	File
Six numerical methods	✅	zof_core.py
CLI app	✅	ZOF_CLI.py
Method selection	✅	CLI + GUI
Coefficient/interval input	✅	CLI + GUI
Iteration tables	✅	Both
Error estimation	✔️ Included	All methods
Web GUI	✔️ Flask	app.py + index.html
Deployment	Ready	Render, Streamlit etc
Hosted link file	Yes	ZOF_hosted_webGUI_link.txt
GitHub repo	Required	You create & upload