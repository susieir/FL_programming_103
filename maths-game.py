""" Maths game"""

import matplotlib.pyplot as plt
print("matplotlib imported")

print("Loading high scores")
scores = []
names = []

try:
    with open("highscore.txt", "r") as f:
        for line in f:
            line = line.strip("\n")
            line = line.split(" ")
            names.append(line[0])
            scores.append(int(line[1]))
except FileNotFoundError:
    print("No high scores file found")

print("High scores")
for pos in range(len(names)):
    print(pos + 1, names[pos], scores[pos])

while True:  # Infinite loop
    score = 0

    print("Welcome to the Maths Quiz")


    print("Can you answer three questions and score maximum points?")
    print("\nQuestion 1: What is the product of 2x2x2?")

    answer = int(input("Your answer :>>"))

    if answer == 8:
        print("Correct")
        score = score + 1
        print("Your score is", score)
    else:
        print("Incorrect, the answer is 8")
        print("Your score is", score)

    print("\nQuestion 2: What is the product of 7x7?")

    answer = int(input("Your answer :>>"))

    if answer == 49:
        print("Correct")
        score = score + 1
        print("Your score is", score)
    else:
        print("Incorrect, the answer is 49")
        print("Your score is", score)

    print("\nQuestion 3: What is the sum of 20+91?")

    answer = int(input("Your answer :>>"))

    if answer == 111:
        print("Correct")
        score = score + 1
        print("Your score is", score)
    else:
        print("Incorrect, the answer is 111")
        print("Your score is", score)

    name = input("What's your name? ")
    position = 0
    for compare_score in scores:
        if score < compare_score:
            position = position + 1
    scores.insert(position, score)
    names.insert(position, name)

    scores = scores[:10]
    names = names[:10]
    plt.bar(names, scores)
    plt.title("Maths game high scores")
    plt.ylabel("Score")
    plt.xlabel("Player")
    plt.show()

    print("Saving high scores")
    with open("highscore.txt", "w") as f:
        for pos in range(len(names)):
            f.write(names[pos] + " " + str(scores[pos]) + "\n")

