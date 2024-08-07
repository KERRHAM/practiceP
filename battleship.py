introduction =  """
    Welcome Sailer, your task is to sink the enemys 3 Battleship's in under 20 shots, 
    To exit the game enter quit to terminal.
    """
print(introduction)
start = input("Are you ready to set sail and attack? ").lower()

if start == "no":
    quit()

boat1 = [25, 35, 45]
boat2 = [1, 2, 3]
boat3 = [99, 89, 79]

hit = []
miss = []
comp = []


def show_board(hit,miss,comp):  
    

    print("           Battleship!!!")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for j in range(10):
            ch = " _ "
            if place in hit:
                ch = " o "
            elif place in miss:
                ch = " x "
            elif place in comp:
                ch = " O "
            row = row + ch
            place = place + 1
        print(x," ", row)

def start_game(strike_attempts):

    while True:
      strike = input(f"Please enter your Guess coordinates!!! ")
      strike = int(strike)
      if strike < 0 or strike > 99:
        print("Please enter a number between 0 and 99!!")
      elif strike in strike_attempts:
        print("You've already entered this coordinate, please try again!!!")
      else:
        break
    return strike

def check_strike(strike, boat1, boat2, hit, miss, comp):
    
    if strike in boat1:
        boat1.remove(strike)
        if len(boat1) > 0:
            hit.append(strike)
            print("Hit!!")
        else:
            comp.append(strike)
    elif strike in boat2:
        boat2.remove(strike)
        if len(boat2) > 0:
            hit.append(strike)
            print("Hit!!")
        else:
            comp.append(strike)
    else:
       miss.append(strike)
       print("Miss!!!")
    
    return boat1, boat2, hit, miss, comp

for i in range(10):
    strike_attempts = hit + miss + comp
    strike = start_game(strike_attempts)
    check_strike(strike, boat1, boat2, hit, miss, comp)
    show_board(hit, miss, comp)

    if len(boat1) < 1:
        print("1 down 1 to go!!")

    if len(boat2) < 1:
        print("Well done, you sunk my battleship's!!!")
        print("Click Run to play again.")
        break


print(f"Hit's {hit_Counter}")
print(f"Misses {miss_Counter}")