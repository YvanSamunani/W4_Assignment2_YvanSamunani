# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




class Hangman:
    def __init__(self, ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10):
        self.ans1= ans1
        self.ans2= ans2
        self.ans3= ans3
        self.ans4= ans4
        self.ans5= ans5
        self.ans6 = ans6
        self.ans7 = ans7
        self.ans8 = ans8
        self.ans9 = ans9
        self.ans10 = ans10
    def check_answer(self,score):
        score=0
        if self.ans1 == "2015":
            print("Correct")
            score = 1
            print("Your Score is: ", score, "/10")
        else:
            print("Wrong")
            score = 0
            wrong_answers = 1
            print("Your Score is: ", score, "/10", "\n" "you are hanging the man")

        if self.ans2 == "Fred Swaniker" or self.ans2 == "Swaniker Fred":
            print("Correct")
            score += 1
            print("Your Score is: ", score, "/10")
        else:
            print("Wrong!")
            score += 0
            print("Your Score is: ", score, "/10")


Q1 = input("Q1) When was ALU founded? : ")

Q2 = input("Q2) Who is the CEO of ALU? : ")
Q3 = input("Q3) Where are ALU campuses : ")
Q4 = input("Q4) How many campuses does ALU have : ")
Q5 = input("Q5) What is the name of ALU Rwanda’s Dean : ")
Q6 = input("Q6) Who is in charge of Student Life : ")
Q7 = input("Q7) What is the name of our Lab? : ")
Q8 = input("Q8) How many students do we have in Year 2 CS? : ")
Q9 = input("Q9) How many degrees does ALU offer? : ")
Q10 = input("Q10) Where are the headquarters of ALU : ")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
