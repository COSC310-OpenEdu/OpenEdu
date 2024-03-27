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
from src.Database.Query.SelectPeopleInCourse import SelectPeopleInCourse
from src.Database.Query.SelectInstructorsForCourse import SelectInstructorsForCourse
from src.Database.Query.SelectGradesForCourse import SelectGradesForCourse
from src.Database.Query.SelectAssignmentsForCourse import SelectAssignmentsForCourse
from src.Database.Query.SelectQuestionsForCourse import SelectQuestionsForCourse
from src.Database.Update.UpdateGrade import UpdateGrade

currentUser = None #Start with no user logged in
app = Flask(__name__)
app.secret_key = "a"

@app.route("/")
def home():
    # Test the database connection
    
        if (session.get("userType") == "Student"):
            courses = SelectRegisteredCourses.query((session['userId']))
            return render_template("/student/courses.html", courses=courses)
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
        

    
@app.route("/student/<courseId>/grades", methods=['GET'])
def seeGrades(courseId): 
 
    # Query for getting grades for every assignment in a class for a given student
    grades = SelectGradeForStudent.queryAll((session['userId'], courseId,));
    assignments = SelectAssignmentsForCourse.queryAll((courseId,))
    questions = SelectQuestionsForCourse.queryAll((courseId,))

    
    # Go to See Grades page
    return render_template("student/seeGrades.html", grades=grades, username=session['username'], courseId=courseId, assignments=assignments, questions=questions)


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
    assignments = SelectAssignmentsForCourse.queryAll((courseId,))
    grades = SelectGradesForCourse.queryAll((courseId,))
    questions = SelectQuestionsForCourse.queryAll((courseId,))
    return render_template("teacher/grading.html", courseId=courseId, grades=grades, assignments=assignments, questions=questions)

@app.route("/updateGrade", methods = ['POST'])
def updateGrade():
    form = request.form
    UpdateGrade.update((form['grade'], form['courseId'], form['questionId'], form['assignmentId'], form['studentId'],))
    return jsonify(form)

@app.route("/teacher/<courseId>/people", methods = ['GET'])
def teacherCoursePeople(courseId):
    instructors = SelectInstructorsForCourse.queryAll((courseId,))
    people = SelectPeopleInCourse.queryAll((courseId,))
    
    return render_template("teacher/people.html", courseId=courseId, people=people, instructors=instructors)

@app.route("/student/<courseId>/people", methods = ['GET'])
def studentCoursePeople(courseId):
    instructors = SelectInstructorsForCourse.queryAll((courseId,))
    people = SelectPeopleInCourse.queryAll((courseId,))
    
    return render_template("student/people.html", courseId=courseId, people=people, instructors=instructors)

@app.route("/teacher/<courseId>/publishQuiz", methods = ['POST', 'GET'])
def publishQuiz(courseId):
    questionForm = request.form
    return render_template("teacher/publishQuiz.html", questionForm=questionForm, courseId=courseId)

@app.route("/student/<courseId>/dashboard", methods = ['GET'])
def courseDashboard(courseId):
    return render_template("student/courseDashboard.html", courseId=courseId)

@app.route("/admin/approveRegistration")
def courseRegistration():
    return render_template("admin/approveRegistration.html")

@app.route("/admin/createCourse")
def createCourse():
    return render_template("admin/createCourse.html")

@app.route("/student/<courseId>/assignments", methods = ['GET'])
def seeAssignments(courseId):
    return render_template("student/seeAssignments.html", courseId=courseId)


if __name__ == "__main__":
    app.run()
