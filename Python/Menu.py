import subprocess
import sys
import os

# Make sure this matches exactly your file names
games = {
    "1": ("Number Guessing Game", "Number_Guessing_Game.py"),
    "2": ("Tic-Tac-Toe Game",  "Tic_Tac_Toe_Game.py"),
    "3": ("Wordle Game",        "Wordle_Game.py"),
    "0": ("Quit",               None)
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== Game Menu ===")
    for key in sorted(games.keys()):
        print(f"{key}) {games[key][0]}")
    choice = input("Select a game → ").strip()
    return choice

def run_game(filename):
    # Ensure path is correct: same folder as Menu.py
    path = os.path.join(os.path.dirname(__file__), filename)
    # Check if file exists
    if not os.path.isfile(path):
        print(f"Error: File not found → {path}")
        input("Press Enter to continue…")
        return
    # Run the game file with the same Python interpreter
    subprocess.run([sys.executable, path])
    input("\nPress Enter to return to menu…")

def main():
    while True:
        choice = show_menu()
        if choice in games:
            desc, filename = games[choice]
            if filename is None:
                print("Goodbye!")
                break
            else:
                print(f"Launching {desc} …")
                run_game(filename)
        else:
            print("Invalid selection; try again.")
            input("Press Enter to continue…")

if __name__ == "__main__":
    main()
