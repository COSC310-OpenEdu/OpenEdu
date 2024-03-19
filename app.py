from flask import Flask, render_template, redirect, url_for, request, session

from src.User import User
from src.Database.DatabaseManager import DatabaseManager
from src.Database.Update.CreateAccount import CreateAccount
from src.Database.Query.SelectCourseQuery import SelectCourseQuery
from src.Database.Query.SelectGradeForStudent import SelectGradeForStudent
from src.Database.Query.SelectStudentUserPass import SelectStudentUserPass
from src.Database.Check.UsernamePasswordCheck import UsernamePasswordCheck


currentUser = None #Start with no user logged in
app = Flask(__name__)
app.secret_key = "a"

@app.route("/")
def home():
    return render_template("template.html")
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    if(request.method == 'GET'):
        return render_template("login.html");
    else:
         #Get inputted username and password from user
        username = request.form.get('uname')
        password = request.form.get('password')

        #Check if user exists in database
        validLogin = UsernamePasswordCheck.check((username, password));

        #If exists, bring back to home page, ow stay on login page
        if validLogin:
            return addUserToSession(username, password)
        else:
            error = "Invalid username and password"
            return render_template("login.html", error=error);

def addUserToSession(username, password):
    #Adds username and userId to session
    StudentData = SelectStudentUserPass.query((username, password));
    session['username'] = request.form['uname']
    session['userId'] = StudentData[0]
    return redirect(url_for('home'))


@app.route("/logout")
def logout():
    #Remove user from session and return to home page
    session.pop('username', None)
    session.pop('userId', None)
    return redirect(url_for('home'))

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
    validLogin = UsernamePasswordCheck.check((form['uname'],form['password']));

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
    grades = SelectGradeForStudent.queryAll((studentId, assignmentId,));
    
    # Query for getting the course name
    courseName = SelectCourseQuery.query((courseId,))
    
    # Go to See Grades page
    return render_template("seeGrades.html", grades=grades, courseName=courseName)


@app.route("/teacher/COSC310/assignments/createQuiz", methods = ['POST', 'GET'])
def createAssignment():
   if request.method == 'GET':
       return render_template("teacher/createQuiz.html")

@app.route("/teacher/dashboard", methods = ['POST','GET'])
def teacherDash():
    # temporarily getting a list of all courses
    courses = []
    for i in range(1,5):
        courseId = i
        courseName = SelectCourseQuery.query((courseId,))
        courses.append(courseName[0])
    return render_template("teacher/dashboard.html", courses = courses)

@app.route("/teacher/COSC310/dashboard", methods = ['POST','GET'])
def teacherCourseDash():
    return render_template("teacher/courseDashboard.html")

@app.route("/teacher/COSC310/assignments")
def teacherCourseAssignments():
    return render_template("teacher/assignmentsTab.html")

@app.route("/teacher/<courseId>/grading", methods = ['GET'])
def teacherCourseGrading(courseId):
    return render_template("teacher/grading.html", courseId=courseId)

if __name__ == "__main__":
    app.run()
