import random

MAX_LINES = 3  # Maximum number of lines to bet on
MAX_BET = 100  # Maximum amount to bet per line
MIN_BET = 1  # Minimum amount to bet per line

rows = 3  # Number of rows in the slot machine
cols = 3  # Number of columns in the slot machine

symbol_count = {
    "A": 2,  # Number of occurrences of symbol A in the slot machine
    "B": 4,  # Number of occurrences of symbol B in the slot machine
    "C": 6,  # Number of occurrences of symbol C in the slot machine
    "D": 8   # Number of occurrences of symbol D in the slot machine
}

symbol_value = {
    "A": 50,
    "B": 20,
    "C": 10,
    "D": 5,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

# Function to get a random spin of the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


# Function to print the slot machine spin
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end=" ")
            else:
                print(column[row])

# Function to prompt the user for the deposit amount
def deposit():
    while True:
        amount = input("What would you like to deposit $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount

# Function to prompt the user for the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines

# Function to prompt the user for the bet amount per line
def get_bet():
    while True:
        bet = input(f"What would you like to bet for each line (${MIN_BET}-{MAX_BET}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a number")
    return bet

# Main function to run the game
def main():
    balance = deposit()  # Prompt the user for the deposit amount
    lines = get_number_of_lines()  # Prompt the user for the number of lines to bet on

    while True:
        bet = get_bet()  # Prompt the user for the bet amount per line
        total_bet = bet * lines  # Calculate the total bet amount

        if total_bet > balance:
            print(f"You do not have enough money to bet that amount. Your current balance is: ${balance}")
        else:
            print(f"You are betting ${bet} on {lines} line(s). Total bet is equal to ${total_bet}.")
            break

    slots = get_slot_machine_spin(rows, cols, symbol_count)  # Get the slot machine spin
    print_slot_machine(slots)  # Print the slot machine spin

    def main():
    
     balance = deposit()
    play_game = input("Press 'q' to start the game or 'x' to exit: ")
    
    if play_game.lower() != "q":
        return
    
    while True:
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough money to bet that amount. Your current balance is: ${balance}")
            break
            
        print(f"You are betting ${bet} on {lines} line(s). Total bet is equal to ${total_bet}.")
        slots = get_slot_machine_spin(rows, cols, symbol_count)
        print_slot_machine(slots)
    
        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        if winning_lines:
            print("Congratulations! You won on line(s):", ", ".join(str(line) for line in winning_lines))
            print(f"YOU WON ${winnings}")
            balance += winnings - total_bet
        else:
            print("Better luck next time!")
            print(f"You lost ${total_bet}")
            balance -= total_bet
            
        print(f"Your current balance is: ${balance}")
            
        if balance == 0:
            print("You ran out of balance.")
            break
            
        play_again = input("Press 'x' to exit the game or any other key to play again: ")
        if play_again.lower() == "x":
            break

    print(f"Thank you for playing! You are left with ${balance}")

main()


  



          
