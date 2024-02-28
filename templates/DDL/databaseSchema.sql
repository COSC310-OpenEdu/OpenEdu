CREATE TABLE User (
    userId      INTEGER,
    firstName   VARCHAR(20),
    lastName    VARCHAR(20),
    email       VARCHAR(20),
    username    VARCHAR(20),
    password    VARCHAR(20),
    profilePicture BLOB,
    profilePictureLocator VARCHAR(20),

    PRIMARY KEY userId
)

CREATE TABLE Course (
    courseId    INTEGER,
    name        VARCHAR(20),

    PRIMARY KEY (couseId)
)

CREATE TABLE Department (
    name    VARCHAR(20),

    PRIMARY KEY (name)
)

CREATE TABLE Student (
    userId  INTEGER,
    year    INTEGER,
    program VARCHAR(20),

    PRIMARY KEY (userId),
    FOREIGN KEY userId REFERENCES User(userId)
)

CREATE TABLE Instructor (
    userId      INTEGER,
    speciality  VARCHAR(20),
    deptName    VARCHAR(20),

    PRIMARY KEY (userId),
    FOREIGN KEY (userId) REFERENCES User(userId)
)

CREATE TABLE Admin (
    userId      INTEGER,
    deptName    VARCHAR(20),

    PRIMARY KEY (userId),
    FOREIGN KEY (userId) REFERENCES User(userId)
)

CREATE TABLE Assignment (
    assignmentId    INTEGER,
    studentId       INTEGER,
    courseId        INTEGER,
    name            VARCHAR(20),
    files           BLOB,
    fileLocator     VARCHAR(20),
    dueDate         DATETIME,

    PRIMARY KEY (assignmentId, studentId, courseId),
    FOREIGN KEY (assignmentId) REFERENCES Assignment(assignmentId),
    FOREIGN KEY (studentId) REFERENCES Student(studentId),
    FOREIGN KEY (courseId) REFERENCES Course(courseId)
)

CREATE TABLE Grades (
    assignmentId    INTEGER,
    instructorId    INTEGER,
    grade           DECIMAL,
    comment         VARCHAR(50),

    PRIMARY KEY (assignmentId, instructorId),
    FOREIGN KEY (assignmentId) REFERENCES Assignment(assignmentId),
    FOREIGN KEY (instructorId) REFERENCES Instructor(instructorId)
)

CREATE TABLE Attend (
    studentId   INTEGER,
    courseId    INTEGER,

    PRIMARY KEY (studentId, courseId),
    FOREIGN KEY (studentId) REFERENCES Student(studentId),
    FOREIGN KEY (courseId) REFERENCES Course(courseId)
)

CREATE TABLE Instructs (
    instructorId    INTEGER,
    courseId        INTEGER,
    
    PRIMARY KEY (instructorId, courseId),
    FOREIGN KEY (instructorId) REFERENCES Instructor(instructorId),
    FOREIGN KEY (courseId) REFERENCES Course(courseId)
)
