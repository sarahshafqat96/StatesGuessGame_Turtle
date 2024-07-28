# Introduction

This project is an interactive game where users guess the names of US states. If guessed correctly, the name is displayed on the map at its respective coordinates. The game uses Python's Turtle 
module to mark correctly guessed states on the map ("US_states_img.gif") and pandas to handle the state data. 
The states name and co-ordinates are provided in the "50_states.csv" file

# Features
- Interactive map of the US with state outlines.
- User prompted to guess state names.
- Correct guesses are marked on the map using coordinates from a CSV file.
- Game continues until the user types "Exit" or guesses all 50 states.
- Export guessed and unguessed states to separate CSV files upon exiting.

# Usage
1. Download all the files in the same directory and run the main script to start the game:
```
python main.py
```
3. Follow the on-screen prompts to:
- Guess the name of a US state.
- See the state name marked on the map if guessed correctly.
- Continue guessing until all states are guessed or type "Exit" to finish.

4. After exiting the game, two CSV files will be created:
- Guessed_states.csv: Contains the names of the states you guessed correctly.
- Missed_states.csv: Contains the names of the states you did not guess.
