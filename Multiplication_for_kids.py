from random import randint

t = 0
n = 0
if __name__ == "__main__":
    for i in range(10):
        number_1 = randint(1, 10)
        number_2 = randint(1, 10)
        number_3 = number_1 * number_2
        print(number_1, "*", number_2, "=")
        answer = int(input("What is the answer? : "))

        if answer == number_3:
            t = t + 1
            print("Correct!")
        else:
            n = n + 1
            print("Wrong. The correct answer is :", number_3)

if t >= 7:
    passing = "passed"
else:
    passing = "failed"
print("You answered: ", t, " correctly, and", n, " incorrectly, you ", passing, " the test.")
