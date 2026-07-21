import random
def sort(input_user,input_comp,user,comp):
    status = "Lose"
    if input_user=="rock" and input_comp=="paper":
        print(f"User chooses {input_user}, Computer chooses {input_comp}, Computer wins!")
    elif input_user=="rock" and input_comp=="scissor":
        print(f"User chooses {input_user}, Computer chooses {input_comp}, User wins!")
        status = "Win"
    elif input_user=="paper" and input_comp=="rock":
        print(f"User chooses {input_user}, Computer chooses {input_comp}, User wins!")
        status = "Win"
    elif input_user=="paper" and input_comp=="scissor":
        print(f"User chooses {input_user}, Computer chooses {input_comp}, Computer wins!")
    elif input_user=="scissor" and input_comp=="paper":
        print(f"User chooses {input_user}, Computer chooses {input_comp}, User wins!")
        status = "Win"
    elif input_user=="scissor" and input_comp=="rock":
        print(f"User chooses {input_user}, Computer chooses {input_comp}, Computer wins!")
    elif input_user==input_comp:
        print(f"User chooses {input_user}, Computer chooses {input_comp}, Neither wins")
        status="Draw"
    if status=="Lose":
        return user,comp+1
    elif status=="Win":
        return user+1,comp
    else:
        return user,comp
print("Welcome to playing rock, paper, scissor suit!")
total = int(input("How many games do you wish to play? "))
limit = total
kit = ["rock","paper","scissor"]
comp_choice = random.choice(kit)
user_win = 0
comp_win = 0
while limit>0:
    user_choice = input("What you choose?(rock,paper, scissor)").lower()
    while True:
        if user_choice=="rock" or user_choice=="scissor" or user_choice=="paper":
            break
        else:
            print("Wrong input!")
            user_choice = input("What you chooce?(rock,paper, scissor)").lower()
    user_win,comp_win=sort(user_choice,comp_choice,user_win,comp_win)
    limit-=1
winrate = user_win/total*100
print(f"Your winrate is {winrate}%")
if winrate<=60:
    print("Well, bad luck it is.. Computers are hard to beat!")
elif winrate>60 and winrate<90:
    print("I would consider as a good game, though not enough..")
elif winrate>=90 and winrate<=99:
    print("Bloody hell, that's close son.. Tough game it is..")
else:
    print("No comment on the win...")
