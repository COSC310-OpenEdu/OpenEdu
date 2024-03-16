
from flask import Flask, render_template, redirect, url_for, request, session

import mysql.connector
from pythonFiles.DatabaseManager import DatabaseManager
from pythonFiles.User import User

currentUser = None #Start with no user logged in
app = Flask(__name__)
app.secret_key = "a"

# Database configuration
# Should put this in a config file but eh
db_config = {
    'user': 'team',
    'password': 'COSC310Team',
    'host': '50.98.157.215',
    'port': '3306',
    'database': 'openEDU'
}

# Establish a database connection
db = mysql.connector.connect(**db_config)


@app.route("/")
def home():
    # Test the database connection
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")  # Simple query to test
    db_version = cursor.fetchone()
    cursor.close()
    return render_template("template.html", db_version=db_version)
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    if(request.method == 'GET'):
        return render_template("login.html");
    else:
         #Get inputted username and password from user
        username = request.form.get('uname')
        password = request.form.get('password')

        #Check if user exists in database
        database = DatabaseManager()
        validLogin = database.checkLogin(username, password)

        #If exists, bring back to home page, ow stay on login page
        if validLogin:
            return addUserToSession(username, password)
        else:
            error = "Invalid username and password"
            return render_template("login.html", error=error);

def addUserToSession(username, password):
    #Adds username and userId to session
    database = DatabaseManager()
    StudentData = database.selectStudentUserPass(username, password)
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
    # Default handeling of page
    if (request.method == 'GET'):
        return render_template("accountCreation.html");
    # Post request occures when form is submitted
    else: # Post Request
        createUser = ("INSERT INTO User (firstName, lastName, email, password, username) VALUES (%s, %s, %s, %s, %s);");
        createTeacher = ("INSERT INTO Instructor (userId) VALUES (LAST_INSERT_ID());");
        createStudent = ("INSERT INTO Student (userId) VALUES (LAST_INSERT_ID());");
        
        # Retrieve form data
        form = request.form;
        userData = (form['fname'],form['lname'],form['email'],form['password'], form['uname']);
        
        cursor = db.cursor();
        
        cursor.execute(createUser, userData);
        
        # Create a student or instructor account depending on user's choice 
        if (form['accountType'] == 'student'):
            cursor.execute(createStudent);
        else:
            cursor.execute(createTeacher);
        
        db.commit();
        
        # Forward to the login page
        return login();

@app.route("/account/update", methods=['GET', 'POST'])
def updateAccount():
    if (request.method == 'GET'):
        return render_template("updateAccount.html");
    else:  
        updateEmail = "UPDATE User SET email = %s WHERE userId = %d";
        updatePassword = "UPDATE User SET password = %s WHERE userId = %d";
        
        form = request.form;
        

        cursor = db.cursor();
        
        if (form['password'] != ''):
            userData = (form['password'], 1);
            cursor.execute(updatePassword, userData);
        if (form['email'] != ''):
            userData = (form['email'], 1);
            cursor.execute(updateEmail, userData);
            
        db.commit();
                  
        return render_template("updateAccount.html");

    
@app.route("/seeGrades", methods=['GET'])
def seeGrades(): 
    # Query for getting grades for every assignment in a class for a given student
    getGrades = "SELECT Assignment.assignmentId, name, grade, comment FROM Assignment JOIN Grades ON Assignment.assignmentId = Grades.assignmentId WHERE Assignment.studentId = %s AND courseId = %s"
    # Query for getting the course name
    getCourseName = "SELECT name FROM Course WHERE courseId  = %s"
    
    cursor = db.cursor()
    cursor.execute(getGrades, ("1","1",)) # Test, change later
    grades = cursor.fetchall()
    cursor.close()
    cursor = db.cursor()
    cursor.execute(getCourseName, ("1",)) # Test, change later
    courseName = cursor.fetchone()
    cursor.close()
    
    # Go to See Grades page
    return render_template("seeGrades.html", grades=grades, courseName=courseName)


@app.route("/createAssignment", methods = ['POST', 'GET'])
def createAssignment():
   if request.method == 'GET':
       return render_template("createAssignment.html")
   if request.method == 'POST':
       questionForm = request.form
       return render_template('assignmentOverview.html', questionForm = questionForm)

@app.route("/createAssignment/overview", methods = ['POST', 'GET'])
def assignmentData():
   questionForm = request.form
   return render_template("assignmentOverview.html", questionForm = questionForm)

if __name__ == "__main__":
    app.run()
