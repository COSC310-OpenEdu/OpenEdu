USE openEDU;

SET foreign_key_checks = 0;
DROP TABLE IF EXISTS User, Course, Department, Student, Instructor, Admin, Assignment, Grades, Attend, Instructs, Question, Solution, CourseRequests;
SET foreign_key_checks = 1;


CREATE TABLE IF NOT EXISTS User (
    userId      INTEGER NOT NULL AUTO_INCREMENT,
    firstName   VARCHAR(20),
    lastName    VARCHAR(20),
    email       VARCHAR(100),
    username    VARCHAR(20),
    password    VARCHAR(20),
    profilePicture BLOB,
    profilePictureLocator VARCHAR(20),

    PRIMARY KEY (userId)
);

CREATE TABLE IF NOT EXISTS Course (
    courseId    INTEGER NOT NULL AUTO_INCREMENT,
    name        VARCHAR(20),
    description VARCHAR(100),
    credits     INTEGER,
    session     INTEGER,
    term        INTEGER,
    day         INTEGER,
    startTime   INTEGER,
    endTime     INTEGER,

    PRIMARY KEY (courseId)
);

CREATE TABLE IF NOT EXISTS Department (
    name    VARCHAR(20) NOT NULL,

    PRIMARY KEY (name)
);

CREATE TABLE IF NOT EXISTS Student (
    userId  INTEGER NOT NULL,
    year    INTEGER,
    program VARCHAR(20),

    PRIMARY KEY (userId),
    FOREIGN KEY (userId) REFERENCES User(userId)
);

CREATE TABLE IF NOT EXISTS Instructor (
    userId      INTEGER NOT NULL,
    speciality  VARCHAR(20),
    deptName    VARCHAR(20),

    PRIMARY KEY (userId),
    FOREIGN KEY (userId) REFERENCES User(userId)
);

CREATE TABLE IF NOT EXISTS Admin (
    userId      INTEGER NOT NULL,
    deptName    VARCHAR(20),

    PRIMARY KEY (userId),
    FOREIGN KEY (userId) REFERENCES User(userId)
);

CREATE TABLE IF NOT EXISTS Assignment (
    assignmentId    INTEGER NOT NULL AUTO_INCREMENT,
    courseId        INTEGER NOT NULL,
    name            VARCHAR(200),
    fileLocator     VARCHAR(200),
    dueDate         DATETIME,
    notQuiz         BIT,

    PRIMARY KEY (assignmentId, courseId),
    FOREIGN KEY (courseId) REFERENCES Course(courseId)
);

CREATE TABLE IF NOT EXISTS Attend (
    studentId   INTEGER NOT NULL,
    courseId    INTEGER NOT NULL,

    PRIMARY KEY (studentId, courseId),
    FOREIGN KEY (studentId) REFERENCES Student(userId),
    FOREIGN KEY (courseId) REFERENCES Course(courseId)
);

CREATE TABLE IF NOT EXISTS CourseRequests (
    studentId   INTEGER NOT NULL,
    courseId    INTEGER NOT NULL,

    PRIMARY KEY (studentId, courseId),
    FOREIGN KEY (studentId) REFERENCES Student(userId),
    FOREIGN KEY (courseId) REFERENCES Course(courseId)
);

CREATE TABLE IF NOT EXISTS Instructs (
    instructorId    INTEGER NOT NULL,
    courseId        INTEGER NOT NULL,
    
    PRIMARY KEY (instructorId, courseId),
    FOREIGN KEY (instructorId) REFERENCES Instructor(userId),
    FOREIGN KEY (courseId) REFERENCES Course(courseId)
);

CREATE TABLE IF NOT EXISTS Question(
    courseId        INTEGER NOT NULL,
    questionId      INTEGER NOT NULL,
    assignmentId    INTEGER NOT NULL,
    questionText    VARCHAR(200),
    questionAnswer  VARCHAR(200),
    longQuestion    BIT,

    PRIMARY KEY (courseId,questionId, assignmentId),
    FOREIGN KEY (courseId) REFERENCES Course(courseId),
    FOREIGN KEY (assignmentId) REFERENCES Assignment(assignmentId)
);

CREATE TABLE IF NOT EXISTS Solution (
    courseId INTEGER NOT NULL,
    questionId INTEGER NOT NULL,
    assignmentId INTEGER NOT NULL,
    studentId INTEGER NOT NULL,
    studentAnswer VARCHAR(1000),

    PRIMARY KEY (courseId, questionId, assignmentId, studentId),
    FOREIGN KEY (courseId,questionId, assignmentId) REFERENCES Question(courseId,questionId, assignmentId),
    FOREIGN KEY (studentId) REFERENCES Student(userId)
);

CREATE TABLE IF NOT EXISTS Grades (
    courseId        INTEGER NOT NULL,
    questionId      INTEGER NOT NULL,
    assignmentId    INTEGER NOT NULL,
    studentId       INTEGER NOT NULL,
    instructorId    INTEGER NOT NULL,
    grade           FLOAT(6,3),
    comment         VARCHAR(50),

    PRIMARY KEY (courseId, questionId, assignmentId, studentId, instructorId),
    FOREIGN KEY (courseId, questionId, assignmentId, studentId) REFERENCES Solution (courseId, questionId, assignmentId, studentId),
    FOREIGN KEY (instructorId) REFERENCES Instructor(userId)
);

-- Insert Courses
INSERT INTO Course (name, description, credits, session, term) VALUES ('COSC303', 'Numerical Analysis',3,1,2);
INSERT INTO Course (name, description, credits, session, term) VALUES ('COSC310', 'Software Engineering',3,1,2);
INSERT INTO Course (name, description, credits, session, term) VALUES ('COSC304', 'Introduction to Databases',3,1,1);
INSERT INTO Course (name, description, credits, session, term) VALUES ('COSC404', 'Database implementation',3,1,2);


-- Insert Departments
INSERT INTO Department (name) VALUES ('COSC');
INSERT INTO Department (name) VALUES ('MATH');
INSERT INTO Department (name) VALUES ('STAT');


-- Insert Student
INSERT INTO User (firstName, lastName, username, email, password) VALUES ('James', 'Smith', 'jsmith', 'jSmith@Example.com', 'jsmith1234');
INSERT INTO Student (userId, year, program) VALUES (LAST_INSERT_ID(), 3, 'Computer Science');

INSERT INTO User (firstName, lastName, username, email, password) VALUES ('Bill', 'Murry', 'bmurray', 'bMurry@Example.com', 'bmurry1234');
INSERT INTO Student (userId, year, program) VALUES (LAST_INSERT_ID(), 2, 'Computer Science');


-- Insert Instructor
INSERT INTO User (firstName, lastName, username, email, password) VALUES ('Jim', 'Bob', 'jimbob', 'jb@Example.com', 'jbob1234');
INSERT INTO Instructor (userId, deptName) VALUES (LAST_INSERT_ID(), 'COSC');


-- Insert Admin
INSERT INTO User (firstName, lastName, username, email, password) VALUES ('Fred', 'Eman', 'feman', 'fe@Example.com', 'feman1234');
INSERT INTO Admin (userId, deptName) VALUES (LAST_INSERT_ID(), 'COSC');



-- Insert Attend
INSERT INTO Attend (studentId, CourseId) VALUES (1,1);
INSERT INTO Attend (studentId, CourseId) VALUES (2,1);
INSERT INTO Attend (studentId, CourseId) VALUES (1,2);


-- Insert Instructs
INSERT INTO Instructs (instructorId, courseId) VALUES (3,1);
INSERT INTO Instructs (instructorId, courseId) VALUES (3,2);
INSERT INTO Instructs (instructorId, courseId) VALUES (3,3);
INSERT INTO Instructs (instructorId, courseId) VALUES (3,4);


-- Insert Assignments
INSERT INTO Assignment (courseId) VALUES (1);
INSERT INTO Assignment (courseId) VALUES (1);
INSERT INTO Assignment (courseId) VALUES (2);

-- Insert Questions 
INSERT INTO Question (assignmentId, questionId, courseId, questionText, questionAnswer, longQuestion) VALUES (1, 1, 1, "This is a question 1", "This is the answer 1", 0);
INSERT INTO Question (assignmentId, questionId, courseId,  questionText, questionAnswer, longQuestion) VALUES (1, 2, 1, "This is a question 2", "This is the answer 2", 1);
INSERT INTO Question (assignmentId, questionId, courseId,  questionText, questionAnswer, longQuestion) VALUES (1, 3, 1, "This is a question 3", "This is the answer 3", 0);

-- INSERT Solutions
INSERT INTO Solution (assignmentId, questionId, courseId,  studentId, studentAnswer) VALUES (1,1,1,1,"The solution 1 Student 1");
INSERT INTO Solution (assignmentId, questionId, courseId,  studentId, studentAnswer) VALUES (1,2,1,1,"The solution 2 Student 1");
INSERT INTO Solution (assignmentId, questionId, courseId,  studentId, studentAnswer) VALUES (1,3,1,1,"The solution 3 Student 1");

INSERT INTO Solution (assignmentId, questionId, courseId,  studentId, studentAnswer) VALUES (1,1,1,2,"The solution 1 Student 2");
INSERT INTO Solution (assignmentId, questionId, courseId,  studentId, studentAnswer) VALUES (1,2,1,2,"The solution 2 Student 2");
INSERT INTO Solution (assignmentId, questionId, courseId,  studentId, studentAnswer) VALUES (1,3,1,2,"The solution 3 Student 2");

-- Insert Grade
INSERT INTO Grades (assignmentId, questionId, courseId,  studentId, instructorId, grade, comment) VALUES (1,1,1,1,3,91.5, "Good");
INSERT INTO Grades (assignmentId, questionId, courseId,  studentId, instructorId, grade, comment) VALUES (1,2,1,1,3,45.5, "See me after class");
INSERT INTO Grades (assignmentId, questionId, courseId,  studentId, instructorId, grade, comment) VALUES (1,3,1,1,3,91.5, "Good");

INSERT INTO Grades (assignmentId, questionId, courseId,  studentId, instructorId, grade, comment) VALUES (1,1,1,2,3,91.5, "Excellent");
INSERT INTO Grades (assignmentId, questionId, courseId,  studentId, instructorId, grade, comment) VALUES (1,2,1,2,3,100.0, "Very Good");
INSERT INTO Grades (assignmentId, questionId, courseId,  studentId, instructorId, grade, comment) VALUES (1,3,1,2,3,91.5, "Very Good");