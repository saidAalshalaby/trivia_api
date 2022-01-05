from models import Question


def create_mock_question():
    """This function to create a mock question in the DB
    to prevent  dropping db during the running of test suite"""
    question = Question(
         question='This is a test question that should deleted',
         answer='this answer should be deleted',
         difficulty=1,
         category='1')
    # create a new mock question in the DB
    question.insert()


# utility for paginating questions
def get_paginated_questions(request, questions, num_of_questions):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * num_of_questions
    end = start + num_of_questions
    questions = [question.format() for question in questions]
    current_questions = questions[start:end]

    return current_questions
