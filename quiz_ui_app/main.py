from quiz_modal import QuizModal
from quiz_view import QuizView
OPEN_TRIVIA_API = 'https://opentdb.com/api.php?amount=20&type=boolean'
try:
    quiz_modal = QuizModal(OPEN_TRIVIA_API)
    question = quiz_modal.get_random_question()
    quiz_view = QuizView(initial_question=question)
except:
    print('Failed to run the application correctly')



