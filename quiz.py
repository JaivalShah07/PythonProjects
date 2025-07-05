que = [{
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["A. J.K. Rowling", "B. Tolkien", "C. Shakespeare", "D. Jane Austen"],
        "answer": "A"
    }]

score = 0

def quiz():

    global score
    for q in que:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input('Enter your answer (A/B/C/D): ').strip().upper()

        if  answer == q["answer"]:
            print('Correct !!')
            score += 10
        else:
            print(f'Wrong. The answer is {q["answer"]}.')

    print(f'\nQuiz finished!! Your final score: {score}')


quiz()