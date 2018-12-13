import random

class Question:
    wrong = '-'
    right = '+'

    def __init__(self, text=None, answers=None):
        self.text = text
        self.answers = answers if answers else {'wrongs': [], 'rights': []}
        self.has_right = True if answers and answers.get('rights') else False

    def __str__(self):
        return 'text: {text}, answers: {answers}'.format(text=self.text, answers=self.answers)

    def add_answer(self, answer):
        if answer.startswith(self.wrong):
            self.answers['wrongs'].append(answer.strip('-'))
        elif answer.startswith(self.right):
            self.answers['rights'].append(answer.strip('+'))
            self.has_right = True

    def print(self):
        answers = [*self.answers['wrongs'], *self.answers['rights']]
        random.shuffle(answers)
        print(self.text)
        print(str(len(self.answers['rights'])) + ' правильных')
        for i in range(len(answers)):
            print(str(i+1) + ". " + answers[i])


class Test:
    def __init__(self, questions):
        self.questions = questions
        for i in range(2):
            random.shuffle(self.questions)

    def get_next_question(self):
        return self.questions.pop(0)
