import random

def load_jokes(file_path):
    jokes = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() and '?' in line:
                    setup, punchline = line.strip().split('?', 1)
                    jokes.append((setup.strip() + '?', punchline.strip()))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    return jokes

def tell_joke(jokes):
    if not jokes:
        print("No jokes to tell!")
        return
    joke = random.choice(jokes)
    print("\n" + joke[0])
    input("Press Enter to see the punchline...")
    print(joke[1])

def main():
    jokes = load_jokes('ADVANCED PROGRAMMING ASSESSMENT/jokes.txt')
    print("Welcome! Type 'alexa tell me a joke' to hear a joke or 'quit' to exit.")

    while True:
        command = input("\nYour command: ").strip().lower()
        if command == "alexa tell me a joke":
            tell_joke(jokes)
        elif command == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Type 'alexa tell me a joke'. Please try again.")

if __name__ == "__main__":
    main()
