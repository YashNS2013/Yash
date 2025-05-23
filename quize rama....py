import random

def load_questions():
    questions = [
        {"question": "Who is the father of Lord Rama?", "answer": "Dasharatha"},
        {"question": "What is the name of Lord Rama's wife?", "answer": "Sita"},
        {"question": "Who is Lord Rama's loyal devotee and companion?", "answer": "Hanuman"},
        {"question": "What is the name of Lord Rama's kingdom?", "answer": "Ayodhya"},
        {"question": "Who is the demon king of Lanka defeated by Lord Rama?", "answer": "Ravana"},
        {"question": "What is the name of Lord Rama's brother who accompanied him to the forest?", "answer": "Lakshmana"},
        {"question": "Who wrote the Ramayana?", "answer": "Valmiki"},
        {"question": "What is the name of the forest where Lord Rama spent his exile?", "answer": "Dandaka"},
        {"question": "Who helped Lord Rama build the bridge to Lanka?", "answer": "Vanaras"},
        {"question": "What is the name of the bird who tried to save Sita from Ravana?", "answer": "Jatayu"}
    ]
    return questions

def ask_question(player, question):
    print(f"{player}, {question['question']}")
    answer = input("Your answer: ")
    return answer.strip().lower() == question['answer'].lower()

def quiz_game():
    print("Welcome to the Two-Player Ramayana Quiz Game!")
    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")

    questions = load_questions()
    random.shuffle(questions)

    player1_points = 0
    player2_points = 0

    for i in range(len(questions)):
        current_player = player1 if i % 2 == 0 else player2
        if ask_question(current_player, questions[i]):
            print("Correct!")
            if current_player == player1:
                player1_points += 1
            else:
                player2_points += 1
        else:
            print("Wrong!")

    print("\nGame Over!")
    print(f"{player1}'s Points: {player1_points}")
    print(f"{player2}'s Points: {player2_points}")

    if player1_points > player2_points:
        print(f"{player1} wins!")
    elif player2_points > player1_points:
        print(f"{player2} wins!")
        print("Better luck next time, Player 1!")
    else:
        print("It's a tie!")
        def ask_question_with_options(player, question, options):
            print(f"{player}, {question['question']}")
            for idx, option in enumerate(options, start=1):
                print(f"{idx}. {option}")
            try:
                choice = int(input("Choose the correct option (1-4): "))
                if 1 <= choice <= 4:
                    return options[choice - 1].strip().lower() == question['answer'].lower()
                else:
                    print("Invalid choice. Moving to the next question.")
                    return False
            except ValueError:
                print("Invalid input. Moving to the next question.")
                return False
        
        def quiz_game_with_options():
            print("Welcome to the Two-Player Ramayana Quiz Game with Options!")
            player1 = input("Enter Player 1 name: ")
            player2 = input("Enter Player 2 name: ")
        
            questions = load_questions()
            random.shuffle(questions)
        
            player1_points = 0
            player2_points = 0
        
            for i in range(len(questions)):
                current_player = player1 if i % 2 == 0 else player2
                options = random.sample([q['answer'] for q in questions if q != questions[i]], 3)
                options.append(questions[i]['answer'])
                random.shuffle(options)
                if ask_question_with_options(current_player, questions[i], options):
                    print("Correct!")
                    if current_player == player1:
                        player1_points += 1
                    else:
                        player2_points += 1
                else:
                    print("Wrong!")
        
            print("\nGame Over!")
            print(f"{player1}'s Points: {player1_points}")
            print(f"{player2}'s Points: {player2_points}")
        
            if player1_points > player2_points:
                print(f"{player1} wins!")
            elif player2_points > player1_points:
                print(f"{player2} wins!")
                print("Better luck next time, Player 1!")
            else:
                print("It's a tie!")

if __name__ == "__main__":
    quiz_game_with_options()  # Call the quiz game with options function
if __name__ == "__main__":
    quiz_game()  # Call the main quiz game function
    