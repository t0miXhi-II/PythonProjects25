
questions = [
                {
                    "question": "What does RAM mean?",
                    "answer": "Random Access Memory"
                },
                {
                    "question": "What does GPU mean?",
                    "answer": "Graphical Processing Unit"
                }
            ]

score = 0

def main():
    #add_question()
    quiz_loop(questions)


def quiz_loop(questions: list):
    for i, question in enumerate(questions):
        print(f"{i + 1}) {question["question"]}")
        user_answer = input("Enter Answer: ").lower()
        check_answer(question, user_answer)
    
    print(f"Quiz Completed!!! Your Score is {score}")


def check_answer(question: dict, user_answer: str):
    if question["answer"].lower() == user_answer.lower():
        global score 
        score += 1
        print(f"Correct Answer!! Your Score is {score}")
    else:
        print(f"Incorrect. Score: {score}")


def add_question():
    question = input("Enter question: ")
    answer = input("Enter answert to question: ")
    new_question = {
        "question": question,
        "answer": answer
    }
    questions.append(new_question)


if __name__ == "__main__":
    main()