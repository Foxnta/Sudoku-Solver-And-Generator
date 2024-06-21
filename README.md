# 🧩 Sudoku Game

## 🚀 Project Overview

This project generates and solves Sudoku puzzles with varying levels of difficulty. Users can request hints and verify the validity of their current Sudoku puzzle while solving it.

## 🌟 Features

1. **Sudoku Generation:**
   - Easy level: 40 numbers.
   - Medium level: 30 numbers.
   - Hard level: 15 numbers.
   - Generates a different Sudoku puzzle each time upon user request.

2. **User Assistance:**
   - Users can request hints to progress in the Sudoku puzzle.
   - Validates the current state of the Sudoku puzzle.
   - Identifies invalid Sudoku puzzles.

## 📋 How to Play

1. **Main Menu:**
   - `1. New Game`: Generates a new Sudoku puzzle.
   - `2. Load Sudoku`: Allows the user to input an existing Sudoku puzzle.
   - `3. End Game`: Ends the game.

2. **New Game:**
   - Select difficulty level:
     - `1. Easy`
     - `2. Medium`
     - `3. Hard`
   - During the game:
     - `1. Request Hint`: Receive a valid hint.
     - `2. View Solution`: Display the full solution.
     - `3. Return to Main Menu`: Go back to the main menu.
     - `4. End Game`: Ends the game.

3. **Load Sudoku:**
   - Users input the current state of their Sudoku puzzle.
   - During the game:
     - `1. Request Hint`: Receive a valid hint.
     - `2. View Solution`: Display the full solution.
     - `3. Return to Main Menu`: Go back to the main menu.
     - `4. End Game`: Ends the game.

## 💡 Algorithm Used

The project uses a **Backtracking Algorithm** to generate and solve Sudoku puzzles. The backtracking approach ensures that the puzzles are valid and can be solved step-by-step by filling in numbers and checking for validity recursively.

### How It Works:
1. **Sudoku Generation:**
   - Uses the backtracking algorithm to fill a 9x9 grid with numbers ensuring that each number follows Sudoku rules.
   - Randomly removes numbers from the filled grid based on the selected difficulty level.

2. **Sudoku Solving:**
   - Validates the current state of the Sudoku puzzle.
   - Provides hints by filling in one of the empty cells with a correct number from the solution.

## 🛠️ Technologies Used
- Python 🐍

Enjoy playing Sudoku! 🧩😊
