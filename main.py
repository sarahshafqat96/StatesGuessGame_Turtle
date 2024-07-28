from turtle import Turtle, Screen
import pandas

#Setting up the screen
screen = Screen()
screen.setup(730, 500)
screen.bgpic("blank_states_img.gif")

#Creating a turtle object
map_turtle = Turtle()
map_turtle.penup()
map_turtle.hideturtle()

data_df = pandas.read_csv("50_states.csv")                                                   #Read data from a csv file
original_states = data_df["state"].tolist()                                                  #Convert the data's columns into lists and store in respective variables
x_coordinates = data_df["x"].tolist()
y_coordinates = data_df["y"].tolist()

guessed_state_list = []                                                                      #Creating empty lists
missed_state_list = []

user_input = screen.textinput("State_Name", "Please guess a state").title()      #User input
while user_input != "Exit" or len(guessed_state_list) == 50:                                 #Unless user types "exit" or he has guessed all 50 states
    if user_input in original_states and user_input not in guessed_state_list:               #If user has guessed a new state correctly
        guessed_state_list.append(user_input)                                                #Append that state in the list
        index = original_states.index(user_input)                                            #Extract its index
        x_cord = x_coordinates[index]                                                        #Use the index to extract its x co-ordinate
        y_cord = y_coordinates[index]                                                        #Use the index to extract its y co-ordinate
        map_turtle.teleport(x_cord, y_cord)                                                  #Send the turtle to those co-ordinates
        map_turtle.write(user_input)                                                         #Turtle will write the state at those co-ordinates
    user_input = screen.textinput("State_Name", "Please guess a state").title()              #Ask the user for their next input

if len(guessed_state_list) < 51:                                                             #If user has not guessed 50 states
    missed_state_list = [m for m in original_states if m not in guessed_state_list]          #Then append the ones not guessed in missed_state_list
else:
    missed_state_list = "YOU GUESSED EVERYTHING PERFECTLY"                                   #Otherwise store this string in the list

user_guess_df = pandas.DataFrame(guessed_state_list, columns=["Guessed_States"])             #Convert the lists into pandas dataframes
user_miss_df = pandas.DataFrame(missed_state_list, columns=["Missed_States"])

user_guess_df.to_csv('Guessed_States.csv', index=False)                                      #Output them to separate csv files.
user_miss_df.to_csv('Missed_States.csv', index=False)
