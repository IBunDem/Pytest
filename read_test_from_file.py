from Test import *


begin = "/\\"
end = "\\/"
right = '+'
wrong = '-'


def get_questions_from_file(file_name):
    file = open(file_name)
    question = Question()
    questions = []

    for line in file:
        # print(line, end='')
        line = line.strip('\n')

        if line == ' ' or line == '' or line.startswith(begin):
            continue
        if line.startswith(end):
            if question.text != '' and question.answers and question.has_right:
                questions.append(question)
                question = Question()
        elif line.startswith(right) or line.startswith(wrong):
            question.add_answer(line)
        else:
            question.text = line
    file.close()
    return questions
