from random import randint
t=0
n=0
number=0
questions=[]
if __name__ == "__main__":
    for i in range(10):
        number_1 = randint(1,10)
        number_2 = randint(1,10)
        number_3 = number_1 * number_2
        number_3 = float(number_3)
        print(number_1, "*", number_2, "=")
        answer=input("What is the answer? : " )
        answer = float(answer)
        if answer == number_3:
            t=t+1
            number=number+1
        else:
            n=n+1
if t >= 7:
    passing = "passed"
    
else:
    passing = "failed"
    print("You answered: ", t ," correctly, and", n, " incorrectly, you ", passing , " the test.")

