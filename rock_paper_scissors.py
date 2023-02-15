import random

ran_num = random.randint(0,2)
player = input("enter your choice ")

if ran_num == 0:
    computer = "rock"
elif ran_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"computer says {computer}" )

if player == computer:
    print("Draw")
elif player == "rock" and computer == "paper":
    print("computer wins!")
elif player == "rock" and computer == "scissors":
    print("player wins!")
elif player == "paper" and computer == "rock":
    print("player wins!")
elif player == "paper" and computer == " scissors":
    print("computer wins!")
elif player == "scissors" and computer == "rock":
    print("computer wins!")
elif player == "scissors" and computer == "paper":
    print("player wins!")
else:
    print("invalid choice")