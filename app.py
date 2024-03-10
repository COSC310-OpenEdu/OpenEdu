
from flask import Flask, render_template, redirect, url_for, request

import mysql.connector
from pythonFiles.DatabaseManager import DatabaseManager

user = None
app = Flask(__name__)

# Database configuration
# Should put this in a config file but eh
db_config = {
    'user': 'team',
    'password': 'COSC310Team',
    'host': '192.168.1.98',
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
    
@app.route("/login")
def login():
    return render_template("login.html");

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

@app.route("/authenticate", methods=['POST'])
def authenticate():
    #Get inputted username and password from user
    username = request.form.get('username')
    password = request.form.get('password')

    #Check if user exists in database
    database = DatabaseManager()
    validLogin = database.checkLogin(username, password)

    #If exists, bring back to home page, ow stay on login page
    if validLogin:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))
    

if __name__ == "__main__":
    app.run()
