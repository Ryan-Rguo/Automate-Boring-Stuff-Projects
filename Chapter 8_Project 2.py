# Chapter 8
# Practice Project 2

# Write your own multiplication quiz without importing PyInputPlus.
# There are 2 arguments:
# 1.quizAmount = the amount of quiz generated.
# 2.timeAllowed = time allowed for each quiz in second.

import random, time

def multiplicationQuiz(quizAmount,timeAllowed):
    print('HERE ARE 10 MULTIPLICATION QUIZ:')
    score = 0
    for i in range(quizAmount):
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        quizTime = time.perf_counter()

        for v in range(3):
            answer = input(str(i + 1) + '. %s * %s = ' % (str(num1), str(num2)))
            answerTime = time.perf_counter()

            if answerTime - quizTime > timeAllowed:
                print('TIME OUT!')
                break
            else:
                if answer == str(num1 * num2):
                    print('Correct, great job!')
                    score += 1
                    time.sleep(1)
                    break
                else:
                    print('Incorrect!')

    print('\nHERE IS YORU RESULT:')
    print(''.ljust(20,'='))
    print('SCORE: ' + str(score) + '/%s' % quizAmount)


