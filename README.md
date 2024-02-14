An E Learning Platform

## Setup Environment locally on Visual Studio Code

1. If you haven't installed Python on your computer,[ install Python 3.12](https://www.python.org/downloads/)
2. Install the Python extension by Microsoft in VSCode
3. Open up the command palette by pressing `CTRL + Shift + P` and select/search for `Python: Create Environment...`
    - For Mac users, replace CTRL with the Command key
4. Open the terminal by pressing CTRL + ` and ensure that (.venv) is what is beside your name in the terminal.
5. Run the command: `python -m pip install flask`
6. You should be good to go! To develop locally and see what the website looks like, enter the command: `flask --app app.py --debug run`
    - Now whenever you save the .py file and refresh the page in your browser, the changes should be automatically reflected there!

