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

hit = [21, 22]
miss = [20, 24, 25]
comp = [23]

def start_game():

    while True:
      strike = input(f"Please enter your Guess coordinates!!! ")
      strike = int(strike)
      if strike < 0 or strike > 99:
        print("Please enter a number between 0 and 99!!")
      else:
        break
    return strike

start_game()
show_board(hit, miss, comp)