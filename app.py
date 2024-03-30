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
from src.Database.Update.UpdateGrade import UpdateGrade
from src.Database.Update.AddQuizToDatabase import AddQuizToDatabase
from src.Database.Update.AddCourseRequest import AddCourseRequest
from src.Search.CourseSearch import CourseSearch
from src.Database.Query.SelectQuestionsForAssignment import SelectQuestionsForAssignment
from src.Database.Check.CheckAssignmentCompletion import CheckAssignmentCompletion
from src.Database.Update.SubmitAssignment import SubmitAssignment
from src.Database.Update.DeleteSolutions import DeleteSolutions
from src.Database.Query.SelectSolutionsForCourse import SelectSolutionsForCourse
from src.Database.Update.AddGrade import AddGrade

currentUser = None  # Start with no user logged in
app = Flask(__name__)
app.secret_key = "a"


@app.route("/")
def home():
    # Test the database connection

    if session.get("userType") == "Student":
        courses = SelectRegisteredCourses.query((session["userId"]))
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
    solutions = SelectSolutionsForCourse.queryAll((courseId,))

    if (len(grades) < len(solutions)):
        for i in range(len(grades) - 1, len(solutions)):
            grades.append(0)
    
    return render_template("teacher/grading.html", courseId=courseId, solutions=solutions, courseName=courseName, grades=grades, assignments=assignments, questions=questions)

@app.route("/updateGrade", methods = ['POST'])
def updateGrade():
    form = request.form
    if (form['insert'] == "1"):
        AddGrade.update((form['courseId'], form['questionId'], form['assignmentId'], form['studentId'], session['userId'], form['grade']))
    else:
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

        courseData = (courseName, description, credits, session, term)
        # Update Database with course information
        try:
            CreateCourse.update(courseData)
            flash("Course created successfully!", "success")
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")
            return render_template("admin/createCourse.html")

        return redirect(url_for("createCourse"))
    else:
        return render_template("admin/createCourse.html")

@app.route("/student/<courseId>-<courseName>/assignments", methods = ['GET'])
def seeAssignments(courseId, courseName):
    assignments = SelectAssignmentsForCourse.queryAll((courseId,))
    return render_template("student/seeAssignments.html", courseId=courseId, assignments=assignments, courseName=courseName)

@app.route("/student/<courseId>-<courseName>/assignments/<assignmentId>-<assignmentName>", methods = ['GET'])
def studentAssignment(courseId, courseName, assignmentId, assignmentName):
    questions = SelectQuestionsForAssignment.queryAll((courseId, assignmentId,))
    completion = CheckAssignmentCompletion.check((courseId, assignmentId, session['userId'],))
    assignmentName = assignmentName.strip('\"')
    return render_template("student/assignment.html", courseId=courseId, courseName=courseName, assignmentId=assignmentId, assignmentName=assignmentName, questions=questions, completion=completion)

@app.route("/submitAssignment", methods=['POST'])
def submitAssignment():
    form = request.form
    courseId = form.get("courseId", "")
    courseName = form.get("courseName", "")
    assignmentId = form.get("assignmentId", "")
    assignmentName = form.get("assignmentName", "")
    questions = SelectQuestionsForAssignment.queryAll((courseId, assignmentId,))

    for question in questions:
       SubmitAssignment.update((courseId, question[0], assignmentId, session['userId'], form.get(str(question[0]), "")))
    
    flash("You have submitted this assignment!")
    return redirect(url_for('studentAssignment', courseId=courseId, courseName=courseName, assignmentId=assignmentId, assignmentName=assignmentName))

@app.route("/deleteSolutions", methods=['POST'])
def deleteSolutions():
    form = request.form
    courseId = form.get("courseId", "")
    courseName = form.get("courseName", "")
    assignmentId = form.get("assignmentId", "")
    assignmentName = form.get("assignmentName", "")
    
    DeleteSolutions.update((courseId, assignmentId, session['userId'],))

    return redirect(url_for('studentAssignment', courseId=courseId, courseName=courseName, assignmentId=assignmentId, assignmentName=assignmentName))

@app.route("/teacher/<courseId>-<courseName>/assignments/<assignmentId>-<assignmentName>/<studentId>", methods = ['GET'])
def teacherAssignment(courseId, courseName, assignmentId, assignmentName, studentId):
    questions = SelectQuestionsForAssignment.queryAll((courseId, assignmentId,))
    completion = None
    if (studentId != False):
        completion = CheckAssignmentCompletion.check((courseId, assignmentId, studentId,))

    if (completion == False):
        flash("This student has not submitted this assignment yet.")
        return redirect(url_for('teacherCourseGrading', _anchor=str(assignmentId), courseId=courseId, courseName=courseName))
    else:
        return render_template("teacher/teacherAssignment.html", courseId=courseId, courseName=courseName, assignmentId=assignmentId, assignmentName=assignmentName, questions=questions, completion=completion)


if __name__ == "__main__":
    app.debug = True
    app.run()
