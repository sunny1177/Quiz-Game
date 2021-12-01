def new_game():
    
    guesses = []
    correct_gusses = 0
    question_num = 1

    for key in Questions:
        print("--------------------")
        print(key)
        for i in options[question_num -1]:
            print(i)
        guess = input("Enter(A, B, C ,OR , D)")
        guess = guess.upper()
        guesses.append(guess)
        correct_gusses += cheak_answer(Questions.get(key), guess)
        question_num += 1
    display_score(correct_gusses,guesses)
    
#----------------------------
def cheak_answer(answer,guess):
    if answer == guess:
        print('CORRECT ANSWER')
        return 1
    else:
        print("WRONG ANSWER")
        return 0
#----------------------------
def display_score(correct_guesses, guesses):
    print('----------------------------')
    print("RESULTS")
    print('----------------------------')
    print("Answers : ", end=" ")
    for i in Questions:
        print(Questions.get(i), end= " ")
    print()
    
    print("Guesses : ", end=" ")
    for i in guesses:
        print(i, end= " ")
    print()

    score = int((correct_guesses/len(Questions)) * 100)
    print ("Your score is : " + str(score)+"%")

#----------------------------
def play_again():
    pass
#----------------------------
#The Questions you want to input, you can put here.
Questions = {
    "Who is creato of Python?:" : "A",
    "What year was Python created?:" : "B",
    "Python is tribute to which python group?:" : "C",
    "Is the Earth round?:" : "A"

}
#The Options you want to input for each questions, you can put here.
options = [["A.Guido van Rossum","B.Ellon Mask","C.Bill Gates","D.Sunny"],
["A.1989","B.1991","C.2000","D.2016"],
["A.Lonley Island","B.Smosh","c.Monty Python","D.SNL"],
["A.True","B.False","C.Sometimes","D.What's Earth?"]
]

new_game()
