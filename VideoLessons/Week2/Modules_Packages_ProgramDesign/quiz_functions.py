def main():
    question = 'What number system do computers use?'
    correct_answer = 'Binary'

    print('Quiz Program!')
    user_answer = ask_question(question)
    check_response(user_answer, correct_answer)


def ask_question(question):
    print('Please answer the question')
    answer = input(f'{question}')
    return answer


def check_response(user_answer, correct_answer):
    if user_answer.upper() == correct_answer.upper():
        print('Correct!')
        return True
    else:
        print(f'Sorry, the answer is {correct_answer}')
        return False
