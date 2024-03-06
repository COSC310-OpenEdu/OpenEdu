USE openEDU;

SET foreign_key_checks = 0;
DROP TABLE IF EXISTS User, Course, Department, Student, Instructor, Admin, Assignment, Grades, Attend, Instructs;
SET foreign_key_checks = 1;


CREATE TABLE IF NOT EXISTS User (
    userId      INTEGER NOT NULL AUTO_INCREMENT,
    firstName   VARCHAR(20),
    lastName    VARCHAR(20),
    email       VARCHAR(20),
    username    VARCHAR(20),
    password    VARCHAR(20),
    profilePicture BLOB,
    profilePictureLocator VARCHAR(20),

    PRIMARY KEY (userId)
);

CREATE TABLE IF NOT EXISTS Course (
    courseId    INTEGER NOT NULL AUTO_INCREMENT,
    name        VARCHAR(20),

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
    studentId       INTEGER NOT NULL,
    courseId        INTEGER NOT NULL,
    name            VARCHAR(20),
    files           BLOB,
    fileLocator     VARCHAR(20),
    dueDate         DATETIME,

    PRIMARY KEY (assignmentId, studentId, courseId),
    FOREIGN KEY (studentId) REFERENCES Student(userId),
    FOREIGN KEY (courseId) REFERENCES Course(courseId)
);

CREATE TABLE IF NOT EXISTS Grades (
    assignmentId    INTEGER NOT NULL,
    instructorId    INTEGER NOT NULL,
    grade           DECIMAL,
    comment         VARCHAR(50),

    PRIMARY KEY (assignmentId, instructorId),
    FOREIGN KEY (assignmentId) REFERENCES Assignment(assignmentId),
    FOREIGN KEY (instructorId) REFERENCES Instructor(userId)
);

CREATE TABLE IF NOT EXISTS Attend (
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

-- Insert Courses
INSERT INTO Course (name) VALUES ('COSC303');
INSERT INTO Course (name) VALUES ('COSC310');
INSERT INTO Course (name) VALUES ('COSC304');
INSERT INTO Course (name) VALUES ('COSC404');


-- Insert Departments
INSERT INTO Department (name) VALUES ('COSC');
INSERT INTO Department (name) VALUES ('MATH');
INSERT INTO Department (name) VALUES ('STAT');


-- Insert Student
INSERT INTO User (firstName, lastName, email, password) VALUES ('James', 'Smith', 'jSmith@Example.com', 'jsmith1234');
INSERT INTO Student (userId, year, program) VALUES (LAST_INSERT_ID(), 3, 'Computer Science');

INSERT INTO User (firstName, lastName, email, password) VALUES ('Bill', 'Murry', 'bMurry@Example.com', 'bmurry1234');
INSERT INTO Student (userId, year, program) VALUES (LAST_INSERT_ID(), 2, 'Computer Science');


-- Insert Instructor
INSERT INTO User (firstName, lastName, email, password) VALUES ('Jim', 'Bob', 'jb@Example.com', 'jbob1234');
INSERT INTO Instructor (userId, deptName) VALUES (LAST_INSERT_ID(), 'COSC');


-- Insert Admin
INSERT INTO User (firstName, lastName, email, password) VALUES ('Fred', 'Eman', 'fe@Example.com', 'feman1234');
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
INSERT INTO Assignment (studentId, courseId) VALUES (1,1);
INSERT INTO Assignment (studentId, courseId) VALUES (1,2);
INSERT INTO Assignment (studentId, courseId) VALUES (2,1);


-- Insert Grade
INSERT INTO Grades (instructorId, assignmentId, grade) VALUES (3,1,91.5);
INSERT INTO Grades (instructorId, assignmentId, grade) VALUES (3,2,81.0);
INSERT INTO Grades (instructorId, assignmentId, grade) VALUES (3,3,83.2);
