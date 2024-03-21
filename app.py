from flask import Flask, render_template, redirect, url_for, request, session, jsonify

from src.User import User
from src.Database.DatabaseManager import DatabaseManager
from src.Database.Update.CreateAccount import CreateAccount
from src.Database.Query.SelectCourseQuery import SelectCourseQuery
from src.Database.Query.SelectGradeForStudent import SelectGradeForStudent
from src.Database.Query.SelectStudentUserPass import SelectStudentUserPass
from src.Database.Check.UsernamePasswordCheck import UsernamePasswordCheck
from src.Database.Query.SelectRegisteredCoursesQuery import SelectRegisteredCourses
from src.Database.Check.CheckUserIsStudent import CheckUserIsStudent
from src.Database.Check.CheckUserIsInstructor import CheckUserIsInstructor

currentUser = None #Start with no user logged in
app = Flask(__name__)
app.secret_key = "a"

@app.route("/")
def home():
    # Test the database connection
    
        if (session.get("userType") == "Student"):
            courses = SelectRegisteredCourses.query((session['userId']))
            return render_template("courses.html", courses=courses)
        elif (session.get("userType") == "Instructor"):
            return teacherHome()
        else:
            return render_template("openEduHome.html")

    
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
    userId = StudentData[0]
    session['username'] = request.form['uname']
    session['userId'] = userId
    #Checks for User type and redirect accordingly
    if userId is None:
        return redirect(url_for('home'))
    if CheckUserIsInstructor.check(userId):
        session["userType"] = "Instructor"
        #URL will be /teacher/dashboard once implemented
        return redirect(url_for('home'))
    if CheckUserIsStudent.check(userId):
        session["userType"] = "Student"
        #URL will be /student/dashboard once implemented
        return redirect(url_for('home'))
    else:
        session["userType"] = "Admin"
        #URL will be /admin/dashboard once implemented
        return redirect(url_for('home'))




@app.route("/logout")
def logout():
    #Remove user from session and return to home page
    session.pop('username', None)
    session.pop('userId', None)
    session.pop("userType", None)
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


@app.route("/teacher/<courseId>/assignments/createQuiz", methods = ['POST', 'GET'])
def createQuiz(courseId):
    if request.method == 'GET':
        return render_template("teacher/createQuiz.html", courseId=courseId)
    if request.method == 'POST':
        questionForm = request.form
        return render_template("teacher/publishQuiz.html", questionForm=questionForm, courseId=courseId)

@app.route("/teacher/homepage", methods = ['POST','GET'])
def teacherHome():
    # temporarily getting a list of all courses
    courses = SelectCourseQuery.query((session['userId'],))
    
    return render_template("teacher/homepage.html", courses = courses)

@app.route("/teacher/<courseId>/dashboard", methods = ['GET'])
def teacherCourseDash(courseId):
    return render_template("teacher/courseDashboard.html", courseId=courseId)

@app.route("/teacher/<courseId>/assignments", methods = ['GET'])
def teacherCourseAssignments(courseId):
    return render_template("teacher/assignmentsTab.html", courseId=courseId)

@app.route("/teacher/<courseId>/grading", methods = ['GET'])
def teacherCourseGrading(courseId):
    return render_template("teacher/grading.html", courseId=courseId)

@app.route("/teacher/<courseId>/publishQuiz", methods = ['POST', 'GET'])
def publishQuiz(courseId):
    questionForm = request.form
    return render_template("teacher/publishQuiz.html", questionForm=questionForm, courseId=courseId)

@app.route("/courseDashboard/<courseId>", methods = ['GET'])
def courseDashboard(courseId):
    return render_template("courseDashboard.html", courseId=courseId)

@app.route("/approveRegistration")
def courseRegistration():
    return render_template("approveRegistration.html")


if __name__ == "__main__":
    app.run()
