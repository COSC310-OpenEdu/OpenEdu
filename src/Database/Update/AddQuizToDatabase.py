from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql
from src.Database.Update.AddQuestionToDatabase import AddQuestionToDatabase
from datetime import datetime, timedelta

class AddQuizToDatabase(DatabaseUpdate):
    @classmethod 
    def update(cls, form, courseId, is_quiz):
        #This method adds a quiz to the database. It stores the quiz name in the
        #assignment table with a duedate. Then each question contained in the quiz
        #is individually added to the quiz database

        quizname = form["quizId"]

        #Add QuizName to Database
        cursor = DatabaseManager.getDatabaseCursor()
        # SQL query now includes the 'quiz' column to indicate quiz or essay
        statement = "INSERT INTO Assignment(courseId, name, dueDate, quiz) VALUES (%s, %s, %s, %s)"
        #one week from now
        dueDate = datetime.now() + timedelta(weeks=1)
        # I've added is_quiz to indicate if it's a quiz or essay
        is_quiz_int = int(is_quiz)
        quizInfo = (courseId, quizname, dueDate, is_quiz_int)
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

            #Get next question and answer
            question = form[questionKey]
            answer = form[answerKey]

            #Add Question to database
            AddQuestionToDatabase.update((question, answer, questionNumber, courseId, assignmentId))
            questionNumber  = questionNumber + 1
        




