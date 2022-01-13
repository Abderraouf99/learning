import requests
import random

class QuizModal:
    def __init__(self, api_link):
        self.questions_answer_list = {}
        self.fetch_questions_from_api(api_link)

    def fetch_questions_from_api(self, api_link):
        try:
            self.questions_answer_list = requests.get(api_link).json()["results"]
        except:
            print('An error occurred while fetching the questions')

    def get_random_question(self):
        return random.choice(self.questions_answer_list)