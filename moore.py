import os

# Global variables for states, input symbols, and output symbols
states = []
input_symbols = ["a", "b"]
output_symbols = [0, 1]

def clear_screen():
    """Clear the terminal screen for better UX."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_moore_machine(num_states):
    """
    Interactively create the Moore machine's transition and output tables.
    Returns a list of lists representing the machine.
    """
    states.clear()
    # Each row: [state, next_state_a, next_state_b, output]
    transition_output_table = [[0 for _ in range(4)] for _ in range(num_states)]
    for i in range(num_states):
        state_name = f"q{i}"
        states.append(state_name)
    for i in range(num_states):
        col_index = 0
        transition_output_table[i][col_index] = states[i]
        # Get transitions for each input symbol
        for symbol in input_symbols:
            clear_screen()
            while True:
                if i != 0:
                    print_transition_table(transition_output_table, input_symbols, i)
                print(f"\nTransition for state {states[i]}")
                for idx, s in enumerate(states, start=1):
                    print(f"{idx} - {states[i]} >> {s}")
                try:
                    transition = int(input(f"\nNext state for input '{symbol}': "))
                    if 1 <= transition <= len(states):
                        col_index += 1
                        transition_output_table[i][col_index] = states[transition - 1]
                        break
                    else:
                        input("Invalid value. Press Enter to retry.")
                        clear_screen()
                except ValueError:
                    input("Invalid input. Press Enter to retry.")
                    clear_screen()
                    continue
        # Get output for the state
        col_index += 1
        while True:
            try:
                clear_screen()
                if i != 0:
                    print_transition_table(transition_output_table, input_symbols, i)
                output_value = int(input(f"Output value for state {states[i]}: "))
                if output_value in output_symbols:
                    transition_output_table[i][col_index] = output_value
                    break
                else:
                    print(f"Please enter one of {output_symbols}")
            except ValueError:
                continue
        print_transition_table(transition_output_table, input_symbols, i + 1)
    return transition_output_table

def print_transition_table(table, input_symbols, num_states):
    """
    Print the transition and output table in a formatted way.
    """
    clear_screen()
    print("_________________________________________________________________________")
    print("|                  Transition Table                  |   Output Table    |")
    print("|____________________________________________________|___________________|")
    print("| Old State |", end="    ")
    for symbol in input_symbols:
        print(f"After input {symbol}", end="    ")
    print("| Character printed |")
    print("|-----------|----------------------------------------|-------------------|")
    for i in range(num_states):
        print("|", end="    ")
        for j in range(4):
            if j == 0:
                print(table[i][j], end="     |          ")
            elif j == 1:
                print(table[i][j], end="                ")
            elif j == 2:
                print(table[i][j], end="          ")
            else:
                print(f"|        {table[i][j]}        |")
    print("|___________|________________________________________|___________________|")

def simulate_moore_machine(input_string, transition_output_table, num_states):
    """
    Simulate the Moore machine for a given input string and print the state and output trace.
    """
    input_length = len(input_string)
    current_state = "q0"
    state_trace = [current_state]
    output_trace = [0]
    # For each input character, find the next state and output
    for i in range(input_length):
        found = False
        for j, symbol in enumerate(input_symbols):
            if input_string[i] == symbol:
                next_state_index = j + 1
                for k in range(num_states):
                    if transition_output_table[k][0] == current_state:
                        current_state = transition_output_table[k][next_state_index]
                        state_trace.append(current_state)
                        # Find output for the new state
                        for l in range(num_states):
                            if transition_output_table[l][0] == current_state:
                                output_trace.append(transition_output_table[l][3])
                                break
                        found = True
                        break
            if found:
                break
    # Print the simulation result in a tabular format
    print("____________________", end="")
    for i in range(input_length):
        if input_string[i] in input_symbols:
            print("___", end="")
    print("\n|Input String  |    ", end="")
    for i in range(input_length):
        if input_string[i] in input_symbols:
            print(input_string[i], end="  ")
    print("|\n|State         |", end=" ")
    for state in state_trace:
        print(state, end=" ")
    print("|\n|Output        | ", end="")
    for out in output_trace:
        print(out, end="  ")
    print("|\n|______________|____", end="")
    for i in range(input_length):
        if input_string[i] in input_symbols:
            print("___", end="")
    print("|")

def main():
    """
    Main loop for the Moore machine simulator CLI.
    """
    clear_screen()
    while True:
        clear_screen()
        print("1. Moore Machine Simulator")
        print("0. Exit")
        try:
            choice = int(input("\nSelect an option: "))
            if choice == 0:
                clear_screen()
                input("Program terminated. Press Enter to exit.")
                break
            elif choice == 1:
                clear_screen()
                num_states = int(input("Enter the number of states: "))
                transition_table = create_moore_machine(num_states)
                input_str = input("\nInput string: ")
                simulate_moore_machine(input_str, transition_table, num_states)
                input("\n\nPress Enter to return to main menu.")
            else:
                clear_screen()
                print("Invalid selection.")
                input("\n\nPress Enter to return to main menu.")
        except ValueError:
            clear_screen()
            print("Invalid selection.")
            input("\n\nPress Enter to return to main menu.")
            continue

if __name__ == "__main__":
    main()