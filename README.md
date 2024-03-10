# An E-Learning Platform

### Website Link
[OpenEdu](https://openedu-2q8f.onrender.com) (It takes a while for the website to appear, but it's there!)

## Where to put Code

- static/CSS: Used for external stylesheets
- template: Used for HTML files

## Setup Environment locally on Visual Studio Code

1. If you haven't installed Python on your computer,[ install Python 3.12](https://www.python.org/downloads/)
   - Make sure that the Python version is 3.12.1 as that's what Render.com (the web hosting website) uses.
2. Install the Python extension by Microsoft in VSCode
3. Open up the command palette by pressing `CTRL + Shift + P` and select/search for `Python: Create Environment...`
    - For Mac users, replace CTRL with the Command key
4. Open the terminal by pressing CTRL + ` and ensure that (.venv) is what is beside the project directory path in the terminal.
    ![image](https://github.com/COSC310-OpenEdu/OpenEdu/assets/78817046/6876c753-3161-456c-bc10-2185c2961020)

6. Run the commands:
    1. `pip install flask`
    2. `pip install mysql-connector-python`
8. You should be good to go! To develop locally and see what the website looks like, enter the command: `flask --app app.py --debug run`
    - Now whenever you save the .py file and refresh the page in your browser, the changes should be automatically reflected there!
