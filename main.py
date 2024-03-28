import random

ROWS = 3
COLS =3

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

symbol_count = {
     "A": 3,
     "B": 6,
     "C": 12,
     "D": 12
}


def slot_spin(rows, cols, symbols):
     all_symbols = []
     for symbols, symbols_count in symbols.items():
          for i in range(symbols_count):
               all_symbols.append(symbols)

     columns = []
     for col in range(cols):
        a_column =[]
        current_symbols = all_symbols[:]
        for row in range(rows):
             value = random.choice(current_symbols)
             current_symbols.remove(value)
             
        columns.append(a_column)

     return columns


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

main()
