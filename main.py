import random

ROWS = 3
COLS =3

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

machine_symbols = {
     "A": 3,
     "B": 6,
     "C": 12,
     "D": 12
}

symbol_values = {
     "A": 7,
     "B": 5,
}


def winnings(cols, lines, bet, values):
     winnings = 0
     winning_lines = []

     for i in range(lines):
          symbol = cols[0][i]
          for x in cols:
               symbol_to_check = x[i]
               if symbol != symbol_to_check:
                    break
          else:
               winnings += values[symbol] * bet
               winning_lines.append(lines)

     return winnings, winning_lines



def slot_spin(rows, cols, symbols):
     displayed_symbols = []
     for key, values in symbols.items():#for key, value in dictionary
            displayed_symbols.extend(key * values) #A*3, B*6 etc

     columns = [] #store the result of the spin
     for _ in range(cols): # '_' means anonymous variable
        a_column =[]
        current_symbols = displayed_symbols[:] #this makes a copy for displayed_symbol for this column
        for _ in range(rows): #loop to generate rows for each column
             value = random.choice(current_symbols)
             current_symbols.remove(value) #remove the random value from current symbols
             a_column.append(value)
             
        columns.append(a_column)

     return columns




def print_slot_result(columns):
     for row in range(len(columns[0])):
        for i, column in enumerate(columns):
             if i != len(columns) - 1:
                  print(column[row], end= "|") #pip operator space in between
             else:
                print(column[row], end='')
        print()



def deposit():
    while True:
        amount = input("What would you like to deposit?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount mus be greater than 0")
        else:
            print("Please enter a number")
    return amount



def number_of_lines():
        while True:
                lines = input("Enter amount of lines to bet on (1-" + str(MAX_LINES)+ ")")
                if lines.isdigit():
                    lines = int(lines)
                    if 1 <= lines <= MAX_LINES:
                        break
                    else:
                        print("Enter a valid number of lines")
                else:
                    print("Please enter a number")
        return lines


def get_bet():
     while True:
                your_bet = input("Enter your bet amount $ for each line")
                if your_bet.isdigit():
                    your_bet = int(your_bet)
                    if MIN_BET <= your_bet <= MAX_BET:
                        break
                    else:
                        print(f"Amount must be between {MIN_BET} - {MAX_BET}")
                else:
                    print("Please enter a number")
     return your_bet



def main():
    balance = deposit()
    lines = number_of_lines()
    while True:
       bet = get_bet()
       total_bet = bet * lines  

       if total_bet > balance:
            print(f'insufficient funds, your deposit ${balance}, your total bet ${total_bet}')
       else:
            break
    
    print(f'Balance ${balance} lines {lines} Bet Amount per line ${bet} Total Bet ${total_bet}')

    slots = slot_spin(ROWS, COLS, machine_symbols)
    print_slot_result(slots)

    winnings, winning_lines = winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    print(f"You won on lines", *winning_lines) #*splat operator

main()
