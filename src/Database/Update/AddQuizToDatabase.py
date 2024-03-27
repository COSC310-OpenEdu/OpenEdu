from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql
from src.Database.Update.AddQuestionToDatabase import AddQuestionoDatabase
from datetime import datetime

class AddQuizToDatabase(DatabaseUpdate):
    @classmethod 
    def update(cls, form):

        quizname = form["quizId"]
        courseId = 2 #This is temporary until form includes courseNumber

        #Add QuizName to Database
        cursor = DatabaseManager.getDatabaseCursor()
        statement = "INSERT INTO Assignment(courseId, name, dueDate) VALUES (%s, %s, %s)"
        quizInfo = (courseId, quizname, datetime.now())
        cursor.execute(statement, quizInfo)

        DatabaseManager.commit()
        assignmentId = cursor.lastrowid #Gotten from adding quizname to database

        #Getting all question and answer keys from form
        keys = form.keys()
        questionKeys = [key for key in keys if key.startswith("questionText")]
        questionKeys = sorted(questionKeys)
        answerKeys = [key for key in keys if key.startswith("answer")]
        answerKeys = sorted(answerKeys)

        #Add each question to the database seperately
        questionNumber = 1
        for questionKey, answerKey in zip(questionKeys, answerKeys):

            question = form[questionKey]
            answer = form[answerKey]

            #Add Question to database
            AddQuestionoDatabase.update((question, answer, questionNumber, courseId, assignmentId))
            questionNumber  = questionNumber + 1
        




