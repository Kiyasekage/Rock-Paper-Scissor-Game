# Rock, Paper, Scissors Game

## Overview

The Rock, Paper, Scissors Game is an interactive Python application where users play against the computer in a series of matches. The program utilizes randomization, input validation, functions, loops, and score tracking to create an engaging command-line gaming experience.

## Features

* Play multiple rounds against the computer.
* Supports the classic choices:

  * Rock
  * Paper
  * Scissors
* Validates user input.
* Tracks player and computer wins.
* Calculates the player's overall win rate.
* Displays a customized message based on performance.

## Technologies Used

* Python 3
* `random` module

## Project Structure

```text
Rock-Paper-Scissors/
│
├── rock_paper_scissors.py
└── README.md
```

## How to Run

1. Ensure Python 3 is installed.
2. Save the program as `rock_paper_scissors.py`.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python rock_paper_scissors.py
```

## Example

### Input

```text
Welcome to playing rock, paper, scissor suit!
How many games do you wish to play? 3

What you choose? (rock, paper, scissor) rock
What you choose? (rock, paper, scissor) paper
What you choose? (rock, paper, scissor) scissor
```

### Output

```text
User chooses rock, Computer chooses paper, Computer wins!
User chooses paper, Computer chooses paper, Neither wins
User chooses scissor, Computer chooses paper, User wins!

Your winrate is 33.33%
Well, bad luck it is.. Computers are hard to beat!
```

## How It Works

1. The program asks the user how many rounds they want to play.
2. It initializes:

   * A list of possible choices (`rock`, `paper`, `scissor`)
   * Player score
   * Computer score
3. The computer randomly selects an option.
4. For each round:

   * The user enters their choice.
   * The program validates the input.
   * The `sort()` function determines the winner.
   * Scores are updated accordingly.
5. After all rounds are completed:

   * The player's win rate is calculated.
   * A final message is displayed based on the player's performance.

## Game Rules

| Player      | Computer    | Result |
| ----------- | ----------- | ------ |
| Rock        | Scissor     | Win    |
| Rock        | Paper       | Lose   |
| Paper       | Rock        | Win    |
| Paper       | Scissor     | Lose   |
| Scissor     | Paper       | Win    |
| Scissor     | Rock        | Lose   |
| Same Choice | Same Choice | Draw   |

## Concepts Demonstrated

* Functions
* Loops (`while`)
* Conditional statements
* Input validation
* Random number generation
* Lists
* Multiple return values
* Score tracking
* Basic game development

## Known Issue

The computer's choice is currently generated only once:

```python
comp_choice = random.choice(kit)
```

This means the computer uses the same choice for every round, which is likely unintended.

A better implementation would generate a new choice during each iteration of the game loop:

```python
while limit > 0:
    comp_choice = random.choice(kit)
    user_choice = input(...)
```

This ensures that the computer makes an independent random decision for every round, making the game fairer and more realistic.

## Future Improvements

* Generate a new computer choice each round.
* Add a replay option after the game ends.
* Track draws separately.
* Implement a best-of-three or tournament mode.
* Create a graphical user interface (GUI).
* Add sound effects and animations.
* Store player statistics in a file.

## Author

Created as a Python practice project to demonstrate functions, loops, input validation, score tracking, and simple game development using Python.
