import random

def displayMenu():
    print("\nDIFFICULTY LEVEL")
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced")
    level = int(input("Select a difficulty level (1-3): "))
    while level not in [1, 2, 3]:
        level = int(input("Invalid choice. Select a difficulty level (1-3): "))
    return level

def randomInt(difficulty):
    if difficulty == 1:
        return random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    elif difficulty == 3:
        return random.randint(1000, 9999)

def decideOperation():
    return random.choice(['+', '-'])

def displayProblem(num1, num2, operation):
    print(f"{num1} {operation} {num2} = ", end="")
    return int(input())

def isCorrect(user_answer, correct_answer, attempt):
    if user_answer == correct_answer:
        print("Correct!")
        return 10 if attempt == 1 else 5
    else:
        print("Wrong answer. Try again!" if attempt == 1 else "Wrong again.")
        return 0

def displayResults(score):
    print(f"\nYour final score is: {score}/100")
    if score > 90:
        print("Rank: A+")
    elif score > 80:
        print("Rank: A")
    elif score > 70:
        print("Rank: B")
    elif score > 60:
        print("Rank: C")
    else:
        print("Rank: F. Better luck next time!")

def playQuiz():
    level = displayMenu()
    score = 0

    for _ in range(10):
        num1 = randomInt(level)
        num2 = randomInt(level)
        operation = decideOperation()

        
        if operation == '-' and num1 < num2:
            num1, num2 = num2, num1

        correct_answer = eval(f"{num1} {operation} {num2}")
        user_score = 0

        for attempt in range(1, 3):  
            user_answer = displayProblem(num1, num2, operation)
            user_score = isCorrect(user_answer, correct_answer, attempt)
            if user_score > 0:
                break

        score += user_score

    displayResults(score)

def main():
    while True:
        playQuiz()
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
