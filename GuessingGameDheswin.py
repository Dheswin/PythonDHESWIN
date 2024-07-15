import random

# List of games and their corresponding clues
games_clues = {
    "Minecraft": [
        "Clue: This game involves breaking and placing blocks in a 3D procedurally generated world.",
        "Clue: Players can build structures and explore different biomes ranging from forests to deserts.",
        "Clue: It has a survival mode where you need to gather resources, craft tools, and fend off monsters like zombies and creepers."
    ],
    "Fortnite": [
        "Clue: This is a battle royale game where 100 players fight to be the last one standing.",
        "Clue: It features unique building mechanics that allow players to construct walls, ramps, and forts during combat.",
        "Clue: Players are dropped onto an island and must scavenge for weapons, resources, and eliminate others to win."
    ],
    "Among Us": [
        "Clue: This game involves Crewmates who complete tasks and Impostors who try to sabotage them.",
        "Clue: Crewmates must work together to complete tasks around the map, while Impostors aim to kill them.",
        "Clue: It became extremely popular during the COVID-19 pandemic, with its simple yet engaging social deduction gameplay."
    ],
    "The Witcher 3": [
        "Clue: This RPG features a monster hunter named Geralt of Rivia, who is searching for his adopted daughter.",
        "Clue: It's set in a richly detailed fantasy world full of quests, monsters, and political intrigue.",
        "Clue: Players can take on various quests, make moral decisions, and fight supernatural beings with swords and magic."
    ],
    "Overwatch": [
        "Clue: This is a team-based multiplayer first-person shooter with a diverse cast of heroes.",
        "Clue: Each character has unique abilities and roles, such as tank, damage, and support.",
        "Clue: It's developed by Blizzard Entertainment and emphasizes teamwork and strategy."
    ],
    "League of Legends": [
        "Clue: This is a multiplayer online battle arena (MOBA) game where two teams of five players compete.",
        "Clue: Players control a 'champion' with unique abilities and must work together to destroy the opposing team's Nexus.",
        "Clue: It is one of the most popular eSports games, with a large competitive scene and regular updates."
    ],
    "Cyberpunk 2077": [
        "Clue: This game is set in a dystopian future in the open world of Night City.",
        "Clue: Players control a customizable character named V, who can acquire cybernetic implants and skills.",
        "Clue: It's developed by CD Projekt Red, known for its complex storylines and detailed world-building."
    ],
    "Call of Duty: Modern Warfare": [
        "Clue: This is a first-person shooter game that is part of a popular franchise.",
        "Clue: It features a campaign mode with special forces missions, as well as multiplayer and cooperative modes.",
        "Clue: The game includes realistic graphics, tactical gameplay, and a variety of modern military weapons."
    ],
    "Half-Life 2": [
        "Clue: This is a first-person shooter developed by Valve, where players control a scientist named Gordon Freeman.",
        "Clue: The game is known for its physics-based puzzles, storytelling, and detailed environments.",
        "Clue: Players must fight against an alien invasion and human collaborators using a variety of weapons and tools."
    ],
    "Elden Ring": [
        "Clue: This is an action RPG developed by FromSoftware, featuring a large open world with horseback combat.",
        "Clue: The game is directed by Hidetaka Miyazaki, known for the Dark Souls series, in collaboration with George R. R. Martin.",
        "Clue: Players explore a dark fantasy world, battling formidable enemies and uncovering deep lore."
    ]
}

# Initialize variables
score = 0
total_questions = 5
questions_asked = 0
full_marks = 100
points_per_question = 20

# List of games to choose from
games_list = list(games_clues.keys())

# Function to ask a question
def ask_question(game, clues):
    global score, questions_asked
    options = random.sample(games_list, 3)
    if game not in options:
        options[random.randint(0, 2)] = game
    random.shuffle(options)

    for clue in clues:
        print(clue)
        print("Options:")
        for idx, option in enumerate(options):
            print(f"{chr(65 + idx)}. {option}")
        
        guess = input("Guess the game (A, B, C, or D): ").strip().upper()
        if guess in ['A', 'B', 'C', 'D']:
            selected_option = options[ord(guess) - 65]
            if selected_option.lower() == game.lower():
                print("Correct! Well done!")
                score += points_per_question
                break
            else:
                print("Incorrect, try again.")
                show_clue = input("Do you want to see another clue? (yes/no): ").strip().lower()
                if show_clue != 'yes':
                    break
        else:
            print("Invalid option. Please choose A, B, C, or D.")
    questions_asked += 1
    print(f"Your current score: {score} out of {full_marks}\n")

# Main game loop
random.shuffle(games_list)
for i in range(total_questions):
    game = games_list.pop()
    clues = games_clues[game]
    print(f"Question {i + 1}:")
    ask_question(game, clues)

# Final score and retry logic
if score == full_marks:
    print(f"Congratulations! You got a perfect score of {score} out of {full_marks}!")
else:
    print(f"Game over! Your final score is {score} out of {full_marks}.")
    retry = input("Do you want to retry? (yes/no): ").strip().lower()
    if retry == 'yes':
        # Reset variables and reshuffle games
        score = 0
        questions_asked = 0
        games_list = list(games_clues.keys())
        random.shuffle(games_list)
        for i in range(total_questions):
            game = games_list.pop()
            clues = games_clues[game]
            print(f"Question {i + 1}:")
            ask_question(game, clues)
        if score == full_marks:
            print(f"Congratulations! You got a perfect score of {score} out of {full_marks}!")
        else:
            print(f"Game over! Your final score is {score} out of {full_marks}.")
    else:
        print("Thank you for playing!")
