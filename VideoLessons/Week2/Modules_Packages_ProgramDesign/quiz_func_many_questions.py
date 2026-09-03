def main():
    # With a set or dictionary we can pair the question with the correct answer
    question_set = {
        'What number system do computers use?': 'Binary',
        'What technology is used to make telephone calls over the internet?': 'VoIP',
        'What does PDF stand for?': 'Portable Document Format'
    }

    print('Quiz Program!')

    for question, correct_answer in question_set.items(): # decompact the set
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

main()

