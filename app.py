from flask import Flask, render_template, redirect, url_for, request

from pythonFiles.User import User
from pythonFiles.Database.Update.CreateAccount import CreateAccount
from pythonFiles.Database.Query.SelectCourseQuery import SelectCourseQuery
from pythonFiles.Database.Query.SelectGradeForStudent import SelectGradeForStudent
from pythonFiles.Database.Query.SelectStudentUserPass import SelectStudentUserPass
from pythonFiles.Database.Check.UsernamePasswordCheck import UsernamepasswordCheck


currentUser = None #Start with no user logged in
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("template.html")
    
@app.route("/login")
def login():
    return render_template("login.html");

@app.route("/login/createaccount", methods=['GET', 'POST'])
def createAccount():
    if (request.method == 'GET'):
        return render_template("accountCreation.html");
    else: # Post request
        # Update Database with user inputted information
        form = request.form;
        CreateAccount.update((form['accountType'],form['fname'],form['lname'],form['email'],form['password'], form['uname']));
                
        # Forward to the login page
        return redirect(url_for('login'))
        

@app.route("/authenticate", methods=['POST'])
def authenticate():
    #Check if the information the user submitted is in the database
    form = request.form;
    validLogin = UsernamepasswordCheck.check((form['uname'],form['password']));

    #If exists, Log the user in. Otherwise stay on the login page.
    if validLogin:
        #Create User class that stores data for current logged-in user
        SData = SelectStudentUserPass.query((form['uname'],form['password']));
        currentUser = User(SData[0], SData[1], SData[2], SData[3], SData[4], SData[5]) 
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))
    
@app.route("/seeGrades", methods=['GET'])
def seeGrades(): 
    studentId = '1'
    assignmentId = '1'
    courseId = '1'
    
    # Query for getting grades for every assignment in a class for a given student
    grades = SelectGradeForStudent.queryAll((studentId, assignmentId));
    
    # Query for getting the course name
    courseName = SelectCourseQuery.query((courseId))
    
    # Go to See Grades page
    return render_template("seeGrades.html", grades=grades, courseName=courseName)

if __name__ == "__main__":
    app.run()
