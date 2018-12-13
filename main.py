from read_test_from_file import *


def main():
    file_name = input('название файла с тестами: ')
    questions = get_questions_from_file(file_name)
    # questions = get_questions_from_file('kompyuternye_seti.ask')
    # questions[0].print()
    test = Test(questions)
    print('обнаружено {len} вопросов'.format(len=len(questions)))
    num = int(input('Введите количество вопросов для теста: '))

    for i in range(num):
        q = test.get_next_question()
        print('Вопрос ' + str(i) + '. ', end='')
        q.print()
        print('---------------')
        inp = int(input('Введите верный ответ: '))
        print('---------------')



if __name__ == '__main__':
    main()
