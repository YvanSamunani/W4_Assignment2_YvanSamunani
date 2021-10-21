# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


answers = ["2015",['Fred Swaniker', 'swaniker fred', 'fred'], "Rwanda and Mauritius", "2", "Hardji Ghandi", "Sila Ogidi", "Fab Lab", "120", "8", "Mauritius"]
score = 0
wrong_answers = 0
count_loses = 0
count_wins = 0


def question_1():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    ans_1 = input("Q1) When was ALU founded?:")
    if ans_1 == answers[0]:
        score += 1
        print("Correct!", score, "/10")

    else:
        print("wrong", score, "/10", "\n", "You're a hanging man")
        wrong_answers += 1
    question_2()


def question_2():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    if wrong_answers <6:
        ans_2= input("Q2) Who is the CEO of ALU? :")
        if ans_2.lower() == answers[1][0].lower() or ans_2.lower() == answers[1][1].lower() or ans_2.lower() == answers[1][2].lower():
            score+= 1
            print("Correct!", score,"/10")

        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1
        question_3()
    else:
        print("The man dies!")
        count_loses += 1
        play_again = input("Do you want to play again [y/n]?:")
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()

        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_3():
    global score
    global wrong_answers
    global count_wins
    global count_loses


    if wrong_answers <6:
        ans_3 = input("Q3) Where are ALU campuses : ")
        if ans_3.lower() == answers[2].lower():
            score += 1
            print("Correct!", score,"/10")

        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1
        question_4()
    else:
        print("The man dies!")
        count_loses += 1
        play_again = input("Do you want to play again [y/n]?:")
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_4():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    if wrong_answers <6:
        ans_4 = input("Q4) How many campuses does ALU have : ")
        if ans_4 == answers[3]:
            score += 1
            print("Correct!", score,"/10")

        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1
        question_5()
    else:
        print("The man dies!")
        count_loses += 1
        play_again = input("Do you want to play again [y/n]?:")
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_5():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    if wrong_answers <6:
        ans_5 = input("Q5) What is the name of ALU Rwanda’s Dean : ")
        if ans_5.lower() == answers[4].lower():
            score += 1
            print("Correct!", score,"/10")

        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1
        question_6()
    else:
        print("The man dies!")
        count_loses +=1
        play_again = input("Do you want to play again [y/n]?:")
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_6():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    if wrong_answers <6:
        ans_6 = input("Q6) Who is in charge of Student Life : ")
        if ans_6.lower() == answers[5].lower():
            score += 1
            print("Correct!", score,"/10")

        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1
        question_7()
    else:
        print("The man dies!")
        count_loses += 1
        play_again = input("Do you want to play again [y/n]?:")
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_7():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    if wrong_answers <6:
        ans_7 = input("Q7) What is the name of our Lab? : ")
        if ans_7.lower() == answers[6].lower():
            score += 1
            print("Correct!", score,"/10")

        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1
        question_8()
    else:
        print("The man dies!")
        count_loses += 1
        play_again = input("Do you want to play again [y/n]?:")
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_8():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    if wrong_answers <6:
        ans_8 = input("Q8) How many students do we have in Year 2 CS? : ")
        if ans_8 == answers[7].lower():
            score += 1
            print("Correct!", score,"/10")

        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1
        question_9()
    else:
        print("The man dies!")
        count_loses += 1
        play_again = input("Do you want to play again [y/n]?:")
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_9():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    if wrong_answers <6:
        ans_9 = input("Q9) How many degrees does ALU offer? : ")
        if ans_9 == answers[8]:
            score += 1
            print("Correct!", score,"/10")

        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1
        question_10()
    else:
        print("The man dies!")
        count_loses += 1
        play_again = input("Do you want to play again [y/n]?:")
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_10():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    if count_loses <6:
        ans_10 = input("Q10) Where are the headquarters of ALU : ")
        if ans_10.lower() == answers[9].lower():
            score += 1
            print("Correct!", score,"/10")

        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1

        play_again= input("Do you want to play again [y/n]?:")
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()
        else:
            count_wins +=1
            print("\n")
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")
    else:
        print("The man dies!")
        count_loses += 1
        play_again = input("Do you want to play again [y/n]?:")
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")

question_1()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
