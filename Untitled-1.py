# Two-player Ramayana quiz game

questions = [
    {
        "question": "Who is the father of Lord Rama?",
        "options": ["Dasharatha", "Bharata", "Lakshmana", "Hanuman"],
        "answer": 1
    },
    {
        "question": "What is the name of Lord Rama's wife?",
        "options": ["Sita", "Draupadi", "Radha", "Kunti"],
        "answer": 1
    },
    {
        "question": "Who helped Lord Rama build the bridge to Lanka?",
        "options": ["Hanuman", "Sugriva", "Vibhishana", "Nala"],
        "answer": 4
    }
]

def ask_question(player, question_data):
    print(f"\n{player}, it's your turn!")
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], 1):
        print(f"{i}. {option}")
    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))
            if 1 <= answer <= 4:
                return answer == question_data["answer"]
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def main():
    print("Welcome to the Ramayana Quiz!")
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")

    scores = {player1: 0, player2: 0}
    players = [player1, player2]

    for i, question in enumerate(questions):
        current_player = players[i % 2]
        if ask_question(current_player, question):
            print("Correct!")
            scores[current_player] += 1
        else:
            print("Wrong answer!")

    print("\nFinal Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

    winner = max(scores, key=scores.get)
    print(f"\nCongratulations {winner}! You are the winner!")

if __name__ == "__main__":
    main()
    # Determine if there's a tie
    max_score = max(scores.values())
    winners = [player for player, score in scores.items() if score == max_score]

    if len(winners) > 1:
        print("\nIt's a tie between: " + " and ".join(winners) + "!")
    else:
        print(f"\nCongratulations {winners[0]}! You are the winner!")