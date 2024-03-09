from flask import Flask, render_template, request
import mysql.connector

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
    return render_template("login.html")

@app.route("/login/createaccount", method=['GET', 'POST'])
def createAccount():
    if (request.method == 'GET'):
        return render_template("accountCreation.html");
    else:
        createUser = ("INSERT INTO User (firstName, lastName, email, password) VALUES (%s, %s, %s, %s);");
        createTeacher = ("INSERT INTO Instructor (userId) VALUES (LAST_INSERT_ID());");
        createStudent = ("INSERT INTO Student (userId) VALUES (LAST_INSERT_ID());");
        
        form = request.form;
        userData = (form['fname'],form['lname'],form['email'],form['password']);
        
        cursor = db.cursor();
        
        cursor.execute(createUser, userData);
        
        if (form['accountType'] == 'student'):
            cursor.execute(createStudent);
        else:
            cursor.execute(createTeacher);
        
        db.commit();
        


if __name__ == "__main__":
    app.run()
