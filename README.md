Number Guessing Game
Welcome to the Number Guessing Game! This game challenges players to guess a randomly generated number within a specific range and offers various helpful hints to make the guessing process more engaging.

Features

Multiple Levels: Choose from three difficulty levels:
Level 1: The number is between 1 and 10.
Level 2: The number is between 1 and 100.
Level 3: The number is between 1 and 1000.
Hints: If you guess incorrectly, a random hint is provided:

Too Low / Too High: Indicates whether your guess was lower or higher than the target.
Steps Away: Tells you how far your guess is from the target number.
Highest Common Factor (HCF): Shows the greatest common divisor of your guess and the target number.
Least Common Multiple (LCM): Displays the least common multiple of your guess and the target number.
Scoring: You start with a score of 100, and each incorrect guess reduces your score by 10 points.

Win/Lose Conditions:

You win by guessing the correct number.
You lose if your score reaches 0 before guessing correctly.
How to Play
Run the script in your Python environment.
Select the difficulty level:
Level 1 for easy (1 to 10)
Level 2 for medium (1 to 100)
Level 3 for hard (1 to 1000)
Start guessing the number.
Pay attention to the hints after each incorrect guess.
Keep guessing until you either find the correct number or your score drops to zero.

Example Gameplay
Choose level:
LEVEL 1
LEVEL 2
LEVEL 3
Level no.: 1
The number is in the range 1 to 10
Enter the number: 5
Too high
5 steps away
Enter the number: 3
CORRECT!
YOU WIN!
score: 90

Dependencies
Python 3.x
random module (comes built-in with Python)


How to Run

Clone this repository:
git clone https://github.com/yourusername/number-guessing-game.git

Navigate to the project directory:
cd number-guessing-game

Run the game:
python number_guessing_game.py

Future Improvements
Add a graphical user interface (GUI) for better user interaction.
Implement multiplayer mode.
Introduce a timer to make the game more challenging.
