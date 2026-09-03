print('quiz program')
print('Please answer the question')
question = 'What number system do computers use?'
answer = input(f'{question}: ')
if answer.upper() == 'BINARY':
    print('Correct!')
else:
    print('Sorry, the answer is binary')
