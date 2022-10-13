import random as r

BallReplies = {
    1: "It is certain",
    2: "It is decidedly so",
    3: "Without a doubt",
    4: "Yes, definitely",
    5: "You may rely on it",
    6: "As I see it, yes",
    7: "Most likely",
    8: "Outlook good"
}

print("Welcome to the 8-Ball, what would you like to ask?")
Quesion = input()
print(BallReplies[r.randint(1,8)])