from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    session,
    jsonify,
    flash,
)

import json

from src.User import User
from src.Database.DatabaseManager import DatabaseManager
from src.Database.Update.CreateAccount import CreateAccount
from src.Database.Update.createCourse import CreateCourse
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
from src.Database.Query.SelectStudentQuery import SelectStudentQuery
from src.Database.Update.UpdateGrade import UpdateGrade
from src.Database.Update.AddQuizToDatabase import AddQuizToDatabase
from src.Database.Update.AddCourseRequest import AddCourseRequest
from src.Database.Update.UpdateEmail import UpdateEmail
from src.Database.Update.UpdatePassword import UpdatePassword
from src.Search.CourseSearch import CourseSearch
from src.Database.Query.SelectAllInstructors import SelectAllInstructors

currentUser = None  # Start with no user logged in
app = Flask(__name__)
app.secret_key = "a"


@app.route("/")
def home():
    # Test the database connection

    if session.get("userType") == "Student":
        courses = SelectRegisteredCourses.queryAll((session["userId"]))
        return render_template("student/courses.html", courses=courses)
    elif session.get("userType") == "Instructor":
        return teacherHome()
    else:
        return render_template("openEduHome.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        # Get inputted username and password from user
        username = request.form.get("uname")
        password = request.form.get("password")

        # Check if user exists in database
        validLogin = UsernamePasswordCheck.check((username, password))
        # If exists, bring back to home page, ow stay on login page
        if validLogin:
            return addUserToSession(username, password)
        else:
            error = "Invalid username and password"
            return render_template("login.html", error=error)


def addUserToSession(username, password):
    # Adds username and userId to session
    StudentData = SelectStudentUserPass.query((username, password))
    userId = StudentData[0]
    session["username"] = request.form["uname"]
    session["userId"] = userId
    # Checks for User type and redirect accordingly
    if userId is None:
        return redirect(url_for("home"))
    if CheckUserIsInstructor.check(userId):
        session["userType"] = "Instructor"
        # URL will be /teacher/dashboard once implemented
        return redirect(url_for("home"))
    if CheckUserIsStudent.check(userId):
        session["userType"] = "Student"
        # URL will be /student/dashboard once implemented
        return redirect(url_for("home"))
    else:
        session["userType"] = "Admin"
        # URL will be /admin/dashboard once implemented
        return redirect(url_for("createCourse"))


@app.route("/logout")
def logout():
    # Remove user from session and return to home page
    session.pop("username", None)
    session.pop("userId", None)
    session.pop("userType", None)
    return redirect(url_for("home"))


@app.route("/login/createaccount", methods=["GET", "POST"])
def createAccount():
    if request.method == "GET":
        return render_template("accountCreation.html")
    else:  # Post request
        # Update Database with user inputted information
        form = request.form
        CreateAccount.update(
            (
                form["accountType"],
                form["fname"],
                form["lname"],
                form["email"],
                form["password"],
                form["uname"],
            )
        )
        # Forward to the login page

        return redirect(url_for("login"))

@app.route("/student/updateAccount", methods=['GET', 'POST'])
def updateAccount():
    if request.method == 'GET':
        return render_template('student/updateAccount.html')
    else:
        requestType = request.form['type'];
        
        # Password update request
        if (requestType == 'password'):
            successful = UpdatePassword.update((session['userId'], request.form['old'], request.form['new']))
            
            if (successful == False):
                return jsonify({"error": 'Password Update Failed'}), 400
            
        # Email update Request
        if (requestType == 'email'):
            successful = UpdateEmail.update((session['userId'], request.form['email'])) 
            
            if (successful == False):
                return jsonify({"error": 'Email Update Failed'}), 400           
        
        return {}
        
@app.route("/student/info", methods=['POST'])
def studentInfo():
    # Returns firstname lastname and email to the given user id
    studentInfo = SelectStudentQuery.query((session['userId'],));
    
    returnData = {
        'firstName': studentInfo[1],
        'lastName': studentInfo[2],
        'email': studentInfo[3]
    };
    
    return json.dumps(returnData);
    
@app.route("/student/<courseId>-<courseName>/grades", methods=['GET'])
def seeGrades(courseId, courseName): 
 
    # Query for getting grades for every assignment in a class for a given student
    grades = SelectGradeForStudent.queryAll((session['userId'], courseId,));
    assignments = SelectAssignmentsForCourse.queryAll((courseId,))
    questions = SelectQuestionsForCourse.queryAll((courseId,))

    
    # Go to See Grades page
    return render_template("student/seeGrades.html", grades=grades, courseName=courseName, username=session['username'], courseId=courseId, assignments=assignments, questions=questions)


@app.route("/teacher/<courseId>-<courseName>/assignments/createQuiz", methods = ['POST', 'GET'])
def createQuiz(courseId, courseName):
    if request.method == 'GET':
        return render_template("teacher/createQuiz.html", courseId=courseId, courseName=courseName)
    if request.method == 'POST':
        questionForm = request.form
        return render_template("teacher/publishQuiz.html", questionForm=questionForm, courseId=courseId, courseName=courseName)
    

@app.route('/search', methods = ['POST', 'GET'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        searchTerm = request.form['searchTerm']
        return CourseSearch.search(searchTerm)

@app.route('/Course/<courseId>/join', methods = ['POST'])
def joinCourse(courseId):
    userId = session['userId']
    
    # Student must be signed in to join a course
    if userId == None:
        return redirect(url_for('login'))
    
    AddCourseRequest.update((userId, courseId))
    
    return {}


@app.route("/teacher/homepage", methods=["POST", "GET"])
def teacherHome():
    # temporarily getting a list of all courses
    
    courses = SelectCourseQuery.query((session['userId'],))
    
    return render_template("teacher/homepage.html", courses = courses)

@app.route("/teacher/<courseId>-<courseName>/dashboard", methods = ['GET'])
def teacherCourseDash(courseId, courseName):
    
    return render_template("teacher/courseDashboard.html", courseId=courseId, courseName=courseName)

@app.route("/teacher/<courseId>-<courseName>/assignments", methods = ['GET'])
def teacherCourseAssignments(courseId, courseName):
    assignments = SelectAssignmentsForCourse.queryAll((courseId,))
    return render_template("teacher/assignmentsTab.html", courseId=courseId, courseName=courseName, assignments=assignments)

@app.route("/teacher/<courseId>-<courseName>/grading", methods = ['GET'])
def teacherCourseGrading(courseId, courseName):
    assignments = SelectAssignmentsForCourse.queryAll((courseId,))
    grades = SelectGradesForCourse.queryAll((courseId,))
    questions = SelectQuestionsForCourse.queryAll((courseId,))
    return render_template("teacher/grading.html", courseId=courseId, courseName=courseName, grades=grades, assignments=assignments, questions=questions)

@app.route("/updateGrade", methods = ['POST'])
def updateGrade():
    form = request.form
    UpdateGrade.update((form['grade'], form['courseId'], form['questionId'], form['assignmentId'], form['studentId'],))
    return jsonify(form)

@app.route("/teacher/<courseId>-<courseName>/people", methods = ['GET'])
def teacherCoursePeople(courseId, courseName):
    instructors = SelectInstructorsForCourse.queryAll((courseId,))
    people = SelectPeopleInCourse.queryAll((courseId,))
    
    return render_template("teacher/people.html", courseId=courseId, courseName=courseName, people=people, instructors=instructors)

@app.route("/student/<courseId>-<courseName>/people", methods = ['GET'])
def studentCoursePeople(courseId, courseName):
    instructors = SelectInstructorsForCourse.queryAll((courseId,))
    people = SelectPeopleInCourse.queryAll((courseId,))
    
    return render_template("student/people.html", courseId=courseId, courseName=courseName, people=people, instructors=instructors)

@app.route("/teacher/<courseId>-<courseName>/publishQuiz", methods = ['POST', 'GET'])
def publishQuiz(courseId, courseName):
    questionForm = request.form
    return render_template("teacher/publishQuiz.html", questionForm=questionForm, courseId=courseId, courseName=courseName)

@app.route("/student/<courseId>-<courseName>/dashboard", methods = ['GET'])
def courseDashboard(courseId,courseName):
    return render_template("student/courseDashboard.html", courseId=courseId, courseName=courseName)


@app.route("/admin/approveRegistration")
def courseRegistration():
    return render_template("admin/approveRegistration.html")


@app.route("/admin/createCourse", methods=["POST", "GET"])
def createCourse():
    if request.method == "POST":
        # Extract form data using .get() to avoid BadRequestKeyError
        form = request.form
        courseName = form.get("courseName", "")
        description = form.get("description", "")
        credits = int(form.get("credits", 0))
        session = int(form.get("session", 0))
        term = int(form.get("term", 0))
        instructorId = int(form.get("instructor", 0))

        courseData = (courseName, description, credits, session, term)
        # Update Database with course information
        try:
            CreateCourse.update(courseData, instructorId)
            flash("Course created successfully!", "success")
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")
            return render_template("admin/createCourse.html")

        return redirect(url_for("createCourse"))
    else:
        instructorIds, instructorNames = SelectAllInstructors.queryAll()
        return render_template("admin/createCourse.html", instructorIds=instructorIds, instructorNames=instructorNames, len=len)

@app.route("/student/<courseId>-<courseName>/assignments", methods = ['GET'])
def seeAssignments(courseId, courseName):
    assignments = SelectAssignmentsForCourse.queryAll((courseId,))
    return render_template("student/seeAssignments.html", courseId=courseId, assignments=assignments, courseName=courseName)


if __name__ == "__main__":
    app.debug = True
    app.run()
