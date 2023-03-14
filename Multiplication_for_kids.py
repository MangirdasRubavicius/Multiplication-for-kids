from random import randint
t=0
n=0
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
            print("Correct.")
            t=t+1
        else:
            print("Incorrect.")
            n=n+1
    print("You answered: ", t ," correctly, and", n, " incorrectly")

