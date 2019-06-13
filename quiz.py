import random

def select_option():
    print("\n1. Ask questions\n")
    print("2. Add questions\n")
    print("3. Exit\n")
    print("4. Delete option\n")
    
    
    option = input("\nPlease select one option:")
    return option


def add_question():
    question=input('\nPlease enter a question: > ').capitalize()
    print("")
    print("Now tell us the answer..")
    answer=input("\n{0} > ".format(question)).lower()
    
    file = open ("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")

def ask_question():
    # empty lists to storage the questions and answers
    questions = []
    answers = []
    
    # when we use the 'with block' we don't need to close the file because it will be closed when the block ends
    with open('questions.txt', 'r') as file:
        lines = file.read().splitlines()
        
    # this for loop will create tuples of number of line + text
    for i, text in enumerate(lines):
        if i%2 == 0:
            # it will save even lines in the answers list
            questions.append(text)
        else:
            # it will save odd lines in the questions list
            answers.append(text)
            
    # the zip question will create a tuple of (question, answer)
   
#   https://pynative.com/python-random-shuffle/
#     mapIndexPosition = list(zip(empName, empSalary))
#     random.shuffle(mapIndexPosition)
#     empName, empSalary = zip(*mapIndexPosition)
   
#   using random.shuffle I randomise the list of question answers
    questions_and_answers = list(zip(questions,answers))
    random.shuffle(questions_and_answers)
    number_of_questions = len(questions)

    score = 0
    
    for question, answer in questions_and_answers:
        guess = input(question +" >").lower()
        
        if guess == answer:
            score += 1
            print("Well done!")
        else:
            print("wrong answer..")
            
    print ("{0} right answers out of {1} questions".format(score,number_of_questions))
    
    
def delete_option():
    with open('questions.txt', 'r+') as file:
        lines = file.read().splitlines()
    
    questions = []
    answers = []
    
    q_number = 0
    for question in questions:
        q_number += 1
        print (str(q_number) + question)

    remove_option = input("\nEnter the number of the question that you want to remove\n")
    
    for i, text in enumerate(lines):
        if i%2 == 0:
            # it will save even lines in the answers list
            questions.append(text)
        else:
            # it will save odd lines in the questions list
            answers.append(text)
    
    
    print(questions[int(remove_option)])

def game_loop():
    play = True
    
    while play:
        option = select_option()
        if option == "1":
            ask_question()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        elif option == "4":
            delete_option()
        else:
            print("Invalid selection")
        
    print("\nBye! Thanks for playing\n")
    
game_loop()